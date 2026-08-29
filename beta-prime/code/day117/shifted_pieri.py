"""Day 117 — Derive the shifted Pieri rule for s^*_{(1,1)} * s^*_mu empirically
in 3 variables, and check whether the correction terms preserve (u,pi)-degree.
"""
from ordinary_schur_deg import (
    factorial_schur, ord_schur, all_partitions_len_le_3, V_expr,
)
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from decompose_s11_pow import expand_in_shifted_basis
from sympy import symbols, expand, Integer

u, y, c = symbols('u y c')


def upi_deg(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


if __name__ == "__main__":
    xs = (u, y, c)
    s11 = factorial_schur((1, 1, 0), xs)
    d_s11 = upi_deg(s11)
    print(f"s^*_{{(1,1)}} = {expand(s11)}")
    print(f"(u,pi)-deg(s^*_{{(1,1)}}) = {d_s11}")
    print()

    # For each mu, compute s^*_{(1,1)} * s^*_mu and decompose in shifted Schur basis.
    max_size = 4  # go up to |mu| = 4
    print(f"Shifted Pieri: s^*_{{(1,1)}} * s^*_mu decomposition")
    print(f"{'mu':>15} {'d_mu':>5} {'lambda':>15} {'d_lam':>5} {'coeff':>10} {'flag':>15}")
    print('-' * 80)
    for N in range(max_size + 1):
        for mu in all_partitions_len_le_3(N):
            s_star_mu = factorial_schur(mu, xs)
            product = expand(s11 * s_star_mu)
            coeffs = expand_in_shifted_basis(product, xs, max_size=N + 2)
            d_mu = upi_deg(s_star_mu)
            # Sort by (|lam|, lam) descending
            for lam, cv in sorted(coeffs.items(), key=lambda kv: (sum(kv[0]), kv[0]), reverse=True):
                d_lam = upi_deg(factorial_schur(lam, xs))
                # Flag: "top" if |lam| = |mu| + 2, else "lower"
                if sum(lam) == N + 2:
                    flag = "TOP"
                else:
                    flag = "lower"
                print(f"{str(mu):>15} {d_mu:>5} {str(lam):>15} {d_lam:>5} {str(cv):>10} {flag:>15}")
            print()
