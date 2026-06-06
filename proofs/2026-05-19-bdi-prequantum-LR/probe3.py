"""
probe3.py — Systematic search for ANY natural filter on chain-factor HW configs
that gives a sub-enumeration matching the HW count at every weight.

Strategy: try a wide list of candidate filters; for each, count failures at
weights where HW > 0 and filter-pass = 0. If ANY filter gives matching counts
at every weight (i.e., it's "always true"), it's trivial. If ANY filter gives
counts < HW at some weights, it's NOT a Sundaram-like sub-enumeration.

The intent: confirm there's no natural pre-quantum-LR filter on BDI HW.
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


def chain_index_of_failure(cfg):
    """Return list of chain indices (0-based) where T_a > B_a."""
    return [i for i in range(len(cfg['B'])) if cfg['T'][i] > cfg['B'][i]]


def main():
    for n in [3, 4]:
        max_c = 5 if n == 3 else 4
        configs = enumerate_HW_configs(n, max_c)
        print(f"=== B_{n}, max_c={max_c}: {len(configs)} HW configs ===")

        # Group by weight
        by_wt = defaultdict(list)
        for c in configs:
            by_wt[c['weight']].append(c)

        # For each candidate filter, count number of HW configs filter-passes,
        # and count weights where filter-pass < HW-count (sub-enumeration fail).
        def Kwon_chain(c):
            return all(t <= b for b, t in zip(c['B'], c['T']))

        def Kwon_strict(c):
            return all(t < b or (t == 0 and b == 0) for b, t in zip(c['B'], c['T']))

        def M_zero(c):
            return all(m == 0 for m in c['M'])

        def carry_grows(c):
            # Strict growth of P_a (King-style)
            P = c['carry']
            return all(P[i+1] > P[i] for i in range(len(P)-1) if P[i] < 2*(len(P)-1-i))

        def carry_at_least_2a(c):
            # P_a >= 2a for a >= 1 (so chain factor a has at least 2a carry)
            P = c['carry']
            return all(P[a] >= 2*a for a in range(1, len(P)))

        def B_dominates_T_total(c):
            return sum(c['B']) >= sum(c['T'])

        def B_strictly_dominates(c):
            return sum(c['B']) > sum(c['T'])

        def total_balance(c):
            # sum B - sum T == S (= sum compensation)
            return sum(c['B']) - sum(c['T']) == c['S']

        def NTedness(c):
            # Filter: M_a is multiple of 2 (mod 2 condition like even-weight in AII)
            return all(m % 2 == 0 for m in c['M'])

        def even_M_even_T(c):
            return all(m % 2 == 0 for m in c['M']) and all(t % 2 == 0 for t in c['T'])

        def MB_dominates_TM(c):
            # On any DESCENT of nearby non-HW, MB > TM. But cfg is HW, this might
            # be reflected in T <= B (= Kwon_chain). Try: B_a > T_a for all a > 0.
            return all(t < b for b, t in zip(c['B'], c['T']))

        filters = [
            ('Kwon_chain', Kwon_chain),
            ('Kwon_strict', Kwon_strict),
            ('M_zero', M_zero),
            ('carry_at_least_2a', carry_at_least_2a),
            ('B_dominates_T_total', B_dominates_T_total),
            ('B_strictly_dominates', B_strictly_dominates),
            ('total_balance', total_balance),
            ('NTedness', NTedness),
            ('even_M_even_T', even_M_even_T),
            ('MB_dominates_TM', MB_dominates_TM),
        ]
        print(f"{'Filter':32s} {'Pass':>6s} {'Total':>6s} {'WtsBad':>7s} {'WtsZeroPass':>13s}")
        for name, f in filters:
            passing = [c for c in configs if f(c)]
            pass_by_wt = defaultdict(int)
            for c in passing:
                pass_by_wt[c['weight']] += 1
            # Weights where pass-count < hw-count (filter-sub-enumeration failure)
            bad_wts = [w for w, lst in by_wt.items() if pass_by_wt[w] < len(lst)]
            # Weights where pass-count = 0 but hw > 0
            zero_pass_wts = [w for w, lst in by_wt.items() if pass_by_wt[w] == 0 and len(lst) > 0]
            print(f"{name:32s} {len(passing):>6d} {len(configs):>6d} {len(bad_wts):>7d} {len(zero_pass_wts):>13d}")

        # Now check the converse: maybe Rick's HW set is a sub-enumeration of
        # some LARGER count. Try: count chain-factor configs WITHOUT HW filter.
        print()
        print("Total chain+sing configs (NO HW filter) per weight: NOT directly comparable")
        print("because that's just the Kostant-partition count, not a tableau class.")

        # Failures pattern: where does Kwon fail (which chain)?
        failures = [c for c in configs if not Kwon_chain(c)]
        chain_idx_count = defaultdict(int)
        for c in failures:
            for i in chain_index_of_failure(c):
                chain_idx_count[i] += 1
        print(f"\nKwon-failing configs: {len(failures)} total")
        print(f"  Chains where T_a > B_a:")
        for i in sorted(chain_idx_count.keys()):
            print(f"    chain {i+1}: {chain_idx_count[i]} times")

        # Weights with ONLY Kwon-failing configs
        only_fails = []
        for w, lst in by_wt.items():
            if all(not Kwon_chain(c) for c in lst):
                only_fails.append((w, lst))
        print(f"\n  Weights with ONLY Kwon-failing HW configs (count > 0):")
        for w, lst in sorted(only_fails)[:10]:
            print(f"    wt {w}: {len(lst)} configs, all Kwon-failing")
            for c in lst[:3]:
                print(f"      M={c['M']} B={c['B']} T={c['T']} S={c['S']}")

        print()


if __name__ == '__main__':
    main()
