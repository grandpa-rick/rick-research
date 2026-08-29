"""Directly compute bar s*_mu(s) := [t^{d_mu}] s*_mu(u=t, y+c=s, yc=t)
for specific mu, to check Observation 3."""

import sympy as sp
from sympy import symbols, expand, Poly, Integer

u, y, c, t, s = symbols('u y c t s')


def fall(x, m):
    """Falling factorial x*(x-1)*(x-2)*...*(x-m+1)."""
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def s_star_mu(mu):
    """s*_mu = (1/V(x)) det[(x_i)_{k_l}] where k_l = mu_l + (3 - l),
    x = (u, y, c), V(x) = (u-y)(u-c)(y-c).
    """
    xs = (u, y, c)
    mu_padded = list(mu) + [0] * (3 - len(mu))
    ks = [mu_padded[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    numer = det3(rows)
    V = (u - y) * (u - c) * (y - c)
    q, r = sp.div(sp.Poly(expand(numer), u, y, c), sp.Poly(expand(V), u, y, c))
    if r.as_expr() != 0:
        raise ValueError("division not clean")
    return expand(q.as_expr())


def substitute_tst(f):
    """Substitute u = t, y = (s + sqrt(s^2 - 4t))/2, etc. is nasty.
    Instead use symmetric-function trick: express f in u, sigma=y+c, pi=yc,
    then substitute u=t, sigma=s, pi=t.
    We use Rick's substitute_sigma_pi routine.
    """
    from route_v_probe_sub import substitute_sigma_pi
    return substitute_sigma_pi(f)


def bar_s_mu(mu):
    """Compute bar s*_mu(s) = [t^{d_mu}] s*_mu(u=t, sigma=s, pi=t)."""
    d = mu[0] + (mu[1] + mu[2]) // 2 if len(mu) >= 3 else 0
    f = s_star_mu(mu)
    # substitute
    import sys
    sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
    from route_v_probe import substitute_sigma_pi, sig, pi
    fsub = substitute_sigma_pi(f)
    # Now fsub is in u, sig, pi. Substitute u = t, sig = s, pi = t.
    fsub2 = expand(fsub.subs({u: t, sig: s, pi: t}))
    p = Poly(fsub2, t, s)
    # Get coefficient of t^d as poly in s
    result = Integer(0)
    for (deg_t, deg_s), coef in p.terms():
        if deg_t == d:
            result += coef * s**deg_s
    return expand(result)


if __name__ == "__main__":
    print("=== Compute bar s*_mu(s) directly ===")
    for mu in [(1,1,0), (2,1,0), (3,1,0), (4,3,3), (4,4,2), (5,3,2), (5,4,1), (5,5,0), (5,5,4), (7,5,4), (7,7,6)]:
        try:
            bs = bar_s_mu(mu)
            d = mu[0] + (mu[1] + mu[2]) // 2
            parity = "even" if (mu[1] - mu[2]) % 2 == 0 else "odd"
            print(f"  mu={mu}, d_mu={d}, parity={parity}: bar s*_mu = {bs}")
        except Exception as e:
            print(f"  mu={mu}: ERROR {e}")
