"""
Day 67 CODE Task 1 — n=4 R-double registry correction.

The Day-64 20-piece registry MISSED the R-double family. Day-66 PROVE
identified the family at n=4 as 3 BDI-feasible variants
α ∈ {0, 1, 2}, with α = c_{P1}[S] differing only.

This script:
1. Verifies the 3 R-double pieces are BDI-feasible at N=4 (replicating
   the Day-66 land-in-cone test).
2. Adds them to the 20-piece registry to make a 23-piece corrected set.
3. Re-runs the prefix[1]/long[1] AXIS classification.
4. Reports impact on the # AXIS = f(n) = 3 - [n even] conjecture.
"""

import sys, json
from pathlib import Path
import numpy as np
from collections import Counter

sys.path.insert(0, '/home/agent/projects/code/2026-06-12-n4-registry')
from n4_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       piece_matrix, verify_piece, enumerate_aii_lattice)
from n4_pieces_v3 import PIECES as PIECES_V3
from n4_reduced import REDUCED_VARS, REDUCED_IDX, reduce_piece

P1, P2, P3, P4 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3]
L1, L2, L3, L4 = AII_VARS[4], AII_VARS[5], AII_VARS[6], AII_VARS[7]
S1, S2, S3 = AII_VARS[8], AII_VARS[9], AII_VARS[10]
LAMBDA = AII_VARS[11]


def make_r_double_n4(alpha):
    """The n=4 R-double backbone (cf. n4_r_double_test.py, Day-66 proof)."""
    return {
        "M_2": [(1, L2)],
        "M_3": [(1, L3)],
        "B_1": [(1, P1), (2, S1), (1, L1)],
        "T_1": [(1, S1), (1, L1)],
        "B_2": [(1, P2), (1, S2), (1, P4)],
        "T_2": [(1, S2), (1, P4)],
        "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
        "T_3": [(1, S3), (1, LAMBDA)],
        "S":   [(1, L4), (2, S3), (2, S1), (alpha, P1)],
    }


# Build extended registry
PIECES_CORRECTED = dict(PIECES_V3)
for alpha in (0, 1, 2):
    PIECES_CORRECTED[f"Rdouble_alpha{alpha}"] = make_r_double_n4(alpha)


