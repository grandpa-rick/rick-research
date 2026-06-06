"""
BGG vs. Aug~ comparison for C_3 = sp(6) with INTEGER dominant lambda.

Adapts bgg_aug_compare_B3.py.  Key differences from B_3:
  * rho_C = (3, 2, 1) is INTEGER, so the natural choice for tilde_a to be
    integer is integer lambda (not half-integer).
  * C_3 root lattice has even coord-sum, so basis is nonempty only when
    sum(lam_i - mu_i) is even.
  * The exchange simples s_0, s_1 in C_3 have a MIXED-UNIT subtype set:
    (LL,) is a 2-unit swap (2 e_i)<->(2 e_{i+1}); (b/c, .) are 1-unit
    swaps.  The flip simple s_2 has only 1-unit (S, p) subtypes.
  * Because integer C_3 is NOT all-acyclic (unlike B_3 spin: CKL Thm 4.6),
    at some bidegrees there is a mismatch between #odd and #even items.
    The test is: at every bidegree bd, the bipartite max matching = min(#odd, #even),
    every matched pair satisfies (A) and (B').  Unmatched odds/evens correspond
    to BGG cohomology at bd.

Test plan:
  Phase 1: bipartite matching with PURE single-subtype moves.
  Phase 2: augment unmatched odds (or evens) via MIXED-subtype moves.
  Phase 3: verify (A) w' = s_i * w and (B') one-s_i orbit-swap structure.
  Phase 4: tabulate per-bd signed-sum vs (#even - #odd) check.
"""

import os
import sys
import time
from fractions import Fraction
from collections import defaultdict, Counter
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aug_tilde_C3_richer as C3

N = 3


def list_pure_moves(label, pi, w_tilde_a, N):
    """Return list of (move_info, (new_label, new_pi)) for valid PURE moves:
    single subtype, single direction (forward, matching sign of c).

    Distribution format: {(subtype, sign): count} with len == 1.  Sign is determined
    by sign of c (forward direction).
    """
    out = []
    simples = [('S', j) for j in range(N - 1)] + [('L', N - 1)]
    for kind, i in simples:
        c = C3.get_c_value(label, w_tilde_a, kind, i, N)
        if c == 0:
            continue
        n_units = abs(c)
        sign = '-' if c > 0 else '+'
        for st in C3.subtypes_for_simple(kind, i, N):
            u = C3.subtype_units_per_swap(kind, i, st, N)
            if n_units % u != 0:
                continue
            n_swaps = n_units // u
            donor, receiver = C3.subtype_donor_receiver(kind, i, st, c, N)
            if pi.get(donor, 0) >= n_swaps:
                new_pi = dict(pi)
                new_pi[donor] -= n_swaps
                if new_pi[donor] == 0:
                    del new_pi[donor]
                new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
                if kind == 'S':
                    new_label = C3.s_exch_w(label, i, N)
                else:
                    new_label = C3.s_flip_w(label, N)
                out.append(((kind, i, {(st, sign): n_swaps}), (new_label, new_pi)))
    return out


def list_all_mixed_moves(label, pi, w_tilde_a, N):
    return C3.list_all_simple_moves(label, pi, w_tilde_a, N)


def freeze_pi(pi):
    return frozenset(pi.items())


