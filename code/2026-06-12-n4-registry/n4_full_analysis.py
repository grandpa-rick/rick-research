"""
Day 64 CODE Task 1 — Full analysis with all v3 pieces.

Test: # AXIS at n=4 = 2 ?
"""

import sys, json
from pathlib import Path
import numpy as np
from collections import Counter
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import AII_VARS, BDI_VARS, N_VARS, N_BDI
from n4_pieces_v3 import PIECES, main as run_pieces_v3
from n4_reduced import REDUCED_VARS, REDUCED_IDX, reduce_piece


def analyze(feasible):
    names = list(feasible.keys())
    n_pieces = len(names)

    # Reduce all pieces
    red = [reduce_piece(feasible[n]) for n in names]

    # --- Column type analysis on reduced pieces ---
    cols_per_var = {av: set() for av in REDUCED_VARS}
    for M in red:
        for i in range(M.shape[1]):
            c = tuple(int(M[r, i]) for r in range(N_BDI))
            cols_per_var[REDUCED_VARS[i]].add(c)

    print(f"\nColumn-type counts in REDUCED pieces (Λ substituted out):")
    print(f"{'AII var':<12} | # cols | role")
    print("-" * 38)
    type_counts = {'RIGID': [], 'BINARY': [], 'AXIS': []}
    for av in REDUCED_VARS:
        n_cols = len(cols_per_var[av])
        if n_cols == 1: role = 'RIGID'
        elif n_cols == 2: role = 'BINARY'
        else: role = 'AXIS'
        type_counts[role].append(av)
        print(f"{av:<12} | {n_cols:>6} | {role}")

    # --- Pairwise difference rank distribution ---
    rank_counter = Counter()
    rank1_walls_by_hyperplane = {}

    for i in range(n_pieces):
        for j in range(i + 1, n_pieces):
            D = red[i] - red[j]
            if np.all(D == 0):
                continue
            r = np.linalg.matrix_rank(D)
            rank_counter[r] += 1
            if r == 1:
                # Identify the hyperplane normal v
                nz_rows = [r2 for r2 in range(N_BDI) if not np.all(D[r2] == 0)]
                r0 = nz_rows[0]
                pivot_col = next(c for c in range(D.shape[1]) if D[r0, c] != 0)
                scale = D[r0, pivot_col]
                v = D[r0, :] / scale  # length 11
                # Make canonical: sign normalize so first nonzero entry is positive
                v_tuple = tuple(round(x, 9) for x in v)
                # Sign: flip if first nonzero is negative
                first_nz = next((x for x in v_tuple if x != 0), 1)
                if first_nz < 0:
                    v_tuple = tuple(-x for x in v_tuple)
                rank1_walls_by_hyperplane.setdefault(v_tuple, []).append((names[i], names[j]))

    print(f"\nRank distribution (over {n_pieces*(n_pieces-1)//2} pairs):")
    for r in sorted(rank_counter):
        print(f"  rank {r}: {rank_counter[r]} pairs")

    print(f"\nRank-1 hyperplanes ({len(rank1_walls_by_hyperplane)} distinct):")
    coord_walls = []  # walls = e_k (single basis vector)
    for v, pairs in sorted(rank1_walls_by_hyperplane.items(),
                            key=lambda kv: -len(kv[1])):
        v_nz = [(REDUCED_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        desc = " + ".join(f"{c}·{av}" for av, c in v_nz)
        n_nz = len(v_nz)
        is_coord = (n_nz == 1)
        marker = "  [COORD]" if is_coord else ""
        print(f"  {{{desc} = 0}}: {len(pairs)} pair(s){marker}")
        if is_coord:
            coord_walls.append(v_nz[0][0])

    # Distinguish walls that meet AII cone interior vs only boundary
    print(f"\n--- Cone-interior wall analysis ---")
    print(f"COORDINATE walls (intersect cone interior):")
    interior_axis = []
    for v, pairs in sorted(rank1_walls_by_hyperplane.items(),
                            key=lambda kv: -len(kv[1])):
        v_nz = [(REDUCED_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        # COORDINATE walls = single-var walls
        if len(v_nz) == 1:
            print(f"  {{{v_nz[0][0]} = 0}}: {len(pairs)} pairs")
            interior_axis.append(v_nz[0][0])
        elif all(c > 0 for _, c in v_nz):
            # all positive coefficients => hyperplane misses cone interior
            # (because cone has all coords ≥ 0; sum positive = 0 ⇒ all zero, only origin)
            print(f"  {{{ ' + '.join(f'{c}·{av}' for av,c in v_nz) } = 0}} - "
                  f"boundary-only ({len(pairs)} pair(s))")
        else:
            print(f"  Mixed-sign wall (cuts cone interior): "
                  f"{ ' + '.join(f'{c}·{av}' for av,c in v_nz) } = 0  ({len(pairs)} pair(s))")

    # Categorize AXIS: variable v is AXIS iff coord-wall {v=0} has ≥3 piece-pairs
    # (equivalently, var has ≥3 distinct column types in the kernel-arrangement
    # interpretation; binary vars have exactly 1 wall-pair).
    print(f"\n--- AXIS classification ---")
    axis_strict = []
    for v, pairs in rank1_walls_by_hyperplane.items():
        v_nz = [(REDUCED_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        if len(v_nz) == 1 and len(pairs) >= 3:
            axis_strict.append((v_nz[0][0], len(pairs)))

    print(f"AXIS variables (coord-wall with ≥3 piece-pair collisions):")
    for av, n in axis_strict:
        print(f"  {av}: {n} pair-collisions")
    print(f"\n# AXIS = {len(axis_strict)} (prediction: f(4) = 2)")

    # Save results
    return {
        'feasible_pieces': list(feasible.keys()),
        'rank_distribution': {int(k): int(v) for k, v in rank_counter.items()},
        'rank1_walls': [
            {'v_normalized': [float(x) for x in v],
             'nonzero_vars': [(av, float(c)) for av, c in [(REDUCED_VARS[k], v[k]) for k in range(len(v))] if c != 0],
             'n_piece_pairs': len(pairs),
             'is_coord': sum(1 for x in v if x != 0) == 1,
             'meets_cone_interior': (sum(1 for x in v if x != 0) == 1) or (any(x < 0 for x in v) and any(x > 0 for x in v))}
            for v, pairs in rank1_walls_by_hyperplane.items()
        ],
        'col_counts': {av: int(len(cols_per_var[av])) for av in REDUCED_VARS},
        'rigid': type_counts['RIGID'],
        'binary': type_counts['BINARY'],
        'axis': [av for av, _ in axis_strict],
        'n_axis': len(axis_strict),
        'axis_pair_counts': [(av, int(n)) for av, n in axis_strict],
    }


def main():
    feasible, pts = run_pieces_v3()
    print(f"\n# Feasible pieces: {len(feasible)}")
    res = analyze(feasible)
    with open(Path(__file__).parent / 'n4_full_analysis.json', 'w') as f:
        json.dump(res, f, indent=2, default=str)
    print(f"\nSaved {Path(__file__).parent / 'n4_full_analysis.json'}")


if __name__ == "__main__":
    main()
