"""Day 124: Compute Pi*(m) for each monomial m = e_1^a1 e_2^a2 e_3^a3
directly by inverting Psi and multiplying by e_2.

Strategy:
  1. Enumerate all partitions nu with |nu| <= N, l <= 3.
  2. Compute s_nu (ordinary Schur, symmetric polynomial in u1, u2, u3) in e-basis.
     This gives a matrix M: nu -> e-basis coefficients.
  3. Compute s*_nu in e-basis (already done).
  4. Compute Psi(m) for a monomial m: express m as sum c_nu s_nu (invert M),
     then Psi(m) = sum c_nu s*_nu, then expand in e-basis.
  5. Pi*(m) = Psi(e_2 * Psi^{-1}(m)):
     write m = sum c_nu s*_nu (invert the s*_nu -> e-basis matrix),
     then Psi^{-1}(m) = sum c_nu s_nu,
     then multiply by e_2, expand in ordinary Schur basis (Pieri),
     then apply Psi to get sum in s*_lambda,
     then expand in e-basis.

For our purpose we want to see: does Pi* increase (1,1,2)-weight by at most 1
on every monomial? If YES: filtration preservation holds automatically.
If NO: filtration preservation is a genuine cancellation phenomenon
requiring careful analysis of which linear combos of monomials have low weight.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational, Matrix
from itertools import product
from collections import defaultdict

from individual_weight import s_star_mu, sym_to_e_basis, weight_112

e1, e2, e3 = symbols('e1 e2 e3')
u1, u2, u3 = symbols('u1 u2 u3')


def s_ord_mu(mu):
    """Ordinary Schur s_mu(u1, u2, u3) via Weyl formula."""
    mu = list(mu) + [0] * (3 - len(mu))
    mu = mu[:3]
    k = [mu[0] + 2, mu[1] + 1, mu[2]]
    xs = [u1, u2, u3]
    rows = [[xs[i]**k[l] for l in range(3)] for i in range(3)]
    numer = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
             - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
             + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
    V = (u1 - u2) * (u1 - u3) * (u2 - u3)
    q, r = sp.div(sp.Poly(expand(numer), u1, u2, u3), sp.Poly(expand(V), u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError(f'Not divisible for mu={mu}')
    return expand(q.as_expr())


def enum_parts(max_total, ell=3):
    """All partitions of total <= max_total with l <= ell."""
    res = []
    for tot in range(max_total + 1):
        # generate partitions of tot with l <= ell
        def gen(remaining, max_part, l):
            if l == 0:
                if remaining == 0:
                    yield ()
                return
            for part in range(min(remaining, max_part) + 1):
                for rest in gen(remaining - part, part, l - 1):
                    yield (part,) + rest
        for p in gen(tot, tot, ell):
            # Normalize (larger first) — gen produces (largest to smallest).
            res.append(p)
    return res


def poly_to_e_coeffs(f, max_deg=20):
    """f is polynomial in e1, e2, e3. Return dict (a1, a2, a3) -> coef."""
    if f == 0:
        return {}
    p = Poly(expand(f), e1, e2, e3)
    return {tuple(k): v for k, v in zip(p.monoms(), p.coeffs())}


def dict_to_poly(d):
    result = Integer(0)
    for (a1, a2, a3), c in d.items():
        result += c * e1**a1 * e2**a2 * e3**a3
    return expand(result)


def build_change_of_basis(max_total, basis='ord'):
    """Build matrix from Schur (or shifted Schur) basis to e-basis monomials.
    Returns (partitions, e_monoms, matrix M) where M[i, j] = coeff of e_monom[i] in basis element[j].
    """
    partitions = enum_parts(max_total)
    # Compute each basis element in e-basis
    e_maps = []
    for mu in partitions:
        if basis == 'ord':
            s = s_ord_mu(mu)
        else:
            s = s_star_mu(mu)
        s_e = sym_to_e_basis(s)
        e_maps.append(poly_to_e_coeffs(s_e))
    # Collect all monomials
    monoms = set()
    for d in e_maps:
        monoms.update(d.keys())
    monoms = sorted(monoms)
    monom_idx = {m: i for i, m in enumerate(monoms)}
    M = sp.zeros(len(monoms), len(partitions))
    for j, d in enumerate(e_maps):
        for m, c in d.items():
            M[monom_idx[m], j] = c
    return partitions, monoms, M


def multiply_e2_ord(nu, ell=3):
    """Apply Pieri: e_2 * s_nu = sum s_lambda for lambda in nu boxplus (1,1) with l <= ell."""
    nu = list(nu) + [0] * (ell + 1 - len(nu))
    results = []
    for i in range(ell + 1):
        for k in range(i + 1, ell + 1):
            new = list(nu)
            new[i] += 1
            new[k] += 1
            if all(new[m] >= new[m + 1] for m in range(len(new) - 1)):
                # trim
                nn = list(new)
                while nn and nn[-1] == 0:
                    nn.pop()
                if len(nn) > ell:
                    continue
                while len(nn) < 3:
                    nn.append(0)
                results.append(tuple(nn[:3]))
    return results


def build_pi_star_matrix(max_total_in, ell=3):
    """Build the matrix representation of Pi* in the e-monomial basis.

    Pi*(m) = Psi(e_2 * Psi^{-1}(m)) where Psi(s_nu) = s*_nu (extended by linearity).

    For an input monomial m of e-basis degree at most max_total_in, output
    monomials of degree at most max_total_in + 2 (since e_2 raises degree by 2).

    We compute Pi*(m) explicitly by:
      1. Express m in shifted-Schur basis: m = sum a_nu s*_nu (via basis inversion).
      2. Psi^{-1}(m) = sum a_nu s_nu.
      3. Multiply by e_2: sum a_nu sum_lambda s_lambda (Pieri).
      4. Psi: sum a_nu sum_lambda s*_lambda.
      5. Express result in e-basis.

    But: for step 1 to work, ALL shifted-Schur functions s*_nu with |nu| relevant
    to m must be included. Total degree of s*_nu = |nu|. But s*_nu, expressed in
    e-basis, has terms of e-basis-degree ranging from 0 up to |nu|. So a monomial
    of e-basis-degree D is a linear combo of s*_nu with |nu| <= D... actually
    that's not right either. Let me think.

    Actually: s*_nu has TOP e-degree = |nu| (the leading term is s_nu). Lower
    degree terms exist. So to express a specific e-monomial of degree D, we
    might need s*_nu of ALL total degrees up to D. But s*_nu with |nu| > D
    can also contribute to a linear combo if we allow cancellation.

    Simplification: work with SHIFTED-e-degree. Note s*_nu of total degree |nu|
    in u_i variables corresponds to e-polynomial of total e-degree = |nu|
    (since s_nu is homogeneous of degree |nu|, and s*_nu = s_nu + lower).

    So the top-e-degree map is s*_nu -> s_nu. So s*_nu spans a subspace with
    a triangular structure w.r.t. total e-degree. To express monomial e^alpha
    of total degree |alpha| in {s*_nu}, we need |nu| = |alpha| (top) plus
    lower |nu| < |alpha| to correct. So {s*_nu : |nu| <= D} spans the same
    space as {s_nu : |nu| <= D}, which is the degree-<=-D component of Sym_3.

    An e-monomial of total e-degree D has total u-degree = D + (deg by e_2 or e_3)
    ... wait. e_1 has degree 1, e_2 has degree 2, e_3 has degree 3. So the
    e-monomial e_1^a1 e_2^a2 e_3^a3 has u-degree a1 + 2 a2 + 3 a3 (this is a
    DIFFERENT weight from the (1,1,2)-weight).

    So to express e^alpha of u-degree D_u in {s*_nu}, need |nu| <= D_u and
    top |nu| = D_u.
    """
    # Enumerate e-monomials of u-degree <= max_total_in
    input_monoms = []
    for a1 in range(max_total_in + 1):
        for a2 in range((max_total_in - a1) // 2 + 1):
            for a3 in range((max_total_in - a1 - 2*a2) // 3 + 1):
                if a1 + 2*a2 + 3*a3 <= max_total_in:
                    input_monoms.append((a1, a2, a3))

    max_total_out = max_total_in + 2  # e_2 adds 2 to u-degree

    # Need s*_nu for |nu| <= max_total_out (u-degree)
    max_partition_size = max_total_out
    partitions = enum_parts(max_partition_size)

    # Precompute s*_nu in e-basis
    s_star_e = {nu: poly_to_e_coeffs(sym_to_e_basis(s_star_mu(nu))) for nu in partitions}

    # Precompute e_2 * s_nu = sum_lambda s_lambda (Pieri)
    e2_pieri = {nu: multiply_e2_ord(nu) for nu in partitions}

    # We need to solve, for each input monom m: express m as sum a_nu s*_nu.
    # Do this by building the (change of basis) matrix from {s*_nu} to e-monomials
    # of u-degree <= max_partition_size, then invert / solve.

    # e-monomials of u-degree <= max_partition_size
    all_e_monoms = []
    for a1 in range(max_partition_size + 1):
        for a2 in range((max_partition_size - a1) // 2 + 1):
            for a3 in range((max_partition_size - a1 - 2*a2) // 3 + 1):
                if a1 + 2*a2 + 3*a3 <= max_partition_size:
                    all_e_monoms.append((a1, a2, a3))
    all_e_monoms.sort()
    monom_idx = {m: i for i, m in enumerate(all_e_monoms)}

    # Sanity check: number of monomials should equal number of partitions with |nu| <= max
    # (both are dimensions of Sym_3 of appropriate degree). They ARE equal because
    # Sym_3 as graded ring has same dim in each degree as the appropriate polynomial
    # ring in e's.
    # print(f'#partitions = {len(partitions)}, #e_monoms = {len(all_e_monoms)}')

    # Build matrix M: columns are s*_nu in e-basis
    M = sp.zeros(len(all_e_monoms), len(partitions))
    for j, nu in enumerate(partitions):
        for m, c in s_star_e[nu].items():
            if m in monom_idx:
                M[monom_idx[m], j] = c

    # Now for each input monom, solve M @ x = e_hat_m
    # Then x_nu = coefficient of s*_nu in m.
    # Then Psi^{-1}(m) = sum x_nu s_nu.
    # Then e_2 * that = sum x_nu * sum_lambda s_lambda.
    # Then Psi(...) = sum x_nu * sum_lambda s*_lambda.
    # Then output in e-basis.

    # Precompute LU of M
    print(f'Computing LU decomposition of {len(all_e_monoms)}x{len(partitions)} matrix...')
    # M should be square if we set up right
    if M.rows != M.cols:
        raise ValueError(f'Matrix not square: {M.rows}x{M.cols}')

    pi_star_action = {}
    for m in input_monoms:
        # RHS
        b = sp.zeros(len(all_e_monoms), 1)
        b[monom_idx[m], 0] = 1
        x = M.solve(b)
        # x[j] = coefficient of s*_{partitions[j]} in m
        # Now compute image
        result = defaultdict(lambda: Integer(0))
        for j, nu in enumerate(partitions):
            if x[j, 0] == 0:
                continue
            coef = x[j, 0]
            for lam in e2_pieri[nu]:
                for mono, c in s_star_e.get(lam, {}).items():
                    result[mono] += coef * c
        pi_star_action[m] = {k: sp.simplify(v) for k, v in result.items() if v != 0}
    return input_monoms, pi_star_action


def weight_112_tuple(t):
    a1, a2, a3 = t
    return a1 + a2 + 2 * a3


def main():
    print('Building Pi* action on e-monomials with u-degree <= 6')
    input_monoms, pi_star = build_pi_star_matrix(6)
    print()
    print('Pi*(m) in e-basis, with (1,1,2)-weights of inputs and outputs:')
    print('=' * 70)
    for m in input_monoms:
        w_in = weight_112_tuple(m)
        image = pi_star[m]
        w_out = max([weight_112_tuple(k) for k in image.keys()], default=-1)
        top_out = w_out
        marker = 'OK' if w_out <= w_in + 1 else '!!! WEIGHT INCREASE > 1'
        print(f'\n  m = e_1^{m[0]} e_2^{m[1]} e_3^{m[2]}  (weight {w_in})')
        print(f'    Pi*(m): weight = {w_out}  {marker}')
        # Print image
        for mono in sorted(image.keys()):
            c = image[mono]
            w = weight_112_tuple(mono)
            top = ' [TOP]' if w == w_out else ''
            print(f'      e_1^{mono[0]} e_2^{mono[1]} e_3^{mono[2]}: {c}  (w={w}){top}')


if __name__ == '__main__':
    main()
