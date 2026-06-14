"""
Day 70+ — Conjecture D-pi coverage check at n=5.

Goal: determine whether the 27-piece registry (all with canonical
pi^{p_2} = e_{B_2}) actually COVERS every BDI lattice point with small
total mass.  In particular: is there a BDI lattice point that no piece
of the registry hits but that some other feasible piece (with
non-canonical p_2) does hit?

Plan:
  Q1. Enumerate BDI lattice points b in P^BDI_Z with sum(b) <= 4.
      Compute Im(pi) for each of the 27 registry pieces by applying pi
      to all AII lattice points with sum <= 4.  Report covered /
      uncovered, with focus on (B_2, S) = (1, 1) and (1, 2).
  Q2. Build a candidate "refutation" piece by taking the base piece and
      adding (1, p_2) to S (so pi^{p_2} = e_{B_2} + e_S).  Check
      feasibility on AII points sum <= 6 and verify it hits (B_2, S) =
      (1, 1).
  Q3. For each uncovered BDI lattice point, search for a feasible piece
      that hits it with CANONICAL pi^{p_2} = e_{B_2}, pi^{p_3} = e_{B_3}
      (by adjusting other columns).  Partial answer is OK.
"""

import sys
import json
import copy
import itertools
from pathlib import Path

sys.path.insert(0, '/home/agent/projects/code/2026-06-13-n5-axis-count')

import numpy as np
from n5_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS,
                       piece_matrix, verify_piece, enumerate_aii_lattice,
                       bdi_feasible_n5, piece_apply)
from n5_pieces import PIECES, P1, P2, P3, P4, P5, L1, L2, L3, L4, L5, S1, S2, S3, S4, S5


# ---------------------------------------------------------------------
# Enumerate BDI lattice points with sum <= N
# ---------------------------------------------------------------------
def enumerate_bdi_lattice(N_max):
    """All length-12 non-negative integer vectors with sum <= N_max that
    satisfy bdi_feasible_n5."""
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


def labelled_bdi(q):
    return {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}


def labelled_aii(p):
    return {AII_VARS[i]: p[i] for i in range(N_VARS) if p[i] != 0}


# ---------------------------------------------------------------------
# Q1: coverage
# ---------------------------------------------------------------------
def run_q1(N_max=4):
    print("=" * 70)
    print(f"Q1: BDI coverage by 27-piece registry, sum <= {N_max}")
    print("=" * 70)

    bdi_pts = enumerate_bdi_lattice(N_max)
    n_bdi = len(bdi_pts)
    print(f"# BDI lattice points with sum <= {N_max}: {n_bdi}")

    # AII points for evaluating the image of each piece.
    aii_pts = enumerate_aii_lattice(N_max)
    print(f"# AII lattice points with sum <= {N_max}: {len(aii_pts)}")

    # Verify pieces are feasible (use deeper sample).
    deep_pts = enumerate_aii_lattice(5)
    print(f"# AII lattice points with sum <= 5 (used for feasibility): {len(deep_pts)}")

    feasible_pieces = {}
    for name, spec in PIECES.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, deep_pts)
        if not bad:
            feasible_pieces[name] = M
    print(f"# feasible pieces in registry: {len(feasible_pieces)}/{len(PIECES)}")

    # Compute union of images: only keep images with sum <= N_max (the
    # only relevant ones for this check).
    covered = set()
    coverer_of = {}  # b -> list of piece names
    for name, M in feasible_pieces.items():
        for p in aii_pts:
            q = piece_apply(M, p)
            if sum(q) > N_max:
                continue
            if q not in coverer_of:
                coverer_of[q] = []
            coverer_of[q].append(name)
            covered.add(q)

    # Restrict covered set to actual BDI lattice points (they are by
    # construction since piece images are BDI-feasible).
    bdi_set = set(bdi_pts)
    covered_in_bdi = covered & bdi_set
    uncovered = sorted(bdi_set - covered_in_bdi, key=lambda q: (sum(q), q))

    print()
    print(f"# BDI lattice points covered by union of piece images: {len(covered_in_bdi)}")
    print(f"# BDI lattice points NOT covered: {len(uncovered)}")
    print()
    print("UNCOVERED BDI lattice points:")
    for q in uncovered:
        lab = labelled_bdi(q)
        print(f"  sum={sum(q):>2}  {lab}")

    # (d) check specific targets
    B_2_idx = BDI_VARS.index("B_2")
    S_idx = BDI_VARS.index("S")
    target_11 = tuple(1 if i in (B_2_idx, S_idx) else 0 for i in range(N_BDI))
    target_12 = tuple(2 if i == S_idx else (1 if i == B_2_idx else 0) for i in range(N_BDI))

    def is_feasible(q):
        ok, _ = bdi_feasible_n5(q)
        return ok

    print()
    print("Specific targets:")
    for name, t in [("(B_2,S)=(1,1)", target_11), ("(B_2,S)=(1,2)", target_12)]:
        f = is_feasible(t)
        c = t in covered_in_bdi
        coverers = coverer_of.get(t, [])
        print(f"  {name}: feasible={f}, covered={c}, by={coverers}")

    return {
        "n_bdi": n_bdi,
        "n_covered": len(covered_in_bdi),
        "uncovered": uncovered,
        "covered_in_bdi": covered_in_bdi,
        "coverer_of": coverer_of,
        "feasible_pieces": feasible_pieces,
        "target_11_covered": target_11 in covered_in_bdi,
        "target_12_covered": target_12 in covered_in_bdi,
    }


