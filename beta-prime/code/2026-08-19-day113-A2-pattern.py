"""Explore A_2 pattern:
Conjecture: A_2 = c_0(j)*(sigma-1)^{↓j} + c_1(j)*pi*(sigma-3)^{↓(j-1)} + c_2(j)*pi^2*(sigma-5)^{↓(j-3)}
where c_k(j) are polynomials in j of degree ≤ 2*2 = 4.

Empirically compute A_2 and try to fit into this form.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational

a, b, c = symbols('a b c')
u = a + 2
y2, y3 = b + 1, c


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


def sigma_pi_form(F):
    """Express F(b, c) as polynomial in sigma = b+c+1 and pi = (b+1)*c.
    Returns None if F is not (b <-> c-1)-symmetric.
    """
    sig, pi_v = symbols('sigma pi')
    # Test symmetry: swap b -> c-1, c -> b+1
    F_swap = F.subs([(b, symbols('_t1')), (c, symbols('_t2'))], simultaneous=True)
    F_swap = F_swap.subs([(symbols('_t1'), c - 1), (symbols('_t2'), b + 1)])
    F_swap = expand(F_swap)
    if expand(F - F_swap) != 0:
        return None
    # Symmetric — express in sigma, pi.
    # sigma = b + c + 1, pi = (b+1)*c = bc + c
    # Use resultant or grobner basis to eliminate b, c.
    # Simple approach: replace c = sigma - b - 1, get poly in b, sigma.
    # Then use pi = (b+1)(sigma - b - 1) = b*sigma - b^2 - b + sigma - b - 1 = -b^2 + b*sigma - 2b + sigma - 1
    # Hmm complicated. Try iterative substitution.
    Fexp = expand(F.subs(c, sig - b - 1))
    # Now poly in b, sigma. For symmetric F, the b-dependence should be expressible via pi = (b+1)(sigma - b - 1).
    # Repeatedly reduce b^2 = -pi + b*sigma - 2*b + sigma - 1 (from pi = -b^2 + b*sigma - 2b + sigma - 1, so b^2 = -pi + b*sigma - 2b + sigma - 1).
    # Iterate until no b appears.
    P = Poly(Fexp, b)
    result = Integer(0)
    # For symmetric F in b (via sigma), it should be expressible in b via just b^2 reduction... let me just compute.
    # Alternative: use resultant to eliminate b.
    from sympy import groebner, symbols as sym
    # Actually easier: substitute b = (y_2 - 1) and iterate to eliminate y_2 using y_2*y_3 = pi with y_3 = sigma - y_2.
    # Let z = y_2. Then y_3 = sigma - z, pi = z*(sigma - z) = sigma*z - z^2.
    # F in terms of y_2 = b+1 = z:
    Fz = expand(F.subs([(b, symbols('z') - 1), (c, sig - symbols('z'))]))
    z = symbols('z')
    Pz = Poly(Fz, z)
    # Reduce z^2 = sigma*z - pi
    coefs = dict(Pz.as_dict())  # {(exp,): coeff}
    # Get univariate coeffs
    coeffs_list = [Integer(0)] * (Pz.degree() + 1)
    for (exp,), cf in coefs.items():
        coeffs_list[exp] = cf
    # Reduce highest degree z^d = z^(d-2)*(sigma*z - pi) = sigma*z^(d-1) - pi*z^(d-2)
    while len(coeffs_list) > 2:
        d = len(coeffs_list) - 1
        top = coeffs_list[d]
        if top == 0:
            coeffs_list.pop()
            continue
        # z^d -> sigma * z^(d-1) - pi * z^(d-2)
        coeffs_list[d - 1] += sig * top
        coeffs_list[d - 2] += -pi_v * top
        coeffs_list.pop()
    # Now Fz = coeffs_list[0] + coeffs_list[1] * z
    # For symmetric F: coeffs_list[1] should be 0 (since coefficient of z should vanish for a symmetric poly, once reduced).
    if len(coeffs_list) > 1 and coeffs_list[1] != 0:
        # Not clean; return as is
        return f"[non-symmetric in z reduction: coef of z = {coeffs_list[1]}]"
    return expand(coeffs_list[0])


def main():
    J = 10
    print(f"Building tables up to j = {J}...")
    tables = bt(J)
    print(f"Computing ds_j/V symbolically...")
    dsV = dsV_all(J, tables)

    print("\n" + "=" * 72)
    print("Extract A_2 for small j and try to fit as sum of (sigma-1-2k)^{↓...} * pi^k")
    print("=" * 72)

    sig_sym, pi_sym = symbols('sigma pi')

    for jj in range(3, J + 1):
        A2 = extract_A_p(jj, 2, dsV)
        A2_sym = sigma_pi_form(A2)
        print(f"\n  j = {jj}:")
        print(f"    A_2 = {A2_sym}")


if __name__ == "__main__":
    main()
