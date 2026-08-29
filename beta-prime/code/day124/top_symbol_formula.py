"""Day 124: Study the TOP-weight symbol of Pi*(e_1^a1 e_2^a2 e_3^a3).

Empirical claim: weight(Pi*(m)) = w(m) + 1 for every monomial m.
Look for a closed form for the top-weight component.

Let sigma_w(f) = sum of monomials of weight exactly w in f (leading symbol).
Then sigma_{w(m)+1}(Pi*(m)) = ?

Do this by computing Pi*(m) - Pi*(1) * m and Pi*(m) - m * Pi*(1) and looking
at top-weight parts.

Also: check if there's a simpler generating operator L such that Pi*(f) has
top part = L(top part of f) where L is like a graded operator on the associated
graded ring.
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


def weight_of_poly(f):
    if f == 0:
        return -1
    p = Poly(expand(f), e1, e2, e3)
    return max(a1 + a2 + 2*a3 for (a1, a2, a3), _ in p.terms())


def sigma_w(f, w):
    """Sum of monomials in f of exactly weight w."""
    if f == 0:
        return Integer(0)
    p = Poly(expand(f), e1, e2, e3)
    result = Integer(0)
    for (a1, a2, a3), coef in p.terms():
        if a1 + a2 + 2*a3 == w:
            result += coef * e1**a1 * e2**a2 * e3**a3
    return expand(result)


def main():
    input_monoms, pi_star = build_pi_star_matrix(6)

    def Pi(f):
        p = expand(f)
        p_poly = Poly(p, e1, e2, e3)
        result = Integer(0)
        for (a1, a2, a3), coef in p_poly.terms():
            m = (a1, a2, a3)
            if m in pi_star:
                result += coef * dict_to_poly(pi_star[m])
        return expand(result)

    print('=' * 70)
    print('Top-weight symbol of Pi*(m):')
    print('=' * 70)
    for m in input_monoms:
        w_in = weight_112_tuple(m)
        pim = Pi(e1**m[0] * e2**m[1] * e3**m[2])
        w_out = weight_of_poly(pim)
        top = sigma_w(pim, w_out)
        m_expr = e1**m[0] * e2**m[1] * e3**m[2]
        print(f'\n  m = {m_expr} (w={w_in}): top^{w_out}(Pi*(m)) = {top}')

    print()
    print('=' * 70)
    print('Test: is Pi*(e_1^a e_2^b e_3^c) top ~ (something explicit)?')
    print('=' * 70)

    # Pi*(1) = 1 + e_2 - e_1, top^1 = -e_1 + e_2
    # Pi*(e_1) top^2 = -e_1^2 + e_1 e_2 = e_1 (top^1(Pi*(1)))
    # Pi*(e_2) top^2 = e_1^2 - 2 e_1 e_2 + e_2^2 - 3 e_3 = (top^1(Pi*(1)))^2 - 3 e_3?  Check.
    top1 = -e1 + e2  # top of Pi*(1)
    print(f'\n  top(Pi*(1)) = {top1}')
    print(f'  top(Pi*(e_1)) = e_1 * top(Pi*(1)) = {expand(e1 * top1)}')
    p1 = Pi(e1); print(f'    actual = {sigma_w(p1, weight_of_poly(p1))}')

    p2 = Pi(e2)
    guess = expand(e2 * top1)
    print(f'\n  top(Pi*(e_2)) guess e_2 * top(Pi*(1)) = {guess}')
    print(f'    actual = {sigma_w(p2, weight_of_poly(p2))}')
    print(f'    diff = {expand(sigma_w(p2, weight_of_poly(p2)) - guess)}')

    p3 = Pi(e3)
    guess = expand(e3 * top1)
    print(f'\n  top(Pi*(e_3)) guess e_3 * top(Pi*(1)) = {guess}')
    print(f'    actual = {sigma_w(p3, weight_of_poly(p3))}')
    print(f'    diff = {expand(sigma_w(p3, weight_of_poly(p3)) - guess)}')

    print()
    print('=' * 70)
    print('CONJECTURE: top(Pi*(f)) = top(f) * (e_2 - e_1) + <correction>')
    print('This makes sense because Pi* = Psi * (e_2 * ) * Psi^-1 and top of Psi is identity.')
    print('=' * 70)

    # For a monomial m, is top(Pi*(m)) = m * (e_2 - e_1) + <lower-weight-of-m>-terms?
    # No, we need weight-(w(m)+1) parts.
    # Let's compute Pi*(m) - m * (e_2 - e_1) top-weight-of-(w(m)+1) part.
    def top_weight_grading(f):
        p = Poly(expand(f), e1, e2, e3)
        d = {}
        for (a1, a2, a3), coef in p.terms():
            w = a1 + a2 + 2*a3
            d.setdefault(w, Integer(0))
            d[w] = d[w] + coef * e1**a1 * e2**a2 * e3**a3
        return {w: expand(v) for w, v in d.items()}

    for m in input_monoms:
        m_expr = e1**m[0] * e2**m[1] * e3**m[2]
        pim = Pi(m_expr)
        w = weight_112_tuple(m)
        pim_grading = top_weight_grading(pim)
        top = pim_grading.get(w + 1, Integer(0))
        guess = expand(m_expr * (e2 - e1))
        diff = expand(top - guess)
        print(f'  m = {m_expr} (w={w}): top^{w+1}(Pi*(m)) - m*(e2-e1) = {diff}')


if __name__ == '__main__':
    main()
