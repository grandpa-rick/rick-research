"""Analytic derivation of beta_m for odd-parity spine at d_max.

Setup: mu = (2l+1, l+1+m, l-m), so k = (mu_1+2, mu_2+1, mu_3) = (2l+3, l+2+m, l-m).
d_mu = 3l+1.

beta_m = [s^0] [t^{3l+1}] s^*_mu(u=t, y+c=s, yc=t).
       = [t^{3l+1}] s^*_mu(t, y, -y) evaluated with y^2 = -t.

Since the substitution y+c = 0, yc = t gives y*c = -y^2 = t, i.e., y^2 = -t.

Strategy:
  1. Compute s^*_mu(u, y, c) symbolically.
  2. Substitute u = t, c = -y, obtain rational function in (t, y).
  3. Multiply out V = 2y(t^2 - y^2), get D'(t, y) polynomial.
  4. D'(t, y) is odd in y (has factor y), so D'(t, y) / y is polynomial in y with only even
     powers (need to verify).
  5. Substitute y^2 = -t, so t^2 - y^2 = t(t+1). This makes s^*_mu = (D'/y) / [2(t^2-y^2)] a rational in t.
     Actually: (D'/y) will be a polynomial in y^2. Then we substitute y^2 = -t, getting poly in t.
     Similarly 2(t^2 - y^2) with y^2 = -t is 2t(t+1).
     So bar-value = P(t) / [2t(t+1)] where P(t) = poly in t.
  6. Extract [t^{3l+1}] coefficient.

Let me implement this and test.
"""

import sympy as sp
from sympy import symbols, expand, Poly, Integer, factor, simplify, Rational, div

u, y, c, t, s = symbols('u y c t s')


def fall(x, k):
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def s_star_mu(mu):
    """s*_mu(u, y, c) via Weyl determinant."""
    mu_padded = list(mu) + [0] * (3 - len(mu))
    ks = [mu_padded[col] + (2 - col) for col in range(3)]
    xs = (u, y, c)
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    numer = det3(rows)
    V = (u - y) * (u - c) * (y - c)
    q, r = div(Poly(expand(numer), u, y, c), Poly(expand(V), u, y, c))
    if r.as_expr() != 0:
        raise ValueError("div not clean")
    return expand(q.as_expr())


def compute_beta_at_s0(mu):
    """Compute beta = [s^0][t^d_mu] bar s*_mu(s) via the c = -y trick.

    Since s = y + c and we want s = 0 => c = -y.
    Substitute u = t, c = -y, then the resulting expression is a rational function.
    yc = -y^2 = t, i.e., y^2 = -t.
    Substituting yields poly in t. Extract coef of t^d_mu.
    """
    d = mu[0] + (mu[1] + mu[2]) // 2
    # 1) Compute s*_mu(u, y, c)
    S = s_star_mu(mu)
    # 2) Substitute c = -y, u = t
    S1 = expand(S.subs({c: -y, u: t}))
    # S1 is now a polynomial in (t, y). It should be an even function of y after dividing by y once?
    # Let's just multiply through by (t^2 - y^2) = (t-y)(t+y) = -V/(2y).
    # Actually V(u=t, y, c=-y) = (t-y)(t+y)(2y) = 2y(t^2 - y^2).
    # But s^*_mu is defined as det/V, so S1 = det(u=t,y,c=-y) / [2y(t^2 - y^2)].
    # Wait, s_star_mu already divides. So S1 IS a polynomial (result of clean division).
    # Now substitute y^2 = -t to get poly in t alone. But y appears to odd degrees potentially.
    # Let's check the y-degree of S1.
    Ss = Poly(S1, y)
    print(f"  y-degrees present in S1: {[deg for (deg,), _ in Ss.terms()]}")
    # If odd powers exist, they must vanish upon symmetric substitution?
    # Actually no: s^*_mu is symmetric in u,y,c only if mu allows... it's symmetric via Weyl.
    # So under c <-> y swap, s^*_mu is invariant. But subst c = -y is not the swap.
    #
    # Hmm. But bar s*_mu is defined via u=t, y+c=s, yc=t. That's a well-defined subst since s^*_mu
    # is symmetric in (y, c). So s^*_mu(t, y, -y) IS a polynomial in (t, y), symmetric under y -> -y
    # (since y+c=0, yc=t = -y^2, so both are functions of y^2).
    # So S1 should have ONLY even powers of y.

    # Let me force by using symmetric-function trick: expression is polynomial in (u, sigma, pi)
    # where sigma = y+c, pi = yc. We substitute sigma = 0, pi = -y^2 = t (since s = 0 means sigma = 0, yc = t always).
    # But we set pi = t as well. So sigma = 0, pi = t.
    # Compute S in (u, sigma, pi) form, then subst u = t, sigma = 0, pi = t. Get poly in t.
    import sys
    if '/home/agent/projects/beta-prime/code/day117' not in sys.path:
        sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
    from route_v_probe import substitute_sigma_pi, sig, pi as pi_sym
    S_full = s_star_mu(mu)  # in (u, y, c)
    S_upi = substitute_sigma_pi(S_full)
    # Now substitute u = t, sig = 0, pi = t
    S_final = expand(S_upi.subs({u: t, sig: 0, pi_sym: t}))
    # Get coef of t^d
    pt = Poly(S_final, t)
    coeff = pt.nth(d)
    return coeff


def survey():
    print("=== Direct constant-term beta via c=-y trick, up to l = 6 ===\n")
    for l in range(1, 7):
        for m in range(l+1):
            mu = (2*l+1, l+1+m, l-m)
            if mu[2] < 0: continue
            try:
                b = compute_beta_at_s0(mu)
                conj = (-1)**(m+1) * ((m+1)*(2*l+1) - (1 if m == l else 0))
                match = "OK" if b == conj else "!!!"
                print(f"  l={l}, m={m}, mu={mu}: beta={b}, conjecture={conj}  {match}")
            except Exception as e:
                print(f"  l={l}, m={m}, mu={mu}: ERROR {e}")


if __name__ == "__main__":
    survey()
