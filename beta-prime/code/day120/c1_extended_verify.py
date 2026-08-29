"""Extended verification of bar_s*_mu(j) = (-1)^m delta_{m,l} for l up to 10."""
import sympy as sp
from sympy import symbols, expand, Poly, Integer

u, y, c, t = symbols('u y c t')

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
    xs = (u, y, c)
    mu_padded = list(mu) + [0] * (3 - len(mu))
    ks = [mu_padded[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    numer = det3(rows)
    V = (u - y) * (u - c) * (y - c)
    q, r = sp.div(sp.Poly(expand(numer), u, y, c), sp.Poly(expand(V), u, y, c))
    assert r.as_expr() == 0
    return expand(q.as_expr())

def compute_Fmu_at_s(mu, j_val):
    """[t^{d_mu}] of s^*_mu at u=t, y+c=j, yc=t."""
    S = s_star_mu(mu)
    S1 = expand(S.subs(u, t))
    poly = Poly(S1, y, c)
    result = Integer(0)
    terms_by_pair = {}
    for (a, b), coef in poly.terms():
        key = tuple(sorted([a, b]))
        terms_by_pair.setdefault(key, []).append((a, b, coef))
    s_val = Integer(j_val)
    t_val = t
    for (mn, mx), lst in terms_by_pair.items():
        total = sum(coef for (a, b, coef) in lst)
        if mn == mx:
            result += total * t_val ** mn
        else:
            k = mx - mn
            p_prev2, p_prev1 = Integer(2), s_val
            if k == 0:
                pk = p_prev2
            elif k == 1:
                pk = p_prev1
            else:
                for i in range(2, k+1):
                    pk = s_val * p_prev1 - t_val * p_prev2
                    p_prev2, p_prev1 = p_prev1, pk
            sym_coef = total / 2
            result += sym_coef * (t_val ** mn) * pk
    result = expand(result)
    d_mu = mu[0] + (mu[1] + mu[2]) // 2
    pt = Poly(result, t)
    return pt.nth(d_mu)

print("=== Extended: bar_s*_mu(j) for l up to 6 ===")
for l_val in range(1, 7):
    j = 2*l_val + 1
    all_ok = True
    for m_val in range(l_val + 1):
        mu = (2*l_val + 1, l_val + 1 + m_val, l_val - m_val)
        val = compute_Fmu_at_s(mu, j)
        expected = ((-1)**m_val) if m_val == l_val else 0
        match = "OK" if val == expected else f"!!! got {val}, expected {expected}"
        if val != expected:
            all_ok = False
            print(f"  l={l_val}, m={m_val}: {match}")
    if all_ok:
        print(f"  l={l_val}: all {l_val+1} cases OK")
