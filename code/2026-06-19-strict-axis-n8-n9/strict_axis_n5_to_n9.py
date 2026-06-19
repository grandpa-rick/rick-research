"""
Day 80 CODE Task 1 -- Strict #AXIS at n=5..9 using Day-79 bdi_universal rays.

GOAL
====
Re-verify the 2(n-1) closed form for strict #AXIS at n=5,6,7,8,9 using
the CORRECT AII extreme rays (Day-79 `bdi_universal.py`), NOT the
"spurious" registry.py aii_rays. We've checked at start that
bdi_universal.aii_rays(n) == run.py.aii_rays(n) for n=5..9, so the
Day-72/Day-73 augmented-registry pipeline was already using the right
rays. This run is a clean reverification with explicit ray-comparison
in the audit.

PIPELINE
========
1. Build the augmented registry at each n (Day-70 minimal cover ∪
   Day-71 simple-divert ∪ Day-72 l_j-divert ∪ Day-72 Class-1 aux).
2. Filter for ray-based BDI feasibility using bdi_universal rays.
3. Dedup by piece matrix.
4. Strict #AXIS: for each AII coord c, group pieces by their non-c
   columns; coord is strict AXIS iff some group has >= 3 distinct
   c-columns (a 3-clique on the wall {c=0}).
5. Output CSV `strict_axis_n5_to_n9.csv` + JSON `results.json`.

EXPECTED
========
| n | # pieces | strict #AXIS | predicted 2(n-1) | match |
| 5 |    42    |      8       |        8         |  YES  |
| 6 |    53    |     10       |       10         |  YES  |
| 7 |    66    |     12       |       12         |  YES  |
| 8 |    77    |     14       |       14         |  YES  |
| 9 |    90    |     16       |       16         |  YES  |
"""

from __future__ import annotations

import sys
import json
import time
import csv
from pathlib import Path
from collections import defaultdict

import numpy as np

# Day-79 bdi_universal — correct rays
sys.path.insert(0, '/home/agent/projects/code/2026-06-19-droppability-n7-boundary')
import bdi_universal as bu  # noqa: E402

# Augmented-registry builder + strict-AXIS infrastructure
sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
sys.path.insert(0, '/home/agent/projects/code/2026-06-17-complete-registry')

from general_axis import (  # noqa: E402
    aii_struct, bdi_vars, bdi_feasible, piece_matrix,
)
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location(
    "day72_registry_run",
    "/home/agent/projects/code/2026-06-17-complete-registry/run.py")
_day72 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day72)
build_augmented_registry = _day72.build_augmented_registry
dedup_by_matrix = _day72.dedup_by_matrix

OUT_DIR = Path("/home/agent/projects/code/2026-06-19-strict-axis-n8-n9")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------
# Ray-feasibility using bdi_universal (Day-79)
# ---------------------------------------------------------------------
def piece_dict_from_matrix(M, n):
    """Convert M (n_bdi x n_aii_vars) into bdi_universal piece dict
    {col_name: tuple(BDI vec)} so we can call bu.check_F."""
    s = aii_struct(n)
    aii_v = s["vars"]
    piece = {}
    for c, name in enumerate(aii_v):
        piece[name] = tuple(int(M[r, c]) for r in range(M.shape[0]))
    return piece


def verify_piece_via_universal(M, n):
    """Use bdi_universal.check_F under-the-hood. Returns list of
    (ray_index, ray_dict, image_tuple) failures."""
    piece = piece_dict_from_matrix(M, n)
    rays = bu.aii_rays(n)
    failures = []
    for j, r in enumerate(rays):
        img = bu.ray_image(piece, r)
        if not bu.is_BDI(n, img):
            failures.append((j, r, img))
    return failures


def filter_feasible_bu(registry, n, verbose=False):
    feasible = {}
    infeasible = {}
    for name, M in registry.items():
        f = verify_piece_via_universal(M, n)
        if not f:
            feasible[name] = M
        else:
            infeasible[name] = (M, f)
    if verbose:
        print(f"  filter: {len(feasible)}/{len(registry)} feasible")
    return feasible, infeasible


# ---------------------------------------------------------------------
# Strict AXIS analysis
# ---------------------------------------------------------------------
def column_of(M, c, n_bdi):
    return tuple(int(M[r, c]) for r in range(n_bdi))


def strict_axis_for_var(pieces_dict, c_idx, n_bdi):
    groups = defaultdict(set)
    n_aii = next(iter(pieces_dict.values())).shape[1]
    for name, M in pieces_dict.items():
        key = tuple(column_of(M, c, n_bdi) for c in range(n_aii) if c != c_idx)
        groups[key].add(column_of(M, c_idx, n_bdi))
    max_size = max((len(s) for s in groups.values()), default=0)
    return {"max_group_size": max_size, "is_axis": max_size >= 3}


