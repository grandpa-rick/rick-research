#!/usr/bin/env python3
"""
Day 75 CODE Task B -- Coordinate-pair coupling map at n = 5.

QUESTION (from Day-74):
  Day-74 saw that within the R-double family at n=5, (s_1, p_1) COUPLE
  (the s_1 engineering inevitably modifies the p_1 column too), but
  (s_4, p_4) do NOT couple. Which pairs of AII coordinates couple in
  the image semigroup?

COUPLING DEFINITION (operational interpretation of CODE.md spec):
  Coords (c_1, c_2) couple iff there exists a BDI-feasible piece pi
  in the n=5 augmented registry such that BOTH c_1 and c_2 are
  "engineered" in pi (i.e., the relevant column or row of pi differs
  from the base piece's). Symmetric relation; build the upper triangle
  and mirror.

  - For an AII var c (c in {p_i, l_i, s_i}): engine(c) is on in pi iff
    pi's c-column != base_piece's c-column.
  - For a BDI routing wall M_i (i in {2,3,4}): engine(M_i) is on in pi
    iff pi's M_i row != base_piece's M_i row (some AII coord beyond
    base's l_i routes to M_i, OR an off-base coef).

REGISTRY:
  Day-72 augmented registry at n=5 (50+ pieces): Day-70 minimal cover
  + Day-71 simple-divert + Day-72 l_j-divert + Class-1 aux. This
  exceeds Day-70's cover and is the operative registry for the Day-75
  PROVE rescue.

OUTPUT:
  - 18 x 18 binary coupling matrix
  - lists of "always couple" pairs and "never couple" pairs
  - sanity check: (s_1, p_1) couples; (s_4, p_4) does not
  - sanity check at n=6: pattern extends

HOW TO READ:
  The matrix entry C[c_1, c_2] = 1 means: "there is some piece in the
  registry where engineering at c_1 occurs together with engineering
  at c_2." This is a UNION over all pieces.
  C[c_1, c_2] = 0 means: across the whole registry, c_1-engine and
  c_2-engine never co-occur. (Stronger evidence that engineering at
  c_1 doesn't pull c_2 along.)
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
sys.path.insert(0, '/home/agent/projects/code/2026-06-17-complete-registry')
from general_axis import aii_struct, bdi_vars, piece_matrix
from general_pieces import base_piece


HERE = Path(__file__).resolve().parent


# AII coord ordering (15 vars) + 3 BDI M routing walls = 18 elements.
def coupling_coord_list(n):
    P = [f"p_{i}" for i in range(1, n + 1)]
    L = [f"l_{i}" for i in range(1, n + 1)]
    SH = [f"s_{i}" for i in range(1, n + 1)]
    Mwalls = [f"M_{i}" for i in range(2, n)]
    return P + L + SH + Mwalls


def coord_to_aii_var(coord):
    """Map coord label like 'p_3' to AII var name 'prefix[3]'."""
    pre = coord[0]
    idx = int(coord.split('_')[1])
    if pre == 'p':
        return f"prefix[{idx}]"
    if pre == 'l':
        return f"long[{idx}]"
    if pre == 's':
        return f"short[{idx}]"
    raise ValueError(coord)


def is_aii_coord(coord):
    return coord[0] in ('p', 'l', 's')


def is_m_wall(coord):
    return coord.startswith('M_')


def load_registry(n):
    """Load Day-72 augmented registry at n. Returns dict {name: M_matrix}."""
    s = aii_struct(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    n_aii = s["n_vars"]
    reg_path = Path(f"/home/agent/projects/code/2026-06-17-complete-registry/registry-n{n}.json")
    with open(reg_path) as f:
        reg = json.load(f)
    pieces = {}
    for name, cols in reg.items():
        M = np.zeros((n_bdi, n_aii), dtype=int)
        for av_name, col in cols.items():
            c = aii_v.index(av_name)
            for r in range(n_bdi):
                M[r, c] = col[r]
        pieces[name] = M
    return pieces


def base_matrix(n):
    s = aii_struct(n)
    return piece_matrix(base_piece(n), s)


def engineered_set(piece_M, base_M, struct, coords):
    """Return set of coupling-list coords that are 'engineered' in piece_M
    relative to base_M."""
    aii_v = struct["vars"]
    bdi_names = bdi_vars(struct["n"])
    engaged = set()
    # AII coord engines: column != base column.
    for coord in coords:
        if is_aii_coord(coord):
            av = coord_to_aii_var(coord)
            if av not in aii_v:
                continue  # e.g., s_n at even n
            ci = aii_v.index(av)
            if not np.array_equal(piece_M[:, ci], base_M[:, ci]):
                engaged.add(coord)
        elif is_m_wall(coord):
            # BDI row engine: row != base row.
            ri = bdi_names.index(coord)
            if not np.array_equal(piece_M[ri, :], base_M[ri, :]):
                engaged.add(coord)
    return engaged


def build_coupling_matrix(n, pieces, base_M):
    coords = coupling_coord_list(n)
    n_c = len(coords)
    struct = aii_struct(n)
    # NOTE: at even n, s_n doesn't exist (drops out of coords).
    coords = [c for c in coords if not (
        c.startswith('s_') and int(c.split('_')[1]) == n and n % 2 == 0
    )]
    n_c = len(coords)

    cidx = {c: i for i, c in enumerate(coords)}
    C = np.zeros((n_c, n_c), dtype=int)
    engaged_by_piece = {}
    # For each piece, find engaged coords, and OR-in all pairs to C.
    for name, M in pieces.items():
        eng = engineered_set(M, base_M, struct, coords)
        engaged_by_piece[name] = sorted(eng)
        for c1 in eng:
            for c2 in eng:
                C[cidx[c1], cidx[c2]] = 1
    return coords, C, engaged_by_piece


def print_matrix(coords, C, title=""):
    print(f"\n{title}")
    print("=" * 76)
    n_c = len(coords)
    # Header
    header = "       " + " ".join(f"{c:>4}" for c in coords)
    print(header)
    for i, ci in enumerate(coords):
        row = "  ".join("." if C[i, j] == 0 else "X" for j in range(n_c))
        print(f"  {ci:>4} {row}")
    print()
    # Diagonal info
    n_diag_on = sum(int(C[i, i]) for i in range(n_c))
    print(f"  diagonal-on (c engineered by SOME piece in registry): {n_diag_on}/{n_c}")


def couples_summary(coords, C):
    """Print a tidy summary of (i, j) pairs where C[i, j] = 1, i < j, and
    a list of coords that never couple with anyone."""
    n_c = len(coords)
    couples = []
    for i in range(n_c):
        for j in range(i + 1, n_c):
            if C[i, j]:
                couples.append((coords[i], coords[j]))
    isolated = [coords[i] for i in range(n_c)
                if sum(int(C[i, j]) for j in range(n_c) if j != i) == 0]
    only_self = [coords[i] for i in range(n_c)
                  if C[i, i] == 0]
    return couples, isolated, only_self


def main():
    print("=" * 76)
    print("Day 75 CODE Task B -- Coord-pair coupling map (n = 5)")
    print("=" * 76)

    # n = 5
    n = 5
    pieces = load_registry(n)
    base_M = base_matrix(n)
    coords5, C5, eng_by_piece5 = build_coupling_matrix(n, pieces, base_M)
    print(f"\nRegistry size (n=5): {len(pieces)} pieces")
    print_matrix(coords5, C5, "n = 5 coupling matrix")
    couples5, isol5, off_diag_only5 = couples_summary(coords5, C5)
    print(f"  # coupled pairs (i<j with X): {len(couples5)}")
    print(f"  # NEVER-engineered coords (zero row & column): {len(isol5)}")
    if isol5:
        print(f"    coords: {isol5}")
    print(f"  # coords with diag-off (never engineered alone): {len(off_diag_only5)}")
    if off_diag_only5:
        print(f"    coords: {off_diag_only5}")

    # Day-74 sanity check
    print("\nDay-74 sanity checks:")
    p1_idx = coords5.index("p_1")
    s1_idx = coords5.index("s_1")
    p4_idx = coords5.index("p_4")
    s4_idx = coords5.index("s_4")
    print(f"  (s_1, p_1) couples?  C[s_1, p_1] = {int(C5[s1_idx, p1_idx])}"
          f"  (expected: 1)")
    print(f"  (s_4, p_4) couples?  C[s_4, p_4] = {int(C5[s4_idx, p4_idx])}"
          f"  (expected: 0 per Day-74)")

    # List per-piece engaged sets for the non-base pieces (informative).
    print("\nPer-piece engaged-coord sets (showing non-empty only):")
    n_non_base = 0
    for name, eng in eng_by_piece5.items():
        if eng:
            n_non_base += 1
            if n_non_base <= 20:
                print(f"  {name}: {eng}")
    print(f"  ... {n_non_base} pieces total have non-empty engaged set.")

    # Sanity-check at n = 6 (does the structure extend?)
    n6 = 6
    pieces6 = load_registry(n6)
    base_M6 = base_matrix(n6)
    coords6, C6, eng_by_piece6 = build_coupling_matrix(n6, pieces6, base_M6)
    print(f"\nRegistry size (n=6): {len(pieces6)} pieces")
    print_matrix(coords6, C6, "n = 6 coupling matrix")
    couples6, isol6, off_diag_only6 = couples_summary(coords6, C6)
    print(f"  # coupled pairs (i<j with X): {len(couples6)}")
    if isol6:
        print(f"  NEVER-engineered coords: {isol6}")

    # Compare patterns: which (s_j, p_j) pairs couple at each n?
    print("\n(s_j, p_j) coupling pattern (predicted to be NON-uniform):")
    print(f"  n = 5:")
    for j in range(1, 6):
        sj = f"s_{j}"
        pj = f"p_{j}"
        if sj in coords5 and pj in coords5:
            v = int(C5[coords5.index(sj), coords5.index(pj)])
            print(f"    (s_{j}, p_{j}): {'COUPLE' if v else 'NO'}")
    print(f"  n = 6:")
    for j in range(1, 7):
        sj = f"s_{j}"
        pj = f"p_{j}"
        if sj in coords6 and pj in coords6:
            v = int(C6[coords6.index(sj), coords6.index(pj)])
            print(f"    (s_{j}, p_{j}): {'COUPLE' if v else 'NO'}")
        else:
            print(f"    (s_{j}, p_{j}): N/A (s_n absent at even n)")

    # Save
    out = {
        "n5": {
            "coords": coords5,
            "matrix": C5.tolist(),
            "n_pieces": len(pieces),
            "couples": couples5,
            "isolated_coords": isol5,
            "diag_off_coords": off_diag_only5,
            "sj_pj_couples": {
                f"s_{j}_p_{j}": (
                    int(C5[coords5.index(f"s_{j}"),
                           coords5.index(f"p_{j}")])
                    if f"s_{j}" in coords5 and f"p_{j}" in coords5
                    else None
                ) for j in range(1, 6)
            },
            "engaged_by_piece": eng_by_piece5,
        },
        "n6": {
            "coords": coords6,
            "matrix": C6.tolist(),
            "n_pieces": len(pieces6),
            "couples": couples6,
            "isolated_coords": isol6,
            "sj_pj_couples": {
                f"s_{j}_p_{j}": (
                    int(C6[coords6.index(f"s_{j}"),
                           coords6.index(f"p_{j}")])
                    if f"s_{j}" in coords6 and f"p_{j}" in coords6
                    else None
                ) for j in range(1, 7)
            },
        },
    }
    with open(HERE / "results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE/'results.json'}")


if __name__ == "__main__":
    main()
