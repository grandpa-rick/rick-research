"""Rank-drop investigation at a = k-2 (equivalently y_1 = k) for k = 1, 2, 3.

Computes (ds_j/V)|_{a=k-2} for k in {1,2,3}, j in {0..8}, and factors.
Also checks a<->b symmetry (b = k-1, i.e., y_2 = k) gives the same result.

Then computes Q_{2R}(k-2, b, c) for R=2,3 at concrete c values, reporting
the b-degree and (factored) coefficients.
"""
from collections import defaultdict
from itertools import combinations
import sympy as sp
from sympy import symbols, expand, factor, Poly, simplify, Integer, cancel


# ------------------------------------------------------------------
# Machinery (copied from 2026-08-18-lemma1-verify.py)
# ------------------------------------------------------------------
def bt(M):
    def vs(mu):
        L = len(mu) + 2
        b = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = b.copy()
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
    for j in range(1, M + 1):
        nx = defaultdict(int)
        for mu, c in cu.items():
            for nu in vs(mu):
                nx[nu] += c
        cu = nx
        rs = []
        for mu, c in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, c))
        T[j] = rs
    return T


def fall(x, k):
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def rise(x, L):
    p = Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def ds(a, b, c, j, T):
    y = (a + 2, b + 1, c)
    tot = Integer(0)
    for mu, kk in T[j]:
        ks = [mu[i] + (2 - i) for i in range(3)]
        M = [[fall(y[i], ks[l]) for l in range(3)] for i in range(3)]
        d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
             - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
             + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        tot += kk * d
    return expand(tot)


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def main():
    a, b, c = symbols('a b c')
    JMAX = 8
    T = bt(JMAX)
    V = (a - b + 1) * (a - c + 2) * (b - c + 1)

    # Precompute q_j = ds_j / V for j = 0..JMAX
    P("=" * 78)
    P("Precomputing q_j = ds_j / V for j = 0..%d" % JMAX)
    P("=" * 78)
    Q = {}
    for j in range(JMAX + 1):
        d = ds(a, b, c, j, T)
        q, r = Poly(d, a, b, c).div(Poly(V, a, b, c))
        assert r.as_expr() == 0, f"ds_{j} not divisible by V!"
        Q[j] = expand(q.as_expr())
        P(f"  j = {j}: ds_j / V computed, deg = {Poly(Q[j], a, b, c).total_degree()}")

    # ------------------------------------------------------------------
    # (1) (ds_j/V)|_{a = k-2} for k in {1,2,3}, j in {0..8}
    # ------------------------------------------------------------------
    P("")
    P("=" * 78)
    P("PART 1: (ds_j / V)|_{a = k-2} for k = 1, 2, 3 and j = 0..%d" % JMAX)
    P("=" * 78)
    results_a = {}
    for k in [1, 2, 3]:
        P("")
        P(f"--- k = {k}  (a = {k-2}, y_1 = {k}) ---")
        for j in range(JMAX + 1):
            qk = expand(Q[j].subs(a, k - 2))
            fk = factor(qk)
            results_a[(k, j)] = fk
            P(f"k = {k}, j = {j}: (ds_j/V)|_{{a={k-2}}} = {fk}")

    # ------------------------------------------------------------------
    # (2) (ds_j/V)|_{b = k-1} — should match by y_1<->y_2 symmetry
    # ------------------------------------------------------------------
    P("")
    P("=" * 78)
    P("PART 2: (ds_j / V)|_{b = k-1} — expect y_1<->y_2 symmetric equality")
    P("=" * 78)
    # The symmetry: y_1 = a+2 and y_2 = b+1. ds_j (a determinant with rows
    # indexed by y_i) is antisymmetric under row swap; V is also antisymmetric.
    # So ds_j/V is SYMMETRIC under (y_1 <-> y_2), i.e., under
    #    (a+2, b+1) <-> (b+1, a+2)   equivalently   a <-> b-1  (and b <-> a+1)
    # Setting y_1 = k (a = k-2) leaves ds_j/V(k-2, b, c) as function of b, c.
    # Setting y_2 = k (b = k-1) leaves ds_j/V(a, k-1, c) as function of a, c.
    # The symmetry says: substituting b -> b-1... more carefully:
    # ds_j/V(a, b, c) = ds_j/V(b-1, a+1, c) under y_1<->y_2 swap.
    # So (ds_j/V)|_{b=k-1}(a, c) = ds_j/V(a, k-1, c) = ds_j/V(k-2, a+1, c)
    #                            = [ (ds_j/V)|_{a=k-2} ] with b -> a+1.
    for k in [1, 2, 3]:
        P("")
        P(f"--- k = {k}  (b = {k-1}, y_2 = {k}) ---")
        for j in range(JMAX + 1):
            # Evaluate at b = k-1: result is polynomial in (a, c).
            qkb = expand(Q[j].subs(b, k - 1))
            fkb = factor(qkb)
            # Reference: take Part 1 result (poly in b,c) and substitute b -> a+1
            ref = results_a[(k, j)]
            ref_renamed = expand(ref.subs(b, a + 1))
            diff = expand(qkb - ref_renamed)
            match = (diff == 0)
            P(f"k = {k}, j = {j}: (ds_j/V)|_{{b={k-1}}} = {fkb}    match(y_1<->y_2 sym) = {match}")

    # ------------------------------------------------------------------
    # (3) Q_{2R}(k-2, b, c) for R = 2, 3; k = 1, 2; concrete c values
    # ------------------------------------------------------------------
    P("")
    P("=" * 78)
    P("PART 3: Q_{2R}(a=k-2, b, c) at concrete c values")
    P("=" * 78)
    P("Q_{2R} = h_{2R} / [(a+3)_{c-1-2R} * (b+2)_{c-1-2R}]")
    P("h_{2R} = sum_{j=0}^{2R} (-1)^{2R-j} C(2R,j) * H_c(a,b,j)")
    P("H_c(a,b,j) = (a+3)_{c-j-1} * (b+2)_{c-j-1} * (ds_j/V)")
    P("")
    P("Note: adjusting per user's task spec:")
    P("H_c(a,b,j) = (a+3)_{c-j-1} * (b+2)_{c-j-1} * (ds_j/V)")
    P("")

    def H_c_expr_at_cval(j_val, c_val, a_val, ab_symbol_b):
        """Compute H_c(a=a_val, b, j) at concrete integer c=c_val, symbolic b.

        H_c(a,b,j) = (a+3)_{c-j-1} * (b+2)_{c-j-1} * (ds_j/V)
        Substituting a=a_val and c=c_val (integers), returns a poly in b.
        """
        L = c_val - j_val - 1
        if L < 0:
            raise ValueError(f"Pochhammer length negative: c={c_val}, j={j_val}")
        poch_a = rise(sp.Integer(a_val) + 3, L)  # concrete integer
        poch_b = rise(ab_symbol_b + 2, L)
        qj_at = expand(Q[j_val].subs({a: a_val, c: c_val}))
        return expand(poch_a * poch_b * qj_at)

    for R in [2, 3]:
        twoR = 2 * R
        P("")
        P("=" * 60)
        P(f"R = {R}, 2R = {twoR}")
        P("=" * 60)
        for k in [1, 2]:
            a_val = k - 2
            P("")
            P(f"  --- k = {k}, a = {a_val} ---")
            # c values: 2R+2, 2R+3, ..., 2R+6
            for cv in range(twoR + 2, twoR + 7):
                # h_{2R}(a=a_val, b, c=cv)
                h2R = Integer(0)
                for jj in range(twoR + 1):
                    coef = ((-1) ** (twoR - jj)) * sp.binomial(twoR, jj)
                    Hj = H_c_expr_at_cval(jj, cv, a_val, b)
                    h2R += coef * Hj
                h2R = expand(h2R)
                # Denominator: (a+3)_{c-1-2R} * (b+2)_{c-1-2R} at a=a_val, c=cv
                L = cv - 1 - twoR
                if L < 0:
                    P(f"    c = {cv}: L = c-1-2R = {L} < 0, skip")
                    continue
                poch_a_val = rise(sp.Integer(a_val) + 3, L)  # concrete number
                poch_b_expr = rise(b + 2, L)
                denom = expand(poch_a_val * poch_b_expr)

                # Divide h2R (poly in b) by denom (poly in b)
                if L == 0:
                    # denom = 1, Q = h2R
                    Qexpr = h2R
                    rem_expr = Integer(0)
                else:
                    q_poly, r_poly = sp.div(Poly(h2R, b), Poly(denom, b))
                    Qexpr = q_poly.as_expr()
                    rem_expr = r_poly.as_expr()

                # Report b-degree and coefficients
                if Qexpr == 0:
                    P(f"    c = {cv}: Q_{{{twoR}}}(a={a_val}, b, {cv}) = 0, rem = {rem_expr}")
                    continue
                Qpoly = Poly(Qexpr, b)
                bdeg = Qpoly.degree()
                P(f"    c = {cv}: b-degree = {bdeg}, remainder = {rem_expr}")
                for i in range(bdeg + 1):
                    cf = Qpoly.nth(i)
                    if cf != 0:
                        P(f"      b^{i}: {factor(cf)}")

    # Save
    with open('/home/agent/projects/beta-prime/code/2026-08-18-rank-drop-yk.txt', 'w') as f:
        f.write('\n'.join(OUT))
    P("")
    P("Saved to 2026-08-18-rank-drop-yk.txt")


if __name__ == "__main__":
    main()