def analyze(feasible, label=""):
    names = list(feasible.keys())
    n_pieces = len(names)

    red = [reduce_piece(feasible[n]) for n in names]

    cols_per_var = {av: set() for av in REDUCED_VARS}
    for M in red:
        for i in range(M.shape[1]):
            c = tuple(int(M[r, i]) for r in range(N_BDI))
            cols_per_var[REDUCED_VARS[i]].add(c)

    print(f"\n=== {label} (n_pieces={n_pieces}) ===")
    print(f"\nColumn-type counts in REDUCED pieces (Λ substituted out):")
    print(f"{'AII var':<12} | # cols | role")
    print("-" * 38)
    type_counts = {'RIGID': [], 'BINARY': [], 'AXIS': []}
    col_counts = {}
    for av in REDUCED_VARS:
        n_cols = len(cols_per_var[av])
        col_counts[av] = n_cols
        if n_cols == 1: role = 'RIGID'
        elif n_cols == 2: role = 'BINARY'
        else: role = 'AXIS'
        type_counts[role].append(av)
        print(f"{av:<12} | {n_cols:>6} | {role}")

    rank_counter = Counter()
    rank1_walls = {}
    for i in range(n_pieces):
        for j in range(i + 1, n_pieces):
            D = red[i] - red[j]
            if np.all(D == 0):
                continue
            r = int(np.linalg.matrix_rank(D))
            rank_counter[r] += 1
            if r == 1:
                nz_rows = [r2 for r2 in range(N_BDI) if not np.all(D[r2] == 0)]
                r0 = nz_rows[0]
                pivot_col = next(c for c in range(D.shape[1]) if D[r0, c] != 0)
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
        v_nz = [(REDUCED_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        desc = " + ".join(f"{c}·{av}" for av, c in v_nz)
        is_coord = (len(v_nz) == 1)
        marker = "  [COORD]" if is_coord else ""
        print(f"  {{{desc} = 0}}: {len(pairs)} pair(s){marker}")

    # AXIS = coord-wall with ≥3 piece-pairs
    axis_strict = []
    for v, pairs in rank1_walls.items():
        v_nz = [(REDUCED_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
        if len(v_nz) == 1 and len(pairs) >= 3:
            axis_strict.append((v_nz[0][0], len(pairs)))

    print(f"\nAXIS variables (coord-wall, ≥3 piece-pair collisions):")
    for av, n in axis_strict:
        print(f"  {av}: {n} pair-collisions")
    print(f"\n# AXIS = {len(axis_strict)}")

    return {
        'label': label,
        'n_pieces': n_pieces,
        'col_counts': col_counts,
        'rigid': type_counts['RIGID'],
        'binary': type_counts['BINARY'],
        'axis_by_colcount': type_counts['AXIS'],
        'axis_by_walls': [av for av, _ in axis_strict],
        'n_axis': len(axis_strict),
        'rank_distribution': {int(k): int(v) for k, v in rank_counter.items()},
    }


def main():
    print(f"Total pieces in CORRECTED registry: {len(PIECES_CORRECTED)}")
    pts = enumerate_aii_lattice(4)
    print(f"# AII lattice pts at N<=4: {len(pts)}")

    feasible = {}
    infeasible = {}
    for name, spec in PIECES_CORRECTED.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, pts)
        if bad:
            infeasible[name] = (M, bad)
        else:
            feasible[name] = M

    print(f"\nFeasible: {len(feasible)}/{len(PIECES_CORRECTED)}")
    print(f"R-double pieces specifically:")
    for k in ["Rdouble_alpha0", "Rdouble_alpha1", "Rdouble_alpha2"]:
        status = "FEASIBLE" if k in feasible else "INFEASIBLE"
        print(f"  {k}: {status}")
        if k in infeasible:
            M, bad = infeasible[k]
            p, q, err = bad[0]
            print(f"    first failure: err={err} at p={p}")

    # Print R-double columns on P1 (the variable whose AXIS status we're testing)
    print(f"\n=== R-double P1 columns (in BDI 9-dim coords) ===")
    for k in ["Rdouble_alpha0", "Rdouble_alpha1", "Rdouble_alpha2"]:
        if k in feasible:
            M = feasible[k]
            col = M[:, 0]
            nz = [(BDI_VARS[r], int(col[r])) for r in range(N_BDI) if col[r] != 0]
            print(f"  {k}: P1 column = {nz}")

    # Run analyses
    res_old = analyze({n: M for n, M in feasible.items()
                        if not n.startswith("Rdouble")},
                       label="OLD 20-piece registry (Day-64)")

    res_new = analyze(feasible, label="CORRECTED registry (with R-double)")

    # Save results
    out_dir = Path(__file__).parent
    with open(out_dir / "results.json", "w") as f:
        json.dump({"old": res_old, "new": res_new}, f, indent=2, default=str)

    # Verdict
    print(f"\n{'='*60}\nVERDICT\n{'='*60}")
    print(f"OLD # AXIS (20-piece): {res_old['n_axis']} — {res_old['axis_by_walls']}")
    print(f"NEW # AXIS (23-piece): {res_new['n_axis']} — {res_new['axis_by_walls']}")
    print(f"prefix[1] col count: {res_old['col_counts'].get('prefix[1]')} → "
          f"{res_new['col_counts'].get('prefix[1]')}")
    print(f"prefix[4] col count: {res_old['col_counts'].get('prefix[4]')} → "
          f"{res_new['col_counts'].get('prefix[4]')}")
    print(f"long[1] col count:   {res_old['col_counts'].get('long[1]')} → "
          f"{res_new['col_counts'].get('long[1]')}")

    return res_old, res_new


if __name__ == "__main__":
    main()
