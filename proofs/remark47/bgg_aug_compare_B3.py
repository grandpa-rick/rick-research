"""
BGG vs. Aug~ comparison for B_3 with dominant spin lambda.

Adapts bgg_aug_compare_B2.py to B_3 = sp(6).

Strategy: in B_3 each simple reflection has MULTIPLE swap-orbits on positive
roots, so an Aug~ move can use a single subtype (PURE) or a mixture (MIXED).
We test:

  (A) For every Aug~ pair (w, π) <-> (w', π'): w' = s_i * w.
      [Automatic from construction of moves; we verify anyway.]
  (B) The π-difference π' - π is a "swap" within ONE s_i-orbit on positive
      roots (PURE move), OR a sum of swaps across multiple s_i-orbits all
      sharing the same simple reflection s_i (MIXED move within one s_i).
      Test: maximize the matching using PURE moves only; report % matched
      purely. Augment unmatched odds via mixed moves; report MIXED stats.

Output stats:
  - % of odd items matched by PURE moves.
  - For PURE pairs: (donor -> receiver) histogram per s_i.
  - For MIXED pairs: subtype-distribution histogram per s_i.
  - All pairs satisfy (A) by construction; verified in code.
"""

import os
import sys
import time
from fractions import Fraction
from collections import defaultdict, Counter
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aug_tilde_B3_richer as B3

N = 3


def list_pure_moves(label, pi, w_tilde_a, N):
    """Return list of (move_info, (new_label, new_pi)) for ALL valid PURE moves.

    A PURE move uses a SINGLE subtype to perform all |c_i| swaps via the donor
    of that one subtype.
    """
    out = []
    for kind, i in [('L', j) for j in range(N - 1)] + [('S', N - 1)]:
        if kind == 'L':
            c = w_tilde_a[i] - w_tilde_a[i + 1]
        else:
            c = w_tilde_a[N - 1]
        if c == 0:
            continue
        n_total = abs(c)
        for st in B3.subtypes_for_simple(kind, i, N):
            donor, receiver = B3.subtype_donor_receiver(kind, i, st, c, N)
            if pi.get(donor, 0) >= n_total:
                # Apply
                new_pi = dict(pi)
                new_pi[donor] -= n_total
                if new_pi[donor] == 0:
                    del new_pi[donor]
                new_pi[receiver] = new_pi.get(receiver, 0) + n_total
                if kind == 'L':
                    new_label = B3.s_long_w(label, i, N)
                else:
                    new_label = B3.s_short_w(label, N)
                # The move's "distribution" is {st: n_total}
                out.append(((kind, i, {st: n_total}), (new_label, new_pi)))
    return out


def list_all_mixed_moves(label, pi, w_tilde_a, N):
    """Return ALL valid mixed moves (including pure ones as special cases).
    Each move is a single simple reflection, possibly with mixed subtypes.
    """
    return B3.list_all_simple_moves(label, pi, w_tilde_a, N)


def freeze_pi(pi):
    return frozenset(pi.items())


def build_basis_and_edges(lam, mu, N, pure_only=False):
    """Return (items, item_index, odd_idxs, edges_per_odd) for (lam, mu).

    items: list of (label, length, pi, bidegree).
    item_index: dict (label, frozenset(pi)) -> idx.
    odd_idxs: list of indices of odd-length items.
    edges_per_odd: dict odd_idx -> list of (move_info, even_idx) bidegree-preserving.
    """
    tilde_a, b, items = B3.collect_items(lam, mu, N)
    if items is None:
        return None
    item_index = {(lbl, freeze_pi(pi)): idx for idx, (lbl, _, pi, _) in enumerate(items)}
    odd_idxs = [idx for idx, (_, lng, _, _) in enumerate(items) if lng % 2 == 1]

    edges = {}
    for idx in odd_idxs:
        label, length, pi, bd = items[idx]
        w_func = B3.w_label_to_func(label, N)
        w_tilde_a = w_func(tilde_a)
        if pure_only:
            moves = list_pure_moves(label, pi, w_tilde_a, N)
        else:
            moves = list_all_mixed_moves(label, pi, w_tilde_a, N)
        ed = []
        for move_info, (new_lbl, new_pi) in moves:
            key = (new_lbl, freeze_pi(new_pi))
            tgt = item_index.get(key)
            if tgt is None:
                continue
            if items[tgt][1] % 2 != 0:
                continue
            if items[tgt][3] != bd:
                continue
            ed.append((move_info, tgt))
        edges[idx] = ed
    return items, item_index, odd_idxs, edges, tilde_a


