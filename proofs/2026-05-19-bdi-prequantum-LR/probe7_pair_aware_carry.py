"""
probe7_pair_aware_carry.py — Test Candidate 1' ("pair-aware carry")
for the image of the descent-recording map R(pi).

Follow-up to probe6 (Candidate 1 falsified at B_3 max_c=5: 0 FP, 268 FN).
All FNs share the pattern: a TM(a) at position i precedes an MB(a) at j > i,
and the reverse-played intermediate state has P_a < 0 between i and j, but
the final state has P_a >= 0.

HYPOTHESIS (Candidate 1', "pair-aware carry"):

Define a TM(a)-MB(a) *carry-borrow pair* in word R as: positions i < j such
that R[i] = TM(a), R[j] = MB(a), and no other letter affecting chain a
(i.e., no other MB(a) or TM(a)) appears strictly between them. (Greedy
left-to-right pairing.)

Modified condition: when reading prefix R_{1:k} left-to-right, treat each
carry-borrow pair as a single atomic compound step. Only check non-negativity
of coords AND carry at COMPOUND boundaries — i.e., positions k such that
k is not strictly inside any pair (k <= i or k >= j for every pair (i,j)).

R in R(pi^hw) iff every compound-boundary state has chain coords >= 0 AND
carry P_a >= 0, AND forward-descent of the reconstructed state recovers R.

Net effect of an atomic pair (TM(a) then MB(a)) on chain a in DESCENT (forward):
  TM(a):  (T, M, B) -> (T-1, M+1, B)
  MB(a):  (T, M, B) -> (T, M-1, B+1)
  Net:    (T, M, B) -> (T-1, M, B+1)
So M is unchanged across the pair, only T-->T-1 and B-->B+1. The carry
P_a = sum_{i<=a} 2*(B_i - T_i) INCREASES by 4 over the pair, which is why
the intermediate dip (P_a < 0 mid-pair) is OK iff we close it within the pair.
"""

import sys
import time
from collections import defaultdict
from itertools import product

sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-19-bdi-prequantum-LR')

from bdi_qLR import (
    descent_recording, reconstruct, carry_profile,
)

from probe6_Rpi_image import (
    alphabet, reverse_letter, coords_nonnegative, carry_nonnegative,
    all_words_up_to,
)


# ----------------------------------------------------------------------------
# Pair identification (greedy left-to-right; no chain-a letter strictly between)
# ----------------------------------------------------------------------------

def find_pairs(word):
    """Return a list of (i, j, a) for each TM(a)-MB(a) carry-borrow pair.

    Greedy: scan left-to-right. For each chain a, keep track of the most
    recent "open" TM(a) (one that has not been closed by an MB(a) and has
    no intervening chain-a letter). When we see MB(a), if a is open, close
    the pair. When we see TM(a), if a was already open, the older open TM(a)
    is "broken" (an intervening TM(a) is a chain-a letter), and the new TM(a)
    becomes the open one. Similarly, two consecutive MB(a) without a TM(a)
    between -> only the first MB(a) closes; the second is unpaired.

    Actually the cleanest interpretation: a pair (i, j, a) requires R[i]=TM(a),
    R[j]=MB(a), and NO other MB(a) or TM(a) in (i, j). So:
      - Scan left-to-right.
      - Maintain `open[a]` = position of the most recent unclosed TM(a) with
        no chain-a letter after it.
      - On TM(a) at pos k: open[a] = k (any prior open[a] is now invalidated
        because a new TM(a) is itself a chain-a letter and breaks the pair).
      - On MB(a) at pos k: if open[a] is not None, emit (open[a], k, a) and
        set open[a] = None. If open[a] is None, MB(a) at pos k is unpaired.
    """
    pairs = []
    open_pos = {}   # a -> position of open TM(a)
    for k, (typ, fac) in enumerate(word):
        if typ == 'TM':
            a = fac
            open_pos[a] = k   # any prior open TM(a) is invalidated
        elif typ == 'MB':
            a = fac
            if open_pos.get(a) is not None:
                pairs.append((open_pos[a], k, a))
                open_pos[a] = None
            # else MB(a) unpaired; do nothing
        # Sing: no chain effect, doesn't affect pairing.
    return pairs


