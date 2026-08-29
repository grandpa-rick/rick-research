"""Day 118 — Explore closed form for d_mu = (u, pi)-wdeg of s*_mu.

Empirically for mu = (a, b, c) with ell <= 3:
  mu=(0,0,0) -> 0
  mu=(1,0,0) -> 1
  mu=(2,0,0) -> 2
  mu=(1,1,0) -> 1  <-- notably NOT 2
  mu=(3,0,0) -> 3
  mu=(2,1,0) -> 2
  mu=(1,1,1) -> 2
  mu=(4,0,0) -> 4
  mu=(3,1,0) -> 3
  mu=(2,2,0) -> 3
  mu=(2,1,1) -> 3
  mu=(5,0,0) -> 5
  mu=(4,1,0) -> 4
  mu=(3,2,0) -> 4
  mu=(3,1,1) -> 4
  mu=(2,2,1) -> 3

Conjecture: d_mu = |mu| - min(mu_2, floor(mu_3/1?)) ... let's see.

Let's just print differences.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from sympy import symbols, expand

u, y, c = symbols('u y c')

if __name__ == "__main__":
    xs = (u, y, c)
    print(f"{'mu':>15} {'|mu|':>5} {'d_mu':>5} {'|mu|-d_mu':>10}")
    for N in range(11):
        for mu in all_partitions_len_le_3(N):
            s = factorial_schur(mu, xs)
            d = joint_u_pi_deg(substitute_sigma_pi(s))
            defect = N - d
            print(f"{str(mu):>15} {N:>5} {d:>5} {defect:>10}")
