"""C1: Derive beta_m = constant term of bar s*_{mu}(s) for mu = (2l+1, l+1+m, l-m).

Conjecture (verified l <= 5): beta_m = (-1)^{m+1} [(m+1)(2l+1) - delta_{m,l}].

Strategy 1: Compute directly for many (l, m) via existing bar_s_mu; extract polynomial pattern.
Strategy 2: Analytic derivation via Molev-Sagan or via expansion of s^*_mu at u=y=c=0-ish.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

import sympy as sp
from sympy import symbols, expand, Poly, Integer, simplify, factor
from compute_bar_s import bar_s_mu

s = symbols('s')


def alpha_beta(mu):
    bs = bar_s_mu(mu)
    p = Poly(bs, s)
    coeffs = p.all_coeffs()[::-1]  # constant first
    beta = coeffs[0] if len(coeffs) > 0 else Integer(0)
    alpha = coeffs[1] if len(coeffs) > 1 else Integer(0)
    return alpha, beta


def survey(max_l=6):
    print("=== beta_m for odd-parity spine mu = (2l+1, l+1+m, l-m) ===\n")
    print("l  m  mu               alpha  beta  conjecture   match")
    for l in range(1, max_l+1):
        for m in range(l+1):
            mu = (2*l+1, l+1+m, l-m)
            if mu[2] < 0: continue
            alpha, beta = alpha_beta(mu)
            conj = (-1)**(m+1) * ((m+1)*(2*l+1) - (1 if m == l else 0))
            match = "OK" if beta == conj else "!!!"
            print(f"{l:2} {m:2}  {str(mu):15}  {int(alpha):+3}   {int(beta):+4}    {conj:+4}    {match}")


def survey_all_ell():
    print("\n=== EXTENDED beta_m survey up to l = 8 ===\n")
    conjectured = True
    for l in range(1, 9):
        for m in range(l+1):
            mu = (2*l+1, l+1+m, l-m)
            if mu[2] < 0: continue
            try:
                alpha, beta = alpha_beta(mu)
            except Exception as e:
                print(f"l={l}, m={m}: ERROR {e}")
                continue
            conj = (-1)**(m+1) * ((m+1)*(2*l+1) - (1 if m == l else 0))
            if beta != conj:
                conjectured = False
                print(f"l={l}, m={m}: beta={beta}, conj={conj}  MISMATCH!")
        print(f"l={l}: {'all match' if conjectured else 'MISMATCH FOUND'}")


if __name__ == "__main__":
    survey(6)
    survey_all_ell()
