"""Day 114 pieri hunt V4 -- BREAKTHROUGH.

From V3 (correcting my earlier indexing error):
    For p >= 1, even j = 2k, m = 2i:
        seed(A_p, j=2k, m=2i) = R_p(k, i) * T(2k, k-i)
    where T(n, r) = binom(n, r) - binom(n, r-1) is the Catalan triangle,
    and R_p(k, i) is a polynomial in i of degree p for fixed k.

    For p = 1: R_1(k, i) = -k(2k-3) (independent of i, degree 0).
    For p = 2: R_2(k, i) = A(k) + i(i+1)  with A(k) = -7, 13, 134, 480 for k=2..5.

So R_p(k, i) is a POLYNOMIAL IN i OF DEGREE p (or p-1?) whose leading coeff
and lower terms depend on k.

Plan for V4:
 (1) For each (p, k), fit R_p(k, i) as polynomial in i. Check that degree = p (or p-1).
 (2) For each fixed degree-d coefficient of R_p(k, i), fit it as polynomial in k.
 (3) Write R_p(k, i) as a bivariate polynomial (k, i) and see if it factors.
 (4) Do the same for ODD j (j = 2k+1, m = 2i+1) and see if similar structure.
 (5) The clincher: does R_p(k, i) equal a shifted-Schur function evaluated at
     something?  Or the Sahi-Stanley Pieri coefficient for s^*_(k-i, k-i) * h^*_p?

Author: Rick, 4am, extra strong coffee.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, Integer, Rational, Poly, expand, factor, simplify, binomial

a, b, c = symbols('a b c')
u = a + 2


def fall(x, m):
    if m < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def bt(M):
    def vs(mu):
        L = len(mu) + 2
        bb = list(mu) + [0] * (L - len(mu))
        r = []
        for pp in combinations(range(L), 2):
            n = bb.copy()
            for i in pp:
                n[i] += 1
            ok = True
            for i in range(L - 1):
                if n[i] < n[i + 1]:
                    ok = False
                    break
            if not ok:
                continue
            while n and n[-1] == 0:
                n.pop()
            if len(n) > 3:
                continue
            r.append(tuple(n))
        return r
    cu = defaultdict(int)
    cu[()] = 1
    T = {0: [((0, 0, 0), 1)]}
    for jj in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[jj] = rs
    return T


def ds_symbolic(jj, tables):
    xs = (u, b + 1, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def V_of():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def dsV_all(J, tables):
    V = V_of()
    cache = {}
    for jj in range(J + 1):
        dsj = ds_symbolic(jj, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0
        cache[jj] = q.as_expr()
    return cache


def extract_A_p(jj, p, dsV_cache):
    S = dsV_cache[jj]
    if jj - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == jj - p:
            result += cf * b**db * c**dc
    return expand(result)


def s_star(lam, x1, x2):
    lam1, lam2 = lam
    assert lam1 >= lam2 >= 0
    num = (fall(x1 + 1, lam1 + 1) * fall(x2, lam2)
           - fall(x1 + 1, lam2) * fall(x2, lam1 + 1))
    den = (x1 - x2 + 1)
    num = sp.expand(num)
    q, r = sp.div(sp.Poly(num, x1, x2), sp.Poly(den, x1, x2))
    if r.as_expr() != 0:
        return sp.together(num / den)
    return q.as_expr()


def s_star_eval(lam, x1_val, x2_val):
    lam1, lam2 = lam
    A1 = fall(x1_val + 1, lam1 + 1) * fall(x2_val, lam2)
    A2 = fall(x1_val + 1, lam2) * fall(x2_val, lam1 + 1)
    num = A1 - A2
    den = x1_val - x2_val + 1
    if den == 0:
        xs, ys = symbols('_xs _ys')
        expr = s_star(lam, xs, ys)
        return sp.limit(expr.subs(ys, xs + 1 + symbols('_eps')), symbols('_eps'), 0).subs(xs, x1_val)
    return sp.Rational(num, den) if isinstance(num, sp.Integer) and isinstance(den, sp.Integer) else sp.simplify(num / den)


def shifted_schur_expand(F, D_max, delta=(0, 0)):
    coeffs = {}
    residual = sp.expand(F)
    for size in range(D_max + 1):
        lams = []
        for lam1 in range(size + 1):
            lam2 = size - lam1
            if lam1 >= lam2 >= 0:
                lams.append((lam1, lam2))
        lams.sort(reverse=True)
        for lam in lams:
            eval_pt_b = lam[0] + delta[0]
            eval_pt_c = lam[1] + delta[1]
            val = sp.expand(residual.subs([(b, eval_pt_b), (c, eval_pt_c)]))
            if val == 0:
                coeffs[lam] = Integer(0)
                continue
            diag = s_star_eval(lam, eval_pt_b, eval_pt_c)
            if diag == 0:
                raise RuntimeError(f"bad delta at lam={lam}")
            c_lam = sp.simplify(val / diag)
            coeffs[lam] = c_lam
            ss = s_star(lam, b, c)
            residual = sp.expand(residual - c_lam * ss)
    return coeffs, residual


def build_all(J=10, p_max=4):
    tables = bt(J)
    dsV = dsV_all(J, tables)
    A_data = {}
    coeffs = {}
    for p in range(1, p_max + 1):
        for jj in range(max(1, p), J + 1):
            A = extract_A_p(jj, p, dsV)
            A_data[(p, jj)] = A
            if A == 0:
                coeffs[(p, jj)] = {}
                continue
            db = sp.Poly(A, b, c).degree(b)
            dc = sp.Poly(A, b, c).degree(c)
            D_max = db + dc + 1
            cf, res = shifted_schur_expand(A, D_max, delta=(0, 0))
            assert sp.expand(res) == 0
            coeffs[(p, jj)] = {lam: v for lam, v in cf.items() if v != 0}
    return A_data, coeffs


def T_catalan(n, k):
    if k < 0 or k > n:
        return Integer(0)
    return binomial(n, k) - binomial(n, k - 1)


def get_seed_row(coeffs, p, jj):
    """Return list of (i, seed_value) for i = 0..k (with jj = 2k)."""
    row = []
    for m in range(0, jj + 1):
        if (jj + m) % 2 != 0:
            continue
        lam1 = (jj + m) // 2
        lam2 = (jj - m) // 2
        if lam1 < lam2 or lam2 < 0:
            continue
        cf = coeffs[(p, jj)].get((lam1, lam2), Integer(0))
        row.append((m // 2, cf))
    return row


def fit_poly(samples, var, max_deg=15):
    """samples = [(x_val, y_val)]. Fit y as polynomial in var (a sympy symbol).
    Return polynomial or None."""
    n = len(samples)
    for D in range(min(n, max_deg + 1)):
        rows = []
        yy = []
        for (xv, yv) in samples[:D + 1]:
            rows.append([Rational(xv) ** k for k in range(D + 1)])
            yy.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        try:
            sol = M.solve(y)
        except Exception:
            continue
        ok = True
        for (xv, yv) in samples[D + 1:]:
            pred = sum(sol[k] * xv ** k for k in range(D + 1))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            return sp.expand(sum(sol[k] * var ** k for k in range(D + 1)))
    return None


def main():
    J = 12  # go further to get more k samples
    p_max = 4
    print("Building A_p tables and coeffs...")
    A_data, coeffs = build_all(J=J, p_max=p_max)
    print("...done")

    i_sym = symbols('i')
    k_sym = symbols('k')

    print("=" * 78)
    print("(1) For each (p, k, even j = 2k), extract R_p(k, i) := seed(A_p, j=2k, m=2i) / T(2k, k-i)")
    print("    and fit R_p(k, i) as a poly in i.")
    print("=" * 78)

    # R_data[(p, k)] = poly in i_sym
    R_data = {}
    for p in range(1, p_max + 1):
        print(f"\n--- p = {p} ---")
        for jj in sorted(k[1] for k in coeffs if k[0] == p):
            if jj % 2 != 0:
                continue
            k = jj // 2
            row = get_seed_row(coeffs, p, jj)
            # ratio
            samples = []
            for (iv, seed) in row:
                Tv = T_catalan(2 * k, k - iv)
                if Tv == 0:
                    if seed != 0:
                        print(f"  p={p}, k={k}, i={iv}: T=0, seed={seed} -> undefined ratio!")
                    continue
                ratio = sp.Rational(seed, Tv)
                samples.append((iv, ratio))
            fit = fit_poly(samples, i_sym, max_deg=p + 2)
            if fit is not None:
                R_data[(p, k)] = fit
                print(f"  k={k}: R_{p}(k={k}, i) = {sp.factor(fit)}")
            else:
                print(f"  k={k}: NO fit found for R_{p}(k, i)")

    print("\n" + "=" * 78)
    print("(2) For each (p, degree-d coefficient of R_p(k, i)), fit as polynomial in k.")
    print("=" * 78)

    # Coefficient of i^d in R_p(k, i) for varying k.
    R_kd_polys = {}
    for p in range(1, p_max + 1):
        print(f"\n--- p = {p} ---")
        max_deg = 0
        for (pp, k) in R_data:
            if pp != p:
                continue
            pol = R_data[(pp, k)]
            d = sp.Poly(pol, i_sym).degree() if pol != 0 else 0
            max_deg = max(max_deg, d)
        for d in range(max_deg + 1):
            samples = []
            for (pp, k) in sorted(R_data):
                if pp != p:
                    continue
                pol = R_data[(pp, k)]
                # coeff of i^d
                c_d = sp.Poly(pol, i_sym).nth(d) if pol != 0 else Integer(0)
                samples.append((k, c_d))
            fit_k = fit_poly(samples, k_sym, max_deg=max(p, 4) + 3)
            if fit_k is not None:
                R_kd_polys[(p, d)] = fit_k
                print(f"  coeff of i^{d} in R_{p}(k, i): {sp.factor(fit_k)}")
            else:
                print(f"  coeff of i^{d}: samples = {samples}, NO fit found")

    print("\n" + "=" * 78)
    print("(3) Assemble R_p(k, i) as bivariate polynomial and see if it factors.")
    print("=" * 78)
    for p in range(1, p_max + 1):
        R_full = Integer(0)
        for (pp, d), pol_k in R_kd_polys.items():
            if pp != p:
                continue
            R_full += pol_k * i_sym ** d
        R_full = sp.expand(R_full)
        print(f"\n  R_{p}(k, i) = {sp.factor(R_full)}")
        print(f"    expanded: {R_full}")
        # Test at (k, i) values not used in the fit -- from (p, k) where k > J//2
        print(f"    verify at previously-unused (k, i):")
        for (pp, k) in R_data:
            if pp != p:
                continue
            pol = R_data[(pp, k)]
            match = sp.expand(pol - R_full.subs(k_sym, k)) == 0
            print(f"      k={k}: {'OK' if match else 'MISMATCH'}")

    print("\n" + "=" * 78)
    print("(4) Now DERIVE the full seed formula:")
    print("      c^{seed}_{lam=(k+i, k-i)}(A_p, j=2k) = R_p(k, i) * T(2k, k-i)")
    print("    Verify against ORIGINAL seed data for all (p, j) computed.")
    print("=" * 78)
    all_ok = True
    for p in range(1, p_max + 1):
        for jj in sorted(k[1] for k in coeffs if k[0] == p):
            if jj % 2 != 0:
                continue
            k = jj // 2
            row = get_seed_row(coeffs, p, jj)
            # sum R_kd*k^k*i^i * T(2k, k-i)
            R_full = Integer(0)
            for (pp, d), pol_k in R_kd_polys.items():
                if pp != p:
                    continue
                R_full += pol_k * i_sym ** d
            for (iv, seed_actual) in row:
                Rv = sp.expand(R_full.subs([(k_sym, k), (i_sym, iv)]))
                Tv = T_catalan(2 * k, k - iv)
                pred = Rv * Tv
                if sp.simplify(pred - seed_actual) != 0:
                    print(f"  MISMATCH p={p}, j={jj}, i={iv}: actual={seed_actual}, predicted={pred}")
                    all_ok = False
        # summary per p
    if all_ok:
        print("  ALL SEEDS MATCH the formula seed = R_p(k, i) * T(2k, k-i)")
    print("\nDone.")


if __name__ == "__main__":
    main()
