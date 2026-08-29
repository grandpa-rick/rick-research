"""Print P_b := phi(Psi_b) for small b."""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from task1_psi_e2_b5_b6 import Psi_direct, sym_to_ebasis_direct, e2_u, E1, E2, E3
from sympy import Poly, Integer, expand


def phi(P):
    return expand(P.subs([(E1, -E1), (E2, E2), (E3, -E3)], simultaneous=True))


def tau(P):
    return expand(P.subs([(E1, E1+3), (E2, 2*E1+E2+3), (E3, E1+E2+E3+1)], simultaneous=True))


for b in range(0, 6):
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    Pb = phi(psi_e)
    print(f"\n=== b={b} ===")
    print(f"Psi_{b} = {expand(psi_e)}")
    print(f"P_{b}   = {Pb}")


print("\n\ntau on small polys:")
print(f"tau(1) = {tau(Integer(1))}")
print(f"tau(E1) = {tau(E1)}")
print(f"tau(E2) = {tau(E2)}")
print(f"tau(E3) = {tau(E3)}")
