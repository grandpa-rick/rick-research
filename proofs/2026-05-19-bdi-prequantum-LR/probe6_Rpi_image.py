"""
probe6_Rpi_image.py — Test Candidate 1 ("carry-balance prefix inequality")
for the image of the descent-recording map R(pi).

Hypothesis to test:
  R in Sigma^* is in R(pi^hw) iff the "carry-non-negativity" condition holds:
  For every PREFIX R_{1:k} of R, the reverse-played intermediate state
  (M', B', T', S') starting from pi^hw has:
    (a) all chain coordinates >= 0
    (b) all carry values P_a >= 0 (where P_a = sum_{i<=a} 2*(B'_i - T'_i))
    (c) the forward descent of the reverse-played FULL state recovers R.

We enumerate at B_3 with max_c <= 5 (drop if too slow).

For each pi^hw observed, we enumerate ALL words in Sigma^* up to length
max{|R| : R observed for pi^hw}, test each against Candidate 1, and compare
the predicted set to the observed set.
"""

import sys
import time
from collections import defaultdict
from itertools import product

sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import (
    descent_recording, reconstruct, carry_profile,
    enumerate_chain_configs, is_Bn_highest,
)


# ----------------------------------------------------------------------------
# Alphabet
# ----------------------------------------------------------------------------

def alphabet(n):
    """Return the alphabet Sigma at type B_n:
      - ('Sing', 'sing')
      - ('MB', a) for a in {1, ..., n-1}
      - ('TM', a) for a in {1, ..., n-1}
    """
    letters = [('Sing', 'sing')]
    for a in range(1, n):
        letters.append(('MB', a))
        letters.append(('TM', a))
    return letters


# ----------------------------------------------------------------------------
# Reverse a single letter from current state (mirroring reconstruct's step)
# ----------------------------------------------------------------------------

def reverse_letter(state, letter):
    """Apply ONE letter in reverse: state is (M, B, T, S); letter = (step_type, factor).
    Returns new state.
    """
    M, B, T, S = state
    M = list(M); B = list(B); T = list(T)
    step_type, factor = letter
    if step_type == 'Sing':
        S += 1
    elif step_type == 'MB':
        a_idx = factor - 1
        M[a_idx] += 1
        B[a_idx] -= 1
    elif step_type == 'TM':
        a_idx = factor - 1
        T[a_idx] += 1
        M[a_idx] -= 1
    else:
        raise ValueError(f"unknown letter type {step_type}")
    return (tuple(M), tuple(B), tuple(T), S)


def coords_nonnegative(state):
    M, B, T, S = state
    if S < 0:
        return False
    for x in M + B + T:
        if x < 0:
            return False
    return True


def carry_nonnegative(state, n):
    M, B, T, S = state
    P = carry_profile(M, B, T, n)
    return all(p >= 0 for p in P)


# ----------------------------------------------------------------------------
# Candidate 1 test: reverse-play word from pi^hw and check prefixes
# ----------------------------------------------------------------------------

def candidate1_test(M_hw, B_hw, T_hw, S_hw, word, n):
    """Test whether `word` (a list of letters in Sigma) satisfies Candidate 1
    starting from (M_hw, B_hw, T_hw, S_hw).

    The reconstruct semantics replay in REVERSED order of the recording. So if
    R = (l_1, l_2, ..., l_L) was recorded by descent, then we recover pi by
    reversing l_L, l_{L-1}, ..., l_1 starting from pi^hw.

    A "prefix" R_{1:k} corresponds to the SUFFIX of the reverse-play. So we
    check the state after replaying letters l_L, l_{L-1}, ..., l_{k+1} (i.e.,
    the LAST L-k reverse-steps), for k = 0, 1, ..., L.

    Equivalently: define states reached during reverse-play
      state_0 = pi^hw
      state_j = reverse(state_{j-1}, l_{L-j+1})  for j = 1, ..., L
    state_L is the full reconstructed pi. state_{L-k} corresponds to "after
    reverse-playing R_{1:k}'s complementary part" — i.e., the state that
    would descend to record l_{L-k+1}, ..., l_L. The prefix condition states
    that EVERY state_j (j = 0, ..., L) must have nonneg coords and nonneg carry.

    Then forward-descent of state_L must recover the FULL word.
    """
    state = (M_hw, B_hw, T_hw, S_hw)
    if not coords_nonnegative(state) or not carry_nonnegative(state, n):
        return False
    # Replay letters in reverse order, checking at each step.
    for letter in reversed(word):
        state = reverse_letter(state, letter)
        if not coords_nonnegative(state):
            return False
        if not carry_nonnegative(state, n):
            return False
    # Now state should be the full reconstructed pi.
    M, B, T, S = state
    # Forward descent must recover the word.
    M_hw2, B_hw2, T_hw2, S_hw2, R = descent_recording(M, B, T, S, n)
    if R != word:
        return False
    if (M_hw2, B_hw2, T_hw2, S_hw2) != (M_hw, B_hw, T_hw, S_hw):
        return False
    return True


# ----------------------------------------------------------------------------
# Enumerate all words in Sigma^* up to given length
# ----------------------------------------------------------------------------

def all_words_up_to(L, sigma):
    """Yield all words (tuples of letters) of length 0, 1, ..., L."""
    yield ()
    for length in range(1, L + 1):
        for w in product(sigma, repeat=length):
            yield w


