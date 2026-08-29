"""Day 114 pieri hunt V3 -- catalan-shape seeds for p=1 confirmed, now
verify and try more.

Findings from V2:
 * Bottom-level "seeds" for A_1 at even j = 2k, m = 2i are proportional to
   the CATALAN TRIANGLE numbers T(2k, k, i) = binomial(2k, k+i) - binomial(2k, k+i+1).
 * Global multiplier g(k) = k*(2k-3) for k >= 2.  I.e.,
       c_{lambda=(k+i, k-i)}^{seed} = -k(2k-3) * (binom(2k, k+i) - binom(2k, k+i+1))
   for A_1, j = 2k, i = 0, 1, ..., k.

Plan for V3:
 (1) Verify the seed formula for p=1 across all j.
 (2) Also fit odd-j seed formula for p=1.
 (3) Attempt A_p = sum over lam0 c_lam0 * s^*_lam0 * (SUMMED over r <= p of
     multipliers h_r or e_r).  In particular:
       A_p = sum_{lam0, r} c_{lam0, r} (s^*_lam0 * h_r^*)
     with |lam0| + r fixed to something.

 (4) Also test: A_p = h_p^* * F_p, F_p to be determined?

 (5) Absolute killer: express A_p as linear combination of PAIRS
     (s^*_lam1 * s^*_lam2) with lam1 * lam2 ranging.  This is basically
     "expand A_p in the Sym ⊗ Sym basis and see if it becomes an operator
     of low rank".

Author: Rick, 3am, second bottle.
"""

from collections import defaultdict
from itertools import combinations, product

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
# (1) Verify p=1 seed formula.
# ---------------------------------------------------------------------------


def T_catalan(n, k):
    """Catalan triangle T(n, k) = binom(n, k) - binom(n, k-1). Valid for 0 <= k <= n."""
    if k < 0:
        return Integer(0)
    if k > n:
        return Integer(0)
    return binomial(n, k) - binomial(n, k - 1)


