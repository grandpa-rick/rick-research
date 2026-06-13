"""
Day 68 CODE Task 1 — n=5 piece registry analysis: # AXIS count.

n=5 is ODD (no Cor-8 linking eq), so the AII coordinate space at n=5 is
the full 15-dim (no reduction needed, unlike at n=4).

A variable is AXIS iff its column-coordinate hyperplane has >=3
rank-1 piece-pair collisions (the same strict-AXIS criterion as Day-67
n=4 and Day-68 n=3 verification).

Candidates from the Day-68 PROVE reformulation:
  C1 (uniform-3): # AXIS(n) = 3, AXIS = {prefix[1], prefix[n], long[1]}
  C2 (split):     # AXIS(n) = 3 + [n odd], so # AXIS(5) = 4
  C3 (different): varies

VERDICT: which one does n=5 support?
"""

import sys, json
from pathlib import Path
import numpy as np
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))

from n5_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       piece_matrix, verify_piece, enumerate_aii_lattice)
from n5_pieces import PIECES


def analyze(feasible, label=""):
    names = list(feasible.keys())
    mats = [feasible[n] for n in names]
    n_pieces = len(names)
    n_bdi = mats[0].shape[0]
    n_aii = mats[0].shape[1]

    cols_per_var = {av: set() for av in AII_VARS}
    for M in mats:
        for i in range(n_aii):
            c = tuple(int(M[r, i]) for r in range(n_bdi))
            cols_per_var[AII_VARS[i]].add(c)

    print(f"\n=== {label} (n_pieces={n_pieces}) ===")
    print(f"\nColumn-type counts per AII variable:")
    print(f"{'AII var':<14} | # cols | role-by-colcount")
    print("-" * 50)
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

    # Rank-1 piece-pair walls
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

    # AXIS = coord-wall with ≥3 piece-pairs (strict criterion)
    axis_strict = []
    for v, pairs in rank1_walls.items():
        v_nz = [(AII_VARS[k], v[k]) for k in range(len(v)) if v[k] != 0]
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
        'axis_by_colcount': type_counts['AXIS-by-colcount'],
        'axis_by_walls': [av for av, _ in axis_strict],
        'n_axis': len(axis_strict),
        'rank_distribution': {int(k): int(v) for k, v in rank_counter.items()},
        'rank1_walls_count': {repr(k): len(v) for k, v in rank1_walls.items()},
    }


def main():
    print(f"Total pieces in registry: {len(PIECES)}")
    # Use N_max = 5 (matches n) for verification; falls back to 4 if too slow.
    print("Enumerating AII lattice points at sum <= 5 ...")
    pts = enumerate_aii_lattice(5)
    print(f"# AII lattice pts at N<=5: {len(pts)}")

    feasible = {}
    infeasible = {}
    for name, spec in PIECES.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, pts)
        if bad:
            infeasible[name] = (M, bad)
        else:
            feasible[name] = M

    print(f"\nFeasible: {len(feasible)}/{len(PIECES)}")
    print(f"R-double pieces:")
    for k in ["Rdouble_alpha0", "Rdouble_alpha1", "Rdouble_alpha2"]:
        status = "FEASIBLE" if k in feasible else "INFEASIBLE"
        print(f"  {k}: {status}")
        if k in infeasible:
            M, bad = infeasible[k]
            p, q, err = bad[0]
            print(f"    first failure: err={err} at p={p}")
    if infeasible:
        print(f"\nInfeasible (excluded from analysis):")
        for name in infeasible:
            print(f"  ✗ {name}")

    # Print R-double columns on P1 (the variable whose AXIS status we're testing)
    print(f"\n=== R-double P1 columns ===")
    for k in ["Rdouble_alpha0", "Rdouble_alpha1", "Rdouble_alpha2"]:
        if k in feasible:
            M = feasible[k]
            col = M[:, 0]   # P1 is column 0
            nz = [(BDI_VARS[r], int(col[r])) for r in range(N_BDI) if col[r] != 0]
            print(f"  {k}: P1 column = {nz}")

    # Analysis (with and without R-double, for comparison)
    res_full = analyze(feasible, label="n=5 FULL registry (R-double IN)")

    feasible_no_rd = {n: M for n, M in feasible.items() if not n.startswith("Rdouble")}
    res_no_rd = analyze(feasible_no_rd, label="n=5 reduced (R-double REMOVED)")

    # Save
    out_dir = Path(__file__).parent
    with open(out_dir / "results.json", "w") as f:
        json.dump({"full": res_full, "no_rd": res_no_rd},
                  f, indent=2, default=str)

    # Save registry as JSON for archival
    registry_json = {}
    for name, M in feasible.items():
        registry_json[name] = {AII_VARS[c]: [int(M[r, c]) for r in range(N_BDI)]
                                for c in range(N_VARS)}
    with open(out_dir / "n5_registry.json", "w") as f:
        json.dump(registry_json, f, indent=2)

    print(f"\n{'='*60}\nVERDICT\n{'='*60}")
    print(f"FULL # AXIS (n=5): {res_full['n_axis']} — {res_full['axis_by_walls']}")
    print(f"NO-RD # AXIS (n=5): {res_no_rd['n_axis']} — {res_no_rd['axis_by_walls']}")
    print()
    print(f"Candidate predictions:")
    print(f"  C1 (uniform-3):    # AXIS(5) = 3")
    print(f"  C2 (3+[n odd]):    # AXIS(5) = 4")
    print(f"  C3 (varies):       # AXIS(5) = ?")
    n_ax = res_full['n_axis']
    if n_ax == 3:
        verdict = "C1 supported (uniform-3)"
    elif n_ax == 4:
        verdict = "C2 supported (split, +1 at odd n)"
    else:
        verdict = f"C3 supported (# AXIS = {n_ax})"
    print(f"\n→ {verdict}")

    # Write count summary
    with open(out_dir / "n5_axis_count.txt", "w") as f:
        f.write(f"# AXIS at n=5 (FULL registry): {res_full['n_axis']}\n")
        f.write(f"AXIS variables: {res_full['axis_by_walls']}\n")
        f.write(f"Verdict: {verdict}\n")
        f.write(f"\nFull col-counts:\n")
        for av, cc in res_full['col_counts'].items():
            f.write(f"  {av}: {cc}\n")
        f.write(f"\nRank distribution: {res_full['rank_distribution']}\n")

    return res_full, res_no_rd


if __name__ == "__main__":
    main()
