"""Day 117 — Test whether the map bar_Phi: bar_s_mu -> bar_s^*_mu (on associated graded)
preserves the relation sum K_{mu', (2^j)} bar_s_mu = 0 in bar F^k for k > j.

We just directly compute:
  sum_K_s_mu := sum_mu K_{mu', (2^j)} * s_mu = e_2^j    (in Lambda_3)
  sum_K_ss_mu := sum_mu K_{mu', (2^j)} * s^*_mu = S_j   (in Lambda_3 with shifted basis)

Both computed as polynomials in (u, y, c). Then substitute (u, sigma, pi).
Compare their (u, pi)-degrees.

We KNOW:
  (u, pi)-deg(e_2^j) = j (since e_2 = u sigma + pi).

WE WANT:
  (u, pi)-deg(S_j) = ?

Empirically it's j too. Let me look at the DIFFERENCE structure:
  S_j - e_2^j = sum_mu K_{mu', (2^j)} * (s^*_mu - s_mu)
              = sum_mu K_{mu', (2^j)} * (lower poly-degree corrections)

The claim we need: (u, pi)-deg of S_j - e_2^j is <= j.

Since (u, pi)-deg(e_2^j) = j, this is equivalent to (u, pi)-deg(S_j) <= j.
So we need to bound (u, pi)-deg of (S_j - e_2^j).

Note: S_j - e_2^j has poly-degree < 2j (strictly, since the top-poly-degree parts cancel).
Say poly-deg <= 2j - 1.
"""
from route_v_probe import (
    bt_tables, ds_uyc, divide, substitute_sigma_pi, joint_u_pi_deg,
    fall, det3,
)
from ordinary_schur_deg import ord_schur, factorial_schur, all_partitions_len_le_3, V_expr
from sympy import symbols, expand, Integer, Poly

u, y, c = symbols('u y c')


def upi_deg_expr(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


if __name__ == "__main__":
    xs = (u, y, c)
    JMAX = 5
    T = bt_tables(JMAX)
    print(f"{'j':>3} {'(u,pi)-deg(e_2^j)':>18} {'(u,pi)-deg(S_j)':>18} {'(u,pi)-deg(S_j - e_2^j)':>26} {'poly-deg(S_j - e_2^j)':>25}")
    for j in range(JMAX + 1):
        # e_2^j
        e2 = u * y + u * c + y * c
        e2j = expand(e2 ** j)
        # S_j
        Sj = Integer(0)
        for mu, kap in T[j]:
            Sj += kap * factorial_schur(mu, xs)
        Sj = expand(Sj)
        diff = expand(Sj - e2j)
        # deg
        d_e2j = upi_deg_expr(e2j)
        d_Sj = upi_deg_expr(Sj)
        d_diff = upi_deg_expr(diff) if diff != 0 else 0
        # poly-deg
        if diff == 0:
            poly_deg = 0
        else:
            p = Poly(diff, u, y, c)
            poly_deg = max(sum(m) for m, _ in p.terms())
        print(f"{j:>3} {d_e2j:>18} {d_Sj:>18} {d_diff:>26} {poly_deg:>25}")
