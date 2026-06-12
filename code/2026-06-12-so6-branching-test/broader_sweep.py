"""
Broader sweep: ℓ(λ) ≤ 6 and |λ| ≤ 10. Test whether any of these λ admit a
dim-22 sub-collection in Res^{gl_6}_{so_6} V_λ, and whether any such
sub-collection (across the broader range) admits Bucket-2 marginals.
"""

from __future__ import annotations

from collections import Counter

from cross_check import (
    all_so6_irreps_in_res, subcollections_summing_to, union_weights,
    signature_matches_any_bucket2,
)


def enumerate_partitions(max_size: int, max_rows: int):
    parts = []

    def recurse(prev: int, remaining: int, cur):
        if remaining == 0 or len(cur) == max_rows:
            parts.append(tuple(cur))
        if len(cur) == max_rows:
            return
        for v in range(min(prev, remaining), 0, -1):
            recurse(v, remaining - v, cur + [v])

    for n in range(0, max_size + 1):
        if n == 0:
            parts.append(())
            continue
        recurse(n, n, [])
    return parts


def main():
    partitions = enumerate_partitions(max_size=10, max_rows=6)
    print(f"Sweeping {len(partitions)} partitions ℓ(λ) ≤ 6, |λ| ≤ 10.")
    n_with_subcoll = 0
    n_hits = 0
    seen_subcoll_keys = set()
    for shape in partitions:
        irreps = all_so6_irreps_in_res(shape)
        subs = list(subcollections_summing_to(irreps, 22))
        if subs:
            n_with_subcoll += 1
        for sub in subs:
            key = tuple(sorted(sub.items()))
            if key in seen_subcoll_keys:
                continue
            seen_subcoll_keys.add(key)
            W = union_weights(sub)
            if sum(W.values()) != 22:
                continue
            hits = signature_matches_any_bucket2(W, max_coord=6)
            ihit = any(len(v) > 0 for v in hits.values())
            if ihit:
                n_hits += 1
                print(f"  λ = {shape}: sub-collection {sub} -- HIT: {hits}")

    print()
    print(f"# partitions admitting dim-22 sub-collections: {n_with_subcoll} / {len(partitions)}")
    print(f"# distinct dim-22 sub-collections: {len(seen_subcoll_keys)}")
    print(f"# of those with ANY Bucket-2 marginal hit: {n_hits}")

    if n_hits == 0:
        print(">>> NO HITS in broader sweep. Refutation extends to ℓ ≤ 6, |λ| ≤ 10.")


if __name__ == "__main__":
    main()
