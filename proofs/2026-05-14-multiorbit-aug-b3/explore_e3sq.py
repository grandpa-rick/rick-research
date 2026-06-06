"""
Explore what e_3^2(pi) does to pi at B_3.
For each pi on slice S_3 (eps_3 >= 2), compute e_3^2(pi) - pi as a multiset move,
and tabulate the distinct moves to see the pattern of e_3^2.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from b_i_b3 import (
    enumerate_partitions, eps_i, e_i_k, kp_clean, kp_repr,
    EM12, EM13, EM23, EP12, EP13, EP23, E1, E2, E3, ROOTS,
)
from collections import Counter, defaultdict


def diff(pi_new, pi_old):
    """Multi-set difference: pi_new - pi_old as (root, delta) tuples sorted."""
    d = {}
    for r in ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


def orbit_class(pi):
    has_A = pi.get(EP13, 0) > 0 or pi.get(EM13, 0) > 0
    has_B = pi.get(EP23, 0) > 0 or pi.get(EM23, 0) > 0
    if has_A and has_B: return 'AB'
    if has_A: return 'A'
    if has_B: return 'B'
    return 'neither'


def main():
    MAX = 5
    # For each pi on slice S_3, compute e_3^2(pi) - pi and tabulate.
    by_class = defaultdict(Counter)
    examples = defaultdict(list)
    for pi in enumerate_partitions(MAX):
        if eps_i(pi, 3) < 2:
            continue
        e2 = e_i_k(pi, 3, 2)
        if e2 is None:
            continue
        d = diff(e2, pi)
        cls = orbit_class(pi)
        by_class[cls][d] += 1
        if len(examples[(cls, d)]) < 2:
            examples[(cls, d)].append(pi)
    print(f"On-slice partitions (eps_3 >= 2, total content <= {MAX}): "
          f"{sum(sum(c.values()) for c in by_class.values())}")
    print()
    for cls in ['A', 'B', 'AB', 'neither']:
        print(f"=== Class {cls} ===")
        cnts = by_class[cls]
        print(f"  Total: {sum(cnts.values())}")
        for d, n in sorted(cnts.items(), key=lambda x: -x[1]):
            ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
            print(f"    {n:5d}  [{ds}]")
            exs = examples[(cls, d)]
            for pi in exs[:1]:
                print(f"           e.g. pi = {kp_repr(pi)}")
        print()


if __name__ == "__main__":
    main()
