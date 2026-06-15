"""
Day 73 CODE Task B -- Strict #AXIS at n = 8, 9.

GOAL:
  Extend Day-72 strict #AXIS verification (n=5,6,7) to n=8 (predicted 14
  = 2(8-1)) and n=9 (predicted 16 = 2(9-1)).

  Confirms the 2(n-1) extrapolation. Also checks the predicted AXIS-var
  set is {p_1, ..., p_{n-2}, p_n, l_1, ..., l_{n-1}}.

PIPELINE:
  1. Build augmented registry at n=8 and n=9, same composition as
     Day-72 (Day-70 minimal cover + simple-divert + l_j-divert + Class-1
     aux).
  2. Filter for BDI-feasibility via AII rays (Day-70 Cor 5.1).
  3. Dedup by matrix.
  4. Strict #AXIS analysis: for each AII coord c, group pieces by their
     non-c columns; a coord is AXIS iff some group has >= 3 distinct
     c-columns.
"""

from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from collections import defaultdict

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
sys.path.insert(0, '/home/agent/projects/code/2026-06-17-complete-registry')

from general_axis import aii_struct, bdi_vars, bdi_feasible, piece_matrix
# The augmented-registry helpers live in run.py in the Day-72 directory.
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "day72_registry_run",
    "/home/agent/projects/code/2026-06-17-complete-registry/run.py")
_day72 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day72)
build_augmented_registry = _day72.build_augmented_registry
filter_feasible = _day72.filter_feasible
dedup_by_matrix = _day72.dedup_by_matrix
aii_rays = _day72.aii_rays
registry_to_json = _day72.registry_to_json
piece_signature = _day72.piece_signature

OUT_DIR = Path("/home/agent/projects/code/2026-06-18-strict-axis-n8-n9")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------
# Strict AXIS analysis (lifted from Day-72 run.py)
# ---------------------------------------------------------------------
def column_of(M, c, n_bdi):
    return tuple(int(M[r, c]) for r in range(n_bdi))


def strict_axis_for_var(pieces_dict, c_idx, n_bdi):
    """For coord index c_idx: group pieces by "other columns" key; count
    distinct M[:, c_idx] within each group."""
    groups = defaultdict(set)
    groups_pieces = defaultdict(list)
    n_aii = next(iter(pieces_dict.values())).shape[1]
    for name, M in pieces_dict.items():
        key = tuple(column_of(M, c, n_bdi) for c in range(n_aii) if c != c_idx)
        col_c = column_of(M, c_idx, n_bdi)
        groups[key].add(col_c)
        groups_pieces[key].append((name, col_c))
    max_size = max((len(s) for s in groups.values()), default=0)
    example = None
    if max_size >= 3:
        for key, s in groups.items():
            if len(s) >= 3:
                example = groups_pieces[key]
                break
    return {
        "max_group_size": max_size,
        "is_axis": max_size >= 3,
        "example_group": example,
    }


