"""
Refined exploration of e_3^2(pi) at B_3.

Classification by FULL chain support:
  Class A: pi has any of {EP13, E1, EM13} > 0, none of {EP23, E2, EM23}.
  Class B: symmetric.
  Class AB: both.
  Class neither: only {E3, EM12, EP12} possibly.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from b_i_b3 import (
    enumerate_partitions, eps_i, e_i_k, kp_clean, kp_repr,
    EM12, EM13, EM23, EP12, EP13, EP23, E1, E2, E3, ROOTS,
)
from collections import Counter, defaultdict


CHAIN_A = (EP13, E1, EM13)
CHAIN_B = (EP23, E2, EM23)


def diff(pi_new, pi_old):
    d = {}
    for r in ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


def chain_class(pi):
    has_A = any(pi.get(r, 0) > 0 for r in CHAIN_A)
    has_B = any(pi.get(r, 0) > 0 for r in CHAIN_B)
    if has_A and has_B: return 'AB'
    if has_A: return 'A'
    if has_B: return 'B'
    return 'neither'


def diff_chains(d):
    """Which chains does the move affect? Plus does it touch E3?"""
    touches_A = any(r in CHAIN_A for r, c in d)
    touches_B = any(r in CHAIN_B for r, c in d)
    touches_E3 = any(r == E3 for r, c in d)
    tag = []
    if touches_A: tag.append('A')
    if touches_B: tag.append('B')
    if touches_E3: tag.append('3')
    return ''.join(tag) if tag else 'none'


def main():
    MAX = 5
    by_cls = defaultdict(Counter)
    by_cls_movetag = defaultdict(Counter)
    examples = defaultdict(list)
    for pi in enumerate_partitions(MAX):
        if eps_i(pi, 3) < 2:
            continue
        e2 = e_i_k(pi, 3, 2)
        if e2 is None:
            continue
        d = diff(e2, pi)
        cls = chain_class(pi)
        by_cls[cls][d] += 1
        by_cls_movetag[cls][diff_chains(d)] += 1
        if len(examples[(cls, d)]) < 2:
            examples[(cls, d)].append(pi)
    total = sum(sum(c.values()) for c in by_cls.values())
    print(f"Total on-slice (eps_3 >= 2, max_total = {MAX}): {total}")
    print()
    for cls in ['A', 'B', 'AB', 'neither']:
        print(f"=== Class {cls} (chain-support) ===")
        cnts = by_cls[cls]
        n = sum(cnts.values())
        print(f"  Total: {n}")
        print(f"  Move-tag breakdown: {dict(by_cls_movetag[cls])}")
        for d, k in sorted(cnts.items(), key=lambda x: -x[1]):
            ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
            print(f"    {k:5d}  {diff_chains(d):>4}  [{ds}]")
        print()


if __name__ == "__main__":
    main()
