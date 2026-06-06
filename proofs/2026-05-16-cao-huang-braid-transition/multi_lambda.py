"""
Test the braid-transition matrix for multiple small lambdas to see
how the support structure scales.
"""

from braid_transition import (
    admissible_F, find_Fp_admissible, compute_braid_transition, weight_F
)
from collections import defaultdict, Counter

def analyze(m1, m2):
    print(f"\n=== lambda = {m1} omega_1 + {m2} omega_2 ===")
    F_adm = admissible_F(m1, m2)
    Fp_adm = find_Fp_admissible(m1, m2)
    M = compute_braid_transition(m1, m2, F_adm, Fp_adm)
    print(f"  dim L(lambda) = {len(F_adm)} = {len(Fp_adm)}")
    print(f"  |supp(M)| = {len(M)}")

    # Count rows
    by_ap = defaultdict(list)
    for (ap, a), c in M.items():
        by_ap[ap].append((a, c))
    trivial = sum(1 for entries in by_ap.values() if len(entries) == 1 and entries[0][1] == 1)
    non_trivial = len(by_ap) - trivial
    print(f"  Trivial (single coef-1) rows: {trivial}")
    print(f"  Non-trivial rows: {non_trivial}")

    # L1 distribution
    l1_dist = Counter()
    for (ap, a) in M.keys():
        d = tuple(ap[i] - a[i] for i in range(4))
        l1_dist[sum(abs(x) for x in d)] += 1
    print(f"  L1 norm distribution: {dict(sorted(l1_dist.items()))}")
    print(f"  # distinct L1 norms: {len(l1_dist)}")

    # Distinct delta vectors
    deltas = set()
    for (ap, a) in M.keys():
        d = tuple(ap[i] - a[i] for i in range(4))
        deltas.add(d)
    print(f"  # distinct delta vectors: {len(deltas)}")

    # Row shapes
    shape_counter = Counter()
    for ap, entries in by_ap.items():
        coefs = sorted([c for _, c in entries], key=lambda x: (-abs(x), -x))
        shape = (len(entries), tuple(str(c) for c in coefs))
        shape_counter[shape] += 1
    print(f"  Distinct row shapes: {len(shape_counter)}")
    for shape, count in sorted(shape_counter.items()):
        print(f"    {shape}: {count} rows")

    return M


for (m1, m2) in [(0, 1), (1, 0), (1, 1), (0, 2), (2, 0), (1, 2), (2, 1), (2, 2)]:
    analyze(m1, m2)
