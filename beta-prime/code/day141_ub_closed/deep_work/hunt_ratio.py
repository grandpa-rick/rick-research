"""
Hunt for closed form of F_P(T; U, V, E_3) in terms of f(T; U, V) := Σ (U)_b(V)_b T^b/b!.

Observation from data:
- LEADING (U)_{b-2k}(V)_{b-2k} coefficient of r_b^(k) is 3^k(2k-1)!! · C(b, 2k)
- This means TOP-in-UV part of F_P is f(T) · exp(3 E_3 T^2 / 2).

Question: Does F_P / f = clean function of T, E_3, U, V?

Compute F_P/f as a series in T and look for closed form.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, E1, E2, E3
from sympy import (symbols, expand, factor, Poly, Integer, Rational,
                    simplify, rf, together, collect, cancel, sqrt, exp,
                    factorial)

U, V = symbols('U V')
T = symbols('T')

def to_UV(P):
    return expand(P.subs([(E1, U + V - 2), (E2, U*V - U - V + 1)], simultaneous=True))

def main():
    B_MAX = 10
    print(f"Building P_b for b = 0..{B_MAX}\n")
    P = build_P(B_MAX)
    P_UV = {b: to_UV(P[b]) for b in P}

    # f(T; U, V) := Σ_b (U)_b (V)_b T^b/b!  as OGF in T
    # F_P(T; U, V, E_3) := Σ_b P_b(U, V, E_3) T^b/b!  as OGF in T (coefs in E_3, U, V)
    # Compute h := F_P/f as OGF in T (coefs in E_3, U, V)

    f_coefs = {b: expand(rf(U, b) * rf(V, b) / factorial(b)) for b in range(B_MAX + 1)}
    g_coefs = {b: expand(P_UV[b] / factorial(b)) for b in range(B_MAX + 1)}

    h_coefs = {}
    for n in range(B_MAX + 1):
        s = g_coefs[n]
        for k in range(0, n):
            s = expand(s - f_coefs[n - k] * h_coefs[k])
        h_coefs[n] = expand(s / f_coefs[0])

    print("h(T) := F_P/f computed as OGF in T (coefs in E_3, U, V):")
    for n in range(B_MAX + 1):
        h_n = h_coefs[n]
        if h_n == 0:
            print(f"\n  [T^{n}] h = 0")
        else:
            # Print each E_3 power separately for clarity
            h_poly_E3 = Poly(h_n, E3)
            print(f"\n  [T^{n}] h:")
            for k in range(h_poly_E3.degree() + 1):
                c = h_poly_E3.coeff_monomial(E3**k)
                if c != 0:
                    c_fact = factor(expand(c))
                    print(f"    [E_3^{k}]: {c_fact}")

    # Also try: extract exp(3 E_3 T^2 / 2) as a factor.
    # Compute h' := h · exp(-3 E_3 T^2/2) and see if it's cleaner.
    print("\n" + "=" * 78)
    print("Alternative: h' := h · exp(-3 E_3 T^2/2). Compute [T^n] h'.")
    print("=" * 78)
    # Let alpha(T) = exp(-3 E_3 T^2/2) = Σ (-3E_3/2)^k T^{2k}/k!
    alpha = {}
    for m in range(B_MAX + 1):
        if m % 2 == 0:
            alpha[m] = expand(Rational(-3, 2)**(m//2) * E3**(m//2) / factorial(m//2))
        else:
            alpha[m] = Integer(0)

    hprime = {}
    for n in range(B_MAX + 1):
        s = Integer(0)
        for k in range(n + 1):
            s = expand(s + h_coefs[n - k] * alpha[k])
        hprime[n] = s

    print("h'(T) := h(T) · exp(-3 E_3 T^2 / 2), collected by E_3 power:")
    for n in range(B_MAX + 1):
        hp_n = hprime[n]
        if hp_n == 0:
            print(f"\n  [T^{n}] h' = 0")
            continue
        hp_poly_E3 = Poly(hp_n, E3)
        print(f"\n  [T^{n}] h':")
        for k in range(hp_poly_E3.degree() + 1):
            c = hp_poly_E3.coeff_monomial(E3**k)
            if c != 0:
                c_fact = factor(expand(c))
                print(f"    [E_3^{k}]: {c_fact}")

if __name__ == '__main__':
    main()
