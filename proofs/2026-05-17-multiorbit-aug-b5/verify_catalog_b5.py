"""
Enumerate the catalog of e_5^2 net moves on the slice S_5 = {eps_5 >= 2} at B_5.

Each "net move" is the diff pi_new - pi_old (as a multiset of root multiplicity
changes) when applying e_5 twice on the slice. The prediction (3-strand braid):
  primitives of e_5 at the short simple = 2 per chain * 4 chains + 1 singleton = 9
  net moves of e_5^2 = unordered pairs with repetition = C(9+1, 2) = 45.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from collections import Counter
import b_i_b5 as B5


def diff_b5(pi_new, pi_old):
    d = {}
    for r in B5.ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


def main():
    print("=" * 70)
    print("B_5: catalog of e_5^2 net moves on slice S_5 (eps_5 >= 2)")
    print("=" * 70)
    seen = Counter()
    for MAX in [3, 4, 5]:
        seen_at = Counter()
        n_on_slice = 0
        for pi in B5.enumerate_partitions(MAX):
            if B5.eps_i(pi, 5) < 2:
                continue
            e2 = B5.e_i_k(pi, 5, 2)
            if e2 is None:
                continue
            n_on_slice += 1
            d = diff_b5(e2, pi)
            seen_at[d] += 1
        n_moves = len(seen_at)
        print(f"  max_total={MAX}: {n_on_slice} on-slice partitions, {n_moves} distinct net moves")
        seen.update(seen_at)
    print(f"\nTotal distinct net moves observed at B_5 i=5: {len(seen)}")
    print(f"Predicted: 45 (= C(9+1, 2) for 9 e_5-primitives)\n")
    for d, n in sorted(seen.items(), key=lambda x: -x[1]):
        ds = ', '.join(f"{c:+d}*{r}" for r, c in d)
        print(f"    [{ds}]  ({n} cases)")


if __name__ == "__main__":
    main()
