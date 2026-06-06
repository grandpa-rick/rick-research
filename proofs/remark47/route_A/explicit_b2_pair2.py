"""
Explicit enumeration for richer B_2 dominant spin pairs.
We pick:
  Pair 2: λ = (5/2, 3/2), μ = (1/2, 1/2)  [more (w,π) pairs, more bidegrees]
  Pair 3: λ = (5/2, 1/2), μ = (1/2, 1/2)  [intermediate]
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
    RHO_B2,
    POS_ROOTS_B2,
)


def w_simple_decomp(label):
    perm, signs = label
    name_map = {
        ((0, 1), (1, 1)): "e",
        ((0, 1), (1, -1)): "s_1",
        ((1, 0), (1, 1)): "s_0",
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


def analyze_pair(lam, mu, name=""):
    print(f"\n=== {name}  λ={lam}, μ={mu} ===")
    tilde_a = tuple(int(lam[i] + RHO_B2[i]) for i in range(2))
    b = tuple(int(mu[i] + RHO_B2[i]) for i in range(2))
    print(f"  tilde_a = {tilde_a}, b = {b}\n")

    weyl = weyl_B2()

    items = []
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        if beta_w[0] < 0:
            continue
        pis = all_kostant_partitions_B2(beta_w)
        for pi in pis:
            bd = bidegree_of_partition(pi)
            items.append((label, length, pi, bd, w_simple_decomp(label)))

    print(f"Total (w, π) pairs: {len(items)}")
    by_w = defaultdict(list)
    for idx, (lbl, lng, pi, bd, nm) in enumerate(items):
        by_w[(nm, lng)].append((idx, pi, bd))
    for (nm, lng), entries in sorted(by_w.items(), key=lambda x: x[0][1]):
        print(f"  w = {nm} (ℓ={lng}): {len(entries)} pairs")
        for (idx, pi, bd) in entries:
            print(f"    [{idx}] π = {pi_to_str(pi)}, bd = {bd}")

    # Aug~
    print(f"\n--- Aug~ pairings ---")
    matched = {}
    fixed_points = []
    for idx, (lbl, lng, pi, bd, nm) in enumerate(items):
        result, move_name = apply_aug_tilde(lbl, pi, tilde_a, priority='s2_first')
        if result is None:
            fixed_points.append(idx)
        else:
            new_lbl, new_pi = result
            partner_idx = None
            for j, (lbl2, _, p, _, _) in enumerate(items):
                if lbl2 == new_lbl and p == new_pi:
                    partner_idx = j
                    break
            matched[idx] = (partner_idx, move_name)

    seen = set()
    for idx, (partner, move) in matched.items():
        if idx in seen:
            continue
        seen.add(idx)
        if partner is not None:
            seen.add(partner)
            a = items[idx]
            b_item = items[partner]
            print(f"  PAIR (move={move}):  "
                  f"[{idx}] {a[4]}(ℓ={a[1]}) π={pi_to_str(a[2])} bd={a[3]}  <-->  "
                  f"[{partner}] {b_item[4]}(ℓ={b_item[1]}) π={pi_to_str(b_item[2])} bd={b_item[3]}")

    print(f"\nFixed points (= contribute to KL):")
    fp_bd = defaultdict(int)
    for idx in fixed_points:
        lbl, lng, pi, bd, nm = items[idx]
        print(f"  [{idx}] {nm}(ℓ={lng}), π = {pi_to_str(pi)}, bd = {bd}")
        fp_bd[bd] += 1

    poly_str = " + ".join(f"{c}*q^{i}*t^{j}" for (i, j), c in sorted(fp_bd.items()))
    print(f"\nKL = {poly_str}\n")
    return fp_bd


if __name__ == "__main__":
    F = Fraction
    half = F(1, 2)

    analyze_pair((F(5, 2), F(1, 2)), (F(1, 2), F(1, 2)), "Pair 2: λ=(5/2,1/2), μ=(1/2,1/2)")
    analyze_pair((F(5, 2), F(3, 2)), (F(1, 2), F(1, 2)), "Pair 3: λ=(5/2,3/2), μ=(1/2,1/2)")
    analyze_pair((F(3, 2), F(3, 2)), (F(3, 2), F(1, 2)), "Pair 4: λ=(3/2,3/2), μ=(3/2,1/2)")
