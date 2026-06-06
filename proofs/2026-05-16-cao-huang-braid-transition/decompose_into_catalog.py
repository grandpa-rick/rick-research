"""
Test: do the 31 distinct delta vectors arise as integer linear combinations
of Rick's 6 catalog moves (interpreted in the natural F-tuple coords)?

Rick's 6 catalog moves at B_2 short simple, in PBW coords (c_1, c_2, c_3, c_4)
where c_1 = single (alpha_1), c_2 = top (2alpha_1+alpha_2), c_3 = mid
(alpha_1+alpha_2), c_4 = bot (alpha_2):
    D_MM   = (0, 0, -2, +2)    # (MB, MB)
    D_TT   = (0, -2, +2, 0)    # (TM, TM)
    D_MT   = (0, -1, 0, +1)    # (MB, TM)
    D_SS   = (-2, 0, 0, 0)     # (Sing, Sing)
    D_MS   = (-1, 0, -1, +1)   # (MB, Sing)
    D_TS   = (-1, -1, +1, 0)   # (TM, Sing)

These are 6 vectors in Z^4 spanning a sublattice.  Are the matrix's
31 delta vectors in F-tuple coords (after some natural coordinate change)
in this sublattice?
"""

import json
from collections import Counter
from fractions import Fraction
import os

HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, 'M_matrix.json')) as f:
    data = json.load(f)

M = {}
for entry in data['M_entries']:
    M[(tuple(entry['a_prime']), tuple(entry['a']))] = Fraction(entry['coef'])

# Rick's 6 catalog deltas in PBW coords (c_1, c_2, c_3, c_4)
catalog_deltas_PBW = {
    'MM': (0, 0, -2, +2),
    'TT': (0, -2, +2, 0),
    'MT': (0, -1, 0, +1),
    'SS': (-2, 0, 0, 0),
    'MS': (-1, 0, -1, +1),
    'TS': (-1, -1, +1, 0),
}

# Matrix delta vectors (F-tuple coords)
deltas_F_tuple = set()
for (ap, a) in M.keys():
    d = tuple(ap[i] - a[i] for i in range(4))
    deltas_F_tuple.add(d)

print(f"Distinct delta vectors (F-tuple coords): {len(deltas_F_tuple)}")
print(f"Rick's catalog moves (PBW coords): {len(catalog_deltas_PBW)}")
print()

# Span the catalog deltas as integer combinations
# These 6 vectors span a sublattice. Let's check the rank.
# Reduce via Hermite normal form, or just count: 4-dim Z-lattice with 6 generators.
# Smith normal form would tell us, but for our purposes, we just compute the
# Z-rank and see which 4-dim vectors are in the span.

# Convert to a Q-vector space first to find the Q-rank
def q_rank(vectors):
    mat = [[Fraction(x) for x in v] for v in vectors]
    # row-reduce
    n_rows = len(mat)
    n_cols = len(mat[0])
    r = 0
    for c in range(n_cols):
        if r >= n_rows:
            break
        pivot = None
        for i in range(r, n_rows):
            if mat[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        pv = mat[r][c]
        for j in range(n_cols):
            mat[r][j] /= pv
        for i in range(n_rows):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                for j in range(n_cols):
                    mat[i][j] -= f * mat[r][j]
        r += 1
    return r

vectors_catalog = list(catalog_deltas_PBW.values())
print(f"Q-rank of 6 catalog deltas: {q_rank(vectors_catalog)} (out of 4)")
# Likely 4. So the catalog deltas span all of Q^4. Trivially any delta in Q^4 is
# a Q-combination. The non-trivial question is whether the matrix's deltas are
# Z-combinations of the catalog deltas.

# To answer: compute the Smith normal form of the lattice spanned by the catalog
# in Z^4, and check which matrix deltas lie in it.

# Naive approach: enumerate integer combinations c_MM * D_MM + ... + c_TS * D_TS
# with |c_i| bounded, check which matrix deltas are hit.

import itertools
# Try small coefficients
hit = {}
catalog_names = list(catalog_deltas_PBW.keys())
catalog_vecs = list(catalog_deltas_PBW.values())
for coefs in itertools.product(range(-5, 6), repeat=6):
    v = [0, 0, 0, 0]
    for i, c in enumerate(coefs):
        for j in range(4):
            v[j] += c * catalog_vecs[i][j]
    v = tuple(v)
    if v in [tuple(d) for d in deltas_F_tuple]:
        # already-seen?
        if v not in hit or sum(abs(c) for c in coefs) < sum(abs(c) for c in hit[v]):
            hit[v] = coefs

print(f"\nMatrix deltas (in F-tuple coords) matching catalog Z-combos:")
print(f"Hits: {len(hit)} / {len(deltas_F_tuple)}")

# Note: this comparison is mixing coordinate systems. F-tuple delta is NOT in
# PBW coords. So we don't expect matches without a coordinate transformation.

# Let me try the comparison directly in F-tuple coords (assuming catalog deltas
# can be interpreted as F-tuple shifts).
print("\n--- Note: this comparison is in F-tuple coords directly, which may not ---")
print("--- match the catalog's PBW coords. Take with grain of salt. ---")


# -------- Better test: Z-rank of the matrix's deltas --------
deltas_list = list(deltas_F_tuple)
print(f"\nQ-rank of all {len(deltas_list)} matrix deltas: {q_rank(deltas_list)}")
# We know the deltas all satisfy delta_1 + delta_2 + delta_3 + delta_4 = 0  (weight pres) ... actually no:
# delta_1 + delta_3 = (a'_1+a'_3) - (a_1+a_3) = (n1) - (n2)  (n1 = f1 count, n2 = f2 count, depending on which side)
# Actually, see: F-tuple delta_1+delta_3 = (a'_1+a'_3) - (a_1+a_3); the F-side has a_1+a_3 = f2-count, while F'-side has a'_1+a'_3 = f1-count. These differ by (n1 - n2). So delta_1+delta_3 = n1 - n2 (varies by weight).
# So no universal sum-constraint.

# Print all matrix deltas
print("\nAll matrix delta vectors in F-tuple coords:")
for d in sorted(deltas_F_tuple):
    print(f"  {d}")
