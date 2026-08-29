"""Day 116: Attack A — Pieri realization for A_p.

Goal: test whether A_p = h^*_p . A_0 in the Okounkov-Olshanski shifted-Schur
algebra, where A_0 = (b+c)^{↓j} is Rick's Slice-0 base.

Formal object: in Λ*(y_2, y_3) (2-variable shifted-symmetric functions),
we have:
  * A_0(j) := (b+c)^{↓j}. In shifted-Schur basis, A_0 = sum_{|μ|=j} kappa_μ · s^*_μ.
    (Verified: A_0 = (b+c)^{↓j} = sum over μ = 2-part partitions of j of the
     s^*_{μ_2,μ_3} coefficients coming from ds_j.)
  * h^*_p := shifted homogeneous = s^*_{(p)} in 2 vars (Okounkov shifted).
  * . = ordinary polynomial multiplication in Λ*.

If A_p = A_0 · h^*_p as symmetric polynomials in (b, c), we're done (deg_π
of h^*_p = ⌊p/2⌋ ... hmm, actually needs checking; but deg_b h^*_p ≤ p+1).

Actually the cleanest statement: expand A_0 · h^*_p in shifted-Schur basis via
Sahi-Stanley Pieri rule and compare to A_p's shifted-Schur expansion.

Author: Day 116 attack A verify.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, Integer, Rational, Poly, expand, factor, simplify

# ---------------------------------------------------------------------------
# Base machinery (copied from day114-Ap-shifted-schur-direct.py).
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


# --- shifted h^*_p in 2 variables ---
# Okounkov's h^*_p is a specific shifted-symmetric function. In 2 vars, one
# convenient realization: h^*_p := s^*_{(p, 0)}. This is NOT the same as
# "sum of monomials" because shifted-schur are non-homogeneous.

def h_star(p_val, x1, x2):
    """Shifted homogeneous h^*_p := s^*_{(p)} = s^*_{(p, 0)}."""
    if p_val == 0:
        return Integer(1)
    return s_star((p_val, 0), x1, x2)


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main():
    J = 10
    p_max = 4

    print("=" * 78)
    print("Day 116 -- Attack A: A_p =? h^*_p * A_0 for A_0 = (b+c)^{↓j}.")
    print("=" * 78)

    print(f"\nBuilding S_j, A_p tables up to j = {J}...")
    tables = bt(J)
    dsV = dsV_all(J, tables)

    A_data = {}   # (p, jj) -> A_p(b, c, j)
    for p in range(0, p_max + 1):
        for jj in range(max(1, p), J + 1):
            A_data[(p, jj)] = extract_A_p(jj, p, dsV)

    # -----------------------------------------------------------------
    # STEP 1: Verify A_0 = (b+c)^{↓j}.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 1: Verify A_0(b, c, j) = (b + c)^{↓j}.")
    print("=" * 78)
    for jj in range(0, J + 1):
        A0 = A_data.get((0, jj), Integer(0))
        expected = fall(b + c, jj)
        diff = sp.expand(A0 - expected)
        status = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  j = {jj}: A_0 = (b+c)^{{↓j}}? {status}")

    # -----------------------------------------------------------------
    # STEP 2: Compute A_0 * h^*_p and compare to A_p (as polynomials
    #         in (b, c)).
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 2: Compare A_p vs h^*_p * A_0 (as polynomials in b, c).")
    print("=" * 78)

    for p in range(1, p_max + 1):
        print(f"\n--- p = {p} ---")
        hp = h_star(p, b, c)
        print(f"  h^*_{p}(b, c) = {sp.factor(sp.expand(hp))}")
        for jj in range(max(1, p), J + 1):
            A_p_val = A_data[(p, jj)]
            A_0_val = A_data[(0, jj)]
            product = sp.expand(A_0_val * hp)
            diff = sp.expand(A_p_val - product)
            if diff == 0:
                print(f"  j={jj}: A_p == h^*_p * A_0 EXACTLY.")
            else:
                # Ratio test?
                # deg
                Pd = sp.Poly(diff, b, c)
                # Try constant multiplier
                # A_p = c * h_p * A_0 ?
                # At (b,c)=(0,0): A_p(0,0,j) vs h^*_p(0,0)*A_0(0,0,j)
                # But A_0(0,0,j) = j! * (-1)^{something}... Let's try
                # different specialisations.
                # First check: is A_p / (h^*_p * A_0) a rational function?
                try:
                    q_num, q_den = sp.together(A_p_val / product).as_numer_denom()
                    q_num = sp.expand(q_num)
                    q_den = sp.expand(q_den)
                    if q_den != 0 and sp.gcd(q_num, q_den) == q_den:
                        # polynomial
                        Q = sp.simplify(q_num / q_den)
                        print(f"  j={jj}: A_p / (h_p * A_0) = {sp.factor(Q)}")
                    else:
                        # Try to see if divisible
                        try:
                            qq, rr = sp.div(sp.Poly(A_p_val, b, c),
                                            sp.Poly(product, b, c))
                            if rr.as_expr() == 0:
                                print(f"  j={jj}: A_p = h_p*A_0 * ({sp.factor(qq.as_expr())})")
                            else:
                                print(f"  j={jj}: A_p != c * h_p*A_0. "
                                      f"deg(diff)_{{b,c}} = ({Pd.degree(b)}, {Pd.degree(c)}).")
                        except Exception:
                            print(f"  j={jj}: no polynomial quotient, "
                                  f"deg(diff)_{{b,c}} = ({Pd.degree(b)}, {Pd.degree(c)}).")
                except Exception as e:
                    print(f"  j={jj}: ratio failed: {e}. diff nonzero.")

    # -----------------------------------------------------------------
    # STEP 3: Try broader Pieri-type ansatz.
    # A_p = sum_{r=0}^{p} c_{p,r}(j) * h^*_r * A_0 * (some other factor?)
    # Or: A_p = (something linear in shifted-Schur) * A_0.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3: Test A_p = P_p(b,c,j) * A_0 for polynomial P_p in (b, c, j).")
    print("        If yes, factor out A_0 and study P_p.")
    print("=" * 78)

    for p in range(1, p_max + 1):
        print(f"\n--- p = {p} ---")
        for jj in range(max(1, p), J + 1):
            A_p_val = A_data[(p, jj)]
            A_0_val = A_data[(0, jj)]
            if A_0_val == 0:
                continue
            try:
                qq, rr = sp.div(sp.Poly(A_p_val, b, c),
                                sp.Poly(A_0_val, b, c))
                if rr.as_expr() == 0:
                    P = qq.as_expr()
                    Pd = sp.Poly(P, b, c)
                    print(f"  j={jj}: A_p / A_0 = polynomial of deg (b,c) = "
                          f"({Pd.degree(b)}, {Pd.degree(c)}) = {sp.factor(P)}")
                else:
                    print(f"  j={jj}: A_p not divisible by A_0. "
                          f"remainder nonzero.")
            except Exception as e:
                print(f"  j={jj}: division failed: {e}")

    # -----------------------------------------------------------------
    # STEP 4: Compare shifted-Schur expansion of h^*_p*A_0 vs A_p.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 4: Expand h^*_p * A_0 in shifted-Schur basis; compare to A_p.")
    print("=" * 78)

    for p in range(1, p_max + 1):
        print(f"\n--- p = {p} ---")
        hp = h_star(p, b, c)
        for jj in range(max(1, p), min(J, 8) + 1):
            A_0_val = A_data[(0, jj)]
            product = sp.expand(A_0_val * hp)
            A_p_val = A_data[(p, jj)]

            # Expand both in shifted-Schur
            db_prod = sp.Poly(product, b, c).degree(b) if product != 0 else 0
            dc_prod = sp.Poly(product, b, c).degree(c) if product != 0 else 0
            D_max_prod = db_prod + dc_prod + 1
            cf_prod, res_prod = shifted_schur_expand(product, D_max_prod)
            assert sp.expand(res_prod) == 0, "h^*_p*A_0 expansion has residual"
            nz_prod = {lam: v for lam, v in cf_prod.items() if v != 0}

            db_ap = sp.Poly(A_p_val, b, c).degree(b) if A_p_val != 0 else 0
            dc_ap = sp.Poly(A_p_val, b, c).degree(c) if A_p_val != 0 else 0
            D_max_ap = db_ap + dc_ap + 1
            cf_ap, res_ap = shifted_schur_expand(A_p_val, D_max_ap)
            assert sp.expand(res_ap) == 0, "A_p expansion has residual"
            nz_ap = {lam: v for lam, v in cf_ap.items() if v != 0}

            print(f"\n  j={jj}:")
            print(f"    A_p support: {sorted(nz_ap.keys(), key=lambda l:(l[0]+l[1], l[0]))[:6]}...")
            print(f"    h^*_p*A_0 support: {sorted(nz_prod.keys(), key=lambda l:(l[0]+l[1], l[0]))[:6]}...")
            # Difference
            all_lams = set(nz_prod.keys()) | set(nz_ap.keys())
            diffs = {}
            for lam in all_lams:
                d = sp.simplify(nz_ap.get(lam, Integer(0)) - nz_prod.get(lam, Integer(0)))
                if d != 0:
                    diffs[lam] = d
            if not diffs:
                print(f"    EXACT MATCH: A_p == h^*_p * A_0.")
            else:
                print(f"    DIFFERENCE (A_p - h^*_p * A_0):")
                for lam in sorted(diffs.keys(), key=lambda l:(l[0]+l[1], l[0])):
                    print(f"      lam={lam}: coeff = {diffs[lam]}")

    print("\n" + "=" * 78)
    print("Done.")
    print("=" * 78)


if __name__ == "__main__":
    main()
