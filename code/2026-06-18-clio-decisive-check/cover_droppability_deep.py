#!/usr/bin/env python3
"""
Deeper droppability analysis (Day 78 stretch, follow-up).

The shallow check (cover_droppability.py at max_sum=6) returned
"fully droppable, zero losses" at every interior (i, alpha) for both
lifted-long and lifted-short witnesses.

To confirm this isn't an artifact of the truncation, we do two things:

(1) Push max_sum to 8 and 10, see if losses appear.
(2) For each (i, alpha), identify the CARRIER-UNIQUE RAYS: which of
    the carrier piece's 17 rays are NOT already in the semigroup of
    the OTHER 52 pieces. These are the only rays that the witness
    needs to compensate for.
(3) Check that each carrier-unique ray IS in the semigroup of the
    modified cover (52 - carriers + witness).

If (3) holds at every (i, alpha) with the witness's tiny image, the
droppability is structural, not numerical luck.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from bdi_n import (
    bdi_coords, vec, add, scale, zero_piece, target_point,
    gen_set, check_F, piece_to_human, semigroup_membership,
)
from task_B_replicate import load_n6_pieces_linkLHS_zero
from cover_droppability import (
    joint_image_set, joint_generators,
    lifted_long_witness, lifted_short_witness,
)

N = 6


def carrier_unique_rays(pieces: dict, carriers: list[str]) -> list[tuple]:
    """Rays of the carrier piece(s) that are NOT in the semigroup of
    the OTHER 52 pieces."""
    others = [p for name, p in pieces.items() if name not in carriers]
    other_gens = joint_generators(others)
    # Use sum bound 8 for the membership test (carrier rays have small sums).
    other_image = joint_image_set(other_gens, max_sum=8)

    unique = []
    carrier_rays = set()
    for name in carriers:
        for g in gen_set(N, pieces[name]):
            carrier_rays.add(g)
    for g in carrier_rays:
        if sum(g) > 8:
            # Fall back to recursive membership.
            if not semigroup_membership(N, g, other_gens, max_coef=4):
                unique.append(g)
        else:
            if g not in other_image:
                unique.append(g)
    return unique


def main():
    print("=" * 76)
    print("Deeper droppability analysis (Day 78 stretch follow-up)")
    print("=" * 76)

    pieces = load_n6_pieces_linkLHS_zero()
    print(f"\nLoaded {len(pieces)} pieces.")

    out = {"by_i_alpha": {}, "summary": {}}

    # ---- Carrier-unique rays + witness-supplies-them check ----
    print(f"\n{'-' * 60}")
    print(f"Step 1: identify carrier-unique rays per (i, alpha)")
    print(f"{'-' * 60}")
    for i in (2, 3, 4):
        for alpha in (1, 2):
            T = target_point(N, i, alpha)
            carriers = [
                name for name, p in pieces.items() if p[f"p{i}"] == T
            ]
            print(f"\n(i={i}, alpha={alpha}): T = e_B{i} + {alpha} e_S")
            print(f"  carriers: {carriers}")
            unique = carrier_unique_rays(pieces, carriers)
            print(f"  carrier-unique rays (not in semigroup of 52 others): "
                  f"{len(unique)}")
            for r in unique:
                rstr = {c: r[k] for k, c in enumerate(bdi_coords(N)) if r[k]}
                print(f"    {rstr}  (sum={sum(r)})")

            # Witness-supplies-them check.
            other_gens = joint_generators(
                [p for name, p in pieces.items() if name not in carriers]
            )
            ll_witness = lifted_long_witness(i, alpha)
            ls_witness = lifted_short_witness(i, alpha)

            # Image of (others + witness) up to sum 8.
            mod_long_gens = list(set(other_gens + gen_set(N, ll_witness)))
            mod_short_gens = list(set(other_gens + gen_set(N, ls_witness)))
            mod_long_img = joint_image_set(mod_long_gens, max_sum=8)
            mod_short_img = joint_image_set(mod_short_gens, max_sum=8)

            long_covers = all(
                (r in mod_long_img if sum(r) <= 8
                 else semigroup_membership(N, r, mod_long_gens, max_coef=4))
                for r in unique
            )
            short_covers = all(
                (r in mod_short_img if sum(r) <= 8
                 else semigroup_membership(N, r, mod_short_gens, max_coef=4))
                for r in unique
            )
            print(f"  lifted-long witness covers all unique rays: {long_covers}")
            print(f"  lifted-short witness covers all unique rays: {short_covers}")

            key = f"i={i}_alpha={alpha}"
            out["by_i_alpha"][key] = {
                "carriers": carriers,
                "n_carrier_unique_rays": len(unique),
                "carrier_unique_rays": [
                    {
                        "vec": r,
                        "coords": {c: r[k] for k, c in enumerate(bdi_coords(N)) if r[k]},
                        "sum": sum(r),
                    }
                    for r in unique
                ],
                "lifted_long_covers_all_unique": long_covers,
                "lifted_short_covers_all_unique": short_covers,
            }

    # ---- Deep image check at max_sum 8 ----
    print(f"\n{'-' * 60}")
    print(f"Step 2: deep droppability at max_sum = 8")
    print(f"{'-' * 60}")
    t0 = time.time()
    full_gens = joint_generators(pieces.values())
    full_image_8 = joint_image_set(full_gens, max_sum=8)
    print(f"  |Im(full cover) <= sum 8| = {len(full_image_8)}  "
          f"({time.time() - t0:.1f}s)")

    deep_results = []
    for i in (2, 3, 4):
        for alpha in (1, 2):
            T = target_point(N, i, alpha)
            carriers = [
                name for name, p in pieces.items() if p[f"p{i}"] == T
            ]
            others = [p for name, p in pieces.items() if name not in carriers]
            for wkind, W in (("lifted_long", lifted_long_witness(i, alpha)),
                              ("lifted_short", lifted_short_witness(i, alpha))):
                mod = others + [W]
                mg = joint_generators(mod)
                mi = joint_image_set(mg, max_sum=8)
                losses = full_image_8 - mi
                losses_sorted = sorted(losses, key=lambda v: (sum(v), v))
                deep_results.append({
                    "i": i, "alpha": alpha, "witness_kind": wkind,
                    "max_sum": 8,
                    "n_losses": len(losses),
                    "smallest_losses": [
                        {
                            "vec": v,
                            "coords": {c: v[k] for k, c in enumerate(bdi_coords(N)) if v[k]},
                            "sum": sum(v),
                        }
                        for v in losses_sorted[:5]
                    ],
                    "covers_all": len(losses) == 0,
                })
                print(f"  i={i}, alpha={alpha}, {wkind}: losses={len(losses)} "
                      f"covers_all={len(losses) == 0}")

    out["deep_results_max_sum_8"] = deep_results

    # Summary.
    print(f"\n{'=' * 76}")
    print("SUMMARY (deep)")
    print(f"{'=' * 76}")
    all_drop_8 = all(r["covers_all"] for r in deep_results)
    print(f"All carriers droppable at max_sum=8 (every witness kind): "
          f"{all_drop_8}")
    out["summary"]["all_droppable_max_sum_8"] = all_drop_8

    with open(HERE / "cover_droppability_deep_results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'cover_droppability_deep_results.json'}")


if __name__ == "__main__":
    main()
