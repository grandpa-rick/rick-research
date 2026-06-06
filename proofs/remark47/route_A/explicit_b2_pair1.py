"""
Explicit enumeration for B_2 dominant spin pair λ = (3/2, 1/2), μ = (1/2, 1/2):
- All (w, π) pairs (W-side).
- Apply Aug~ from Rick's aug_tilde_B2.py.
- Print pair structure for comparison to CKL pull-back.

This script reuses Rick's existing Aug~ machinery and produces
human-readable output.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47')

from fractions import Fraction
from collections import defaultdict
from aug_tilde_B2 import (
    weyl_B2,
    all_kostant_partitions_B2,
    bidegree_of_partition,
    apply_aug_tilde,
    s1_w,
    s2_w,
    length_of_label,
    RHO_B2,
    POS_ROOTS_B2,
)


def label_to_str(label):
    perm, signs = label
    return f"perm={perm}, signs={signs}"


def w_simple_decomp(label):
    """Identify the W-element by the standard generators s_1 (short, e_2)
    and s_0 (long, e_1 - e_2). Returns string."""
    # In B_2: s_0 = swap coords (perm flip), s_1 = sign-flip on coord 2.
    # W = (Z/2)^2 sx S_2, |W| = 8.
    perm, signs = label
    # Map (perm, signs) -> canonical name
    name_map = {
        ((0, 1), (1, 1)): "e",
        ((0, 1), (1, -1)): "s_1",  # short reflection on coord 2
        ((1, 0), (1, 1)): "s_0",   # swap (long simple, but "long" depends on convention)
        ((1, 0), (1, -1)): "s_0 s_1",
        ((1, 0), (-1, 1)): "s_1 s_0",
        ((1, 0), (-1, -1)): "s_1 s_0 s_1",
        ((0, 1), (-1, 1)): "s_0 s_1 s_0",
        ((0, 1), (-1, -1)): "w_0",
    }
    return name_map.get((perm, signs), "?")


def pi_to_str(pi):
    parts = []
    for r in [(1, -1), (1, 1), (1, 0), (0, 1)]:
        if r in pi:
            parts.append(f"{r}^{pi[r]}")
    return " + ".join(parts) if parts else "(empty)"


def main():
    F = Fraction
    half = F(1, 2)

    # Test pair: λ = (3/2, 1/2), μ = (1/2, 1/2)
    lam = (F(3, 2), F(1, 2))
    mu = (F(1, 2), F(1, 2))

    tilde_a = tuple(int(lam[i] + RHO_B2[i]) for i in range(2))
    b = tuple(int(mu[i] + RHO_B2[i]) for i in range(2))

    print(f"=== B_2 spin pair λ={lam}, μ={mu} ===")
    print(f"  tilde_a = {tilde_a}, b = {b}")
    print(f"  POS_ROOTS_B2: long = (1,-1), (1,1); short = (1,0), (0,1)")
    print()

    weyl = weyl_B2()
    print(f"All 8 elements of W(B_2):")
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        print(f"  {w_simple_decomp(label):10s} ({label_to_str(label):28s})  ℓ={length}  w·a-b = {beta_w}")
    print()

    # Enumerate (w, π) pairs
    items = []  # (label, length, pi, bidegree, name)
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        if beta_w[0] < 0:
            continue
        pis = all_kostant_partitions_B2(beta_w)
        for pi in pis:
            bd = bidegree_of_partition(pi)
            items.append((label, length, pi, bd, w_simple_decomp(label)))

    print(f"Total (w, π) pairs (with β_w in N^2): {len(items)}\n")
    for idx, (label, length, pi, bd, name) in enumerate(items):
        print(f"  [{idx}] w = {name}, ℓ={length}, π = {pi_to_str(pi)}, bidegree = {bd}")
    print()

    # Apply Aug~ to each
    print("=== Aug~ pairings (priority: s2_first, i.e. M_2 [long-long] first) ===\n")
    matched = {}
    fixed_points = []
    for idx, (label, length, pi, bd, name) in enumerate(items):
        result, move_name = apply_aug_tilde(label, pi, tilde_a, priority='s2_first')
        if result is None:
            fixed_points.append(idx)
        else:
            new_label, new_pi = result
            partner_idx = None
            for j, (lbl, lng, p, b_, _) in enumerate(items):
                if lbl == new_label and p == new_pi:
                    partner_idx = j
                    break
            matched[idx] = (partner_idx, move_name)

    seen = set()
    for idx, (partner, move) in matched.items():
        if partner in seen:
            continue
        seen.add(idx)
        seen.add(partner)
        a_label, a_len, a_pi, a_bd, a_name = items[idx]
        b_label, b_len, b_pi, b_bd, b_name = items[partner]
        print(f"  PAIR (move={move}):")
        print(f"    [{idx}] {a_name} (ℓ={a_len}), π = {pi_to_str(a_pi)}, bd = {a_bd}")
        print(f"    [{partner}] {b_name} (ℓ={b_len}), π = {pi_to_str(b_pi)}, bd = {b_bd}")
    print()

    print(f"Fixed points (these contribute to KL):")
    fp_bd = defaultdict(int)
    for idx in fixed_points:
        label, length, pi, bd, name = items[idx]
        print(f"  [{idx}] {name} (ℓ={length}), π = {pi_to_str(pi)}, bd = {bd}")
        fp_bd[bd] += 1
    print()

    print(f"KL polynomial (from fixed points):")
    poly_str = " + ".join(f"{c}*q^{i}*t^{j}" for (i, j), c in sorted(fp_bd.items()))
    print(f"  KL^B_2_{{(3/2,1/2),(1/2,1/2)}}(q,t) = {poly_str}")


if __name__ == "__main__":
    main()
