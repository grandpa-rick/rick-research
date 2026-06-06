"""
probe8_suffix_balance.py — Test Candidate 3 ("suffix-balance carry")
for the image of the descent-recording map R(pi).

Background: probe6 (Candidate 1 = prefix carry >= 0) and probe7 (Candidate 1' =
pair-aware prefix carry) both FALSIFIED at B_3 max_c=5. Root cause: pi(0)
(the input Kostant partition itself) need NOT have carry >= 0; only pi^hw
does. Carry-deficits are LIFTED by FUTURE letters in the descent recording,
not "paid" by past letters. So locality is suffix-based, not prefix-based.

HYPOTHESIS (Candidate 3, "suffix balance"):

Reverse-play R from pi^hw. Let pi(k) = state after reverse-playing
R[k+1..L] (Python 1-indexed: letters at indices k..L-1 in 0-indexed). So
pi(L) = pi^hw, pi(0) = original pi.

For each k in 0..L, for each chain a in 1..n-1:

  (C3-coord) chain coords M_a, B_a, T_a of pi(k) are >= 0; S >= 0.

  (C3-chain) T_a(pi(k)) - B_a(pi(k)) <= #MB(a) in R[0..k-1] - #TM(a) in R[0..k-1].

  Equivalently (multiply by 2): the carry "deficit" -P_a (if any) at pi(k) is
  bounded by twice the prefix net MB(a)-TM(a) count.

Wait — P_a is summed over chains 1..a. The chain-level condition above is
PER-CHAIN: T_a <= B_a + (prefix net carry on chain a). The carry condition
would be the cumulative sum: P_a(pi(k)) + 2 * sum_{b<=a}(prefix_net_b) >= 0.

We test BOTH variants (chain-local and carry-cumulative).

ALSO test forward variant: P_a(pi(k)) + 2 * sum_{b<=a}(suffix_net_b ON FUTURE
LETTERS) >= 0, where suffix_net_b at step k = #MB(b) - #TM(b) in R[k..L-1]
(the letters that have ALREADY been reverse-played). Actually, by symmetry,
prefix + suffix net = total net = (B_hw - T_hw, since net effect of full word
on chain a is to go from pi(0) to pi^hw). So the two variants are dual.

Finally, forward-descent of pi(0) must recover the word R.
"""

import sys
import time
from collections import defaultdict
from itertools import product

sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-19-bdi-prequantum-LR')

from bdi_qLR import descent_recording, carry_profile

from probe6_Rpi_image import (
    alphabet, reverse_letter, coords_nonnegative,
    all_words_up_to,
)


# ----------------------------------------------------------------------------
# Prefix / suffix net counts on a given word
# ----------------------------------------------------------------------------

def prefix_net_counts(word, n):
    """Return prefix_net[k][a-1] = #MB(a) in R[0..k-1] - #TM(a) in R[0..k-1]
    for k = 0..L. Returns a list of L+1 tuples of length n-1.
    """
    L = len(word)
    out = [tuple([0] * (n - 1))]
    cur = [0] * (n - 1)
    for k in range(L):
        typ, fac = word[k]
        if typ == 'MB':
            cur[fac - 1] += 1
        elif typ == 'TM':
            cur[fac - 1] -= 1
        out.append(tuple(cur))
    return out


# ----------------------------------------------------------------------------
# Candidate 3 test (per-chain version)
# ----------------------------------------------------------------------------

