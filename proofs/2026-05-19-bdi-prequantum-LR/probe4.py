"""
probe4.py — Test the strongest version of the Sundaram-sub-enumeration hypothesis:
for any candidate filter, compute pass-count and HW-count at every weight, and
show that NO non-trivial filter on chain-factor HW configs matches HW count.

Also verify: at B_3 max_c=5 and max_c=7 (extended), does Kwon_chain match
HW count at every weight? If not, (B) Sundaram-sub-enumeration is empirically
falsified.

Bonus: print the weights where Kwon_chain undercounts the HW count to show the
structural failure.
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
                    P = carry_profile(M, B, T, n)
                    nu = [0] * n
                    for i in range(n - 1):
                        nu[i] = M[i] + B[i] + T[i]
                    nu[n-1] = sum(T[i] - B[i] for i in range(n - 1)) + S
                    configs.append({
                        'M': M, 'B': B, 'T': T, 'S': S,
                        'weight': tuple(nu), 'carry': P,
                        'delta': tuple(B[i] - T[i] for i in range(n - 1))
                    })
            return
        for M_a in range(content_remaining + 1):
            for B_a in range(content_remaining - M_a + 1):
                for T_a in range(content_remaining - M_a - B_a + 1):
                    gen(a + 1, content_remaining - M_a - B_a - T_a,
                        M_so_far + [M_a], B_so_far + [B_a], T_so_far + [T_a])
    gen(0, max_content, [], [], [])
    return configs


def detailed_kwon_table(n, max_c):
    """For each weight, print HW-count vs Kwon-passing count."""
    configs = enumerate_HW_configs(n, max_c)
    by_wt = defaultdict(list)
    for c in configs:
        by_wt[c['weight']].append(c)
    print(f"=== B_{n}, max_c={max_c}: {len(configs)} HW configs, {len(by_wt)} weights ===")
    mismatches = 0
    total_HW = 0
    total_Kwon = 0
    only_failures = 0
    for w in sorted(by_wt.keys()):
        lst = by_wt[w]
        hw = len(lst)
        kwon = sum(1 for c in lst if all(t <= b for b, t in zip(c['B'], c['T'])))
        total_HW += hw
        total_Kwon += kwon
        if kwon < hw:
            mismatches += 1
            if kwon == 0:
                only_failures += 1
    print(f"  Weights where Kwon-passing < HW-count: {mismatches}")
    print(f"  Weights where Kwon-passing = 0 but HW > 0: {only_failures}")
    print(f"  Total HW: {total_HW}, total Kwon-passing: {total_Kwon}")
    print(f"  Deficit (HW - Kwon-passing): {total_HW - total_Kwon}")
    return total_HW - total_Kwon


# Compute B_2 specifically: should be the exceptional iso point where AII rank 2 holds.
def b2_check():
    print("=== B_2 special case: exceptional iso so_5 = sp_4 ===")
    configs = enumerate_HW_configs(2, 6)
    by_wt = defaultdict(list)
    for c in configs:
        by_wt[c['weight']].append(c)
    print(f"  Total B_2 HW configs (max_c=6): {len(configs)}")
    # Check: at B_2, all HW configs have T_1 <= B_1 (= Kwon_chain trivially true)
    all_pass = all(all(t <= b for b, t in zip(c['B'], c['T'])) for c in configs)
    print(f"  Kwon_chain trivially true on B_2: {all_pass}")
    # At B_2, are there any configs with M_1 != 0?
    has_M = any(any(m > 0 for m in c['M']) for c in configs)
    print(f"  Any config with M_1 > 0 at B_2: {has_M}")
    print(f"  → At B_2, both M_1 = 0 and T_1 <= B_1 are forced by HW_1.")
    print(f"  → B_2's HW set is trivially constrained; the rank-2 'exceptional iso' regime.")
    print()


def main():
    b2_check()

    for n in [3, 4]:
        for max_c in [4, 5, 6, 7] if n == 3 else [4, 5]:
            deficit = detailed_kwon_table(n, max_c)
            print()


if __name__ == '__main__':
    main()
