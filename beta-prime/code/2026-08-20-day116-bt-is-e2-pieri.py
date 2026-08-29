"""Verify: bt(j) exactly computes the coefficients of e_2^j in the Schur basis
(in at most 3 variables, since bt truncates to len(mu) <= 3).

bt starts at the empty partition and repeatedly applies vs(): adds 1 to two DIFFERENT
positions of mu, keeping the result a partition (weakly decreasing), and keeps only
partitions with <= 3 parts.

"Add 1 to two different positions and remain a partition" is exactly Pieri's rule for
multiplication by e_2 = s_{(1,1)}: nu / mu is a vertical strip of size 2.

So bt(j) = (Pieri e_2)^j truncated to <= 3 rows = coefficients of e_2^j in the
Schur basis, in 3 variables.

Equivalently: kap_mu = [s_mu] (e_2^j) in the algebra of symmetric functions in 3 vars,
i.e., = K_{mu', (2^j)} by omega-duality (since omega(e_2^j) = h_2^j and K_{mu, nu}
counts SSYT of shape mu content nu; the transpose relates omega).

Actually: e_2^j = omega(h_2^j) = sum_mu K_{mu, (2^j)} omega(s_mu) = sum_mu K_{mu, (2^j)} s_{mu'}
                = sum_{lam} K_{lam', (2^j)} s_lam.

Hence kap_lam = K_{lam', (2^j)}. This proves the "kappa formula" without needing
verification.

This script verifies bt(j) matches the classical e_2-Pieri rule.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer


u_var, y_var, c = symbols('u y c')


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
    for jj in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
    return dict(cu)


def V_uyc():
    return (u_var - y_var) * (u_var - c) * (y_var - c)


def ord_schur(mu):
    """Ordinary Schur s_mu(u, y, c). mu tuple of 3 parts."""
    n = 3
    rows = [[(u_var, y_var, c)[i]**(mu[col] + n - 1 - col) for col in range(n)]
            for i in range(n)]
    num = det3(rows)
    V = V_uyc()
    q, r = sp.div(Poly(num, u_var, y_var, c), Poly(V, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def e2_pieri_expand(j_max):
    """Expand e_2^j in Schur polynomials (3 variables) by leading-monomial peel."""
    e2 = u_var * y_var + u_var * c + y_var * c
    results = {}
    for jj in range(j_max + 1):
        F = expand(e2 ** jj)
        expansion = {}
        while True:
            F = expand(F)
            if F == 0:
                break
            P = Poly(F, u_var, y_var, c)
            if P.total_degree() < 0:
                break
            leading = sorted(P.terms(), reverse=True)[0]
            monom, cf = leading
            mu = tuple(monom)
            if not (mu[0] >= mu[1] >= mu[2]):
                print(f"    !! non-partition leading monomial {mu} coef {cf}")
                break
            s_mu = ord_schur(mu)
            expansion[mu] = cf
            F = expand(F - cf * s_mu)
        results[jj] = expansion
    return results


def main():
    J_MAX = 8
    print(f"Computing bt(j) tables and (e_2)^j Schur expansions for j <= {J_MAX} ...\n")
    e2_expansions = e2_pieri_expand(J_MAX)
    for jj in range(J_MAX + 1):
        bt_j = bt(jj) if jj > 0 else {(): 1}
        # Normalize bt keys to 3-tuples
        bt_norm = {}
        for mu, k in bt_j.items():
            padded = tuple(list(mu) + [0] * (3 - len(mu)))
            bt_norm[padded] = k
        e2_j = e2_expansions[jj]
        all_mus = set(bt_norm.keys()) | set(e2_j.keys())
        ok = True
        for mu in sorted(all_mus, reverse=True):
            kb = bt_norm.get(mu, 0)
            ke = e2_j.get(mu, 0)
            if kb != ke:
                ok = False
                print(f"  j={jj}, mu={mu}: bt = {kb}, e2-Pieri = {ke}  MISMATCH")
        print(f"j={jj}: bt(j) == [s_mu]((e_2)^j) coefficients in 3 vars?  {'OK' if ok else 'FAIL'}"
              f"  (#nonzero: bt={len(bt_norm)}, e2={len(e2_j)})")


if __name__ == "__main__":
    main()
