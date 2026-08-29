"""
P_b in (U, V, E_3) coordinates where U = u+1, V = v+1.
Then p_b = (U)_b (V)_b (rising factorials) and φ_1 = UV.

Express r_b^(k) as polynomial in U, V and try (U)_a (V)_c basis decomposition
(where (U)_a = U(U+1)...(U+a-1) is rising factorial).

Also compute Û_b(w) := U_b evaluated at w. We have:
Û_b(w) = (P̂_b|_{E_3 = w - UV} - (U)_b (V)_b) / (w - UV)
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, E1, E2, E3, w
from sympy import (symbols, expand, factor, Poly, Integer, Rational,
                    simplify, rf, together, collect, cancel, div, sympify)

U, V = symbols('U V')

def to_UV(P):
    """Substitute E_1 = U + V - 2, E_2 = UV - U - V + 1."""
    return expand(P.subs([(E1, U + V - 2), (E2, U*V - U - V + 1)], simultaneous=True))

def try_rising_UV_basis(P, U_var, V_var, deg_bound):
    """Express P(U, V) as sum c_{a, c} (U)_a (V)_c."""
    coefs = {}
    remaining = P
    max_dU = Poly(P, U_var).degree() if P != 0 else 0
    max_dV = Poly(P, V_var).degree() if P != 0 else 0
    for tot in range(max_dU + max_dV, -1, -1):
        for a in range(min(tot, max_dU) + 1):
            c = tot - a
            if c > max_dV: continue
            # Peel off (U)_a (V)_c using top monomial U^a V^c.
            top_ac = Poly(remaining, U_var, V_var).coeff_monomial(U_var**a * V_var**c)
            if top_ac == 0: continue
            coefs[(a, c)] = top_ac
            remaining = expand(remaining - top_ac * rf(U_var, a) * rf(V_var, c))
    if expand(remaining) != 0:
        coefs['REM'] = remaining
    return coefs

def main():
    B_MAX = 8
    print(f"Building P_b for b = 0..{B_MAX}\n")
    P = build_P(B_MAX)

    P_UV = {b: to_UV(P[b]) for b in P}

    # Extract r_b^(k) in (U, V)
    print("=" * 78)
    print("r_b^(k) = [E_3^k] P_b in (U, V) = (u+1, v+1) basis:")
    print("=" * 78)
    r_data = {}
    for b in range(B_MAX + 1):
        pd = {}
        Pp = Poly(P_UV[b], E3)
        for k in range(b // 2 + 1):
            pd[k] = expand(Pp.coeff_monomial(E3**k))
        r_data[b] = pd
        print(f"\n--- b = {b} ---")
        for k in sorted(pd.keys()):
            r = pd[k]
            if r == 0: continue
            print(f"  r_{b}^({k}):")
            coefs = try_rising_UV_basis(r, U, V, b)
            # Print in order of a + c descending
            def sort_key(k):
                if isinstance(k, str):
                    return (-1, 0, 0)
                a, c = k
                return (-(a + c), a, c)
            for key in sorted(coefs.keys(), key=sort_key):
                if key == 'REM':
                    print(f"    REMAINDER (shouldn't happen): {coefs[key]}")
                else:
                    a, c = key
                    coef = coefs[key]
                    if coef != 0:
                        print(f"    (U)_{a} (V)_{c}  ·  {coef}")

if __name__ == '__main__':
    main()
