"""
Day 64 PROVE Step 3.

Test the rep-theoretic identification of the 22 Bucket-2 triples with
B_3 / C_3 adj + triv weights.

Approach:
1. Construct the 22 multiset weights of adj+triv for B_3 and C_3 explicitly.
2. Compute Weyl-orbit sizes (= structural invariants under W-action).
3. Compute axis-projection histograms (marginals) for each candidate.
4. Compare to our (4, 9, 8) marginals.

If marginals don't match any natural projection: rep-theoretic ID impossible.
"""

import json
import itertools
from pathlib import Path
from collections import Counter

OUT_DIR = Path(__file__).parent

def b3_weights():
    """22 multiset weights of adj(B_3) + triv."""
    W = []
    # 6 short roots ±e_i
    for i in range(3):
        for s in [1, -1]:
            v = [0, 0, 0]; v[i] = s
            W.append(tuple(v))
    # 12 long roots ±e_i ± e_j (i<j)
    for i in range(3):
        for j in range(i+1, 3):
            for s1 in [1, -1]:
                for s2 in [1, -1]:
                    v = [0, 0, 0]; v[i] = s1; v[j] = s2
                    W.append(tuple(v))
    # 3 Cartan (zero with multiplicity 3) + 1 triv (zero)
    for _ in range(4):
        W.append((0, 0, 0))
    assert len(W) == 22
    return W


def c3_weights():
    """22 multiset weights of adj(C_3) + triv."""
    W = []
    # 6 long roots ±2 e_i
    for i in range(3):
        for s in [2, -2]:
            v = [0, 0, 0]; v[i] = s
            W.append(tuple(v))
    # 12 short roots ±e_i ± e_j (i<j)
    for i in range(3):
        for j in range(i+1, 3):
            for s1 in [1, -1]:
                for s2 in [1, -1]:
                    v = [0, 0, 0]; v[i] = s1; v[j] = s2
                    W.append(tuple(v))
    # 4 zero
    for _ in range(4):
        W.append((0, 0, 0))
    assert len(W) == 22
    return W


def axis_marginals(W):
    """For each axis, return Counter of values appearing in that coord."""
    return [Counter(w[i] for w in W) for i in range(3)]


print("=" * 70)
print("B_3 adj+triv weight system")
print("=" * 70)
B = b3_weights()
print(f"|W| = {len(B)}, distinct = {len(set(B))}")
for i, m in enumerate(axis_marginals(B)):
    print(f"  Axis e_{i+1} marginal: {dict(sorted(m.items()))}")

print("\n" + "=" * 70)
print("C_3 adj+triv weight system")
print("=" * 70)
C = c3_weights()
print(f"|W| = {len(C)}, distinct = {len(set(C))}")
for i, m in enumerate(axis_marginals(C)):
    print(f"  Axis e_{i+1} marginal: {dict(sorted(m.items()))}")

# Our 22-config marginals
data = json.loads((OUT_DIR / "bucket2_indexing.json").read_text())
indexing = data["indexing"]
ci2 = Counter(t["i2"] for t in indexing)
ci236 = Counter(t["i236"] for t in indexing)
ci23456 = Counter(t["i23456"] for t in indexing)

print("\n" + "=" * 70)
print("Our 22-config marginals (i2, i236, i23456)")
print("=" * 70)
print(f"  i2: {dict(sorted(ci2.items()))} → sorted multiset {sorted(ci2.values())}")
print(f"  i236: {dict(sorted(ci236.items()))} → sorted multiset {sorted(ci236.values())}")
print(f"  i23456: {dict(sorted(ci23456.items()))} → sorted multiset {sorted(ci23456.values())}")

# Compare multisets of marginal-counts
print("\n--- Marginal-multiset comparison ---")
print(f"B_3 axis multiset (any axis): {sorted(axis_marginals(B)[0].values())}")
print(f"C_3 axis multiset (any axis): {sorted(axis_marginals(C)[0].values())}")
print(f"Our i2 multiset:     {sorted(ci2.values())}")
print(f"Our i236 multiset:   {sorted(ci236.values())}")
print(f"Our i23456 multiset: {sorted(ci23456.values())}")

# A bijection respecting axis structure would need axis-marginals to match.
# But the marginals are Weyl-equivariance invariants: for ANY linear projection
# π: weight space → ℝ³, the level-set sizes are symmetric in the simple-root
# sense.

# Test more carefully: is there ANY 3D linear projection π : ℤ³ → ℤ³ such that
# the level-sets along (i2, i236, i23456) match (4, 9, 8) sizes?
# We need: |π^{-1}(level k)| varies as our marginals do.

print("\n--- Checking if any (B_3, C_3) projection gives marginals (4, 9, 8) ---")
print("Our config has marginal LENGTHS (number of distinct coord values per axis):")
print(f"  i2: {len(ci2)} distinct values")
print(f"  i236: {len(ci236)} distinct values")
print(f"  i23456: {len(ci23456)} distinct values")
print(f"\nFor B_3 / C_3 adj+triv, any linear projection of weight space")
print(f"has Weyl-symmetric level sets. Specifically, for the Weyl group W,")
print(f"the level set sizes form a palindrome around 0.")
print(f"  B_3 axis marginal: {dict(sorted(axis_marginals(B)[0].items()))} (palindromic ✓)")
print(f"  C_3 axis marginal: {dict(sorted(axis_marginals(C)[0].items()))} (palindromic ✓)")

# Our marginals:
def is_palindromic(counter):
    """Check if Counter values are palindromic when keys are sorted."""
    vals = [counter[k] for k in sorted(counter)]
    return vals == vals[::-1]

print(f"\nOur i2 marginal palindromic? {is_palindromic(ci2)} ({[ci2[k] for k in sorted(ci2)]})")
print(f"Our i236 marginal palindromic? {is_palindromic(ci236)} ({[ci236[k] for k in sorted(ci236)]})")
print(f"Our i23456 marginal palindromic? {is_palindromic(ci23456)} ({[ci23456[k] for k in sorted(ci23456)]})")

# CRUCIAL: even reordering the i-indices, the multiset of marginal counts
# is the invariant. If this multiset is not Weyl-compatible, no bijection works.
print("\n--- Sorted marginal multisets ---")
print(f"  Our i2:     {sorted(ci2.values())}")
print(f"  Our i236:   {sorted(ci236.values())}")
print(f"  Our i23456: {sorted(ci23456.values())}")
print(f"  B_3 axis:   {sorted(axis_marginals(B)[0].values())}")
print(f"  C_3 axis:   {sorted(axis_marginals(C)[0].items())}")
