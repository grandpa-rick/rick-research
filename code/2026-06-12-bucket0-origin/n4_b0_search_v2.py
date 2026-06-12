"""
Day 66 PROVE Phase 1 — n=4 B0-analog, FILTERED to 20 feasible pieces.

The "B0-analog at n=4" is: classes of pieces that share all AII-var columns
EXCEPT for a single axis-variable's S-entry — i.e., the "S-multiplicity chain"
on one fixed axis variable.

At n=3: B0 = 3 pieces sharing (m_236, m_23456) columns and differing in m_2.S
multiplicity ∈ {0, 1, 2}. The "S-mass" of m_2 ranges over an A_1-weight ladder.

Predictions to test at n=4:
- f(n) = 3 - [n even] gives 2
- C(n, 1) = n gives 4
- "rep-theoretic" gives # = (dim of analog adj rep)
"""
import sys, json
from pathlib import Path
sys.path.insert(0, '/home/agent/projects/code/2026-06-12-n4-registry')

from n4_setup import AII_VARS, BDI_VARS, N_VARS, N_BDI
from n4_pieces_v3 import PIECES

with open('/home/agent/projects/code/2026-06-12-n4-registry/n4_full_analysis.json') as f:
    n4_data = json.load(f)
FEASIBLE = set(n4_data['feasible_pieces'])
print(f"# feasible pieces: {len(FEASIBLE)}")

def piece_column(spec, aii_var):
    col = [0] * N_BDI
    for i, bdi in enumerate(BDI_VARS):
        for (coef, av) in spec.get(bdi, []):
            if av == aii_var:
                col[i] += coef
    return tuple(col)

piece_cols = {}
for name, spec in PIECES.items():
    if name not in FEASIBLE: continue
    cols = {v: piece_column(spec, v) for v in AII_VARS}
    piece_cols[name] = cols

S_idx = BDI_VARS.index("S")
print(f"S column index: {S_idx}")

# === Test 1: classes where ALL other-var columns agree, varying var = V. ===
print("\n=== Equivalence classes (vary V, others fixed) on feasible pieces ===")
for V in AII_VARS:
    others = [v for v in AII_VARS if v != V]
    classes = {}
    for name, cols in piece_cols.items():
        other_cols = tuple(cols[v] for v in others)
        classes.setdefault(other_cols, []).append(name)
    multi = {k: v for k, v in classes.items() if len(v) >= 2}
    if multi:
        sizes = sorted(len(v) for v in multi.values())
        print(f"  V={V}: class sizes = {sizes}")
        for other_cols, names in multi.items():
            V_cols = [piece_cols[n][V] for n in names]
            # Check if the variation is SOLELY in the S-entry
            non_S = {tuple(c[i] for i in range(N_BDI) if i != S_idx) for c in V_cols}
            S_vals = sorted([c[S_idx] for c in V_cols])
            print(f"    size {len(names)}: V-cols vary, S-mults={S_vals}, "
                  f"non-S {'differ' if len(non_S)>1 else 'SAME'}")
            if len(non_S) == 1:
                print(f"      ** S-mass chain: {names}")
                for n in names:
                    print(f"         {n}: c[{V}] = {piece_cols[n][V]}")

print()
print("="*60)
print("INTERPRETATION:")
print("  We want classes where V varies ONLY in its S-entry while non-S")
print("  entries are identical.  Count those classes by V.")
