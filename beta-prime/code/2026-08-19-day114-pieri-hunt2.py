"""Day 114 pieri hunt V2 -- more targeted.

Observations from V1:
 1) SEEDS for p=1 at even j after normalizing by GCD give
        (1, 1), (2, 3, 1), (5, 9, 5, 1), (14, 28, 20, 7, 1), (42, 90, 75, 35, 9, 1)
    The leading integers 1, 2, 5, 14, 42 are CATALAN NUMBERS C_1, C_2, C_3, C_4, C_5.
    The trailing integers 1, 1, 1, 1, 1 are just 1.
    Suggestion: seed(p=1, j=2k, m=2i) might be C(k, i) * C(k, i+1) * ??
 2) At TOP-LEVEL (|mu| = j+p), coefficients look small and hookish.

Plan:
 (A) Recompute seeds cleanly and factor GCDs; test if bottom-level
     seed(p=1, j=2k, m=2i) = -(2 choose something) or Narayana.
 (B) For the TOP level (|mu| = j+p), check if coefficients match
     the Sahi-Stanley Pieri rule for  s^*_{(j-p, 0)} h^*_{p}.
 (C) Broaden search: A_p might equal sum_r c_r * s^*_{(j-p, r-p)} h_r for small r.
 (D) Match TOP level to  s^*_{lam0} * h_p^*  for the CORRECT choice of lam0.

Author: Rick, 2am, drunk.
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


# ---------------------------------------------------------------------------
# (A) SEEDS analysis: catalan pattern?
# ---------------------------------------------------------------------------


def catalan(n):
    return binomial(2 * n, n) // (n + 1)


def analyze_seeds(coeffs, p_max=4):
    print("=" * 78)
    print("SEED ANALYSIS -- (p=1 catalan pattern?)")
    print("=" * 78)
    for p in range(1, p_max + 1):
        print(f"\n--- p = {p} ---")
        js = sorted(k[1] for k in coeffs if k[0] == p)
        for jj in js:
            seed_row = []
            for m in range(0, jj + 1):
                if (jj + m) % 2 != 0:
                    continue
                lam1 = (jj + m) // 2
                lam2 = (jj - m) // 2
                if lam1 < lam2 or lam2 < 0:
                    continue
                cf = coeffs[(p, jj)].get((lam1, lam2), Integer(0))
                seed_row.append((m, cf))
            if not seed_row or all(x[1] == 0 for x in seed_row):
                continue
            # GCD (over nonzero seeds)
            nz = [x[1] for x in seed_row if x[1] != 0]
            g = nz[0]
            for v in nz[1:]:
                g = sp.gcd(g, v)
            norm = [(m, cf // g) for (m, cf) in seed_row]
            # Print
            raw = [int(cf) for (_, cf) in seed_row]
            norm_row = [int(cf) for (_, cf) in norm]
            print(f"  j={jj}: raw = {raw}, gcd = {g}, normalized = {norm_row}")


# ---------------------------------------------------------------------------
# (B) Fit Catalan-shape formula.
# ---------------------------------------------------------------------------


def test_catalan_seed(coeffs):
    """Test: for p=1, is
        seed(j=2k, m=2i) = -C_k * (binomial(2k-1, k-i) - binomial(2k-1, k-i-1)) ?
        (Narayana-like)
    or
        seed(j=2k, m=2i) = -SOME EXPLICIT combinatorial statistic
    Do a fit.
    """
    print("\n" + "=" * 78)
    print("Testing p=1 seed against Catalan/binomial formulas...")
    print("=" * 78)
    p = 1
    js = sorted(k[1] for k in coeffs if k[0] == p)
    for jj in js:
        if jj % 2 != 0:
            continue
        k = jj // 2
        # seeds at m = 0, 2, 4, ..., 2k
        seeds = []
        for i in range(k + 1):
            m = 2 * i
            lam1 = (jj + m) // 2
            lam2 = (jj - m) // 2
            cf = coeffs[(p, jj)].get((lam1, lam2), Integer(0))
            seeds.append(cf)
        # Overall structure: seeds are negative for j >= 4.
        # test 1: is |seeds[i]| = catalan(k) * binomial(k, i) * binomial(k, i+1) / catalan(k) style?
        # For k=2: (4, 6, 2).  binom(2,0)*binom(2,1)=2, ...
        # test:  binom(2k, k+m/2) - binom(2k, k+m/2+1)?  This is Narayana-like.
        cands = {}
        cands['binom_diff']   = [binomial(2*k, k + i) - binomial(2*k, k + i + 1) for i in range(k + 1)]
        cands['binom_prod']   = [binomial(k, i) * binomial(k, i + 1) if i + 1 <= k else 0 for i in range(k + 1)]
        cands['naray_alt']    = [Rational(binomial(k, i) * binomial(k, i + 1), (i + 1) if (i + 1) > 0 else 1) if i + 1 <= k else 0 for i in range(k + 1)]
        # Actual seeds absolute value
        abs_seeds = [abs(s) for s in seeds]
        print(f"  j={jj} (k={k}):  seeds = {[int(s) for s in seeds]}   abs = {[int(s) for s in abs_seeds]}")
        for name, cand in cands.items():
            print(f"     candidate '{name}' = {[int(x) for x in cand]}")
        # Try:  seeds = A * binomial(k, i) * binomial(k, i+1) for i=0..k
        # (with binomial(k, k+1) = 0)
        # Actually for k=3 (j=6):  seeds (5,9,5,1), binom(3,0)*binom(3,1)=3, hmm.
        # Let me try seeds[i] / binom(2k, i+k)?


# ---------------------------------------------------------------------------
# (C) TOP LEVEL analysis: match to Sahi-Stanley Pieri for h^*_p at (lam_0)?
# ---------------------------------------------------------------------------


def sahi_stanley_pieri_h(lam, r, n_vars=2):
    """(Simplified) 2-variable shifted-Schur Pieri: compute
       s^*_lam(b, c) * h_r^*(b, c) with h^*_r := s^*_(r).
    Expand back and return dict {mu: coeff}."""
    prod = sp.expand(s_star(lam, b, c) * s_star((r, 0), b, c))
    if prod == 0:
        return {}
    P = sp.Poly(prod, b, c)
    db, dc = P.degree(b), P.degree(c)
    D_max = db + dc + 1
    cf, res = shifted_schur_expand(prod, D_max)
    assert sp.expand(res) == 0
    return {mu: v for mu, v in cf.items() if v != 0}


def test_pieri_h_all(coeffs, p, jj_target):
    """Compare top-level coeffs of A_p at level j=jj_target vs s^*_{lam0}*s^*_{(p,0)}.
    Sweep lam0 across possibilities."""
    print(f"\n  === p={p}, j={jj_target}: testing top-level Pieri matches ===")
    top_level = {mu: cf for mu, cf in coeffs[(p, jj_target)].items()
                 if mu[0] + mu[1] == jj_target + p}
    print(f"    A_p top-level (|mu|={jj_target + p}): {sorted(top_level.items())}")
    # Try lam0 = (jj_target - p + r, ...) for various shapes with |lam0| = jj_target.
    # Only match lam0 with 2-part shape.
    candidates = []
    for a1 in range(0, jj_target + 1):
        a2 = jj_target - a1
        if a1 < a2:
            continue
        candidates.append((a1, a2))
    # Also try |lam0| = jj_target - k for k = 0..p.
    for L in range(jj_target - p, jj_target + 1):
        for a1 in range(0, L + 1):
            a2 = L - a1
            if a1 < a2:
                continue
            lam0 = (a1, a2)
            if lam0 in candidates:
                continue
            candidates.append(lam0)
    # Filter to reasonable # of candidates
    for lam0 in candidates:
        # r = jj_target + p - |lam0|.
        r = jj_target + p - lam0[0] - lam0[1]
        if r <= 0:
            continue
        # s^*_lam0 * s^*_(r, 0)
        try:
            prod = sahi_stanley_pieri_h(lam0, r)
        except Exception:
            continue
        prod_top = {mu: v for mu, v in prod.items() if mu[0] + mu[1] == jj_target + p}
        # normalize
        if not prod_top or not top_level:
            continue
        # Are they equal up to a global constant?
        # take first nonzero mu common to both
        common = set(prod_top).intersection(top_level)
        if not common:
            continue
        # Ratio at each common mu
        mus = sorted(common)
        ratios = []
        for mu in mus:
            if prod_top[mu] == 0:
                continue
            r_val = sp.Rational(top_level[mu], prod_top[mu])
            ratios.append(r_val)
        if len(ratios) < 2:
            continue
        if all(r == ratios[0] for r in ratios):
            # match with constant factor
            print(f"    lam0={lam0}, r={r}: TOP LEVEL MATCHES with factor {ratios[0]}")
            print(f"        pieri = {sorted(prod_top.items())}")


# ---------------------------------------------------------------------------
# (D) Test: A_p as SUM of s^*_lam * h_r^* for varying (lam, r)?
# Try:  Is A_p a POWER SUM in shifted schur, e.g., A_p = p_p^*?
# ---------------------------------------------------------------------------


def test_A_p_as_sum_of_pieri(coeffs, A_data, p, jj):
    """For a fixed (p, j), express A_p as sum_{lam0} c_lam0 * (s^*_lam0 * s^*_(p, 0)).
    Set up linear system across all mu."""
    print(f"\n  === p={p}, j={jj}: express A_p as sum of Pieri products (s^*_lam0 * h_p^*) ===")
    # Candidate lam0's: |lam0| = j (or j-1, j-2, ..., j-p).
    cands = []
    for L in range(jj - p, jj + 1):
        for a1 in range(0, L + 1):
            a2 = L - a1
            if a1 < a2:
                continue
            cands.append((a1, a2))
    if not cands:
        return
    # Compute Pieri expansions
    pieri = {}   # lam0 -> {mu: coeff}
    for lam0 in cands:
        try:
            pieri[lam0] = sahi_stanley_pieri_h(lam0, p)
        except Exception:
            continue
    # Set up linear system: for each mu with c_mu(A_p) != 0, sum_lam0 x_lam0 * pieri[lam0].get(mu, 0) = c_mu(A_p).
    all_mus = set()
    for lam0 in cands:
        if lam0 not in pieri:
            continue
        all_mus.update(pieri[lam0].keys())
    all_mus.update(coeffs[(p, jj)].keys())
    all_mus = sorted(all_mus)
    lam0s = [l for l in cands if l in pieri]
    if not lam0s or not all_mus:
        return
    M = sp.zeros(len(all_mus), len(lam0s))
    y = sp.zeros(len(all_mus), 1)
    for i, mu in enumerate(all_mus):
        y[i, 0] = coeffs[(p, jj)].get(mu, Integer(0))
        for j_, lam0 in enumerate(lam0s):
            M[i, j_] = pieri[lam0].get(mu, Integer(0))
    # Solve
    try:
        sol = M.solve(y)
        # Verify
        for i, mu in enumerate(all_mus):
            pred = sum(sol[j_] * pieri[lam0s[j_]].get(mu, Integer(0))
                       for j_ in range(len(lam0s)))
            if sp.simplify(pred - y[i]) != 0:
                raise ValueError("verify failed")
        # Print nonzero coeffs
        nz = [(lam0s[j_], sol[j_]) for j_ in range(len(lam0s)) if sol[j_] != 0]
        print(f"    A_p = sum_lam0 c_lam0 (s^*_lam0 * h_{p}^*), coeffs:")
        for lam0, cv in nz:
            print(f"      c_{lam0} = {cv}")
    except Exception as e:
        # Try least-squares (approximate) via pinv
        try:
            aug = M.row_join(y)
            _, pivots = aug.rref()
            print(f"    No exact solution. Rank(M) = {M.rank()}, rank(M|y) = {aug.rank()}")
        except Exception:
            print(f"    No solution found.")


# ---------------------------------------------------------------------------
# (E) Alternative: is A_p a linear comb of s^*_(a,b)*e_p^*?
# For 2 vars, e_p^* = s^*_(1^p) only makes sense for p <= 2.
# So this is a limited test.
# Instead, try: A_p = sum_lam0 c_lam0 (s^*_lam0 * s^*_(p, r)) for varying r
# for row-shape multipliers.
# ---------------------------------------------------------------------------


def test_A_p_as_sum_of_pieri_varied(coeffs, p, jj, max_r=None):
    """Same as above but for a family of multipliers: s^*_(p+r, r) for r=0..p."""
    if max_r is None:
        max_r = min(p, 2)
    print(f"\n  === p={p}, j={jj}: A_p = sum_(lam0, r) c * (s^*_lam0 * s^*_(p+r-r, r)) ===")
    all_mus_needed = set(coeffs[(p, jj)].keys())
    # Sizes we allow for the multiplier
    multipliers = []
    for r in range(0, max_r + 1):
        # Any shape (a1, a2) with a1+a2 = p+r... too many. Let's only do (p, 0)
        # and its close cousins.
        pass
    # Simpler: is A_p / (something fixed) a shifted schur function itself?
    # Since we have every c_lambda(j) as polynomial in j (from prior work),
    # we could also test if c_lam(j, p) equals sum of Pieri multiplier values.


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main():
    J = 10
    p_max = 4
    print("Building A_p tables and coeffs...")
    A_data, coeffs = build_all(J=J, p_max=p_max)
    print("...done")

    analyze_seeds(coeffs, p_max=p_max)
    test_catalan_seed(coeffs)

    print("\n" + "=" * 78)
    print("(B) TOP-LEVEL Pieri match testing")
    print("=" * 78)
    for (p, jj) in sorted(coeffs.keys()):
        if p > 4 or jj < 2 * p or jj > 8:
            continue
        test_pieri_h_all(coeffs, p, jj)

    print("\n" + "=" * 78)
    print("(D) FULL Pieri linear-combination test")
    print("=" * 78)
    for (p, jj) in sorted(coeffs.keys()):
        if p > 4 or jj < 2 * p or jj > 8:
            continue
        test_A_p_as_sum_of_pieri(coeffs, A_data, p, jj)

    print("\nDone.")


if __name__ == "__main__":
    main()
