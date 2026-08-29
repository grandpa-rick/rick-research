"""Day 124: Study the difference s*_mu - s_mu via Weyl formula.

s_mu = det(u_i^{k_j}) / V(u), k = (mu_1 + 2, mu_2 + 1, mu_3).
s*_mu = det([u_i]_{k_j}) / V(u).

[u_i]_k = sum_m stirling1(k, m) u_i^m  (signed Stirling first kind).

So det([u_i]_{k_j}) - det(u_i^{k_j}) = sum over "lower" configurations.

Let's compute s*_mu - s_mu in e-basis for several mu, and check:
  weight_{112}(s*_mu - s_mu) <= d_mu?
  If YES: this means s*_mu = s_mu + (lower or equal weight terms) in e-basis.

We already saw examples where top(s*_mu) != top(s_mu), BUT with same weight d_mu.
So (s*_mu - s_mu) can have SAME weight d_mu (not lower).

Nevertheless, let's compute and see the STRUCTURE of the difference.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

from sympy import symbols, expand, Poly, Integer
from individual_weight import s_star_mu, sym_to_e_basis
from pi_star_on_monomials import s_ord_mu, enum_parts, weight_112_tuple

e1, e2, e3 = symbols('e1 e2 e3')


def d_mu(mu):
    return mu[0] + (mu[1] + mu[2]) // 2


def weight_of(f):
    if f == 0:
        return -1
    p = Poly(expand(f), e1, e2, e3)
    return max(a1 + a2 + 2*a3 for (a1, a2, a3), _ in p.terms())


def main():
    print('=' * 80)
    print(f"{'mu':<15} {'d(mu)':<8} {'w(s*-s)':<10} description")
    print('=' * 80)
    for mu in enum_parts(6):
        s = s_ord_mu(mu)
        ss = s_star_mu(mu)
        diff = expand(sym_to_e_basis(ss - s))
        d = d_mu(mu)
        w = weight_of(diff)
        print(f"  {str(mu):<15} {d:<8} {w:<10} diff = {diff}")


if __name__ == '__main__':
    main()
