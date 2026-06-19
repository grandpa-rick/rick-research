#!/usr/bin/env python3
"""
Universal droppability check for Day-79 Tasks 1, 2, 3.

Handles BOTH n=6 (even, with linkLHS) and n=7 (odd).

For each (n, i, alpha):
  - Identify carriers (pieces in registry with prefix[i] = T = e_{B_i} + alpha e_S)
  - Build witness pieces (lifted-long, lifted-short, pure-prefix, ...)
  - Check joint-image preservation: Im(registry - carriers + witness) ⊇ Im(registry)

Reports per (n, i, alpha, witness_kind):
  - whether carrier exists
  - whether witness is F-feasible
  - joint image size (orig vs modified) at max_sum cap
  - n_losses
  - whether T is still in modified image
"""
from __future__ import annotations
import json
import time
from pathlib import Path

import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from bdi_universal import (
    bdi_coords, vec, add, scale, zero_vec, zero_piece, piece_columns,
    target_point, coord_dict, is_BDI,
    aii_rays, ray_image, gen_set, check_F,
    load_registry, joint_generators, joint_image_set, semigroup_membership,
)


# ===================================================================
# Witness constructions
# ===================================================================
def lifted_long_witness(n: int, i: int, alpha: int) -> dict:
    """W = {prefix[1] = e_{B_i}, long[2] = alpha * e_S, rest 0}."""
    piece = zero_piece(n)
    piece["prefix[1]"] = vec(n, **{f"B{i}": 1})
    piece["long[2]"] = scale(alpha, vec(n, S=1))
    return piece


def lifted_short_witness(n: int, i: int, alpha: int) -> dict:
    """W = {prefix[1] = e_{B_i}, short[2] = alpha * e_S, rest 0}."""
    piece = zero_piece(n)
    piece["prefix[1]"] = vec(n, **{f"B{i}": 1})
    piece["short[2]"] = scale(alpha, vec(n, S=1))
    return piece


def pure_prefix_witness(n: int, i: int, alpha: int) -> dict:
    """W = {prefix[i] = e_{B_i} + alpha e_S, rest 0}.

    This is the 'classical' carrier — image is T as ray 1.
    Returned for comparison; if used as 'replacement', it IS the carrier,
    so this doesn't represent dropping.
    """
    piece = zero_piece(n)
    piece[f"prefix[{i}]"] = target_point(n, i, alpha)
    return piece


# ===================================================================
# Carrier identification
# ===================================================================
def find_carriers(pieces: dict, n: int, i: int, alpha: int) -> list[str]:
    """Names of pieces with prefix[i] = T = e_{B_i} + alpha e_S."""
    T = target_point(n, i, alpha)
    return [name for name, p in pieces.items() if p[f"prefix[{i}]"] == T]


# ===================================================================
# Single (n, i, alpha) droppability check
# ===================================================================
def droppability_check(pieces: dict, n: int, i: int, alpha: int,
                       witness_kind: str, max_sum: int,
                       original_image: set | None = None,
                       original_gens: list | None = None) -> dict:
    """Check whether (i, alpha) carrier(s) can be replaced by witness."""
    T = target_point(n, i, alpha)
    carriers = find_carriers(pieces, n, i, alpha)

    # Construct witness
    if witness_kind == "lifted_long":
        W = lifted_long_witness(n, i, alpha)
    elif witness_kind == "lifted_short":
        W = lifted_short_witness(n, i, alpha)
    elif witness_kind == "pure_prefix":
        W = pure_prefix_witness(n, i, alpha)
    else:
        raise ValueError(witness_kind)

    w_feasible = check_F(n, W)

    # Modified cover
    others = {name: p for name, p in pieces.items() if name not in carriers}
    modified_pieces = list(others.values()) + [W]
    mod_gens = joint_generators(modified_pieces, n)
    mod_image = joint_image_set(mod_gens, n, max_sum=max_sum)

    # Compute original image if not given
    if original_image is None:
        full_gens = joint_generators(pieces.values(), n)
        original_image = joint_image_set(full_gens, n, max_sum=max_sum)

    losses = original_image - mod_image
    losses_sorted = sorted(losses, key=lambda v: (sum(v), v))

    return {
        "n": n,
        "i": i,
        "alpha": alpha,
        "witness_kind": witness_kind,
        "carrier_names": carriers,
        "n_carriers": len(carriers),
        "T_coords": coord_dict(n, T),
        "witness_F_feasible": w_feasible,
        "max_sum": max_sum,
        "original_image_size": len(original_image),
        "modified_image_size": len(mod_image),
        "n_losses": len(losses),
        "smallest_losses": [
            {"vec": v, "coords": coord_dict(n, v), "sum": sum(v)}
            for v in losses_sorted[:10]
        ],
        "covers_all": len(losses) == 0,
        "T_in_modified_image": T in mod_image,
    }


