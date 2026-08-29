"""Derive beta_m symbolically. Approach:

We have mu = (2l+1, l+1+m, l-m). k = (mu_1+2, mu_2+1, mu_3) = (2l+3, l+2+m, l-m).

The Weyl determinant for s*_mu:
  det[ [x_i]_{k_j} ]_{i, j = 1..3} / V(u, y, c)
where [x]_k = falling factorial.

Substitution:
  u = t, c = -y (so s = y+c = 0), then y c = -y^2 = t (i.e., y^2 = -t).

Under c = -y, u = t:
  V(t, y, -y) = (t - y)(t + y)(2y) = 2y(t^2 - y^2)
  [t]_{k_j} = t(t-1)...(t-k_j+1)
  [y]_{k_j} = y(y-1)...(y-k_j+1)
  [-y]_{k_j} = (-y)(-y-1)...(-y-k_j+1) = (-1)^{k_j} y(y+1)...(y+k_j-1) = (-1)^{k_j} [y]^{k_j}
  where [y]^k = rising factorial.

Det = sum_{sigma in S_3} sign(sigma) [t]_{k_{sigma(1)}} [y]_{k_{sigma(2)}} [-y]_{k_{sigma(3)}}
    = sum sign(sigma) [t]_{k_{sigma(1)}} [y]_{k_{sigma(2)}} (-1)^{k_{sigma(3)}} [y]^{k_{sigma(3)}}

Now with u = t, c = -y, s^*_mu = Det / V(t, y, -y).

Also since V and Det both change under y -> -y, let's see:
  V(t, y, -y) = 2y(t^2 - y^2), under y -> -y: -2y(t^2 - y^2), so V is ODD in y.
  Det: under y -> -y, rows 2 and 3 (with y and -y) swap; det picks up sign -1. So Det is ANTI-symmetric in y <-> -y, i.e., ODD in y.
  So s^*_mu = Det/V is EVEN in y (odd / odd = even). Good.

Now bar s*_mu = s^*_mu | y^2 -> -t. But we also want coefficient of t^d, and 1/V still has factor (t^2-y^2)|_{y^2=-t} = t^2 + t = t(t+1).

Actually let me be more careful. The definition is:
  bar s*_mu(s) = [t^{d_mu}] s^*_mu(t, y, c) with y+c=s, yc=t.
This is a function of s, computed as follows: express s^*_mu in (u, sigma, pi), substitute u=t, sigma=s, pi=t, then extract t^{d_mu}.

Setting s = 0: (u, sigma, pi) -> (t, 0, t). So we need:
  beta_m = [t^{d_mu}] s^*_mu (u, sigma, pi) | u=t, sigma=0, pi=t.

Alternatively, using (u, y, c) directly: (t, y, -y) with y^2 = -t. But careful:
The substitution (u, y, c) -> (u, sigma, pi) and then (sigma=0, pi=t) forces y+c=0 and yc=t.
So (y, c) satisfy y+c=0, yc=t, giving y = ±sqrt(-t), c = ∓sqrt(-t). Two choices, but s^*_mu is symmetric in (y, c), so the answer is the same.

Let's just compute the WHOLE process purely symbolically for small l and see the structure.
"""

import sympy as sp
from sympy import symbols, expand, Poly, Integer, div, simplify, factor, together, cancel, Rational

l_sym = symbols('l', integer=True, positive=True)
m_sym = symbols('m', integer=True, nonnegative=True)
u, y, c, t = symbols('u y c t')


def fall(x, k):
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def det3_from_rows(rows):
    (a1, a2, a3) = rows[0]
    (b1, b2, b3) = rows[1]
    (c1, c2, c3) = rows[2]
    return (a1*(b2*c3 - b3*c2) - a2*(b1*c3 - b3*c1) + a3*(b1*c2 - b2*c1))


def compute_beta_symbolic(l_val, m_val):
    """Compute beta_m using explicit falling factorials for specific (l, m)."""
    # mu = (2l+1, l+1+m, l-m)
    m1 = 2*l_val + 1
    m2 = l_val + 1 + m_val
    m3 = l_val - m_val
    if m3 < 0:
        return None
    k1 = m1 + 2  # 2l+3
    k2 = m2 + 1  # l+2+m
    k3 = m3      # l-m
    # Weyl det
    row1 = [fall(u, k1), fall(u, k2), fall(u, k3)]
    row2 = [fall(y, k1), fall(y, k2), fall(y, k3)]
    row3 = [fall(c, k1), fall(c, k2), fall(c, k3)]
    det = det3_from_rows([row1, row2, row3])
    V = (u - y) * (u - c) * (y - c)
    S, r = div(Poly(expand(det), u, y, c), Poly(expand(V), u, y, c))
    if r.as_expr() != 0:
        raise ValueError("no clean division")
    S = S.as_expr()
    # Substitute u = t, c = -y (so s = y+c = 0)
    S1 = expand(S.subs({u: t, c: -y}))
    # S1 is polynomial in (t, y), even in y
    # Substitute y^2 = -t: replace y^2 with -t iteratively
    py = Poly(S1, y)
    terms = py.terms()
    # Each term is ((deg_y,), coeff_in_t)
    result = Integer(0)
    for (deg_y,), coeff in terms:
        if deg_y % 2 != 0:
            raise ValueError(f"Odd y-degree at l={l_val}, m={m_val}: deg_y={deg_y}, coeff={coeff}")
        # y^{deg_y} = (y^2)^{deg_y/2} = (-t)^{deg_y/2}
        result += coeff * (-t) ** (deg_y // 2)
    result = expand(result)
    # Extract coefficient of t^{d_mu}
    d = m1 + (m2 + m3) // 2
    pt = Poly(result, t)
    beta = pt.nth(d)
    return beta


def survey():
    print("=== Symbolic derivation cross-check ===\n")
    for l_val in range(1, 5):
        for m_val in range(l_val + 1):
            beta = compute_beta_symbolic(l_val, m_val)
            conj = (-1)**(m_val + 1) * ((m_val+1)*(2*l_val+1) - (1 if m_val == l_val else 0))
            print(f"  l={l_val}, m={m_val}: beta={beta}, conj={conj}  {'OK' if beta == conj else '!!!'}")


if __name__ == "__main__":
    survey()
