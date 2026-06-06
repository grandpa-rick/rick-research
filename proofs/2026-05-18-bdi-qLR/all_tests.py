"""
all_tests.py — comprehensive verification of BDIqLR algorithm at B_2, B_3, B_4.

Tests:
  1. Per-element B_n-highest test: chain-factor formula vs direct CST.
  2. Multiplicity formula: sum vs direct enumeration (saturated weights).
  3. Descent recording is bijective: reverse-play reconstructs input.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

import importlib
import bdi_qLR
importlib.reload(bdi_qLR)
from bdi_qLR import (is_Bn_highest, count_Bn_highest, total_Bn_highest_count,
                     descent_recording, reconstruct, enumerate_chain_configs)
from collections import Counter


# ============================================================================
# B_2: rank-2 anchor test
# ============================================================================

def test_b2():
    import b_i_b2 as B2
    print("=" * 50)
    print("B_2: rank-2 anchor")
    print("=" * 50)

    # B_2 chain coords: chain a=1 (M_1, B_1, T_1), sing S.
    # Map: M_1 = #beta_12 (= alpha_1+alpha_2 = E_1 = mid),
    #      B_1 = ??? B_2 has chain {beta_22 (bot), beta_12 (mid), gamma_12 (top)}
    # Wait — in B_2, the alpha_2 = E_2 chain at the short simple is:
    #   bot = beta_22 = e_2 (NO — beta_22 = alpha_2 = e_2; that's the simple itself, the SINGLETON not chain)
    # Hmm let me re-read b_i_b2.py:
    #   B11 = alpha_1 = e_1 - e_2 (long simple, MUST be E_1 - E_n type, here n=2, so E_1 - E_2 ✓)
    #   B12 = alpha_1 + alpha_2 = e_1 (chain mid of alpha_n = alpha_2)
    #   G12 = alpha_1 + 2 alpha_2 = e_1 + e_2 (chain top)
    #   B22 = alpha_2 = e_2 (singleton — alpha_n itself)
    # alpha_2-chain: {B11 (bot = e_1-e_2), B12 (mid = e_1), G12 (top = e_1+e_2)}
    # So chain a=1 at B_2:
    #   M_1 = #B12 (e_1, mid)
    #   B_1 = #B11 (e_1 - e_2, bot)
    #   T_1 = #G12 (e_1 + e_2, top)
    # Sing: S = #B22 (e_2)

    n_total = 0
    n_agree = 0
    n_disagree = 0
    disagreements = []
    for M1 in range(6):
        for B1 in range(6):
            for T1 in range(6):
                for S in range(6):
                    if M1+B1+T1+S > 5: continue
                    M = (M1,); B = (B1,); T = (T1,)
                    # Map to b_i_b2 Kp
                    pi = {}
                    if M1: pi['beta_12'] = M1
                    if B1: pi['beta_11'] = B1
                    if T1: pi['gamma_12'] = T1
                    if S: pi['beta_22'] = S
                    mine = is_Bn_highest(M, B, T, S, 2)
                    direct = (B2.eps_i(pi, 2) == 0)
                    n_total += 1
                    if mine == direct:
                        n_agree += 1
                    else:
                        n_disagree += 1
                        if len(disagreements) < 3:
                            disagreements.append((M, B, T, S, mine, direct))
    print(f"  per-element B_2-highest: {n_agree}/{n_total} agree, {n_disagree} disagree")
    for M, B, T, S, mine, direct in disagreements:
        print(f"    M={M} B={B} T={T} S={S}: chain={mine}, direct={direct}")

    # Test reconstruction at B_2
    ok = 0; fail = 0
    for M1 in range(5):
        for B1 in range(5):
            for T1 in range(5):
                for S in range(5):
                    if M1+B1+T1+S > 4: continue
                    M = (M1,); B = (B1,); T = (T1,)
                    M_hw, B_hw, T_hw, S_hw, R = descent_recording(M, B, T, S, 2)
                    M_r, B_r, T_r, S_r = reconstruct(M_hw, B_hw, T_hw, S_hw, R)
                    if (M_r, B_r, T_r, S_r) == (M, B, T, S):
                        ok += 1
                    else:
                        fail += 1
    print(f"  reconstruction: {ok} ok, {fail} fail")
    return n_disagree == 0 and fail == 0


def test_b3():
    import b_i_b3 as B3
    print("=" * 50)
    print("B_3")
    print("=" * 50)

    # Per-element test
    n_total = 0; n_agree = 0; n_disagree = 0
    for M1 in range(6):
      for B1 in range(6):
        for T1 in range(6):
          for M2 in range(6):
            for B2 in range(6):
              for T2 in range(6):
                for S in range(6):
                    if M1+B1+T1+M2+B2+T2+S > 5: continue
                    M = (M1, M2); B = (B1, B2); T = (T1, T2)
                    pi = {}
                    if M1: pi['e1'] = M1
                    if B1: pi['e1-e3'] = B1
                    if T1: pi['e1+e3'] = T1
                    if M2: pi['e2'] = M2
                    if B2: pi['e2-e3'] = B2
                    if T2: pi['e2+e3'] = T2
                    if S: pi['e3'] = S
                    mine = is_Bn_highest(M, B, T, S, 3)
                    direct = (B3.eps_i(pi, 3) == 0)
                    n_total += 1
                    n_agree += (mine == direct)
                    n_disagree += (mine != direct)
    print(f"  per-element B_3-highest: {n_agree}/{n_total} agree, {n_disagree} disagree")

    # Multiplicity test (saturated)
    bucket_hi = Counter(); bucket_lo = Counter()
    for MAX, bucket in [(12, bucket_lo), (14, bucket_hi)]:
        for pi in B3.enumerate_partitions(MAX):
            E1 = pi.get('e1', 0) + pi.get('e1-e2', 0) + pi.get('e1-e3', 0) + pi.get('e1+e2', 0) + pi.get('e1+e3', 0)
            E2 = pi.get('e2', 0) - pi.get('e1-e2', 0) + pi.get('e2-e3', 0) + pi.get('e1+e2', 0) + pi.get('e2+e3', 0)
            E3 = pi.get('e3', 0) - pi.get('e1-e3', 0) - pi.get('e2-e3', 0) + pi.get('e1+e3', 0) + pi.get('e2+e3', 0)
            w = (E1, E2, E3)
            if B3.eps_i(pi, 3) == 0:
                bucket[w] += 1
    m_agree = 0; m_disagree = 0; m_skip = 0
    for w in sorted(bucket_hi):
        if sum(abs(x) for x in w) > 3: continue
        if bucket_lo[w] != bucket_hi[w]:
            m_skip += 1; continue
        chain = total_Bn_highest_count([w[0], w[1]], w[2], 3)
        if bucket_hi[w] == chain: m_agree += 1
        else: m_disagree += 1
    print(f"  multiplicity (|w|_1 <= 3, saturated): {m_agree} agree, {m_disagree} disagree, {m_skip} skipped")

    # Reconstruction
    ok = 0; fail = 0
    for M1 in range(4):
      for B1 in range(4):
        for T1 in range(4):
          for M2 in range(4):
            for B2 in range(4):
              for T2 in range(4):
                for S in range(4):
                    if M1+B1+T1+M2+B2+T2+S > 5: continue
                    M = (M1, M2); B = (B1, B2); T = (T1, T2)
                    M_hw, B_hw, T_hw, S_hw, R = descent_recording(M, B, T, S, 3)
                    M_r, B_r, T_r, S_r = reconstruct(M_hw, B_hw, T_hw, S_hw, R)
                    if (M_r, B_r, T_r, S_r) == (M, B, T, S):
                        ok += 1
                    else:
                        fail += 1
    print(f"  reconstruction: {ok} ok, {fail} fail")
    return n_disagree == 0 and m_disagree == 0 and fail == 0


def test_b4():
    import b_i_b4 as B4
    print("=" * 50)
    print("B_4")
    print("=" * 50)

    # Per-element test (chain+sing only, NT excluded for speed)
    n_total = 0; n_agree = 0; n_disagree = 0
    for M1 in range(5):
      for M2 in range(5):
        for M3 in range(5):
          if M1+M2+M3 > 4: continue
          for B1 in range(5):
            for B2 in range(5):
              for B3 in range(5):
                if M1+M2+M3+B1+B2+B3 > 4: continue
                for T1 in range(5):
                  for T2 in range(5):
                    for T3 in range(5):
                      for S in range(5):
                        if M1+M2+M3+B1+B2+B3+T1+T2+T3+S > 4: continue
                        M = (M1, M2, M3); B = (B1, B2, B3); T = (T1, T2, T3)
                        pi = {}
                        for a, mm in enumerate(M):
                            if mm: pi[f'e{a+1}'] = mm
                        for a, bb in enumerate(B):
                            if bb: pi[f'e{a+1}-e4'] = bb
                        for a, tt in enumerate(T):
                            if tt: pi[f'e{a+1}+e4'] = tt
                        if S: pi['e4'] = S
                        mine = is_Bn_highest(M, B, T, S, 4)
                        direct = (B4.eps_i(pi, 4) == 0)
                        n_total += 1
                        n_agree += (mine == direct)
                        n_disagree += (mine != direct)
    print(f"  per-element B_4-highest (chain+sing only): {n_agree}/{n_total} agree, {n_disagree} disagree")

    # Multiplicity test (saturated)
    bucket_hi = Counter(); bucket_lo = Counter()
    for MAX, bucket in [(8, bucket_lo), (10, bucket_hi)]:
        for pi in B4.enumerate_partitions(MAX):
            E1 = (pi.get('e1', 0) + pi.get('e1-e2', 0) + pi.get('e1-e3', 0) + pi.get('e1-e4', 0)
                  + pi.get('e1+e2', 0) + pi.get('e1+e3', 0) + pi.get('e1+e4', 0))
            E2 = (pi.get('e2', 0) - pi.get('e1-e2', 0) + pi.get('e2-e3', 0) + pi.get('e2-e4', 0)
                  + pi.get('e1+e2', 0) + pi.get('e2+e3', 0) + pi.get('e2+e4', 0))
            E3 = (pi.get('e3', 0) - pi.get('e1-e3', 0) - pi.get('e2-e3', 0) + pi.get('e3-e4', 0)
                  + pi.get('e1+e3', 0) + pi.get('e2+e3', 0) + pi.get('e3+e4', 0))
            E4 = (pi.get('e4', 0) - pi.get('e1-e4', 0) - pi.get('e2-e4', 0) - pi.get('e3-e4', 0)
                  + pi.get('e1+e4', 0) + pi.get('e2+e4', 0) + pi.get('e3+e4', 0))
            w = (E1, E2, E3, E4)
            if B4.eps_i(pi, 4) == 0:
                bucket[w] += 1
    m_agree = 0; m_disagree = 0; m_skip = 0
    for w in sorted(bucket_hi):
        if sum(abs(x) for x in w) > 3: continue
        if bucket_lo[w] != bucket_hi[w]:
            m_skip += 1; continue
        chain = total_Bn_highest_count([w[0], w[1], w[2]], w[3], 4)
        if bucket_hi[w] == chain: m_agree += 1
        else: m_disagree += 1
    print(f"  multiplicity (|w|_1 <= 3, saturated): {m_agree} agree, {m_disagree} disagree, {m_skip} skipped")

    # Reconstruction
    ok = 0; fail = 0
    for M1 in range(5):
      for M2 in range(5):
        for M3 in range(5):
          if M1+M2+M3 > 4: continue
          for B1 in range(5):
            for B2 in range(5):
              for B3 in range(5):
                if M1+M2+M3+B1+B2+B3 > 4: continue
                for T1 in range(5):
                  for T2 in range(5):
                    for T3 in range(5):
                      for S in range(5):
                        if M1+M2+M3+B1+B2+B3+T1+T2+T3+S > 4: continue
                        M = (M1, M2, M3); B = (B1, B2, B3); T = (T1, T2, T3)
                        M_hw, B_hw, T_hw, S_hw, R = descent_recording(M, B, T, S, 4)
                        M_r, B_r, T_r, S_r = reconstruct(M_hw, B_hw, T_hw, S_hw, R)
                        if (M_r, B_r, T_r, S_r) == (M, B, T, S):
                            ok += 1
                        else:
                            fail += 1
    print(f"  reconstruction: {ok} ok, {fail} fail")

    return n_disagree == 0 and m_disagree == 0 and fail == 0


if __name__ == '__main__':
    print("=" * 70)
    print("BDIqLR — all tests at B_2, B_3, B_4")
    print("=" * 70)
    print()
    ok2 = test_b2()
    print()
    ok3 = test_b3()
    print()
    ok4 = test_b4()
    print()
    print("=" * 70)
    if ok2 and ok3 and ok4:
        print("ALL TESTS PASSED.")
    else:
        print(f"FAILURES: B_2={not ok2}, B_3={not ok3}, B_4={not ok4}")
    print("=" * 70)
