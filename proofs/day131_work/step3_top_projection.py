"""Project the FULL recursion:
  Psi_{b+1} = [E_2 - (b+1) E_1 + (b+1)^2] Psi_b
              - 3b E_3 sigma(Psi_{b-1})
              - b(b-1)(E_1 - 2b - 2) E_3 sigma(Psi_{b-2})

to top-weight. sigma_top is a ring endomorphism of Q[E_1, E_2, E_3]:
  sigma_top(E_1) = E_1
  sigma_top(E_2) = E_2 - 2 E_1
  sigma_top(E_3) = E_3

Yielding:
  tops[b+1] = (E_2 - (b+1) E_1) tops[b]
              - 3b E_3 sigma_top(tops[b-1])
              - b(b-1) E_1 E_3 sigma_top(tops[b-2])

Verify for b = 0..5.

Also: check that this is EQUIVALENT to the ODE 3-term recursion.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import expand, Poly, Integer, Symbol

def sigma_top(P):
    """Ring endomorphism: E_2 -> E_2 - 2 E_1, others fixed."""
    return expand(P.subs(E2, E2 - 2*E1))

tops = {-2: Integer(0), -1: Integer(0)}
tops[0] = Integer(1)
for b in range(1, 7):
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    tops[b] = top_weight_part(psi_e, b)
    print(f"tops[{b}] = {tops[b]}", flush=True)

print("\n=== TOP-WEIGHT RECURSION CHECK ===")
for b in range(0, 6):
    lhs = tops[b+1]
    rhs = expand(
        (E2 - (b+1) * E1) * tops[b]
        - 3 * b * E3 * sigma_top(tops[b-1])
        - b * (b-1) * E1 * E3 * sigma_top(tops[b-2])
    )
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: {'OK' if diff_val == 0 else 'FAIL diff=' + str(diff_val)}")

print("\n=== Sanity: equivalent to ODE 3-term recursion? ===")
# ODE version: tops[b+1] = (E_2 - (3b+1) E_1) tops[b]
#                        + b [2 E_1 E_2 - (3b-1) E_1^2 - 3 E_3] tops[b-1]
#                        + b(b-1) [E_1^2 E_2 - (b-1) E_1^3 - E_1 E_3] tops[b-2]
for b in range(0, 6):
    ode = expand(
        (E2 - (3*b+1) * E1) * tops[b]
        + b * (2 * E1 * E2 - (3*b-1) * E1**2 - 3 * E3) * tops[b-1]
        + b * (b-1) * (E1**2 * E2 - (b-1) * E1**3 - E1 * E3) * tops[b-2]
    )
    top_proj = expand(
        (E2 - (b+1) * E1) * tops[b]
        - 3 * b * E3 * sigma_top(tops[b-1])
        - b * (b-1) * E1 * E3 * sigma_top(tops[b-2])
    )
    diff_val = expand(ode - top_proj)
    print(f"  b={b}: ODE-vs-top-projection diff = {diff_val}")