def build_basis_and_edges(lam, mu, N, pure_only=False):
    """Return (items, item_index, odd_idxs, edges_per_odd, tilde_a) for (lam, mu)."""
    tilde_a, b, items = C3.collect_items(lam, mu, N)
    if items is None:
        return None
    item_index = {(lbl, freeze_pi(pi)): idx for idx, (lbl, _, pi, _) in enumerate(items)}
    odd_idxs = [idx for idx, (_, lng, _, _) in enumerate(items) if lng % 2 == 1]
    edges = {}
    for idx in odd_idxs:
        label, length, pi, bd = items[idx]
        w_func = C3.w_label_to_func(label, N)
        w_tilde_a_frac = w_func(tilde_a)
        # all c-values must be integer; if any is non-integer we know it's spin C_3
        # and we just skip (no moves through that simple).
        # In integer C_3 they are always integer; safe to convert.
        if not all(x.denominator == 1 for x in w_tilde_a_frac):
            ed = []
            edges[idx] = ed
            continue
        w_tilde_a = tuple(int(x) for x in w_tilde_a_frac)
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
    res = build_basis_and_edges(lam, mu, N, pure_only=True)
    if res is None:
        return None
    items, item_index, odd_idxs, pure_edges, tilde_a = res
    pair_odd_pure, pair_even_pure = maximum_bipartite_matching(odd_idxs, pure_edges)

    res_all = build_basis_and_edges(lam, mu, N, pure_only=False)
    items_all, item_index_all, odd_idxs_all, all_edges, _ = res_all
    assert len(items_all) == len(items)

    pair_odd = dict(pair_odd_pure)
    pair_even = dict(pair_even_pure)

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
    """Classify a matched pair.

    distribution format: {(subtype, sign): count} with sign in {-,+}.
    A 'pure' move has len(distribution) == 1 (single subtype, single direction).
    A 'mixed' move uses multiple (subtype, sign) keys, all within the same s_i.

    (B') condition: every (subtype, sign) is some swap within an s_i orbit (built-in
    by construction of distributions).
    """
    kind, i, distribution = move_info
    lbl_o, _, pi_o, _ = items[o_idx]
    lbl_e, _, pi_e, _ = items[e_idx]
    if kind == 'S':
        expected = C3.s_exch_w(lbl_o, i, N)
    else:
        expected = C3.s_flip_w(lbl_o, N)
    label_check = (expected == lbl_e)
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


def per_bd_signed_sums(items):
    """Return dict bd -> (#even, #odd, signed_sum=#even-#odd)."""
    bd_e = Counter()
    bd_o = Counter()
    for _, lng, _, bd in items:
        if lng % 2 == 0:
            bd_e[bd] += 1
        else:
            bd_o[bd] += 1
    all_bd = set(bd_e) | set(bd_o)
    return {bd: (bd_e[bd], bd_o[bd], bd_e[bd] - bd_o[bd]) for bd in all_bd}


