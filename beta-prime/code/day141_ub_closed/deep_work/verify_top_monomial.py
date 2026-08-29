"""
Verify the TOP-MONOMIAL closed form:

  [U^{b-2k} V^{b-2k}] r_b^(k)(U, V) = 3^k (2k-1)!! C(b, 2k)

Equivalently, in EGF form:
  TOP-in-UV part of F_P(T; U, V, E_3) = f(T; U, V) · exp(3 E_3 T^2 / 2)

where f(T; U, V) = Σ_b (U)_b (V)_b T^b/b!.

This gives the following "top-monomial closed form" for U_b(w):
  U_b^{TOP}(w) := Σ_k 3^k (2k-1)!! C(b, 2k) · (U)_{b-2k}(V)_{b-2k}·(w - UV)^{k-1}
  = coefficient of U^{b-2k}V^{b-2k}(w-UV)^{k-1} matches actual U_b(w) exactly.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, E1, E2, E3, w
from sympy import (symbols, expand, Poly, Integer, Rational, rf, factorial,
                    binomial, div)

U, V = symbols('U V')

def to_UV(P):
    return expand(P.subs([(E1, U + V - 2), (E2, U*V - U - V + 1)], simultaneous=True))

def double_factorial(n):
    if n <= 0: return 1
    if n == 1: return 1
    return n * double_factorial(n - 2)

def main():
    B_MAX = 10
    P = build_P(B_MAX)
    P_UV = {b: to_UV(P[b]) for b in P}

    print("VERIFY: [U^{b-2k} V^{b-2k}] r_b^(k) = 3^k (2k-1)!! C(b, 2k)")
    print("=" * 78)
    all_pass = True
    for b in range(2, B_MAX + 1):
        Pp = Poly(P_UV[b], E3)
        for k in range(1, b // 2 + 1):
            r_bk = Pp.coeff_monomial(E3**k)
            r_bk = expand(r_bk)
            # Extract [U^{b-2k} V^{b-2k}]
            r_bk_poly = Poly(r_bk, U, V)
            top_mon_coef = r_bk_poly.coeff_monomial(U**(b - 2*k) * V**(b - 2*k))
            predicted = 3**k * double_factorial(2*k - 1) * binomial(b, 2*k)
            status = "OK" if top_mon_coef == predicted else f"FAIL (got {top_mon_coef}, predicted {predicted})"
            if top_mon_coef != predicted:
                all_pass = False
            print(f"  b={b}, k={k}: coef of U^{b-2*k}V^{b-2*k} = {top_mon_coef}, predicted = {predicted}  [{status}]")

    print()
    print(f"Overall: {'ALL PASS' if all_pass else 'SOME FAIL'}")

    # Now express U_b(w) - U_b^{TOP}(w) explicitly for small b
    print("\n" + "=" * 78)
    print("Compute U_b(w) - U_b^{TOP}(w) (the correction/lower-degree part):")
    print("=" * 78)

    phi_1 = U * V
    for b in range(2, min(B_MAX, 6) + 1):
        # Actual U_b(w):
        Pshift = expand(P_UV[b].subs(E3, w - phi_1))
        p_b = expand(rf(U, b) * rf(V, b))
        numer = expand(Pshift - p_b)
        q, rr = div(numer, w - phi_1, w)
        U_b_actual = expand(q)

        # U_b^{TOP}(w):
        U_b_top = Integer(0)
        for k in range(1, b // 2 + 1):
            coef = 3**k * double_factorial(2*k - 1) * binomial(b, 2*k)
            term = coef * rf(U, b - 2*k) * rf(V, b - 2*k) * (w - phi_1)**(k - 1)
            U_b_top += term
        U_b_top = expand(U_b_top)

        correction = expand(U_b_actual - U_b_top)
        print(f"\n--- b = {b} ---")
        print(f"  Correction (U_b - U_b^TOP) has degree in (U, V) <= b - 2 = {b-2} (individually)")
        cor_poly = Poly(correction, w)
        for d in range(cor_poly.degree() + 1) if correction != 0 else range(0):
            c = cor_poly.coeff_monomial(w**d)
            if c != 0:
                print(f"  [w^{d}] correction: {c}")

if __name__ == '__main__':
    main()