def predicted_axis_vars(n):
    """Day-72 prediction: {p_1, ..., p_{n-2}, p_n, l_1, ..., l_{n-1}}.
    That's (n-2) + 1 + (n-1) = 2n - 2 = 2(n-1) vars."""
    vars_pred = []
    for i in range(1, n - 1):
        vars_pred.append(f"prefix[{i}]")
    vars_pred.append(f"prefix[{n}]")
    for j in range(1, n):
        vars_pred.append(f"long[{j}]")
    return vars_pred


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
    n_aii = s["n_vars"]
    rays = aii_rays(n)
    print(f"  # AII rays: {len(rays)} (expected "
          f"{3*n - (1 if n%2==0 else 0)})")
    print(f"  # AII vars: {n_aii}, # BDI vars: {n_bdi}")

    t0 = time.time()
    reg = build_augmented_registry(n)
    print(f"  Built augmented registry: {len(reg)} pieces (raw)")

    feasible, infeasible = filter_feasible(reg, n, verbose=False)
    print(f"  After feasibility filter: {len(feasible)} pieces")
    if infeasible:
        print(f"  Infeasible (showing first 3):")
        for nm, (_, fails) in list(infeasible.items())[:3]:
            j, r, img = fails[0]
            print(f"    {nm}: ray {j} = {r} -> img {img}")

    deduped = dedup_by_matrix(feasible)
    print(f"  After dedup: {len(deduped)} distinct pieces")
    print(f"  Registry-build time: {time.time()-t0:.2f}s")

    t1 = time.time()
    per_var = {}
    axis_vars = []
    for c_idx, av in enumerate(aii_v):
        r = strict_axis_for_var(deduped, c_idx, n_bdi)
        per_var[av] = r
        if r["is_axis"]:
            axis_vars.append(av)
    print(f"  Strict #AXIS analysis time: {time.time()-t1:.2f}s")

    n_axis = len(axis_vars)
    pred_count = 2 * (n - 1)
    pred_vars = predicted_axis_vars(n)

    print(f"\n  STRICT #AXIS = {n_axis}")
    print(f"  Day-72 prediction 2(n-1) = {pred_count}")
    print(f"  Match: {'YES' if n_axis == pred_count else 'NO'}")
    print(f"\n  AXIS vars:     {sorted(axis_vars)}")
    print(f"  Predicted:     {sorted(pred_vars)}")
    matched = set(axis_vars) == set(pred_vars)
    print(f"  Var-set match: {'YES' if matched else 'NO'}")
    if not matched:
        missing = set(pred_vars) - set(axis_vars)
        extra = set(axis_vars) - set(pred_vars)
        if missing:
            print(f"    Missing (predicted but not AXIS): {sorted(missing)}")
        if extra:
            print(f"    Extra (AXIS but not predicted): {sorted(extra)}")

    print(f"\n  Per-var max_3clique_size:")
    for av in aii_v:
        d = per_var[av]
        mark = " AXIS" if d["is_axis"] else ""
        print(f"    {av:<14}  max = {d['max_group_size']}{mark}")

    return {
        "n": n,
        "n_pieces": len(deduped),
        "n_aii_vars": n_aii,
        "n_bdi_vars": n_bdi,
        "strict_n_axis": n_axis,
        "axis_vars": sorted(axis_vars),
        "predicted_axis_vars": sorted(pred_vars),
        "predicted_count_2nm1": pred_count,
        "count_match": n_axis == pred_count,
        "var_set_match": matched,
        "missing_predicted": sorted(set(pred_vars) - set(axis_vars)),
        "extra_unpredicted": sorted(set(axis_vars) - set(pred_vars)),
        "per_var": {av: {
            "max_group_size": d["max_group_size"],
            "is_axis": d["is_axis"],
        } for av, d in per_var.items()},
    }


def verify_test():
    """Cross-check: ensure Day-72 n=5 result reproduces (regression
    guard before lifting to n=8, 9)."""
    print("\n[verify_test] Regenerating n=5 strict #AXIS as sanity check...")
    out = run_for_n(5)
    expected = 8  # Day-72: n=5 gave 8 = 2*(5-1)
    assert out["strict_n_axis"] == expected, (
        f"REGRESSION: n=5 strict #AXIS = {out['strict_n_axis']}, "
        f"expected {expected}"
    )
    print(f"[verify_test] n=5 strict #AXIS = {out['strict_n_axis']} == "
          f"{expected} OK")
    return out


def main():
    results = {}

    # Regression guard.
    results[5] = verify_test()

    # New: n = 8, 9.
    for n in [8, 9]:
        results[n] = run_for_n(n)

    # Summary table
    print(f"\n{'='*70}")
    print(f"SUMMARY: Strict #AXIS vs 2(n-1) extrapolation")
    print(f"{'='*70}")
    print(f"  {'n':>3}  {'# pieces':>10}  {'#AXIS':>6}  "
          f"{'pred=2(n-1)':>12}  {'match':>6}  {'vars OK':>8}")
    for n in sorted(results.keys()):
        r = results[n]
        cm = "YES" if r["count_match"] else "NO"
        vm = "YES" if r["var_set_match"] else "NO"
        print(f"  {n:>3}  {r['n_pieces']:>10}  {r['strict_n_axis']:>6}  "
              f"{r['predicted_count_2nm1']:>12}  {cm:>6}  {vm:>8}")

    # Day-72 + Day-73 growth check
    print(f"\n  Growth check (n=5,6,7 from Day-72; n=8,9 from Day-73):")
    day72 = {5: 8, 6: 10, 7: 12}
    combined = dict(day72)
    for n, r in results.items():
        combined[n] = r["strict_n_axis"]
    for n in sorted(combined.keys()):
        pred = 2 * (n - 1)
        status = "OK" if combined[n] == pred else "MISMATCH"
        print(f"    n={n}: #AXIS = {combined[n]}, pred = {pred}  {status}")

    out_path = OUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  saved results to {out_path}")

    # Pass/fail headline
    all_match = all(r["count_match"] and r["var_set_match"]
                    for n, r in results.items() if n in (8, 9))
    print(f"\n{'='*70}")
    print(f"HEADLINE: 2(n-1) extrapolation at n=8,9: "
          f"{'CONFIRMED' if all_match else 'BROKEN'}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
