"""Day 141 — Attack angle (a): find closed form for U_b(w) via EGF substitution.

RESULT SUMMARY (see comments and companion scripts):

Attack angle (a) assumed:  F_140(T) = A(T) · exp(E3 · M(T))
so that substituting E3 = w - φ_1 factorizes nicely.

HOWEVER: Day 140's P_b (built by verify_gf_form.build_P) does NOT satisfy this
factorization. We verified in `factor_day140_egf.py`:
    log F_140(T) has NON-TRIVIAL E3^2 coefficient starting at T^5 (namely 27/5 · E3^2 T^5)
    and E3^3 coefficients at higher T-orders.

For comparison, Day 130's ORIGINAL P (top-weight of Ψ(e_2^b)) DOES factorize this way,
but Day 140 is working with a different (transformed) family — see the "sigma" and
"phi_map" operators in verify_gf_form.py that build a different recursion.

So attack angle (a) as stated FAILS at step 0.

FALLBACK: compute U_b(w) directly from its definition
    U_b(w) := (P_b|_{E3 = w - φ_1} - p_b) / (w - φ_1)
and report the polynomials + patterns. See `direct_Ub.py` for full run.

BEST GUESS at closed form:  the EGF has the honest divided-difference expression
    Σ_b U_b(w) T^b/b! = (F_140(T)|_{E3 = w - φ_1} - H(T)) / (w - φ_1)
where H(T) = Σ p_b T^b/b!. But F_140 itself has no obvious closed form.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3, w

from sympy import (symbols, expand, Poly, Integer, factorial, Rational, factor,
                   div, log, exp, Symbol)

T = symbols('T')

def truncate_T(expr, order):
    p = Poly(expr, T)
    out = Integer(0)
    for deg, coef in p.as_dict().items():
        if deg[0] <= order:
            out += coef * T**deg[0]
    return out


def main():
    B_MAX = 8
    print(f"Building Day 140 P_b for b = 0..{B_MAX}")
    P = build_P(B_MAX)
    phi1 = phi_k(1)   # = E2 + E1 + 1

    # === Step 1: Direct computation of U_b(w) ===
    U = {}
    for b in range(2, B_MAX+1):
        Pshift = expand(P[b].subs(E3, w - phi1))
        numer = expand(Pshift - p_b_fn(b))
        q, r = div(numer, w - phi1, w)
        if expand(r) != 0:
            print(f"  b={b}: division remainder = {r}")
            continue
        U[b] = expand(q)

    print("\n" + "="*78)
    print("U_b(w) for b = 2..8  (Day 140's P_b, direct from definition)")
    print("="*78)
    for b in range(2, B_MAX+1):
        Uq = Poly(U[b], w)
        print(f"\n  U_{b}(w) [deg_w = {Uq.degree()}]:")
        for d in range(Uq.degree()+1):
            c = Uq.coeff_monomial(w**d)
            if c != 0:
                print(f"    [w^{d}]  {factor(expand(c))}")

    # === Step 2: probe pretend-EGF-factorization to confirm it fails ===
    print("\n" + "="*78)
    print("VERIFICATION that F_140 does NOT factor as A(T) · exp(E3 · M(T))")
    print("="*78)
    F = Integer(0)
    for b in range(B_MAX+1):
        F += P[b] * T**b / factorial(b)
    F = expand(F)

    # Compute log F to check E3-linearity
    Fm1 = expand(F - 1)
    logF = Integer(0)
    current = Integer(1)
    for k in range(1, B_MAX+1):
        current = truncate_T(expand(current * Fm1), B_MAX)
        logF += (-1)**(k-1) * current / k
    logF = expand(logF)

    print("Highest E3-power in log F (as truncated series) by T-order:")
    logF_poly_T = Poly(logF, T)
    for n in range(B_MAX+1):
        c = logF_poly_T.as_dict().get((n,), Integer(0))
        c = expand(c)
        if c == 0:
            continue
        cP = Poly(c, E3) if c != 0 else None
        max_e3 = cP.degree() if cP is not None else 0
        e3_coeffs = {}
        for d in range(max_e3+1):
            ck = cP.coeff_monomial(E3**d)
            if ck != 0:
                e3_coeffs[d] = ck
        print(f"  T^{n}: max E3-degree = {max_e3}, E3-degrees present = {sorted(e3_coeffs.keys())}")

    print("\nConclusion: if log F had ONLY E3^0 and E3^1 terms, F = H·exp(E3·M) would work.")
    print("But E3^2 appears at T^5 and E3^3 at higher orders, so factorization fails.")

    # === Step 3: honest EGF closed form ===
    print("\n" + "="*78)
    print("HONEST EGF CLOSED FORM")
    print("="*78)
    print("""
    Σ_b U_b(w) T^b/b! = [F_140(T)|_{E3 = w - φ_1} - H(T)] / (w - φ_1)

where:
    H(T) = Σ_b p_b T^b/b!,   p_b = ∏_{k=1}^b (E2 + kE1 + k²),   φ_1 = E2 + E1 + 1.

This is a legitimate closed form of the EGF but F_140(T) itself does not have
a compact known closed form (unlike Day 130's Ψ, whose EGF was A·exp(E3·M)).
Attack angle (a) does NOT yield a simplification.
""")

    # === Step 4: patterns observed ===
    print("="*78)
    print("PATTERNS SEEN")
    print("="*78)
    print("""
1. Leading coefficient of U_b (in w) at highest degree ⌊(b-2)/2⌋:
     b=2: 3
     b=4: 27
     b=6: 405
     b=8: 8505
   Ratios 9, 15, 21 = 3(2d+1); so LC(b=2d+2) = ∏_{j=1}^{d+1} 3(2j-1) = 3 · 9 · 15 · 21 · ...

2. For odd b, the leading coefficient is a polynomial in E1, E2:
     b=3: 25 E1 + 9 E2 + 57
     b=5: 3(205 E1 + 45 E2 + 741)
     b=7: 189(95 E1 + 15 E2 + 471)

3. U_b(0) and U_b(φ_1) do not obviously factor.

4. Attack angle (a) is blocked; further attack should try:
   (i)  factor Day 140's log F structurally (why does E3^2 appear at T^5?)
   (ii) find a substitution E3 = f(w, T, E1, E2) that DOES linearize the recursion
   (iii) study U_b(w) as a divided difference in a broader interpolation family
""")


if __name__ == "__main__":
    main()
