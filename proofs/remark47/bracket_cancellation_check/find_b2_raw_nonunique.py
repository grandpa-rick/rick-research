"""
Find a B_2 RAW non-unique case explicitly, so we know what (pi, c, pi')
example to test against Kashiwara bracket cancellation.

Setup follows su1_phase_a_B2_C2.py.
"""

from collections import defaultdict
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from su1_phase_a_B2_C2 import (
    b2_subtypes_for_simple, b2_subtype_units,
    b2_subtype_donor_receiver, b2_donor_roots,
    enumerate_orbit_swap_multisets, apply_multiset,
    enumerate_pis, reduce_multiset, freeze_pi, freeze_multiset,
)


def find_examples(kind, i, max_pi_total=4, c_values=(1, 2, 3, 4, -1, -2, -3, -4)):
    """Find (pi, c, pi') with multiple RAW multisets but single REDUCED."""
    subtypes = b2_subtypes_for_simple(kind, i)
    donor_roots = b2_donor_roots(kind, i)

    def sr_units(st): return b2_subtype_units(kind, i, st)
    def sr_dr(st, c): return b2_subtype_donor_receiver(kind, i, st, c)

    pis = enumerate_pis(donor_roots, max_pi_total)

    examples = []
    for pi in pis:
        if sum(pi.values()) == 0:
            continue
        for c in c_values:
            multisets = enumerate_orbit_swap_multisets(pi, c, sr_units, sr_dr, subtypes)
            end_states = defaultdict(list)
            for M in multisets:
                epi = apply_multiset(pi, M, sr_dr)
                end_states[freeze_pi(epi)].append(M)
            for end_pi_frozen, ms_list in end_states.items():
                if len(ms_list) > 1:
                    # RAW non-unique. Verify REDUCED collapses.
                    reduced_set = set(freeze_multiset(reduce_multiset(M)) for M in ms_list)
                    if len(reduced_set) == 1:
                        examples.append({
                            'kind': kind, 'i': i,
                            'pi': pi, 'c': c,
                            'pi_prime': dict(end_pi_frozen),
                            'raw_multisets': ms_list,
                            'reduced': next(iter(reduced_set)),
                        })
    return examples


def print_example(ex):
    print(f"\nB_2 simple kind={ex['kind']} i={ex['i']}")
    print(f"  pi      = {ex['pi']}")
    print(f"  c       = {ex['c']}")
    print(f"  pi'     = {ex['pi_prime']}")
    print(f"  RAW multisets ({len(ex['raw_multisets'])}):")
    for M in ex['raw_multisets']:
        print(f"    {M}")
    print(f"  REDUCED = {dict(ex['reduced'])}")


if __name__ == "__main__":
    print("Searching for B_2 RAW non-unique examples at s_0 (long exchange)...")
    exs_s0 = find_examples('L', 0)
    print(f"Found {len(exs_s0)} examples at s_0.")
    if exs_s0:
        print_example(exs_s0[0])
        print_example(exs_s0[1] if len(exs_s0) > 1 else exs_s0[0])

    print("\nSearching for B_2 RAW non-unique examples at s_1 (short flip)...")
    exs_s1 = find_examples('S', 1)
    print(f"Found {len(exs_s1)} examples at s_1.")
    if exs_s1:
        print_example(exs_s1[0])
        print_example(exs_s1[1] if len(exs_s1) > 1 else exs_s1[0])
