#!/usr/bin/env python3
"""
Cross-check: are the Task-A witness pieces actually OUTSIDE the n=6
augmented registry?

The witness pieces are 'minimal' pieces (mostly zero columns) that
realize T = e_{B_i} + alpha * e_S as a non-p_i ray.  If they ARE in
the registry then Task A's YES is not 'new'; if they are NOT in the
registry then the registry mis-classified them.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from bdi_n import (
    bdi_coords, vec, add, scale, zero_piece, target_point,
    check_F, gen_set, all_cols, piece_to_human,
)
from task_B_replicate import load_n6_pieces_linkLHS_zero


def piece_signature(n: int, piece: dict) -> tuple:
    """Hashable signature: sorted tuple of (col_name, col_tuple)."""
    return tuple(sorted((c, piece[c]) for c in all_cols(n)))


def main():
    n = 6
    print(f"Loading n=6 registry ...")
    reg_pieces = load_n6_pieces_linkLHS_zero()
    reg_sigs = {piece_signature(n, p): name for name, p in reg_pieces.items()}
    print(f"  {len(reg_pieces)} pieces in registry.")

    # Build the canonical 'split_BS' witness for each (i, alpha) via the
    # p_{j-1} + l_j route with j = 1 case (set p_0 = ... — actually use j=2
    # which sets p_1 = e_{B_i} and l_2 = alpha e_S; minimal otherwise).
    out = {"witnesses": []}
    for i in (2, 3, 4):
        for alpha in (1, 2):
            T = target_point(n, i, alpha)
            # Build the lifted-long witness via the "split_BS" decomp at j=2:
            # p_1 = e_{B_i}, l_2 = alpha * e_S, everything else zero.
            piece = zero_piece(n)
            piece["p1"] = vec(n, **{f"B{i}": 1})
            piece["l2"] = scale(alpha, vec(n, S=1))
            assert check_F(n, piece), f"witness must be F-feasible at i={i}, a={alpha}"
            assert add(piece["p1"], piece["l2"]) == T
            assert piece[f"p{i}"] != T
            sig = piece_signature(n, piece)
            in_registry = sig in reg_sigs
            out["witnesses"].append({
                "i": i,
                "alpha": alpha,
                "route": "lifted-long p_1 + l_2 (split_BS)",
                "witness_columns": piece_to_human(n, piece),
                "in_registry": in_registry,
                "registry_name": reg_sigs.get(sig, None),
            })
            print(f"  i={i}, alpha={alpha}: "
                  f"witness {{p_1=e_B{i}, l_2={alpha}*e_S}} "
                  f"-- in registry? {in_registry}")

            # Also build the lifted-short witness via "split_BS" at j=2 with s_2:
            piece2 = zero_piece(n)
            piece2["p1"] = vec(n, **{f"B{i}": 1})
            piece2["s2"] = scale(alpha, vec(n, S=1))
            assert check_F(n, piece2)
            assert add(piece2["p1"], piece2["s2"]) == T
            assert piece2[f"p{i}"] != T
            sig2 = piece_signature(n, piece2)
            in_registry2 = sig2 in reg_sigs
            out["witnesses"].append({
                "i": i,
                "alpha": alpha,
                "route": "lifted-short p_1 + s_2 (split_BS)",
                "witness_columns": piece_to_human(n, piece2),
                "in_registry": in_registry2,
                "registry_name": reg_sigs.get(sig2, None),
            })
            print(f"               witness {{p_1=e_B{i}, s_2={alpha}*e_S}} "
                  f"-- in registry? {in_registry2}")

    # Summary.
    n_in = sum(1 for w in out["witnesses"] if w["in_registry"])
    n_out = sum(1 for w in out["witnesses"] if not w["in_registry"])
    print(f"\nWitnesses in registry: {n_in}")
    print(f"Witnesses OUTSIDE registry: {n_out}")
    print(f"\nUpshot: the YES answer relies on pieces "
          f"{'inside' if n_out == 0 else 'OUTSIDE'} the 53-piece registry.")
    out["n_in_registry"] = n_in
    out["n_outside_registry"] = n_out

    with open(HERE / "witness_outside_registry.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'witness_outside_registry.json'}")


if __name__ == "__main__":
    main()
