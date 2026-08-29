"""Day 124 major experiment: fully verify monomial-by-monomial filtration
preservation for Pi* up to LARGE u-degree, then look for algebraic structure.

Also: derive Pi* as a differential/pseudo-differential operator on Q[e1, e2, e3]
and see if the weight-preserving structure is manifest in that description.

Key question: Pi*(e_1^a1 e_2^a2 e_3^a3) is a specific polynomial. What is its
STRUCTURE?

Approach: We know Pi*(1), Pi*(e_1), Pi*(e_2), Pi*(e_3). If Pi* were multiplicative
(it's not — it's not a ring hom), we'd be done. Let's compute the "defect":
  R(f, g) := Pi*(f * g) - f * Pi*(g) - Pi*(f) * g + f * g * Pi*(1)
This is symmetric in f, g and measures how far Pi* deviates from being a
derivation-plus-multiplication-by-Pi*(1). If R(f, g) has "small weight" (like
w(f) + w(g)) then top-weight of Pi*(f * g) at weight w(f) + w(g) + 1 equals
f * top(Pi*(g)) + Pi*(f) * g - f g * Pi*(1) at that weight, giving inductive
control.
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


def top_grading(f):
    """Return top-weight component."""
    w = weight_of_poly(f)
    if w < 0:
        return Integer(0), -1
    p = Poly(expand(f), e1, e2, e3)
    top = Integer(0)
    for (a1, a2, a3), coef in p.terms():
        if a1 + a2 + 2*a3 == w:
            top += coef * e1**a1 * e2**a2 * e3**a3
    return expand(top), w


def main():
    print('Building Pi* action on e-monomials u-degree <= 8')
    input_monoms, pi_star = build_pi_star_matrix(8)

    def Pi(f):
        p = expand(f)
        p_poly = Poly(p, e1, e2, e3)
        result = Integer(0)
        for (a1, a2, a3), coef in p_poly.terms():
            m = (a1, a2, a3)
            if m in pi_star:
                result += coef * dict_to_poly(pi_star[m])
            else:
                raise ValueError(f'Monomial {m} not computed (need larger table)')
        return expand(result)

    # First: check R(f, g) := Pi*(f*g) - f * Pi*(g) - Pi*(f) * g + f * g * Pi*(1)
    # for various f, g. Does its weight satisfy w(R) <= w(f) + w(g)?
    print()
    print('=' * 70)
    print('Defect R(f, g) = Pi*(fg) - f Pi*(g) - Pi*(f) g + fg Pi*(1)')
    print('Testing whether weight(R(f,g)) <= w(f) + w(g)  (strict decrease of 1)')
    print('=' * 70)
    Pi_1 = Pi(Integer(1))
    for f, g in [(e1, e1), (e1, e2), (e2, e2), (e2, e3), (e3, e3), (e1, e3),
                 (e2**2, e1), (e2, e2*e3), (e1*e2, e3)]:
        fg = expand(f * g)
        R = expand(Pi(fg) - f * Pi(g) - Pi(f) * g + f * g * Pi_1)
        wR = weight_of_poly(R)
        wf = weight_of_poly(f)
        wg = weight_of_poly(g)
        wfg = weight_of_poly(fg)
        bound = wf + wg  # (want <= this)
        status = 'OK' if wR <= bound else '!!!'
        print(f'  f = {f} (w={wf}), g = {g} (w={wg}): w(R) = {wR}, bound = {bound} {status}')
        if wR > bound:
            print(f'    R = {R}')

    # If R is well-behaved, we get the inductive step.
    # But we need to know what the FUNCTION top(Pi*(m)) is.

    # Let's tabulate top(Pi*(e_1^a1 e_2^a2 e_3^a3)) for many (a1, a2, a3).
    print()
    print('=' * 70)
    print('Top-weight symbol of Pi*(e_1^a1 e_2^a2 e_3^a3)  -- for a3 = 0')
    print('=' * 70)
    # Conjecture: top(Pi*(e_1^a e_2^b)) = e_1^a * top(Pi*(e_2^b))
    #   (since top(Pi*(e_1)) = e_1 (e_2 - e_1), and e_1 factors nicely)
    for a1 in range(0, 5):
        for a2 in range(0, 4):
            m = e1**a1 * e2**a2
            if weight_of_poly(m) > 5:
                continue
            pim = Pi(m)
            top, w = top_grading(pim)
            # Compare with e_1^a1 * top(Pi*(e_2^a2))
            pi_e2 = Pi(e2**a2)
            top_e2, _ = top_grading(pi_e2)
            guess = expand(e1**a1 * top_e2)
            diff = expand(top - guess)
            print(f'  m = e_1^{a1} e_2^{a2}: top = {top}, e_1^{a1} * top(Pi*(e_2^{a2})) - actual = {expand(guess - top)}')

    print()
    print('=' * 70)
    print('Top-weight symbol of Pi*(e_1^a1 e_2^a2 e_3^a3) - all a3')
    print('=' * 70)
    # Conjecture: top(Pi*(m)) depends "nicely" on a3.
    for a3 in range(0, 3):
        print(f'\n  a3 = {a3}:')
        for a1 in range(0, 4):
            for a2 in range(0, 3):
                m = e1**a1 * e2**a2 * e3**a3
                if weight_of_poly(m) > 5:
                    continue
                pim = Pi(m)
                top, w = top_grading(pim)
                # Guess: top(Pi*(e_1^a1 e_2^a2 e_3^a3)) = e_3^a3 * (something)?
                if a3 > 0:
                    pi_no_e3 = Pi(e1**a1 * e2**a2)
                    top_no_e3, _ = top_grading(pi_no_e3)
                    guess1 = expand(e3**a3 * top_no_e3)
                    d1 = expand(top - guess1)
                    print(f'    a1={a1}, a2={a2}: top = {top}')
                    print(f'      e_3^{a3} * top(Pi*(e_1^{a1} e_2^{a2})) - actual = {d1}')
                else:
                    print(f'    a1={a1}, a2={a2}: top = {top}')


if __name__ == '__main__':
    main()
