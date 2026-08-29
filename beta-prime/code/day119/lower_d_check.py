"""Check what happens at d < d_max. Compute [t^d] S_j directly using the shifted-Schur code,
verifying that it vanishes as a polynomial in s."""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly

u, y, c = symbols('u y c')
t, s = symbols('t s')


def evaluate_s_star_at_ts(mu):
    """Return s*_mu(u=t, sigma=s, pi=t) as a poly in t, s."""
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def check_full_S_j():
    for j in [3, 4, 5, 6]:
        twoj = 2 * j
        S = Integer(0)
        for mu in all_mu_3parts(twoj):
            K = kostka_mu_prime_2j(mu)
            if K == 0:
                continue
            S += K * evaluate_s_star_at_ts(mu)
        S = expand(S)
        p = Poly(S, t, s)
        # find max deg_t
        max_dt = 0
        for (dt, ds), coef in p.terms():
            max_dt = max(max_dt, dt)
        print(f"j={j}: deg_t S_j = {max_dt} (expected {j})")
        # print all [t^d] for d > j
        for d in range(j+1, max_dt + 2):
            coef_d = Integer(0)
            for (dt, ds), coef in p.terms():
                if dt == d:
                    coef_d += coef * s**ds
            coef_d = expand(coef_d)
            print(f"  [t^{d}] S_j = {coef_d}")


if __name__ == "__main__":
    check_full_S_j()
