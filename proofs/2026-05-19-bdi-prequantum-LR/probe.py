"""
probe.py — Empirically probe the BDI HW set on B_2 and B_3 for any
"pre-quantum-LR" structure analogous to Azenhas's Sundaram/Kwon-companion bijection.

Day-24, Rick. Test (A) subsumption vs (B) finer asymmetric mirror.

Strategy:
1. Enumerate B_n-highest chain+sing configs at B_2 and B_3 up to small weight.
2. For each HW config, attempt to construct a candidate "BDI-Sundaram-tableau"
   and test candidate Sundaram-like properties.
3. Output: for each candidate property, count how many HW configs satisfy it
   vs total, and look for non-trivial splits with a Lie-theoretic name.
4. Verdict on (A) vs (B).
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import is_Bn_highest, carry_profile
from itertools import product
from collections import defaultdict


def enumerate_HW_configs(n, max_content):
    """Enumerate all chain+sing configs (M, B, T, S) at B_n with total
    chain+sing content <= max_content, returning only B_n-highest configs.

    Returns list of dicts {'M': M, 'B': B, 'T': T, 'S': S, 'weight': nu,
    'carry': P, 'content': c}."""
    configs = []
    # M, B, T are tuples of length n-1.
    # Total content = sum of all entries + S <= max_content.
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
                    c = sum(M[i] + B[i] + T[i] for i in range(n - 1)) + S
                    configs.append({
                        'M': M, 'B': B, 'T': T, 'S': S,
                        'weight': tuple(nu), 'carry': P, 'content': c,
                        'delta': tuple(B[i] - T[i] for i in range(n - 1))
                    })
            return
        # Choose (M_a, B_a, T_a) at chain a (a+1 in 1-indexed)
        for M_a in range(content_remaining + 1):
            for B_a in range(content_remaining - M_a + 1):
                for T_a in range(content_remaining - M_a - B_a + 1):
                    gen(a + 1, content_remaining - M_a - B_a - T_a,
                        M_so_far + [M_a], B_so_far + [B_a], T_so_far + [T_a])
    gen(0, max_content, [], [], [])
    return configs


def candidate_properties(cfg, n):
    """For a given HW config, evaluate candidate Sundaram-like properties.
    Returns dict {property_name: True/False}."""
    M = cfg['M']
    B = cfg['B']
    T = cfg['T']
    S = cfg['S']
    P = cfg['carry']
    Delta = cfg['delta']
    out = {}

    # Property 1: B_a >= T_a for ALL chains a (=> Delta_a >= 0).
    # Implied by HW_1 for a=1; not automatic for a >= 2.
    out['all_Delta_nonneg'] = all(d >= 0 for d in Delta)

    # Property 2: B_a > T_a for ALL chains a (strict).
    out['all_Delta_pos'] = all(d > 0 for d in Delta)

    # Property 3: King-symplectic-style. P_a >= 2*(a) for all 1 <= a <= n-1.
    out['King_carry'] = all(P[a] >= 2 * a for a in range(1, n))

    # Property 4: Carry monotone non-decreasing (Delta_a >= 0).
    # Same as all_Delta_nonneg, since P_a = P_{a-1} + 2*Delta_a.
    out['carry_monotone'] = all(P[a] >= P[a-1] for a in range(1, n))

    # Property 5: M_a = 0 for all a (mid-trivial).
    out['M_zero'] = all(m == 0 for m in M)

    # Property 6: T_a = 0 for all a (no tops).
    out['T_zero'] = all(t == 0 for t in T)

    # Property 7: Sundaram-style flag: row a has B_a + T_a >= some threshold.
    # E.g. B_a + T_a >= a (analog of King's i-th row starts at 2i-1 -> col-1
    # constraint).
    out['flag_a'] = all((B[a-1] + T[a-1]) >= a for a in range(1, n))

    # Property 8: Kwon-symplectic on chain factors. The chain factor C_a is
    # symplectic if T_a <= B_a (= Delta_a >= 0).
    out['Kwon_chain'] = all(t <= b for b, t in zip(B, T))

    # Property 9: S > 0 (non-trivial singleton).
    out['S_pos'] = S > 0

    # Property 10: S = 0.
    out['S_zero'] = S == 0

    # Property 11: Sundaram flag on right-companion-analog.
    # Suggested in Azenhas 2601: G(k, 1) >= 2k - 1 for the first column.
    # BDI analog: M_a + ... encoding "first column" of chain a.
    # Let's try B_a >= 2*a - 1.
    out['Sundaram_flag_strict'] = all(B[a-1] >= 2*a - 1 for a in range(1, n))

    # Property 12: pi^hw has any short-long edge content at all.
    out['any_short_long'] = any(B[a-1] + T[a-1] > 0 for a in range(n - 1)) or S > 0

    return out


def main():
    print("=" * 72)
    print("BDI pre-quantum-LR probe: B_2 and B_3")
    print("=" * 72)
    print()

    for n, max_c in [(2, 4), (3, 4)]:
        print(f"--- B_{n}, max content = {max_c} ---")
        configs = enumerate_HW_configs(n, max_c)
        print(f"Total HW configs: {len(configs)}")

        # Group by weight
        by_weight = defaultdict(list)
        for cfg in configs:
            by_weight[cfg['weight']].append(cfg)

        print(f"Distinct weights: {len(by_weight)}")

        # Candidate property counts
        property_counts = defaultdict(int)
        property_failing_configs = defaultdict(list)
        for cfg in configs:
            props = candidate_properties(cfg, n)
            for p, val in props.items():
                if val:
                    property_counts[p] += 1
                elif len(property_failing_configs[p]) < 3:
                    property_failing_configs[p].append(cfg)

        print(f"\nProperty satisfaction over {len(configs)} HW configs:")
        for p in sorted(property_counts.keys()):
            cnt = property_counts[p]
            print(f"  {p:30s}: {cnt}/{len(configs)} = {cnt/len(configs):.3f}")
            if 0 < cnt < len(configs):
                fail = property_failing_configs[p]
                print(f"    Example fails: M={fail[0]['M']} B={fail[0]['B']} T={fail[0]['T']} S={fail[0]['S']} (wt={fail[0]['weight']})")

        # Weight-by-weight HW counts (sample)
        print(f"\nHW counts by weight (first 15):")
        for w in sorted(by_weight.keys())[:15]:
            print(f"  wt {w}: {len(by_weight[w])}")
        print()


if __name__ == '__main__':
    main()