def maximum_bipartite_matching(odd_idxs, edges):
    """Hopcroft-Karp simplified.

    edges: dict odd_idx -> list of (move_info, even_idx).
    Returns:
       pair_odd: dict odd -> (even, move_info)
       pair_even: dict even -> odd
    """
    pair_odd = {}
    pair_even = {}

    def try_aug(o, visited):
        for move_info, ev in edges.get(o, []):
            if ev in visited:
                continue
            visited.add(ev)
            if ev not in pair_even or try_aug(pair_even[ev], visited):
                pair_odd[o] = (ev, move_info)
                pair_even[ev] = o
                return True
        return False

    for o in odd_idxs:
        try_aug(o, set())
    return pair_odd, pair_even


def match_pure_then_mixed(lam, mu, N):
    """Match odd items: first using pure moves, then augment with mixed.

    Returns:
       items, pair_odd_pure, pair_odd_all, unmatched
       pair_odd_pure: matched via pure moves only.
       pair_odd_all: full matching (pure + mixed augmentation).
       unmatched: odd indices not matched even with mixed (should be 0 if oracle holds).
    """
    res = build_basis_and_edges(lam, mu, N, pure_only=True)
    if res is None:
        return None
    items, item_index, odd_idxs, pure_edges, tilde_a = res

    # Phase 1: max matching with PURE edges only
    pair_odd_pure, pair_even_pure = maximum_bipartite_matching(odd_idxs, pure_edges)

    # Phase 2: augment with mixed edges (for unmatched odds)
    # Rebuild edges with mixed allowed
    res_all = build_basis_and_edges(lam, mu, N, pure_only=False)
    items_all, item_index_all, odd_idxs_all, all_edges, _ = res_all
    # Sanity: same item list
    assert len(items_all) == len(items)

    # Run a SECOND matching on top of pair_odd_pure: try to extend by augmenting through mixed edges.
    pair_odd = dict(pair_odd_pure)  # odd -> (even, move_info)
    pair_even = dict(pair_even_pure)  # even -> odd

    def try_aug_mixed(o, visited):
        for move_info, ev in all_edges.get(o, []):
            if ev in visited:
                continue
            visited.add(ev)
            if ev not in pair_even:
                pair_odd[o] = (ev, move_info)
                pair_even[ev] = o
                return True
            else:
                # Try to re-route the current occupant
                occupant = pair_even[ev]
                if try_aug_mixed(occupant, visited):
                    pair_odd[o] = (ev, move_info)
                    pair_even[ev] = o
                    return True
        return False

    for o in odd_idxs:
        if o not in pair_odd:
            try_aug_mixed(o, set())

    unmatched = [o for o in odd_idxs if o not in pair_odd]
    return items, pair_odd_pure, pair_odd, unmatched, tilde_a


def classify_move(move_info, items, o_idx, e_idx, N):
    """Classify a matched pair's move.

    Returns dict with:
       kind: 'L' or 'S'
       i: simple-reflection index
       n_subtypes: number of distinct subtypes used
       distribution: dict subtype -> count
       label_check: w_e == s_i * w_o (LEFT mult)?
       pi_diff: dict root -> (new_count - old_count)
    """
    kind, i, distribution = move_info
    lbl_o, _, pi_o, _ = items[o_idx]
    lbl_e, _, pi_e, _ = items[e_idx]
    # Check (A)
    if kind == 'L':
        expected = B3.s_long_w(lbl_o, i, N)
    else:
        expected = B3.s_short_w(lbl_o, N)
    label_check = (expected == lbl_e)
    # Compute pi-diff
    all_roots = set(pi_o.keys()) | set(pi_e.keys())
    pi_diff = {}
    for r in all_roots:
        d = pi_e.get(r, 0) - pi_o.get(r, 0)
        if d != 0:
            pi_diff[r] = d
    return {
        'kind': kind,
        'i': i,
        'n_subtypes': len(distribution),
        'distribution': distribution,
        'label_check': label_check,
        'pi_diff': pi_diff,
    }


