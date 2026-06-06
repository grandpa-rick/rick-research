"""
Compare Rick's Aug~ involution on (w, π) pairs with GY's ψ_J on W elements,
projected to the w-component.

Plan:
  1. For each dominant spin pair (λ, μ) in B_2, enumerate all (w, π) pairs.
  2. Apply Aug~ to each, extract Aug~'s action on the w-component (i.e., just look
     at how w changes — could be: w → w (fixed point), w → s_0 w (M_1 move),
     or w → s_1 w (M_2 move)).
  3. Compare:
     (a) Does Aug~'s w-projection match ψ_J for some specific J (depending on (λ, μ))?
     (b) Tabulate the discrepancies.

Note: Aug~'s action on w is EITHER w → w (fixed point), w → s_0 w, or w → s_1 w.
ψ_J's action on w is more general (it permutes via the cell-involution in W_J).

A single Aug~ flip is a single simple-reflection multiplication; ψ_J for J = full I
in B_2 acts by potentially-longer permutations (e.g., s_1 → s_1 s_0 s_1 = s_1 · (s_0 s_1)).
So Aug~ at the w-level is at most a generator action; ψ_J full is a composition.

Therefore the natural comparison is whether (i) for some J, ψ_J's action on w PROJECTS
to Aug~'s action on (w, π) when we forget π.

Since ψ_J is a single involution (not parametrized by π), but Aug~'s action on w varies
by π (M_1 might apply for some π, M_2 for others), we should expect the comparison to
be about whether Aug~ partitions the w-orbit consistent with one of the ψ_J's.
"""

import sys
import os
sys.path.insert(0, '/home/agent/projects/proofs/remark47')
sys.path.insert(0, '/home/agent/projects/proofs/remark47/route_B')

from fractions import Fraction
from collections import defaultdict
from aug_tilde_B2 import (
    weyl_B2, w_label_to_func, s2_w, s1_w, length_of_label,
    all_kostant_partitions_B2, bidegree_of_partition,
    apply_aug_tilde, RHO_B2,
)
from kl_W_B2 import (
    all_elements_B2, length, multiply, ID, S0, S1, reduced_word
)
from psi_J_B2 import compute_psi_J


# Translate Rick's W(B_2) labels to GY's signed-permutation tuples.
# Rick: label = (perm, signs) where w(v) = (signs[i] * v[perm[i]] for i in 0,1).
# GY (in kl_W_B2.py): w = (pi, signs) same convention.
# Identical convention. Good.

# Rick's s_0 (in aug_tilde_B2.py) is "s_2" in his code (the long-long swap pairing,
# associated with simple short root α_1 = e_1, sign-flip). Wait, let me re-read.
#
# In aug_tilde_B2.py:
#   s2_w: (s_2 w)(v) = s_2(w(v)) where s_2 sends (v_0, v_1) → (v_0, -v_1) — sign flip on coord 1.
#       This is the SHORT simple reflection. In Rick's notes (proof md), this is "M_2 = short simple".
#   s1_w: (s_1 w)(v) = s_1(w(v)) where s_1 swaps coords 0 and 1.
#       This is the LONG simple reflection.
#
# In GY/our route_B convention:
#   S0 = swap = LONG simple s_0
#   S1 = sign-flip on coord 1 = SHORT simple s_1
#
# So Rick's "s_2" = GY's S1 = our s_1 (short).
# Rick's "s_1" = GY's S0 = our s_0 (long).
#
# Rick's M_2 = short-simple move = corresponds to multiplication by GY's s_1.
# Rick's M_1 = long-simple move = corresponds to multiplication by GY's s_0.

# So when Aug~ reports move "s2" (M_2), w → s_short · w = s_1 · w (in GY notation).
# When Aug~ reports move "s1" (M_1), w → s_long · w = s_0 · w (in GY notation).


def name_w(label):
    """Convert label to readable name using GY's reduced word."""
    rw = reduced_word(label)
    return "e" if not rw else "".join(f"s{i}" for i in rw)


