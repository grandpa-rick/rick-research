"""Test the ODE-derived 3-term recursion:

  tops[b+1] = (E_2 - (3b+1) E_1) tops[b]
            + b * [2 E_1 E_2 - (3b-1) E_1^2 - 3 E_3] tops[b-1]
            + b(b-1) * [E_1^2 E_2 - (b-1) E_1^3 - E_1 E_3] tops[b-2]

for b = 0..5.  If this holds, then F' = ((E_2-E_1)/(1+E_1 T) - E_3 T (3+E_1 T)/(1+E_1 T)^3) F.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import expand, Poly, Integer

def get_tops(bmax):
    tops = {}
    tops[-1] = Integer(0)
    tops[-2] = Integer(0)
    for b in range(0, bmax+1):
        print(f"Computing tops[{b}]...", flush=True)
        psi_u = Psi_direct(e2_u**b) if b > 0 else Integer(1)
        psi_e = sym_to_ebasis_direct(psi_u) if psi_u != 1 else Integer(1)
        tops[b] = top_weight_part(psi_e, b)
    return tops

def test_recursion(tops, bmax):
    print("\n=== ODE 3-term recursion check ===")
    for b in range(0, bmax):
        lhs = tops[b+1]
        c_b = E2 - (3*b+1)*E1
        c_bm1 = 2*E1*E2 - (3*b-1)*E1**2 - 3*E3
        c_bm2 = E1**2 * E2 - (b-1)*E1**3 - E1*E3
        rhs = expand(
            c_b * tops[b]
            + b * c_bm1 * tops[b-1]
            + b*(b-1) * c_bm2 * tops[b-2]
        )
        diff = expand(lhs - rhs)
        status = 'OK' if diff == 0 else f'FAIL diff={diff}'
        print(f"  b={b}: {status}")

if __name__ == '__main__':
    tops = get_tops(6)
    test_recursion(tops, 6)