def run_battery(n: int, i_range, alpha_range, witness_kinds,
                max_sum: int) -> dict:
    """Run droppability check for all (i, alpha, witness_kind) combinations."""
    print(f"\n{'='*72}")
    print(f"n = {n}: i in {list(i_range)}, alpha in {list(alpha_range)}, "
          f"witnesses {witness_kinds}, max_sum={max_sum}")
    print(f"{'='*72}")
    pieces = load_registry(n)
    print(f"Loaded {len(pieces)} pieces from registry-n{n}.json")
    print(f"F-feasibility: "
          f"{sum(1 for p in pieces.values() if check_F(n, p))}/{len(pieces)}")

    print(f"\nEnumerating joint image of full cover up to coord-sum {max_sum}")
    t0 = time.time()
    full_gens = joint_generators(pieces.values(), n)
    full_image = joint_image_set(full_gens, n, max_sum)
    print(f"  {len(full_gens)} distinct ray-image generators; "
          f"|Im(cover) <= sum {max_sum}| = {len(full_image)}  "
          f"({time.time()-t0:.1f}s)")

    results = []
    for i in i_range:
        for alpha in alpha_range:
            for wk in witness_kinds:
                t0 = time.time()
                r = droppability_check(pieces, n, i, alpha, wk, max_sum,
                                       original_image=full_image)
                dt = time.time() - t0
                results.append(r)
                ok = "DROPPABLE" if r["covers_all"] else "NOT-DROPPABLE"
                wf = "F-OK" if r["witness_F_feasible"] else "W-NOT-F"
                ncar = r["n_carriers"]
                print(f"  i={i} alpha={alpha} {wk:>14}: "
                      f"carriers={ncar} witness={wf} "
                      f"losses={r['n_losses']:3d} T_in_mod={r['T_in_modified_image']} "
                      f"{ok}  ({dt:.1f}s)")
                if not r["covers_all"] and r["smallest_losses"]:
                    for L in r["smallest_losses"][:3]:
                        print(f"     LOSS sum={L['sum']}: {L['coords']}")

    return {
        "n": n,
        "max_sum": max_sum,
        "n_pieces": len(pieces),
        "n_distinct_rays": len(full_gens),
        "original_image_size": len(full_image),
        "results": results,
    }


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=7)
    ap.add_argument("--i", type=str, default="2,3,4,5")
    ap.add_argument("--alpha", type=str, default="1,2")
    ap.add_argument("--witness", type=str,
                    default="lifted_long,lifted_short")
    ap.add_argument("--max-sum", type=int, default=8)
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    i_range = [int(x) for x in args.i.split(",")]
    alpha_range = [int(x) for x in args.alpha.split(",")]
    witness_kinds = args.witness.split(",")

    out = run_battery(args.n, i_range, alpha_range, witness_kinds, args.max_sum)
    if args.out:
        with open(args.out, "w") as f:
            json.dump(out, f, indent=2, default=str)
        print(f"\nWrote {args.out}")
