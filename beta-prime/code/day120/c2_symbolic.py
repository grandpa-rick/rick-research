"""Symbolic form of the Weyl-formula for K_even(l, r) and K_odd(l, r).

For 3-part mu with |mu| = 2j:
  K_{mu', (2^j)} = sum_{tau in S_3} sign(tau) * multinomial(j; a, b, c)
where
  A_tau = m_1 - (3 - tau(1)) + 2, i.e., A_tau = rho_1 - pi_1
  Let pi = (pi_1, pi_2, pi_3) be a permutation of (2, 1, 0) with sign = sign(pi as perm of (2,1,0)).
  Then A = rho_1 - pi_1, B = rho_2 - pi_2, C = rho_3 - pi_3.
  a = (A+B-C)/2, b = (A-B+C)/2, c = (-A+B+C)/2, and term = C(j; a, b, c) if valid, else 0.

For mu = (2l, l+1+r, l+1-r), j = 2l+1:
  rho = (2l+2, l+2+r, l+1-r).

Let me tabulate a, b, c for each pi:
"""

import sympy as sp
from sympy import symbols, expand, factorial, binomial, Rational, Sum, simplify, S, Poly


def formula_terms():
    l, r = symbols('l r', integer=True, nonnegative=True)
    # rho for even spine
    rho = [2*l+2, l+2+r, l+1-r]
    j = 2*l+1
    from itertools import permutations
    terms = []
    for tau in permutations([1, 2, 3]):
        inv = sum(1 for i in range(3) for k in range(i+1, 3) if tau[i] > tau[k])
        sign = (-1) ** inv
        pi = [3 - t for t in tau]
        A = rho[0] - pi[0]
        B = rho[1] - pi[1]
        C = rho[2] - pi[2]
        a = sp.Rational(1, 2) * (A + B - C)
        b = sp.Rational(1, 2) * (A - B + C)
        c = sp.Rational(1, 2) * (-A + B + C)
        # Multinomial (2l+1)! / (a! b! c!)
        # But easier: use C(2l+1, a) * C(2l+1-a, b) or C(2l+1, a, b, c)
        # Store as symbolic
        terms.append((pi, sign, sp.simplify(a), sp.simplify(b), sp.simplify(c)))
    print("=== Weyl formula terms for K_even(l, r), j = 2l+1 ===")
    print("mu = (2l, l+1+r, l+1-r), rho = (2l+2, l+2+r, l+1-r)")
    print()
    for pi, sign, a, b, c in terms:
        print(f"  pi={pi}, sign={sign:+d}: (a, b, c) = ({a}, {b}, {c})")
    return terms


def formula_terms_odd():
    """Same for odd-spine mu = (2l+1, l+1+r, l-r), j = 2l+1."""
    l, r = symbols('l r', integer=True, nonnegative=True)
    rho = [2*l+3, l+2+r, l-r]
    j = 2*l+1
    from itertools import permutations
    print("\n=== Weyl formula terms for K_odd(l, r), j = 2l+1 ===")
    print("mu = (2l+1, l+1+r, l-r), rho = (2l+3, l+2+r, l-r)")
    print()
    for tau in permutations([1, 2, 3]):
        inv = sum(1 for i in range(3) for k in range(i+1, 3) if tau[i] > tau[k])
        sign = (-1) ** inv
        pi = [3 - t for t in tau]
        A = rho[0] - pi[0]
        B = rho[1] - pi[1]
        C = rho[2] - pi[2]
        a = sp.Rational(1, 2) * (A + B - C)
        b = sp.Rational(1, 2) * (A - B + C)
        c = sp.Rational(1, 2) * (-A + B + C)
        print(f"  pi={pi}, sign={sign:+d}: (a, b, c) = ({a}, {b}, {c})")


def check_c2_alt_sum():
    """Compute sum_{r=0}^{l-1} (-1)^r K_even(l, r) using the Weyl formula symbolically.
    Even better: substitute known formulas."""
    print("\n=== Numerical check of A_even(l) ===")
    import sys
    sys.path.insert(0, '/home/agent/projects/beta-prime/code/day120')
    from c2_weyl_formula import kostka_weyl
    for l in range(1, 12):
        total = 0
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K = kostka_weyl(mu)
            total += (-1)**r * K
        expected = (-1)**(l+1)
        print(f"l={l}: A_even = {total}, expected {expected}  {'OK' if total == expected else '!!!'}")


if __name__ == "__main__":
    formula_terms()
    formula_terms_odd()
    check_c2_alt_sum()