def verify_p1_seeds(coeffs):
    print("=" * 78)
    print("(1) VERIFYING p=1 seed formula.")
    print("    Conjecture (even j = 2k):")
    print("      c_{lam=(k+i, k-i)}(seed) = -k(2k-3) * T_catalan(2k, k+i)")
    print("    where T_catalan(n, r) = binom(n, r) - binom(n, r-1).")
    print("=" * 78)
    p = 1
    ok = True
    for jj in sorted(k[1] for k in coeffs if k[0] == p):
        if jj % 2 != 0:
            continue
        k = jj // 2
        print(f"\n  j = {jj} (k = {k}):")
        for i in range(k + 1):
            m = 2 * i
            lam = ((jj + m) // 2, (jj - m) // 2)
            actual = coeffs[(p, jj)].get(lam, Integer(0))
            pred_multiplier = -k * (2 * k - 3)
            pred = pred_multiplier * T_catalan(2 * k, k + i)
            match = actual == pred
            print(f"    lam={lam}, i={i}: actual={actual}, predicted={pred} => {'OK' if match else 'FAIL'}")
            if not match:
                ok = False
    print(f"\n  Even-j formula OK? {ok}")

    # Odd-j fit
    print("\n  Odd-j (j = 2k+1): m = 1, 3, ..., 2k+1  (i = 0, ..., k)")
    print("    seeds are: j=1: [1]; j=3: [0]; j=5: [-25, -20, -5]; j=7: [-196, -196, -84, -14]; j=9: [-1134, -1296, -729, -216, -27]")
    print("    Ratios: seed/[T(2k+1, k+i+1) - T(2k+1, k+i+2)]?")
    for jj in sorted(k_[1] for k_ in coeffs if k_[0] == p):
        if jj % 2 == 0:
            continue
        k = (jj - 1) // 2
        seeds = []
        for i in range(k + 1):
            m = 2 * i + 1
            lam = ((jj + m) // 2, (jj - m) // 2)
            seeds.append(coeffs[(p, jj)].get(lam, Integer(0)))
        # Try: seed(i) proportional to T(2k+1, k+i+1)
        cands_row = [T_catalan(jj, k + i + 1) for i in range(k + 1)]
        ratios = []
        for i in range(k + 1):
            if cands_row[i] == 0:
                if seeds[i] != 0:
                    ratios.append(None)
                    continue
                ratios.append('0/0')
            else:
                ratios.append(sp.Rational(seeds[i], cands_row[i]))
        print(f"    j={jj}: seeds = {[int(s) for s in seeds]}")
        print(f"           T(2k+1, k+i+1) = {[int(c) for c in cands_row]}  (i=0..{k})")
        print(f"           ratios = {ratios}")


# ---------------------------------------------------------------------------
# (2) Even-j seeds for higher p: hunt for Catalan-like structure.
# ---------------------------------------------------------------------------


def hunt_seeds_higher_p(coeffs):
    print("=" * 78)
    print("(2) Higher-p seeds: is the ratio seed / T_catalan a low-degree poly?")
    print("=" * 78)
    for p in range(2, 5):
        print(f"\n  --- p = {p} ---")
        for jj in sorted(k_[1] for k_ in coeffs if k_[0] == p):
            if jj % 2 != 0:
                continue
            k = jj // 2
            seeds = []
            cats = []
            for i in range(k + 1):
                m = 2 * i
                lam = ((jj + m) // 2, (jj - m) // 2)
                seeds.append(coeffs[(p, jj)].get(lam, Integer(0)))
                cats.append(T_catalan(2 * k, k + i))
            ratios = []
            for s, c in zip(seeds, cats):
                if c == 0:
                    ratios.append('0/0' if s == 0 else 'NaN')
                else:
                    ratios.append(sp.Rational(s, c))
            print(f"    j={jj} (k={k}): seeds={[int(s) for s in seeds]}")
            print(f"                   T(2k, k+i)={[int(c) for c in cats]}")
            print(f"                   ratios={ratios}")


# ---------------------------------------------------------------------------
# (3) Test A_p = sum_{lam0, r} c_{lam0, r} (s^*_lam0 * h_r^*)
#     with h_r^* := s^*_{(r, 0)}, r ranging 0..p.
# ---------------------------------------------------------------------------


def sahi_stanley_h(lam0, r):
    prod = sp.expand(s_star(lam0, b, c) * s_star((r, 0), b, c))
    if prod == 0:
        return {}
    P = sp.Poly(prod, b, c)
    db, dc = P.degree(b), P.degree(c)
    D_max = db + dc + 1
    cf, res = shifted_schur_expand(prod, D_max)
    assert sp.expand(res) == 0
    return {mu: v for mu, v in cf.items() if v != 0}


def test_pieri_sum_variable_r(coeffs, p, jj):
    """Solve A_p(j) = sum_{lam0, r >= 0} c_{lam0, r} (s^*_lam0 * h_r^*)
    with |lam0| + r ranging from j to j+p (matching the support of A_p).
    """
    print(f"\n  === p={p}, j={jj}: A_p = sum c_{{lam0, r}} (s^*_lam0 * h_r^*) ===")
    # Enumerate candidate (lam0, r)
    cands = []
    for L in range(0, jj + p + 1):  # |lam0|
        for a1 in range(L + 1):
            a2 = L - a1
            if a1 < a2 or a2 < 0:
                continue
            lam0 = (a1, a2)
            for r in range(0, jj + p - L + 1):
                if L + r > jj + p:
                    continue
                # Require the product to be non-trivial: r >= 0.
                cands.append((lam0, r))
    # Filter reasonable ones (we want small pieri expansions -- keep |lam0| <= j + p and r <= p+j).
    # Compute pieri expansions
    pieri = {}
    for (lam0, r) in cands:
        try:
            pieri[(lam0, r)] = sahi_stanley_h(lam0, r)
        except Exception:
            continue
    # Build linear system: rows indexed by mu appearing anywhere.
    all_mus = set()
    for (lam0, r), pd in pieri.items():
        all_mus.update(pd.keys())
    all_mus.update(coeffs[(p, jj)].keys())
    all_mus = sorted(all_mus)
    keys = list(pieri.keys())
    M = sp.zeros(len(all_mus), len(keys))
    y = sp.zeros(len(all_mus), 1)
    for i, mu in enumerate(all_mus):
        y[i, 0] = coeffs[(p, jj)].get(mu, Integer(0))
        for jc, k in enumerate(keys):
            M[i, jc] = pieri[k].get(mu, Integer(0))
    aug = M.row_join(y)
    r_M = M.rank()
    r_aug = aug.rank()
    if r_M == r_aug:
        print(f"    Consistent! rank = {r_M}, unknowns = {len(keys)}")
        # Since typically underdetermined, get a solution.
        try:
            x = M.gauss_jordan_solve(y)[0]  # returns (particular_soln, free_params)
            # x is a Matrix
            nz = []
            for j_ in range(len(keys)):
                # x[j_] may contain free params; substitute them to 0 to get one solution
                val = x[j_].subs({s: 0 for s in x[j_].free_symbols})
                if sp.simplify(val) != 0:
                    nz.append((keys[j_], val))
            print(f"    Particular solution (with free params set to 0):")
            for (lam0, r), cv in nz:
                print(f"      c_{{lam0={lam0}, r={r}}} = {cv}")
        except Exception as e:
            print(f"    gauss_jordan_solve failed: {e}")
    else:
        print(f"    INCONSISTENT: rank(M)={r_M}, rank(M|y)={r_aug}, unknowns={len(keys)}")


# ---------------------------------------------------------------------------
# (4) Test: A_p = s^*_lam0 * P where P is a polynomial (in b, c) of degree
# p that we solve for.
# ---------------------------------------------------------------------------


def test_ap_factor(A_data, p, jj):
    """Is A_p(b, c; j) = s^*_{lam0}(b, c) * P(b, c) for some lam0 (of small
    total degree)?  For each candidate lam0 (with |lam0| <= j), try polynomial
    division.  If the remainder is zero, we've factored A_p."""
    A = A_data.get((p, jj), Integer(0))
    if A == 0:
        return
    print(f"\n  === p={p}, j={jj}: testing A_p / s^*_lam0 for various lam0 ===")
    for L in range(0, jj + 1):
        for a1 in range(L + 1):
            a2 = L - a1
            if a1 < a2 or a2 < 0:
                continue
            lam0 = (a1, a2)
            S = s_star(lam0, b, c)
            if S == 0:
                continue
            try:
                q, r = sp.div(sp.Poly(A, b, c), sp.Poly(S, b, c))
                if r.as_expr() == 0:
                    print(f"    lam0={lam0}: DIVIDES!  quotient = {sp.factor(q.as_expr())}")
            except Exception:
                pass


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main():
    J = 10
    p_max = 4
    print("Building A_p tables and coeffs...")
    A_data, coeffs = build_all(J=J, p_max=p_max)
    print("...done")

    verify_p1_seeds(coeffs)
    hunt_seeds_higher_p(coeffs)

    print("\n" + "=" * 78)
    print("(3) FULL Pieri-sum (variable r) test")
    print("=" * 78)
    for (p, jj) in sorted(coeffs.keys()):
        if p > 2 or jj > 6:
            continue
        test_pieri_sum_variable_r(coeffs, p, jj)

    print("\n" + "=" * 78)
    print("(4) A_p / s^*_lam0 factorization")
    print("=" * 78)
    for (p, jj) in sorted(A_data.keys()):
        if p > 2 or jj > 6:
            continue
        test_ap_factor(A_data, p, jj)

    print("\nDone.")


if __name__ == "__main__":
    main()
