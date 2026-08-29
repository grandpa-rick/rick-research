"""Push Rick's route_v_probe further: check deg_t S_j for j up to 10 or higher."""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from route_v_probe import bt_tables, ds_uyc, substitute_sigma_pi, joint_u_pi_deg
import sympy as sp
from sympy import symbols, expand, Poly, Integer, div

u, y, c = symbols('u y c')
sig, pi = symbols('sigma pi')

if __name__ == "__main__":
    JMAX = 8
    T = bt_tables(JMAX)
    print(f"Compute deg_(u,pi) S_j for j <= {JMAX}\n")
    print(f"{'j':>3} {'expected':>10} {'(u,pi)-deg S_j':>18}")
    print('-' * 40)
    for j in range(JMAX + 1):
        dsj = ds_uyc(j, T)
        V_full = (u - y) * (u - c) * (y - c)
        q, r = div(Poly(dsj, u, y, c), Poly(expand(V_full), u, y, c))
        if r.as_expr() != 0:
            print(f"j={j}: DIVISION FAILED")
            continue
        S_uyc = q.as_expr()
        S_sigpi = substitute_sigma_pi(S_uyc)
        S_deg = joint_u_pi_deg(S_sigpi)
        status = "OK" if S_deg <= j else f"!!! EXCEEDS {j}"
        print(f"{j:>3} {j:>10} {S_deg:>18}  {status}")
