"""Day 117 — Extended empirical check: does E: F^k -> F^{k+1} hold for larger mu?

We test up to |mu| = 8 (partitions of length <= 3).
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

    max_size = 8
    print(f"Testing E and E' filtration behavior up to |mu| = {max_size}")
    print(f"{'mu':>18} {'d_mu':>5} {'d(E(s*_mu))':>13} {'bd d_mu+1':>10} {'d(s11 s*_mu)':>14}")
    print('-' * 75)
    all_ok = True
    failures = []
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
            flag = "OK" if d_E <= d_mu + 1 else "!!FAIL!!"
            if d_E > d_mu + 1:
                all_ok = False
                failures.append((mu, d_mu, d_E))
            print(f"{str(mu):>18} {d_mu:>5} {d_E:>13} {flag:>10} {d_prod:>14}")
    print()
    print(f"All: d(E(s^*_mu)) <= d_mu + 1?  {all_ok}")
    if failures:
        print("Failures:")
        for mu, d_mu, d_E in failures:
            print(f"  mu = {mu}: d_mu = {d_mu}, d(E) = {d_E}")
