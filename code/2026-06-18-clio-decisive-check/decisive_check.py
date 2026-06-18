#!/usr/bin/env python3
"""
Clio's decisive check (her review §9 Q1, addressed in CODE.md Day 78):

For each interior i in {2, ..., n-2} at n in {5, 6, 7} and each
alpha in {1, 2}, is the lattice point
                  T = e_{B_i} + alpha * e_S
coverable by some F-feasible piece pi such that pi^{p_i} != T?

=================================================================
SUPPORT-REDUCTION LEMMA  (the heart of the analysis)
=================================================================
Let T = e_{B_i} + alpha * e_S. Suppose T = sum_k a_k * r_k where
each r_k is a BDI vector (a ray-image of some piece) and a_k in N.

For each k with a_k > 0, every coordinate c with r_k[c] > 0 must
also have T[c] > 0 (otherwise the sum overshoots on coord c).
Hence supp(r_k) subseteq {B_i, S}. Write r_k = c_1 * e_{B_i} + c_2 * e_S.

BDI of r_k requires:
  - all entries >= 0 (auto: c_1, c_2 >= 0)
  - T_a <= B_a for each a (auto: T_a = 0)
  - P_a = 2 sum_{b<=a}(B_b - T_b) >= 0 (auto for a < i: 0;
                                       for a >= i: 2 c_1 >= 0)
  - M_a constraint (auto: M_a = 0)
  - S = c_2 <= P_{n-1}(r_k) = 2 c_1.

So c_2 <= 2 c_1. Also r_k <= T coordwise means c_1 <= 1, c_2 <= alpha.

Case c_1 = 0: forces c_2 = 0, r_k = 0 (does not contribute).
Case c_1 = 1: c_2 in {0, 1, 2}, all BDI.

So nonzero contributing rays r_k lie in
    {e_{B_i}, e_{B_i} + e_S, e_{B_i} + 2 e_S}.

Let n_beta = # rays equal to e_{B_i} + beta * e_S (multiplicity).
Then n_0 + n_1 + n_2 = 1  (B_i-sum) and n_1 + 2 n_2 = alpha (S-sum).

  alpha = 1:  n_1 = 1, n_0 = n_2 = 0.
  alpha = 2:  n_2 = 1, n_0 = n_1 = 0.

CONCLUSION: T in Im(pi) iff some ray of pi equals T (with mult 1).

So the decisive question reduces to:

  Does an F-feasible piece pi exist with pi^{p_i} != T but some
  OTHER ray of pi equals T?

The piece has 3n - 1 rays. Excluding the p_i column itself, we have
3n - 2 alternative ray slots. We enumerate each by constructing a
minimal piece witness (only the relevant columns nonzero) and
checking F-feasibility.
=================================================================
"""
from __future__ import annotations
import json
import time
from pathlib import Path

from bdi_n import (
    bdi_coords, bdi_idx, zero_piece, zero_vec, vec, add, scale,
    is_BDI, check_F, gen_set, p_cols, l_cols, s_cols, all_cols,
    target_point, semigroup_membership, piece_to_human,
)

HERE = Path(__file__).resolve().parent

# ===================================================================
# Route enumeration
# ===================================================================
RAY_SLOTS = {
    "p_j":            "p_j = T (some prefix column equals T)",
    "l_1":            "l_1 = T (the pure long[1] ray equals T)",
    "s_1":            "s_1 = T (the pure short[1] ray equals T)",
    "p_{j-1}+l_j":    "p_{j-1} + l_j = T (lifted-long ray)",
    "p_{j-1}+s_j":    "p_{j-1} + s_j = T (lifted-short ray)",
}


def witness_p_j(n: int, j: int, T: tuple) -> dict:
    """Minimal witness: p_j = T, every other column = 0."""
    piece = zero_piece(n)
    piece[f"p{j}"] = T
    return piece


def witness_l1(n: int, T: tuple) -> dict:
    """Minimal witness: l_1 = T, every other column = 0."""
    piece = zero_piece(n)
    piece["l1"] = T
    return piece


def witness_s1(n: int, T: tuple) -> dict:
    """Minimal witness: s_1 = T, every other column = 0."""
    piece = zero_piece(n)
    piece["s1"] = T
    return piece


def witness_pj1_lj(n: int, j: int, T: tuple, decomp: str = "split_BS") -> dict:
    """Minimal witness: p_{j-1} + l_j = T, every other column = 0.

    Several decompositions of T = e_{B_i} + alpha e_S are possible:
      - "all_in_l":   p_{j-1} = 0,    l_j = T
      - "split_BS":   p_{j-1} = e_{B_i}, l_j = alpha * e_S
      - "all_in_p":   p_{j-1} = T,    l_j = 0
    """
    piece = zero_piece(n)
    if j < 2 or j > n:
        raise ValueError(f"j must be in [2, n], got {j}")
    if decomp == "all_in_l":
        piece[f"l{j}"] = T
    elif decomp == "all_in_p":
        piece[f"p{j-1}"] = T
    elif decomp == "split_BS":
        # Read off B_i and S coordinates from T.
        i = _i_from_target(n, T)
        alpha = T[bdi_idx(n)["S"]]
        piece[f"p{j-1}"] = vec(n, **{f"B{i}": 1})
        piece[f"l{j}"] = scale(alpha, vec(n, S=1))
    else:
        raise ValueError(f"unknown decomp {decomp}")
    return piece


