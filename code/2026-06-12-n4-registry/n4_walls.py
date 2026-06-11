"""
Day 64 CODE Task 1 — Kernel arrangement at n=4 (reduced pieces).

For each pair of pieces (M_i, M_j), compute rank(M_i - M_j).
The codim-1 walls correspond to rank-1 differences:
  M_i - M_j = u v^T  =>  ker = {p : v^T p = 0}

The AXIS variables = those whose coordinate hyperplane appears as a wall.
"""

import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import AII_VARS, BDI_VARS, N_VARS, N_BDI
from n4_pieces_v2 import PIECES, main as run_pieces_v2
from n4_reduced import REDUCED_VARS, REDUCED_IDX, reduce_piece


def main():
    feasible, pts = run_pieces_v2()
    print(f"\n{'='*60}")
    print(f"Kernel arrangement at n=4 (reduced pieces)")
    print(f"{'='*60}\n")

    # Reduce pieces
    names = list(feasible.keys())
    red = [reduce_piece(feasible[n]) for n in names]
    n_pieces = len(names)
    print(f"# pieces: {n_pieces}")

    # Pairwise diff ranks
    from collections import Counter
    rank_counter = Counter()
    rank1_walls = []
    for i in range(n_pieces):
        for j in range(i + 1, n_pieces):
            D = red[i] - red[j]
            r = np.linalg.matrix_rank(D)
            rank_counter[r] += 1
            if r == 1:
                # Find column index of nonzero col
                # D = u v^T; v = direction of kernel normal
                # In matrix form: pick any nonzero column, that's u * scalar;
                # the v direction = D[any_nonzero_row, :] / nonzero_scalar
                # Find nonzero row and column
                nz_rows = [r2 for r2 in range(N_BDI) if not np.all(D[r2] == 0)]
                nz_cols = [c2 for c2 in range(D.shape[1]) if not np.all(D[:, c2] == 0)]
                if nz_rows and nz_cols:
                    r0 = nz_rows[0]
                    c0 = nz_cols[0]
                    scale = D[r0, c0]
                    v = D[r0, :] / scale  # length 11
                    u = D[:, c0] / 1      # length 9 (using c0 column with v_c0 = 1 after rescaling)
                    # Actually: D = u v^T with v_c0 = 1 (we rescaled by scale of pivot col)
                    # u = D[:, c0] / v_c0 = D[:, c0] / 1; but we picked scale so D[r0,c0]/scale=1
                    # We want v: v[k] = D[r0, k] / D[r0, c0]. u: u[r] = D[r, c0].
                    v_normalized = D[r0, :].copy() / scale
                    u_normalized = D[:, c0].copy()
                    # Find which AII variable v points to (if it's a coordinate hyperplane)
                    v_nz = [(REDUCED_VARS[k], v_normalized[k])
                            for k in range(D.shape[1]) if abs(v_normalized[k]) > 1e-9]
                    rank1_walls.append({
                        'piece_i': names[i],
                        'piece_j': names[j],
                        'v_nz': v_nz,
                    })

    print(f"\nRank distribution of piece-pair differences:")
    for r in sorted(rank_counter):
        print(f"  rank {r}: {rank_counter[r]} pairs")
    print(f"Total pairs: {n_pieces * (n_pieces - 1) // 2}")

    # Group rank-1 walls by their v-direction (hyperplane)
    print(f"\nRank-1 walls (# = {len(rank1_walls)}):")
    walls_by_v = {}
    for w in rank1_walls:
        key = tuple(sorted([(av, round(c, 6)) for (av, c) in w['v_nz']]))
        walls_by_v.setdefault(key, []).append((w['piece_i'], w['piece_j']))

    for key, pairs in walls_by_v.items():
        desc = " + ".join(f"{c}*{av}" for av, c in key)
        print(f"  hyperplane {{{desc} = 0}}: {len(pairs)} piece-pair(s)")

    # Walls that pass through interior of AII cone:
    # In cone interior all AII vars > 0; a coord hyperplane {var_k = 0} touches the boundary.
    # All sign-flip hyperplanes {a*v_k + b*v_l = 0} with a,b same sign meet the cone only at origin.
    # COORDINATE walls: v = single basis vector (one nonzero entry).
    coord_walls = []
    for key in walls_by_v:
        if len(key) == 1:
            coord_walls.append(key[0])  # (var, coef)
    print(f"\nCOORDINATE walls (= AXIS variables): {len(coord_walls)}")
    for (av, coef) in coord_walls:
        print(f"  {av}")


if __name__ == "__main__":
    main()