def candidate3_chain_test(M_hw, B_hw, T_hw, S_hw, word, n):
    """Test PER-CHAIN suffix-balance:

      For every k in 0..L and every chain a in 1..n-1:
        coords of pi(k) >= 0
        T_a(pi(k)) - B_a(pi(k)) <= prefix_net_a(k)

      where prefix_net_a(k) = #MB(a) - #TM(a) in R[0..k-1].

      Plus forward-descent of pi(0) recovers R.
    """
    L = len(word)
    pn = prefix_net_counts(word, n)  # pn[k] is a tuple of length n-1

    # Compute reverse-play states pi(L), pi(L-1), ..., pi(0).
    state = (M_hw, B_hw, T_hw, S_hw)
    states = [None] * (L + 1)
    states[L] = state
    for step in range(L):
        idx = L - 1 - step
        letter = word[idx]
        state = reverse_letter(state, letter)
        states[idx] = state

    for k in range(L + 1):
        M, B, T, S = states[k]
        if S < 0:
            return False
        for a_idx in range(n - 1):
            if M[a_idx] < 0 or B[a_idx] < 0 or T[a_idx] < 0:
                return False
            # T_a - B_a <= prefix_net_a(k)
            if T[a_idx] - B[a_idx] > pn[k][a_idx]:
                return False

    # Forward-descent of pi(0) recovers R, and HW matches.
    M0, B0, T0, S0 = states[0]
    M_hw2, B_hw2, T_hw2, S_hw2, R = descent_recording(M0, B0, T0, S0, n)
    if tuple(R) != tuple(word):
        return False
    if (M_hw2, B_hw2, T_hw2, S_hw2) != (M_hw, B_hw, T_hw, S_hw):
        return False
    return True


# ----------------------------------------------------------------------------
# Candidate 3 test (cumulative carry version)
# ----------------------------------------------------------------------------

def candidate3_carry_test(M_hw, B_hw, T_hw, S_hw, word, n):
    """Test CUMULATIVE-CARRY suffix-balance:

      For every k in 0..L and every a in 1..n-1:
        coords of pi(k) >= 0
        P_a(pi(k)) + 2 * sum_{b<=a} prefix_net_b(k) >= 0

      Plus the (HW_sing) condition: S(pi(k)) <= P_{n-1}(pi(k)) +
      2 * sum prefix_net? No: S non-negativity is about coords. The
      P_a >= 0 condition at the FINAL (=initial pi^hw) state is the HW
      condition; at intermediate states the suffix-balance condition allows
      P_a < 0 iff prefix-net compensates.

      Plus forward-descent of pi(0) recovers R, and HW matches.
    """
    L = len(word)
    pn = prefix_net_counts(word, n)

    state = (M_hw, B_hw, T_hw, S_hw)
    states = [None] * (L + 1)
    states[L] = state
    for step in range(L):
        idx = L - 1 - step
        letter = word[idx]
        state = reverse_letter(state, letter)
        states[idx] = state

    for k in range(L + 1):
        M, B, T, S = states[k]
        if S < 0:
            return False
        for a_idx in range(n - 1):
            if M[a_idx] < 0 or B[a_idx] < 0 or T[a_idx] < 0:
                return False
        P = carry_profile(M, B, T, n)  # P = (P_0=0, P_1, ..., P_{n-1})
        # Cumulative prefix net
        cum_pn = 0
        for a in range(1, n):
            cum_pn += pn[k][a - 1]
            # P_a + 2 * cum_pn >= 0
            if P[a] + 2 * cum_pn < 0:
                return False

    M0, B0, T0, S0 = states[0]
    M_hw2, B_hw2, T_hw2, S_hw2, R = descent_recording(M0, B0, T0, S0, n)
    if tuple(R) != tuple(word):
        return False
    if (M_hw2, B_hw2, T_hw2, S_hw2) != (M_hw, B_hw, T_hw, S_hw):
        return False
    return True


# ----------------------------------------------------------------------------
# Cached image enumeration (Stage 1 from probe6/7)
# ----------------------------------------------------------------------------

def enumerate_image(n, max_c, time_budget_sec=120):
    """Return image_map: pi^hw -> set of observed words R."""
    image_map = defaultdict(set)
    pi_count = 0
    t0 = time.time()
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
        if time.time() - t0 > time_budget_sec:
            print(f"  [enum] time budget exceeded at total_c <= {total_c}")
            break
    return image_map, pi_count


# ----------------------------------------------------------------------------
# Main experiment
# ----------------------------------------------------------------------------

