"""
probe2.py — Drill into B_3 HW configs failing Kwon_chain (T_a > B_a for some a).
Goal: see if there's a natural pairing (= bijection / R-matrix) between
Kwon-passing and Kwon-failing configs, OR if the Kwon filter just cuts a
subset that doesn't biject naturally.

Also extend to B_4 and check pattern.

If the filter cuts a sub-collection that does NOT biject with anything natural,
Hypothesis (A) is supported (no pre-quantum-LR layer).
If the filter cuts a sub-collection that BIJECTS via chain-factor R-matrix to
another natural sub-collection (= the "Sundaram side" vs "Kwon side"), (B) wins.
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


def show_b3_kwon_failures(max_c):
    """Show the B_3 HW configs failing Kwon_chain, grouped by weight."""
    n = 3
    configs = enumerate_HW_configs(n, max_c)
    failing = [c for c in configs if any(t > b for b, t in zip(c['B'], c['T']))]
    passing = [c for c in configs if all(t <= b for b, t in zip(c['B'], c['T']))]
    print(f"B_3, max_c={max_c}: {len(configs)} HW configs total.")
    print(f"  Kwon-passing (T_a <= B_a for all a): {len(passing)}")
    print(f"  Kwon-failing (T_a > B_a for some a): {len(failing)}")
    print()

    # Group by weight
    pass_by_wt = defaultdict(list)
    fail_by_wt = defaultdict(list)
    for c in passing:
        pass_by_wt[c['weight']].append(c)
    for c in failing:
        fail_by_wt[c['weight']].append(c)

    print("Weights where Kwon-failing configs exist:")
    for w in sorted(fail_by_wt.keys()):
        p_count = len(pass_by_wt[w])
        f_count = len(fail_by_wt[w])
        print(f"  wt {w}: {p_count} passing, {f_count} failing (total {p_count+f_count})")
        for c in fail_by_wt[w]:
            print(f"    FAIL: M={c['M']} B={c['B']} T={c['T']} S={c['S']} delta={c['delta']} carry={c['carry']}")
        for c in pass_by_wt[w]:
            print(f"    PASS: M={c['M']} B={c['B']} T={c['T']} S={c['S']} delta={c['delta']} carry={c['carry']}")
        print()


def b4_kwon_summary(max_c):
    """At B_4, summarize Kwon-chain pass/fail counts."""
    n = 4
    configs = enumerate_HW_configs(n, max_c)
    failing = [c for c in configs if any(t > b for b, t in zip(c['B'], c['T']))]
    passing = [c for c in configs if all(t <= b for b, t in zip(c['B'], c['T']))]
    print(f"B_4, max_c={max_c}: {len(configs)} HW configs total.")
    print(f"  Kwon-passing: {len(passing)}")
    print(f"  Kwon-failing: {len(failing)} ({len(failing)/max(1,len(configs)):.3f})")

    # Group by weight: how many fail-weights have only failing configs (= no
    # passing companion)?
    pass_by_wt = defaultdict(list)
    fail_by_wt = defaultdict(list)
    for c in passing:
        pass_by_wt[c['weight']].append(c)
    for c in failing:
        fail_by_wt[c['weight']].append(c)

    weights_with_fails_only = [w for w in fail_by_wt if w not in pass_by_wt]
    weights_with_fails = list(fail_by_wt.keys())
    print(f"  Weights with Kwon-failing configs: {len(weights_with_fails)}")
    print(f"  Weights with ONLY failing configs (= subset isn't a sub-enumeration of HW): {len(weights_with_fails_only)}")
    print()


if __name__ == '__main__':
    show_b3_kwon_failures(4)
    print("=" * 72)
    b4_kwon_summary(4)
