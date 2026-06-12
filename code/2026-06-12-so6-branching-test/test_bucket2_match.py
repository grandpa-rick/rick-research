"""
Test: does any union of so_6 irreps (total dim 22) admit a basis change matching
Bucket-2 marginals {1,2,9,10}, {1,1,1,1,2,3,3,4,6}, {1,1,1,2,4,4,4,5}?

Strategy:
1. Enumerate so_6 irreps with dim ≤ 22 (cases: (0,0,0)=1, (1,0,0)=6, (1,1,1)=10,
   (1,1,-1)=10 [conjugate spinor pair under diagram involution σ_0], (1,1,0)=15,
   (2,0,0)=20). (1,1,1) and (1,1,-1) are distinct as SO(6) reps; we include both.
2. For each multiset decomposition of 22 into these dims, build the union weight
   multiset W (with the appropriate diagram-involution twist for (1,1,-1)).
3. For each W, enumerate linear functionals f = (a, b, c) with |coords| ≤ MAX and
   collect their level-count signatures. Check whether all three Bucket-2 marginal
   signatures appear (with linearly independent choices). If yes, candidate found.

Bucket-2 marginal signatures (sorted level-set count multisets):
  T_i2     = (1, 2, 9, 10)
  T_i236   = (1, 1, 1, 1, 2, 3, 3, 4, 6)
  T_i23456 = (1, 1, 1, 2, 4, 4, 4, 5)
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations_with_replacement, product

from so6_weights import so6_dim_from_weights, so6_weight_multiset

# ---------------------------------------------------------------------------
# Step 1: enumerate so_6 irreps with dim <= 22 (integer weights, including σ_0-conjugates).
# ---------------------------------------------------------------------------

BASE_IRREPS = [
    # (label, highest weight (l_1, l_2, l_3), dim)
    ("triv",     (0, 0, 0),  1),
    ("vec",      (1, 0, 0),  6),
    ("spin111",  (1, 1, 1),  10),
    ("spin11m1", (1, 1, -1), 10),  # σ_0-conjugate of spin111 (last coord flipped)
    ("adj",      (1, 1, 0),  15),
    ("sym2",     (2, 0, 0),  20),
]


def irrep_weight_multiset(label: str, hw: tuple[int, int, int]) -> Counter:
    """Return so_6 weight multiset for one of the BASE_IRREPS, handling σ_0-twist."""
    l1, l2, l3 = hw
    if l3 >= 0:
        return so6_weight_multiset(l1, l2, l3)
    # For l_3 < 0: apply σ_0 (flip last coord) to the +l_3 multiset.
    base = so6_weight_multiset(l1, l2, -l3)
    out: Counter = Counter()
    for w, m in base.items():
        out[(w[0], w[1], -w[2])] += m
    return out


# ---------------------------------------------------------------------------
# Step 2: enumerate decompositions of 22 into these dims (multisets, capped).
# ---------------------------------------------------------------------------

def decompositions_of_22(max_copies_each: int = 22) -> list[tuple[tuple[str, tuple[int, int, int], int], ...]]:
    """All decompositions of 22 into BASE_IRREPS, as unordered tuples of irrep entries."""
    dims = [(lab, hw, d) for (lab, hw, d) in BASE_IRREPS]
    # DFS over irreps in order; for each, choose count k >= 0.
    results: list[tuple] = []

    def recurse(idx: int, remaining: int, picked: list):
        if remaining == 0:
            results.append(tuple(picked))
            return
        if idx == len(dims):
            return
        lab, hw, d = dims[idx]
        max_k = min(max_copies_each, remaining // d)
        for k in range(max_k, -1, -1):
            picked_new = picked + [(lab, hw, d)] * k
            recurse(idx + 1, remaining - k * d, picked_new)

    recurse(0, 22, [])
    # Filter out trivially silly cases: more than 8 trivials makes the weight multiset
    # have huge mult at origin — still legal to check, but usually unhelpful.
    return results


# ---------------------------------------------------------------------------
# Step 3: For each W, search linear functionals for Bucket-2 marginals.
# ---------------------------------------------------------------------------

T_I2 = (1, 2, 9, 10)
T_I236 = (1, 1, 1, 1, 2, 3, 3, 4, 6)
T_I23456 = (1, 1, 1, 2, 4, 4, 4, 5)
TARGETS = {T_I2: "i_2", T_I236: "i_236", T_I23456: "i_23456"}


def union_weight_multiset(decomp: tuple) -> Counter:
    W: Counter = Counter()
    for (lab, hw, d) in decomp:
        for w, m in irrep_weight_multiset(lab, hw).items():
            W[w] += m
    return W


def level_signature(W: Counter, f: tuple[int, int, int]) -> tuple[int, ...]:
    """Sorted multiset of level-set counts for projection f."""
    hist: Counter = Counter()
    for w, m in W.items():
        v = f[0] * w[0] + f[1] * w[1] + f[2] * w[2]
        hist[v] += m
    return tuple(sorted(hist.values()))


def enumerate_functionals(max_coord: int) -> list[tuple[int, int, int]]:
    """Functionals f = (a, b, c) with max(|a|,|b|,|c|) ≤ max_coord, excluding (0,0,0)
    and one representative per ±-class (so f and -f counted once)."""
    out = []
    seen = set()
    for a, b, c in product(range(-max_coord, max_coord + 1), repeat=3):
        if (a, b, c) == (0, 0, 0):
            continue
        key = (a, b, c)
        neg = (-a, -b, -c)
        if neg in seen:
            continue
        seen.add(key)
        out.append((a, b, c))
    return out


def search_decomp(decomp: tuple, max_coord: int = 5) -> dict:
    """For a decomposition, find all functionals giving each target signature."""
    W = union_weight_multiset(decomp)
    if sum(W.values()) != 22:
        raise RuntimeError(f"unexpected total dim: {sum(W.values())} vs 22")
    fs = enumerate_functionals(max_coord)
    matches: dict[tuple, list] = {t: [] for t in TARGETS}
    for f in fs:
        sig = level_signature(W, f)
        for t in TARGETS:
            if sig == t:
                matches[t].append(f)
    return {"W": W, "matches": matches}


def linearly_independent_triple(fs1, fs2, fs3) -> tuple | None:
    """Find one (f1, f2, f3) one from each list with linearly independent f1, f2, f3."""
    def det(a, b, c):
        return (a[0] * (b[1] * c[2] - b[2] * c[1])
                - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0]))
    for f1 in fs1:
        for f2 in fs2:
            for f3 in fs3:
                if det(f1, f2, f3) != 0:
                    return (f1, f2, f3)
    return None


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main():
    decomps = decompositions_of_22()
    print(f"Enumerated {len(decomps)} decompositions of 22 into so_6 irreps.")
    print("Sample:")
    for d in decomps[:10]:
        labels = Counter(lab for (lab, hw, dd) in d)
        print(f"  {dict(labels)}")
    print("...")

    print()
    print("Searching for marginal-matches (|coord| <= 4):")
    print()
    any_full_match = False
    for decomp in decomps:
        result = search_decomp(decomp, max_coord=4)
        m = result["matches"]
        n_i2 = len(m[T_I2])
        n_i236 = len(m[T_I236])
        n_i23456 = len(m[T_I23456])
        if n_i2 > 0 or n_i236 > 0 or n_i23456 > 0:
            labels = Counter(lab for (lab, hw, dd) in decomp)
            print(f"  Decomp {dict(labels)}: i2={n_i2}, i236={n_i236}, i23456={n_i23456}")
            if n_i2 > 0 and n_i236 > 0 and n_i23456 > 0:
                triple = linearly_independent_triple(m[T_I2], m[T_I236], m[T_I23456])
                if triple:
                    print(f"    *** FULL MATCH (lin-indep): f_i2={triple[0]}, f_i236={triple[1]}, f_i23456={triple[2]}")
                    any_full_match = True
                else:
                    print(f"    PARTIAL MATCH on all 3 signatures, but no linearly independent triple.")

    print()
    if any_full_match:
        print(">>> CANDIDATE(S) FOUND. Proceed to Test 2 (8-vector restriction-operator check).")
    else:
        print(">>> NO MATCHES. OQ-NAITOSAGAKI-BDI is REFUTED at the marginal-pattern level.")


if __name__ == "__main__":
    main()
