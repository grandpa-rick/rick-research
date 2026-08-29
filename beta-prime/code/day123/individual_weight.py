"""Day 123: Study (1,1,2)-weight of individual s*_mu.

For each mu with |mu| = 2j, l(mu) <= 3, mu_1 <= j, compute s*_mu in e-basis and
its (1,1,2)-weight = max(a1 + a2 + 2 a3 : coefficient nonzero).

Compare with d_mu = mu_1 + floor((mu_2 + mu_3)/2) = deg_t F_mu.

Understand why the weighted sum E_j has weight <= j.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')

import sympy as sp
from sympy import symbols, expand, Poly, factor, Integer, Rational
from itertools import combinations

e1, e2, e3 = symbols('e1 e2 e3')
u1, u2, u3 = symbols('u1 u2 u3')


def s_star_mu(mu):
    mu = list(mu) + [0] * (3 - len(mu))
    mu = mu[:3]
    k = [mu[0] + 2, mu[1] + 1, mu[2]]
    xs = [u1, u2, u3]

    def fall(x, m):
        p = Integer(1)
        for i in range(m):
            p *= (x - i)
        return p

    rows = [[fall(xs[i], k[l]) for l in range(3)] for i in range(3)]
    numer = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
             - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
             + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
    V = (u1 - u2) * (u1 - u3) * (u2 - u3)
    q, r = sp.div(sp.Poly(expand(numer), u1, u2, u3), sp.Poly(expand(V), u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError(f'Not divisible for mu={mu}')
    return expand(q.as_expr())


def sym_to_e_basis(f):
    from sympy.polys.polyfuncs import symmetrize
    result, remainder, formulas = symmetrize(f, [u1, u2, u3], formal=True)
    if remainder != 0:
        raise ValueError(f'Not symmetric: {f}')
    s_syms = [x for (x, _) in formulas]
    e_subs = dict(zip(s_syms, [e1, e2, e3]))
    return expand(result.subs(e_subs))


def weight_112(expr):
    """Max value of a1 + a2 + 2 a3 over nonzero monomials in e1^a1 e2^a2 e3^a3."""
    if expr == 0:
        return -1
    p = Poly(expr, e1, e2, e3)
    max_w = -1
    for (a1, a2, a3), coef in p.terms():
        w = a1 + a2 + 2 * a3
        if w > max_w:
            max_w = w
    return max_w


def main():
    print('=' * 70)
    print('(1,1,2)-weight of s*_mu vs d_mu = mu_1 + floor((mu_2+mu_3)/2)')
    print('=' * 70)
    for total in range(0, 11):
        print(f'\n|mu| = {total}:')
        for mu1 in range(total + 1):
            for mu2 in range(mu1 + 1):
                mu3 = total - mu1 - mu2
                if mu3 < 0 or mu3 > mu2:
                    continue
                if mu1 == 0 and total > 0:
                    continue
                mu = (mu1, mu2, mu3)
                s_star = s_star_mu(mu)
                s_star_e = sym_to_e_basis(s_star)
                w = weight_112(s_star_e)
                d = mu1 + (mu2 + mu3) // 2
                marker = 'OK' if w <= d else ('!!!' if w > d else '')
                print(f'  mu={mu}: (1,1,2)-weight = {w}, d_mu = {d}, |mu|/2 = {total/2}   {marker}')
                if total <= 4:
                    print(f'    s*_mu = {s_star_e}')


if __name__ == '__main__':
    main()
