"""
probe_b3.py — B_3 enumeration and candidate Cross-indicator fitting.

Truth: is_Bn_highest from bdi_qLR.py. The forward-carry characterization gives:
  HW iff for each chain a:  M_a <= P_{a-1}  AND  M_a <= P_a  AND  S <= P_{n-1}
where P_a = sum_{b<=a} 2(B_b - T_b) is the CUMULATIVE carry.

The PROVE uses dP_a := 2(B_a - T_a) per-chain.  In its notation, candidates from
the PROVE list translate (with cumulative P_a^{cum} = dP_1 + ... + dP_a) as:

  C1 (pointwise lift):       [S <= dP_1] AND [S <= dP_2]
  C2 (sum lift):             [S <= dP_1 + dP_2]                    = [S <= P_2^{cum}]
  C3 (cumulative-and lift):  [S <= dP_1] AND [S <= dP_1 + dP_2]    = [S <= min(dP_1, dP_1+dP_2)]
  C4 (min lift):             [S <= min(dP_1, dP_2)]
  C5 (max lift):             [S <= max(dP_1, dP_2)]

We test:
  (T-strict)  HW = chi_1(M_1,B_1,T_1) * chi_2(M_2,B_2,T_2) * Cross(dP_1,dP_2,S)
  (T-carry)   HW = chi_1(M_1,B_1,T_1) * chi_2(M_2,B_2,T_2;dP_1) * Cross(dP_2|dP_1, S)

i.e., whether the cross-chain singleton constraint depends only on (dP_1, dP_2, S).
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import is_Bn_highest

from itertools import product
from collections import defaultdict


def enumerate_b3(max_content):
    """All (M, B, T, S) at B_3 with M_1+B_1+T_1+M_2+B_2+T_2+S <= max_content."""
    out = []
    for tot in range(max_content + 1):
        # iterate composition into 7 nonneg ints
        for M1 in range(tot + 1):
            for B1 in range(tot - M1 + 1):
                for T1 in range(tot - M1 - B1 + 1):
                    for M2 in range(tot - M1 - B1 - T1 + 1):
                        for B2 in range(tot - M1 - B1 - T1 - M2 + 1):
                            for T2 in range(tot - M1 - B1 - T1 - M2 - B2 + 1):
                                S = tot - M1 - B1 - T1 - M2 - B2 - T2
                                out.append(((M1, M2), (B1, B2), (T1, T2), S))
    return out


def per_chain_inner_at_B3(M, B, T):
    """Per-chain inner conditions at B_3 in 'as-purely-per-chain-as-possible' form.

    Chain 1: M_1 = 0 and T_1 <= B_1 (carry-free; chain 1 sees P_0 = 0).
    Chain 2: WITHOUT carry input, we cannot give a purely per-chain condition that's
             sound. But the OBVIOUS necessary condition that doesn't need P_1 is...
             none. So strict per-chain chi_2 = 1.
    """
    M1, M2 = M; B1, B2 = B; T1, T2 = T
    chi1 = (M1 == 0) and (T1 <= B1)
    chi2 = True  # strict per-chain: no carry-free condition on (M_2, B_2, T_2)
    return chi1, chi2


def candidates_for_cross(M, B, T, S):
    """Evaluate each candidate Cross indicator. Note we feed in the FULL chain
    state because the PROVE's candidates are functions of (dP_1, dP_2, S).
    dP_a = 2(B_a - T_a) here."""
    B1, B2 = B; T1, T2 = T
    dP1 = 2 * (B1 - T1)
    dP2 = 2 * (B2 - T2)
    return {
        'C1_pointwise':  (S <= dP1) and (S <= dP2),
        'C2_sum':        (S <= dP1 + dP2),
        'C3_cumul':      (S <= dP1) and (S <= dP1 + dP2),
        'C4_min':        (S <= min(dP1, dP2)),
        'C5_max':        (S <= max(dP1, dP2)),
        # Strict cumulative carry test
        'TRUE_cum':      (S <= dP1 + dP2),
    }


def test_candidates(max_content):
    print(f"\n=== B_3 candidate fit, content <= {max_content} ===")
    configs = enumerate_b3(max_content)
    n_total = len(configs)
    n_hw = 0

    # Pre-aggregate
    stats = defaultdict(lambda: {'FP': 0, 'FN': 0, 'TP': 0, 'TN': 0})

    # For each config, compute truth, per-chain inner, and each candidate Cross
    fn_examples = defaultdict(list)
    fp_examples = defaultdict(list)

    for (M, B, T, S) in configs:
        truth = is_Bn_highest(M, B, T, S, 3)
        if truth:
            n_hw += 1

        chi1, chi2 = per_chain_inner_at_B3(M, B, T)
        per_chain_strict = chi1 and chi2  # strict (T-strict) inner part

        cands = candidates_for_cross(M, B, T, S)

        # For each candidate, predicted = chi1 AND chi2 AND cand
        for name, cval in cands.items():
            pred = per_chain_strict and cval
            if pred and not truth:
                stats[name]['FP'] += 1
                if len(fp_examples[name]) < 3:
                    fp_examples[name].append((M, B, T, S))
            elif (not pred) and truth:
                stats[name]['FN'] += 1
                if len(fn_examples[name]) < 3:
                    fn_examples[name].append((M, B, T, S))
            elif pred and truth:
                stats[name]['TP'] += 1
            else:
                stats[name]['TN'] += 1

    print(f"  Total configs: {n_total}, HW configs: {n_hw}")
    print(f"  Per-chain strict (chi_1 = [M_1=0, T_1<=B_1], chi_2 = True)")
    print()
    print(f"  {'Candidate':<20} {'FP':>5} {'FN':>5} {'TP':>5} {'TN':>5}")
    print(f"  {'-'*20} {'-'*5} {'-'*5} {'-'*5} {'-'*5}")
    for name, s in stats.items():
        print(f"  {name:<20} {s['FP']:>5} {s['FN']:>5} {s['TP']:>5} {s['TN']:>5}")

    print()
    for name in stats:
        if stats[name]['FP'] + stats[name]['FN'] == 0:
            print(f"  *** {name}: PERFECT FIT ***")

    # Show example FNs/FPs for the sum-lift candidate
    print()
    print("FN examples for C2_sum (TRUE HW but candidate says no):")
    for (M, B, T, S) in fn_examples['C2_sum']:
        dP1 = 2*(B[0]-T[0]); dP2 = 2*(B[1]-T[1])
        chi1, chi2 = per_chain_inner_at_B3(M, B, T)
        print(f"  M={M} B={B} T={T} S={S}: chi1={chi1}, chi2={chi2}, dP1={dP1}, dP2={dP2}, S<=dP1+dP2: {S <= dP1+dP2}")

    print()
    print("FP examples for C2_sum (NOT HW but candidate says yes):")
    for (M, B, T, S) in fp_examples['C2_sum']:
        dP1 = 2*(B[0]-T[0]); dP2 = 2*(B[1]-T[1])
        chi1, chi2 = per_chain_inner_at_B3(M, B, T)
        # which constraint fails?
        P0, P1, P2 = 0, 2*(B[0]-T[0]), 2*(B[0]-T[0])+2*(B[1]-T[1])
        fail = []
        if M[0] > P0: fail.append(f"M_1={M[0]}>P_0={P0}")
        if M[0] > P1: fail.append(f"M_1={M[0]}>P_1={P1}")
        if M[1] > P1: fail.append(f"M_2={M[1]}>P_1={P1}")
        if M[1] > P2: fail.append(f"M_2={M[1]}>P_2={P2}")
        if S > P2: fail.append(f"S={S}>P_2={P2}")
        print(f"  M={M} B={B} T={T} S={S}: chi1={chi1}, chi2={chi2}, fails: {fail}")


def test_strict_T_hypothesis(max_content):
    """Test: does HW factor as chi_1(M_1,B_1,T_1) * chi_2(M_2,B_2,T_2) * Cross(dP_1,dP_2,S)?

    This means: the truth value depends on (M_1,B_1,T_1), (M_2,B_2,T_2), (S) via
    a tensor-product structure. Equivalently, for two chain-2 states (M_2, B_2, T_2)
    and (M_2', B_2', T_2') with the same dP_2 = 2(B_2-T_2), and any S, if one is
    HW then the other is too (given chain-1 fixed).

    The minimal falsification: pick chain-1 fixed, find two chain-2 states with the
    same dP_2 such that one is HW and the other is not.

    Stronger falsification: chi_2 needs to depend on M_2 directly (via constraint
    M_2 <= P_1), which is NOT a function of (M_2, B_2, T_2) alone — it needs P_1
    (chain-1 dependent). So strict (T) MUST fail at B_3.
    """
    print(f"\n=== Strict-(T) falsification test, content <= {max_content} ===")
    configs = enumerate_b3(max_content)
    # Find chain-1 state and dP_2 such that two chain-2 states with same dP_2 differ in HW.
    # Index by (chain_1, dP_2, S) and check HW values across (M_2, B_2, T_2) with same dP_2.
    by_key = defaultdict(list)
    for (M, B, T, S) in configs:
        dP2 = 2 * (B[1] - T[1])
        chain1 = (M[0], B[0], T[0])
        key = (chain1, dP2, S)
        truth = is_Bn_highest(M, B, T, S, 3)
        by_key[key].append(((M[1], B[1], T[1]), truth))

    # Look for keys with inconsistent truth
    n_keys = 0
    n_inconsistent = 0
    examples = []
    for key, lst in by_key.items():
        if len(set(t for _, t in lst)) > 1:
            n_inconsistent += 1
            if len(examples) < 5:
                examples.append((key, lst))
        n_keys += 1
    print(f"  Total (chain1, dP_2, S) keys: {n_keys}, inconsistent: {n_inconsistent}")
    if examples:
        print("  Examples of inconsistency (T-strict broken):")
        for key, lst in examples:
            chain1, dP2, S = key
            print(f"    chain_1={chain1}, dP_2={dP2}, S={S}:")
            for (M2,B2,T2), t in lst:
                print(f"      chain_2=({M2},{B2},{T2}): HW={t}")
    return n_inconsistent == 0


def test_carry_recursive_T(max_content):
    """Test: HW = (chain1 HW given P_0=0) * (chain2 HW given P_1) * [S <= P_2]
    with each piece evaluated using the carry. This MUST hold by construction
    of is_Bn_highest, but verify by direct comparison."""
    print(f"\n=== Carry-recursive-(T') verification, content <= {max_content} ===")
    configs = enumerate_b3(max_content)
    n_disagree = 0
    for (M, B, T, S) in configs:
        truth = is_Bn_highest(M, B, T, S, 3)
        # Compute carry-recursive prediction:
        P0 = 0
        # chi_1(M_1, B_1, T_1; P_0): M_1 <= P_0 AND M_1 <= P_0 + dP_1
        dP1 = 2*(B[0]-T[0])
        P1 = P0 + dP1
        chi1 = (M[0] <= P0) and (M[0] <= P1)
        dP2 = 2*(B[1]-T[1])
        P2 = P1 + dP2
        chi2 = (M[1] <= P1) and (M[1] <= P2)
        cross = (S <= P2)
        pred = chi1 and chi2 and cross
        if pred != truth:
            n_disagree += 1
            if n_disagree <= 3:
                print(f"  DISAGREE: M={M} B={B} T={T} S={S}: truth={truth}, pred={pred}")
    print(f"  Disagreements: {n_disagree} / {len(configs)}")
    return n_disagree == 0


if __name__ == '__main__':
    print("=" * 76)
    print("B_3 cross-chain term: candidate fitting + strict-(T) falsification")
    print("=" * 76)

    test_candidates(6)
    test_strict_T_hypothesis(6)
    test_carry_recursive_T(6)
