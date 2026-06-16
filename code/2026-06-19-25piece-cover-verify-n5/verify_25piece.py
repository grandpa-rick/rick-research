#!/usr/bin/env python3
"""
Day-74 CODE Task B — 25-piece minimal cover verification at n = 5.

CLAIM (Day-73 §7): Removing the multiplicity-2 pieces "Lemma B k=2"
(P5_P5_dbl_BT2) and "Lemma C k=2" (P5_L1_M2dbl) from Day-72's
27-piece registry yields a 25-piece subcover that:
  (1) Still covers T_5 = P^{BDI}_{Z} at sum <= 4.
  (2) Is minimal: removing ANY single piece breaks coverage.
  (3) Has W (the set of AXIS walls / 3-clique-supporting walls) = {p_1}.
  (4) Has NO non-canonical 3-cliques on {p_5, l_1}.

VERIFICATION:
  - Load 27-piece registry from 2026-06-13-n5-axis-count/n5_registry.json.
  - Image-containment check: confirm Lemma B k=2 and Lemma C k=2 are
    image-redundant in the remaining 25 pieces' joint image.
  - Coverage check on T_5 at sum <= 4 (before/after removal).
  - Minimality check on the 25-piece subcover.
  - Wall identification: find all coordinate-walls with >=3 rank-1
    piece-pair collisions.
"""
import sys
import json
import itertools
from pathlib import Path

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-13-n5-axis-count')
from n5_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS,
                      bdi_feasible_n5, enumerate_aii_lattice,
                      piece_apply, verify_piece)


REGISTRY_PATH = "/home/agent/projects/code/2026-06-13-n5-axis-count/n5_registry.json"
PIECES_TO_REMOVE = ["P5_P5_dbl_BT2", "P5_L1_M2dbl"]


def load_registry():
    with open(REGISTRY_PATH) as f:
        reg = json.load(f)
    pieces = {}
    for name, cols in reg.items():
        M = np.zeros((N_BDI, N_VARS), dtype=int)
        for av, col in cols.items():
            ai = AII_VARS.index(av)
            for r in range(N_BDI):
                M[r, ai] = col[r]
        pieces[name] = M
    return pieces


def enumerate_bdi_lattice(N_max):
    pts = []

    def gen(remaining, depth, current):
        if depth == N_BDI:
            ok, _ = bdi_feasible_n5(tuple(current))
            if ok:
                pts.append(tuple(current))
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()

    gen(N_max, 0, [])
    return pts


def image_at_sum(M, sum_bound):
    """The set of BDI lattice points in M(P^{AII}_n) with sum <= sum_bound,
    computed via direct image enumeration over AII lattice."""
    aii_pts = enumerate_aii_lattice(sum_bound)
    covered = set()
    for p in aii_pts:
        q = piece_apply(M, p)
        if sum(q) <= sum_bound:
            covered.add(q)
    return covered


def cover_image(pieces, sum_bound):
    """The union image of a set of pieces at sum_bound."""
    covered = set()
    aii_pts = enumerate_aii_lattice(sum_bound)
    for name, M in pieces.items():
        for p in aii_pts:
            q = piece_apply(M, p)
            if sum(q) <= sum_bound:
                covered.add(q)
    return covered


def find_rank1_walls(pieces):
    """For a set of pieces, find rank-1 piece-pair differences and
    classify by the coordinate hyperplane (or non-coord hyperplane)."""
    names = list(pieces.keys())
    mats = [pieces[n] for n in names]
    rank1_walls = {}  # v_tuple -> list of (i, j) pairs
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            D = mats[i] - mats[j]
            if np.all(D == 0):
                continue
            r = int(np.linalg.matrix_rank(D))
            if r != 1:
                continue
            nz_rows = [k for k in range(N_BDI) if not np.all(D[k] == 0)]
            r0 = nz_rows[0]
            pivot_col = next(c for c in range(N_VARS) if D[r0, c] != 0)
            scale = D[r0, pivot_col]
            v = D[r0, :] / scale
            v_tuple = tuple(round(x, 9) for x in v)
            first_nz = next((x for x in v_tuple if x != 0), 1)
            if first_nz < 0:
                v_tuple = tuple(-x for x in v_tuple)
            rank1_walls.setdefault(v_tuple, []).append((names[i], names[j]))
    return rank1_walls


