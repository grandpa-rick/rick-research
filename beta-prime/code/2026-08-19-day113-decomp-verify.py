"""Day 113 Lemma 1 proof — verify decomposition:
    A_1 = alpha * A_0 - s*_{(j+1, 0)}(y_2, y_3) + B
where:
    A_1 = [a^{j-1}] S_j(a, b, c),
    A_0 = [a^j] S_j(a, b, c) = sum_{mu, mu_1=j} kappa_mu * s*_{(m_2, m_3)}(y_2, y_3),
    B   = sum_{mu, mu_1=j-1} kappa_mu * s*_{(m_2, m_3)}(y_2, y_3),
    alpha = b + c - binomial(j, 2),
    y_2 = b + 1, y_3 = c.

Verify for j = 1..8. Also print B in factored form to seek a pattern.
"""

import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, simplify

a, b, c = symbols('a b c')
y2, y3 = b + 1, c
u = a + 2


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


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
    xs = (u, y2, y3)
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


def s_star_two_var(a_p, b_p, z1, z2):
    """s*_{(a_p, b_p)}(z1, z2) for a_p >= b_p >= 0."""
    if a_p < b_p:
        return Integer(0)
    num = fall(z1, a_p + 1) * fall(z2, b_p) - fall(z2, a_p + 1) * fall(z1, b_p)
    denom = z1 - z2
    q, r = sp.div(Poly(num, [b, c]), Poly(denom, [b, c]))
    assert r.as_expr() == 0
    return q.as_expr()


def compute_A0(jj, tables):
    """A_0 = sum_{mu, mu_1=j} kappa * s*_{(m_2, m_3)}(y_2, y_3)."""
    result = Integer(0)
    for mu, kap in tables[jj]:
        if mu[0] == jj:
            m2, m3 = mu[1], mu[2]
            result += kap * s_star_two_var(m2, m3, y2, y3)
    return expand(result)


def compute_B(jj, tables):
    """B = sum_{mu, mu_1=j-1} kappa * s*_{(m_2, m_3)}(y_2, y_3)."""
    result = Integer(0)
    for mu, kap in tables[jj]:
        if mu[0] == jj - 1:
            m2, m3 = mu[1], mu[2]
            result += kap * s_star_two_var(m2, m3, y2, y3)
    return expand(result)


def main():
    J = 8
    print(f"Building tables up to j={J}...")
    tables = bt(J)
    print("Computing ds_j/V symbolically...")
    dsV = dsV_all(J, tables)

    print("\n" + "=" * 72)
    print("DECOMPOSITION VERIFICATION: A_1 = alpha*A_0 - s*_{(j+1,0)} + B")
    print("=" * 72)

    for jj in range(1, J + 1):
        A1_actual = extract_A_p(jj, 1, dsV)
        A0 = compute_A0(jj, tables)
        # A0 should equal (b+c)^{↓j} — check
        A0_expected = fall(b + c, jj)
        A0_check = "OK" if sp.simplify(A0 - A0_expected) == 0 else "FAIL"

        alpha = b + c - Integer(comb(jj, 2))
        s_j1_0 = s_star_two_var(jj + 1, 0, y2, y3)
        B = compute_B(jj, tables)

        A1_pred = expand(alpha * A0 - s_j1_0 + B)
        diff = expand(A1_actual - A1_pred)
        status = "OK" if diff == 0 else f"FAIL diff = {diff}"

        print(f"\n  j = {jj}: A_0 formula check = {A0_check}, decomposition = {status}")
        print(f"    A_1 (actual)     = {sp.factor(A1_actual)}")
        print(f"    B                = {sp.factor(B)}")

    print("\n" + "=" * 72)
    print("B AS FUNCTION OF j: try to fit a closed form")
    print("=" * 72)
    Bs = {}
    for jj in range(1, J + 1):
        Bs[jj] = compute_B(jj, tables)
    for jj in sorted(Bs.keys()):
        print(f"  j = {jj}: B = {sp.factor(Bs[jj])}")


if __name__ == "__main__":
    main()
