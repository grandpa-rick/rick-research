#!/usr/bin/env python3
"""
Task 3 (clean version): enumerate single-ray witness pieces with T in image.

A "witness piece" P is constructed by:
  1. Pick an AII ray R (one of 3n or 3n-1 rays).
  2. R involves k columns (1, 2, or 3).
  3. Choose a decomposition T = val_1 + ... + val_k (nonneg int vecs).
  4. Set P[col_j] = val_j for the k columns of R; all other columns = 0.
  5. Check F-feasibility of P.

Classify by:
  - the primary ray R giving T
  - the decomposition pattern (val_1, ..., val_k)

For each (n, i, alpha), report:
  - which rays support a witness, and how many decompositions each
  - propose a canonical witness
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from bdi_universal import (
    bdi_coords, vec, add, scale, zero_vec, zero_piece, piece_columns,
    target_point, coord_dict, is_BDI,
    aii_rays, ray_image, gen_set, check_F,
)


def all_decompositions(T: tuple, k: int) -> list[tuple]:
    """All k-tuples of nonneg int vecs summing to T (with possibly zero entries)."""
    dim = len(T)
    # Enumerate by recursion: for each coordinate independently distribute.
    # T[c] is split among k vectors -> compositions of T[c] into k nonneg parts.
    # Cross-product over coords.
    if k == 0:
        return [tuple()]
    parts = []
    for c in range(dim):
        # compositions of T[c] into k parts
        comps = compositions(T[c], k)
        parts.append(comps)
    # Cartesian product over coords
    # Each result is a k-tuple of vectors, each of length dim.
    results = []

    def recurse(c, partial):
        # partial is list of length c, each a length-k tuple (val_1[c'],...,val_k[c']) for c'=0..c-1
        if c == dim:
            # Construct k vectors
            kv = []
            for j in range(k):
                v = tuple(partial[c_][j] for c_ in range(dim))
                kv.append(v)
            results.append(tuple(kv))
            return
        for comp in parts[c]:
            partial.append(comp)
            recurse(c + 1, partial)
            partial.pop()

    recurse(0, [])
    return results


def compositions(n: int, k: int) -> list[tuple]:
    """All k-tuples of nonneg ints summing to n."""
    if k == 0:
        return [tuple()] if n == 0 else []
    out = []
    for first in range(n + 1):
        for rest in compositions(n - first, k - 1):
            out.append((first,) + rest)
    return out


def enumerate_single_ray_witnesses(n: int, i: int, alpha: int) -> list[dict]:
    """For each AII ray, enumerate witness pieces giving T via that ray."""
    T = target_point(n, i, alpha)
    rays = aii_rays(n)
    witnesses = []

    for ray_idx, ray in enumerate(rays):
        cols = list(ray.keys())  # 1, 2, or 3 columns
        k = len(cols)
        # All decompositions of T into k parts.
        decomps = all_decompositions(T, k)
        for d in decomps:
            piece = zero_piece(n)
            for col, val in zip(cols, d):
                piece[col] = val
            if not check_F(n, piece):
                continue
            # Classify
            kind = "pure" if k == 1 else ("pair" if k == 2 else "triple")
            n_nonzero = sum(1 for v in d if any(x > 0 for x in v))
            witnesses.append({
                "ray_idx": ray_idx,
                "ray": dict(ray),
                "kind": kind,
                "cols": cols,
                "vals": [coord_dict(n, v) for v in d],
                "vals_raw": [list(v) for v in d],
                "n_nonzero_cols_used": n_nonzero,
            })
    return witnesses


def witness_signature(w: dict) -> str:
    """Canonical signature for grouping."""
    parts = []
    for col, v in zip(w["cols"], w["vals_raw"]):
        if any(x > 0 for x in v):
            cd = w["vals"][w["cols"].index(col)]
            parts.append(f"{col}={cd}")
    return " + ".join(sorted(parts)) if parts else "0"


def main():
    out = {"by_case": []}
    cases = []
    # n=6 interior i=2,3,4
    for i in (2, 3, 4):
        for alpha in (1, 2):
            cases.append((6, i, alpha))
    # n=7 interior i=2,3,4,5
    for i in (2, 3, 4, 5):
        for alpha in (1, 2):
            cases.append((7, i, alpha))

    print(f"# Task 3: Single-ray witness enumeration", flush=True)
    print(f"# (witness = piece with T as image of one AII ray)", flush=True)
    print()

    for (n, i, alpha) in cases:
        T = target_point(n, i, alpha)
        print(f"\n=== n={n}, i={i}, alpha={alpha}: T = {coord_dict(n, T)} ===",
              flush=True)
        ws = enumerate_single_ray_witnesses(n, i, alpha)
        # Group by ray
        by_ray = {}
        for w in ws:
            ridx = w["ray_idx"]
            by_ray.setdefault(ridx, []).append(w)

        rays = aii_rays(n)
        rays_with_witnesses = sorted(by_ray.keys())
        print(f"  # rays supporting a witness: {len(rays_with_witnesses)}/"
              f"{len(rays)}", flush=True)
        print(f"  # total witnesses (across decompositions): {len(ws)}",
              flush=True)

        ray_summary = []
        for ridx in rays_with_witnesses:
            r = rays[ridx]
            r_witnesses = by_ray[ridx]
            print(f"  Ray {ridx} ({r}): {len(r_witnesses)} witnesses",
                  flush=True)
            ray_summary.append({
                "ray_idx": ridx,
                "ray": dict(r),
                "n_witnesses": len(r_witnesses),
                "examples": r_witnesses[:5],
            })

        out["by_case"].append({
            "n": n, "i": i, "alpha": alpha,
            "T_coords": coord_dict(n, T),
            "n_rays_with_witnesses": len(rays_with_witnesses),
            "n_total_witnesses": len(ws),
            "ray_summary": ray_summary,
        })

    out_path = HERE / "task3_witness_families" / "results_clean.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {out_path}", flush=True)


if __name__ == "__main__":
    main()
