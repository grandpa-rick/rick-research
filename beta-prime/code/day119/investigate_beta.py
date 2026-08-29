"""Compute beta_mu = constant term of bar s*_mu(s) for mu at d_max, odd j.
Look for a pattern.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from compute_bar_s import bar_s_mu
import sympy as sp
from sympy import Poly, symbols, expand, Integer

s = symbols('s')

def alpha_beta(mu):
    bs = bar_s_mu(mu)
    p = Poly(bs, s)
    coeffs = p.all_coeffs()[::-1]  # constant first
    beta = coeffs[0] if len(coeffs) > 0 else 0
    alpha = coeffs[1] if len(coeffs) > 1 else 0
    return alpha, beta


if __name__ == "__main__":
    print("=== alpha, beta for mu = (2l+1, l+1+m, l-m) ===\n")
    for l in range(1, 6):
        print(f"--- l = {l} (j = {2*l+1}) ---")
        for m in range(l + 1):
            mu = (2*l+1, l+1+m, l-m)
            alpha, beta = alpha_beta(mu)
            print(f"  mu = {mu}: alpha = {alpha}, beta = {beta}")
        print()
