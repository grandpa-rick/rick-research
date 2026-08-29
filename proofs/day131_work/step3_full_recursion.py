"""FULL Psi recursion (not just top-weight):

  Psi_{b+1} = [E_2 - (b+1) E_1 + (b+1)^2] Psi_b
              - 3b E_3 sigma(Psi_{b-1})
              - b(b-1)(E_1 - 2b - 2) E_3 sigma(Psi_{b-2})

This is a clean 3-term (in b) recursion with sigma as the only "unusual" operator.

Verify for b = 0, 1, 2, 3, 4, 5.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom, max_weight)
from sympy import expand, Poly, Integer, factor, simplify, symbols

def sigma(p):
    return expand(p.subs({u1: u1-1, u2: u2-1, u3: u3-1}, simultaneous=True))

# Compute Psi_b as u-polynomials
psi = {0: Integer(1)}
for b in range(1, 7):
    print(f"Computing Psi_{b}...", flush=True)
    psi[b] = Psi_direct(e2_u**b)
psi[-1] = Integer(0)
psi[-2] = Integer(0)

print("\n=== FULL RECURSION CHECK ===")
for b in range(0, 6):
    lhs = psi[b+1]
    Psi_b = psi[b]
    Psi_bm1 = psi[b-1]
    Psi_bm2 = psi[b-2]
    sigma_bm1 = sigma(Psi_bm1)
    sigma_bm2 = sigma(Psi_bm2)
    rhs = expand(
        (e2_u - (b+1) * e1_u + (b+1)**2) * Psi_b
        - 3 * b * e3_u * sigma_bm1
        - b * (b-1) * (e1_u - 2*b - 2) * e3_u * sigma_bm2
    )
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: {'OK' if diff_val == 0 else 'FAIL diff=' + str(diff_val)}")
