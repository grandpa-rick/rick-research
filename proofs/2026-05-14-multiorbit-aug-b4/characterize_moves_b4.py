"""
Characterize the 28 e_4^2 net moves on S_4 at B_4 into structural classes:
  - intra-chain: both e_4-primitives from the same chain (A, B, or C)
  - cross-chain: primitives from two different chains
  - singleton-involving: at least one primitive is the alpha_4 singleton (E_4)

Prediction (three-strand braid): 9 intra + 12 cross + 7 singleton = 28.

For B_4, the alpha_4-string structure on Phi^+ has three length-3 chains:
  Chain A: bot=EM14, mid=E1,  top=EP14
  Chain B: bot=EM24, mid=E2,  top=EP24
  Chain C: bot=EM34, mid=E3,  top=EP34
plus the alpha_4 singleton E_4 itself.

Each chain has 2 "e_4-primitives":
  T -> M: delta = -1*top + 1*mid
  M -> B: delta = -1*mid + 1*bot
Combining two firings (with possible repetition) gives the 3 intra-chain moves
per chain (TT, TB, MM) -- noting that one "T->M" and one "M->B" gives the
"T->B" net move -1*top + 1*bot. Then 4 cross-chain pairings between any two
distinct chains, and 7 singleton-involving combinations.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from collections import Counter, defaultdict
import b_i_b4 as B4
from b_i_b4 import (
    enumerate_partitions, eps_i, e_i_k, kp_repr,
    EM12, EM13, EM14, EM23, EM24, EM34,
    EP12, EP13, EP14, EP23, EP24, EP34,
    E1, E2, E3, E4, ROOTS,
)


# Chains at alpha_4
CHAINS = {
    'A': {'bot': EM14, 'mid': E1, 'top': EP14},
    'B': {'bot': EM24, 'mid': E2, 'top': EP24},
    'C': {'bot': EM34, 'mid': E3, 'top': EP34},
}


def _delta_to_canon(d_dict):
    """Convert dict of root->delta into canonical sorted tuple form (root, delta)."""
    return tuple(sorted((r, c) for r, c in d_dict.items() if c != 0))


def _add(d, root, val):
    d[root] = d.get(root, 0) + val


# Build the 28 predicted net moves with their structural labels.
# Each is (label, class, delta_tuple).

PREDICTED_MOVES = []


def primitive_delta(chain_name, kind):
    """Return delta dict for one application of an e_4-primitive on `chain_name` (A,B,C)
    of type `kind` ('TM' for top->mid, 'MB' for mid->bot)."""
    c = CHAINS[chain_name]
    d = {}
    if kind == 'TM':
        _add(d, c['top'], -1)
        _add(d, c['mid'], +1)
    elif kind == 'MB':
        _add(d, c['mid'], -1)
        _add(d, c['bot'], +1)
    else:
        raise ValueError(kind)
    return d


def singleton_delta():
    return {E4: -1}


# Intra-chain: 9 moves
for cname in ['A', 'B', 'C']:
    # TM + TM (twice "top to mid")
    d = {}
    for r, v in primitive_delta(cname, 'TM').items(): _add(d, r, v)
    for r, v in primitive_delta(cname, 'TM').items(): _add(d, r, v)
    PREDICTED_MOVES.append((f'intra-{cname}: T-T (T->M twice)', 'intra', _delta_to_canon(d)))

    # MB + MB
    d = {}
    for r, v in primitive_delta(cname, 'MB').items(): _add(d, r, v)
    for r, v in primitive_delta(cname, 'MB').items(): _add(d, r, v)
    PREDICTED_MOVES.append((f'intra-{cname}: B-B (M->B twice)', 'intra', _delta_to_canon(d)))

    # TM + MB (one of each: net is top -> bot)
    d = {}
    for r, v in primitive_delta(cname, 'TM').items(): _add(d, r, v)
    for r, v in primitive_delta(cname, 'MB').items(): _add(d, r, v)
    PREDICTED_MOVES.append((f'intra-{cname}: T-B (T->M then M->B)', 'intra', _delta_to_canon(d)))

# Cross-chain: 12 moves (3 pairs * 4 combinations)
for (cn1, cn2) in [('A', 'B'), ('A', 'C'), ('B', 'C')]:
    for k1 in ['TM', 'MB']:
        for k2 in ['TM', 'MB']:
            d = {}
            for r, v in primitive_delta(cn1, k1).items(): _add(d, r, v)
            for r, v in primitive_delta(cn2, k2).items(): _add(d, r, v)
            PREDICTED_MOVES.append((f'cross-{cn1}{cn2}: {k1}+{k2}', 'cross', _delta_to_canon(d)))

# Singleton-involving: 7 moves
# E4 with itself
d = dict(singleton_delta())
for r, v in singleton_delta().items(): _add(d, r, v)  # add second one
# Actually simpler:
d = {E4: -2}
PREDICTED_MOVES.append(('singleton: E4-E4 (self-pair)', 'singleton', _delta_to_canon(d)))

# E4 with each of 6 chain primitives
for cname in ['A', 'B', 'C']:
    for kind in ['TM', 'MB']:
        d = {}
        for r, v in singleton_delta().items(): _add(d, r, v)
        for r, v in primitive_delta(cname, kind).items(): _add(d, r, v)
        PREDICTED_MOVES.append((f'singleton: E4-{cname}_{kind}', 'singleton', _delta_to_canon(d)))


def diff_b4(pi_new, pi_old):
    d = {}
    for r in B4.ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


def main():
    MAX = 5
    print(f"Characterizing e_4^2 net moves on S_4 at B_4 (max_total={MAX})")
    print(f"Slice S_4 = {{pi : eps_4(pi) >= 2}}\n")

    # Predicted: build delta -> (label, class)
    predicted_lookup = {}
    pred_class_count = Counter()
    for (label, cls, delta) in PREDICTED_MOVES:
        if delta in predicted_lookup:
            print(f"!!! COLLISION: predicted move {delta} appears twice:")
            print(f"    existing: {predicted_lookup[delta]}")
            print(f"    new:      {(label, cls)}")
        predicted_lookup[delta] = (label, cls)
        pred_class_count[cls] += 1

    print(f"Built {len(PREDICTED_MOVES)} predicted moves.")
    print(f"  Predicted class counts: intra={pred_class_count['intra']}, "
          f"cross={pred_class_count['cross']}, singleton={pred_class_count['singleton']}\n")

    # Enumerate observed moves
    seen = Counter()
    for pi in enumerate_partitions(MAX):
        if eps_i(pi, 4) < 2:
            continue
        e2 = e_i_k(pi, 4, 2)
        if e2 is None:
            continue
        d = diff_b4(e2, pi)
        seen[d] += 1
    print(f"Observed {len(seen)} distinct e_4^2 net moves.\n")

    # Match each observed against predicted
    observed_class = Counter()
    unmatched_observed = []
    matched = set()
    for d, n in seen.items():
        if d in predicted_lookup:
            label, cls = predicted_lookup[d]
            observed_class[cls] += 1
            matched.add(d)
        else:
            unmatched_observed.append((d, n))

    # Unobserved predictions
    unobserved_predicted = []
    for (label, cls, delta) in PREDICTED_MOVES:
        if delta not in seen:
            unobserved_predicted.append((label, cls, delta))

    print(f"Observed class counts (from {len(matched)} matched moves):")
    print(f"  intra:      {observed_class['intra']}  (predicted 9)")
    print(f"  cross:      {observed_class['cross']}  (predicted 12)")
    print(f"  singleton:  {observed_class['singleton']}  (predicted 7)")
    print(f"  total:      {sum(observed_class.values())}  (predicted 28)\n")

    if unmatched_observed:
        print(f"!! {len(unmatched_observed)} observed moves were NOT in predicted catalog:")
        for d, n in unmatched_observed:
            ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
            print(f"    [{ds}]  ({n} cases)")
    else:
        print("All observed moves matched a predicted entry.")

    if unobserved_predicted:
        print(f"\n!! {len(unobserved_predicted)} predicted moves were NOT observed:")
        for label, cls, d in unobserved_predicted:
            ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
            print(f"    [{label} | {cls}]  [{ds}]")
    else:
        print("\nAll predicted moves were observed.\n")

    # Print all 28 observed (= predicted) entries with their labels.
    print("=" * 70)
    print("Full catalog (each predicted move with empirical occurrence count):")
    print("=" * 70)
    by_class = defaultdict(list)
    for (label, cls, delta) in PREDICTED_MOVES:
        n = seen.get(delta, 0)
        by_class[cls].append((label, delta, n))
    for cls in ['intra', 'cross', 'singleton']:
        print(f"\n  Class: {cls}  ({len(by_class[cls])} moves)")
        for label, delta, n in by_class[cls]:
            ds = ', '.join(f"{c:+d}*{r}" for r, c in delta)
            print(f"    {label:40s} [{ds}]  ({n} cases)")

    print()
    print("=" * 70)
    verdict = (observed_class['intra'] == 9 and
               observed_class['cross'] == 12 and
               observed_class['singleton'] == 7 and
               len(unmatched_observed) == 0 and
               len(unobserved_predicted) == 0)
    if verdict:
        print("VERDICT: three-strand braid hypothesis CONFIRMED at B_4.")
    else:
        print("VERDICT: three-strand braid hypothesis FALSIFIED at B_4.")
    print("=" * 70)


if __name__ == "__main__":
    main()
