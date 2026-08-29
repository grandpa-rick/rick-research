"""Day 124: Compare (1,1,2)-weight of s_μ vs s*_μ.

For each partition μ, compute:
  - w(s_μ) in e-basis (ordinary Schur)
  - w(s*_μ) in e-basis (shifted Schur)

Empirical observation to test: w(s_μ) = w(s*_μ) for all μ, and this is
some explicit function d(μ).

If yes, Psi being weight-preserving on the basis {s_μ} means Ψ maps
weight-w(s_μ) basis element to weight-w(s*_μ) basis element. If w(s_μ) = w(s*_μ),
then Ψ is filtration-preserving on the s_-basis.

But we want filtration preservation on the e-monomial basis. So there's an
additional relationship needed: express e-monomial as combination of s_μ, and
match filtration parts.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer

from individual_weight import s_star_mu, sym_to_e_basis
from pi_star_on_monomials import s_ord_mu, enum_parts, poly_to_e_coeffs, weight_112_tuple

e1, e2, e3 = symbols('e1 e2 e3')


def weight_of_poly(f):
    if f == 0:
        return -1
    p = Poly(expand(f), e1, e2, e3)
    return max(a1 + a2 + 2*a3 for (a1, a2, a3), _ in p.terms())


def d_mu(mu):
    return mu[0] + (mu[1] + mu[2]) // 2


def main():
    print('=' * 80)
    print(f"{'mu':<15} {'|mu|':<6} {'d(mu)':<8} {'w(s_mu)':<10} {'w(s*_mu)':<10} {'match?'}")
    print('=' * 80)
    all_match_smu_dmu = True
    all_match_sstar_dmu = True
    for mu in enum_parts(8):
        s = s_ord_mu(mu)
        s_e = sym_to_e_basis(s)
        w_s = weight_of_poly(s_e)
        ss = s_star_mu(mu)
        ss_e = sym_to_e_basis(ss)
        w_ss = weight_of_poly(ss_e)
        d = d_mu(mu)
        match_s = (w_s == d)
        match_ss = (w_ss == d)
        if not match_s:
            all_match_smu_dmu = False
        if not match_ss:
            all_match_sstar_dmu = False
        agree = (w_s == w_ss)
        marker = '' if agree else '<-- DISAGREE'
        print(f"  {str(mu):<15} {sum(mu):<6} {d:<8} {w_s:<10} {w_ss:<10} {marker}")

    print()
    print(f'w(s_mu) = d_mu (for all tested mu): {all_match_smu_dmu}')
    print(f'w(s*_mu) = d_mu (for all tested mu): {all_match_sstar_dmu}')

    # Alternative: check w(s*_mu) <= max(w(monomials in s_mu)) via top-degree part
    # But s_mu top e-degree is |mu|, no wait, top e-degree of s_mu is |mu|.
    # Hmm the KEY IS how weight distributes in s_mu itself.
    print()
    print('=' * 80)
    print(f"{'mu':<15} {'|mu|':<6} weights of monomials in s_mu (as multiset)")
    print('=' * 80)
    for mu in enum_parts(5):
        s = s_ord_mu(mu)
        s_e = sym_to_e_basis(s)
        p = Poly(s_e, e1, e2, e3)
        weights = sorted([a1 + a2 + 2*a3 for (a1, a2, a3), _ in p.terms()])
        print(f"  {str(mu):<15} {sum(mu):<6} {weights}")

    print()
    print('=' * 80)
    print(f"{'mu':<15} {'|mu|':<6} weights of monomials in s*_mu")
    print('=' * 80)
    for mu in enum_parts(5):
        ss = s_star_mu(mu)
        ss_e = sym_to_e_basis(ss)
        p = Poly(ss_e, e1, e2, e3)
        weights = sorted([a1 + a2 + 2*a3 for (a1, a2, a3), _ in p.terms()])
        print(f"  {str(mu):<15} {sum(mu):<6} {weights}")


if __name__ == '__main__':
    main()
