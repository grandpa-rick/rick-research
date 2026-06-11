"""
Day 64 CODE Task 1 — Normalize pieces by absorbing linkLHS into shorts.

The Cor-8 linking equation Λ = s1 + s2 + s3 induces a gauge freedom in
piece space: for any 9-vector α (one per BDI coord),

    M[*, Λ] += α,  M[*, s_i] -= α for i=1,2,3

gives an equivalent piece on the AII polytope.

To remove this gauge, we NORMALIZE every piece by subtracting from its
Λ column and adding to each s_i column equally, so that the Λ column
becomes zero. After this, the Λ column is 0 in every piece, and column
diversity for Λ is 1 (RIGID).

Then we re-count column types.
"""

import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       LINKLHS_IDX, SHORT_IDX, piece_columns)
from n4_pieces_v2 import PIECES, main as run_pieces_v2


def normalize_piece(M):
    """Set Λ column to zero by absorbing into s1, s2, s3 columns.
       For each BDI row r:
         α_r := M[r, Λ]
         M[r, Λ] -= α_r → 0
         M[r, s_i] += α_r for i=1,2,3
    """
    M = M.copy()
    alpha = M[:, LINKLHS_IDX].copy()
    M[:, LINKLHS_IDX] = 0
    for si in SHORT_IDX:
        M[:, si] += alpha
    return M


def main():
    feasible, pts = run_pieces_v2()
    print(f"\n{'='*60}")
    print(f"Normalize linkLHS column to zero (gauge fix)")
    print(f"{'='*60}\n")

    # Normalize all pieces
    norm_pieces = {name: normalize_piece(M) for name, M in feasible.items()}

    # Sanity check: pieces still give same BDI image on AII polytope?
    # (Yes by construction; verify on a few pts.)
    from n4_setup import piece_apply, bdi_feasible_n4
    for name, M_norm in norm_pieces.items():
        M_orig = feasible[name]
        for p in pts[:30]:
            q1 = piece_apply(M_orig, p)
            q2 = piece_apply(M_norm, p)
            if q1 != q2:
                print(f"  MISMATCH for {name} at p={p}: {q1} vs {q2}")
                return
    print("Sanity check: normalized pieces match originals on all sample pts ✓\n")

    # Column-type analysis
    cols_per_var = {av: set() for av in AII_VARS}
    for name, M in norm_pieces.items():
        cols = piece_columns(M)
        for i, c in enumerate(cols):
            cols_per_var[AII_VARS[i]].add(c)

    print(f"{'AII var':<12} | # cols | role | distinct columns")
    print("-" * 80)
    rigid = []
    binary = []
    axis = []
    for av in AII_VARS:
        cols = cols_per_var[av]
        n_cols = len(cols)
        if n_cols == 1:
            role = "RIGID"; rigid.append(av)
        elif n_cols == 2:
            role = "BINARY"; binary.append(av)
        else:
            role = "AXIS"; axis.append(av)
        col_descs = []
        for c in sorted(cols):
            nonzero = [(BDI_VARS[r], c[r]) for r in range(N_BDI) if c[r] != 0]
            col_descs.append(", ".join(f"{v}={k}" for v, k in nonzero) or "0")
        print(f"{av:<12} | {n_cols:>6} | {role:<7} | {col_descs}")

    print(f"\nSummary (after linkLHS gauge fix):")
    print(f"  RIGID  ({len(rigid)}): {rigid}")
    print(f"  BINARY ({len(binary)}): {binary}")
    print(f"  AXIS   ({len(axis)}): {axis}")
    print(f"\n# AXIS = {len(axis)} (Day-62 prediction: f(4) = 2)")


if __name__ == "__main__":
    main()
