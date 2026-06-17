#!/usr/bin/env python3
"""
Day 76 CODE Task A SUPPLEMENT 2 -- joint-cover containment.

For each F-feasible piece (under Day-70 §6 RIGID/BINARY restrictions) with
pi^{p_i} = e_{B_i} + alpha * e_S for some interior i, check whether
Im(piece) is contained in the JOINT image of the n=6 augmented registry
(the 53 pieces of the Day-72 cover combined).

This is the analog of the Day-74 n=5 check that found "3456 / 4320 pieces
image-contained in the reference cover's joint image."

A piece contained in the joint cover image is "explained" by the cover.
A piece NOT contained reveals a NEW image direction beyond the cover.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from d_pi_uniqueness_n6 import (
    load_registry_n6, simpdiv_piece, gen_set_n6_r, check_F_n6_r,
    add_r, vec_r, scale_r, BDI_COORDS_REG, NB_REG, ZERO_REG,
    enumerate_image_set, semigroup_membership,
    enumerate_feasible_pieces, candidate_columns_for_enum,
    get_base_piece_n6, image_signature,
)

HERE = Path(__file__).resolve().parent


def main():
    print("=" * 76)
    print("Day 76 CODE Task A SUPPLEMENT 2 -- joint-cover containment at n=6")
    print("=" * 76)

    base = get_base_piece_n6()
    cands = candidate_columns_for_enum(base)

    # Joint cover generators: union of all 53 pieces' generators.
    pieces = load_registry_n6()
    print(f"\nLoaded n=6 registry: {len(pieces)} pieces")
    joint_gens = set()
    for name, piece in pieces.items():
        for g in gen_set_n6_r(piece):
            joint_gens.add(g)
    print(f"Joint-cover generators: {len(joint_gens)} distinct")

    # Enumerate joint cover's image semigroup up to sum 8.
    print(f"\nEnumerating joint-cover image up to sum 8 ...")
    t0 = time.time()
    joint_image = enumerate_image_set(joint_gens, max_total=8)
    el = time.time() - t0
    print(f"|Im(joint cover) up to sum 8| = {len(joint_image)} "
          f"(enum time {el:.1f}s)")

    interior = [2, 3, 4]
    results = {"interior": interior, "by_i": {}}
    overall_pass = True

    for i in interior:
        print(f"\n{'=' * 60}")
        print(f"Interior coord p_{i}")
        print(f"{'=' * 60}")
        per_alpha = {}
        for alpha in range(3):
            print(f"\n  --- alpha = {alpha} (pi^{{p_{i}}} = e_{{B_{i}}} + "
                  f"{alpha} e_S) ---")
            t0 = time.time()
            feasible = enumerate_feasible_pieces(base, i, alpha, cands)
            enum_t = time.time() - t0
            print(f"    F-feasible: {len(feasible)} ({enum_t:.1f}s)")

            # Bucket by signature.
            sig_count = {}
            for piece in feasible:
                sig = image_signature(piece)
                sig_count[sig] = sig_count.get(sig, 0) + 1
            print(f"    Distinct signatures: {len(sig_count)}")

            # Check joint-cover containment.
            t0 = time.time()
            contained = 0
            not_contained = 0
            not_contained_examples = []
            for sig, cnt in sig_count.items():
                ok = all(g in joint_image for g in sig if sum(g) <= 8)
                # For high-sum generators, fall back to recursive membership
                # (none expected at this enumeration's scale).
                if ok:
                    for g in sig:
                        if sum(g) > 8:
                            if not semigroup_membership(g, list(joint_gens),
                                                         max_coef=6):
                                ok = False
                                break
                if ok:
                    contained += cnt
                else:
                    not_contained += cnt
                    if len(not_contained_examples) < 5:
                        not_contained_examples.append(sig)
            chk_t = time.time() - t0
            print(f"    Joint-cover-contained: {contained}/{len(feasible)} "
                  f"({100*contained/len(feasible):.1f}%)")
            print(f"    NOT-contained:         {not_contained}/{len(feasible)} "
                  f"({100*not_contained/len(feasible):.1f}%)")
            print(f"    (check time: {chk_t:.1f}s)")
            per_alpha[alpha] = {
                "n_feasible": len(feasible),
                "n_distinct_signatures": len(sig_count),
                "n_joint_contained": contained,
                "n_joint_not_contained": not_contained,
                "pct_contained": 100 * contained / len(feasible),
            }

        # Acceptance: high fraction contained in cover (>90% as a rough cut).
        all_above_90 = all(per_alpha[a]["pct_contained"] >= 90.0
                            for a in range(3))
        verdict = "PASS" if all_above_90 else "FAIL"
        print(f"\n  VERDICT (p_{i}, joint-cover containment >= 90%): {verdict}")
        if not all_above_90:
            overall_pass = False
        results["by_i"][i] = {"per_alpha": per_alpha, "verdict": verdict}

    results["overall_pass"] = overall_pass
    print(f"\n{'=' * 76}")
    print(f"OVERALL VERDICT (joint-cover containment): "
          f"{'PASS' if overall_pass else 'FAIL'}")
    print(f"{'=' * 76}")

    with open(HERE / "cover_joint_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'cover_joint_results.json'}")


if __name__ == "__main__":
    main()