def run_full_test(max_lam1_int=4, verbose=True):
    """Run the full BGG vs Aug~ comparison for B_3."""
    pairs = B3.enumerate_dominant_spin_pairs(max_lam1_int, N)
    if verbose:
        print(f"Enumerating {len(pairs)} dominant spin pairs (max λ_1 = {max_lam1_int} + 1/2).")

    grand = {
        'n_lambda_mu_pairs': 0,
        'n_basis_total': 0,
        'n_odd_total': 0,
        'n_pure_matched_total': 0,
        'n_mixed_matched_total': 0,
        'n_unmatched_total': 0,
        'n_A_ok': 0,
        'n_A_total': 0,
        'pure_donor_recv_by_si': defaultdict(Counter),  # (kind, i) -> {(donor, receiver, n_swaps): count}
        'mixed_distrib_by_si': defaultdict(Counter),    # (kind, i) -> {frozen(distribution): count}
        'unmatched_examples': [],
        'mixed_examples': [],  # collect a few mixed-pair examples
    }

    t0 = time.time()
    for k_lm, (lam, mu) in enumerate(pairs):
        res = match_pure_then_mixed(lam, mu, N)
        if res is None:
            continue
        items, pair_odd_pure, pair_odd_all, unmatched, _ = res
        grand['n_lambda_mu_pairs'] += 1
        grand['n_basis_total'] += len(items)
        n_odd = sum(1 for _, lng, _, _ in items if lng % 2 == 1)
        grand['n_odd_total'] += n_odd
        n_pure = len(pair_odd_pure)
        n_all = len(pair_odd_all)
        n_mixed = n_all - n_pure
        n_unm = len(unmatched)
        grand['n_pure_matched_total'] += n_pure
        grand['n_mixed_matched_total'] += n_mixed
        grand['n_unmatched_total'] += n_unm

        # (A) and (B) checks on all matched pairs
        for o_idx, (e_idx, move_info) in pair_odd_all.items():
            cls = classify_move(move_info, items, o_idx, e_idx, N)
            grand['n_A_total'] += 1
            if cls['label_check']:
                grand['n_A_ok'] += 1
            ksi = (cls['kind'], cls['i'])
            if cls['n_subtypes'] == 1:
                # PURE move
                st, n_swaps = next(iter(cls['distribution'].items()))
                # Get donor/receiver
                # We need the value of c to compute donor/receiver from (kind, i, st)
                # Easier: read directly from pi_diff
                pos_d = [r for r, d in cls['pi_diff'].items() if d > 0]
                neg_d = [r for r, d in cls['pi_diff'].items() if d < 0]
                # For a pure move: should be exactly 1 positive root with +n_swaps and 1 negative root with -n_swaps
                if len(pos_d) == 1 and len(neg_d) == 1:
                    donor = neg_d[0]
                    receiver = pos_d[0]
                    grand['pure_donor_recv_by_si'][ksi][(donor, receiver, n_swaps, st)] += 1
                else:
                    # Pure move but pi_diff doesn't look like a single swap? shouldn't happen
                    grand['pure_donor_recv_by_si'][ksi][('IRREG', tuple(sorted(cls['pi_diff'].items())))] += 1
            else:
                # MIXED move
                key = tuple(sorted(cls['distribution'].items()))
                grand['mixed_distrib_by_si'][ksi][key] += 1
                if len(grand['mixed_examples']) < 8:
                    grand['mixed_examples'].append({
                        'lam': lam, 'mu': mu,
                        'odd': items[o_idx],
                        'even': items[e_idx],
                        'kind': cls['kind'], 'i': cls['i'],
                        'distribution': cls['distribution'],
                        'pi_diff': cls['pi_diff'],
                    })

        if unmatched and len(grand['unmatched_examples']) < 5:
            for o in unmatched[:2]:
                grand['unmatched_examples'].append({
                    'lam': lam, 'mu': mu,
                    'item': items[o],
                })

        if verbose and (k_lm + 1) % 100 == 0:
            elapsed = time.time() - t0
            print(f"  ... {k_lm+1}/{len(pairs)} pairs processed ({elapsed:.1f}s)")

    elapsed = time.time() - t0
    if verbose:
        print(f"Done in {elapsed:.1f}s.")
    return grand


