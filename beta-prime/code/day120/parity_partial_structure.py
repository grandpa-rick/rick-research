"""Day 120 — Structure of A_sum(d) and B_sum(d) as polynomials in s.

From parity_split.py, we see A_sum(d) + B_sum(d) = 0 but A_sum(d) != 0 for d < d_max.

The polys A_sum(d) look highly structured. Try to detect:
  - degree in s
  - leading coefficient
  - whether A_sum(d) = -B_sum(d) always (should be yes by construction)
  - closed form for A_sum(d) as function of j and d

Plot: for each j, tabulate A_sum(d) as we go from d = d_max down to j+1.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly, factor, LC, degree

u, y, c = symbols('u y c')
t, s = symbols('t s')


def eval_ts(mu):
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def parity(mu):
    return (mu[1] - mu[2]) % 2


def get_cd(expr, d):
    p = Poly(expr, t, s)
    out = Integer(0)
    for (dt, ds), coef in p.terms():
        if dt == d:
            out += coef * s**ds
    return expand(out)


if __name__ == "__main__":
    for j in range(3, 10):
        twoj = 2 * j
        mu_evals = []
        for mu in all_mu_3parts(twoj):
            K = kostka_mu_prime_2j(mu)
            if K == 0:
                continue
            ev = eval_ts(mu)
            mu_evals.append((mu, K, ev))
        d_max = max(d_mu(mu) for mu, _, _ in mu_evals)
        print(f"=== j={j}, d_max={d_max} ===")
        for d in range(d_max, j, -1):
            A_sum = Integer(0)
            for mu, K, ev in mu_evals:
                if parity(mu) == 0:
                    A_sum += K * get_cd(ev, d)
            A_sum = expand(A_sum)
            if A_sum == 0:
                print(f"  d={d} (offset from d_max: {d - d_max}): A_sum = 0")
                continue
            deg_s = degree(A_sum, s) if A_sum != 0 else 0
            try:
                fac = factor(A_sum)
            except Exception:
                fac = A_sum
            print(f"  d={d} (offset {d - d_max}): deg_s={deg_s}, A_sum = {fac}")
