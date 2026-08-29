"""Day 115: falsification tests for the layer-shape lemma.

Three checks per PROVE.md:
    (1) Extend to p = 5, j in {10, 11, 12}. Verify ansatz form + degree bounds.
    (2) Extend to p = 6, j in {12, 13}. Same.
    (3) Odd-j seed factorization: does the Catalan-triangle structure survive?
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational, factor, binomial

a, b, c = symbols('a b c')
u = a + 2
sig, pi_v = symbols('sigma pi')
j_sym = symbols('j')


def fall(x, m):
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
            result += cf * b ** db * c ** dc
    return expand(result)


def is_sym_bc1(F):
    F_swap = F.subs([(b, symbols('_t1')), (c, symbols('_t2'))], simultaneous=True)
    F_swap = F_swap.subs([(symbols('_t1'), c - 1), (symbols('_t2'), b + 1)])
    return expand(F - expand(F_swap)) == 0


def to_pi_sigma_shifted(F):
    z = symbols('_z_pi_sig_')
    Fz = expand(F.subs([(b, z - 1), (c, sig - z)]))
    Pz = sp.Poly(Fz, z)
    D = Pz.degree()
    coefs = [Pz.coeff_monomial(z ** i) for i in range(D + 1)]
    while len(coefs) > 2:
        top = coefs[-1]
        d = len(coefs) - 1
        if top == 0:
            coefs.pop()
            continue
        coefs[d - 1] = sp.expand(coefs[d - 1] + sig * top)
        coefs[d - 2] = sp.expand(coefs[d - 2] - pi_v * top)
        coefs.pop()
    while len(coefs) < 2:
        coefs.append(Integer(0))
    if sp.simplify(coefs[1]) != 0:
        return None
    return sp.expand(coefs[0])


def falling_sigma(shift, length):
    if length <= 0:
        return Integer(1) if length == 0 else None
    r = Integer(1)
    for i in range(length):
        r *= (sig - shift - i)
    return sp.expand(r)


def fit_in_pi_sigma(F_ps, k_max, shift, length, D_alpha):
    fall_sig = falling_sigma(shift, length)
    unknowns = []
    basis_map = {}
    for k in range(k_max + 1):
        for d in range(D_alpha + 1):
            basis_map[(k, d)] = sp.expand(pi_v ** k * fall_sig * sig ** d)
            unknowns.append((k, d))
    syms = symbols(' '.join(f'x_{k}_{d}' for (k, d) in unknowns))
    if not isinstance(syms, tuple):
        syms = (syms,)
    expr = sp.expand(sum(syms[i] * basis_map[unknowns[i]] for i in range(len(unknowns))) - F_ps)
    P = sp.Poly(expr, pi_v, sig)
    eqs = [cf for _, cf in P.terms()]
    sol = sp.solve(eqs, syms, dict=True)
    if not sol:
        return None
    s = sol[0]
    for x in syms:
        if x not in s:
            s[x] = Integer(0)
    pred = sp.expand(sum(s[syms[i]] * basis_map[unknowns[i]] for i in range(len(unknowns))))
    if sp.expand(pred - F_ps) != 0:
        return None
    result = {}
    for k in range(k_max + 1):
        alpha_k = Integer(0)
        for d in range(D_alpha + 1):
            alpha_k += s[symbols(f'x_{k}_{d}')] * sig ** d
        result[k] = sp.expand(alpha_k)
    return result


# ---------------------------------------------------------------------------
# Test 1 and 2: extend to p=5 and p=6.
# ---------------------------------------------------------------------------

def test_p(p, j_range, J, tables, dsV):
    print(f"\n{'=' * 72}")
    print(f"  Test  p = {p}, j in {list(j_range)}")
    print(f"{'=' * 72}")
    results = {}
    for jj in j_range:
        A = extract_A_p(jj, p, dsV)
        if not is_sym_bc1(A):
            print(f"  j = {jj}: NOT symmetric — abort.")
            continue
        F_ps = to_pi_sigma_shifted(A)
        if F_ps is None:
            print(f"  j = {jj}: cannot convert to (pi, sigma).")
            continue
        Pps = sp.Poly(F_ps, pi_v, sig)
        print(f"  j = {jj}: (deg_pi, deg_sig) = ({Pps.degree(pi_v)}, {Pps.degree(sig)})")
        length = jj - 2 * p
        shift = 2 * p + 1
        found = None
        for D_alpha in range(0, 2 * p + 2):
            sol = fit_in_pi_sigma(F_ps, k_max=p, shift=shift, length=length, D_alpha=D_alpha)
            if sol is not None:
                found = (D_alpha, sol)
                break
        if found is None:
            print(f"  j = {jj}: NO FIT with shift={shift}, length={length}, k_max={p}, D_alpha<={2*p+1}.")
            continue
        D_alpha, sol = found
        results[jj] = sol
        # Verify degree bounds
        all_ok = True
        for k in range(p + 1):
            alpha_k = sol[k]
            if alpha_k == 0:
                deg_k = -1
            else:
                deg_k = sp.Poly(alpha_k, sig).degree()
            expected_deg = 2 * p - k
            ok = (deg_k <= expected_deg)
            marker = "OK" if ok else "FAIL"
            print(f"    alpha_{{{p},{k}}}: deg_sig = {deg_k} (expected <= {expected_deg}) [{marker}]")
            if not ok:
                all_ok = False
        if all_ok:
            print(f"    -> all deg_sig bounds pass.")
    return results


def main():
    J = 13
    print(f"Building shifted-Schur tables & ds_j/V up to j = {J} ...")
    tables = bt(J)
    dsV = dsV_all(J, tables)
    print("done.\n")

    # Test 1: p = 5, j = 10, 11, 12
    results5 = test_p(5, [10, 11, 12], J, tables, dsV)

    # Test 2: p = 6, j = 12, 13
    results6 = test_p(6, [12, 13], J, tables, dsV)

    # Now fit alpha_{p,k}(j, sigma) as bivariate poly and check j-degree
    print("\n" + "=" * 72)
    print("  j-degree bounds on alpha_{p,k}(j, sigma) — need deg_j <= 2p")
    print("=" * 72)

    for p, results in [(5, results5), (6, results6)]:
        if not results:
            continue
        js = sorted(results.keys())
        if len(js) < 2:
            print(f"\n  p = {p}: only {len(js)} j-values, can't fit as poly in j.")
            continue
        print(f"\n  p = {p}: fitting alpha_{{{p},k}}(j, sigma) using j = {js}")
        # For each k, and each sigma-power d, fit as polynomial in j.
        for k in range(p + 1):
            # Collect samples of alpha_{p,k}(j, sigma) as polys in sigma.
            samples = {jj: results[jj][k] for jj in js}
            # For each sigma-power d, collect (j, coef) samples.
            max_d = 0
            for jj, alpha in samples.items():
                if alpha != 0:
                    max_d = max(max_d, sp.Poly(alpha, sig).degree())
            print(f"    alpha_{{{p},{k}}}: max sigma-degree observed = {max_d}")
            worst_deg_j = -1
            for d in range(max_d + 1):
                data = []
                for jj in js:
                    alpha = samples[jj]
                    coef = sp.Poly(alpha, sig).coeff_monomial(sig ** d) if alpha != 0 else Integer(0)
                    data.append((jj, coef))
                # Try to fit as polynomial in j of degree <= len(js) - 1
                # We want to know if degree is <= 2p
                # Use divided differences
                # Find min degree that fits
                for D in range(len(js)):
                    if D > 2 * p + 2:
                        break
                    rows = []
                    yy = []
                    for (jv, yv) in data[:D + 1]:
                        rows.append([Rational(jv) ** i for i in range(D + 1)])
                        yy.append(yv)
                    M = sp.Matrix(rows)
                    y = sp.Matrix(yy)
                    try:
                        sol_v = M.solve(y)
                    except Exception:
                        continue
                    ok = True
                    for (jv, yv) in data[D + 1:]:
                        pred = sum(sol_v[i] * jv ** i for i in range(D + 1))
                        if sp.simplify(pred - yv) != 0:
                            ok = False
                            break
                    if ok:
                        worst_deg_j = max(worst_deg_j, D)
                        break
                else:
                    worst_deg_j = max(worst_deg_j, len(js))  # unknown, at least
            marker = "OK" if worst_deg_j <= 2 * p else "FAIL"
            print(f"      worst deg_j across all d = {worst_deg_j} (expected <= {2*p}) [{marker}]")


if __name__ == "__main__":
    main()
