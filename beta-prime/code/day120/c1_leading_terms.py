"""Extract the polynomial P(t, y^2) = s^*_mu(t, y, -y), look at its structure."""

import sympy as sp
from sympy import symbols, expand, Poly, Integer, div

u, y, c, t = symbols('u y c t')


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


def compute_P(l_val, m_val):
    """Compute P(t, z) where z = y^2 (formal), representing s^*_mu(t, y, -y)."""
    m1 = 2*l_val + 1
    m2 = l_val + 1 + m_val
    m3 = l_val - m_val
    k1 = m1 + 2
    k2 = m2 + 1
    k3 = m3
    row1 = [fall(u, k1), fall(u, k2), fall(u, k3)]
    row2 = [fall(y, k1), fall(y, k2), fall(y, k3)]
    row3 = [fall(c, k1), fall(c, k2), fall(c, k3)]
    det = det3([row1, row2, row3])
    V = (u - y) * (u - c) * (y - c)
    S, r = div(Poly(expand(det), u, y, c), Poly(expand(V), u, y, c))
    S = S.as_expr()
    S1 = expand(S.subs({u: t, c: -y}))
    # S1 is polynomial in (t, y) with only even y-powers.
    return S1


def show_structure(l_val, m_val):
    S1 = compute_P(l_val, m_val)
    mu = (2*l_val+1, l_val+1+m_val, l_val-m_val)
    d = mu[0] + (mu[1] + mu[2]) // 2
    print(f"\n--- l={l_val}, m={m_val}, mu={mu}, d_mu={d} ---")
    # As polynomial in y, coefficients are polynomials in t
    p = Poly(S1, y)
    for (deg_y,), coeff_t in sorted(p.terms(), reverse=True):
        # coeff_t is a polynomial in t
        pt = Poly(coeff_t, t)
        max_deg = pt.degree()
        # Just show the highest few t-degrees
        print(f"  y^{deg_y}: t-poly deg {max_deg}, coeffs by desc t-deg:")
        top_coeffs = [pt.nth(max_deg - i) for i in range(min(5, max_deg+1))]
        print(f"    {top_coeffs} (top-5)")
    # Now do the substitution and get beta
    result = Integer(0)
    for (deg_y,), coeff in p.terms():
        result += coeff * (-t) ** (deg_y // 2)
    result = expand(result)
    pt_res = Poly(result, t)
    print(f"  After y^2 -> -t: max t-deg = {pt_res.degree()}, want t^{d}")
    print(f"    Coefficients (from top): {[pt_res.nth(pt_res.degree() - i) for i in range(min(5, pt_res.degree()+1))]}")
    # Actual beta
    beta = pt_res.nth(d)
    print(f"  beta_m = [t^{d}] = {beta}")
    return beta


if __name__ == "__main__":
    # Look at some small cases to understand structure
    for l_val in [3, 4]:
        for m_val in range(l_val + 1):
            show_structure(l_val, m_val)
