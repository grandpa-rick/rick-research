"""
Verify the e_3^2 move catalog is stable at higher max_total.
Also check the B_2 analog to compare move counts.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from collections import Counter

import b_i_b3 as B3
import b_i_b2 as B2


CHAIN_A_B3 = (B3.EP13, B3.E1, B3.EM13)
CHAIN_B_B3 = (B3.EP23, B3.E2, B3.EM23)


def diff_b3(pi_new, pi_old):
    d = {}
    for r in B3.ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


def diff_b2(pi_new, pi_old):
    d = {}
    for r in B2.ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


def main():
    print("=" * 70)
    print("B_3: catalog of e_3^2 net moves on slice S_3 (eps_3 >= 2)")
    print("=" * 70)
    seen = Counter()
    for MAX in [4, 5, 6]:
        seen_at = Counter()
        for pi in B3.enumerate_partitions(MAX):
            if B3.eps_i(pi, 3) < 2:
                continue
            e2 = B3.e_i_k(pi, 3, 2)
            if e2 is None:
                continue
            d = diff_b3(e2, pi)
            seen_at[d] += 1
        n_partitions = sum(seen_at.values())
        n_moves = len(seen_at)
        print(f"  max_total={MAX}: {n_partitions} on-slice, {n_moves} distinct net moves")
        seen.update(seen_at)
    print(f"\nTotal distinct net moves observed at B_3 i=3: {len(seen)}")
    for d, n in sorted(seen.items(), key=lambda x: -x[1]):
        ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
        print(f"    [{ds}]")

    print()
    print("=" * 70)
    print("B_2: catalog of e_2^2 net moves on slice S_2 (eps_2 >= 2)")
    print("=" * 70)
    seen_b2 = Counter()
    for pi in B2.enumerate_partitions(6):
        if B2.eps_i(pi, 2) < 2:
            continue
        e2 = B2.e_i_k(pi, 2, 2)
        if e2 is None:
            continue
        d = diff_b2(e2, pi)
        seen_b2[d] += 1
    print(f"  max_total=6: {sum(seen_b2.values())} on-slice, {len(seen_b2)} distinct net moves")
    for d, n in sorted(seen_b2.items(), key=lambda x: -x[1]):
        ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
        print(f"    [{ds}]  ({n} cases)")


if __name__ == "__main__":
    main()