# ----------------------------------------------------------------------------
# Main experiment
# ----------------------------------------------------------------------------

def run_experiment(n, max_c, time_budget_sec=300):
    sigma = alphabet(n)
    print(f"=== B_{n}, max_c = {max_c}, |Sigma| = {len(sigma)} ===")
    print(f"Alphabet: {sigma}")

    t0 = time.time()

    # Step 1: enumerate ALL chain configs (M, B, T, S) with total content <= max_c,
    # compute pi^hw and R(pi) via descent_recording.
    # Group: image_map[pi^hw] = set of R observed.
    image_map = defaultdict(set)
    pi_count = 0
    for total_c in range(max_c + 1):
        # Enumerate all (M, B, T, S) with total = sum(M)+sum(B)+sum(T)+S = total_c.
        # We iterate via content tuples c = (c_1, ..., c_{n-1}) and S separately.
        for parts in product(range(max_c + 1), repeat=n - 1):
            if sum(parts) > max_c:
                continue
            for S in range(max_c - sum(parts) + 1):
                # Use enumerate_chain_configs which expects c (chain contents) and weight_n.
                # But we want ALL pi, so iterate over each (M_a, B_a, T_a) with M_a+B_a+T_a = parts[a].
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

    # Step 2: for each pi^hw, enumerate all words up to max length observed,
    # test Candidate 1, compare predicted vs observed.
    total_pairs_tested = 0
    discrepancies_PnO = []  # predicted but not observed
    discrepancies_OnP = []  # observed but not predicted
    max_word_len_global = 0
    max_chain_coord = 0

    hw_keys = sorted(image_map.keys(), key=lambda k: (sum(k[0]) + sum(k[1]) + sum(k[2]) + k[3], k))
    for hw_key in hw_keys:
        if time.time() - t0 > time_budget_sec:
            print(f"  Stage 2 time budget exceeded.")
            break
        M_hw, B_hw, T_hw, S_hw = hw_key
        observed = image_map[hw_key]
        max_L = max(len(R) for R in observed)
        max_word_len_global = max(max_word_len_global, max_L)
        for c in M_hw + B_hw + T_hw:
            max_chain_coord = max(max_chain_coord, c)
        max_chain_coord = max(max_chain_coord, S_hw)

        # Enumerate candidate words up to max_L (note: |Sigma|^max_L can grow).
        # For B_3, |Sigma| = 5; max_L up to ~6 -> 5^6 ~ 15625 words per pi^hw.
        # Cap |Sigma|^L total to avoid blowup.
        predicted = set()
        word_budget = 0
        for w in all_words_up_to(max_L, sigma):
            word_budget += 1
            total_pairs_tested += 1
            if candidate1_test(M_hw, B_hw, T_hw, S_hw, list(w), n):
                predicted.add(tuple(w))
            if word_budget > 200000:
                # Safety break per pi^hw
                break

        # Compare predicted vs observed
        PnO = predicted - observed
        OnP = observed - predicted
        if PnO:
            for w in sorted(PnO)[:3]:
                discrepancies_PnO.append((hw_key, w))
        if OnP:
            for w in sorted(OnP)[:3]:
                discrepancies_OnP.append((hw_key, w))

    t2 = time.time()
    print(f"Total candidate (pi^hw, word) pairs tested: {total_pairs_tested}")
    print(f"Max word length: {max_word_len_global}")
    print(f"Max chain coord (in pi^hw): {max_chain_coord}")
    print(f"Test elapsed: {t2 - t0:.2f}s")
    print()
    print(f"Discrepancies (predicted-but-not-observed): {len(discrepancies_PnO)} examples collected")
    for hw_key, w in discrepancies_PnO[:5]:
        print(f"  pi^hw = (M={hw_key[0]}, B={hw_key[1]}, T={hw_key[2]}, S={hw_key[3]})")
        print(f"    extra word: {w}")
    print()
    print(f"Discrepancies (observed-but-not-predicted): {len(discrepancies_OnP)} examples collected")
    for hw_key, w in discrepancies_OnP[:5]:
        print(f"  pi^hw = (M={hw_key[0]}, B={hw_key[1]}, T={hw_key[2]}, S={hw_key[3]})")
        print(f"    missing word: {w}")

    print()
    if not discrepancies_PnO and not discrepancies_OnP:
        print("VERDICT: CONFIRMED (no discrepancies)")
    else:
        print("VERDICT: FALSIFIED")
    print()
    return discrepancies_PnO, discrepancies_OnP, total_pairs_tested, max_word_len_global, max_chain_coord


if __name__ == '__main__':
    # Try B_3 with max_c = 5 first; fall back if time exceeded.
    for max_c in [5, 4, 3]:
        print(f"\n{'='*72}")
        print(f"Attempting B_3 with max_c = {max_c}")
        print(f"{'='*72}\n")
        t_start = time.time()
        try:
            PnO, OnP, n_pairs, max_L, max_cc = run_experiment(3, max_c, time_budget_sec=240)
            elapsed = time.time() - t_start
            print(f"\nFinished max_c={max_c} in {elapsed:.1f}s")
            break
        except KeyboardInterrupt:
            print(f"Interrupted at max_c={max_c}")
            continue