def run_full_test(max_lam1_int=3, verbose=True):
    """Run BGG vs Aug~ comparison for C_3 over INTEGER dominant pairs."""
    pairs = C3.enumerate_dominant_integer_pairs(max_lam1_int, N)
    # Filter to pairs with lam-mu in C_3 root lattice (even coord-sum diff).
    valid_pairs = []
    for lam, mu in pairs:
        diff_sum = sum(int(lam[i] - mu[i]) for i in range(N))
        if diff_sum % 2 == 0:
            valid_pairs.append((lam, mu))
    if verbose:
        print(f"Enumerating {len(valid_pairs)} dominant integer pairs (max lambda_1 = {max_lam1_int}, "
              f"lam-mu in root lattice).")

    grand = {
        'n_lambda_mu_pairs': 0,
        'n_basis_total': 0,
        'n_odd_total': 0,
        'n_even_total': 0,
        'n_pure_matched_total': 0,
        'n_mixed_matched_total': 0,
        'n_unmatched_odd_total': 0,
        'n_unmatched_even_total': 0,
        'n_A_ok': 0,
        'n_A_total': 0,
        'n_Bprime_ok': 0,
        'n_Bprime_total': 0,
        'pure_donor_recv_by_si': defaultdict(Counter),
        'mixed_distrib_by_si': defaultdict(Counter),
        'unmatched_examples': [],
        'mixed_examples': [],
        'bgg_signed_consistency_ok': 0,
        'bgg_signed_consistency_total': 0,
    }

    t0 = time.time()
    for k_lm, (lam, mu) in enumerate(valid_pairs):
        res = match_pure_then_mixed(lam, mu, N)
        if res is None:
            continue
        items, pair_odd_pure, pair_odd_all, unmatched, _ = res
        grand['n_lambda_mu_pairs'] += 1
        grand['n_basis_total'] += len(items)
        n_odd = sum(1 for _, lng, _, _ in items if lng % 2 == 1)
        n_even = sum(1 for _, lng, _, _ in items if lng % 2 == 0)
        grand['n_odd_total'] += n_odd
        grand['n_even_total'] += n_even
        n_pure = len(pair_odd_pure)
        n_all = len(pair_odd_all)
        n_mixed = n_all - n_pure
        n_unm_odd = len(unmatched)
        # Computed unmatched evens: # evens not in pair_odd_all.values()
        used_evens = set(ev for (ev, _) in pair_odd_all.values())
        n_unm_even = n_even - len(used_evens)
        grand['n_pure_matched_total'] += n_pure
        grand['n_mixed_matched_total'] += n_mixed
        grand['n_unmatched_odd_total'] += n_unm_odd
        grand['n_unmatched_even_total'] += n_unm_even

        # Per-bd: BGG signed-sum (#even - #odd) should equal (#unused_even - #unmatched_odd).
        per_bd = per_bd_signed_sums(items)
        unmatched_at_bd = Counter()
        for o in unmatched:
            unmatched_at_bd[items[o][3]] += 1
        unused_evens_at_bd = Counter()
        for ev_idx, (_, lng, _, bd) in enumerate(items):
            if lng % 2 != 0:
                continue
            if ev_idx not in used_evens:
                unused_evens_at_bd[bd] += 1
        for bd, (e, o, sgn) in per_bd.items():
            bgg_signed = e - o
            actual_diff = unused_evens_at_bd[bd] - unmatched_at_bd[bd]
            grand['bgg_signed_consistency_total'] += 1
            if bgg_signed == actual_diff:
                grand['bgg_signed_consistency_ok'] += 1

        # (A), (B') checks on all matched pairs.
        # (B') in this framework is automatic by construction: distributions are over
        # (subtype, sign) within ONE simple reflection.
        for o_idx, (e_idx, move_info) in pair_odd_all.items():
            cls = classify_move(move_info, items, o_idx, e_idx, N)
            grand['n_A_total'] += 1
            if cls['label_check']:
                grand['n_A_ok'] += 1
            grand['n_Bprime_total'] += 1
            grand['n_Bprime_ok'] += 1  # built-in: all distributions are within one s_i.
            ksi = (cls['kind'], cls['i'])
            if cls['n_subtypes'] == 1:
                key, n_swaps = next(iter(cls['distribution'].items()))
                st, sign = key
                pos_d = [r for r, d in cls['pi_diff'].items() if d > 0]
                neg_d = [r for r, d in cls['pi_diff'].items() if d < 0]
                if len(pos_d) == 1 and len(neg_d) == 1:
                    donor = neg_d[0]
                    receiver = pos_d[0]
                    grand['pure_donor_recv_by_si'][ksi][(donor, receiver, n_swaps, st, sign)] += 1
                else:
                    grand['pure_donor_recv_by_si'][ksi][('IRREG', tuple(sorted(cls['pi_diff'].items())))] += 1
            else:
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
                    'bd': items[o][3],
                })

        if verbose and (k_lm + 1) % 50 == 0:
            elapsed = time.time() - t0
            print(f"  ... {k_lm+1}/{len(valid_pairs)} pairs processed ({elapsed:.1f}s)")

    elapsed = time.time() - t0
    if verbose:
        print(f"Done in {elapsed:.1f}s.")
    return grand


