"""Day 124: Study Psi at the TOP-WEIGHT level.

Psi preserves weight exactly (empirical). This means Psi induces a linear
automorphism of the associated graded ring gr(Q[e_1, e_2, e_3]) w.r.t. (1,1,2)-weight.

Q: What is Psi at the top-weight level? Is it the IDENTITY?
   I.e., does top_w(Psi(m)) = top_w(m) = m (when m is a monomial of weight w)?

If yes, Psi = identity + lower-weight terms. This is a "unipotent" structure.
If yes, then Pi* = Psi ∘ (e_2 ·) ∘ Psi^{-1} at top weight equals just (e_2 ·)
at top weight. Which means top(Pi*(f)) = e_2 * top(f) modulo lower.

BUT: we saw top(Pi*(1)) = -e_1 + e_2, not just e_2. So this specific formula
doesn't hold. Let's check what's going on.

Actually: top(Pi*(1)) = weight-1 part of Pi*(1) = -e_1 + e_2 (weight 1 each).
This has weight 1, same as e_2. So Pi* raises weight by 1 exactly.
And top(Pi*(1)) is NOT just e_2 = the top of e_2.
It's -e_1 + e_2.

Hmm, this suggests that Psi is NOT the identity at top weight.

Let's compute Psi at top weight and see.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer

from psi_filtration_test import build_psi_matrix, compute_psi
from pi_star_on_monomials import weight_112_tuple, dict_to_poly

e1, e2, e3 = symbols('e1 e2 e3')


def top_weight_part(f_dict, w):
    """Return dict of monomials of weight exactly w."""
    return {m: c for m, c in f_dict.items() if weight_112_tuple(m) == w}


def main():
    N = 8
    monoms, monom_idx, partitions, M_ord, M_star = build_psi_matrix(N)

    print('=' * 80)
    print('For each e-monomial m of weight w, compute Psi(m) and its top-weight part:')
    print('=' * 80)
    for m in monoms:
        w = weight_112_tuple(m)
        f_dict = {m: Integer(1)}
        psi_f = compute_psi(f_dict, monoms, monom_idx, partitions, M_ord, M_star)
        top = top_weight_part(psi_f, w)
        m_expr = e1**m[0] * e2**m[1] * e3**m[2]
        top_expr = dict_to_poly(top)
        # Compare with m itself
        diff_from_m = expand(top_expr - m_expr)
        print(f'  m = {m_expr} (w={w}): top_w(Psi(m)) = {top_expr}   diff from m: {diff_from_m}')


if __name__ == '__main__':
    main()
