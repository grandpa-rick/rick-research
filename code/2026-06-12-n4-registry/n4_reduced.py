"""
Day 64 CODE Task 1 — Reduced piece registry at n=4.

The Cor-8 linking equation Λ = s1+s2+s3 reduces AII dim from 12 to 11.
Substituting Λ = s1+s2+s3 into each piece eliminates the gauge ambiguity.

After substitution, each piece is a 9×11 matrix (11 = drop Λ column).
The column of s_i absorbs the (original Λ_col) shifted by s_i's original column.

Count distinct columns per AII variable across pieces.

Day-62 prediction: # AXIS at n=4 = f(4) = 2.
"""

import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       LINKLHS_IDX, SHORT_IDX, piece_columns)
from n4_pieces_v2 import PIECES, main as run_pieces_v2


# Reduced variable list: drop linkLHS
REDUCED_VARS = [v for i, v in enumerate(AII_VARS) if i != LINKLHS_IDX]
REDUCED_IDX = [i for i in range(N_VARS) if i != LINKLHS_IDX]


def reduce_piece(M):
    """Substitute linkLHS = short[1]+short[2]+short[3] in piece M.
       Returns 9×11 reduced matrix."""
    M = M.copy()
    # Add Λ column to each s_i column, then drop Λ column
    alpha = M[:, LINKLHS_IDX].copy()
    for si in SHORT_IDX:
        M[:, si] += alpha
    # Drop Λ column
    M_red = M[:, REDUCED_IDX]
    return M_red


def piece_columns_red(M_red):
    """Return list of 11 columns (each 9-tuple)."""
    return [tuple(int(M_red[r, c]) for r in range(N_BDI))
            for c in range(M_red.shape[1])]


def main():
    feasible, pts = run_pieces_v2()
    print(f"\n{'='*60}")
    print(f"Reduced piece registry (substitute Λ = s1+s2+s3)")
    print(f"{'='*60}\n")

    # Reduce all pieces
    red_pieces = {name: reduce_piece(M) for name, M in feasible.items()}

    # Sanity: reduced pieces still match original on AII polytope
    from n4_setup import piece_apply
    for name, M_red in red_pieces.items():
        M_orig = feasible[name]
        for p in pts[:30]:
            q1 = piece_apply(M_orig, p)
            # Apply reduced piece: use p_red = drop Λ from p (linkLHS column unused)
            p_red = [p[i] for i in REDUCED_IDX]
            q2 = tuple(int(np.dot(M_red[i], p_red)) for i in range(N_BDI))
            if q1 != q2:
                print(f"  MISMATCH {name} at p={p}: {q1} vs {q2}")
                return
    print("Sanity check ✓\n")

    # Column-type analysis on REDUCED pieces
    cols_per_var = {av: set() for av in REDUCED_VARS}
    for name, M in red_pieces.items():
        cols = piece_columns_red(M)
        for i, c in enumerate(cols):
            cols_per_var[REDUCED_VARS[i]].add(c)

    print(f"{'AII var':<12} | # cols | role | distinct columns")
    print("-" * 80)
    rigid, binary, axis = [], [], []
    for av in REDUCED_VARS:
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

    print(f"\nSummary (reduced):")
    print(f"  RIGID  ({len(rigid)}): {rigid}")
    print(f"  BINARY ({len(binary)}): {binary}")
    print(f"  AXIS   ({len(axis)}): {axis}")
    print(f"\n# AXIS = {len(axis)} (Day-62 prediction: f(4) = 2)")


if __name__ == "__main__":
    main()
