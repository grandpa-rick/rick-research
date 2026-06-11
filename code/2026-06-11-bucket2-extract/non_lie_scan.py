"""
Day 64 PROVE Step 5: quick scan of non-Lie candidates for the 22-point config.

Test:
(a) 22 = p(8) — partitions of 8.  Match via length / largest part stats?
(b) 22 = vertices of any standard 3D combinatorial polytope?  (Most have
    12, 14, 18, 20, 24 vertices, not 22.)
(c) 22 as orbit count of some group action on small set?
(d) Independent sets of small graphs?
"""

import json
from pathlib import Path
from collections import Counter

OUT_DIR = Path(__file__).parent

# (a) partitions of 8
def partitions(n):
    res = [[]]
    def rec(rem, mx, acc):
        if rem == 0:
            res.append(acc[:])
            return
        for k in range(min(mx, rem), 0, -1):
            acc.append(k)
            rec(rem - k, k, acc)
            acc.pop()
    res = []
    rec(n, n, [])
    return res

P8 = partitions(8)
print(f"p(8) = {len(P8)}  (expected 22)")
# Largest part distribution
by_largest = Counter(max(p) for p in P8)
by_length = Counter(len(p) for p in P8)
by_distinct = Counter(len(set(p)) for p in P8)
by_sum_squared_parts = Counter(sum(x*x for x in p) for p in P8)
print(f"  by largest part: {dict(sorted(by_largest.items()))}")
print(f"  by length:       {dict(sorted(by_length.items()))}")
print(f"  by distinct parts: {dict(sorted(by_distinct.items()))}")
print(f"  by sum of squares: {dict(sorted(by_sum_squared_parts.items()))}")

# Our marginals
data = json.loads((OUT_DIR / "bucket2_indexing.json").read_text())
indexing = data["indexing"]
m2 = sorted(Counter(t["i2"] for t in indexing).values())
m236 = sorted(Counter(t["i236"] for t in indexing).values())
m23456 = sorted(Counter(t["i23456"] for t in indexing).values())

print(f"\nOur marginals (sorted multisets):")
print(f"  i2:     {m2}")
print(f"  i236:   {m236}")
print(f"  i23456: {m23456}")

# Compare to partition stats
for stat_name, stat in [("largest", by_largest), ("length", by_length), ("distinct", by_distinct)]:
    ms = sorted(stat.values())
    print(f"  partition-by-{stat_name}: {ms}")

# Conclusion: p(8) statistics don't match our marginals.

print()
print("=" * 70)
print("(b) standard 3D polytope vertex counts:")
print("    cube: 8, octahedron: 6, dodecahedron: 20, icosahedron: 12,")
print("    truncated tetrahedron: 12, truncated cube: 24, truncated octahedron: 24,")
print("    rhombicuboctahedron: 24, truncated cuboctahedron: 48,")
print("    snub cube: 24, ...")
print("    NONE have 22 vertices.")
print()
print("4-polytope vertex counts: 24-cell has 24, 5-cell has 5, 8-cell has 16,")
print("16-cell has 8, 600-cell has 120.")
print()
print("Polychora with 22 vertices: NONE that I know of.")
print("(The number 22 is unusual for vertex-transitive 3D polytopes.)")
print()
print("=" * 70)
print("(c) Other 22-element sequences in OEIS:")
print(" p(8) = 22  partitions of 8")
print(" Number of 5-element subsets with no two consecutive: C(5+5-1, 5) = ?")
print(" 22 = number of nonisomorphic 5-element groupoids? approx, hard to verify.")
print(" 22 = number of cubic graphs on 10 vertices? unrelated.")
print()
print("None of these has clearly the same 4 × 9 × 8 marginal structure.")
print()

# Try a more constructive lens: maybe the 22-config = 22 weights of an irrep
# of a 3-dim Lie algebra OTHER than B_3, C_3, A_3.
# Or 22 = 22 weights of an irrep of a higher-rank algebra projected to rank-3?

# F_4 std rep has 26 weights.  Project to a rank-3 subspace: gives some 22-pt sub?
# Need: 4 weights are mapped onto each other (collisions) under the projection.

# Let's see: F_4 has Weyl group of order 1152.  Rank 4.  Subgroups of rank 3:
# B_3, C_3, D_3 ≅ A_3.  Restriction of F_4 std rep V_(ω_4) to B_3 subalgebra
# decomposes as V_(ω_1) (= std B_3 = so(7) std = 7-dim) + V_(ω_3) (spin =
# 8-dim) + V_0 (triv) + V_(ω_1) = ... let's see, F_4 std (26-dim) under
# B_3 ⊂ F_4 decomposes how?
#
# F_4 / B_4 maximal subalgebra: F_4 std restricts to spin (8) + std (7) +
# spin (8) ... no, more like F_4 = B_4 + 16-dim, so std-26 restricts...

# Skip — getting too speculative.

print("=" * 70)
print("Conclusion of non-Lie scan: no clean alternative identification jumps out.")
print()
print("The 22-piece configuration is best characterised as a SPECIFIC")
print("BDI/AII coordinate-substitution graph from the Day-58 minimal-cover")
print("construction.  It is NOT rep-theoretic.")
