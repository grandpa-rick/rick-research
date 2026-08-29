"""Diagnostic: compute Day 140's P_b for small b, then figure out its EGF factorization."""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3

from sympy import symbols, expand, Poly, Integer, factorial, factor, Rational, log, exp, series, Symbol, sqrt

T = symbols('T')

def main():
    B_MAX = 6
    P = build_P(B_MAX)
    print("Day 140's P_b polynomials:")
    for b in range(B_MAX+1):
        print(f"\n  P_{b} = {P[b]}")

    print("\n\np_b = ∏ φ_k:")
    for b in range(B_MAX+1):
        print(f"  p_{b} = {p_b_fn(b)}")

    print("\n\nCheck P_b|_{E3=0} vs p_b:")
    for b in range(B_MAX+1):
        pb_from_P = expand(P[b].subs(E3, 0))
        pb_from_prod = p_b_fn(b)
        diff = expand(pb_from_P - pb_from_prod)
        print(f"  b={b}: P|_E3=0 = {pb_from_P}   p_b = {pb_from_prod}   diff = {diff}")

    # Look at EGF: F(T) = Σ P_b T^b/b! and try to factor.
    # First: at E3=0, Σ P_b|_{E3=0} T^b/b! = ?
    # If it's A(T) = (1-E1 T)^{-E2/E1 - 1}, expand:
    #   [T^b] A(T) · b! = ∏_{k=0}^{b-1} (-E2/E1 - 1 - k) · (-E1)^b
    #                   = ∏_{k=0}^{b-1} (E2 + E1 + k E1) = ∏_{k=0}^{b-1} (E2 + (k+1) E1)
    #                   = ∏_{j=1}^{b} (E2 + j E1)
    # But p_b = ∏_{k=1..b} (E2 + k E1 + k²). Different.
    # So A(T) is definitely NOT Σ p_b T^b/b!.
    # But we saw P_b|_{E3=0} = ??? Let's find out.

    print("\n\nSuppose Σ P_b|_{E3=0} T^b/b! = ∏(E2 + k E1)? Check:")
    for b in range(B_MAX+1):
        pred = Integer(1)
        for k in range(1, b+1):
            pred *= (E2 + k*E1)
        pred = expand(pred)
        actual = expand(P[b].subs(E3, 0))
        diff = expand(actual - pred)
        print(f"  b={b}: actual={actual}   predicted=∏(E2+kE1)={pred}   diff={diff}")


if __name__ == '__main__':
    main()
