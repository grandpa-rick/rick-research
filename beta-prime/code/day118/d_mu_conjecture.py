"""Verify the closed-form conjecture:
   d_mu = mu_1 + floor((mu_2 + mu_3) / 2)
for all mu with ell(mu) <= 3.

This is important because if it holds we can compute d_mu (and d_lambda for
lambdas that can appear in the shifted Pieri) instantly without any SymPy.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from sympy import symbols

u, y, c = symbols('u y c')

def d_conj(mu):
    mu = tuple(list(mu) + [0] * (3 - len(mu)))
    return mu[0] + (mu[1] + mu[2]) // 2

if __name__ == "__main__":
    xs = (u, y, c)
    all_ok = True
    n = 0
    for N in range(11):
        for mu in all_partitions_len_le_3(N):
            n += 1
            s = factorial_schur(mu, xs)
            d = joint_u_pi_deg(substitute_sigma_pi(s))
            d_pred = d_conj(mu)
            if d != d_pred:
                print(f"MISMATCH: mu = {mu}, actual d = {d}, predicted = {d_pred}")
                all_ok = False
    print(f"Tested {n} cases. Formula d_mu = mu_1 + floor((mu_2+mu_3)/2): OK = {all_ok}")
