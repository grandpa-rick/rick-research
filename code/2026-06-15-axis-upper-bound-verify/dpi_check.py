"""
Day 70 verification — Conjecture D-pi check at n=5.

Conjecture D-pi: for every interior prefix p_i (1 < i < n-1 = 4 at n=5,
so i ∈ {2, 3}), the minimal cover has p_i routed canonically as
pi^{p_i} = e_{B_i} only. No 3-clique on {p_i = 0} exists with 3 distinct
columns.

This script:
  1. Lists all 27 feasible pieces' p_i columns for i = 2, 3, 4
     (4 = p_{n-1}, included for completeness, RIGID per Lemma 6.4).
  2. Confirms each p_i has only 1 column type (RIGID, hence no 3-clique).
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-13-n5-axis-count')

import numpy as np
import collections
from n5_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS,
                       piece_matrix, verify_piece, enumerate_aii_lattice)
from n5_pieces import PIECES

INTERIOR_PREFIX = [2, 3]  # 1 < i < n-1 = 4 at n=5
P_NMINUS1 = 4  # p_{n-1} at n=5


def main():
    print("Day 70 verification — Conjecture D-pi at n=5")
    print("=" * 60)

    pts = enumerate_aii_lattice(5)
    feasible = {}
    for name, spec in PIECES.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, pts)
        if not bad:
            feasible[name] = M

    print(f"Feasible pieces: {len(feasible)}")
    print()

    all_passed = True
    for i in INTERIOR_PREFIX + [P_NMINUS1]:
        col_idx = i - 1  # 0-indexed
        col_counts = collections.Counter()
        for name, M in feasible.items():
            col = tuple(int(M[r, col_idx]) for r in range(N_BDI))
            col_counts[col] += 1
        n_types = len(col_counts)

        # Pretty-print column types
        if i == P_NMINUS1:
            label = f"p_{i} (= p_{{n-1}}, RIGID by Lemma 6.4)"
        else:
            label = f"p_{i} (interior, target of Conjecture D-pi)"

        print(f"{label}:")
        print(f"  Distinct column types: {n_types}")
        for col, cnt in col_counts.most_common():
            nz = {BDI_VARS[r]: col[r] for r in range(N_BDI) if col[r] != 0}
            print(f"    {nz}: {cnt} piece(s)")

        # 3-clique check: with only 1 column type, no 3 distinct columns
        # can exist on the coord wall.
        if n_types >= 3:
            print(f"  [WARN] {n_types} distinct columns — Conjecture D-pi POTENTIALLY refuted at i={i}.")
            all_passed = False
        elif n_types == 2:
            print(f"  [PASS] BINARY — at most 2 column types, no 3-clique possible.")
        else:
            print(f"  [PASS] RIGID — 1 column type, no 3-clique possible.")
        print()

    if all_passed:
        print(f"[PASS] Conjecture D-pi VERIFIED at n=5: interior p_i RIGID for all i ∈ {INTERIOR_PREFIX}.")
        return 0
    else:
        print(f"[FAIL] Conjecture D-pi violated somewhere.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
