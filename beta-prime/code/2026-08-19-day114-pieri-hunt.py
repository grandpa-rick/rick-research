"""Day 114 (compute pass): Pieri-rule hunt for A_p in the shifted-Schur basis.

Hypothesis (Rick's): A_p = (something small) * h^*_p or e^*_p, or
A_p is a bilinear Sahi-Stanley Pieri product for some base lambda_0.

Strategy:
 1) Reload / recompute A_p and its (c_lambda) shifted-Schur expansion (from
    day114-Ap-shifted-schur-direct.py machinery).
 2) Recompute the "seed integers" c_lambda at |lambda| = j (bottom of support)
    and stare at them across (p, j).  See if they factor as
         seed(p, j, m) = [known Pieri multiplier for h^*_p or e^*_p]
    or as a product of a fixed s^*_{lambda_0} * (something on m).
 3) Compute A_p / A_{p-1} as a rational function of (b, c) for concrete j.
    If Pieri holds we expect the ratio to be a low-degree polynomial (Pieri
    multiplier).  If it isn't polynomial, that alone kills the "single
    Pieri step" hypothesis (though a sum of Pieri steps could still work).
 4) Compute the generating function F(t) = sum_{p >= 0} A_p t^p for a fixed
    j (small, say j = 4 or 6) and see if F(t) has a closed form.
 5) Try dividing by s^*_{(j, 0)}(b, c) (i.e., (b+1)^{↓(j+1)} minus (c)^{↓(j+1)}
    over (b - c + 1)) and see if the quotient is polynomial and simple.
 6) Independent test: compute s^*_lambda * h^*_p in the shifted Schur basis
    (Sahi-Stanley Pieri rule) for small lambda's and check if any linear
    combination matches c_lambda(j, p) at bottom level.

Author: compute agent, Rick's day 114.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, Integer, Rational, Poly, expand, factor, simplify

# ---------------------------------------------------------------------------
# Copy the machinery from day114-Ap-shifted-schur-direct.py (self contained).
# ---------------------------------------------------------------------------

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
        for p in combinations(range(L), 2):
            n = bb.copy()
            for i in p:
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


# --- shifted schur (2 var) ---


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


# ---------------------------------------------------------------------------
# Compute A_p and shifted-Schur expansions.
# ---------------------------------------------------------------------------


def build_all(J=10, p_max=4):
    tables = bt(J)
    dsV = dsV_all(J, tables)
    A_data = {}
    coeffs = {}
    for p in range(1, p_max + 1):
        j_min = max(2 * p, 1)  # A_p defined for j >= 2p roughly, but 1 also works
        for jj in range(j_min, J + 1):
            A = extract_A_p(jj, p, dsV)
            A_data[(p, jj)] = A
            # expand into shifted schur
            db = sp.Poly(A, b, c).degree(b) if A != 0 else 0
            dc = sp.Poly(A, b, c).degree(c) if A != 0 else 0
            D_max = db + dc + 1
            cf, res = shifted_schur_expand(A, D_max, delta=(0, 0))
            assert sp.expand(res) == 0, f"nonzero residual for (p={p}, j={jj})"
            coeffs[(p, jj)] = {lam: v for lam, v in cf.items() if v != 0}
    return A_data, coeffs


# ---------------------------------------------------------------------------
# Sahi-Stanley Pieri rule for s^*_lambda * h_r^*.
# For 2-variable case, the formula (Molev 2009 style / Okounkov-Olshanski) is:
#   s^*_lam * h_r^* = sum over mu / lam = horizontal r-strip of
#         [prod over columns j in mu\lam of (lam'_j - j + 1 + ??)] s^*_mu
# For n=2 variables, mu \subseteq lam only in the sense of Young diagrams,
# and mu / lam a horizontal r-strip means lam_i <= mu_i <= lam_{i-1}.
#
# The proper form for factorial Schur functions (see Molev-Sagan):
#   s^*_lambda * h_r^*(x | a) = sum over horizontal r-strips mu \supset lambda
#      psi_{lam, mu} * s^*_mu
# where psi involves the "content" a_{lam_i + n - i} - a_{mu_i + n - i - 1}.
# For the shifted schur (Okounkov / SV), a_k = k so the content shift is
# specific.
#
# Rather than trying to reconstruct the exact formula from memory, let me
# compute s^*_lambda * h_r^*(b, c) directly (in 2 vars, h_r = complete
# homogeneous which coincides with s^*_(r, 0) as SHIFTED schur — no, wait,
# in the SHIFTED world h_r^* is a different beast).
# ---------------------------------------------------------------------------


def h_r_star(r, x1, x2):
    """Shifted complete homogeneous h_r^*.
    In Okounkov, h_r^* is defined by h_r^*(x) = sum_{lambda: |lambda|=r} s^*_lambda(x).
    Actually h_r^* corresponds to lambda = (r) (row of length r), i.e.,
    h_r^* = s^*_{(r)} in the shifted schur basis? Not quite -- shifted
    schur functions don't obey the same Pieri identity as ordinary Schur.

    Actually the correct statement is: h_r^*(x) := s^*_{(r)}(x) is the
    shifted homogeneous. Let's just define h_r^* = s^*_{(r, 0)}.
    """
    return s_star((r, 0), x1, x2)


def e_r_star(r, x1, x2):
    """Shifted elementary e_r^* = s^*_{(1^r)}."""
    if r == 0:
        return Integer(1)
    if r == 1:
        return s_star((1, 0), x1, x2)
    if r == 2:
        return s_star((1, 1), x1, x2)
    # For 2-variable case, only r = 0, 1, 2 makes sense
    return Integer(0)


# ---------------------------------------------------------------------------
# Test 1: seeds at |lambda| = j.  For each (p, j), extract seed sequence
# (as m := lam_1 - lam_2 varies).  Fit as polynomial in m.  Check if it
# factors as (small)*p(m).
# ---------------------------------------------------------------------------


def print_seeds(coeffs, p_max=4):
    print("\n" + "=" * 78)
    print("SEEDS: c_lambda(bottom) for |lambda| = j.")
    print("=" * 78)
    m_sym = symbols('m')
    seeds = {}   # (p, j) -> list of (m, seed)
    for p in range(1, p_max + 1):
        js = sorted(k[1] for k in coeffs if k[0] == p)
        for jj in js:
            row = []
            for m in range(0, jj + 1):
                if (jj + m) % 2 != 0:
                    continue
                lam1 = (jj + m) // 2
                lam2 = (jj - m) // 2
                if lam1 < lam2 or lam2 < 0:
                    continue
                lam = (lam1, lam2)
                cf = coeffs[(p, jj)].get(lam, Integer(0))
                row.append((m, lam, cf))
            seeds[(p, jj)] = row
            print(f"  p={p}, j={jj}: seeds = {[int(r[2]) for r in row]}   (m = {[r[0] for r in row]})")
    return seeds


def fit_poly_in_m(samples, max_deg=15):
    """samples = [(m_val, y_val)]. Return polynomial in m or None."""
    m_sym = symbols('m')
    n = len(samples)
    for D in range(min(n, max_deg + 1)):
        rows = []
        yy = []
        for (mv, yv) in samples[:D + 1]:
            rows.append([Rational(mv) ** i for i in range(D + 1)])
            yy.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        try:
            sol = M.solve(y)
        except Exception:
            continue
        ok = True
        for (mv, yv) in samples[D + 1:]:
            pred = sum(sol[i] * mv ** i for i in range(D + 1))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            return sp.expand(sum(sol[i] * m_sym ** i for i in range(D + 1)))
    return None


def fit_seeds_in_m(seeds, p_max=4):
    """For each (p, j), fit seed(m) as a polynomial in m and factor."""
    print("\n" + "=" * 78)
    print("SEED POLYNOMIALS IN m (for fixed p, j).")
    print("=" * 78)
    all_fits = {}
    for p in range(1, p_max + 1):
        print(f"\n  p = {p}:")
        for (pp, jj) in sorted(seeds):
            if pp != p:
                continue
            samples = [(r[0], r[2]) for r in seeds[(p, jj)]]
            if len(samples) < 2:
                print(f"    j={jj}: only {len(samples)} samples, skipping")
                continue
            poly_m = fit_poly_in_m(samples)
            if poly_m is None:
                print(f"    j={jj}: NO fit ({len(samples)} samples)")
            else:
                all_fits[(p, jj)] = poly_m
                fm = sp.factor(poly_m)
                print(f"    j={jj}: seed(m) = {fm}")
    return all_fits


# ---------------------------------------------------------------------------
# Test 2: bivariate fit of seed as function of (j, m) for fixed p.
# ---------------------------------------------------------------------------


def fit_bivariate_jm_for_fixed_p(seeds, p):
    print(f"\n  Bivariate seed(j, m) fit for p = {p}:")
    all_samples = []
    for (pp, jj) in seeds:
        if pp != p:
            continue
        for (mv, lam, cf) in seeds[(pp, jj)]:
            all_samples.append(((jj, mv), cf))
    j_sym, m_sym = symbols('jj mm')

    for total_deg in range(0, 15):
        unknowns = []
        for dj in range(total_deg + 1):
            for dm in range(total_deg + 1 - dj):
                unknowns.append((dj, dm))
        if len(unknowns) > len(all_samples):
            continue
        rows = []
        yy = []
        for ((jv, mv), yv) in all_samples:
            rows.append([Rational(jv) ** dj * Rational(mv) ** dm for (dj, dm) in unknowns])
            yy.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        try:
            x = M.solve(y)
        except Exception:
            continue
        ok = True
        for ((jv, mv), yv) in all_samples:
            pred = sum(x[i] * Rational(jv) ** unknowns[i][0] * Rational(mv) ** unknowns[i][1]
                       for i in range(len(unknowns)))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            expr = sum(x[i] * j_sym ** unknowns[i][0] * m_sym ** unknowns[i][1]
                       for i in range(len(unknowns)))
            print(f"    p={p}: seed(j, m) = {sp.factor(sp.expand(expr))}")
            return sp.expand(expr)
    print(f"    p={p}: NO bivariate (j, m) fit up to total degree 15")
    return None


# ---------------------------------------------------------------------------
# Test 3: is A_p = s^*_{(j, 0)} * (something simpler)?
# ---------------------------------------------------------------------------


def test_divide_by_ssj0(A_data):
    print("\n" + "=" * 78)
    print("Test: A_p / s^*_{(j, 0)}(b, c) -- is quotient polynomial in (b, c)?")
    print("=" * 78)
    for (p, jj), A in sorted(A_data.items()):
        if p > 4:
            continue
        S = s_star((jj, 0), b, c)
        # A / S
        try:
            q, r = sp.div(sp.Poly(A, b, c), sp.Poly(S, b, c))
            if r.as_expr() == 0:
                print(f"  p={p}, j={jj}: DIVIDES.  quotient = {sp.factor(q.as_expr())}")
            else:
                print(f"  p={p}, j={jj}: does not divide (nonzero remainder).")
        except Exception as e:
            print(f"  p={p}, j={jj}: division failed: {e}")


# ---------------------------------------------------------------------------
# Test 4: A_p / A_{p-1}?  Compute ratio as rational function, see if polynomial.
# ---------------------------------------------------------------------------


def test_ratio_ap_over_ap1(A_data, p_max=4):
    print("\n" + "=" * 78)
    print("Test: A_p / A_{p-1} -- is ratio a low-degree polynomial in (b, c)?")
    print("=" * 78)
    for p in range(2, p_max + 1):
        for jj in range(max(2 * p, 1), 11):
            if (p, jj) not in A_data or (p - 1, jj) not in A_data:
                continue
            A = A_data[(p, jj)]
            Aprev = A_data[(p - 1, jj)]
            if Aprev == 0:
                continue
            try:
                q, r = sp.div(sp.Poly(A, b, c), sp.Poly(Aprev, b, c))
                if r.as_expr() == 0:
                    print(f"  p={p}, j={jj}: A_p / A_{{p-1}} = {sp.factor(q.as_expr())}")
                else:
                    # Try the other way
                    quotient_rat = sp.together(A / Aprev)
                    quotient_simple = sp.cancel(quotient_rat)
                    print(f"  p={p}, j={jj}: no polynomial quotient; cancel(A_p/A_{{p-1}}) = "
                          f"[num deg = {sp.Poly(sp.numer(quotient_simple), b, c).total_degree()}, "
                          f"den deg = {sp.Poly(sp.denom(quotient_simple), b, c).total_degree()}]")
            except Exception as e:
                print(f"  p={p}, j={jj}: division exception: {e}")


# ---------------------------------------------------------------------------
# Test 5: generating function F(t) = sum_p A_p * t^p at fixed j.
# ---------------------------------------------------------------------------


def test_generating_function(A_data, j_fix=6, p_max=6):
    print("\n" + "=" * 78)
    print(f"Test: F(t) = sum_p A_p(b, c; j={j_fix}) t^p.")
    print("=" * 78)
    t = symbols('t')
    F = Integer(0)
    for p in range(0, p_max + 1):
        if (p, j_fix) in A_data:
            F += A_data[(p, j_fix)] * t**p
        elif p == 0:
            # A_0 is not tracked, but for the ds decomposition A_0 is the
            # top-degree term.
            pass
    # Try to factor F as function of (b, c, t)
    Fs = sp.factor(F)
    print(f"  F(t) [j={j_fix}] = ")
    print(f"  {sp.expand(F)}")
    print(f"  factored:")
    print(f"  {Fs}")


# ---------------------------------------------------------------------------
# Test 6: compute s^*_lambda * h_r^* directly (product in 2-variable
# shifted Schur) and expand back.  See if it matches c_lambda(bottom).
# ---------------------------------------------------------------------------


def pieri_h(lam, r):
    """Compute (s^*_lam * h_r^*)(b, c) and expand in the shifted-Schur basis.
    Return dict {mu: coeff}."""
    prod = sp.expand(s_star(lam, b, c) * h_r_star(r, b, c))
    db = sp.Poly(prod, b, c).degree(b) if prod != 0 else 0
    dc = sp.Poly(prod, b, c).degree(c) if prod != 0 else 0
    D_max = db + dc + 1
    cf, res = shifted_schur_expand(prod, D_max)
    assert sp.expand(res) == 0
    return {mu: v for mu, v in cf.items() if v != 0}


def pieri_e(lam, r):
    """(s^*_lam * e_r^*) expanded."""
    prod = sp.expand(s_star(lam, b, c) * e_r_star(r, b, c))
    db = sp.Poly(prod, b, c).degree(b) if prod != 0 else 0
    dc = sp.Poly(prod, b, c).degree(c) if prod != 0 else 0
    D_max = db + dc + 1
    cf, res = shifted_schur_expand(prod, D_max)
    assert sp.expand(res) == 0
    return {mu: v for mu, v in cf.items() if v != 0}


def test_pieri_h_at_seed(coeffs, p_max=4):
    """For each p, try to write the SEED-LEVEL coefficients c_lambda(|lam|=j)
    as [some multiplier] * (Pieri coefficient of s^*_{lam0} * h_p^*)."""
    print("\n" + "=" * 78)
    print("Test: is A_p 'looking like' s^*_{lam0} * h_p^* at seed level?")
    print("=" * 78)
    print("  For each j, print (Pieri coeff s^*_{(j-p, 0)} * h^*_p) vs SEED.")
    for p in range(1, p_max + 1):
        js = sorted(k[1] for k in coeffs if k[0] == p)
        for jj in js:
            # Test candidate lam_0 = (jj - p, 0)
            if jj - p < 0:
                continue
            lam0 = (jj - p, 0)
            expansion = pieri_h(lam0, p)
            print(f"\n  p={p}, j={jj}, lam0={lam0}: (s^*_lam0 * h_{p}^*) expansion:")
            for mu, cf in sorted(expansion.items(), key=lambda x: (x[0][0] + x[0][1], x[0])):
                print(f"    mu={mu}: coeff={cf}")
            # Compare to seed level
            print(f"  Seed of A_{p} at j={jj} (only |mu|=j part):")
            for mu, cf in sorted(coeffs[(p, jj)].items(), key=lambda x: (x[0][0] + x[0][1], x[0])):
                if mu[0] + mu[1] != jj:
                    continue
                print(f"    mu={mu}: c_mu(A_p)={cf}")


# ---------------------------------------------------------------------------
# Test 7: ratios seed[m] / seed[m+1] or seed[m] / (something Pieri-like).
# ---------------------------------------------------------------------------


def stare_at_seeds(seeds):
    print("\n" + "=" * 78)
    print("STARING at seed sequences.  Test seed[m] and neighbors.")
    print("=" * 78)
    for (p, jj), row in sorted(seeds.items()):
        vals = [r[2] for r in row]
        ms = [r[0] for r in row]
        if len(vals) < 2:
            continue
        print(f"\n  p={p}, j={jj}: seeds = {[int(v) for v in vals]} at m = {ms}")
        # GCD
        g = vals[0]
        for v in vals[1:]:
            g = sp.gcd(g, v)
        print(f"    GCD = {g}")
        # normalize
        norm = [v / g for v in vals]
        print(f"    normalized = {[int(nv) for nv in norm]}")
        # Ratios
        for i in range(len(vals) - 1):
            r = sp.Rational(vals[i + 1], vals[i])
            print(f"    seed[m={ms[i+1]}] / seed[m={ms[i]}] = {r}")


# ---------------------------------------------------------------------------
# Test 8: alternative -- does the seed sequence match a HOOK CONTENT product?
# For the "top" coefficient at |lambda| = j+p (top of support), same story.
# ---------------------------------------------------------------------------


def print_top_level(coeffs, p_max=4):
    print("\n" + "=" * 78)
    print("TOP-level coefficients: c_lambda at |lambda| = j + p.")
    print("=" * 78)
    for p in range(1, p_max + 1):
        js = sorted(k[1] for k in coeffs if k[0] == p)
        for jj in js:
            print(f"\n  p={p}, j={jj}:")
            for mu, cf in sorted(coeffs[(p, jj)].items(), key=lambda x: (x[0][0] + x[0][1], x[0])):
                if mu[0] + mu[1] != jj + p:
                    continue
                print(f"    mu={mu}: coeff = {cf}")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main():
    J = 10
    p_max = 4
    print("=" * 78)
    print("Day-114 pieri hunt.")
    print("=" * 78)
    A_data, coeffs = build_all(J=J, p_max=p_max)

    # (1) SEEDS - fixed j, varying m
    seeds = print_seeds(coeffs, p_max=p_max)

    # (2) Fit seed(m) as polynomial in m for each (p, j)
    fits = fit_seeds_in_m(seeds, p_max=p_max)

    # (2.5) Fit bivariate (j, m) for each p
    print("\n" + "=" * 78)
    print("BIVARIATE seed(j, m) FIT FOR EACH p")
    print("=" * 78)
    biv_fits = {}
    for p in range(1, p_max + 1):
        biv_fits[p] = fit_bivariate_jm_for_fixed_p(seeds, p)

    # (3) Top-level coefficients
    print_top_level(coeffs, p_max=p_max)

    # (4) Divide by s^*_{(j,0)}
    test_divide_by_ssj0(A_data)

    # (5) A_p / A_{p-1}
    test_ratio_ap_over_ap1(A_data, p_max=p_max)

    # (6) Generating function
    for j_fix in (4, 6):
        test_generating_function(A_data, j_fix=j_fix, p_max=p_max)

    # (7) Test Pieri h_p^* directly
    test_pieri_h_at_seed(coeffs, p_max=min(p_max, 3))

    # (8) Stare at seeds
    stare_at_seeds(seeds)

    print("\n" + "=" * 78)
    print("Done.")
    print("=" * 78)


if __name__ == "__main__":
    main()