def compound_boundaries(L, pairs):
    """Return sorted list of compound-boundary indices in 0..L.

    k is a boundary iff for every pair (i, j, a), k <= i or k >= j+1.
    (We include k=0 and k=L always.)

    Note: positions k correspond to "after reading R_{1:k}", i.e., state pi(k).
    A pair occupies positions i and j of the word (0-indexed). The state
    "inside the pair" is at k = i+1, ..., j (since after reading R[i]=TM(a)
    we're at pi(i+1), which is inside the pair, up to after reading R[j]=MB(a)
    which is at pi(j+1) = boundary after the pair).

    So k is a boundary iff k <= i or k >= j+1 for every pair (i, j, a).
    """
    boundaries = []
    for k in range(L + 1):
        ok = True
        for (i, j, a) in pairs:
            if i < k < j + 1:
                ok = False
                break
        if not ok:
            continue
        boundaries.append(k)
    return boundaries


# ----------------------------------------------------------------------------
# Candidate 1' test
# ----------------------------------------------------------------------------

def candidate1prime_test(M_hw, B_hw, T_hw, S_hw, word, n):
    """Test pair-aware non-negativity for `word` starting from pi^hw.

    Approach:
      1. Identify pairs in `word`.
      2. Compute compound boundaries B = sorted([0..L] minus inside-pair).
      3. Reverse-play the word to get all intermediate states; for each
         boundary k, the state pi(k) = state reached after replaying the
         LAST L-k letters of the word from pi^hw.
      4. Check coords and carry non-negativity at each boundary state.
      5. Finally, forward-descent of pi(0) must recover the word.
    """
    L = len(word)
    pairs = find_pairs(list(word))
    bdries = compound_boundaries(L, pairs)

    # Compute reverse-play states pi(L), pi(L-1), ..., pi(0).
    # pi(L) = pi^hw. After replaying letter R[L-1], we get pi(L-1). Etc.
    state = (M_hw, B_hw, T_hw, S_hw)
    # states[k] = pi(k)
    states = [None] * (L + 1)
    states[L] = state
    for step in range(L):
        # step = 0,...,L-1; we apply R[L-1-step] in reverse to get pi(L-1-step)
        idx = L - 1 - step
        letter = word[idx]
        state = reverse_letter(state, letter)
        states[idx] = state

    # Check at each boundary
    for k in bdries:
        st = states[k]
        if not coords_nonnegative(st):
            return False
        if not carry_nonnegative(st, n):
            return False

    # Finally, forward-descent of pi(0) must recover the word.
    pi0 = states[0]
    M0, B0, T0, S0 = pi0
    M_hw2, B_hw2, T_hw2, S_hw2, R = descent_recording(M0, B0, T0, S0, n)
    if tuple(R) != tuple(word):
        return False
    if (M_hw2, B_hw2, T_hw2, S_hw2) != (M_hw, B_hw, T_hw, S_hw):
        return False
    return True


# ----------------------------------------------------------------------------
# Main experiment (mirror probe6 but with candidate1prime_test)
# ----------------------------------------------------------------------------

