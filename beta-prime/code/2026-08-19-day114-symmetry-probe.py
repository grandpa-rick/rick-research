"""Quick probe: is A_2 symmetric under (b, c) -> (c-1, b+1)?
If yes, express in Rick's (pi = (b+1)*c, sigma = b + c + 1) — the natural
'shifted-Schur' variables.  Then rerun the ansatz scan in THOSE variables.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer, factor

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


def is_sym_bc1(F):
    """Test invariance under (b, c) -> (c-1, b+1)."""
    F_swap = F.subs([(b, symbols('_t1')), (c, symbols('_t2'))], simultaneous=True)
    F_swap = F_swap.subs([(symbols('_t1'), c - 1), (symbols('_t2'), b + 1)])
    return expand(F - expand(F_swap)) == 0


def to_pi_sigma_shifted(F):
    """Convert F(b,c) to F(pi, sigma) with pi = (b+1)*c, sigma = b + c + 1.
    Uses z = b+1, then y = sigma - z = c, and z*y = pi, i.e. z^2 = sigma*z - pi.
    Requires F to be symmetric under (b,c)->(c-1,b+1) (i.e., under z<->y swap).
    """
    sig, pi_v = symbols('sigma pi')
    z = symbols('z')
    # b = z - 1, c = sigma - z
    Fz = expand(F.subs([(b, z - 1), (c, sig - z)]))
    # Polynomial in z with coefficients in Q[sigma]
    Pz = sp.Poly(Fz, z)
    D = Pz.degree()
    coefs = [Pz.coeff_monomial(z ** i) for i in range(D + 1)]
    # Reduce degrees > 1 via z^d = sigma * z^{d-1} - pi * z^{d-2}
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
        return None  # not symmetric under z <-> sigma-z
    return sp.expand(coefs[0])


def main():
    J = 12
    print(f"Building tables & dsV up to j = {J}...")
    tables = bt(J)
    dsV = dsV_all(J, tables)

    print("\n" + "=" * 72)
    print("Test whether A_2(b, c, j) is symmetric under (b, c) -> (c-1, b+1).")
    print("=" * 72)
    for jj in range(4, J + 1):
        A2 = extract_A_p(jj, 2, dsV)
        sym = is_sym_bc1(A2)
        print(f"  j = {jj}: {'SYMMETRIC' if sym else 'NOT symmetric'}")
        if sym:
            F_ps = to_pi_sigma_shifted(A2)
            print(f"    A_2(pi=(b+1)c, sigma=b+c+1)  =  {sp.expand(F_ps)}")
            print(f"    factored:  {sp.factor(F_ps)}")


if __name__ == "__main__":
    main()
