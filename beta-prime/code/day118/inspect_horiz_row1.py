"""Day 118 — For each mu where the structural bound fails (horiz 2-strip in row 1
gives d_lambda = d_mu + 2), check whether the coefficient c^lambda_mu in the
shifted Pieri actually vanishes.

If it does: this is a NEW STRUCTURAL VANISHING to prove.
If not: there must be cancellation somewhere else.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day118')

from verify_pieri_extended import verify_mu, get_factorial_schur, get_d
from sympy import symbols

u, y, c = symbols('u y c')

if __name__ == "__main__":
    print("Checking coefficients of horizontal-2-strip-in-row-1 lambda")
    print("(i.e., lam = (mu_1+2, mu_2, mu_3))")
    print()
    print(f"{'mu':>15} {'lam':>15} {'d_mu':>5} {'d_lam':>6} {'coeff c^lam_mu':>20}")
    print('-' * 70)
    from verify_pieri_extended import all_partitions_len_le_3
    for N in range(9):
        for mu in all_partitions_len_le_3(N):
            lam = (mu[0] + 2, mu[1], mu[2])
            # coefficient of s*_lam in s*_(1,1) · s*_mu
            ok, d_mu, failures, coeffs = verify_mu(mu)
            d_mu = get_d(mu)
            d_lam = get_d(lam)
            coeff = coeffs.get(lam, 0)
            marker = ""
            if d_lam > d_mu + 1:
                marker = " <-- danger (needs to vanish or produce cancellation)"
            print(f"{str(mu):>15} {str(lam):>15} {d_mu:>5} {d_lam:>6} {str(coeff):>20}{marker}")
