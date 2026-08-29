"""Day 124: Check if Pi* satisfies a Leibniz-like rule.

If Pi*(f * g) = Pi*(f) * g + f * Pi*(g) - Pi*(1) * f * g (some derivation-like
structure), then filtration preservation is trivial: weight(Pi*(f g)) <=
max(w(f) + 1 + w(g), w(f) + w(g) + 1) = w(f) + w(g) + 1 = w(f g) + 1.

Test:
  Pi*(e_1 * e_2) vs Pi*(e_1) * e_2 + e_1 * Pi*(e_2) - Pi*(1) * e_1 * e_2
  Pi*(e_1 * e_3), etc.

Or simpler: does Pi*(f) = D(f) + Pi*(1) * f  for some derivation D?
  Pi*(f) - Pi*(1) * f  should be linear in f AND a derivation of some kind.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer

from pi_star_on_monomials import build_pi_star_matrix, weight_112_tuple

e1, e2, e3 = symbols('e1 e2 e3')


def dict_to_poly(d):
    result = Integer(0)
    for (a1, a2, a3), c in d.items():
        result += c * e1**a1 * e2**a2 * e3**a3
    return expand(result)


def main():
    input_monoms, pi_star = build_pi_star_matrix(6)

    def Pi(f):
        # f is dict or poly; return image as poly
        p = expand(f)
        p_poly = Poly(p, e1, e2, e3)
        result = Integer(0)
        for (a1, a2, a3), coef in p_poly.terms():
            m = (a1, a2, a3)
            if m in pi_star:
                result += coef * dict_to_poly(pi_star[m])
            else:
                raise ValueError(f'Monomial {m} not precomputed')
        return expand(result)

    print('Values of Pi* on basis:')
    print(f'  Pi*(1)   = {Pi(1)}')
    print(f'  Pi*(e_1) = {Pi(e1)}')
    print(f'  Pi*(e_2) = {Pi(e2)}')
    print(f'  Pi*(e_3) = {Pi(e3)}')
    print()
    print('Check derivation-like rule: define D(f) = Pi*(f) - Pi*(1)*f.')
    print(f'  D(1) = 0')
    print(f'  D(e_1) = {expand(Pi(e1) - Pi(1) * e1)}')
    print(f'  D(e_2) = {expand(Pi(e2) - Pi(1) * e2)}')
    print(f'  D(e_3) = {expand(Pi(e3) - Pi(1) * e3)}')
    print(f'  D(e_1^2) = {expand(Pi(e1**2) - Pi(1) * e1**2)}')
    print(f'  D(e_1)^2 test: 2 e_1 D(e_1) = {expand(2 * e1 * (Pi(e1) - Pi(1) * e1))}')

    print()
    print('Check Leibniz: D(f*g) = D(f) g + f D(g)?')
    D = lambda f: expand(Pi(f) - Pi(1) * f)
    products = [(e1, e1), (e1, e2), (e1, e3), (e2, e2), (e2, e3), (e3, e3),
                (e1**2, e1), (e1, e2**2)]
    for f, g in products:
        lhs = D(f * g)
        rhs = expand(D(f) * g + f * D(g))
        diff = expand(lhs - rhs)
        status = 'OK' if diff == 0 else 'FAIL'
        print(f'  D({f} * {g}): diff = {diff}   {status}')

    print()
    print('The naive derivation rule may fail. Instead test the weight-refined:')
    print('is Pi*(f*g) close to Pi*(f)*g + f*Pi*(g) - Pi*(1)*f*g at TOP weight?')
    print()

    # Top weight of Pi*(f)
    def top_weight_part(f):
        f = expand(f)
        if f == 0:
            return Integer(0), -1
        p = Poly(f, e1, e2, e3)
        w = 0
        for (a1, a2, a3), _ in p.terms():
            w = max(w, a1 + a2 + 2 * a3)
        top = Integer(0)
        for (a1, a2, a3), coef in p.terms():
            if a1 + a2 + 2 * a3 == w:
                top += coef * e1**a1 * e2**a2 * e3**a3
        return expand(top), w

    for f, g in products:
        fg = expand(f * g)
        lhs = Pi(fg)
        rhs_candidate = expand(Pi(f) * g + f * Pi(g) - Pi(1) * f * g)
        top_lhs, w_lhs = top_weight_part(lhs)
        top_rhs, w_rhs = top_weight_part(rhs_candidate)
        diff_top, _ = top_weight_part(expand(top_lhs - top_rhs))
        print(f'  f={f}, g={g}: top(Pi*(fg))={top_lhs} (w={w_lhs})')
        print(f'           top(Pi*(f)g+fPi*(g)-Pi*(1)fg)={top_rhs} (w={w_rhs})')
        print(f'           top(diff) at highest weight = {expand(top_lhs - top_rhs)}')


if __name__ == '__main__':
    main()