def witness_pj1_sj(n: int, j: int, T: tuple, decomp: str = "split_BS") -> dict:
    """Minimal witness: p_{j-1} + s_j = T, every other column = 0.

    Same decompositions as witness_pj1_lj.
    """
    piece = zero_piece(n)
    if j < 2 or j > n - 1:
        raise ValueError(f"j must be in [2, n-1], got {j}")
    if decomp == "all_in_l":
        piece[f"s{j}"] = T
    elif decomp == "all_in_p":
        piece[f"p{j-1}"] = T
    elif decomp == "split_BS":
        i = _i_from_target(n, T)
        alpha = T[bdi_idx(n)["S"]]
        piece[f"p{j-1}"] = vec(n, **{f"B{i}": 1})
        piece[f"s{j}"] = scale(alpha, vec(n, S=1))
    else:
        raise ValueError(f"unknown decomp {decomp}")
    return piece


def _i_from_target(n: int, T: tuple) -> int:
    """Extract i from T = e_{B_i} + alpha e_S."""
    idx = bdi_idx(n)
    for a in range(1, n):
        if T[idx[f"B{a}"]] == 1:
            return a
    raise ValueError(f"T={T} has no B-coordinate set")


# ===================================================================
# Enumerate all routes for given (n, i, alpha)
# ===================================================================
def enumerate_alternative_routes(n: int, i: int, alpha: int) -> dict:
    """For each alternative ray slot (excluding p_i), test if some
    F-feasible witness piece can have that slot equal to T."""
    T = target_point(n, i, alpha)
    assert is_BDI(n, T), f"target T={T} must be BDI"

    routes = []

    # (A) p_j = T for j != i, j in [1, n]
    for j in range(1, n + 1):
        if j == i:
            continue
        piece = witness_p_j(n, j, T)
        feasible = check_F(n, piece)
        # Verify the constructed ray's value equals T:
        ray_value = piece[f"p{j}"]
        # Verify p_i != T:
        p_i_value = piece[f"p{i}"]
        routes.append({
            "slot_type": "p_j",
            "j": j,
            "decomp": "single_column",
            "feasible": feasible,
            "ray_equals_T": ray_value == T,
            "p_i_neq_T": p_i_value != T,
            "witness": piece_to_human(n, piece),
        })

    # (B) l_1 = T
    piece = witness_l1(n, T)
    feasible = check_F(n, piece)
    routes.append({
        "slot_type": "l_1",
        "j": 1,
        "decomp": "single_column",
        "feasible": feasible,
        "ray_equals_T": piece["l1"] == T,
        "p_i_neq_T": piece[f"p{i}"] != T,
        "witness": piece_to_human(n, piece),
    })

    # (C) s_1 = T
    piece = witness_s1(n, T)
    feasible = check_F(n, piece)
    routes.append({
        "slot_type": "s_1",
        "j": 1,
        "decomp": "single_column",
        "feasible": feasible,
        "ray_equals_T": piece["s1"] == T,
        "p_i_neq_T": piece[f"p{i}"] != T,
        "witness": piece_to_human(n, piece),
    })

    # (D) p_{j-1} + l_j = T for j = 2..n
    for j in range(2, n + 1):
        for decomp in ("all_in_l", "split_BS", "all_in_p"):
            piece = witness_pj1_lj(n, j, T, decomp=decomp)
            feasible = check_F(n, piece)
            # Compute the ray value:
            ray_value = add(piece[f"p{j-1}"], piece[f"l{j}"])
            # p_i value (might be set if j-1 == i and decomp == "all_in_p"):
            p_i_value = piece[f"p{i}"]
            routes.append({
                "slot_type": "p_{j-1}+l_j",
                "j": j,
                "decomp": decomp,
                "feasible": feasible,
                "ray_equals_T": ray_value == T,
                "p_i_neq_T": p_i_value != T,
                "witness": piece_to_human(n, piece),
            })

    # (E) p_{j-1} + s_j = T for j = 2..n-1
    for j in range(2, n):
        for decomp in ("all_in_l", "split_BS", "all_in_p"):
            piece = witness_pj1_sj(n, j, T, decomp=decomp)
            feasible = check_F(n, piece)
            ray_value = add(piece[f"p{j-1}"], piece[f"s{j}"])
            p_i_value = piece[f"p{i}"]
            routes.append({
                "slot_type": "p_{j-1}+s_j",
                "j": j,
                "decomp": decomp,
                "feasible": feasible,
                "ray_equals_T": ray_value == T,
                "p_i_neq_T": p_i_value != T,
                "witness": piece_to_human(n, piece),
            })

    # Filter to genuinely successful routes:
    successes = [
        r for r in routes
        if r["feasible"] and r["ray_equals_T"] and r["p_i_neq_T"]
    ]

    return {
        "n": n,
        "i": i,
        "alpha": alpha,
        "target_T": {c: T[k] for k, c in enumerate(bdi_coords(n)) if T[k]},
        "answer_YES": len(successes) > 0,
        "n_routes_tried": len(routes),
        "n_successes": len(successes),
        "successes": successes,
        "all_routes": routes,
    }


