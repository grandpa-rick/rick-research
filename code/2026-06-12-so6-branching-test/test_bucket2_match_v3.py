"""
Even wider search + direct gl_6 weight-multiset enumeration test.

Confirms: no union of so_6 irreps with total dim 22 yields any Bucket-2 marginal signature.
Also: for every gl_6 partition λ ⊂ (5^3), the so_6-restricted weight multiset of V_λ does
not match any Bucket-2 marginal as a prefix-axis or a basis-changed marginal.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

from so6_weights import gl4_weight_multiset, so6_weight_multiset
from test_bucket2_match import (
    BASE_IRREPS, T_I2, T_I236, T_I23456, TARGETS,
    decompositions_of_22, enumerate_functionals,
    irrep_weight_multiset, level_signature, union_weight_multiset,
)


# ---------------------------------------------------------------------------
# Wider search: functional coords up to ±10
# ---------------------------------------------------------------------------

def search_wide(max_coord=10):
    decomps = decompositions_of_22()
    print(f"\n=== WIDE SEARCH (max_coord={max_coord}) ===\n")
    found_any = False
    for decomp in decomps:
        labels = Counter(lab for (lab, hw, dd) in decomp)
        W = union_weight_multiset(decomp)
        fs = enumerate_functionals(max_coord)
        observed = set()
        for f in fs:
            sig = level_signature(W, f)
            observed.add(sig)
        for t, lab_t in TARGETS.items():
            if t in observed:
                print(f"  Decomp {dict(labels)} HIT {lab_t} = {t}")
                found_any = True
    if not found_any:
        print("  Still no matches.")
    return found_any


# ---------------------------------------------------------------------------
# Direct gl_6 weight multiset enumeration: enumerate all gl_6 partitions
# λ ⊂ (5^3), compute V_λ ↓ so_6 weight multiset, search marginals.
# ---------------------------------------------------------------------------

def gl6_ssyt_weights(shape: tuple[int, ...]) -> Counter:
    """gl_6 weight multiset of V_shape via SSYT enumeration in alphabet [6]."""
    from so6_weights import ssyt_shape
    cnt: Counter = Counter()
    for T in ssyt_shape(shape, 6):
        n = [0] * 6
        for row in T:
            for v in row:
                n[v - 1] += 1
        cnt[tuple(n)] += 1
    return cnt


def project_to_so6(gl6_weights: Counter) -> Counter:
    """Project gl_6 weight (n_1,...,n_6) to so_6 weight (n_1-n_6, n_2-n_5, n_3-n_4).

    This corresponds to the Cartan inclusion so_6 ⊂ gl_6 with so_6 acting on
    diagonals diag(a_1, a_2, a_3, -a_3, -a_2, -a_1).
    """
    out: Counter = Counter()
    for n, m in gl6_weights.items():
        w = (n[0] - n[5], n[1] - n[4], n[2] - n[3])
        out[w] += m
    return out


def enumerate_gl6_partitions_in_5_cubed() -> list[tuple[int, ...]]:
    parts = []
    for l1 in range(0, 6):
        for l2 in range(0, l1 + 1):
            for l3 in range(0, l2 + 1):
                shape = tuple(p for p in (l1, l2, l3) if p > 0)
                parts.append(shape)
    return parts


def gl6_direct_search(max_coord=6):
    print(f"\n=== DIRECT gl_6 SEARCH (max_coord={max_coord}) ===\n")
    parts = enumerate_gl6_partitions_in_5_cubed()
    print(f"Partitions λ ⊂ (5^3) (= ≤3 rows, parts ≤5): {len(parts)}")
    fs = enumerate_functionals(max_coord)
    found_any = False
    for shape in parts:
        gl6 = gl6_ssyt_weights(shape)
        so6 = project_to_so6(gl6)
        dim = sum(so6.values())
        if dim == 0:
            continue
        # We need marginal signature multisets summing to 22 to match Bucket-2.
        # Bucket-2 marginals sum to 22 each; so dim must be 22.
        if dim != 22:
            continue
        observed = set()
        for f in fs:
            sig = level_signature(so6, f)
            observed.add(sig)
        for t, lab_t in TARGETS.items():
            if t in observed:
                print(f"  Partition {shape} (dim {dim}) HIT {lab_t}")
                found_any = True
    if not found_any:
        print("  No gl_6 partition has dim exactly 22 (necessary for marginal-sum match).")
    return found_any


def gl6_dim_audit():
    print("\n=== gl_6 DIMENSION AUDIT for λ ⊂ (5^3) ===\n")
    parts = enumerate_gl6_partitions_in_5_cubed()
    dims_seen = []
    for shape in parts:
        gl6 = gl6_ssyt_weights(shape)
        d = sum(gl6.values())
        dims_seen.append((shape, d))
    # Find any with d == 22
    matches = [(s, d) for s, d in dims_seen if d == 22]
    print(f"  Partitions: {len(parts)}; dims: {sorted(set(d for _,d in dims_seen))[:20]} ...")
    print(f"  Partitions with dim exactly 22: {matches}")


def main():
    search_wide(max_coord=10)
    gl6_dim_audit()
    gl6_direct_search(max_coord=6)


if __name__ == "__main__":
    main()