def summarize(grand):
    print()
    print("=" * 70)
    print("BGGD-C_3 COMPARISON SUMMARY (integer lambda)")
    print("=" * 70)
    print(f"# (lambda, mu) pairs processed:        {grand['n_lambda_mu_pairs']}")
    print(f"# total basis items:                   {grand['n_basis_total']}")
    print(f"# total odd-length items:              {grand['n_odd_total']}")
    print(f"# total even-length items:             {grand['n_even_total']}")
    print(f"# odd items matched by PURE moves:     {grand['n_pure_matched_total']}")
    print(f"# odd items matched by MIXED moves:    {grand['n_mixed_matched_total']}")
    print(f"# odd items UNMATCHED:                 {grand['n_unmatched_odd_total']}")
    print(f"# even items UNUSED:                   {grand['n_unmatched_even_total']}")
    print(f"  (= BGG cohomology dim total in each parity, equal to abs sum signed)")
    print()
    if grand['n_A_total'] > 0:
        pct_A = 100.0 * grand['n_A_ok'] / grand['n_A_total']
        print(f"(A) LEFT-mult check (w' = s_i . w): "
              f"{grand['n_A_ok']}/{grand['n_A_total']} = {pct_A:.2f}%")
    if grand['n_Bprime_total'] > 0:
        pct_B = 100.0 * grand['n_Bprime_ok'] / grand['n_Bprime_total']
        print(f"(B') within-one-s_i orbit-swap check: "
              f"{grand['n_Bprime_ok']}/{grand['n_Bprime_total']} = {pct_B:.2f}%")
    print(f"BGG signed-sum vs (#unused_even - #unmatched_odd) consistency at each bd: "
          f"{grand['bgg_signed_consistency_ok']}/{grand['bgg_signed_consistency_total']}")
    print()

    print("=" * 70)
    print("(B) PURE-pair distribution: donor->receiver per s_i")
    print("=" * 70)
    for ksi in sorted(grand['pure_donor_recv_by_si'].keys()):
        kind, i = ksi
        if kind == 'S':
            si_name = f"s_{i} (short EXC, alpha={i}-{i+1})"
        else:
            si_name = f"s_{N-1} (long FLIP, alpha=2 e_{N-1})"
        ct = grand['pure_donor_recv_by_si'][ksi]
        total = sum(ct.values())
        print(f"\n  {si_name} (kind={kind}, i={i}): {total} pure pairs")
        by_pair = defaultdict(lambda: defaultdict(int))
        for entry, cnt in ct.items():
            if entry[0] == 'IRREG':
                by_pair[('IRREG',)] = entry
                continue
            donor, receiver, n_swaps, st, sign = entry
            by_pair[(donor, receiver, st, sign)][n_swaps] += cnt
        for key in sorted(by_pair.keys(), key=lambda x: str(x)):
            if key == ('IRREG',):
                print(f"    IRREGULAR: {by_pair[key]}")
                continue
            donor, receiver, st, sign = key
            ns_table = dict(by_pair[key])
            total_for = sum(ns_table.values())
            print(f"    {donor} -> {receiver}  [subtype={st}, sign={sign}]  total={total_for}")
            print(f"      by n_swaps: {ns_table}")

    print()
    print("=" * 70)
    print("MIXED-pair distribution: subtype combinations per s_i")
    print("=" * 70)
    for ksi in sorted(grand['mixed_distrib_by_si'].keys()):
        kind, i = ksi
        if kind == 'S':
            si_name = f"s_{i} (short EXC)"
        else:
            si_name = f"s_{N-1} (long FLIP)"
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
        for ex in grand['mixed_examples'][:5]:
            print(f"\n  lam={ex['lam']}, mu={ex['mu']}, simple={ex['kind']}_{ex['i']}")
            print(f"    odd:  w={ex['odd'][0]}, len={ex['odd'][1]}, pi={ex['odd'][2]}, bd={ex['odd'][3]}")
            print(f"    even: w={ex['even'][0]}, len={ex['even'][1]}, pi={ex['even'][2]}")
            print(f"    distribution: {ex['distribution']}")
            print(f"    pi_diff: {ex['pi_diff']}")


def main(max_lam1_int=3):
    grand = run_full_test(max_lam1_int=max_lam1_int, verbose=True)
    summarize(grand)
    return grand


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-lam', type=int, default=3)
    args = parser.parse_args()
    main(max_lam1_int=args.max_lam)