# ===================================================================
# Verify (computationally) that NO multi-ray decomposition works:
# we already proved this; this is just a defensive check via direct
# semigroup membership in a SPECIFIC bad-case piece (where p_i = 0,
# and every ray of the piece happens to be 0 or e_{B_j} for j != i).
# ===================================================================
def verify_support_lemma_corollary(n: int, i: int, alpha: int) -> dict:
    """Construct a piece with rays NOT containing T = e_{B_i} + alpha e_S,
    but with various e_{B_j} (j != i) rays that have S=0; verify that T is
    NOT in semigroup."""
    T = target_point(n, i, alpha)
    piece = zero_piece(n)
    # Populate prefix columns with e_{B_j} for j != i (base-like).
    for j in range(1, n):
        if j == i:
            continue
        piece[f"p{j}"] = vec(n, **{f"B{j}": 1})
    gens = gen_set(n, piece)
    # T should NOT be in semigroup (since rays have no S contribution
    # except possibly via zero rays).
    in_sg = semigroup_membership(n, T, gens, max_coef=alpha + 1)
    return {
        "n": n, "i": i, "alpha": alpha,
        "T_in_image_of_no_T_piece": in_sg,
        "expected_FALSE": not in_sg,
    }


# ===================================================================
# Main
# ===================================================================
def main():
    print("=" * 76)
    print("Clio's decisive check (CODE.md Day 78)")
    print("Question: T = e_{B_i} + alpha e_S in Im(pi) for some")
    print("          F-feasible pi with pi^{p_i} != T?")
    print("=" * 76)

    out = {
        "support_reduction_lemma": (
            "T = e_{B_i} + alpha e_S in Im(pi) iff some ray of pi equals T."
        ),
        "by_n": {},
        "support_corollary_checks": [],
    }

    for n in (5, 6, 7):
        print(f"\n{'#' * 60}")
        print(f"# n = {n}")
        print(f"{'#' * 60}")
        out["by_n"][n] = {"by_i_alpha": {}}
        interior = list(range(2, n - 1))  # i = 2..n-2
        print(f"Interior coords (i = 2..n-2): {interior}")
        for i in interior:
            for alpha in (1, 2):
                t0 = time.time()
                res = enumerate_alternative_routes(n, i, alpha)
                dt = time.time() - t0
                key = f"i={i}_alpha={alpha}"
                out["by_n"][n]["by_i_alpha"][key] = res
                ans = "YES" if res["answer_YES"] else "NO"
                print(f"  i={i}, alpha={alpha}: {ans}  "
                      f"({res['n_successes']}/{res['n_routes_tried']} "
                      f"routes succeed; {dt:.2f}s)")
                if res["answer_YES"]:
                    # Show the first 3 successful routes briefly.
                    for r in res["successes"][:3]:
                        print(f"      ROUTE: {r['slot_type']} "
                              f"(j={r['j']}, decomp={r['decomp']})  "
                              f"witness cols: {list(r['witness'].keys())}")

        # Defensive support-lemma corollary check.
        for i in interior:
            for alpha in (1, 2):
                chk = verify_support_lemma_corollary(n, i, alpha)
                out["support_corollary_checks"].append(chk)

    # Summary.
    print(f"\n{'=' * 76}")
    print("SUMMARY")
    print(f"{'=' * 76}")
    all_yes = True
    for n in (5, 6, 7):
        interior = list(range(2, n - 1))
        for i in interior:
            for alpha in (1, 2):
                key = f"i={i}_alpha={alpha}"
                ans = out["by_n"][n]["by_i_alpha"][key]["answer_YES"]
                marker = "YES" if ans else "NO"
                print(f"  n={n}, i={i}, alpha={alpha}: {marker}")
                if not ans:
                    all_yes = False
    out["overall_answer_YES_everywhere"] = all_yes
    print(f"\nOverall: T = e_{{B_i}} + alpha e_S is coverable by some "
          f"F-feasible pi with pi^{{p_i}} != T for ALL tested "
          f"(n, i, alpha): {'YES' if all_yes else 'NO'}")

    # Defensive lemma checks.
    print(f"\nSupport-lemma corollary checks "
          f"({len(out['support_corollary_checks'])} cases): "
          f"all expected_FALSE={all(c['expected_FALSE'] for c in out['support_corollary_checks'])}")

    # Save JSON.
    with open(HERE / "decisive_results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'decisive_results.json'}")


if __name__ == "__main__":
    main()
