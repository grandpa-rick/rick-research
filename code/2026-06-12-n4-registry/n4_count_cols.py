"""
Day 64 CODE Task 1 — Count distinct columns per AII variable across n=4 pieces.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import AII_VARS, BDI_VARS, N_VARS, N_BDI, piece_columns
from n4_pieces_v2 import PIECES, main as run_pieces


def main():
    feasible, pts = run_pieces()
    print(f"\n{'='*60}")
    print(f"Column-type analysis across {len(feasible)} feasible n=4 pieces")
    print(f"{'='*60}\n")

    # Collect columns
    cols_per_var = {av: set() for av in AII_VARS}
    for name, M in feasible.items():
        cols = piece_columns(M)
        for i, c in enumerate(cols):
            cols_per_var[AII_VARS[i]].add(c)

    # Classify
    print(f"{'AII var':<12} | # cols | role | distinct columns (as (BDI_var, coef) pairs)")
    print("-" * 80)
    for av in AII_VARS:
        cols = cols_per_var[av]
        n_cols = len(cols)
        if n_cols == 1:
            role = "RIGID"
        elif n_cols == 2:
            role = "BINARY"
        else:
            role = "AXIS"
        col_descs = []
        for c in sorted(cols):
            nonzero = [(BDI_VARS[r], c[r]) for r in range(N_BDI) if c[r] != 0]
            col_descs.append(", ".join(f"{v}={k}" for v, k in nonzero) or "0")
        print(f"{av:<12} | {n_cols:>6} | {role:<7} | {col_descs}")

    rigid = [av for av in AII_VARS if len(cols_per_var[av]) == 1]
    binary = [av for av in AII_VARS if len(cols_per_var[av]) == 2]
    axis = [av for av in AII_VARS if len(cols_per_var[av]) >= 3]
    print(f"\nSummary:")
    print(f"  RIGID  ({len(rigid)}): {rigid}")
    print(f"  BINARY ({len(binary)}): {binary}")
    print(f"  AXIS   ({len(axis)}): {axis}")

    return cols_per_var, rigid, binary, axis


if __name__ == "__main__":
    main()
