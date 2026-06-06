"""
Full systematic comparison: Aug~ vs ψ_J on W(B_2).

For each dominant spin pair (λ, μ) with λ_1 ≤ 9/2, enumerate all (w, π) pairs.
Compute Aug~'s action and tabulate:
  - Aug~ orbits at the w-level (i.e., for each w, what is the multiset of (π → π', w'))
  - Whether the w-level action is consistent with ψ_J for some J

Key observation: Aug~ on (w, π) is parametrized — different π's at the same w may
go to DIFFERENT w''s (or fixed). ψ_J(w) is a SINGLE value not depending on π.

So Aug~ at the w-level is at best a partial match to ψ_J.

Three measures:
  1. EXACT MATCH: For all (w, π), Aug~_w(w, π) = ψ_J(w). [Strong]
  2. ORBIT MATCH: For each w, Aug~ sends some (w, π) to ψ_J(w) [exists witness].
  3. FIXED-POINT MATCH: w fixed by ψ_J iff (w, π) fixed by Aug~ for some π. [Weak]
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47')
sys.path.insert(0, '/home/agent/projects/proofs/remark47/route_B')

from fractions import Fraction
from collections import defaultdict
from aug_tilde_B2 import (
    weyl_B2, w_label_to_func, s2_w, s1_w,
    all_kostant_partitions_B2, bidegree_of_partition,
    apply_aug_tilde, RHO_B2,
)
from kl_W_B2 import (
    all_elements_B2, length, multiply, ID, S0, S1, reduced_word
)
from psi_J_B2 import compute_psi_J


def name_w(label):
    rw = reduced_word(label)
    return "e" if not rw else "".join(f"s{i}" for i in rw)


def aug_tilde_action_data(lam, mu, priority='s2_first'):
    """For one spin pair, return list of (w_label, pi, bd, target_w, move_name)."""
    tilde_a = tuple(int(lam[i] + RHO_B2[i]) for i in range(2))
    b = tuple(int(mu[i] + RHO_B2[i]) for i in range(2))
    weyl = weyl_B2()
    out = []
    for w_func, length_, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        if beta_w[0] < 0:
            continue
        pis = all_kostant_partitions_B2(beta_w)
        for pi in pis:
            bd = bidegree_of_partition(pi)
            result, move_name = apply_aug_tilde(label, pi, tilde_a, priority=priority)
            if result is None:
                target_label = label
            else:
                target_label, _ = result
            out.append((label, pi, bd, target_label, move_name))
    return out


def main():
    F = Fraction
    half = F(1, 2)

    # Enumerate dominant spin pairs
    test_pairs = []
    for l1 in range(5):
        for l2 in range(l1 + 1):
            lam = (l1 + half, l2 + half)
            for m1 in range(l1 + 1):
                for m2 in range(m1 + 1):
                    mu = (m1 + half, m2 + half)
                    test_pairs.append((lam, mu))
    print(f"Total dominant spin pairs (λ_1 ≤ 9/2): {len(test_pairs)}")

    # Precompute psi_J for all J
    psi_maps = {}
    for J in [(), (0,), (1,), (0, 1)]:
        psi_maps[J], _ = compute_psi_J(J)

    # Aggregate stats
    stats = {J: {'pair_match': 0, 'pair_total': 0, 'item_match': 0, 'item_total': 0}
             for J in psi_maps}

    detailed_examples = []  # (lam, mu, action_data)

    for lam, mu in test_pairs:
        data = aug_tilde_action_data(lam, mu)
        # Per-item match
        for J in psi_maps:
            psi_J = psi_maps[J]
            all_match = True
            for (w, pi, bd, target, move) in data:
                stats[J]['item_total'] += 1
                if target == psi_J[w]:
                    stats[J]['item_match'] += 1
                else:
                    all_match = False
            stats[J]['pair_total'] += 1
            if all_match:
                stats[J]['pair_match'] += 1
        if any(action[3] != psi_maps[(0,1)][action[0]] for action in data):
            detailed_examples.append((lam, mu, data))

    print("\n=== Per-J statistics over all dominant spin pairs ===")
    print(f"  {'J':<10s} {'item-level match':<25s} {'pair-level match':<20s}")
    for J in psi_maps:
        s = stats[J]
        print(f"  {str(J):<10s} {s['item_match']}/{s['item_total']:<10d}  ({100*s['item_match']/s['item_total']:.1f}%)   "
              f"{s['pair_match']}/{s['pair_total']} ({100*s['pair_match']/s['pair_total']:.1f}%)")

    # Show a few detailed mismatches for J = (0, 1) which is most interesting
    print(f"\n=== Examples where Aug~'s w-action ≠ ψ_I (J=full) ===")
    for lam, mu, data in detailed_examples[:8]:
        psi_I = psi_maps[(0, 1)]
        print(f"\n  λ={lam}, μ={mu}: items={len(data)}")
        for (w, pi, bd, target, move) in data:
            psi_target = psi_I[w]
            mark = "✓" if target == psi_target else "✗"
            pi_str = "{" + ",".join(f"{r}:{c}" for r, c in sorted(pi.items())) + "}"
            print(f"    {mark} w={name_w(w):<10s} π={pi_str:<35s} bd={bd}: Aug~→{name_w(target):<10s} (move={move}); ψ_I(w)={name_w(psi_target)}")

    # Now ask: does Aug~'s w-action match ψ_J(w) for J depending on (λ, μ)?
    print(f"\n=== Per-pair, can we find J such that Aug~ matches ψ_J? ===")
    pair_J_matches = defaultdict(list)
    for lam, mu in test_pairs:
        data = aug_tilde_action_data(lam, mu)
        for J in psi_maps:
            psi_J = psi_maps[J]
            if all(target == psi_J[w] for (w, pi, bd, target, move) in data):
                pair_J_matches[J].append((lam, mu))

    for J in psi_maps:
        print(f"  J = {J}: {len(pair_J_matches[J])}/{len(test_pairs)} pairs match")

    # Identify pairs that don't match ANY J
    no_match = []
    for lam, mu in test_pairs:
        data = aug_tilde_action_data(lam, mu)
        any_match = False
        for J in psi_maps:
            psi_J = psi_maps[J]
            if all(target == psi_J[w] for (w, pi, bd, target, move) in data):
                any_match = True
                break
        if not any_match:
            no_match.append((lam, mu, data))
    print(f"\n  Pairs matching NO J: {len(no_match)}/{len(test_pairs)}")

    # Show a few of these "no-J-match" pairs
    print(f"\n=== Examples of (λ, μ) where Aug~ matches NONE of ψ_J ===")
    for lam, mu, data in no_match[:5]:
        print(f"\n  λ={lam}, μ={mu}: items={len(data)}")
        for (w, pi, bd, target, move) in data:
            pi_str = "{" + ",".join(f"{r}:{c}" for r, c in sorted(pi.items())) + "}"
            psi_strs = ", ".join(f"ψ_{J}={name_w(psi_maps[J][w])}" for J in psi_maps)
            print(f"    w={name_w(w):<10s} π={pi_str:<35s}: Aug~→{name_w(target):<10s} ({move}); {psi_strs}")


if __name__ == "__main__":
    main()
