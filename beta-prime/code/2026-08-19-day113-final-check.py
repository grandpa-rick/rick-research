"""Final sanity check: A_1(b,c,j) = j*(3-j)/2 * (b+c)^{↓j} + j*(b+1)*c*(b+c-2)^{↓(j-1)}"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational

a, b, c = symbols('a b c')
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


def main():
    J = 12
    print(f"Building tables & computing dsV up to j = {J}...")
    tables = bt(J)
    dsV = dsV_all(J, tables)

    print("\n" + "=" * 72)
    print("FINAL CHECK: A_1 = j*(3-j)/2 * (b+c)^{↓j} + j*(b+1)*c*(b+c-2)^{↓(j-1)}")
    print("=" * 72)

    all_ok = True
    for jj in range(1, J + 1):
        A1_actual = extract_A_p(jj, 1, dsV)

        # Formula
        term0 = Rational(jj * (3 - jj), 2) * fall(b + c, jj)
        term1 = jj * (b + 1) * c * fall(b + c - 2, jj - 1)
        A1_formula = expand(term0 + term1)

        diff = expand(A1_actual - A1_formula)
        status = "OK" if diff == 0 else f"FAIL diff = {diff}"
        print(f"  j = {jj}: {status}")
        if diff != 0:
            all_ok = False

    print()
    print(f"Clean-formula verification: {'PASS' if all_ok else 'FAIL'} for j = 1..{J}")


if __name__ == "__main__":
    main()