# ---------------------------------------------------------------------
# Q2: candidate refutation piece
# ---------------------------------------------------------------------
def run_q2():
    print()
    print("=" * 70)
    print("Q2: candidate refutation piece (pi^{p_2} = e_{B_2} + e_S)")
    print("=" * 70)

    # Build spec_refute from base piece.
    spec_base = PIECES["P5_base"]
    spec_refute = copy.deepcopy(spec_base)
    # Base already has B_2: [(1, P2), (1, S2), (1, P5)] which contains
    # (1, P2).  Now add (1, P2) to S.
    spec_refute["S"] = list(spec_refute["S"]) + [(1, P2)]

    print("spec_refute (only S and B_2 columns matter):")
    print(f"  B_2: {spec_refute['B_2']}")
    print(f"  S:   {spec_refute['S']}")

    M_refute = piece_matrix(spec_refute)
    # Show the p_2 column
    P2_idx = AII_VARS.index(P2)
    col_p2 = tuple(int(M_refute[r, P2_idx]) for r in range(N_BDI))
    print(f"  pi^{{p_2}} column = {labelled_bdi(col_p2)}")

    # (a) feasibility
    deep_pts = enumerate_aii_lattice(6)
    print(f"  # AII pts sum<=6 used for feasibility: {len(deep_pts)}")
    bad = verify_piece(M_refute, deep_pts)
    print(f"  # infeasibilities: {len(bad)}")
    if bad:
        for p, q, err in bad[:5]:
            print(f"    p={labelled_aii(p)} -> q={labelled_bdi(q)} err={err}")
    feasible = (len(bad) == 0)

    # (b) image hits (B_2, S) = (1, 1)?
    aii_pts4 = enumerate_aii_lattice(4)
    B_2_idx = BDI_VARS.index("B_2")
    S_idx = BDI_VARS.index("S")
    target_11 = tuple(1 if i in (B_2_idx, S_idx) else 0 for i in range(N_BDI))

    hits_11 = False
    hits_11_preimage = None
    for p in aii_pts4:
        q = piece_apply(M_refute, p)
        if q == target_11:
            hits_11 = True
            hits_11_preimage = p
            break

    print(f"  Hits (B_2,S)=(1,1)? {hits_11}")
    if hits_11:
        print(f"    preimage: {labelled_aii(hits_11_preimage)}")
        # Apply once to verify
        q_check = piece_apply(M_refute, hits_11_preimage)
        print(f"    image:    {labelled_bdi(q_check)}")

    return {
        "feasible": feasible,
        "n_infeasibilities": len(bad),
        "hits_11": hits_11,
        "hits_11_preimage": hits_11_preimage,
        "spec": spec_refute,
        "matrix": M_refute,
    }


