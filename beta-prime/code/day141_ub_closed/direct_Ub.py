"""Compute U_b(w) DIRECTLY for Day 140's P, hunt for patterns.

Since Attack Angle (a) assumed F = A·exp(E3·M) which does NOT hold for Day 140,
we bypass and use the definition:
    U_b(w) := (P_b|_{E3 = w - φ_1} - p_b) / (w - φ_1),   φ_1 = E2 + E1 + 1.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3, w

from sympy import (symbols, expand, Poly, Integer, factorial, Rational, factor,
                   div, collect, simplify, together)

def main():
    B_MAX = 8
    print(f"Building P_b for b = 0..{B_MAX}")
    P = build_P(B_MAX)
    phi1 = phi_k(1)

    U = {}
    print("\nComputing U_b(w) = (P_b|_{E3 = w - φ_1} - p_b) / (w - φ_1):")
    for b in range(2, B_MAX+1):
        Pshift = expand(P[b].subs(E3, w - phi1))
        numer = expand(Pshift - p_b_fn(b))
        q, r = div(numer, w - phi1, w)
        q = expand(q)
        if r != 0:
            print(f"  b={b}: FAIL, remainder = {r}")
            continue
        U[b] = q
        Uq = Poly(q, w)
        print(f"\n  U_{b}(w), degree in w = {Uq.degree()}:")
        for d in range(Uq.degree()+1):
            c = Uq.coeff_monomial(w**d)
            if c != 0:
                print(f"    [w^{d}]  {factor(expand(c))}")

    # Now hunt for structure.
    # (1) Leading coefficient in w
    print("\n" + "="*78)
    print("LEADING COEFFICIENTS [w^d] with d = deg(U_b):")
    print("="*78)
    for b in range(2, B_MAX+1):
        Uq = Poly(U[b], w)
        d = Uq.degree()
        lc = Uq.coeff_monomial(w**d)
        print(f"  b={b}: deg={d}, LC = {factor(lc)}")

    # (2) Constant term U_b(0) — this equals T[p]_b via Day 140
    print("\n" + "="*78)
    print("U_b(0):")
    print("="*78)
    for b in range(2, B_MAX+1):
        U0 = expand(U[b].subs(w, 0))
        print(f"  b={b}: U_b(0) = {factor(U0)}")

    # (3) U_b(φ_1)  — divided-difference value at w = φ_1 relates to derivative
    print("\n" + "="*78)
    print("U_b(φ_1)  (note: φ_1 = E2 + E1 + 1):")
    print("="*78)
    for b in range(2, B_MAX+1):
        Uphi = expand(U[b].subs(w, phi1))
        print(f"  b={b}: U_b(φ_1) = {factor(Uphi)}")

    # (4) EGF Σ U_b(w) T^b/b! — compute it as series and try to close.
    from sympy import Symbol
    T = Symbol('T')
    U_egf = Integer(0)
    for b in range(2, B_MAX+1):
        U_egf += U[b] * T**b / factorial(b)
    U_egf = expand(U_egf)
    # It's polynomial in w — collect by w
    print("\n" + "="*78)
    print("Σ U_b(w) T^b/b!, collected by powers of w:")
    print("="*78)
    # For each power of w, print the T-series
    max_wdeg = max(Poly(U[b], w).degree() for b in U)
    for wd in range(max_wdeg+1):
        coef_series = Integer(0)
        for b in U:
            Ub_w_coef = Poly(U[b], w).coeff_monomial(w**wd)
            coef_series += Ub_w_coef * T**b / factorial(b)
        coef_series = expand(coef_series)
        if coef_series == 0: continue
        print(f"\n  Coefficient of w^{wd}:")
        for b in range(B_MAX+1):
            c = Poly(coef_series, T).as_dict().get((b,), Integer(0))
            if c != 0:
                print(f"    T^{b}/b!:  {factor(expand(c * factorial(b)))}")

    # (5) Try to write U_b(w) as a product ∏ (something).
    print("\n" + "="*78)
    print("Attempt to factor U_b(w) directly (as polynomial in w, coeffs in E1,E2):")
    print("="*78)
    for b in range(2, B_MAX+1):
        f = factor(U[b])
        print(f"\n  U_{b}(w) = {f}")

    # (6) Row of U_b at w = -1, w = -φ_1, etc. — probe special values
    print("\n" + "="*78)
    print("Special values:")
    print("="*78)
    for b in range(2, B_MAX+1):
        Um1 = factor(expand(U[b].subs(w, -1)))
        U0 = factor(expand(U[b].subs(w, 0)))
        Uneg_phi = factor(expand(U[b].subs(w, -phi1)))
        Uphi_m1 = factor(expand(U[b].subs(w, phi1 - 1)))
        print(f"\n  b={b}: U(-1) = {Um1}")
        print(f"        U(-φ_1) = {Uneg_phi}")


if __name__ == '__main__':
    main()
