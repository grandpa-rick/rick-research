"""Day 117 — Test the (u,pi)-degree behavior of both:
  E(s^*_mu) := sum_{lambda/mu vert 2-strip} s^*_lambda   (the vert-2-strip Pieri sum)
  E'(s^*_mu) := s^*_{(1,1)} * s^*_mu - E(s^*_mu)         (the Pieri correction)

Claim: (u,pi)-deg(E(s^*_mu)) <= d_mu + 1 AND (u,pi)-deg(E'(s^*_mu)) <= d_mu + 1.

If both hold, then for any f in F^k:
  s^*_{(1,1)} * f  in F^{k+1}   (product)
  E'(f)  in F^{k+1}              (by linearity of the claim)
  E(f) = s^*_{(1,1)}*f - E'(f)  in F^{k+1}
So E: F^k -> F^{k+1}, and by induction, S_j = E^j(1) in F^j.
"""
from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from eprime_filtration import vert_2_strips_from
from sympy import symbols, expand, Integer

u, y, c = symbols('u y c')


def upi_deg(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


if __name__ == "__main__":
    xs = (u, y, c)
    s11 = factorial_schur((1, 1, 0), xs)

    max_size = 5
    print(f"{'mu':>15} {'d_mu':>5} {'d(E(s^*_mu))':>13} {'d(E prime)':>12} {'d(s11 * s^*_mu)':>16}")
    print('-' * 75)
    all_ok_E = True
    all_ok_Ep = True
    for N in range(max_size + 1):
        for mu in all_partitions_len_le_3(N):
            s_star_mu = factorial_schur(mu, xs)
            d_mu = upi_deg(s_star_mu)
            product = expand(s11 * s_star_mu)
            d_prod = upi_deg(product)
            e_part = Integer(0)
            for lam in vert_2_strips_from(mu):
                e_part += factorial_schur(lam, xs)
            e_part = expand(e_part)
            d_E = upi_deg(e_part) if e_part != 0 else 0
            e_prime = expand(product - e_part)
            d_Ep = upi_deg(e_prime) if e_prime != 0 else 0
            flagE = "OK" if d_E <= d_mu + 1 else "!!"
            flagEp = "OK" if d_Ep <= d_mu + 1 else "!!"
            if d_E > d_mu + 1:
                all_ok_E = False
            if d_Ep > d_mu + 1:
                all_ok_Ep = False
            print(f"{str(mu):>15} {d_mu:>5} {d_E:>13} {flagE} {d_Ep:>12} {flagEp} {d_prod:>16}")
    print()
    print(f"All E:  d(E(s^*_mu)) <= d_mu + 1?   {all_ok_E}")
    print(f"All E': d(E'(s^*_mu)) <= d_mu + 1?  {all_ok_Ep}")
