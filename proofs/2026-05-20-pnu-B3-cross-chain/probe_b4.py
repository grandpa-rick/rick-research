"""
probe_b4.py — B_4 spot-check.

At B_4 the carry-recursive characterization predicts:
  HW iff for each a in {1,2,3}: M_a <= P_{a-1} AND M_a <= P_a
       AND S <= P_3 = sum_{a=1..3} 2(B_a - T_a).

We verify this against the direct CST eps_i.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')
from bdi_qLR import is_Bn_highest
import b_i_b4 as B4

from itertools import product


def enumerate_b4_chain(max_content):
    """Enumerate (M, B, T, S) at B_4 with chain+sing content <= max_content."""
    for tot in range(max_content + 1):
        # 10 nonneg ints: M_1,M_2,M_3,B_1,B_2,B_3,T_1,T_2,T_3,S summing to tot
        # 10-fold loop is feasible up to tot~6
        for parts in iter_compositions(tot, 10):
            M = (parts[0], parts[1], parts[2])
            B = (parts[3], parts[4], parts[5])
            T = (parts[6], parts[7], parts[8])
            S = parts[9]
            yield (M, B, T, S)


def iter_compositions(n, k):
    """Yield all weak compositions of n into k nonneg parts."""
    if k == 1:
        yield (n,)
        return
    for i in range(n + 1):
        for rest in iter_compositions(n - i, k - 1):
            yield (i,) + rest


def to_kp_b4(M, B, T, S):
    pi = {}
    for a_idx in range(3):
        a = a_idx + 1
        if M[a_idx]: pi[f'e{a}'] = M[a_idx]
        if B[a_idx]: pi[f'e{a}-e4'] = B[a_idx]
        if T[a_idx]: pi[f'e{a}+e4'] = T[a_idx]
    if S: pi['e4'] = S
    return pi


def check_b4(max_content):
    print(f"=== B_4 verification, chain+sing content <= {max_content} ===")
    n_total = 0
    n_agree_local = 0  # chain-test vs direct CST
    n_agree_carry = 0  # carry-recursive prediction vs direct CST
    n_agree_C2_sum = 0  # candidate C2_sum (after per-chain strict NULL chi_2,chi_3): NOT testing here, just truth.

    n_hw = 0
    examples_singleton_max = []  # configs where S = P_3 exactly

    disagree_local = []
    disagree_carry = []

    for (M, B, T, S) in enumerate_b4_chain(max_content):
        pi = to_kp_b4(M, B, T, S)
        truth = (B4.eps_i(pi, 4) == 0)
        if truth:
            n_hw += 1

        # Local chain test (from is_Bn_highest):
        local = is_Bn_highest(M, B, T, S, 4)
        if local == truth:
            n_agree_local += 1
        else:
            if len(disagree_local) < 3:
                disagree_local.append((M, B, T, S, local, truth))

        # Carry-recursive direct check (should match is_Bn_highest exactly)
        P0 = 0
        dP1 = 2*(B[0]-T[0]); P1 = P0 + dP1
        dP2 = 2*(B[1]-T[1]); P2 = P1 + dP2
        dP3 = 2*(B[2]-T[2]); P3 = P2 + dP3
        chi1 = (M[0] <= P0) and (M[0] <= P1)
        chi2 = (M[1] <= P1) and (M[1] <= P2)
        chi3 = (M[2] <= P2) and (M[2] <= P3)
        cross_sum = (S <= P3)
        carry_pred = chi1 and chi2 and chi3 and cross_sum
        if carry_pred == truth:
            n_agree_carry += 1
        else:
            if len(disagree_carry) < 3:
                disagree_carry.append((M, B, T, S, carry_pred, truth))

        # Configs where S = P_3 exactly (cross-chain saturation)
        if truth and S == P3 and S > 0 and len(examples_singleton_max) < 5:
            examples_singleton_max.append((M, B, T, S, P3))

        n_total += 1

    print(f"  Total: {n_total}, HW: {n_hw}")
    print(f"  Local chain test agrees with direct CST: {n_agree_local}/{n_total}")
    print(f"  Carry-recursive (chi_a + [S<=P_3]) agrees with direct: {n_agree_carry}/{n_total}")

    if disagree_local:
        print(f"  Local-test disagreements:")
        for M, B, T, S, mine, direct in disagree_local:
            print(f"    M={M} B={B} T={T} S={S}: local={mine}, direct={direct}")
    if disagree_carry:
        print(f"  Carry-recursive disagreements:")
        for M, B, T, S, mine, direct in disagree_carry:
            print(f"    M={M} B={B} T={T} S={S}: carry={mine}, direct={direct}")

    print()
    print(f"  Examples of singleton-saturating HW configs (S = P_3 > 0):")
    for M, B, T, S, P3 in examples_singleton_max:
        print(f"    M={M} B={B} T={T} S={S}: P_3 = {P3} (saturated)")


if __name__ == '__main__':
    print("=" * 70)
    print("B_4 spot-check: carry-recursive (T') prediction vs direct CST")
    print("=" * 70)
    # max_content = 5 gives manageable size; 6 starts being slow.
    check_b4(5)
