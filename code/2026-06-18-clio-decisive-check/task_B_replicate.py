#!/usr/bin/env python3
"""
Task B: replicate Clio's section 3 "minus-its-carrier" check at n = 6.

For each interior i in {2, 3, 4} and each alpha in {1, 2}, compute
the joint image of (53-piece cover) MINUS the simpdiv carrier
`simpdiv_p{i}_a{alpha}` (and, for alpha=1, also MINUS `aux_class1_p{i}`).
Check whether T = e_{B_i} + alpha * e_S is still in the joint semigroup.

Expected per Clio: NO at every interior i, alpha in {1, 2}.

We use the support-reduction lemma (proven in decisive_check.py):
T in semigroup iff some ray of the cover equals T.  So we just need
to check whether any ray of any cover piece (other than the carrier)
equals T.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from bdi_n import (
    bdi_coords, bdi_idx, vec, add, target_point, gen_set, all_cols,
    is_BDI, check_F, zero_piece,
)

REG_PATH = Path("/home/agent/projects/code/2026-06-17-complete-registry/registry-n6.json")


def load_n6_pieces_linkLHS_zero() -> dict:
    """Load registry-n6.json and gauge linkLHS to zero.

    Registry format: {piece_name: {aii_var_name: [list of 15 ints]}}
    AII var names: prefix[1..6], long[1..6], short[1..5], linkLHS.

    Returns: {piece_name: {col_name: bdi_vec_tuple}}, with
        col_name in {p1..p6, l1..l6, s1..s5}.
    In linkLHS = 0 gauge, short[j] is shifted by old linkLHS.
    """
    with open(REG_PATH) as f:
        reg = json.load(f)
    pieces = {}
    for name, cols_dict in reg.items():
        linkLHS = tuple(cols_dict["linkLHS"])
        piece = {}
        for j in range(1, 7):
            piece[f"p{j}"] = tuple(cols_dict[f"prefix[{j}]"])
            piece[f"l{j}"] = tuple(cols_dict[f"long[{j}]"])
        for j in range(1, 6):
            base_sj = tuple(cols_dict[f"short[{j}]"])
            piece[f"s{j}"] = add(base_sj, linkLHS)
        pieces[name] = piece
    return pieces


def cover_minus_carrier_check(n: int, i: int, alpha: int,
                              pieces: dict) -> dict:
    """For the 53-piece cover, remove the carrier(s) of T = e_{B_i}+alpha*e_S
    and check whether T appears as a ray of any remaining piece."""
    T = target_point(n, i, alpha)
    # Identify the carriers (pieces whose p_i column == T):
    carriers = []
    for name, piece in pieces.items():
        if piece[f"p{i}"] == T:
            carriers.append(name)

    # Remove carriers and gather all rays from remaining pieces.
    remaining_pieces = {n: p for n, p in pieces.items() if n not in carriers}
    T_in_some_ray = []  # (piece_name, ray_index)
    for name, piece in remaining_pieces.items():
        rays = gen_set(n, piece)
        for k, r in enumerate(rays):
            if r == T:
                T_in_some_ray.append((name, k))

    return {
        "i": i,
        "alpha": alpha,
        "target_T_coords": {c: T[k] for k, c in enumerate(bdi_coords(n)) if T[k]},
        "carrier_piece_names": carriers,
        "n_remaining_pieces": len(remaining_pieces),
        "T_appears_as_ray_in_remaining": T_in_some_ray,
        "answer_T_covered_after_removal": len(T_in_some_ray) > 0,
    }


def main():
    print("=" * 76)
    print("Task B: Clio's section 3 'cover-minus-carrier' replication")
    print(f"  Registry: {REG_PATH.name}")
    print("=" * 76)

    pieces = load_n6_pieces_linkLHS_zero()
    print(f"\nLoaded {len(pieces)} pieces from registry.")

    # Sanity check each piece is F-feasible in linkLHS=0 gauge.
    n = 6
    n_feasible = sum(1 for p in pieces.values() if check_F(n, p))
    print(f"F-feasible (in linkLHS=0 gauge): {n_feasible}/{len(pieces)}")

    # Run check for each (i, alpha).
    out = {"by_i_alpha": {}}
    for i in (2, 3, 4):
        for alpha in (1, 2):
            res = cover_minus_carrier_check(n, i, alpha, pieces)
            key = f"i={i}_alpha={alpha}"
            out["by_i_alpha"][key] = res
            ans = "YES (covered)" if res["answer_T_covered_after_removal"] else "NO (uncovered)"
            print(f"\n  i={i}, alpha={alpha}: T = {res['target_T_coords']}")
            print(f"    Carriers in registry: {res['carrier_piece_names']}")
            print(f"    After removing carriers ({res['n_remaining_pieces']} "
                  f"pieces remain): T covered = {ans}")
            if res["T_appears_as_ray_in_remaining"]:
                for name, k in res["T_appears_as_ray_in_remaining"]:
                    print(f"      via {name} ray index {k}")

    # Verdict: matches Clio's prediction (NO at every interior, alpha).
    all_uncovered = all(
        not r["answer_T_covered_after_removal"]
        for r in out["by_i_alpha"].values()
    )
    print(f"\n{'=' * 76}")
    print(f"Clio's prediction (T uncovered after removing carrier): "
          f"{'CONFIRMED' if all_uncovered else 'REFUTED'} for all (i, alpha)")
    print(f"{'=' * 76}")
    out["clio_prediction_confirmed"] = all_uncovered

    with open(HERE / "task_B_results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'task_B_results.json'}")


if __name__ == "__main__":
    main()
