"""Day 117 — Route V: does each individual D_mu / (y - c) satisfy joint
(u, pi)-degree <= j + 2, or is cancellation essential?"""
from route_v_probe import (
    bt_tables, ds_uyc, divide, substitute_sigma_pi, joint_u_pi_deg,
    fall, det3,
)
from sympy import symbols, expand, Integer

u, y, c = symbols('u y c')


def D_mu(mu):
    xs = (u, y, c)
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    return expand(det3(rows))


if __name__ == "__main__":
    JMAX = 4
    T = bt_tables(JMAX)
    print("j  mu               kap    (u,pi)-deg D_mu/(y-c)   j+2")
    print('-' * 60)
    for j in range(JMAX + 1):
        for mu, kap in T[j]:
            Dmu = D_mu(mu)
            Dmu_over_yc = divide(Dmu, y - c, [u, y, c])
            Dmu_sigpi = substitute_sigma_pi(Dmu_over_yc)
            d = joint_u_pi_deg(Dmu_sigpi)
            flag = "OK " if d <= j + 2 else "OVER"
            print(f"{j}  {str(mu):16} {kap:4}   {d:>6}                {j+2}  {flag}")
