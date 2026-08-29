"""Day 124: Verify deg_t (Sigma(s_mu)) = deg_t (Sigma(s*_mu)) = d_mu = mu_1 + floor((mu_2+mu_3)/2).

If so, Psi's t-degree preservation (top of s_mu, s*_mu match d_mu) makes sense.

Also, this suggests that in the ASSOCIATED GRADED ring w.r.t. the ker(Sigma)-adic filtration
or the (1,1,2)-weight filtration, Psi respects the degree.

Compute Sigma(s_mu) as polynomial in (j, t) and take deg_t.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer

from individual_weight import s_star_mu, sym_to_e_basis
from pi_star_on_monomials import s_ord_mu, enum_parts

e1, e2, e3, u1, u2, u3, j, t = symbols('e1 e2 e3 u1 u2 u3 j t')


def sigma_e(f_e):
    """Substitute e_1 -> t + j, e_2 -> t(j+1), e_3 -> t^2."""
    return expand(f_e.subs({e1: t + j, e2: t * (j + 1), e3: t**2}))


def deg_t_of_poly_jt(f):
    if f == 0:
        return -1
    p = Poly(f, t)
    return p.degree()


def d_mu(mu):
    return mu[0] + (mu[1] + mu[2]) // 2


def main():
    print('=' * 80)
    print(f"{'mu':<15} {'d(mu)':<8} {'deg_t Sigma(s_mu)':<20} {'deg_t Sigma(s*_mu)':<20}")
    print('=' * 80)
    for mu in enum_parts(6):
        s = s_ord_mu(mu)
        s_e = sym_to_e_basis(s)
        sig_s = sigma_e(s_e)
        d_s = deg_t_of_poly_jt(sig_s)

        ss = s_star_mu(mu)
        ss_e = sym_to_e_basis(ss)
        sig_ss = sigma_e(ss_e)
        d_ss = deg_t_of_poly_jt(sig_ss)

        d = d_mu(mu)
        print(f"  {str(mu):<15} {d:<8} {d_s:<20} {d_ss:<20}")


if __name__ == '__main__':
    main()