def run_experiment(n, max_c, time_budget_sec=300):
    sigma = alphabet(n)
    print(f"=== B_{n}, max_c = {max_c}, |Sigma| = {len(sigma)} ===")
    print(f"Alphabet: {sigma}")

    t0 = time.time()

    image_map = defaultdict(set)
    pi_count = 0
    for total_c in range(max_c + 1):
        for parts in product(range(max_c + 1), repeat=n - 1):
            if sum(parts) > max_c:
                continue
            for S in range(max_c - sum(parts) + 1):
                chain_choices = []
                for a in range(n - 1):
                    choices = []
                    for M_a in range(parts[a] + 1):
                        for B_a in range(parts[a] - M_a + 1):
                            T_a = parts[a] - M_a - B_a
                            choices.append((M_a, B_a, T_a))
                    chain_choices.append(choices)
                for combo in product(*chain_choices):
                    M = tuple(x[0] for x in combo)
                    B = tuple(x[1] for x in combo)
                    T = tuple(x[2] for x in combo)
                    M_hw, B_hw, T_hw, S_hw, R = descent_recording(M, B, T, S, n)
                    key = (M_hw, B_hw, T_hw, S_hw)
                    image_map[key].add(tuple(R))
                    pi_count += 1
        if time.time() - t0 > time_budget_sec * 0.3:
            print(f"  Stage 1 time budget exceeded at total_c <= {total_c}")
            break

    t1 = time.time()
    print(f"Enumerated {pi_count} pi's in {t1 - t0:.2f}s")
    print(f"Distinct pi^hw observed: {len(image_map)}")

    total_pairs_tested = 0
    fp_list = []  # predicted but not observed (false positives)
    fn_list = []  # observed but not predicted (false negatives)
    max_word_len_global = 0

    hw_keys = sorted(image_map.keys(),
                     key=lambda k: (sum(k[0]) + sum(k[1]) + sum(k[2]) + k[3], k))
    for hw_key in hw_keys:
        if time.time() - t0 > time_budget_sec:
            print(f"  Stage 2 time budget exceeded.")
            break
        M_hw, B_hw, T_hw, S_hw = hw_key
        observed = image_map[hw_key]
        max_L = max(len(R) for R in observed)
        max_word_len_global = max(max_word_len_global, max_L)

        predicted = set()
        word_budget = 0
        for w in all_words_up_to(max_L, sigma):
            word_budget += 1
            total_pairs_tested += 1
            if candidate1prime_test(M_hw, B_hw, T_hw, S_hw, list(w), n):
                predicted.add(tuple(w))
            if word_budget > 200000:
                break

        PnO = predicted - observed
        OnP = observed - predicted
        for w in sorted(PnO):
            fp_list.append((hw_key, w))
        for w in sorted(OnP):
            fn_list.append((hw_key, w))

    t2 = time.time()
    print(f"Total candidate (pi^hw, word) pairs tested: {total_pairs_tested}")
    print(f"Max word length: {max_word_len_global}")
    print(f"Test elapsed: {t2 - t0:.2f}s")
    print()
    print(f"#False positives (predicted, not observed): {len(fp_list)}")
    for hw_key, w in fp_list[:8]:
        prs = find_pairs(list(w))
        print(f"  pi^hw = (M={hw_key[0]}, B={hw_key[1]}, T={hw_key[2]}, S={hw_key[3]})")
        print(f"    extra word: {w}")
        print(f"    pairs: {prs}")
    print()
    print(f"#False negatives (observed, not predicted): {len(fn_list)}")
    for hw_key, w in fn_list[:8]:
        prs = find_pairs(list(w))
        print(f"  pi^hw = (M={hw_key[0]}, B={hw_key[1]}, T={hw_key[2]}, S={hw_key[3]})")
        print(f"    missing word: {w}")
        print(f"    pairs: {prs}")

    print()
    if not fp_list and not fn_list:
        verdict = "CONFIRMED"
        print("VERDICT: CONFIRMED (no discrepancies)")
    elif fp_list and not fn_list:
        verdict = "FALSIFIED-too-loose"
        print("VERDICT: FALSIFIED-too-loose")
    elif fn_list and not fp_list:
        verdict = "FALSIFIED-too-strict"
        print("VERDICT: FALSIFIED-too-strict")
    else:
        verdict = "FALSIFIED-both"
        print("VERDICT: FALSIFIED (both FP and FN)")

    # Pattern analysis on FNs
    if fn_list:
        print()
        print("FN pattern analysis:")
        # Classify FNs:
        #   - has_nested_same: contains TM(a)...TM(a) before any MB(a) (greedy pairer
        #     only catches the inner pair, missing the outer)
        #   - has_cross_chain: TM(a) at i, MB(b) at j > i, b != a, no chain-a or
        #     chain-b letter strictly between (true cross-chain "borrow")
        #   - failure_at_initial: pi(0) already has P_a < 0 (the FIRST boundary fails)
        nested_count = 0
        cross_count = 0
        only_pair_present = 0  # exactly one detected pair, no nesting, no cross
        fail_at_initial = 0

        for hw_key, w in fn_list:
            wl = list(w)
            prs = find_pairs(wl)
            # Nested same-chain?
            has_nested = False
            for a in range(1, n):
                pos_tm = [k for k, (t, f) in enumerate(wl) if t == 'TM' and f == a]
                pos_mb = [k for k, (t, f) in enumerate(wl) if t == 'MB' and f == a]
                if len(pos_tm) >= 2 and len(pos_mb) >= 1:
                    if pos_tm[1] < (pos_mb[0] if pos_mb else 10**9):
                        has_nested = True
                        break
            # Cross-chain?
            has_cross = False
            for i, (t1_, f1) in enumerate(wl):
                if t1_ != 'TM':
                    continue
                a = f1
                for j in range(i + 1, len(wl)):
                    t2_, f2 = wl[j]
                    if t2_ == 'MB' and f2 != a:
                        b = f2
                        ok = True
                        for k in range(i + 1, j):
                            tk, fk = wl[k]
                            if tk in ('MB', 'TM') and fk in (a, b):
                                ok = False
                                break
                        if ok:
                            has_cross = True
                            break
                if has_cross:
                    break
            if has_nested:
                nested_count += 1
            if has_cross:
                cross_count += 1
            if not has_nested and not has_cross:
                only_pair_present += 1
            # Did pi(0) (the very first compound boundary) fail?
            M_hw, B_hw, T_hw, S_hw = hw_key
            L = len(wl)
            state = (M_hw, B_hw, T_hw, S_hw)
            for step in range(L):
                idx = L - 1 - step
                letter = wl[idx]
                state = reverse_letter(state, letter)
            # state == pi(0)
            if not coords_nonnegative(state) or not carry_nonnegative(state, n):
                fail_at_initial += 1

        print(f"  Total FNs: {len(fn_list)}")
        print(f"  FNs with nested same-chain (TM(a)...TM(a) before MB(a)): {nested_count}")
        print(f"  FNs with cross-chain TM(a)..MB(b), b!=a (no a,b between): {cross_count}")
        print(f"  FNs with neither (just a single same-chain pair detected): {only_pair_present}")
        print(f"  FNs where pi(0) itself fails coords/carry (start-state in deficit): {fail_at_initial}")

    if fp_list:
        print()
        print("FP pattern analysis:")
        # Are the FPs words that pass coords/carry at boundaries but actually
        # don't descend back to themselves? Or do they have unpaired TM/MB?
        unpaired_TM = 0
        unpaired_MB = 0
        for hw_key, w in fp_list:
            prs = find_pairs(list(w))
            paired_tms = set((i,) for i, j, a in prs)
            paired_mbs = set((j,) for i, j, a in prs)
            for k, (t, f) in enumerate(w):
                if t == 'TM' and (k,) not in paired_tms:
                    unpaired_TM += 1
                if t == 'MB' and (k,) not in paired_mbs:
                    unpaired_MB += 1
        print(f"  Total FPs: {len(fp_list)}")
        print(f"  Unpaired TM-letter instances across FPs: {unpaired_TM}")
        print(f"  Unpaired MB-letter instances across FPs: {unpaired_MB}")

    print()
    return fp_list, fn_list, total_pairs_tested, max_word_len_global, verdict


if __name__ == '__main__':
    print(f"\n{'='*72}")
    print(f"Attempting B_3 with max_c = 5")
    print(f"{'='*72}\n")
    t_start = time.time()
    fp, fn, n_pairs, max_L, verdict = run_experiment(3, 5, time_budget_sec=270)
    elapsed = time.time() - t_start
    print(f"\nFinished max_c=5 in {elapsed:.1f}s")
    print(f"Final verdict: {verdict}")
