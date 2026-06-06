"""
Compute Mathas's involution ψ_C on each left cell of W(B_2).

Recipe (Prop B.4 of GY 2023):
  For each left cell C of W, the longest element w_I acts on V(C) (the KL cell module)
  by w_I · [C_x] = ±[C_{ψ_C(x)}], with ψ_C an involution and the sign constant on C.

In C[W] with KL basis {C_w}_w (at q=1):
  Since all P_{x,w}(q) = 1 in W(B_2), we have
    C_w = sum_{x ≤ w} x  ∈ Z[W]
  (group ring element). [Standard convention; W(B_2) has trivial KL polys.]

To compute ψ_C(x):
  1. Compute w_I · C_x = w_I * (sum_{y ≤ x} y) ∈ Z[W].
  2. Re-expand into KL basis: solve w_I · C_x = sum_z a_z C_z.
  3. Modulo C^< := span(C_y : y <_L C), the only KL elements that survive are those with y ∼_L x (i.e., y ∈ C). Among these, the highest-Bruhat one is ψ_C(x) (with sign).

Concretely the formula simplifies because cells have nice structure. Let's just compute.
"""

from fractions import Fraction
from itertools import permutations, product
from kl_W_B2 import (
    all_elements_B2, length, multiply, ID, S0, S1,
    bruhat_le, kl_polynomial_table, left_preorder_relations,
    compute_left_cells, reduced_word, transitive_closure
)


def name_elements(elts):
    out = {}
    for w in elts:
        rw = reduced_word(w)
        out[w] = "e" if not rw else "".join(f"s{i}" for i in rw)
    return out


# Group ring: sparse dict {w: coeff}.
def gr_zero():
    return {}

def gr_singleton(w, c=1):
    return {w: c} if c else {}

def gr_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}

def gr_sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v != 0}

def gr_left_mul(w, a):
    """Left multiply group ring element a by group element w."""
    return {multiply(w, x): c for x, c in a.items() if c}


def C_basis_element(w, elements):
    """Return C_w as group ring element: sum over x ≤_Bruhat w of x. (Valid because P_{x,w}=1 in W(B_2).)"""
    return {x: 1 for x in elements if bruhat_le(x, w)}


def expand_in_KL(gr_elt, elements):
    """Given group ring element a = sum c_w w, find {C_w → coeffs} such that
    a = sum b_w C_w. Since {C_w} is a basis of Z[W], this is unique.

    Method: triangular w.r.t. Bruhat. Iterate from longest to shortest.
    """
    out = {}
    a = dict(gr_elt)
    # Sort elements by descending length
    by_len = sorted(elements, key=lambda w: -length(w))
    for w in by_len:
        coeff = a.get(w, 0)
        if coeff == 0:
            continue
        # subtract coeff * C_w
        Cw = C_basis_element(w, elements)
        for x, c in Cw.items():
            a[x] = a.get(x, 0) - coeff * c
            if a[x] == 0:
                del a[x]
        out[w] = coeff
    if any(v != 0 for v in a.values()):
        raise RuntimeError(f"Failed to expand: leftover {a}")
    return out


def w_longest_B2(elements):
    """Return w_I = the longest element w_0 of W(B_2)."""
    return max(elements, key=length)


