"""
Day 142 Angle-4 / ODE — compute P_b in (U, V, E_3) coordinates for b = 0..B_MAX.

We use the same build_P from day140_interior/verify_gf_form.py and the
substitution E_1 = U+V-2, E_2 = UV - U - V + 1 (i.e. u = U-1, v = V-1
where E_1 = u+v, E_2 = uv).

Under this substitution:
  p_b = phi_1(0)*phi_2*...*phi_b evaluates to (U)_b (V)_b (rising factorials).
  phi_1 = E_2 + E_1 + 1 = UV.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, E1, E2, E3
from sympy import symbols, expand, Integer, rf

U, V = symbols('U V')

def to_UV(P):
    """Substitute E_1 = U + V - 2, E_2 = UV - U - V + 1 (i.e. u=U-1, v=V-1)."""
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, U + V - 2), (E2, U*V - U - V + 1)], simultaneous=True))

def compute_P_UV(B_max):
    """Return dict {b: P_b(U, V, E_3)} for b = 0..B_max, expanded."""
    P = build_P(B_max)
    return {b: to_UV(P[b]) for b in range(B_max + 1)}

def check_pb_leading(P_UV_dict):
    """Check that P_b|_{E_3 = 0} = (U)_b (V)_b."""
    ok = True
    for b, Pb in P_UV_dict.items():
        pb0 = expand(Pb.subs(E3, 0))
        expected = expand(rf(U, b) * rf(V, b))
        if expand(pb0 - expected) != 0:
            print(f"  b={b}: MISMATCH  {pb0} vs {expected}")
            ok = False
    return ok

if __name__ == '__main__':
    B_MAX = 12
    print(f"Computing P_b in (U, V, E_3) for b = 0..{B_MAX}")
    P_UV = compute_P_UV(B_MAX)
    print("Sanity check: P_b|_{E_3=0} = (U)_b (V)_b ...")
    if check_pb_leading(P_UV):
        print("  ALL OK")
    for b in range(min(B_MAX, 5) + 1):
        print(f"\nP_{b}(U,V,E_3) =")
        print(f"  {P_UV[b]}")
