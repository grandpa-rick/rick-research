"""Day 117 — Test whether (s^*_{(1,1)})^j = sum_mu K_{mu', (2^j)} s^*_mu.

If YES, then S_j = product of j copies of s^*_{(1,1)}, which has (u,pi)-deg 1,
so S_j has (u,pi)-deg <= j. StructB closes IMMEDIATELY.
"""
from route_v_probe import (
    bt_tables, ds_uyc, divide, substitute_sigma_pi, joint_u_pi_deg,
    fall, det3,
)
from sympy import symbols, expand, Integer, Poly

u, y, c = symbols('u y c')


def factorial_schur(mu, xs):
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = (xs[0] - xs[1]) * (xs[0] - xs[2]) * (xs[1] - xs[2])
    q, r = Poly(num, *xs).div(Poly(V, *xs))
    assert r.as_expr() == 0
    return q.as_expr()


if __name__ == "__main__":
    xs = (u, y, c)
    # Compute s^*_{(1,1)} = s^*_{(1,1,0)}
    s11 = factorial_schur((1, 1, 0), xs)
    print(f"s^*_{{(1,1)}}(u,y,c) = {expand(s11)}")
    print()

    JMAX = 4
    T = bt_tables(JMAX)
    for j in range(JMAX + 1):
        # LHS: (s^*_{(1,1)})^j
        lhs = expand(s11 ** j)
        # RHS: sum_mu K_{mu', (2^j)} s^*_mu
        rhs = Integer(0)
        for mu, kap in T[j]:
            rhs += kap * factorial_schur(mu, xs)
        rhs = expand(rhs)
        diff = expand(lhs - rhs)
        status = "MATCH" if diff == 0 else "DIFFER"
        print(f"j={j}: LHS - RHS = {diff}    -> {status}")
