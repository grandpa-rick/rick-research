"""
Off-slice obstruction classification: B_3 and B_4 short simple (i = n, k(n) = 2).

Conjecture (test #4 in connections/multiorbit-catalog-as-three-strand-braid.md):
  The off-slice obstruction [e_n^k, B_n] pi = e_n^{k-1} pi at eps_n = k(n) - 1 = 1
  decomposes into ONLY moves whose support involves the alpha_n singleton.
  Specifically: intra-chain = 0, cross-chain = 0, singleton-involving = all.

Setup:
  Off-slice region for short simple n: {pi : eps_n(pi) = 1}.
  The commutator on this region equals e_n^{k-1} = e_n^1 = e_n (a SINGLE primitive).
  Each application of e_n on pi produces a "net move" which is a single root delta:
    EITHER a chain primitive (T->M or M->B on chain A, B, C, ...)
    OR the singleton primitive (drops one E_n, no replacement).

Three-strand braid classification of single primitives:
  - chain primitive on chain X -> classify as "intra-chain" (single-chain-only support).
  - singleton primitive (E_n -> 0) -> "singleton-involving".
  - (cross-chain is not possible from a SINGLE primitive — it requires two primitives
    from two distinct chains.)

Empirical procedure:
  1. Enumerate pi with eps_n(pi) = 1 (up to max_total).
  2. For each pi: compute C(pi) := [e_n^2, B_n] pi (Z-linear combination).
  3. Check that C(pi) == e_n(pi) (identity already-verified at B_3, B_4).
  4. Read off the net move (root multiplicity delta) of e_n(pi).
  5. Classify it as intra-chain / cross-chain / singleton-involving.
  6. Report distinct moves and their counts per class.
"""

import sys
from collections import Counter, defaultdict

# Make B_3 and B_4 modules importable.
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

import b_i_b3 as B3
import b_i_b4 as B4


# ====================================================================
# Chain structure for alpha_n short simple
# ====================================================================

B3_CHAINS = {
    'A': {'bot': B3.EM13, 'mid': B3.E1, 'top': B3.EP13},
    'B': {'bot': B3.EM23, 'mid': B3.E2, 'top': B3.EP23},
}
B3_SINGLETON = B3.E3

B4_CHAINS = {
    'A': {'bot': B4.EM14, 'mid': B4.E1, 'top': B4.EP14},
    'B': {'bot': B4.EM24, 'mid': B4.E2, 'top': B4.EP24},
    'C': {'bot': B4.EM34, 'mid': B4.E3, 'top': B4.EP34},
}
B4_SINGLETON = B4.E4


def chains_for(rank):
    return B3_CHAINS if rank == 3 else B4_CHAINS


def singleton_for(rank):
    return B3_SINGLETON if rank == 3 else B4_SINGLETON


def module_for(rank):
    return B3 if rank == 3 else B4


# ====================================================================
# Net move = canonical tuple of (root, delta) for nonzero entries
# ====================================================================

def diff(mod, pi_new, pi_old):
    d = {}
    for r in mod.ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


# ====================================================================
# Single-primitive classification.
#
# A SINGLE e_n step produces one of:
#   (i)  chain primitive of type 'TM' (top -> mid):  delta = -top + mid
#   (ii) chain primitive of type 'MB' (mid -> bot):  delta = -mid + bot
#   (iii) singleton primitive:                       delta = -singleton (E_n)
#
# Each of (i)-(ii) is a single-chain-only support => "intra-chain" class.
# (iii) is singleton-only support => "singleton-involving".
# Cross-chain is impossible for a single primitive (needs two chains).
# ====================================================================

def classify_single_primitive(rank, delta_tuple):
    """Return (class_name, label) for a single-primitive net move.

    delta_tuple: canonical sorted tuple of (root, delta).
    """
    chains = chains_for(rank)
    singleton = singleton_for(rank)
    deltas = dict(delta_tuple)
    # Identify support
    support_roots = set(deltas.keys())

    # Case singleton: only entry is -1*singleton
    if deltas == {singleton: -1}:
        return ('singleton', f'{singleton} -> 0')

    # Case chain primitive: -1 of top/mid AND +1 of mid/bot on same chain
    for cname, c in chains.items():
        d_tm = {c['top']: -1, c['mid']: +1}
        if deltas == d_tm:
            return ('intra', f"chain-{cname}: TM ({c['top']} -> {c['mid']})")
        d_mb = {c['mid']: -1, c['bot']: +1}
        if deltas == d_mb:
            return ('intra', f"chain-{cname}: MB ({c['mid']} -> {c['bot']})")

    # Unrecognized (e.g., spans roots from two distinct chains -> "cross")
    # For a SINGLE e_n step this shouldn't happen, but flag it.
    # Check if support involves two distinct chains:
    chain_membership = defaultdict(set)
    for r in support_roots:
        for cname, c in chains.items():
            if r in (c['top'], c['mid'], c['bot']):
                chain_membership[cname].add(r)
    has_singleton = singleton in support_roots
    n_chains = len(chain_membership)
    if has_singleton and n_chains == 0:
        return ('singleton', f'singleton-only: {delta_tuple}')
    if has_singleton or n_chains >= 2:
        # singleton + chain OR cross-chain
        if n_chains >= 2:
            return ('cross', f'cross-chain support: {delta_tuple}')
        else:
            return ('singleton', f'singleton + chain: {delta_tuple}')
    return ('UNKNOWN', f'unrecognized: {delta_tuple}')


# ====================================================================
# Pretty-print delta
# ====================================================================

