"""Day 123: Study leading t-coefficients of F_mu, look for uniform pattern.

Key empirical fact: deg_t F_mu = mu_1 + floor((mu_2 + mu_3)/2)  for 3-part mu.

We want deg_t S_j = deg_t sum_mu K_{mu', (2^j)} F_mu <= j.
This is equivalent to a cascade of cancellations at each t^d level for j < d <= d_max.

Let's look at:
  (i) The leading t-coeff of F_mu (as poly in j).
  (ii) The leading t-coeff of A_a and B_a (build intuition).
  (iii) Can we recognize S_j as some known specialization?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

import sympy as sp
from sympy import symbols, expand, Poly, factor, Integer

from ab_recursion import build_AB
from n_mu_formula import N_mu, F_mu

j, t = symbols('j t')


def F(mu, A, B):
    if len(mu) > 3 and any(mu[3:]):
        return sp.Integer(0)
    mu3 = list(mu[:3])
    while len(mu3) < 3:
        mu3.append(0)
    return F_mu(tuple(mu3), A, B)


def leading_t_coeff(expr, var=t):
    if expr == 0:
        return Integer(0)
    p = Poly(expr, var)
    return p.LC()


def deg_t(expr):
    if expr == 0:
        return -1
    return Poly(expr, t).degree()


def kostka_via_e2j(j_val, max_ell=3):
    """Compute Schur expansion of e_2^{j_val} restricted to length <= max_ell.
    Returns dict mu -> coefficient.
    Uses iterated Pieri.
    """
    from collections import defaultdict
    # start with 1 (empty partition)
    current = defaultdict(int)
    current[()] = 1

    def e2_action(nu, ell=max_ell):
        """List of lambdas with mult 1 from e_2 * s_nu (with length <= ell)."""
        nu_padded = list(nu) + [0] * max(0, ell + 1 - len(nu))
        # positions where boxes can be added (partition constraint)
        # iterate over pairs (i, j), i < j, add box to row i and row j
        results = []
        # Add to rows within [0, ell) (i.e., row index)
        for i in range(ell + 2):
            for j2 in range(i + 1, ell + 2):
                new_nu = list(nu_padded)
                while len(new_nu) <= j2:
                    new_nu.append(0)
                new_nu[i] += 1
                new_nu[j2] += 1
                # check partition
                if all(new_nu[k] >= new_nu[k + 1] for k in range(len(new_nu) - 1)):
                    # truncate zeros
                    while new_nu and new_nu[-1] == 0:
                        new_nu.pop()
                    if len(new_nu) <= ell:
                        results.append(tuple(new_nu))
                    # else too long, drop
        return results

    for _ in range(j_val):
        new_current = defaultdict(int)
        for nu, c in current.items():
            for lam in e2_action(nu):
                new_current[lam] += c
        current = new_current
    return dict(current)


def main():
    A, B = build_AB(20)

    # (i) Leading t-coefficients of F_mu, mu <= 3 parts
    print('=' * 70)
    print('Leading t-coeff [t^{deg_t F_mu}] F_mu(j, t) for all mu vdash n <= 8')
    print('with length <= 3, mu_1 <= n/2  (i.e., relevant for S_{n/2}):')
    print('=' * 70)

    for total in range(0, 13, 2):
        j_val = total // 2
        print(f'\n|mu| = {total}, j = {j_val}, mu_1 <= {j_val}:')
        for mu1 in range(0, j_val + 1):
            for mu2 in range(0, mu1 + 1):
                mu3 = total - mu1 - mu2
                if mu3 < 0 or mu3 > mu2:
                    continue
                mu = (mu1, mu2, mu3)
                Fmu = F(mu, A, B)
                d = deg_t(Fmu)
                lc = leading_t_coeff(Fmu)
                exp_d = mu1 + (mu2 + mu3) // 2
                marker = 'OK' if d == exp_d else '!!!'
                print(f'  mu={mu}: deg_t={d} (exp {exp_d} {marker}), lead = {expand(lc)}')

    # (ii) Verify deg_t formula for F_mu
    print('\n' + '=' * 70)
    print('Verify formula: deg_t F_mu = mu_1 + floor((mu_2 + mu_3)/2)')
    print('=' * 70)
    all_ok = True
    for mu1 in range(0, 10):
        for mu2 in range(0, mu1 + 1):
            for mu3 in range(0, mu2 + 1):
                if mu1 + mu2 + mu3 > 15:
                    continue
                mu = (mu1, mu2, mu3)
                Fmu = F(mu, A, B)
                d = deg_t(Fmu)
                exp_d = mu1 + (mu2 + mu3) // 2
                if d != exp_d:
                    print(f'  MISMATCH mu={mu}: got {d}, exp {exp_d}')
                    all_ok = False
    print(f'Formula holds: {all_ok}')

    # (iii) Compute S_j and its coefficients for j = 1..6
    print('\n' + '=' * 70)
    print('S_j and its top t-coefficients:')
    print('=' * 70)
    for j_val in range(1, 7):
        e2j = kostka_via_e2j(j_val, max_ell=3)
        # sort mu's by mu_1 descending to trace top-t contributions
        S_j = Integer(0)
        contribs = []  # (mu, K, F_mu, deg, lead)
        for mu, K in sorted(e2j.items(), key=lambda x: (-x[0][0] if x[0] else 0)):
            if not mu:
                mu = (0, 0, 0)
            Fmu = F(mu, A, B)
            S_j += K * Fmu
            d = deg_t(Fmu)
            lc = leading_t_coeff(Fmu)
            contribs.append((mu, K, d, expand(lc)))
        S_j = expand(S_j)
        print(f'\nj = {j_val}:')
        for mu, K, d, lc in contribs:
            print(f'  mu={mu}, K={K}, deg_t F={d}, top t-coeff={lc}')
        # S_j t-decomposition
        p = Poly(S_j, t)
        max_d = p.degree()
        print(f'  S_j has deg_t = {max_d}  (goal: <= {j_val})')
        # print top few t-coefficients as polys in j
        for k in range(max_d, max(-1, max_d - 4), -1):
            coef = expand(p.nth(k))
            print(f'  [t^{k}] S_j = {coef}')


if __name__ == '__main__':
    main()