def run_experiment(n, max_c, time_budget_sec=300, variant='chain'):
    sigma = alphabet(n)
    print(f"=== B_{n}, max_c = {max_c}, |Sigma| = {len(sigma)}, variant={variant} ===")

    t0 = time.time()
    image_map, pi_count = enumerate_image(n, max_c,
                                          time_budget_sec=time_budget_sec * 0.3)
    t1 = time.time()
    print(f"Enumerated {pi_count} pi's in {t1 - t0:.2f}s; "
          f"distinct pi^hw = {len(image_map)}")

    if variant == 'chain':
        test_fn = candidate3_chain_test
    elif variant == 'carry':
        test_fn = candidate3_carry_test
    else:
        raise ValueError(variant)

    fp_list = []  # predicted, not observed
    fn_list = []  # observed, not predicted
    total_pairs_tested = 0
    max_word_len = 0

    hw_keys = sorted(image_map.keys(),
                     key=lambda k: (sum(k[0]) + sum(k[1]) + sum(k[2]) + k[3], k))
    for hw_key in hw_keys:
        if time.time() - t0 > time_budget_sec:
            print(f"  Stage 2 time budget exceeded.")
            break
        M_hw, B_hw, T_hw, S_hw = hw_key
        observed = image_map[hw_key]
        max_L = max(len(R) for R in observed)
        max_word_len = max(max_word_len, max_L)

        predicted = set()
        word_budget = 0
        for w in all_words_up_to(max_L, sigma):
            word_budget += 1
            total_pairs_tested += 1
            if test_fn(M_hw, B_hw, T_hw, S_hw, list(w), n):
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
    print(f"Max word length: {max_word_len}")
    print(f"Test elapsed: {t2 - t0:.2f}s")
    print()
    print(f"#FP (predicted, not observed): {len(fp_list)}")
    for hw_key, w in fp_list[:8]:
        print(f"  pi^hw = (M={hw_key[0]}, B={hw_key[1]}, T={hw_key[2]}, S={hw_key[3]})")
        print(f"    extra word: {w}")
    print()
    print(f"#FN (observed, not predicted): {len(fn_list)}")
    for hw_key, w in fn_list[:8]:
        print(f"  pi^hw = (M={hw_key[0]}, B={hw_key[1]}, T={hw_key[2]}, S={hw_key[3]})")
        print(f"    missing word: {w}")
    print()
    if not fp_list and not fn_list:
        verdict = "CONFIRMED"
    elif fp_list and not fn_list:
        verdict = "FALSIFIED-too-loose"
    elif fn_list and not fp_list:
        verdict = "FALSIFIED-too-strict"
    else:
        verdict = "FALSIFIED-both"
    print(f"VERDICT [{variant}]: {verdict}")
    return fp_list, fn_list, verdict


if __name__ == '__main__':
    # Stage A: B_3, max_c = 5, chain variant.
    print(f"\n{'='*72}\nStage A: B_3, max_c=5, CHAIN variant\n{'='*72}\n")
    t_a = time.time()
    fpA, fnA, vA = run_experiment(3, 5, time_budget_sec=270, variant='chain')
    print(f"Stage A elapsed: {time.time() - t_a:.1f}s")

    # Stage B: B_3, max_c = 5, carry variant.
    print(f"\n{'='*72}\nStage B: B_3, max_c=5, CARRY variant\n{'='*72}\n")
    t_b = time.time()
    fpB, fnB, vB = run_experiment(3, 5, time_budget_sec=270, variant='carry')
    print(f"Stage B elapsed: {time.time() - t_b:.1f}s")

    print(f"\n{'='*72}")
    print(f"Summary:")
    print(f"  Stage A (chain):  {vA}  #FP={len(fpA)}  #FN={len(fnA)}")
    print(f"  Stage B (carry):  {vB}  #FP={len(fpB)}  #FN={len(fnB)}")
    print(f"{'='*72}")

    # Stage C: if either confirms at max_c=5, push to max_c=7.
    best_variant = None
    if vA == 'CONFIRMED':
        best_variant = 'chain'
    elif vB == 'CONFIRMED':
        best_variant = 'carry'
    if best_variant is not None:
        print(f"\n{'='*72}\nStage C: B_3, max_c=7, {best_variant} variant\n{'='*72}\n")
        t_c = time.time()
        fpC, fnC, vC = run_experiment(3, 7, time_budget_sec=540,
                                      variant=best_variant)
        print(f"Stage C elapsed: {time.time() - t_c:.1f}s")
        print(f"Stage C verdict ({best_variant}, max_c=7): {vC}  "
              f"#FP={len(fpC)}  #FN={len(fnC)}")
