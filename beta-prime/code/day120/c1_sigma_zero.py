"""Compute s^*_mu with sigma = 0 substitution directly.

When sigma = 0, the (y, c) variables satisfy y + c = 0, so any symmetric polynomial in (y, c)
becomes a polynomial in pi = yc alone.

s^*_mu(u, y, c) is symmetric in (y, c), so with sigma = 0:
  s^*_mu(u, y, c)|_{y+c=0} = F(u, pi) where pi = yc.

Then bar s^*_mu(0) = [t^{d_mu}] F(t, t).
"""

import sympy as sp
from sympy import symbols, expand, Poly, Integer, div, simplify

u, y, c, t = symbols('u y c t')
pi = symbols('pi')


def fall(x, k):
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def det3(rows):
    (a1, a2, a3) = rows[0]
    (b1, b2, b3) = rows[1]
    (c1, c2, c3) = rows[2]
    return (a1*(b2*c3 - b3*c2) - a2*(b1*c3 - b3*c1) + a3*(b1*c2 - b2*c1))


def s_star(mu):
    m_padded = list(mu) + [0] * (3 - len(mu))
    ks = [m_padded[col] + (2 - col) for col in range(3)]
    xs = (u, y, c)
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    numer = det3(rows)
    V = (u - y) * (u - c) * (y - c)
    q, r = div(Poly(expand(numer), u, y, c), Poly(expand(V), u, y, c))
    if r.as_expr() != 0:
        raise ValueError("no clean division")
    return expand(q.as_expr())


def s_star_at_sigma0(mu):
    """Compute F(u, pi) = s^*_mu(u, y, c) with y+c=0, i.e., c=-y and yc = -y^2 = pi.
    So we substitute c = -y and then y^2 -> -pi.
    """
    S = s_star(mu)
    # Substitute c = -y
    S1 = expand(S.subs({c: -y}))
    # S1 is polynomial in (u, y), even in y (as we verified before)
    p_y = Poly(S1, y)
    result = Integer(0)
    for (deg_y,), coeff in p_y.terms():
        if deg_y % 2 != 0:
            raise ValueError(f"Odd y-degree: {deg_y}")
        result += coeff * (-pi) ** (deg_y // 2)
    return expand(result)


def bar_s_at_0(mu):
    F = s_star_at_sigma0(mu)
    # F is polynomial in (u, pi). Substitute u = t, pi = t.
    G = expand(F.subs({u: t, pi: t}))
    d = mu[0] + (mu[1] + mu[2]) // 2
    p = Poly(G, t)
    return p.nth(d)


def survey():
    print("=== beta_m via sigma=0 substitution ===\n")
    for l_val in range(1, 6):
        for m_val in range(l_val + 1):
            mu = (2*l_val+1, l_val+1+m_val, l_val-m_val)
            if mu[2] < 0: continue
            b = bar_s_at_0(mu)
            conj = (-1)**(m_val+1) * ((m_val+1)*(2*l_val+1) - (1 if m_val == l_val else 0))
            print(f"  l={l_val}, m={m_val}, mu={mu}: beta={b}, conj={conj}, {'OK' if b == conj else '!!!'}")


def analyze_structure_at_m_l(l_val):
    """For m = l, mu_3 = 0. Show that we CAN simplify."""
    m_val = l_val
    mu = (2*l_val+1, l_val+1+m_val, 0)  # 2-part!
    print(f"\n--- Analysis at m = l = {l_val}, mu = {mu} (2-part) ---")
    # k = (mu_1+2, mu_2+1, mu_3) = (2l+3, l+2+m, 0)
    # k_3 = 0, so column 3 of det is (1, 1, 1)^T
    k1 = mu[0] + 2  # 2l+3
    k2 = mu[1] + 1  # 2l+2
    # (mu_2 = l+1+l = 2l+1, so k2 = 2l+2)
    k3 = 0
    print(f"  k = ({k1}, {k2}, {k3})")
    # Expand along column 3
    # det = (y)_{k1}(c)_{k2} - (y)_{k2}(c)_{k1} - [(u)_{k1}(c)_{k2} - (u)_{k2}(c)_{k1}] + (u)_{k1}(y)_{k2} - (u)_{k2}(y)_{k1}
    #     = ...
    F = s_star_at_sigma0(mu)
    print(f"  F(u, pi) degree info: u_deg = {Poly(F, u).degree()}, pi_deg = {Poly(F, pi).degree()}")
    # Now substitute u = t, pi = t and get top coef
    G = expand(F.subs({u: t, pi: t}))
    d = mu[0] + mu[1] // 2  # since mu_3 = 0
    p = Poly(G, t)
    print(f"  degree of G in t: {p.degree()}, d_mu = {d}")
    print(f"  top few coefficients of G (from degree d down):")
    for i in range(min(3, d+1)):
        print(f"    [t^{d-i}] = {p.nth(d-i)}")


if __name__ == "__main__":
    survey()
    for l_val in [2, 3, 4]:
        analyze_structure_at_m_l(l_val)