def fmt_delta(d):
    if not d:
        return '<no change>'
    return ', '.join(f"{c:+d}*{r}" for r, c in d)


# ====================================================================
# Main test for one rank (3 or 4).
# ====================================================================

def run_for_rank(rank, max_total):
    mod = module_for(rank)
    n = rank  # short simple index
    k = 2

    print(f"\n{'=' * 75}")
    print(f"B_{rank} off-slice obstruction at short simple i = {n}, k(n) = {k}")
    print(f"  Off-slice locus: {{pi : eps_{n}(pi) = {k - 1} = 1}}")
    print(f"  max_total = {max_total}")
    print(f"{'=' * 75}\n")

    # Enumerate eps_n = 1 partitions
    target_pis = []
    for pi in mod.enumerate_partitions(max_total):
        if mod.eps_i(pi, n) == k - 1:
            target_pis.append(pi)
    print(f"  Number of partitions with eps_{n} = 1 (up to total {max_total}): {len(target_pis)}")

    # Verify [e_n^k, B_n] pi == e_n^{k-1} pi for each (sanity)
    n_mismatch_commutator = 0
    mismatch_examples = []
    move_counts = Counter()      # net_move -> # partitions
    move_class = {}               # net_move -> class label
    move_label = {}               # net_move -> human label
    class_total = Counter()       # class -> total partition count
    distinct_moves_by_class = defaultdict(set)

    for pi in target_pis:
        # Compute the commutator C(pi) = [e_n^k, B_n] pi = (e^k B - B e^k) pi
        pi_lc = mod.LinComb.from_kp(pi)
        ek = mod.apply_e_k(pi_lc, n, k)
        B_ek = mod.apply_B(ek, n)
        B = mod.apply_B(pi_lc, n)
        ek_B = mod.apply_e_k(B, n, k)
        comm = ek_B - B_ek

        # Expected: e_n^{k-1} pi = e_n pi (a single Kostant partition)
        expected_pi = mod.e_i_k(pi, n, k - 1)
        expected_lc = mod.LinComb.from_kp(expected_pi) if expected_pi is not None else mod.LinComb.zero()

        if comm != expected_lc:
            n_mismatch_commutator += 1
            if len(mismatch_examples) < 3:
                mismatch_examples.append((pi, comm, expected_lc))
            continue

        # Read off the net move from e_n(pi)
        if expected_pi is None:
            # Shouldn't happen on eps_n = 1: e_n should be defined.
            continue
        d = diff(mod, expected_pi, pi)
        cls, label = classify_single_primitive(rank, d)
        move_counts[d] += 1
        move_class[d] = cls
        move_label[d] = label
        class_total[cls] += 1
        distinct_moves_by_class[cls].add(d)

    print(f"\n  Commutator sanity: mismatches with e_n^{{k-1}} pi = {n_mismatch_commutator}/{len(target_pis)}")
    if mismatch_examples:
        print("  Mismatches (first few):")
        for pi, c, e in mismatch_examples:
            print(f"    pi = {mod.kp_repr(pi)}: comm = {c}, expected = {e}")
        print("  *** This is unexpected; conjecture-test below is unreliable. ***")

    # Report
    print(f"\n  Class totals (number of partitions on which each class of move appears):")
    print(f"    intra-chain:        {class_total['intra']}")
    print(f"    cross-chain:        {class_total['cross']}")
    print(f"    singleton-involving:{class_total['singleton']}")
    print(f"    UNKNOWN:            {class_total['UNKNOWN']}")
    print(f"    total partitions:   {sum(class_total.values())}")

    print(f"\n  Distinct moves observed per class:")
    for cls in ('intra', 'cross', 'singleton', 'UNKNOWN'):
        if not distinct_moves_by_class[cls]:
            print(f"    {cls}: (none)")
            continue
        print(f"    {cls}: {len(distinct_moves_by_class[cls])} distinct move(s)")
        for d in sorted(distinct_moves_by_class[cls]):
            print(f"      [{move_label[d]}]  delta = {fmt_delta(d)}  ({move_counts[d]} partitions)")

    return {
        'rank': rank,
        'n_partitions': len(target_pis),
        'n_mismatch': n_mismatch_commutator,
        'class_total': dict(class_total),
        'distinct_moves_by_class': {c: sorted(s) for c, s in distinct_moves_by_class.items()},
        'move_counts': dict(move_counts),
        'move_label': dict(move_label),
        'move_class': dict(move_class),
    }


def main():
    MAX_B3 = 5
    MAX_B4 = 5

    results = {}
    results['B3'] = run_for_rank(3, MAX_B3)
    results['B4'] = run_for_rank(4, MAX_B4)

    # Verdict
    print(f"\n{'=' * 75}")
    print("VERDICT")
    print(f"{'=' * 75}")
    for tag, res in results.items():
        ct = res['class_total']
        n_intra = ct.get('intra', 0)
        n_cross = ct.get('cross', 0)
        n_singleton = ct.get('singleton', 0)
        if n_intra == 0 and n_cross == 0 and n_singleton > 0:
            v = "CONFIRMED (only singleton-involving moves off-slice)"
        elif n_singleton > 0 and (n_intra > 0 or n_cross > 0):
            v = "PARTIAL / FALSIFIED (mixed classes off-slice)"
        elif n_singleton == 0 and (n_intra > 0 or n_cross > 0):
            v = "REFUTED (no singleton moves, found chain moves)"
        else:
            v = "EMPTY / unclear"
        print(f"  {tag}: intra={n_intra}, cross={n_cross}, singleton={n_singleton} -> {v}")

    return results


if __name__ == '__main__':
    main()
