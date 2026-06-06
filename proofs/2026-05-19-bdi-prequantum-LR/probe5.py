"""
probe5.py — Final test: is there ANY tableau-class count equinumerous with
Rick's chain-factor HW count?

Candidates:
1. Sum over even-partition LR decompositions (Sp branching): for AII at rank n,
   count_LR(lambda, nu, mu_even). Not directly applicable at BDI iquantum.
2. Compare B_2 HW count to known Sp_4 branching at small weights.
3. Look for "shape" of HW count: is it polynomial in weight components?
   Does it match any classical formula?

The point: rule out the possibility that some external classical tableau class
matches Rick's HW count (=> (B) might hold via an external class).
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import is_Bn_highest, carry_profile
from collections import defaultdict


def enumerate_HW_configs(n, max_content):
    configs = []
    def gen(a, content_remaining, M_so_far, B_so_far, T_so_far):
        if a == n - 1:
            for S in range(content_remaining + 1):
                M, B, T = tuple(M_so_far), tuple(B_so_far), tuple(T_so_far)
                if is_Bn_highest(M, B, T, S, n):
                    nu = [0] * n
                    for i in range(n - 1):
                        nu[i] = M[i] + B[i] + T[i]
                    nu[n-1] = sum(T[i] - B[i] for i in range(n - 1)) + S
                    configs.append({'M': M, 'B': B, 'T': T, 'S': S, 'weight': tuple(nu)})
            return
        for M_a in range(content_remaining + 1):
            for B_a in range(content_remaining - M_a + 1):
                for T_a in range(content_remaining - M_a - B_a + 1):
                    gen(a + 1, content_remaining - M_a - B_a - T_a,
                        M_so_far + [M_a], B_so_far + [B_a], T_so_far + [T_a])
    gen(0, max_content, [], [], [])
    return configs


def b2_hw_counts(max_c):
    """B_2 HW counts. Compare with Sp_4 branching counts."""
    configs = enumerate_HW_configs(2, max_c)
    by_wt = defaultdict(int)
    for c in configs:
        by_wt[c['weight']] += 1
    print(f"B_2 HW counts (max_c={max_c}):")
    for w in sorted(by_wt.keys()):
        print(f"  wt {w}: {by_wt[w]}")
    print()
    return by_wt


def b3_hw_counts(max_c):
    """B_3 HW counts."""
    configs = enumerate_HW_configs(3, max_c)
    by_wt = defaultdict(int)
    for c in configs:
        by_wt[c['weight']] += 1
    print(f"B_3 HW counts (max_c={max_c}): {len(configs)} total")
    # Print weights where count > 1 (interesting cases)
    print(f"  Weights with count > 1:")
    for w in sorted(by_wt.keys()):
        if by_wt[w] > 1:
            print(f"    wt {w}: count = {by_wt[w]}")
    print()


# Compare with "naive" overcount: count chain-factor configs without HW filter
def naive_chain_count(n, max_c):
    """Count chain+sing configs (no HW filter) by weight."""
    by_wt = defaultdict(int)
    def gen(a, content_remaining, M_so_far, B_so_far, T_so_far):
        if a == n - 1:
            for S in range(content_remaining + 1):
                M, B, T = tuple(M_so_far), tuple(B_so_far), tuple(T_so_far)
                nu = [0] * n
                for i in range(n - 1):
                    nu[i] = M[i] + B[i] + T[i]
                nu[n-1] = sum(T[i] - B[i] for i in range(n - 1)) + S
                by_wt[tuple(nu)] += 1
            return
        for M_a in range(content_remaining + 1):
            for B_a in range(content_remaining - M_a + 1):
                for T_a in range(content_remaining - M_a - B_a + 1):
                    gen(a + 1, content_remaining - M_a - B_a - T_a,
                        M_so_far + [M_a], B_so_far + [B_a], T_so_far + [T_a])
    gen(0, max_c, [], [], [])
    return by_wt


def main():
    b2 = b2_hw_counts(6)
    b3_hw_counts(5)

    # Test: at B_3, compute B_3 HW counts at low weights and see if they match
    # any natural formula.
    print("--- B_3 HW counts at small weights ---")
    configs = enumerate_HW_configs(3, 6)
    by_wt = defaultdict(int)
    for c in configs:
        by_wt[c['weight']] += 1
    # Display in matrix-like form
    sample_weights = [(0,0,0), (1,0,0), (0,1,0), (1,1,0), (2,0,0), (0,2,0),
                      (1,1,1), (2,1,0), (1,2,0), (2,2,0), (3,0,0), (0,3,0)]
    for w in sample_weights:
        print(f"  wt {w}: HW count = {by_wt[w]}")
    print()

    # Comparison: at B_2, the HW count at wt (nu_1, nu_2) should equal the
    # multiplicity of Sp_4-irrep with HW labels for the chain content.
    # For Sp_4 = SO_5: V^Sp_4(a, b) has well-known dimensions.
    # B_2 chain-factor HW count at weight (nu_1, nu_2) is:
    print("--- B_2 HW counts as function of (nu_1, nu_2) ---")
    for nu1 in range(0, 5):
        for nu2 in range(-nu1, nu1 + 1):
            wt = (nu1, nu2)
            print(f"  wt ({nu1}, {nu2}): HW = {b2.get(wt, 0)}")


if __name__ == '__main__':
    main()