def aug_tilde_action_on_w(lam, mu, priority='s2_first'):
    """For a given dominant spin pair, compute Aug~'s w-projected action.

    Returns:
      action_by_w: dict mapping w_label -> dict mapping π_tuple -> (target_w_label, move_name)
                   where move_name in {None (fixed), 's1' (M_1=long), 's2' (M_2=short)}.

    Also returns the list of items.
    """
    F = Fraction
    half = F(1, 2)
    tilde_a = tuple(int(lam[i] + RHO_B2[i]) for i in range(2))
    b = tuple(int(mu[i] + RHO_B2[i]) for i in range(2))

    weyl = weyl_B2()
    items = []
    for w_func, length_, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        if beta_w[0] < 0:
            continue
        pis = all_kostant_partitions_B2(beta_w)
        for pi in pis:
            bd = bidegree_of_partition(pi)
            items.append((label, length_, pi, bd))

    action = defaultdict(dict)
    for (label, length_, pi, bd) in items:
        result, move_name = apply_aug_tilde(label, pi, tilde_a, priority=priority)
        pi_tup = frozenset(pi.items())
        if result is None:
            action[label][pi_tup] = (label, None, bd)
        else:
            new_label, new_pi = result
            action[label][pi_tup] = (new_label, move_name, bd)
    return action, items


def compare_aug_to_psi_J(lam, mu, priority='s2_first', verbose=True):
    """Compare Aug~'s w-projection to each ψ_J for J ⊆ {0, 1}."""
    action, items = aug_tilde_action_on_w(lam, mu, priority)

    # ψ_J for each J
    psi_maps = {}
    for J in [(), (0,), (1,), (0, 1)]:
        psi_maps[J], _ = compute_psi_J(J)

    if verbose:
        print(f"\n=== B_2 spin pair: λ={lam}, μ={mu} ===")
        F = Fraction
        tilde_a = tuple(int(lam[i] + RHO_B2[i]) for i in range(2))
        b = tuple(int(mu[i] + RHO_B2[i]) for i in range(2))
        print(f"  tilde_a = {tilde_a}, b = {b}")
        print(f"  Total items: {len(items)}")

        # Show Aug~ orbits at the w-level
        print(f"\n  Aug~ action on (w, π) projected to w:")
        for w_label, sub in action.items():
            for pi_tup, (target, move, bd) in sub.items():
                pi_str = "{" + ", ".join(f"{r}:{c}" for r, c in sorted(pi_tup)) + "}"
                if move is None:
                    print(f"    w={name_w(w_label):<10s}, π={pi_str:<40s}, bd={bd}: FIXED")
                else:
                    print(f"    w={name_w(w_label):<10s}, π={pi_str:<40s}, bd={bd}: → w'={name_w(target):<10s} via {move}")

    # For each J, check if Aug~'s w-action matches ψ_J at the w-level
    # i.e., for each (w, π), check if Aug~(w, π)'s w-component = ψ_J(w).
    print(f"\n  Comparison: Aug~ w-action vs ψ_J for each J")
    print(f"  {'J':<10s} {'matches/total':<15s} {'Aug~ fixes / ψ_J fixes':<30s}")
    for J in [(), (0,), (1,), (0, 1)]:
        psi_J = psi_maps[J]
        match_count = 0
        total = 0
        psi_fix_w_set = set(w for w in psi_J if psi_J[w] == w)
        aug_fix_w_set_at_some_pi = set()  # w that has at least one π for which Aug~ fixes (w, π)
        aug_total_w = set()  # all w appearing in items
        for w_label, sub in action.items():
            aug_total_w.add(w_label)
            for pi_tup, (target, move, bd) in sub.items():
                total += 1
                if target == psi_J[w_label]:
                    match_count += 1
                if move is None:
                    aug_fix_w_set_at_some_pi.add(w_label)
        print(f"  {str(J):<10s} {f'{match_count}/{total}':<15s} aug_fix={[name_w(w) for w in aug_fix_w_set_at_some_pi]}, ψ_J_fix={[name_w(w) for w in psi_fix_w_set if w in aug_total_w]}")

    return action, items, psi_maps


def main():
    F = Fraction
    half = F(1, 2)

    # Test on a few specific pairs
    test_pairs = [
        ((half, half), (half, half)),
        ((F(3,2), half), (half, half)),
        ((F(3,2), F(3,2)), (half, half)),
        ((F(3,2), F(3,2)), (F(3,2), half)),
        ((F(5,2), F(3,2)), (half, half)),
        ((F(5,2), F(3,2)), (F(3,2), half)),
        ((F(5,2), F(3,2)), (F(3,2), F(3,2))),
    ]

    for lam, mu in test_pairs:
        compare_aug_to_psi_J(lam, mu, verbose=True)


if __name__ == "__main__":
    main()