# ---------------------------------------------------------------------
# Q3: can we hit each uncovered point with canonical p_2, p_3?
# ---------------------------------------------------------------------
def run_q3(uncovered, feasible_pieces_dict, aii_pts):
    print()
    print("=" * 70)
    print("Q3: for each uncovered BDI point, search for a feasible piece")
    print("    with canonical pi^{p_2}=e_{B_2}, pi^{p_3}=e_{B_3}")
    print("=" * 70)

    # Strategy: build "canonical" variant pieces by tweaking one column
    # at a time of the base piece (or other registry pieces).  The 27
    # registry pieces ALREADY all have canonical p_2.  Per dpi_check,
    # they also all have canonical p_3 (RIGID).  So the registry is the
    # canonical-p_2,p_3 set.  Any uncovered point requires *non*-registry
    # tweaks while preserving p_2 and p_3 columns.
    #
    # Try: take each registry piece, perturb one of the OTHER columns
    # (p_1, p_4, p_5, L_1..L_5, S_1..S_5) by adding a single BDI basis
    # vector e_v (v in BDI_VARS).  Check feasibility & whether new image
    # hits the target.

    BDI_BASIS = list(range(N_BDI))
    AII_COLS_TO_PERTURB = [i for i in range(N_VARS)
                            if AII_VARS[i] != "prefix[2]" and AII_VARS[i] != "prefix[3]"]
    # We want canonical p_2 = e_{B_2} and p_3 = e_{B_3}, so don't perturb
    # those columns.

    deep_pts = enumerate_aii_lattice(4)  # speed: use sum<=4 for Q3 search
    P2_idx = AII_VARS.index("prefix[2]")
    P3_idx = AII_VARS.index("prefix[3]")
    B_2_idx = BDI_VARS.index("B_2")
    B_3_idx = BDI_VARS.index("B_3")

    def has_canonical_p2_p3(M):
        col_p2 = M[:, P2_idx]
        col_p3 = M[:, P3_idx]
        e_B2 = np.zeros(N_BDI, dtype=int); e_B2[B_2_idx] = 1
        e_B3 = np.zeros(N_BDI, dtype=int); e_B3[B_3_idx] = 1
        return np.array_equal(col_p2, e_B2) and np.array_equal(col_p3, e_B3)

    # First confirm registry has canonical p_2, p_3.
    n_canonical = sum(1 for M in feasible_pieces_dict.values() if has_canonical_p2_p3(M))
    print(f"  Registry pieces with canonical p_2 AND p_3: {n_canonical}/{len(feasible_pieces_dict)}")

    # Subset of pieces to perturb: just the base piece (keeps Q3 quick).
    # This is a "partial" answer per the spec.
    base_pieces = {"P5_base": feasible_pieces_dict["P5_base"]}

    results = {}
    for q_idx, q_target in enumerate(uncovered):
        lab_target = labelled_bdi(q_target)

        found_piece = None
        # Try each base piece + single-column single-basis perturbation.
        for piece_name, M in base_pieces.items():
            for col_idx in AII_COLS_TO_PERTURB:
                for b in BDI_BASIS:
                    M_new = M.copy()
                    M_new[b, col_idx] += 1
                    if not has_canonical_p2_p3(M_new):
                        continue
                    bad = verify_piece(M_new, deep_pts)
                    if bad:
                        continue
                    # Search image
                    hit = False
                    for p in aii_pts:
                        if piece_apply(M_new, p) == q_target:
                            hit = True
                            break
                    if hit:
                        found_piece = (piece_name, AII_VARS[col_idx],
                                        BDI_VARS[b])
                        break
                if found_piece:
                    break
            if found_piece:
                break

        if found_piece:
            results[q_target] = ("yes", found_piece)
            tag = "YES"
        else:
            results[q_target] = ("no", None)
            tag = "no "
        if q_idx < 25 or found_piece:
            print(f"  [{tag}] {lab_target}" +
                  (f"  via '{found_piece[0]}' +e_{{{found_piece[2]}}} on {found_piece[1]}" if found_piece else ""))

    n_yes = sum(1 for v in results.values() if v[0] == "yes")
    print(f"\n  Summary: {n_yes}/{len(uncovered)} uncovered points coverable "
           f"by single-column perturbation of base piece (keeping canonical p_2,p_3).")
    return results


# ---------------------------------------------------------------------
# Main + write results.txt
# ---------------------------------------------------------------------
def main():
    out_dir = Path("/home/agent/projects/code/2026-06-16-dpi-coverage-check")
    out_dir.mkdir(exist_ok=True)

    q1 = run_q1(N_max=4)
    q2 = run_q2()
    aii_pts4 = enumerate_aii_lattice(4)
    q3 = run_q3(q1["uncovered"], q1["feasible_pieces"], aii_pts4)

    # Save results.txt
    with open(out_dir / "results.txt", "w") as f:
        f.write("Conjecture D-pi coverage check at n=5\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Q1(a) # BDI lattice points with sum <= 4: {q1['n_bdi']}\n")
        f.write(f"Q1(b) # covered by 27-piece registry:    {q1['n_covered']}\n")
        f.write(f"Q1(c) Uncovered points ({len(q1['uncovered'])}):\n")
        for q in q1["uncovered"]:
            f.write(f"        sum={sum(q):>2}  {labelled_bdi(q)}\n")
        f.write(f"Q1(d) (B_2,S)=(1,1) covered? {q1['target_11_covered']}\n")
        f.write(f"      (B_2,S)=(1,2) covered? {q1['target_12_covered']}\n\n")

        f.write(f"Q2(a) refutation piece feasible (sum<=6)?: "
                 f"{q2['feasible']} (# infeasibilities: {q2['n_infeasibilities']})\n")
        f.write(f"Q2(b) refutation piece hits (B_2,S)=(1,1)?: {q2['hits_11']}\n")
        if q2["hits_11"]:
            f.write(f"      preimage: {labelled_aii(q2['hits_11_preimage'])}\n")
        f.write(f"Q2(c) 27-piece registry covers (B_2,S)=(1,1)? "
                 f"{q1['target_11_covered']}\n")
        f.write(f"      => refutation piece covers it but registry does not? "
                 f"{q2['hits_11'] and not q1['target_11_covered']}\n\n")

        f.write("Q3 results (single-column perturbation search):\n")
        for q, (status, info) in q3.items():
            f.write(f"  {labelled_bdi(q)}: {status}")
            if info:
                f.write(f"  via '{info[0]}' + e_{{{info[2]}}} on col {info[1]}")
            f.write("\n")

    print()
    print(f"results.txt written to {out_dir/'results.txt'}")


if __name__ == "__main__":
    main()
