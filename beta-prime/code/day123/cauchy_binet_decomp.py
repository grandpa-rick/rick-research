"""Day 123: Cauchy-Binet decomposition of shifted Schur in terms of ordinary Schur.

Fact: [x]_k = sum_m s(k, m) x^m  where s(k, m) are signed Stirling numbers of first kind.

So the Weyl determinant det([x_i]_{k_l}) = det(X * S) where
  X_{i, m} = x_i^m   (3 x (K+1) matrix)
  S_{m, l} = s(k_l, m)   ((K+1) x 3 matrix, entry 0 if m > k_l)

By Cauchy-Binet:
  det([x_i]_{k_l}) = sum_{|J|=3} det(X_{[3], J}) det(S_{J, [3]})

Now det(X_{[3], J}) = det(x_i^{J_m}) = -s_{lambda(J)}(x) V(x)
where lambda(J) = (J_3 - 2, J_2 - 1, J_1) for J_1 < J_2 < J_3 (extra -1 from column reversal for 3x3).

So s*_mu(x) = det/V = -sum_J det(S_{J,[3]}(l_mu)) s_{lambda(J)}(x)

Aggregate:
  sum_mu K_{mu', (2^j)} s*_mu = sum_J D_J^{(j)} s_{lambda(J)}
where D_J^{(j)} = -sum_mu K_{mu', (2^j)} det(S_{J,[3]}(l_mu)).

Under specialization phi(s_lambda) = s_lambda(t, y, c)|_{spec} with deg_t = lambda_1 + floor((lambda_2+lambda_3)/2):
  phi(e_2^j) = sum_J D_J^{(j)} * phi_ord(s_{lambda(J)})

We want deg_t phi(e_2^j) <= j, so want: whenever deg_t phi_ord(s_lambda(J)) > j, either
D_J = 0, or cancellations among terms.

Let's compute D_J and study.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')

import sympy as sp
from sympy import symbols, expand, Poly, factor, Integer, Rational
from sympy.functions.combinatorial.numbers import stirling
from collections import defaultdict
from itertools import combinations

j, t = symbols('j t')


def stir_first(k, m):
    """Signed Stirling number of first kind: [x]_k = sum_m stir_first(k, m) x^m."""
    return stirling(k, m, kind=1, signed=True)


def kostka_via_e2j(j_val, max_ell=3):
    """Schur expansion of e_2^{j_val} restricted to length <= max_ell. Returns dict mu -> coef."""
    current = defaultdict(int)
    current[()] = 1

    def e2_action(nu, ell=max_ell):
        nu_padded = list(nu) + [0] * max(0, ell + 1 - len(nu))
        results = []
        for i in range(ell + 2):
            for j2 in range(i + 1, ell + 2):
                new_nu = list(nu_padded)
                while len(new_nu) <= j2:
                    new_nu.append(0)
                new_nu[i] += 1
                new_nu[j2] += 1
                if all(new_nu[k] >= new_nu[k + 1] for k in range(len(new_nu) - 1)):
                    while new_nu and new_nu[-1] == 0:
                        new_nu.pop()
                    if len(new_nu) <= ell:
                        results.append(tuple(new_nu))
        return results

    for _ in range(j_val):
        new_current = defaultdict(int)
        for nu, c in current.items():
            for lam in e2_action(nu):
                new_current[lam] += c
        current = new_current
    # Add missing keys for uniformity
    out = {}
    for mu, K in current.items():
        mu_padded = list(mu) + [0] * (3 - len(mu))
        out[tuple(mu_padded)] = K
    return out


def stir_matrix(l_mu):
    """S submatrix: rows indexed by m (0..max l_mu), cols by l=1,2,3 with k_l = l_mu[l]."""
    K = max(l_mu)
    S = []
    for m in range(K + 1):
        row = [stir_first(k, m) for k in l_mu]
        S.append(row)
    return S


def det3(M):
    """3x3 determinant."""
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def D_J(J, j_val):
    """Compute D_J^{(j)} = -sum_mu K_{mu', (2^j)} * det(S_{J,[3]}(l_mu))."""
    e2j = kostka_via_e2j(j_val, max_ell=3)
    total = Integer(0)
    for mu, K in e2j.items():
        mu_padded = list(mu) + [0] * (3 - len(mu))
        l_mu = (mu_padded[0] + 2, mu_padded[1] + 1, mu_padded[2])
        if max(J) > max(l_mu):
            continue
        # Build 3x3 minor: rows J, cols [3] of S
        M = []
        for jrow in J:
            row = [stir_first(k, jrow) for k in l_mu]
            M.append(row)
        d = det3(M)
        total += K * d
    return -total


def lambda_from_J(J):
    """lambda(J) = (J_3 - 2, J_2 - 1, J_1) for J = (J_1 < J_2 < J_3)."""
    a1, a2, a3 = sorted(J)
    return (a3 - 2, a2 - 1, a1)


def is_partition(lam):
    return all(lam[i] >= lam[i+1] for i in range(len(lam) - 1)) and lam[-1] >= 0


def main():
    for j_val in range(1, 7):
        print('=' * 70)
        print(f'j = {j_val}')
        print('=' * 70)
        # enumerate J subsets that could contribute
        # max J entry: max l_mu[0] = mu_1 + 2 with mu_1 <= j, so <= j + 2
        # min J entry: 0
        K = j_val + 2
        results = []
        for J in combinations(range(K + 1), 3):
            lam = lambda_from_J(J)
            if not is_partition(lam):
                continue
            D = D_J(J, j_val)
            if D == 0:
                continue
            d_t = lam[0] + (lam[1] + lam[2]) // 2
            results.append((J, lam, D, d_t))
        for J, lam, D, d_t in results:
            marker = '' if d_t <= j_val else '  ***t-deg > j!'
            print(f'  J={J}, lambda={lam}, deg_t phi_ord(s_lambda)={d_t}, D_J={D}{marker}')

        # Verify: sum_J D_J * phi_ord(s_lambda(J)) equals phi(e_2^j) [computed elsewhere]
        # Just print total number of nonzero terms
        print(f'  Total nonzero D_J: {len(results)}')


if __name__ == '__main__':
    main()
