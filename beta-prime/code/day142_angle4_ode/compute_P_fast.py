"""
Fast(er) P_b construction.  Builds P_b in (E_1, E_2, E_3) then substitutes.
For specific values of (U, V) we can plug in (E_1, E_2) numerically then work in E_3 only.
"""

import sys, os
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, E1, E2, E3
from sympy import symbols, expand, Integer, Rational, Poly, rf, factorial

U, V = symbols('U V')

def compute_P_at(U_val, V_val, B_max):
    """Compute P_b(U_val, V_val, E_3) for b = 0..B_max.
    U_val, V_val are (possibly symbolic) values with which to substitute E_1 = U_val+V_val-2, E_2 = U_val V_val - U_val - V_val + 1.
    Returns dict {b: polynomial in E_3}.
    """
    P = build_P(B_max)
    E1_val = U_val + V_val - 2
    E2_val = U_val * V_val - U_val - V_val + 1
    out = {}
    for b in range(B_max + 1):
        Pb = P[b].subs([(E1, E1_val), (E2, E2_val)], simultaneous=True)
        out[b] = expand(Pb)
    return out

def compute_P_UV_full(B_max):
    """Full (U, V, E_3) polynomial version."""
    return compute_P_at(U, V, B_max)

if __name__ == '__main__':
    import time
    t0 = time.time()
    # Numeric test: (U, V) = (2, 3).  See if we get sensible polynomials.
    P_23 = compute_P_at(2, 3, 12)
    print(f"P at (U,V)=(2,3) built in {time.time()-t0:.1f}s")
    for b in range(6):
        print(f"P_{b} = {P_23[b]}")

    t1 = time.time()
    P_00 = compute_P_at(0, 0, 18)
    print(f"\nP at (U,V)=(0,0) up to b=18 built in {time.time()-t1:.1f}s")
    for b in range(8):
        print(f"P_{b} = {P_00[b]}")

    t2 = time.time()
    P_full = compute_P_UV_full(12)
    print(f"\nFull P in (U,V,E_3) up to b=12 built in {time.time()-t2:.1f}s")
