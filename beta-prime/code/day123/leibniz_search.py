"""Day 123: Search for Leibniz identity for phi(e_2 * s_nu).

phi(s_mu) = F_mu(j, t) via (A,B) closed form (length <= 3 only; else 0).

For each test partition nu, use ordinary Pieri:
  e_2 * s_nu = sum_lambda s_lambda   where lambda/nu is a vertical 2-strip.
For length <= 3 only, the possible lambdas are:
  1. (nu1+1, nu2+1, nu3)               always
  2. (nu1+1, nu2, nu3+1)               iff nu2 > nu3
  3. (nu1, nu2+1, nu3+1)               iff nu1 > nu2
Plus length > 3 lambdas which phi kills.

Test candidate A(j, t) via:
  phi(e_2 * s_nu) - t * A(j, t) * phi(s_nu) = Delta(nu)
  Want deg_t Delta <= deg_t phi(s_nu).
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')

import sympy as sp
from sympy import symbols, expand, Poly, factor, simplify

from ab_recursion import build_AB
from n_mu_formula import N_mu, F_mu

j, t = symbols('j t')


def F(mu, A, B):
    """phi(s_mu) — kills length > 3."""
    if len(mu) > 3 and any(mu[3:]):
        return sp.Integer(0)
    mu3 = list(mu[:3])
    while len(mu3) < 3:
        mu3.append(0)
    return F_mu(tuple(mu3), A, B)


def e2_pieri(nu):
    """Return list of lambda's such that lambda/nu is a vertical 2-strip.
    Only lambdas with length <= 3 are returned (others map to 0 under phi).
    """
    n = list(nu) + [0, 0, 0]
    n = n[:3]
    n1, n2, n3 = n
    results = []
    # (rows 1, 2)
    results.append((n1 + 1, n2 + 1, n3))
    # (rows 1, 3): valid iff n2 > n3
    if n2 > n3:
        results.append((n1 + 1, n2, n3 + 1))
    # (rows 2, 3): valid iff n1 > n2
    if n1 > n2:
        results.append((n1, n2 + 1, n3 + 1))
    # length 4+ lambdas: phi kills them, skip
    return results


def phi_e2_nu(nu, A, B):
    """Compute phi(e_2 * s_nu) via Pieri."""
    lambdas = e2_pieri(nu)
    total = sp.Integer(0)
    for lam in lambdas:
        total += F(lam, A, B)
    return expand(total)


def deg_t(expr):
    if expr == 0:
        return -1
    return Poly(expr, t).degree()


def main():
    A, B = build_AB(20)

    test_nus = [
        (0, 0, 0),
        (1, 0, 0),
        (2, 0, 0),
        (1, 1, 0),
        (3, 0, 0),
        (2, 1, 0),
        (2, 2, 0),
        (1, 1, 1),
        (4, 0, 0),
        (3, 1, 0),
        (2, 2, 1),
        (3, 2, 0),
        (2, 1, 1),
        (3, 3, 0),
        (4, 1, 0),
        (4, 2, 0),
        (4, 1, 1),
        (3, 2, 1),
        (2, 2, 2),
    ]

    # Compute phi(s_nu) and phi(e_2 * s_nu) for each nu
    data = []
    for nu in test_nus:
        f_nu = F(nu, A, B)
        f_e2_nu = phi_e2_nu(nu, A, B)
        data.append((nu, f_nu, f_e2_nu))

    print('=' * 70)
    print('Table of phi(s_nu) and phi(e_2 * s_nu):')
    print('=' * 70)
    for nu, f_nu, f_e2_nu in data:
        print(f'\nnu = {nu}')
        print(f'  phi(s_nu)      = {f_nu}')
        print(f'    deg_t = {deg_t(f_nu)}, deg_j = {Poly(f_nu, j).degree() if f_nu != 0 else -1}')
        print(f'  phi(e_2*s_nu) = {f_e2_nu}')
        print(f'    deg_t = {deg_t(f_e2_nu)}, deg_j = {Poly(f_e2_nu, j).degree() if f_e2_nu != 0 else -1}')

    # Now: try candidate A(j, t)
    # Simplest guess: A = j (from the empty case)
    print()
    print('=' * 70)
    print('Test candidate A(j,t) = j:')
    print('=' * 70)
    A_cand = j
    all_ok = True
    for nu, f_nu, f_e2_nu in data:
        Delta = expand(f_e2_nu - t * A_cand * f_nu)
        dt_Delta = deg_t(Delta)
        dt_phi = deg_t(f_nu)
        ok = dt_Delta <= dt_phi if f_nu != 0 else dt_Delta <= 0
        marker = 'OK' if ok else '!!! FAIL'
        if not ok:
            all_ok = False
        print(f'  nu={nu}: deg_t Delta = {dt_Delta}, deg_t phi(s_nu) = {dt_phi}  {marker}')
        if not ok or True:
            print(f'    Delta = {Delta}')

    print(f'\n[A = j]  Overall: {"PASS" if all_ok else "FAIL"}')


if __name__ == '__main__':
    main()
