"""Day 117 — Test the following claim:
  For f in Q[u, y, c]^S3 = Q[e_1, e_2, e_3],
  (u, pi)-deg(f) <= k
  IFF
  deg_t f(t+1, 2t, t^2) <= k   (i.e., substitute e_1 = t+1, e_2 = 2t, e_3 = t^2)

  This substitution comes from u = t, sigma = 1, pi = t.

If the equivalence holds, we can prove StructB by bounding a 1-var polynomial degree.

Actually WAIT: the substitution u = t, sigma = 1, pi = t gives
  e_1 = u + sigma = t + 1
  e_2 = u sigma + pi = t + t = 2t
  e_3 = u pi = t^2
So f(t+1, 2t, t^2) = f(u,y,c) at these values.

Test: for each basis element e_1^i1 e_2^i2 e_3^i3, verify that
  deg_t (t+1)^i1 (2t)^i2 (t^2)^i3 <= i1 + i2 + 2*i3
and check what the "top" contribution looks like.
"""
from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import bt_tables, substitute_sigma_pi, joint_u_pi_deg
from sympy import symbols, expand, Integer, Poly

u, y, c, t, sig, pi = symbols('u y c t sigma pi')


def upi_deg(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


def substitute_1param(expr):
    """f(u, y, c) -> f(t, y(t), c(t)) where y+c = 1, yc = t.
    Do via e_1 = t + 1, e_2 = 2t, e_3 = t^2 substitution."""
    # Express as poly in u, y, c. Convert to e_1, e_2, e_3 first.
    # Simpler: substitute u = t, y = 1/2 + delta, c = 1/2 - delta, expand, then use delta^2 = 1/4 - t.
    # Actually cleaner: substitute u = t, and treat expression in u, y, c;
    # It's symmetric in y, c, so we can rewrite in sigma = y+c, pi = yc. Then sigma = 1, pi = t.
    # But it's symmetric in ALL three including u — but u = t means we're treating u specially.
    # The expr is symmetric in u, y, c so f(t, y, c) is symmetric in y, c only (once u is set).
    # Then rewrite in sigma, pi and substitute sigma = 1, pi = t.
    from route_v_probe import substitute_sigma_pi as substitute_sigma_pi_
    # First substitute u = t
    expr1 = expr.subs(u, t)
    # Now symmetric in y, c
    from route_v_probe import substitute_sigma_pi
    expr2 = substitute_sigma_pi(expr1)
    # Now expr2 is in t, sigma, pi. Substitute sigma = 1, pi = t.
    expr3 = expr2.subs({sig: 1, pi: t})
    return expand(expr3)


if __name__ == "__main__":
    xs = (u, y, c)
    JMAX = 6
    T = bt_tables(JMAX)
    print(f"Testing: is (u,pi)-deg(S_j) captured by t-degree of S_j(t, sigma=1, pi=t)?")
    print(f"{'j':>3} {'(u,pi)-deg(S_j)':>18} {'t-deg S_j(...)':>20}")
    for j in range(JMAX + 1):
        Sj = Integer(0)
        for mu, kap in T[j]:
            Sj += kap * factorial_schur(mu, xs)
        Sj = expand(Sj)
        d_upi = upi_deg(Sj)
        Sj_sub = substitute_1param(Sj)
        deg_t = 0
        if Sj_sub != 0:
            p = Poly(Sj_sub, t)
            deg_t = p.degree()
        print(f"{j:>3} {d_upi:>18} {deg_t:>20}")
    print()

    # Also test on a few individual basis elements to verify the characterization
    print("Testing characterization on individual monomials e_1^i e_2^j e_3^k:")
    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(3):
                if i1 + i2 + 2*i3 > 5:
                    continue
                # e_1^i1 * e_2^i2 * e_3^i3 substituted:
                # (t+1)^i1 * (2t)^i2 * (t^2)^i3
                v = expand((t+1)**i1 * (2*t)**i2 * (t**2)**i3)
                deg_t = Poly(v, t).degree() if v != 0 else 0
                wdeg = i1 + i2 + 2*i3
                match = "MATCH" if deg_t == wdeg else "MISMATCH"
                print(f"  e_1^{i1} e_2^{i2} e_3^{i3}: t-deg = {deg_t}, wdeg = {wdeg}  {match}")
