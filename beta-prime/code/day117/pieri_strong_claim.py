"""Day 117 — Test the STRONG per-term shifted-Pieri claim:
  In s^*_{(1,1)} * s^*_mu = sum_{lambda/mu vert 2-strip} s^*_lambda + sum_{lower lambda} c^lambda_mu s^*_lambda,
  ALL "lower" lambda appearing satisfy d_lambda <= d_mu + 1.

If this is proved as an algebraic identity (from Molev's shifted Pieri), then
E'(s^*_mu) in F^{d_mu + 1} PER-TERM, hence E(s^*_mu) = s^*_{(1,1)} s^*_mu - E'(s^*_mu) in F^{d_mu + 1}.

We also test the SEPARATE claim: all VERT-2-STRIP lambda have d_lambda <= d_mu + 2
(the extreme case).
"""
from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from eprime_filtration import vert_2_strips_from
from decompose_s11_pow import expand_in_shifted_basis
from sympy import symbols, expand, Integer

u, y, c = symbols('u y c')


def upi_deg(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


if __name__ == "__main__":
    xs = (u, y, c)
    s11 = factorial_schur((1, 1, 0), xs)

    max_size = 6
    print(f"Testing STRONG per-term Pieri claim (lower lambda has d_lambda <= d_mu + 1)")
    print(f"Also: top (vert-2-strip) lambda has d_lambda <= d_mu + 2 (individually)")
    print()
    print(f"{'mu':>15} {'d_mu':>5} {'max d_top':>10} {'max d_lower':>12} {'flag_lower'}")
    print('-' * 80)
    all_ok_strong = True
    for N in range(max_size + 1):
        for mu in all_partitions_len_le_3(N):
            s_star_mu = factorial_schur(mu, xs)
            d_mu = upi_deg(s_star_mu)
            product = expand(s11 * s_star_mu)
            coeffs = expand_in_shifted_basis(product, xs, max_size=N + 2)
            # Split into TOP (|lambda| = |mu| + 2) and LOWER
            vert_strips = set(vert_2_strips_from(mu))
            max_d_top = -1
            max_d_lower = -1
            lower_fails = []
            for lam, cv in coeffs.items():
                d_lam = upi_deg(factorial_schur(lam, xs))
                if lam in vert_strips:
                    max_d_top = max(max_d_top, d_lam)
                else:
                    max_d_lower = max(max_d_lower, d_lam)
                    if d_lam > d_mu + 1:
                        lower_fails.append((lam, d_lam, cv))
            flag = "OK" if not lower_fails else "!!FAIL!!"
            if lower_fails:
                all_ok_strong = False
            print(f"{str(mu):>15} {d_mu:>5} {max_d_top:>10} {max_d_lower:>12}  {flag}")
            if lower_fails:
                for lam, d, cv in lower_fails:
                    print(f"    FAIL: lambda={lam}, d_lam={d}, coeff={cv}")
    print()
    print(f"STRONG per-term claim (all lower d_lam <= d_mu + 1): {all_ok_strong}")
