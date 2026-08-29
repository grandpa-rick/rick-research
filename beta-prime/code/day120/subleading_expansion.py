"""Day 120 — Subleading expansion of s*_mu(u=t, sigma=s, pi=t).

For each mu, s*_mu evaluated at (u=t, sigma=s, pi=t) is a polynomial in t, s.
Top t-degree is d_mu (Day 118 theorem). We want the coefficients of

    t^{d_mu}, t^{d_mu - 1}, t^{d_mu - 2}, ...

as polynomials in s. These are the "subleading" pieces that couple into
[t^d] S_j for d < d_mu.

Structure to explore:
  - Fix spine-type mu = (a, b, c). What's the leading coeff bar_s_mu(s)?
    (Already computed Day 119; recall bar_s_mu(s) = [t^{d_mu}] eval.)
  - What's the sub-leading [t^{d_mu - 1}] as poly in s?
  - Do they factor nicely (e.g., (s - N) for integer N)?

We compute for many mu, all subleading orders k = 0..K, and store as a table.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import d_mu
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly, factor, simplify

u, y, c = symbols('u y c')
t, s = symbols('t s')


def eval_ts(mu):
    """s*_mu(u=t, sigma=s, pi=t) as poly in t, s."""
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def sub_coeffs(mu, k_max=4):
    """Return list [c_0, c_1, ..., c_k] where c_k = [t^{d_mu - k}] eval(mu) as poly in s."""
    d = d_mu(mu)
    expr = eval_ts(mu)
    p = Poly(expr, t, s)
    out = [Integer(0)] * (k_max + 1)
    for (dt, ds), coef in p.terms():
        k = d - dt
        if 0 <= k <= k_max:
            out[k] += coef * s**ds
    return [expand(x) for x in out]


def try_factor(poly, s_sym=s):
    """Try to express poly as an integer times a monic thing, and factor."""
    if poly == 0:
        return "0"
    try:
        f = factor(poly)
        return str(f)
    except Exception:
        return str(poly)


if __name__ == "__main__":
    print("=" * 70)
    print("Subleading coefficients [t^{d_mu - k}] s*_mu(t, s, t) for spine mu")
    print("=" * 70)

    # Systematically enumerate mu = (a, b, c) with a >= b >= c, ell <= 3, |mu| <= 12
    mu_list = []
    for a in range(1, 8):
        for b in range(0, a + 1):
            for cc in range(0, b + 1):
                if a + b + cc <= 12:
                    mu_list.append((a, b, cc))

    K_MAX = 3
    print(f"\n{'mu':>12} {'d_mu':>4} " + " ".join(f"{'[t^{d-'+str(k)+'}]':>25}" for k in range(K_MAX + 1)))
    print("-" * (16 + (K_MAX + 1) * 26))
    for mu in mu_list:
        d = d_mu(mu)
        cs = sub_coeffs(mu, K_MAX)
        row = f"{str(mu):>12} {d:>4} "
        for k in range(K_MAX + 1):
            row += f"{str(try_factor(cs[k])):>25} "
        print(row)

    # Special focus: look at fixed (mu_2, mu_3) family across mu_1 = a
    print("\n" + "=" * 70)
    print("Family analysis: fix (b, c), vary a")
    print("=" * 70)
    for (b, cc) in [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 3), (3, 2)]:
        print(f"\n--- family a >= {b}, mu=(a,{b},{cc}) ---")
        for a in range(max(b, 1), 8):
            mu = (a, b, cc)
            cs = sub_coeffs(mu, K_MAX)
            print(f"  mu={mu}, d_mu={d_mu(mu)}:")
            for k in range(K_MAX + 1):
                print(f"    [t^{{d_mu-{k}}}] = {try_factor(cs[k])}")
