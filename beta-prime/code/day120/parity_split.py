"""Day 120 — Check whether the vanishing [t^d] S_j = 0 splits by parity of (mu_2 - mu_3).

Recall Day 119: for d = d_max, splitting by parity gives Identity A (even-parity)
and Identity B (odd-parity, alpha-weighted) separately vanishing.

Question: does the SAME parity split work for d < d_max?
I.e., does sum_{mu, p(mu)=0} K_{mu',(2^j)} [t^d] s*_mu = 0 separately?
And sum_{mu, p(mu)=1} K [t^d] s*_mu = 0 separately?

If YES: the general-d case decomposes into "identity A/B at each t-power d".
If NO: we need to understand the coupling more carefully.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly

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
    print("Testing parity split for [t^d] S_j = 0")
    print("A_sum := sum_{mu : (mu_2-mu_3) even} K * [t^d] s*_mu")
    print("B_sum := sum_{mu : (mu_2-mu_3) odd} K * [t^d] s*_mu")
    print()

    for j in range(2, 9):
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
        for d in range(j+1, d_max + 1):
            A_sum = Integer(0)
            B_sum = Integer(0)
            for mu, K, ev in mu_evals:
                cd = get_cd(ev, d)
                if parity(mu) == 0:
                    A_sum += K * cd
                else:
                    B_sum += K * cd
            A_sum = expand(A_sum)
            B_sum = expand(B_sum)
            total = expand(A_sum + B_sum)
            statusA = "0" if A_sum == 0 else str(A_sum)
            statusB = "0" if B_sum == 0 else str(B_sum)
            statusT = "OK" if total == 0 else "!!!"
            print(f"  d={d}: A_sum = {statusA}, B_sum = {statusB}, total = {total}  {statusT}")