def summarize(grand):
    print()
    print("=" * 70)
    print("BGGD-B_3 COMPARISON SUMMARY")
    print("=" * 70)
    print(f"# (λ, μ) pairs processed:           {grand['n_lambda_mu_pairs']}")
    print(f"# total basis items:                {grand['n_basis_total']}")
    print(f"# total odd-length items:           {grand['n_odd_total']}")
    print(f"# odd items matched by PURE moves:  {grand['n_pure_matched_total']}")
    print(f"# odd items matched by MIXED moves: {grand['n_mixed_matched_total']}")
    print(f"# odd items UNMATCHED:              {grand['n_unmatched_total']}")
    if grand['n_odd_total'] > 0:
        pct_pure = 100.0 * grand['n_pure_matched_total'] / grand['n_odd_total']
        pct_mixed = 100.0 * grand['n_mixed_matched_total'] / grand['n_odd_total']
        pct_unm = 100.0 * grand['n_unmatched_total'] / grand['n_odd_total']
        print(f"  PURE %:  {pct_pure:.2f}%")
        print(f"  MIXED %: {pct_mixed:.2f}%")
        print(f"  UNMATCHED %: {pct_unm:.2f}%")
    print()
    if grand['n_A_total'] > 0:
        pct_A = 100.0 * grand['n_A_ok'] / grand['n_A_total']
        print(f"(A) LEFT-mult check (w' = s_i · w): "
              f"{grand['n_A_ok']}/{grand['n_A_total']} = {pct_A:.2f}%")
    print()

    # (B) statistics — pure
    print("=" * 70)
    print("(B) PURE-pair distribution: donor->receiver per s_i")
    print("=" * 70)
    for ksi in sorted(grand['pure_donor_recv_by_si'].keys()):
        kind, i = ksi
        si_name = f"s_{i}" if kind == 'L' else f"s_{N-1}(short)"
        ct = grand['pure_donor_recv_by_si'][ksi]
        total = sum(ct.values())
        print(f"\n  {si_name} (kind={kind}, i={i}): {total} pure pairs")
        # group by (donor, receiver) ignoring n_swaps and subtype tag
        by_pair = defaultdict(lambda: defaultdict(int))
        for entry, cnt in ct.items():
            if entry[0] == 'IRREG':
                by_pair[('IRREG',)] = entry
                continue
            donor, receiver, n_swaps, st = entry
            by_pair[(donor, receiver, st)][n_swaps] += cnt
        for key in sorted(by_pair.keys(), key=lambda x: str(x)):
            if key == ('IRREG',):
                print(f"    IRREGULAR: {by_pair[key]}")
                continue
            donor, receiver, st = key
            ns_table = dict(by_pair[key])
            total_for = sum(ns_table.values())
            print(f"    {donor} -> {receiver}  [subtype={st}]  total={total_for}")
            print(f"      by n_swaps: {ns_table}")

    # (B) statistics — mixed
    print()
    print("=" * 70)
    print("MIXED-pair distribution: subtype combinations per s_i")
    print("=" * 70)
    for ksi in sorted(grand['mixed_distrib_by_si'].keys()):
        kind, i = ksi
        si_name = f"s_{i}" if kind == 'L' else f"s_{N-1}(short)"
        ct = grand['mixed_distrib_by_si'][ksi]
        total = sum(ct.values())
        print(f"\n  {si_name} (kind={kind}, i={i}): {total} mixed pairs")
        sorted_combos = sorted(ct.items(), key=lambda x: -x[1])
        for combo, cnt in sorted_combos[:15]:
            print(f"    {dict(combo)}  occurs {cnt} times")
        if len(sorted_combos) > 15:
            print(f"    ... and {len(sorted_combos) - 15} more distinct combos")

    if grand['mixed_examples']:
        print()
        print("=" * 70)
        print("Sample MIXED pair examples:")
        print("=" * 70)
        for ex in grand['mixed_examples']:
            print(f"\n  λ={ex['lam']}, μ={ex['mu']}, simple={ex['kind']}_{ex['i']}")
            print(f"    odd:  w={ex['odd'][0]}, len={ex['odd'][1]}, π={ex['odd'][2]}, bd={ex['odd'][3]}")
            print(f"    even: w={ex['even'][0]}, len={ex['even'][1]}, π={ex['even'][2]}")
            print(f"    distribution: {ex['distribution']}")
            print(f"    pi_diff: {ex['pi_diff']}")

    if grand['unmatched_examples']:
        print()
        print("=" * 70)
        print("UNMATCHED odd items (should be 0; if non-zero, oracle fails):")
        print("=" * 70)
        for ex in grand['unmatched_examples']:
            print(f"  λ={ex['lam']}, μ={ex['mu']}, item={ex['item']}")


def main(max_lam1_int=4):
    grand = run_full_test(max_lam1_int=max_lam1_int, verbose=True)
    summarize(grand)
    return grand


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-lam', type=int, default=4)
    args = parser.parse_args()
    main(max_lam1_int=args.max_lam)
