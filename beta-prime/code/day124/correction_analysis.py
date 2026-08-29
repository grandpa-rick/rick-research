"""Day 124: Analyze s*_mu - s_mu as e-polynomial. Does it have weight < d_mu?

If YES: then s*_mu has same TOP-weight (d_mu) part as s_mu, and Psi at top-weight
level is the IDENTITY on the (s_mu -> s*_mu) map.

But then top-weight of Psi(m) for a monomial m = ... hmm this doesn't quite follow.

Actually: if top(s*_mu) = top(s_mu) (same weight-d_mu monomials), then
top(Psi(f)) at any weight can be computed by:
  top_w(Psi(f)) = sum_{mu} c_mu top_w(s*_mu) = sum_{mu, d_mu = w} c_mu top(s_mu)
= top_w(f).

Wait, that would show Psi ≡ identity at top-weight. But we've seen top(Psi(e_2)) = -e_1 + e_2, not e_2. So this must be wrong.

Let me test carefully: does top(s*_mu) = top(s_mu)?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer

from individual_weight import s_star_mu, sym_to_e_basis
from pi_star_on_monomials import s_ord_mu, enum_parts, weight_112_tuple

e1, e2, e3 = symbols('e1 e2 e3')


def top_weight_part_of_poly(f, w):
    if f == 0:
        return Integer(0)
    p = Poly(expand(f), e1, e2, e3)
    result = Integer(0)
    for (a1, a2, a3), coef in p.terms():
        if a1 + a2 + 2*a3 == w:
            result += coef * e1**a1 * e2**a2 * e3**a3
    return expand(result)


def d_mu(mu):
    return mu[0] + (mu[1] + mu[2]) // 2


def main():
    print('=' * 80)
    print('Comparing top-weight parts of s_mu and s*_mu:')
    print('=' * 80)
    for mu in enum_parts(5):
        s = s_ord_mu(mu)
        s_e = sym_to_e_basis(s)
        ss = s_star_mu(mu)
        ss_e = sym_to_e_basis(ss)
        d = d_mu(mu)
        top_s = top_weight_part_of_poly(s_e, d)
        top_ss = top_weight_part_of_poly(ss_e, d)
        diff = expand(top_ss - top_s)
        marker = 'SAME' if diff == 0 else 'DIFFERENT'
        print(f'\n  mu = {mu} (d = {d}):')
        print(f'    top(s_mu)  = {top_s}')
        print(f'    top(s*_mu) = {top_ss}')
        print(f'    diff       = {diff}   [{marker}]')


if __name__ == '__main__':
    main()
