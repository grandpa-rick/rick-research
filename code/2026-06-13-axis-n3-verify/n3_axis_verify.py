"""
Day 68 PROVE Phase 1 — n=3 AXIS classification via REDUCED kernel-arrangement.

Re-derive # AXIS at n=3 from the 26-piece minimal cover using the SAME
methodology as Day-67 n=4 (`n4_rdouble_corrected.py`). Goal: confirm
# AXIS(n=3) = 3 with the R-double family already present, and identify
the 3 AXIS variables.

At n=3 the AII has 9 column-mult variables (no Cor-8 linking eq since n
is odd). So the "REDUCED" representation = the full 9-dim AII matrix.

A variable is AXIS iff its column-coordinate hyperplane has >=3 rank-1
piece-pair collisions (the same strict-AXIS criterion used at n=4).
"""

import sys, json
from pathlib import Path
import numpy as np
from collections import Counter

sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v9 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS, BDI_VARS


def analyze(pieces_dict, label=""):
    names = list(pieces_dict.keys())
    n_pieces = len(names)
    mats = [np.array(piece_matrix(pieces_dict[n]).tolist(), dtype=int)
            for n in names]
    n_bdi = mats[0].shape[0]
    n_aii = mats[0].shape[1]

    cols_per_var = {av: set() for av in AII_VARS}
    for M in mats:
        for i in range(n_aii):
            c = tuple(int(M[r, i]) for r in range(n_bdi))
            cols_per_var[AII_VARS[i]].add(c)

    print(f"\n=== {label} (n_pieces={n_pieces}) ===")
    print(f"\nColumn-type counts per AII variable:")
    print(f"{'AII var':<14} | # cols | role")
    print("-" * 40)
    type_counts = {'RIGID': [], 'BINARY': [], 'AXIS-by-colcount': []}
    col_counts = {}
    for av in AII_VARS:
        n_cols = len(cols_per_var[av])
        col_counts[av] = n_cols
        if n_cols == 1: role = 'RIGID'
        elif n_cols == 2: role = 'BINARY'
        else: role = 'AXIS-by-colcount'
        type_counts[role].append(av)
        print(f"{av:<14} | {n_cols:>6} | {role}")

    rank_counter = Counter()
    rank1_walls = {}
    for i in range(n_pieces):
        for j in range(i + 1, n_pieces):
            D = mats[i] - mats[j]
            if np.all(D == 0):
                continue
            r = int(np.linalg.matrix_rank(D))
            rank_counter[r] += 1
            if r == 1:
                nz_rows = [r2 for r2 in range(n_bdi) if not np.all(D[r2] == 0)]
                r0 = nz_rows[0]
                pivot_col = next(c for c in range(n_aii) if D[r0, c] != 0)
                scale = D[r0, pivot_col]
                v = D[r0, :] / scale
                v_tuple = tuple(round(x, 9) for x in v)
                first_nz = next((x for x in v_tuple if x != 0), 1)
                if first_nz < 0:
                    v_tuple = tuple(-x for x in v_tuple)
                rank1_walls.setdefault(v_tuple, []).append((names[i], names[j]))

    print(f"\nRank distribution (over {n_pieces*(n_pieces-1)//2} pairs):")
    for r in sorted(rank_counter):
        print(f"  rank {r}: {rank_counter[r]} pairs")

    print(f"\nRank-1 hyperplanes ({len(rank1_walls)} distinct):")
    for v, pairs in sorted(rank1_walls.items(), key=lambda kv: -len(kv[1])):
        v_nz = [(AII_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        desc = " + ".join(f"{c}·{av}" for av, c in v_nz)
        is_coord = (len(v_nz) == 1)
        marker = "  [COORD]" if is_coord else ""
        print(f"  {{{desc} = 0}}: {len(pairs)} pair(s){marker}")

    # AXIS = coord-wall with ≥3 piece-pairs
    axis_strict = []
    for v, pairs in rank1_walls.items():
        v_nz = [(AII_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        if len(v_nz) == 1 and len(pairs) >= 3:
            axis_strict.append((v_nz[0][0], len(pairs)))

    print(f"\nAXIS variables (coord-wall, >=3 piece-pair collisions):")
    for av, n in axis_strict:
        print(f"  {av}: {n} pair-collisions")
    print(f"\n# AXIS = {len(axis_strict)}")

    return {
        'label': label,
        'n_pieces': n_pieces,
        'col_counts': col_counts,
        'axis_by_walls': [av for av, _ in axis_strict],
        'n_axis': len(axis_strict),
        'rank_distribution': {int(k): int(v) for k, v in rank_counter.items()},
    }


def main():
    # The 26-piece minimal cover at n=3
    pieces_26 = {n: ALL_PI[n] for n in MIN_COVER_26 if n in ALL_PI}
    print(f"n=3 minimal cover: {len(pieces_26)}/{len(MIN_COVER_26)} pieces present")

    rdoubles = ["R_double_m2345", "P5d_Rdouble_plus_m2", "P7_Rdouble_m2_dbl_S"]
    print(f"\nR-double pieces present:")
    for r in rdoubles:
        print(f"  {r}: {'YES' if r in pieces_26 else 'MISSING'}")

    # Analyze with R-double IN (full 26-piece cover)
    res_full = analyze(pieces_26, label="n=3 FULL 26-piece minimal cover (R-double IN)")

    # Analyze with R-double REMOVED (23-piece reduced)
    pieces_minus_rd = {n: M for n, M in pieces_26.items()
                       if n not in rdoubles}
    res_minus = analyze(pieces_minus_rd,
                        label="n=3 reduced 23-piece (R-double REMOVED)")

    # Save results
    out_dir = Path(__file__).parent
    with open(out_dir / "results.json", "w") as f:
        json.dump({"full_26": res_full, "minus_rd_23": res_minus},
                  f, indent=2, default=str)

    print(f"\n{'='*60}\nVERDICT\n{'='*60}")
    print(f"FULL 26-piece #AXIS = {res_full['n_axis']} — {res_full['axis_by_walls']}")
    print(f"MINUS-RD 23-piece #AXIS = {res_minus['n_axis']} — {res_minus['axis_by_walls']}")
    print(f"\nm_2 col count: {res_full['col_counts']['m_2']} (full) vs "
          f"{res_minus['col_counts']['m_2']} (minus-RD)")
    print(f"m_236 col count: {res_full['col_counts']['m_236']} (full) vs "
          f"{res_minus['col_counts']['m_236']} (minus-RD)")
    print(f"m_23456 col count: {res_full['col_counts']['m_23456']} (full) vs "
          f"{res_minus['col_counts']['m_23456']} (minus-RD)")

    return res_full, res_minus


if __name__ == "__main__":
    main()
