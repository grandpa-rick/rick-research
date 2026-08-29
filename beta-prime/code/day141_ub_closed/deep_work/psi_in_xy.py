"""
Compute Ψ_b for b = 0..8 in (x, y, E_3) coordinates where E_1 = -(x+y), E_2 = xy.
Ψ_b|_{E_3 = 0} = (x+1)_b (y+1)_b (rising factorials).
Extract r̃_b^{(k)} = [E_3^k] Ψ_b and try various factorizations.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, sigma, phi_map, E1, E2, E3, w
from sympy import (symbols, expand, factor, Poly, Integer, Rational, simplify,
                    rf, gamma, cancel, collect, together)

x, y = symbols('x y')

def to_xy(P):
    """Substitute E_1 = -(x+y), E_2 = xy."""
    return expand(P.subs([(E1, -(x + y)), (E2, x * y)], simultaneous=True))

def build_Psi(B_max):
    """Rebuild Ψ_b (not applying phi_map like build_P)."""
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return Psi

def extract_E3_coeffs(P_xy, k_max):
    """Given a polynomial in (x, y, E3), extract [E_3^k] for k = 0..k_max."""
    out = {}
    Ppoly = Poly(P_xy, E3)
    for k in range(k_max + 1):
        c = Ppoly.coeff_monomial(E3**k)
        out[k] = expand(c)
    return out

def try_rising_factorial_basis(P, degree_bound):
    """Try to express P (polynomial in x, y) as sum of terms (x+1)_a (y+1)_c · const.
    Uses symmetry in (x, y)? Not necessarily.
    Return dict {(a, c): coefficient}."""
    # Basis: (x+1)_a for a = 0..degree_bound, similarly (y+1)_c.
    # This is a change of basis. Do it symbolically.
    from sympy import rf as rising
    coefs = {}
    remaining = P
    # Try (x+1)_a (y+1)_c basis for a + c = deg down to 0.
    max_deg_x = Poly(P, x).degree() if P != 0 else 0
    max_deg_y = Poly(P, y).degree() if P != 0 else 0
    for tot in range(max_deg_x + max_deg_y, -1, -1):
        for a in range(min(tot, max_deg_x) + 1):
            c = tot - a
            if c > max_deg_y: continue
            # Coefficient of x^a y^c in remaining.
            # Actually we want to peel off using (x+1)_a (y+1)_c
            # Its top-degree term is x^a y^c.
            top_ac = Poly(remaining, x, y).coeff_monomial(x**a * y**c)
            if top_ac == 0: continue
            coefs[(a, c)] = top_ac
            remaining = expand(remaining - top_ac * rising(x + 1, a) * rising(y + 1, c))
    if expand(remaining) != 0:
        coefs['REMAINDER'] = remaining
    return coefs

def main():
    B_MAX = 6
    print(f"Building Ψ_b for b = 0..{B_MAX}\n")
    Psi = build_Psi(B_MAX)

    # First, verify Ψ_b|_{E_3=0} = (x+1)_b (y+1)_b
    print("=" * 78)
    print("VERIFY Ψ_b|_{E_3=0} = (x+1)_b (y+1)_b")
    print("=" * 78)
    from sympy import rf as rising
    for b in range(0, B_MAX + 1):
        lhs = to_xy(Psi[b].subs(E3, 0))
        rhs = expand(rising(x + 1, b) * rising(y + 1, b))
        diff = expand(lhs - rhs)
        status = "OK" if diff == 0 else f"FAIL: {diff}"
        print(f"  b={b}: {status}")

    # Extract [E_3^k] Ψ_b in (x, y).
    print("\n" + "=" * 78)
    print("r̃_b^(k) = [E_3^k] Ψ_b, in (x, y):")
    print("=" * 78)
    r_data = {}
    for b in range(0, B_MAX + 1):
        Psi_xy = to_xy(Psi[b])
        r_data[b] = extract_E3_coeffs(Psi_xy, b // 2)
        print(f"\n--- b = {b} ---")
        for k in sorted(r_data[b].keys()):
            r = r_data[b][k]
            if r == 0: continue
            r_fact = factor(r)
            print(f"  r̃_{b}^({k})  =  {r_fact}")

    # Try (x+1)_a (y+1)_c decomposition for r̃_b^(k)
    print("\n" + "=" * 78)
    print("(x+1)_a (y+1)_c BASIS DECOMPOSITION of r̃_b^(k):")
    print("=" * 78)
    for b in range(1, B_MAX + 1):
        for k in sorted(r_data[b].keys()):
            r = r_data[b][k]
            if r == 0: continue
            print(f"\n  r̃_{b}^({k}):")
            coefs = try_rising_factorial_basis(r, b)
            for (a, c) in sorted(coefs.keys(), key=lambda ac: (-(ac[0]+ac[1] if isinstance(ac, tuple) else 0), ac)):
                if isinstance((a, c), str) or a == 'REMAINDER':
                    continue
                v = coefs[(a, c)]
                if v != 0:
                    print(f"    (x+1)_{a} (y+1)_{c} · {v}")
            if 'REMAINDER' in coefs:
                print(f"    REMAINDER: {coefs['REMAINDER']}")

if __name__ == '__main__':
    main()
