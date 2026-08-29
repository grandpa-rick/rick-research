"""Day 124 CRITICAL TEST: Does Psi itself preserve the (1,1,2)-filtration
on Q[e_1, e_2, e_3]?

If YES: Pi* = Psi ∘ (e_2 ·) ∘ Psi^{-1} preserves filtration up to +1 trivially.
Lemma 2 is instantly proved.

Psi: Q[e_1, e_2, e_3] -> Q[e_1, e_2, e_3] is the linear map defined by
Psi(s_mu) = s*_mu extended linearly.

To compute Psi(m) for an e-monomial m:
  1. Express m in ordinary Schur basis: m = sum a_nu s_nu.
  2. Psi(m) = sum a_nu s*_nu.
  3. Convert to e-basis.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer
from itertools import product

from individual_weight import s_star_mu, sym_to_e_basis
from pi_star_on_monomials import s_ord_mu, enum_parts, poly_to_e_coeffs, dict_to_poly, weight_112_tuple

e1, e2, e3 = symbols('e1 e2 e3')


def weight_of_poly(f):
    if f == 0:
        return -1
    p = Poly(expand(f), e1, e2, e3)
    return max(a1 + a2 + 2*a3 for (a1, a2, a3), _ in p.terms())


def build_psi_matrix(N):
    """Build Psi as a matrix on Q[e_1, e_2, e_3] restricted to u-degree <= N."""
    partitions = enum_parts(N)
    # Compute s_nu in e-basis
    ord_e = [poly_to_e_coeffs(sym_to_e_basis(s_ord_mu(nu))) for nu in partitions]
    # Compute s*_nu in e-basis
    star_e = [poly_to_e_coeffs(sym_to_e_basis(s_star_mu(nu))) for nu in partitions]

    # e-monomials of u-degree <= N
    monoms = []
    for a1 in range(N + 1):
        for a2 in range((N - a1) // 2 + 1):
            for a3 in range((N - a1 - 2*a2) // 3 + 1):
                if a1 + 2*a2 + 3*a3 <= N:
                    monoms.append((a1, a2, a3))
    monoms.sort()
    monom_idx = {m: i for i, m in enumerate(monoms)}

    # Matrix M_ord: columns are s_nu in e-basis
    M_ord = sp.zeros(len(monoms), len(partitions))
    for j, d in enumerate(ord_e):
        for m, c in d.items():
            if m in monom_idx:
                M_ord[monom_idx[m], j] = c

    # Matrix M_star: columns are s*_nu in e-basis
    M_star = sp.zeros(len(monoms), len(partitions))
    for j, d in enumerate(star_e):
        for m, c in d.items():
            if m in monom_idx:
                M_star[monom_idx[m], j] = c

    # Psi = M_star * M_ord^{-1}
    # I.e., for input monomial m: solve M_ord * x = m_hat, output = M_star * x.
    return monoms, monom_idx, partitions, M_ord, M_star


def compute_psi(f_dict, monoms, monom_idx, partitions, M_ord, M_star):
    """f_dict: e-monomial dict of input polynomial. Returns Psi(f) as e-monomial dict."""
    # RHS: input vector
    b = sp.zeros(len(monoms), 1)
    for m, c in f_dict.items():
        if m in monom_idx:
            b[monom_idx[m], 0] = c
        else:
            raise ValueError(f'Monomial {m} out of range')
    x = M_ord.solve(b)
    # Output: M_star * x
    out_vec = M_star * x
    result = {}
    for i, m in enumerate(monoms):
        if out_vec[i, 0] != 0:
            result[m] = out_vec[i, 0]
    return result


def main():
    for N in [4, 6, 8, 10]:
        print(f'\n\n===== Testing Psi filtration preservation, u-degree <= {N} =====')
        monoms, monom_idx, partitions, M_ord, M_star = build_psi_matrix(N)
        all_ok = True
        strict = []
        equal = []
        exceeds = []
        for m in monoms:
            f_dict = {m: Integer(1)}
            psi_f = compute_psi(f_dict, monoms, monom_idx, partitions, M_ord, M_star)
            if not psi_f:
                w_out = -1
            else:
                w_out = max(weight_112_tuple(k) for k in psi_f.keys())
            w_in = weight_112_tuple(m)
            diff = w_out - w_in
            if diff > 0:
                exceeds.append((m, w_in, w_out))
                all_ok = False
            elif diff == 0:
                equal.append((m, w_in, w_out))
            else:
                strict.append((m, w_in, w_out))
        print(f'  Total monomials: {len(monoms)}')
        print(f'  Weight preserved (out == in): {len(equal)}')
        print(f'  Weight decreased (out < in): {len(strict)}')
        print(f'  Weight increased (out > in) [VIOLATIONS]: {len(exceeds)}')
        if exceeds:
            print(f'  VIOLATIONS:')
            for m, w_in, w_out in exceeds[:20]:
                # Print Psi(m) too
                f_dict = {m: Integer(1)}
                psi_f = compute_psi(f_dict, monoms, monom_idx, partitions, M_ord, M_star)
                m_expr = e1**m[0] * e2**m[1] * e3**m[2]
                psi_expr = dict_to_poly(psi_f)
                print(f'    m = {m_expr} (w_in={w_in}): Psi(m) = {psi_expr} (w_out={w_out})')
        elif strict[:5]:
            print(f'  Sample strict decreases:')
            for m, w_in, w_out in strict[:5]:
                print(f'    m = {m}: w_in={w_in}, w_out={w_out}')
        print(f'  Overall: {"Psi PRESERVES FILTRATION!" if all_ok else "Psi INCREASES WEIGHT — need different structural viewpoint"}')


if __name__ == '__main__':
    main()
