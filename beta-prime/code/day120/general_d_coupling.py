"""Day 120 — Enumerate contributing mu's for fixed j, d.
Print the coupled identity in explicit form for small j.

For each (j, d) with j < d <= d_max:
  Contributors: all mu with 0 < d_mu - d <= K (K = subleading depth needed).
  Each contributes K_{mu', (2^j)} * [t^d] s*_mu(t, s, t)  (a poly in s).
  Vanishing identity: sum_mu K * [t^d] s*_mu = 0.

We print grouped by delta = d_mu - d.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly, factor

u, y, c = symbols('u y c')
t, s = symbols('t s')


def eval_ts(mu):
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def get_t_coefficient(expr, d):
    p = Poly(expr, t, s)
    out = Integer(0)
    for (dt, ds), coef in p.terms():
        if dt == d:
            out += coef * s**ds
    return expand(out)


def coupled_identity(j, d, mu_evals):
    """Return sorted list [(delta, mu, K, [t^d] eval), ...] contributing to [t^d] S_j."""
    entries = []
    for mu, K, ev in mu_evals:
        delta = d_mu(mu) - d
        if delta < 0:
            continue  # d_mu < d, contributes nothing at t^d (t-degree too low)
        cd = get_t_coefficient(ev, d)
        if cd == 0:
            continue
        entries.append((delta, mu, K, cd))
    entries.sort()
    return entries


def print_identity(j, d, entries):
    print(f"\n--- [t^{d}] S_{j} = 0  (j={j}, d={d}, delta_range=[{min(e[0] for e in entries) if entries else 'n/a'}, {max(e[0] for e in entries) if entries else 'n/a'}]) ---")
    total = Integer(0)
    for delta, mu, K, cd in entries:
        contrib = K * cd
        total += contrib
        m1, m2, m3 = mu
        parity = "even" if (m2 - m3) % 2 == 0 else "odd"
        print(f"  delta={delta} mu={mu} ({parity}) K={K}: [t^{d}] = {cd},  contrib = {expand(contrib)}")
    total = expand(total)
    print(f"  SUM = {total}")


if __name__ == "__main__":
    for j in [3, 5, 7]:
        print("=" * 70)
        print(f"j = {j}")
        print("=" * 70)
        twoj = 2 * j
        mu_evals = []
        for mu in all_mu_3parts(twoj):
            K = kostka_mu_prime_2j(mu)
            if K == 0:
                continue
            ev = eval_ts(mu)
            mu_evals.append((mu, K, ev))
        d_max = max(d_mu(mu) for mu, _, _ in mu_evals)
        # For each d in (j, d_max], print the coupled identity
        for d in range(j + 1, d_max + 1):
            entries = coupled_identity(j, d, mu_evals)
            print_identity(j, d, entries)
