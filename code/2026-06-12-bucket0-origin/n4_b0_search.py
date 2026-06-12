"""
Day 66 PROVE Phase 1 — find n=4 analogues of Bucket-0.

At n=3: Bucket-0 = 3 pieces sharing m_236 and m_23456 columns, differing only
in m_2 column (specifically in the S-entry of c_m2 ∈ {0,1,2}).

At n=4: the analogue m_2 is prefix[1] = P1. But P1 collapsed from AXIS to RIGID,
i.e., has only 1 distinct column across the 20-piece registry. So the
"R-double family" at n=4 is naturally indexed by long[1] = L1 or prefix[4] = P4
(the 2 axis vars at n=4).

Strategy: for each AII var V at n=4, find equivalence classes of pieces where
all *other* AII columns agree and only V's column changes. The largest such
class is the "B0-analog".
"""
import sys, json
from pathlib import Path
sys.path.insert(0, '/home/agent/projects/code/2026-06-12-n4-registry')

from n4_setup import AII_VARS, BDI_VARS, N_VARS, N_BDI
from n4_pieces_v3 import PIECES

print(f"n=4 registry size: {len(PIECES)}")
print(f"AII vars: {AII_VARS}")
print(f"BDI vars: {BDI_VARS}")

# For each piece, compute the columns of each AII var.
def piece_column(spec, aii_var):
    col = [0] * N_BDI
    for i, bdi in enumerate(BDI_VARS):
        for (coef, av) in spec.get(bdi, []):
            if av == aii_var:
                col[i] += coef
    return tuple(col)

piece_cols = {}
for name, spec in PIECES.items():
    cols = {v: piece_column(spec, v) for v in AII_VARS}
    piece_cols[name] = cols

# For each AII var V: group pieces by their column-tuple on ALL OTHER vars.
# Then find groups of size ≥ 2 where V-column is the only thing that varies.
print()
for V in AII_VARS:
    if V == "Lambda":  # Λ is gauge-fixed; skip
        continue
    others = [v for v in AII_VARS if v != V]
    classes = {}
    for name, cols in piece_cols.items():
        other_cols = tuple(cols[v] for v in others)
        classes.setdefault(other_cols, []).append(name)
    multi = {k: v for k, v in classes.items() if len(v) >= 2}
    if multi:
        print(f"=== Var {V}: ===")
        for other_cols, names in multi.items():
            V_cols = sorted(set(piece_cols[n][V] for n in names))
            print(f"  Class of size {len(names)}: V-cols = {V_cols}")
            for n in names:
                print(f"    {n}: {V} = {piece_cols[n][V]}")
        print()

# Also: find equivalence classes where only ONE var differs among a TRIPLE
# of pieces (looking for the n=4 analog of B0-3 specifically).
print()
print("=== Triples of pieces differing only in V ===")
for V in AII_VARS:
    if V == "Lambda":
        continue
    others = [v for v in AII_VARS if v != V]
    classes = {}
    for name, cols in piece_cols.items():
        other_cols = tuple(cols[v] for v in others)
        classes.setdefault(other_cols, []).append(name)
    triples = {k: v for k, v in classes.items() if len(v) >= 3}
    if triples:
        for other_cols, names in triples.items():
            V_cols = sorted(set(piece_cols[n][V] for n in names))
            print(f"  V = {V}: triple class of size {len(names)}, V-cols = {V_cols}")
            for n in names:
                print(f"    {n}: {V} = {piece_cols[n][V]}")
        print()
