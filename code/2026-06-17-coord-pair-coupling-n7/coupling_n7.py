#!/usr/bin/env python3
"""
Day 76 CODE Task B -- Coordinate-pair coupling map at n = 7.

Extends Day-75 coupling map (code/2026-06-20-coord-pair-coupling) from
n=5, 6 to n=7. Day-75 found that only (s_1, p_1) couples; (s_j, p_j) for
j > 1 are decoupled. This script verifies the pattern extends.

Output: 24x24 coupling matrix; counts; (s_j, p_j) pattern.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
sys.path.insert(0, '/home/agent/projects/code/2026-06-17-complete-registry')
sys.path.insert(0, '/home/agent/projects/code/2026-06-20-coord-pair-coupling')

from general_axis import aii_struct, bdi_vars, piece_matrix
from general_pieces import base_piece
from coupling_map import (
    coupling_coord_list, coord_to_aii_var, is_aii_coord, is_m_wall,
    load_registry, base_matrix, engineered_set, build_coupling_matrix,
    print_matrix, couples_summary,
)

HERE = Path(__file__).resolve().parent


def main():
    print("=" * 76)
    print("Day 76 CODE Task B -- Coord-pair coupling map at n = 7")
    print("=" * 76)

    n = 7
    pieces = load_registry(n)
    base_M = base_matrix(n)
    coords, C, eng_by_piece = build_coupling_matrix(n, pieces, base_M)
    print(f"\nRegistry size (n=7): {len(pieces)} pieces")
    print(f"Coupling coord count: {len(coords)} (expected ~24)")
    print_matrix(coords, C, f"n = 7 coupling matrix ({len(coords)}x{len(coords)})")
    couples, isolated, off_diag = couples_summary(coords, C)
    print(f"\n  # coupled pairs (i<j with X): {len(couples)}")
    print(f"  # NEVER-engineered coords: {len(isolated)}")
    if isolated:
        print(f"    coords: {isolated}")

    # Per-piece engaged-coord sets (informational)
    print("\nPer-piece engaged-coord sets (showing non-empty, first 30):")
    n_non_base = 0
    for name, eng in eng_by_piece.items():
        if eng:
            n_non_base += 1
            if n_non_base <= 30:
                print(f"  {name}: {eng}")
    print(f"  ... {n_non_base} pieces total have non-empty engaged set.")

    # The key (s_j, p_j) pattern.
    print("\n(s_j, p_j) coupling pattern at n = 7:")
    sj_pj_couples = {}
    for j in range(1, n + 1):
        sj = f"s_{j}"
        pj = f"p_{j}"
        if sj in coords and pj in coords:
            v = int(C[coords.index(sj), coords.index(pj)])
            sj_pj_couples[f"s_{j}_p_{j}"] = v
            print(f"  (s_{j}, p_{j}): {'COUPLE' if v else 'NO'}")
        else:
            # at odd n, s_n exists; n=7 is odd so s_7 should exist.
            sj_pj_couples[f"s_{j}_p_{j}"] = None
            print(f"  (s_{j}, p_{j}): N/A")

    # Compare to predicted pattern (Day-75 / Day-76 Theorem 8.1):
    # only (s_1, p_1) should be COUPLE.
    predicted = {f"s_{j}_p_{j}": (1 if j == 1 else 0) for j in range(1, n + 1)}
    matches = all(sj_pj_couples.get(f"s_{j}_p_{j}", -1) == predicted[f"s_{j}_p_{j}"]
                  for j in range(1, n + 1))
    print(f"\n  Pattern matches Day-76 Theorem 8.1 prediction: {matches}")
    if not matches:
        print("  Productive falsification: which (s_j, p_j) couples that shouldn't?")
        for j in range(1, n + 1):
            ac = sj_pj_couples.get(f"s_{j}_p_{j}")
            pr = predicted[f"s_{j}_p_{j}"]
            if ac != pr:
                print(f"    j={j}: actual={ac}, predicted={pr}")

    # Save
    out = {
        "n": n,
        "n_pieces": len(pieces),
        "n_coords": len(coords),
        "coords": coords,
        "matrix": C.tolist(),
        "n_couples_pairs": len(couples),
        "couples": couples,
        "isolated_coords": isolated,
        "diag_off_coords": off_diag,
        "sj_pj_couples": sj_pj_couples,
        "predicted_only_s1_p1_couples": predicted,
        "pattern_matches_theorem_8_1": matches,
    }
    with open(HERE / "results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE/'results.json'}")


if __name__ == "__main__":
    main()
