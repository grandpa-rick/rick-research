"""
Deeper analysis of the support: try several classification schemes and
verify the matrix M is invertible.
"""

import json
from collections import defaultdict, Counter
from fractions import Fraction
import os

HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, 'M_matrix.json')) as f:
    data = json.load(f)

F = [tuple(a) for a in data['F_admissible']]
Fp = [tuple(a) for a in data['Fp_admissible']]
M = {}
for entry in data['M_entries']:
    M[(tuple(entry['a_prime']), tuple(entry['a']))] = Fraction(entry['coef'])

print(f"|F| = {len(F)}, |F'| = {len(Fp)}, |supp(M)| = {len(M)}")

# -------- Verify M is invertible (rank 40) --------
# Build M as a 40x40 matrix
F_idx = {a: i for i, a in enumerate(F)}
Fp_idx = {a: i for i, a in enumerate(Fp)}
M_mat = [[Fraction(0)] * 40 for _ in range(40)]
for (ap, a), c in M.items():
    M_mat[Fp_idx[ap]][F_idx[a]] = c


def rref(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    pivots = []
    r = 0
    for c in range(n_cols):
        if r >= n_rows:
            break
        pivot_row = None
        for i in range(r, n_rows):
            if matrix[i][c] != 0:
                pivot_row = i
                break
        if pivot_row is None:
            continue
        matrix[r], matrix[pivot_row] = matrix[pivot_row], matrix[r]
        pv = matrix[r][c]
        for j in range(n_cols):
            matrix[r][j] /= pv
        for i in range(n_rows):
            if i != r and matrix[i][c] != 0:
                factor = matrix[i][c]
                for j in range(n_cols):
                    matrix[i][j] -= factor * matrix[r][j]
        pivots.append(c)
        r += 1
    return pivots


M_copy = [list(r) for r in M_mat]
pivots = rref(M_copy)
print(f"Rank of M = {len(pivots)}")
assert len(pivots) == 40, "M is not invertible — bug!"

# -------- Compute M^{-1} and look at its support --------
# We want the 40x40 inverse. Solve M X = I by RREF.
print("\nComputing M^{-1}...")
# Augmented [M | I]
n = 40
aug = []
for i in range(n):
    row = list(M_mat[i]) + [Fraction(0)] * n
    row[n + i] = Fraction(1)
    aug.append(row)
rref(aug)
# Read off M^{-1} = right-half block
M_inv_mat = [r[n:] for r in aug]
M_inv = {}
for i in range(n):
    for j in range(n):
        if M_inv_mat[i][j] != 0:
            # i = F-idx, j = F'-idx
            M_inv[(F[i], Fp[j])] = M_inv_mat[i][j]
print(f"|supp(M^{{-1}})| = {len(M_inv)}")

# Check supports differ
M_supp = set((ap, a) for ap, a in M.keys())
Minv_supp = set((a, ap) for a, ap in M_inv.keys())
print(f"Symmetric? {M_supp == set((ap, a) for ap, a in Minv_supp)}")


# -------- Try various classifications --------

# Classification A: delta in F-tuple coords
print("\n=== Classification A: delta = a' - a in F-tuple coords ===")
deltas_A = Counter()
for (ap, a) in M.keys():
    d = tuple(ap[i] - a[i] for i in range(4))
    deltas_A[d] += 1
print(f"Distinct deltas: {len(deltas_A)}")

# Classification B: L1 norm of delta
print("\n=== Classification B: L1 norm of delta ===")
l1_dist = Counter()
for (ap, a) in M.keys():
    d = tuple(ap[i] - a[i] for i in range(4))
    l1_dist[sum(abs(x) for x in d)] += 1
print(f"Distinct L1 norms: {len(l1_dist)}")
for k, v in sorted(l1_dist.items()):
    print(f"  L1 = {k}: {v} entries")

# Classification C: "type" of multi-entry rows (number of entries + leading coef)
print("\n=== Classification C: row shape (n_entries, sorted coefs) ===")
by_ap = defaultdict(list)
for (ap, a), c in M.items():
    by_ap[ap].append((a, c))
shape_counter = Counter()
for ap, entries in by_ap.items():
    coefs = sorted([c for _, c in entries], key=lambda x: (-abs(x), -x))
    shape = (len(entries), tuple(coefs))
    shape_counter[shape] += 1
print(f"Distinct row shapes: {len(shape_counter)}")
for shape, count in sorted(shape_counter.items()):
    print(f"  {shape}: {count} rows")


# -------- Classification D: think of (a, a') as a PAIR OF WORDS,
#         and classify by which letters are commuted past each other --------
# Each entry corresponds to a "straightening trace" from F'-word to F-form.
# The number of commutations is the inversion count between the two word patterns.

print("\n=== Classification D: number of f_1's and f_2's in the multi-set form ===")
# Total f_1 count = a_2 + a_4 = a'_1 + a'_3
# Total f_2 count = a_1 + a_3 = a'_2 + a'_4
# Both are the same on both sides (weight-preservation).
# But within the WORD, the positioning differs.
def f12_counts(a, F_side):
    if F_side == 'F':
        # word: f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1}
        return (a[3] + a[1], a[2] + a[0])  # (f1, f2)
    else:
        # word: f_2^{a'_4} f_1^{a'_3} f_2^{a'_2} f_1^{a'_1}
        return (a[2] + a[0], a[3] + a[1])

# Build classification: (n_f1, n_f2) gives the weight
wt_dist = Counter()
for (ap, a) in M.keys():
    n1, n2 = f12_counts(a, 'F')
    n1p, n2p = f12_counts(ap, 'Fp')
    assert (n1, n2) == (n1p, n2p)
    wt_dist[(n1, n2)] += 1
print(f"Distinct weights in support: {len(wt_dist)}")
# Don't print all 24


# -------- Classification E: count by structure of the F'-word --------
# Each F'-word has 4 "blocks". Some might be 0 (degenerate). Classify by
# the pattern of which blocks are 0.
print("\n=== Classification E: F'-word block-zero pattern ===")
block_pattern = Counter()
for ap in by_ap:
    pattern = tuple(1 if ap[i] > 0 else 0 for i in range(4))
    block_pattern[pattern] += 1
print(f"Distinct F'-block patterns: {len(block_pattern)}")
for p, c in sorted(block_pattern.items()):
    print(f"  pattern {p}: {c} rows")


# -------- Classification F: split rows into "trivial" and "non-trivial" --------
print("\n=== Classification F: rows by trivial/non-trivial ===")
trivial_rows = []
non_trivial_rows = []
for ap, entries in by_ap.items():
    if len(entries) == 1 and entries[0][1] == 1:
        trivial_rows.append(ap)
    else:
        non_trivial_rows.append(ap)
print(f"Trivial rows (single entry, coef 1): {len(trivial_rows)}")
print(f"Non-trivial rows: {len(non_trivial_rows)}")
print()
print("Non-trivial rows in detail (Rick's 'support patterns'):")
for ap in sorted(non_trivial_rows):
    entries = by_ap[ap]
    print(f"  a' = {ap}  weight ({ap[0]+ap[2]},{ap[1]+ap[3]}):")
    for a, c in sorted(entries):
        d = tuple(ap[i] - a[i] for i in range(4))
        print(f"    coef={c}  a={a}  delta={d}  L1={sum(abs(x) for x in d)}")
    print()


# -------- Classification G: cluster the 12 non-trivial rows --------
# Maybe they cluster naturally into 6 types based on some intrinsic property.
print("=== Classification G: clustering of non-trivial rows ===\n")
# Try: by the PAIR of leading and trailing F' block exponents
# Or: by the SHAPE (a'_1, a'_4) which are the "ends" of the F' word
print("F' word ends (a'_1, a'_4):")
end_pattern = Counter()
for ap in non_trivial_rows:
    end_pattern[(ap[0], ap[3])] += 1
print(f"  Distinct (a'_1, a'_4): {len(end_pattern)}")
for p, c in sorted(end_pattern.items()):
    print(f"  {p}: {c} rows")

# Try by middle pattern
print("\nF' word middles (a'_2, a'_3):")
mid_pattern = Counter()
for ap in non_trivial_rows:
    mid_pattern[(ap[1], ap[2])] += 1
for p, c in sorted(mid_pattern.items()):
    print(f"  {p}: {c} rows")


# -------- Classification H: ROOT-SPACE delta --------
# Compute the "root-space delta" of each entry: the shift in root coordinates.
# But both sides have same weight, so root-space delta = 0 always.
# However, the LMNP-style "position" in the word matters.

# Each F-vector at weight (n1, n2) has a specific "(a_1, a_2, a_3, a_4)" tuple.
# These tuples form a 4-dim grid (or rather, a subset).

# Encode the delta as a pair of "shifts" rel. to a baseline:
# baseline_F(weight) = some "diagonal" tuple, e.g., (n2_half, n1_half, n2_half, n1_half)
# Then re-classify the entries by (a - baseline, a' - baseline)
