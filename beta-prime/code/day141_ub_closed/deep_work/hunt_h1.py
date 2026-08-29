"""Hunt for closed form of h_1(T) := [E_3^1] F̃(T) / F̃|_{E_3=0}(T)
in the (x, y) coordinates.

We know:
- F̃(T)|_{E_3=0} = Σ_b (x+1)_b (y+1)_b T^b/b!  (a hypergeometric)
- Top-weight h_1^{top}(T) = M(T) = Σ_{n≥2} (-1)^{n-1}(n^2-1)/n E_1^{n-2} T^n
- log F̃ has E_3^2 T^5 term = 27/5 (nontrivial), so F̃ ≠ f · exp(E_3 h_1)

Extract h_1(T) coefficients and look for pattern.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, sigma, E1, E2, E3
from sympy import (symbols, expand, factor, Poly, Integer, Rational,
                    simplify, series, rf, together, collect, cancel)

x, y = symbols('x y')
T = symbols('T')

def to_xy(P):
    return expand(P.subs([(E1, -(x+y)), (E2, x*y)], simultaneous=True))

def build_Psi(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return Psi

def extract_E3_coeff_k(P, k):
    from sympy import Poly
    return Poly(P, E3).coeff_monomial(E3**k)

def main():
    from sympy import factorial
    B_MAX = 8
    Psi = build_Psi(B_MAX)

    # Convert to (x, y, E3):
    Psi_xy = {b: to_xy(Psi[b]) for b in Psi}

    # F̃|_{E_3=0} in (x, y):
    # r_data[b][k] = [E_3^k] Ψ_b in (x, y)
    r_data = {}
    for b in range(B_MAX + 1):
        pd = {}
        for k in range(b // 2 + 1):
            pd[k] = expand(extract_E3_coeff_k(Psi_xy[b], k))
        r_data[b] = pd

    # Formal EGF variable T
    # F0(T) = Σ r_data[b][0] T^b / b!
    # F1(T) = Σ r_data[b][1] T^b / b!
    # h_1(T) = F1(T) / F0(T)  (formal power series in T)
    print("Computing h_1(T) = F1(T)/F0(T) via series division")
    print("(where F1 = Σ [E_3^1]Ψ_b T^b/b!, F0 = Σ [E_3^0]Ψ_b T^b/b!)")
    print()

    # Compute h_1(T) coefficients iteratively.
    # F1(T) = F0(T) * h_1(T)
    # Let h_1(T) = Σ_n h_n T^n. Extract h_n.
    F0 = {b: r_data[b].get(0, Integer(0)) for b in range(B_MAX + 1)}
    F1 = {b: r_data[b].get(1, Integer(0)) for b in range(B_MAX + 1)}

    # Convert F1_b = Σ_{k=0}^b h_{b-k} F0_k · C(b, k) [using EGF convolution]
    # Actually EGF: [T^b/b!] F1 = Σ_{k=0}^b C(b, k) [T^k/k!]F0 · [T^{b-k}/(b-k)!]h_1
    # But h_1 could be OGF or EGF. Let me set h_1 as an OGF? No, EGF makes sense.
    # Let h_1(T) = Σ h_n T^n/n! (EGF). Then F1_b = Σ C(b, k) F0_k h_{b-k}.
    # But h_1 might not be an EGF, it might be a normal OGF. Let me try OGF:
    # F1(T) as EGF = F0(T) as EGF · h_1(T) as OGF? No, that mixes types.

    # Cleanest: define A(T) = F1(T), B(T) = F0(T), both as formal series in T
    # (coefficients being (x+1)_b(y+1)_b/b!, r̃_b^(1)/b! respectively).
    # Then h(T) := A(T)/B(T) as a series in T.
    # Compute coefficients [T^n] h up to n = B_MAX.

    A_coefs = {b: F1[b] / factorial(b) for b in range(B_MAX + 1)}
    B_coefs = {b: F0[b] / factorial(b) for b in range(B_MAX + 1)}
    # h[n] * B[0] + h[n-1]*B[1] + ... + h[0]*B[n] = A[n]
    # B[0] = 1.
    h_coefs = {}
    for n in range(B_MAX + 1):
        s = A_coefs[n]
        for k in range(0, n):
            s -= h_coefs[k] * B_coefs[n - k]
        h_coefs[n] = expand(s / B_coefs[0])
        h_coefs[n] = together(h_coefs[n])

    print("Series coefficients of h_1(T) := F1(T)/F0(T):")
    for n in range(B_MAX + 1):
        h_n_fact = factor(h_coefs[n])
        print(f"\n  [T^{n}] h_1(T) = {h_n_fact}")

    # Also print the TOP-weight M(T) coefficients for comparison
    print("\n" + "="*78)
    print("Top-weight M(T) for comparison (E_1 = -(x+y)):")
    from sympy import log
    print("  M(T) = (1/E_1^2)[E_1 T/(1+E_1 T)^2 - log(1+E_1 T)]")
    print("  Expand around T=0:")
    for n in range(2, B_MAX + 1):
        c = (-1)**(n-1) * (n*n - 1) / n * (-(x+y))**(n-2)  # E_1^{n-2} with E_1 = -(x+y)
        print(f"    [T^{n}] M(T) = {factor(c)}")

    # DIFFERENCE: h_1[n] - M[n]
    print("\n" + "="*78)
    print("DIFFERENCE h_1[T^n] - M[T^n] (should have LOWER weight = degree in x+y, xy):")
    for n in range(2, B_MAX + 1):
        M_n = (-1)**(n-1) * (n*n - 1) * (-(x+y))**(n-2) / n
        d = expand(h_coefs[n] - M_n)
        d_fact = factor(d)
        print(f"\n  [T^{n}] (h_1 - M) = {d_fact}")

if __name__ == '__main__':
    main()