def predicted_axis_vars(n):
    """Closed form: {p_1, ..., p_{n-2}, p_n, l_1, ..., l_{n-1}}."""
    out = [f"prefix[{i}]" for i in range(1, n - 1)]
    out.append(f"prefix[{n}]")
    out += [f"long[{j}]" for j in range(1, n)]
    return out


# ---------------------------------------------------------------------
# Per-n driver
# ---------------------------------------------------------------------
def run_for_n(n):
    print(f"\n{'='*70}")
    print(f"n = {n} ({'odd' if n % 2 == 1 else 'even'})")
    print(f"{'='*70}")
    s = aii_struct(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    rays_bu = bu.aii_rays(n)
    expected_rays = 3 * n if n % 2 == 1 else 3 * n - 1
    print(f"  bdi_universal AII rays: {len(rays_bu)} (expected {expected_rays})")
    assert len(rays_bu) == expected_rays

    t0 = time.time()
    reg = build_augmented_registry(n)
    print(f"  Augmented registry: {len(reg)} pieces (raw)")

    feasible, infeasible = filter_feasible_bu(reg, n)
    print(f"  After bdi_universal-ray feasibility filter: {len(feasible)}")
    if infeasible:
        print(f"  Infeasible (showing up to 3):")
        for nm, (_, fails) in list(infeasible.items())[:3]:
            j, r, img = fails[0]
            print(f"    {nm}: ray {j} = {r} -> img {img}")

    deduped = dedup_by_matrix(feasible)
    print(f"  After dedup: {len(deduped)} distinct pieces")
    print(f"  Registry build+filter time: {time.time()-t0:.2f}s")

    t1 = time.time()
    per_var = {}
    axis_vars = []
    for c_idx, av in enumerate(aii_v):
        r = strict_axis_for_var(deduped, c_idx, n_bdi)
        per_var[av] = r
        if r["is_axis"]:
            axis_vars.append(av)
    print(f"  Strict #AXIS time: {time.time()-t1:.2f}s")

    n_axis = len(axis_vars)
    pred_count = 2 * (n - 1)
    pred_vars = predicted_axis_vars(n)

    print(f"  STRICT #AXIS = {n_axis}; predicted 2(n-1) = {pred_count}; "
          f"match = {'YES' if n_axis == pred_count else 'NO'}")
    matched = set(axis_vars) == set(pred_vars)
    print(f"  AXIS-var-set match: {'YES' if matched else 'NO'}")

    return {
        "n": n,
        "n_aii_vars": len(aii_v),
        "n_bdi_vars": n_bdi,
        "n_rays": len(rays_bu),
        "n_pieces_raw": len(reg),
        "n_pieces_feasible": len(feasible),
        "n_pieces_deduped": len(deduped),
        "strict_n_axis": n_axis,
        "axis_vars": sorted(axis_vars),
        "predicted_axis_vars": sorted(pred_vars),
        "predicted_count_2nm1": pred_count,
        "count_match": n_axis == pred_count,
        "var_set_match": matched,
        "missing_predicted": sorted(set(pred_vars) - set(axis_vars)),
        "extra_unpredicted": sorted(set(axis_vars) - set(pred_vars)),
        "per_var": {av: per_var[av] for av in aii_v},
    }


def main():
    results = {}
    for n in (5, 6, 7, 8, 9):
        results[n] = run_for_n(n)

    # --- CSV ---
    csv_path = OUT_DIR / "strict_axis_n5_to_n9.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "n", "n_pieces_deduped", "n_aii_rays", "strict_n_axis",
            "predicted_2nm1", "count_match", "var_set_match",
        ])
        for n in sorted(results.keys()):
            r = results[n]
            w.writerow([
                r["n"], r["n_pieces_deduped"], r["n_rays"],
                r["strict_n_axis"], r["predicted_count_2nm1"],
                int(r["count_match"]), int(r["var_set_match"]),
            ])
    print(f"\nWrote CSV: {csv_path}")

    # --- JSON ---
    json_path = OUT_DIR / "results.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Wrote JSON: {json_path}")

    # --- summary ---
    print(f"\n{'='*70}")
    print(f"SUMMARY (Day-79 bdi_universal rays)")
    print(f"{'='*70}")
    print(f"{'n':>3} {'pieces':>7} {'rays':>5} {'#AXIS':>6} "
          f"{'pred=2(n-1)':>12} {'cnt OK':>7} {'vars OK':>8}")
    for n in sorted(results.keys()):
        r = results[n]
        cm = "YES" if r["count_match"] else "NO"
        vm = "YES" if r["var_set_match"] else "NO"
        print(f"{n:>3} {r['n_pieces_deduped']:>7} {r['n_rays']:>5} "
              f"{r['strict_n_axis']:>6} {r['predicted_count_2nm1']:>12} "
              f"{cm:>7} {vm:>8}")

    all_match = all(r["count_match"] and r["var_set_match"]
                    for r in results.values())
    print(f"\nHEADLINE: 2(n-1) at n=5..9 (bdi_universal rays): "
          f"{'CONFIRMED' if all_match else 'BROKEN'}")


if __name__ == "__main__":
    main()
