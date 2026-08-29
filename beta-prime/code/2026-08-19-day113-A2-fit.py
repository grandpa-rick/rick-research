"""Fit A_2 as: sum_{k=0}^{2} c_k(j) * pi^k * (sigma - 1 - 2k)^{↓(j - 2k)}
Test that c_k(j) are polynomials in j of degree ≤ 4.

Basis:
  k=0: (sigma-1)^{↓j} = (b+c)^{↓j}
  k=1: pi * (sigma-3)^{↓(j-1)} = (b+1)*c * (b+c-2)^{↓(j-1)}
  k=2: pi^2 * (sigma-5)^{↓(j-3)} = ((b+1)*c)^2 * (b+c-4)^{↓(j-3)}
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational

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


def basis_element(k, jj):
    """pi^k * (sigma - 1 - 2k)^{↓(j - 2k)} = ((b+1)*c)^k * (b + c - 2k)^{↓(j - 2k)}"""
    pi = (b + 1) * c
    m = b + c - 2 * k
    L = jj - 2 * k
    if L < 0:
        return None
    fac = Integer(1)
    for i in range(L):
        fac *= (m - i)
    return expand(pi**k * fac)


def try_fit_A2(dsV_cache, J):
    """For each j from 4..J, extract A_2 and try to decompose as
       c_0 * B_0(j) + c_1 * B_1(j) + c_2 * B_2(j)
       where B_k(j) = pi^k * (sigma - 1 - 2k)^{↓(j - 2k)}.
    """
    results = {}
    for jj in range(4, J + 1):
        A2 = extract_A_p(jj, 2, dsV_cache)
        B0 = basis_element(0, jj)
        B1 = basis_element(1, jj)
        B2 = basis_element(2, jj)
        if B2 is None:
            continue
        # Solve A2 = c0*B0 + c1*B1 + c2*B2
        c0, c1, c2 = symbols('c0 c1 c2')
        expr = c0*B0 + c1*B1 + c2*B2 - A2
        expr = expand(expr)
        # Coefficient of each (b, c)-monomial must be 0
        P = Poly(expr, b, c)
        eqs = []
        for monom, cf in P.terms():
            eqs.append(cf)
        sol = sp.solve(eqs, (c0, c1, c2), dict=True)
        if not sol:
            print(f"  j = {jj}: NO SOLUTION (A_2 does not fit basis)")
            continue
        s = sol[0]
        # Verify solution
        pred = expand(s[c0]*B0 + s[c1]*B1 + s[c2]*B2)
        diff = expand(pred - A2)
        if diff != 0:
            print(f"  j = {jj}: PARTIAL - diff = {diff}")
            continue
        results[jj] = (s[c0], s[c1], s[c2])
        print(f"  j = {jj}: c_0 = {sp.factor(s[c0])}, c_1 = {sp.factor(s[c1])}, c_2 = {sp.factor(s[c2])}")
    return results


def fit_j_poly(samples, name):
    """Given [(j, val), ...], fit polynomial in j of minimal degree."""
    j_sym = symbols('j')
    n = len(samples)
    for D in range(n):
        rows = []
        yy = []
        for (jv, yv) in samples[:D + 1]:
            rows.append([Rational(jv) ** i for i in range(D + 1)])
            yy.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        try:
            sol = M.solve(y)
        except:
            continue
        ok = True
        for (jv, yv) in samples[D + 1:]:
            pred = sum(sol[i] * jv ** i for i in range(D + 1))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            poly = sum(sol[i] * j_sym ** i for i in range(D + 1))
            print(f"  {name}: j-degree = {D}, poly = {sp.expand(poly)}")
            return D, poly
    return None, None


def main():
    J = 12
    print(f"Building tables up to j = {J}...")
    tables = bt(J)
    print(f"Computing ds_j/V...")
    dsV = dsV_all(J, tables)

    print("\n" + "=" * 72)
    print("Fit A_2 in basis {pi^k * (sigma - 1 - 2k)^{↓(j-2k)}}")
    print("=" * 72)
    results = try_fit_A2(dsV, J)

    print("\n" + "=" * 72)
    print("Fit c_k(j) as polynomial in j")
    print("=" * 72)
    if results:
        c0_samples = [(jj, results[jj][0]) for jj in sorted(results.keys())]
        c1_samples = [(jj, results[jj][1]) for jj in sorted(results.keys())]
        c2_samples = [(jj, results[jj][2]) for jj in sorted(results.keys())]
        fit_j_poly(c0_samples, "c_0(j)")
        fit_j_poly(c1_samples, "c_1(j)")
        fit_j_poly(c2_samples, "c_2(j)")


if __name__ == "__main__":
    main()
