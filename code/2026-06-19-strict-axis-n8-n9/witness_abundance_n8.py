"""
Day 80 CODE Task 2 -- Witness abundance at n=8, (i, alpha) = (3, 1).

GOAL
====
For n=8 and fixed interior (i, alpha) = (3, 1), enumerate every AII
extreme ray and check whether each supports at least one F-feasible
single-ray witness piece for T = e_{B_3} + 1 * e_S.

"Witness piece" P:
  - Pick AII ray R = sum of k columns (k=1, 2, or 3 at even n).
  - Choose decomposition T = val_1 + ... + val_k (nonneg int vecs).
  - Set P[col_j] = val_j for the k columns of R; all other cols = 0.
  - F-feasible iff every AII ray r' satisfies M @ r' is BDI.

We extend Day-79's task3 result (every ray supports a witness for
n=6,7 across all interior (i, alpha)) to n=8.

If 23/23 rays at n=8 support a witness for (i, alpha) = (3, 1), the
abundance pattern propagates beyond n=6,7 -> material support for
Day-80 PROVE.

If any ray FAILS to support a witness, that's a SHARP DATA POINT
worth flagging.

EXTRA: also report per-ray decomposition count (witness multiplicity).
"""
from __future__ import annotations
import json
import csv
import sys
from pathlib import Path

# Day-79 bdi_universal
sys.path.insert(0, '/home/agent/projects/code/2026-06-19-droppability-n7-boundary')
from bdi_universal import (  # noqa: E402
    target_point, aii_rays, zero_piece, check_F, coord_dict, is_BDI,
)

OUT_DIR = Path("/home/agent/projects/code/2026-06-19-strict-axis-n8-n9")
OUT_DIR.mkdir(exist_ok=True)


def compositions(n: int, k: int):
    if k == 0:
        return [tuple()] if n == 0 else []
    out = []
    for first in range(n + 1):
        for rest in compositions(n - first, k - 1):
            out.append((first,) + rest)
    return out


def all_decompositions(T: tuple, k: int):
    """All k-tuples of nonneg int vecs summing to T (coord-wise)."""
    dim = len(T)
    if k == 0:
        return [tuple()] if all(x == 0 for x in T) else []
    parts = []
    for c in range(dim):
        parts.append(compositions(T[c], k))
    results = []

    def recurse(c, partial):
        if c == dim:
            kv = tuple(
                tuple(partial[c_][j] for c_ in range(dim))
                for j in range(k)
            )
            results.append(kv)
            return
        for comp in parts[c]:
            partial.append(comp)
            recurse(c + 1, partial)
            partial.pop()

    recurse(0, [])
    return results


def enumerate_witnesses(n, i, alpha):
    T = target_point(n, i, alpha)
    rays = aii_rays(n)
    by_ray = {}
    for ridx, ray in enumerate(rays):
        cols = list(ray.keys())
        k = len(cols)
        decomps = all_decompositions(T, k)
        feas = []
        for d in decomps:
            piece = zero_piece(n)
            for col, val in zip(cols, d):
                piece[col] = val
            if not check_F(n, piece):
                continue
            feas.append({
                "cols": cols,
                "vals_raw": [list(v) for v in d],
                "vals_human": [coord_dict(n, v) for v in d],
            })
        by_ray[ridx] = {
            "ray": dict(ray),
            "k": k,
            "n_decompositions_total": len(decomps),
            "n_feasible_witnesses": len(feas),
            "examples": feas[:3],
        }
    return T, rays, by_ray


def main():
    n, i, alpha = 8, 3, 1
    print(f"=== Witness abundance at n={n}, i={i}, alpha={alpha} ===\n")

    T, rays, by_ray = enumerate_witnesses(n, i, alpha)
    print(f"T = e_B_{i} + {alpha} * e_S = {coord_dict(n, T)}")
    print(f"#AII rays at n={n}: {len(rays)} (expected 3n-1 = {3*n-1})")
    assert len(rays) == 3 * n - 1, f"Expected 3n-1={3*n-1}, got {len(rays)}"

    # Per-ray summary
    print(f"\nPer-ray witness counts:")
    n_rays_with_witness = 0
    failures = []
    for ridx in sorted(by_ray.keys()):
        info = by_ray[ridx]
        nfeas = info["n_feasible_witnesses"]
        if nfeas > 0:
            n_rays_with_witness += 1
        else:
            failures.append(ridx)
        print(f"  Ray {ridx:>2} ({info['ray']}): "
              f"{nfeas:>3} feasible witnesses / "
              f"{info['n_decompositions_total']} decompositions")

    print(f"\n{'='*70}")
    print(f"# rays supporting >=1 witness: {n_rays_with_witness} / {len(rays)}")
    if failures:
        print(f"FAILING RAYS (no witness): {failures}")
        print(f"  -> sharp data point: not every ray supports a witness at n=8")
    else:
        print(f"ALL {len(rays)} rays support a witness "
              f"-> abundance pattern extends from n=6,7 to n=8")
    print(f"{'='*70}")

    # --- CSV ---
    csv_path = OUT_DIR / "witness_abundance_n8_i3_a1.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "ray_idx", "ray", "k_cols",
            "n_decompositions_total", "n_feasible_witnesses",
            "supports_witness",
        ])
        for ridx in sorted(by_ray.keys()):
            info = by_ray[ridx]
            w.writerow([
                ridx,
                "+".join(f"{c}*{v}" if v != 1 else c
                         for c, v in info["ray"].items()),
                info["k"],
                info["n_decompositions_total"],
                info["n_feasible_witnesses"],
                int(info["n_feasible_witnesses"] > 0),
            ])
    print(f"\nWrote CSV: {csv_path}")

    # --- JSON ---
    json_path = OUT_DIR / "witness_abundance_n8_i3_a1.json"
    out = {
        "n": n, "i": i, "alpha": alpha,
        "T_coords": coord_dict(n, T),
        "n_aii_rays": len(rays),
        "n_rays_with_witness": n_rays_with_witness,
        "failing_rays": failures,
        "abundance_holds": len(failures) == 0,
        "by_ray": {
            str(ridx): {
                "ray": info["ray"],
                "k": info["k"],
                "n_decompositions_total": info["n_decompositions_total"],
                "n_feasible_witnesses": info["n_feasible_witnesses"],
                "examples": info["examples"],
            }
            for ridx, info in by_ray.items()
        },
    }
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"Wrote JSON: {json_path}")


if __name__ == "__main__":
    main()