def find_3cliques_per_wall(pieces, sum_bound=4):
    """Find triples of pieces pairwise rank-1 differing on the SAME single
    AII column. Returns dict: wall_var -> list of triples (a, b, c)."""
    names = list(pieces.keys())
    mats = {n: pieces[n] for n in names}
    cliques = {}
    for a, b, c in itertools.combinations(names, 3):
        Ma, Mb, Mc = mats[a], mats[b], mats[c]
        cols_ab = [j for j in range(N_VARS) if not np.array_equal(Ma[:, j], Mb[:, j])]
        cols_bc = [j for j in range(N_VARS) if not np.array_equal(Mb[:, j], Mc[:, j])]
        cols_ac = [j for j in range(N_VARS) if not np.array_equal(Ma[:, j], Mc[:, j])]
        if len(cols_ab) == 1 and len(cols_bc) == 1 and len(cols_ac) == 1 \
                and cols_ab == cols_bc == cols_ac:
            col = cols_ab[0]
            cs = {tuple(Ma[:, col]), tuple(Mb[:, col]), tuple(Mc[:, col])}
            if len(cs) == 3:
                cliques.setdefault(AII_VARS[col], []).append((a, b, c))
    return cliques


def main():
    print("=" * 70)
    print("Day-74 CODE Task B — 25-piece minimal cover verification at n = 5")
    print("=" * 70)

    pieces_27 = load_registry()
    print(f"\nLoaded 27-piece registry: {len(pieces_27)} pieces")
    assert len(pieces_27) == 27

    # Feasibility sanity (Day-70 Thm 4.2 — every piece in registry is feasible).
    aii_pts = enumerate_aii_lattice(6)
    bad_pieces = {}
    for name, M in pieces_27.items():
        infs = verify_piece(M, aii_pts)
        if infs:
            bad_pieces[name] = infs[:2]
    assert not bad_pieces, f"INFEASIBLE pieces: {list(bad_pieces.keys())}"
    print(f"  All 27 pieces feasible on AII sample sum <= 6 ✓")

    # Identify the two pieces to remove.
    print(f"\n[1] Identifying Lemma B k=2 and Lemma C k=2 in the registry:")
    for name in PIECES_TO_REMOVE:
        assert name in pieces_27, f"missing {name}"
    print(f"  Lemma B k=2 piece (P5_P5_dbl_BT2): pi^{{p_5}} = 2(e_{{B_2}} + e_{{T_2}})")
    print(f"  Lemma C k=2 piece (P5_L1_M2dbl):   pi^{{l_1}} = 2 e_{{M_2}} + 3 e_{{B_1}} + e_{{T_1}}")
    print(f"  (Both are multiplicity-2 routings of AXIS columns.)")

    # Coverage at sum <= 4: full vs 25-piece subcover.
    bdi_lattice = enumerate_bdi_lattice(4)
    T5 = set(bdi_lattice)
    print(f"\n[2] BDI lattice T_5 at sum <= 4: |T_5| = {len(T5)}")

    cov_27 = cover_image(pieces_27, 4)
    print(f"  27-piece cover image at sum <= 4: |Im_27| = {len(cov_27)}")
    uncov_27 = T5 - cov_27
    print(f"  Uncovered by 27-piece cover: {len(uncov_27)}")
    if uncov_27:
        print("  Sample uncovered:")
        for q in sorted(uncov_27)[:5]:
            lab = {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}
            print(f"    {lab}")

    # Remove the two multiplicity-2 pieces.
    pieces_25 = {n: M for n, M in pieces_27.items() if n not in PIECES_TO_REMOVE}
    assert len(pieces_25) == 25
    print(f"\n[3] 25-piece subcover (removing Lemma B k=2 and Lemma C k=2):")
    cov_25 = cover_image(pieces_25, 4)
    print(f"  25-piece cover image at sum <= 4: |Im_25| = {len(cov_25)}")
    uncov_25 = T5 - cov_25
    print(f"  Uncovered by 25-piece cover: {len(uncov_25)}")

    # Check: does removing the 2 pieces lose ANY image points compared to 27?
    lost_image = cov_27 - cov_25
    print(f"\n  Image points lost by removal: {len(lost_image)}")
    if not lost_image:
        print(f"  ✓ Lemma B k=2 and Lemma C k=2 are IMAGE-REDUNDANT in the rest")
        print(f"    (their image is fully covered by the other 25 pieces)")
    else:
        print(f"  ✗ Removal LOSES coverage of:")
        for q in sorted(lost_image)[:10]:
            lab = {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}
            print(f"    {lab}")

    # Minimality of 25-piece subcover.
    # We test minimality in the image-redundancy sense: a piece is REDUNDANT iff
    # removing it doesn't reduce the joint image at sum <= 4.
    # (The 27-piece registry does NOT actually cover T_5 — 147 of 395 points
    # at sum<=4 are uncovered. So "minimal" here means image-irredundant in the
    # union image of the remaining 25 pieces.)
    print(f"\n[4] Image-redundancy minimality check (sum <= 4): "
          f"any piece whose image is contained in the rest?")
    image_redundant_pieces = []
    for name in pieces_25:
        sub = {n: M for n, M in pieces_25.items() if n != name}
        cov_sub = cover_image(sub, 4)
        if cov_sub == cov_25:
            image_redundant_pieces.append(name)
    if not image_redundant_pieces:
        print(f"  ✓ 25-piece cover is MINIMAL (image-irredundant) on sum <= 4")
    else:
        print(f"  ⚠ 25-piece cover NOT image-minimal — "
              f"{len(image_redundant_pieces)} further redundant piece(s):")
        for name in image_redundant_pieces:
            print(f"    {name}")

    # Walls W: identify AXIS coordinate-walls.
    print(f"\n[5] Walls (rank-1 piece-pair coordinate hyperplanes) in 25-piece cover:")
    walls = find_rank1_walls(pieces_25)
    coord_walls = {}
    for v, pairs in walls.items():
        nz = [(k, vv) for k, vv in enumerate(v) if vv]
        if len(nz) == 1:
            coord_walls[AII_VARS[nz[0][0]]] = len(pairs)
    print(f"  Coordinate-walls (rank-1 piece-pair counts):")
    for av in sorted(coord_walls.keys()):
        c = coord_walls[av]
        mark = "  [AXIS-by-count >=3]" if c >= 3 else ""
        print(f"    {av:<14} {c} pair(s){mark}")

    axis_strict = [av for av, c in coord_walls.items() if c >= 3]
    print(f"\n  W (coord-walls with >=3 piece-pair collisions): {sorted(axis_strict)}")
    # Day-73 §7 prediction: W = {prefix[1]} only (which is p_1)
    expected_W = ["prefix[1]"]
    if sorted(axis_strict) == sorted(expected_W):
        print(f"  ✓ MATCHES Day-73 §7 prediction: W = {{p_1}}")
    else:
        print(f"  ✗ DIFFERS from Day-73 §7 prediction: expected {sorted(expected_W)}")

    # 3-clique search per wall.
    print(f"\n[6] 3-clique search (triples pairwise rank-1 on the same column):")
    cliques = find_3cliques_per_wall(pieces_25, sum_bound=4)
    for av in sorted(cliques.keys()):
        cls = cliques[av]
        print(f"  Wall {{{av} = 0}}: {len(cls)} 3-clique(s)")
        for tri in cls[:3]:
            print(f"    {tri}")
    if not cliques:
        print("  (no 3-cliques found)")

    # Day-73 §7 prediction: NO 3-cliques on {p_5, l_1} in the 25-piece cover.
    forbidden_walls = ["prefix[5]", "long[1]"]
    has_forbidden = any(av in cliques for av in forbidden_walls)
    if has_forbidden:
        print(f"\n  ✗ Found 3-cliques on forbidden walls "
              f"{[av for av in forbidden_walls if av in cliques]}")
    else:
        print(f"\n  ✓ No 3-cliques on {{p_5, l_1}} — matches Day-73 §7 prediction")

    # Summary
    print("\n" + "=" * 70)
    print("REPORT")
    print("=" * 70)
    out = {
        "T_5_size_sum_le_4": len(T5),
        "cov_27_size": len(cov_27),
        "cov_27_uncovered": len(uncov_27),
        "cov_25_size": len(cov_25),
        "cov_25_uncovered": len(uncov_25),
        "image_lost_by_removing_pieces": len(lost_image),
        "lemma_B_C_image_redundant_in_25": len(lost_image) == 0,
        "25_piece_minimal_on_sum_le_4":
            not image_redundant_pieces,
        "image_redundant_additional": image_redundant_pieces,
        "coord_walls": coord_walls,
        "W_axis_walls": sorted(axis_strict),
        "W_matches_prediction": sorted(axis_strict) == sorted(expected_W),
        "3_cliques_by_wall": {av: len(c) for av, c in cliques.items()},
        "no_3clique_on_p5_l1": not has_forbidden,
    }
    print(json.dumps(out, indent=2))

    out_path = Path(__file__).parent / "results.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
