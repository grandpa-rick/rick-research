"""Day 120 — Empirical verification of [t^d] S_j = 0 for d > j, all d.

Extends Day 119 lower_d_check.py:
  - Directly compute s*_mu(u=t, sigma=s, pi=t) for every mu with K_{mu',(2^j)} > 0.
  - Sum: S_j(t, s) = sum_mu K_{mu', (2^j)} s*_mu(t, s, t).
  - For each d > j, print [t^d] S_j as poly in s. Should be 0.

Also splits contributions by d_mu = d, d_mu = d+1, d_mu = d+2, ...
to see which mu's carry weight at each t-power (the "coupling").
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


def eval_s_star(mu):
    """s*_mu(u=t, sigma=s, pi=t) as sympy poly in t, s."""
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def get_t_coefficient(expr, d):
    """Return [t^d] expr as poly in s."""
    p = Poly(expr, t, s)
    out = Integer(0)
    for (dt, ds), coef in p.terms():
        if dt == d:
            out += coef * s**ds
    return expand(out)


def coupling_at_t_d(j, d, mu_evals, verbose=False):
    """Return the [t^d] contribution of each mu (with K > 0) as a poly in s,
    grouped by d_mu - d.

    Returns dict {delta: [(mu, K, contribution_poly)]}
    where delta = d_mu - d (subleading order).
    """
    twoj = 2 * j
    groups = {}
    for mu, K, ev in mu_evals:
        c_d = get_t_coefficient(ev, d)
        if c_d == 0:
            continue
        delta = d_mu(mu) - d
        groups.setdefault(delta, []).append((mu, K, c_d))
    return groups


def check_S_j_vanishing(j, verbose=True):
    twoj = 2 * j
    # Precompute all mu evals
    mu_evals = []
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K == 0:
            continue
        ev = eval_s_star(mu)
        mu_evals.append((mu, K, ev))

    # total S_j
    S = Integer(0)
    for mu, K, ev in mu_evals:
        S += K * ev
    S = expand(S)

    p = Poly(S, t, s)
    max_dt = max(dt for (dt, _), _ in p.terms())
    print(f"j={j}: deg_t S_j = {max_dt} (target: <= {j})")

    ok = True
    d_max = max(d_mu(mu) for mu, _, _ in mu_evals)
    for d in range(j + 1, max(max_dt, d_max) + 1):
        coef_d = get_t_coefficient(S, d)
        status = "OK" if coef_d == 0 else "!!! NONZERO"
        print(f"  [t^{d}] S_j = {coef_d}  {status}")
        if coef_d != 0:
            ok = False

    if verbose:
        # Coupling breakdown
        print(f"\n  Coupling analysis (contributions at t^d grouped by delta = d_mu - d):")
        for d in range(j + 1, d_max + 1):
            groups = coupling_at_t_d(j, d, mu_evals)
            print(f"    d={d}:")
            for delta in sorted(groups.keys()):
                terms = groups[delta]
                subtotal = sum(K * poly for mu, K, poly in terms)
                subtotal = expand(subtotal)
                print(f"      delta={delta} ({len(terms)} mu's), K*contrib sum = {subtotal}")
                if delta <= 2 and len(terms) <= 8:
                    for mu, K, poly in terms:
                        print(f"        mu={mu} K={K}: [t^{d}] s*_mu = {poly}")

    return ok


if __name__ == "__main__":
    for j in [3, 4, 5, 6, 7]:
        print("=" * 70)
        check_S_j_vanishing(j, verbose=(j <= 5))
        print()
