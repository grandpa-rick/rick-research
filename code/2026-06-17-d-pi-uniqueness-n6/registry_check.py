#!/usr/bin/env python3
"""
Day 76 CODE Task A SUPPLEMENT -- D-pi uniqueness on the n=6 minimal cover.

Tests D-pi uniqueness (weak form) on the 53-piece augmented registry at n=6:
  For each registry piece pi, for each interior i in {2, 3, 4}:
    if pi^{p_i} has form e_{B_i} + alpha * e_S for some alpha in {0, 1, 2},
    check that Im(pi) is image-contained in Im(pi_alpha^{(i)}) where
    pi_alpha^{(i)} is the simple-divert piece.

This is a focused check on the COVER (53 pieces). The broader F-feasibility
enumeration (d_pi_uniqueness_n6.py) tests a wider class but may include
pieces outside the cover where containment fails by design.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from d_pi_uniqueness_n6 import (
    load_registry_n6, simpdiv_piece, gen_set_n6_r, check_F_n6_r,
    add_r, vec_r, scale_r, BDI_COORDS_REG, NB_REG, ZERO_REG,
    enumerate_image_set, semigroup_membership, image_equivalent,
)

HERE = Path(__file__).resolve().parent


def main():
    print("=" * 76)
    print("Day 76 CODE Task A SUPPLEMENT -- D-pi uniqueness on n=6 minimal cover")
    print("=" * 76)

    pieces = load_registry_n6()
    print(f"\nLoaded n=6 registry: {len(pieces)} pieces (in linkLHS=0 gauge).")

    # Verify all pieces are F-feasible.
    n_feas = sum(1 for p in pieces.values() if check_F_n6_r(p))
    print(f"F-feasible: {n_feas}/{len(pieces)}")
    if n_feas != len(pieces):
        print("WARNING: some registry pieces NOT F-feasible "
              "(under run.py's ray set)")
        for name, p in pieces.items():
            if not check_F_n6_r(p):
                print(f"  infeasible: {name}")

    base = pieces["P6_base"]

    interior = [2, 3, 4]
    results = {"interior": interior, "by_i": {}}

    # Precompute simpdiv images.
    simpdiv = {}
    simpdiv_imgs = {}
    for i in interior:
        for alpha in range(3):
            simpdiv[(i, alpha)] = simpdiv_piece(base, i, alpha)

    # Pairwise distinctness of simpdiv images per interior.
    print(f"\n{'-'*60}")
    print("Pairwise image-equivalence of simpdiv pieces (per interior):")
    print(f"{'-'*60}")
    for i in interior:
        eq01 = image_equivalent(simpdiv[(i, 0)], simpdiv[(i, 1)], max_coef=4)
        eq12 = image_equivalent(simpdiv[(i, 1)], simpdiv[(i, 2)], max_coef=4)
        eq02 = image_equivalent(simpdiv[(i, 0)], simpdiv[(i, 2)], max_coef=4)
        print(f"  i={i}: Im(pi_0) ≃ Im(pi_1): {eq01}, "
              f"Im(pi_1) ≃ Im(pi_2): {eq12}, Im(pi_0) ≃ Im(pi_2): {eq02}")
        n_distinct = 3 if not (eq01 or eq12 or eq02) else (
            1 if (eq01 and eq12 and eq02) else 2)
        print(f"    -> {n_distinct} distinct image classes")

    # Precompute simpdiv image sets up to max sum.
    print(f"\nPrecomputing simpdiv image sets up to sum 8 ...")
    for i in interior:
        for alpha in range(3):
            gens = list(set(gen_set_n6_r(simpdiv[(i, alpha)])))
            simpdiv_imgs[(i, alpha)] = enumerate_image_set(gens, max_total=8)
        sizes = [len(simpdiv_imgs[(i, a)]) for a in range(3)]
        print(f"  i={i}: |Im(simpdiv_α)| (sum≤8) = {sizes}")

    # For each registry piece, identify its p_i column for each interior.
    # If p_i column == e_{B_i} + alpha * e_S for some alpha in {0,1,2}, check
    # Im(piece) ⊆ Im(simpdiv_alpha^{(i)}).
    print(f"\n{'-'*60}")
    print("Per-piece D-pi uniqueness check (cover-restricted):")
    print(f"{'-'*60}")

    expected_p_i = {(i, alpha): add_r(vec_r(**{f"B{i}": 1}),
                                       scale_r(alpha, vec_r(S=1)))
                    for i in interior for alpha in range(3)}

    per_piece_results = {}
    fails_per_i = {i: 0 for i in interior}
    fails_per_i_pieces = {i: [] for i in interior}
    passes_per_i = {i: 0 for i in interior}
    not_applicable_per_i = {i: 0 for i in interior}

    for name, piece in pieces.items():
        per_piece_results[name] = {}
        for i in interior:
            p_col = piece[f"p{i}"]
            alpha = None
            for a in range(3):
                if p_col == expected_p_i[(i, a)]:
                    alpha = a
                    break
            if alpha is None:
                # This piece's p_i column is OUTSIDE the {b_0, b_1, b_2}
                # family. Not applicable for D-pi check at interior i.
                per_piece_results[name][i] = {"alpha": None, "status": "N/A"}
                not_applicable_per_i[i] += 1
                continue

            # Check Im(piece) ⊆ Im(simpdiv_alpha^{(i)}) by set-membership
            # on each piece generator.
            piece_gens = list(set(gen_set_n6_r(piece)))
            target_set = simpdiv_imgs[(i, alpha)]
            target_gens = list(set(gen_set_n6_r(simpdiv[(i, alpha)])))
            ok = True
            failing_gen = None
            for g in piece_gens:
                if sum(g) <= 8:
                    if g not in target_set:
                        ok = False
                        failing_gen = g
                        break
                else:
                    if not semigroup_membership(g, target_gens, max_coef=6):
                        ok = False
                        failing_gen = g
                        break
            status = "PASS" if ok else "FAIL"
            per_piece_results[name][i] = {
                "alpha": alpha,
                "status": status,
                "failing_generator": (
                    {k: v for k, v in zip(BDI_COORDS_REG, failing_gen) if v}
                    if failing_gen else None
                ),
            }
            if ok:
                passes_per_i[i] += 1
            else:
                fails_per_i[i] += 1
                fails_per_i_pieces[i].append((name, alpha, failing_gen))

    # Summary
    print()
    for i in interior:
        n_pieces_with_p_i_routing = passes_per_i[i] + fails_per_i[i]
        print(f"  Interior p_{i}: {n_pieces_with_p_i_routing} of {len(pieces)} "
              f"pieces have p_{i} ∈ {{b_0, b_1, b_2}}")
        print(f"    PASS (image-contained): {passes_per_i[i]}")
        print(f"    FAIL (image NOT contained): {fails_per_i[i]}")
        if fails_per_i_pieces[i]:
            print(f"    Failing pieces:")
            for name, alpha, fg in fails_per_i_pieces[i][:5]:
                nz = {k: v for k, v in zip(BDI_COORDS_REG, fg) if v}
                print(f"      {name} (alpha={alpha}): failing gen {nz}")
        results["by_i"][i] = {
            "n_applicable": n_pieces_with_p_i_routing,
            "n_pass": passes_per_i[i],
            "n_fail": fails_per_i[i],
            "n_not_applicable": not_applicable_per_i[i],
            "failing_pieces": [
                (n, a, {k: v for k, v in zip(BDI_COORDS_REG, fg) if v})
                for n, a, fg in fails_per_i_pieces[i]
            ],
        }

    overall = all(fails_per_i[i] == 0 for i in interior)
    print()
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")
    results["overall_pass"] = overall

    with open(HERE / "registry_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'registry_results.json'}")


if __name__ == "__main__":
    main()
