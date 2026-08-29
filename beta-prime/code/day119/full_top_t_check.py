"""Check that sum_{d_mu = d_max} K_{mu',(2^j)} * bar s*_mu(s) = 0 as polynomial in s."""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts
from compute_bar_s import bar_s_mu
from sympy import expand, Integer, symbols, Poly

s = symbols('s')

if __name__ == "__main__":
    for j in range(1, 8):
        twoj = 2 * j
        # find d_max
        d_max = 0
        support = []
        for mu in all_mu_3parts(twoj):
            K = kostka_mu_prime_2j(mu)
            if K > 0:
                support.append((mu, d_mu(mu), K))
                d_max = max(d_max, d_mu(mu))
        top = [(mu, K) for (mu, d, K) in support if d == d_max]
        # sum
        total = Integer(0)
        for mu, K in top:
            bs = bar_s_mu(mu)
            total += K * bs
        total = expand(total)
        status = "OK (vanishes)" if total == 0 else f"!!! = {total}"
        print(f"j={j}, d_max={d_max}: sum = {total}  {status}")
