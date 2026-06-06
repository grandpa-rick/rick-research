"""
test_multiplicity.py — verify the BDIqLR multiplicity formula against direct
enumeration of B_n-highest Kostant partitions.

For each B_n-weight nu of bounded magnitude:
  (a) Direct: enumerate KPs of total content <= MAX (MAX chosen large enough
      so that direct count saturates).
  (b) Chain: total_Bn_highest_count(nu_chains, nu_n, n).
Verify agreement.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from bdi_qLR import total_Bn_highest_count
from collections import Counter


def direct_buckets_B3(MAX):
    """Bucket KPs at B_3 by weight, count B_3-highest in each bucket."""
    import b_i_b3 as B3
    bucket = Counter()
    for pi in B3.enumerate_partitions(MAX):
        E1 = pi.get('e1', 0) + pi.get('e1-e2', 0) + pi.get('e1-e3', 0) + pi.get('e1+e2', 0) + pi.get('e1+e3', 0)
        E2 = pi.get('e2', 0) - pi.get('e1-e2', 0) + pi.get('e2-e3', 0) + pi.get('e1+e2', 0) + pi.get('e2+e3', 0)
        E3 = pi.get('e3', 0) - pi.get('e1-e3', 0) - pi.get('e2-e3', 0) + pi.get('e1+e3', 0) + pi.get('e2+e3', 0)
        weight = (E1, E2, E3)
        if B3.eps_i(pi, 3) == 0:
            bucket[weight] += 1
    return bucket


def direct_buckets_B4(MAX):
    """Bucket KPs at B_4 by weight, count B_4-highest in each bucket."""
    import b_i_b4 as B4
    bucket = Counter()
    for pi in B4.enumerate_partitions(MAX):
        E1 = (pi.get('e1', 0) + pi.get('e1-e2', 0) + pi.get('e1-e3', 0) + pi.get('e1-e4', 0)
              + pi.get('e1+e2', 0) + pi.get('e1+e3', 0) + pi.get('e1+e4', 0))
        E2 = (pi.get('e2', 0) - pi.get('e1-e2', 0) + pi.get('e2-e3', 0) + pi.get('e2-e4', 0)
              + pi.get('e1+e2', 0) + pi.get('e2+e3', 0) + pi.get('e2+e4', 0))
        E3 = (pi.get('e3', 0) - pi.get('e1-e3', 0) - pi.get('e2-e3', 0) + pi.get('e3-e4', 0)
              + pi.get('e1+e3', 0) + pi.get('e2+e3', 0) + pi.get('e3+e4', 0))
        E4 = (pi.get('e4', 0) - pi.get('e1-e4', 0) - pi.get('e2-e4', 0) - pi.get('e3-e4', 0)
              + pi.get('e1+e4', 0) + pi.get('e2+e4', 0) + pi.get('e3+e4', 0))
        weight = (E1, E2, E3, E4)
        if B4.eps_i(pi, 4) == 0:
            bucket[weight] += 1
    return bucket


def saturated_b3_test(max_weight_l1=3, MAX_HI=14, MAX_LO=12):
    """Run B_3 test where direct count has saturated.

    A weight has 'saturated' count if direct@MAX_HI == direct@MAX_LO."""
    bucket_lo = direct_buckets_B3(MAX_LO)
    bucket_hi = direct_buckets_B3(MAX_HI)
    print(f"B_3 saturated test (weights with |w|_1 <= {max_weight_l1}, MAX_LO={MAX_LO}, MAX_HI={MAX_HI})")
    agree = 0; disagree = 0
    disagreements = []
    n_saturated = 0
    n_unsaturated = 0
    for w in sorted(bucket_hi):
        if sum(abs(x) for x in w) > max_weight_l1:
            continue
        if bucket_lo[w] != bucket_hi[w]:
            n_unsaturated += 1
            continue
        n_saturated += 1
        direct = bucket_hi[w]
        chain = total_Bn_highest_count([w[0], w[1]], w[2], 3)
        if direct == chain:
            agree += 1
        else:
            disagree += 1
            disagreements.append((w, direct, chain))
    print(f"  saturated weights: {n_saturated} (unsaturated: {n_unsaturated})")
    print(f"  agree: {agree}, disagree: {disagree}")
    for w, d, c in disagreements[:10]:
        print(f"    weight={w}: direct={d}, chain={c}")
    return disagree == 0


def saturated_b4_test(max_weight_l1=3, MAX_HI=10, MAX_LO=8):
    bucket_lo = direct_buckets_B4(MAX_LO)
    bucket_hi = direct_buckets_B4(MAX_HI)
    print(f"B_4 saturated test (weights with |w|_1 <= {max_weight_l1}, MAX_LO={MAX_LO}, MAX_HI={MAX_HI})")
    agree = 0; disagree = 0
    disagreements = []
    n_saturated = 0
    n_unsaturated = 0
    for w in sorted(bucket_hi):
        if sum(abs(x) for x in w) > max_weight_l1:
            continue
        if bucket_lo[w] != bucket_hi[w]:
            n_unsaturated += 1
            continue
        n_saturated += 1
        direct = bucket_hi[w]
        chain = total_Bn_highest_count([w[0], w[1], w[2]], w[3], 4)
        if direct == chain:
            agree += 1
        else:
            disagree += 1
            disagreements.append((w, direct, chain))
    print(f"  saturated weights: {n_saturated} (unsaturated: {n_unsaturated})")
    print(f"  agree: {agree}, disagree: {disagree}")
    for w, d, c in disagreements[:10]:
        print(f"    weight={w}: direct={d}, chain={c}")
    return disagree == 0


if __name__ == '__main__':
    print("=" * 72)
    print("BDIqLR multiplicity formula vs direct enumeration (saturated)")
    print("=" * 72)
    print()
    ok3 = saturated_b3_test()
    print()
    ok4 = saturated_b4_test()
    print()
    print("ALL TESTS PASSED" if (ok3 and ok4) else "SOME TESTS FAILED")