def compute_mathas_involution_B2():
    """Compute ψ_C on each left cell of W(B_2)."""
    elements = all_elements_B2()
    elements_sorted = sorted(elements, key=lambda w: (length(w), w))
    name = name_elements(elements_sorted)
    P = kl_polynomial_table(elements_sorted)
    cells = compute_left_cells(elements_sorted, P)
    wI = w_longest_B2(elements_sorted)

    print(f"w_I = {name[wI]} (= w_0 of W(B_2))")
    print(f"\nLeft cells:")
    for i, cell in enumerate(sorted(cells, key=lambda c: (-len(c), min(length(x) for x in c)))):
        cell_names = sorted([name[w] for w in cell])
        print(f"  Cell {i}: {cell_names}")

    # Determine ≤_L on cells (for computing C^<)
    one_step = left_preorder_relations(P, elements_sorted)
    le_relation = transitive_closure(one_step, elements_sorted)
    # x ≤_L y iff (x, y) in le_relation

    print("\n=== Computing ψ_C on each cell ===")
    psi_C = {}  # x -> ψ_C(x)
    sign_C = {}  # cell -> sign

    for cell_i, cell in enumerate(sorted(cells, key=lambda c: (-len(c), min(length(x) for x in c)))):
        cell_names = sorted([name[w] for w in cell])
        print(f"\nCell {cell_i}: {cell_names}")
        # C^< = elements y such that for all x in cell, y <_L x and y not in cell.
        # i.e., y ≤_L x but y not equiv to x.
        cell_set = set(cell)
        below_cell = set()
        for y in elements_sorted:
            if y in cell_set:
                continue
            # y is below cell iff y ≤_L (some / any) x in cell, but not in cell
            x = next(iter(cell))
            if (y, x) in le_relation:
                below_cell.add(y)
        below_names = sorted([name[y] for y in below_cell])
        # Actually: V(C) = C^≤ / C^<, where C^≤ = span{C_y : y ≤_L cell}, C^< = span{C_y : y <_L cell, not in cell}.
        # The "lower-order terms" are coefficients on C_y with y <_L x (i.e., y in below_cell).
        print(f"  Below cell (lower-order C_y): {below_names}")

        # Compute w_I · C_x for each x in cell, expand in KL basis, take projection onto cell.
        # Mathas: w_I · C_x = ε * C_{ψ_C(x)} + (terms in C^<).
        # So pick out the projection on the cell.

        for x in sorted(cell, key=lambda w: length(w)):
            # Compute w_I * C_x in group ring
            Cx = C_basis_element(x, elements_sorted)
            wI_Cx = gr_left_mul(wI, Cx)
            # Expand in KL basis
            kl_expansion = expand_in_KL(wI_Cx, elements_sorted)
            # Restrict to cell
            cell_part = {y: c for y, c in kl_expansion.items() if y in cell_set}
            # The result should be ±C_{ψ_C(x)}
            assert len(cell_part) == 1, f"Expected one cell element, got {[(name[y], c) for y, c in cell_part.items()]}"
            (yC, sign), = list(cell_part.items()) and [(list(cell_part.keys())[0], list(cell_part.values())[0])]
            yC = list(cell_part.keys())[0]
            sign = list(cell_part.values())[0]
            # Lower-order terms
            lot = {y: c for y, c in kl_expansion.items() if y not in cell_set}
            psi_C[x] = yC
            print(f"  w_I · C_{name[x]} = {sign:+d} C_{name[yC]}  (+ lot: {[(name[y], c) for y, c in lot.items()]})")
        # Verify involution and constant sign
        for x in cell:
            assert psi_C[psi_C[x]] == x, f"Not involution at {name[x]}!"
        # All signs same in cell — check
        signs_in_cell = set()
        for x in cell:
            Cx = C_basis_element(x, elements_sorted)
            wI_Cx = gr_left_mul(wI, Cx)
            kl_expansion = expand_in_KL(wI_Cx, elements_sorted)
            cell_part = {y: c for y, c in kl_expansion.items() if y in cell_set}
            signs_in_cell.add(list(cell_part.values())[0])
        assert len(signs_in_cell) == 1, f"Sign not constant on cell: {signs_in_cell}"
        sign_C[frozenset(cell)] = signs_in_cell.pop()

    print("\n=== Mathas involution ψ_C summary ===")
    for x in elements_sorted:
        print(f"  ψ_C({name[x]:<10s}) = {name[psi_C[x]]}")

    return elements_sorted, name, psi_C, sign_C, cells, le_relation


if __name__ == "__main__":
    compute_mathas_involution_B2()
