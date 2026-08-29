"""Analyze the T-identity recursion at top weight.

We want:  Psi(e_2^{b+1}) = (E_2 - (2b+3) E_1) Psi(e_2^b) + M_b + N_b

where:
  M_b := [sum_i u_i · T(D_i(e_2^b V))] / V
  N_b := T(e_2(D)(e_2^b V)) / V

Both M_b and N_b are symmetric polys in u.
We want to understand their TOP-WEIGHT parts and how they relate to tops[b], tops[b-1], tops[b-2].

Approach:
  For b = 0..5, compute
    - Psi_b in E-basis
    - Contributions e_2 * Psi_b, M_b, N_b in E-basis
    - Their top-weight-(b+1) parts
    - Verify: e_2 * Psi_b - Sigma_{i} u_i T((D_j+D_k)(e_2^b V))/V + N_b = Psi_{b+1}
    - Look at each contribution's top-weight-(b+1) part
  Look for the polynomial-in-b pattern.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom, max_weight,
                                 list_top_weight_coeffs)
from sympy import expand, Poly, Integer, factor, simplify, symbols, Rational, diff, Symbol

D1 = lambda p: expand(u1 * diff(p, u1))
D2 = lambda p: expand(u2 * diff(p, u2))
D3 = lambda p: expand(u3 * diff(p, u3))

def e2_D(p):
    return expand(D1(D2(p)) + D1(D3(p)) + D2(D3(p)))

def divV_symmetric(x, description=""):
    x = expand(x)
    q, r = Poly(x, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise RuntimeError(f"Nonzero remainder dividing {description}: {r.as_expr()}")
    return q.as_expr()

def make_pieces(b):
    """Return the pieces of the T-identity applied to f = e_2^b V."""
    g = expand(e2_u**b * V)

    # Piece 1: e_2(u) * T(g)/V = e_2 * Psi(e_2^b) — symmetric, weight <= b+1 (with top = E_2 tops[b])
    Psi_b = divV_symmetric(T_u(g), f"T(e_2^{b} V)")
    piece_1 = expand(e2_u * Psi_b)

    # Piece 2 = M_b_style: [sum_i u_i T((D_j+D_k)(e_2^b V))] / V
    d23 = expand(D2(g) + D3(g))
    d13 = expand(D1(g) + D3(g))
    d12 = expand(D1(g) + D2(g))
    sum_mid = expand(u1 * T_u(d23) + u2 * T_u(d13) + u3 * T_u(d12))
    piece_2 = divV_symmetric(sum_mid, f"sum_i u_i T((D_j+D_k)(e_2^{b} V))")

    # Piece 3 = N_b: T(e_2(D) g) / V
    piece_3 = divV_symmetric(T_u(e2_D(g)), f"T(e_2(D)(e_2^{b} V))")

    total = expand(piece_1 - piece_2 + piece_3)
    Psi_bp1 = Psi_direct(e2_u**(b+1))
    diff_check = expand(total - Psi_bp1)
    assert diff_check == 0, f"Recursion mismatch at b={b}: diff = {diff_check}"

    return piece_1, piece_2, piece_3, Psi_b, Psi_bp1

def in_ebasis(p):
    return sym_to_ebasis_direct(p)

def print_by_weight(p_E, label, up_to_weight):
    p_E = expand(p_E)
    weights = {}
    poly = Poly(p_E, E1, E2, E3)
    for monom, coeff in poly.as_dict().items():
        i, j, k = monom
        w = weight_of_e_monom(i, j, k)
        weights.setdefault(w, []).append(((i, j, k), coeff))
    print(f"  {label}:")
    for w in sorted(weights.keys()):
        if w > up_to_weight:
            continue
        terms = weights[w]
        print(f"    weight {w}: {sum(c * E1**i * E2**j * E3**k for (i,j,k), c in terms)}")

def top_part(p_E, target):
    return top_weight_part(p_E, target)

def main():
    print("=" * 80)
    print("STEP 3 ANALYSIS: top-weight decomposition of T-identity pieces")
    print("=" * 80)

    for b in range(0, 5):
        print(f"\n{'='*70}\nb = {b}\n{'='*70}")
        piece_1, piece_2, piece_3, Psi_b, Psi_bp1 = make_pieces(b)

        Psi_b_E = in_ebasis(Psi_b)
        Psi_bp1_E = in_ebasis(Psi_bp1)
        piece_1_E = in_ebasis(piece_1)
        piece_2_E = in_ebasis(piece_2)
        piece_3_E = in_ebasis(piece_3)

        tops_b = top_part(Psi_b_E, b)
        tops_bp1 = top_part(Psi_bp1_E, b+1)
        print(f"  tops[{b}] = {tops_b}")
        print(f"  tops[{b+1}] = {tops_bp1}")

        p1_top = top_part(piece_1_E, b+1)
        p2_top = top_part(piece_2_E, b+1)
        p3_top = top_part(piece_3_E, b+1)
        print(f"\n  piece_1_top (from e_2 * Psi_b): {p1_top}")
        print(f"  piece_2_top (middle sum): {p2_top}")
        print(f"  piece_3_top (T(e_2(D) g)/V): {p3_top}")

        computed_top = expand(p1_top - p2_top + p3_top)
        assert computed_top == tops_bp1, f"top-weight combo doesn't match: {computed_top} vs {tops_bp1}"
        print(f"  CHECK: piece_1_top - piece_2_top + piece_3_top = tops[{b+1}]? YES")

        # print weight distribution of each piece
        print(f"\n  Weight distribution:")
        print_by_weight(piece_1_E, "piece_1 (e_2 Psi_b)", b + 1)
        print_by_weight(piece_2_E, "piece_2 (middle)", b + 1)
        print_by_weight(piece_3_E, "piece_3 (T(e_2(D)g)/V)", b + 1)

if __name__ == '__main__':
    main()
