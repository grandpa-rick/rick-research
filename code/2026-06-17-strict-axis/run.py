"""
Day 72 CODE Task B -- Strict # AXIS at n = 5, 6, 7.

DEFINITION (Day-71 + Day-72 R-AXIS framework):
  A coord c is "STRICT AXIS" for a registry R iff there exist three
  pieces pi_1, pi_2, pi_3 in R such that
    (i) for every c' != c, the column M[:, c'] is equal across all three;
    (ii) the three columns M[:, c] are pairwise distinct.
  This is a 3-clique on the wall {c = 0}.

ALGORITHM:
  For each AII coord c:
    group pieces by their "key" = tuple of all columns except c.
    for each group: count distinct c-column values within.
    if some group has count >= 3: c is AXIS.

INPUT: registry-n{5,6,7}.json from 2026-06-17-complete-registry/.

OUTPUT: results.json with the strict # AXIS at each n and per-axis
diagnostics.
"""

import sys
import json
from pathlib import Path
from collections import defaultdict

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
from general_axis import aii_struct, bdi_vars

REG_DIR = Path("/home/agent/projects/code/2026-06-17-complete-registry")
OUT_DIR = Path("/home/agent/projects/code/2026-06-17-strict-axis")
OUT_DIR.mkdir(exist_ok=True)


def load_registry(n):
    with open(REG_DIR / f"registry-n{n}.json") as f:
        reg = json.load(f)
    s = aii_struct(n)
    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    n_aii = s["n_vars"]
    pieces = {}
    for name, cols in reg.items():
        M = np.zeros((n_bdi, n_aii), dtype=int)
        for av, col in cols.items():
            c = aii_v.index(av)
            for r in range(n_bdi):
                M[r, c] = col[r]
        pieces[name] = M
    return pieces, s


def column_of(M, c, n_bdi):
    return tuple(int(M[r, c]) for r in range(n_bdi))


def strict_axis_for_var(pieces_dict, c_idx, n_bdi):
    """For coord index c_idx: group pieces by "other columns" key; count
    distinct M[:, c_idx] within each group. Return:
      - max_group_size: largest # distinct c-cols within one group
      - max_3clique_group: an example group with >=3 distinct c-cols
      - is_axis: bool
    """
    groups = defaultdict(set)   # key (other cols) -> set of M[:, c_idx]
    groups_pieces = defaultdict(list)  # key -> list of piece names
    n_aii = next(iter(pieces_dict.values())).shape[1]
    for name, M in pieces_dict.items():
        key = tuple(column_of(M, c, n_bdi) for c in range(n_aii) if c != c_idx)
        col_c = column_of(M, c_idx, n_bdi)
        groups[key].add(col_c)
        groups_pieces[key].append((name, col_c))
    max_size = max((len(s) for s in groups.values()), default=0)
    example_group = None
    if max_size >= 3:
        for key, s in groups.items():
            if len(s) >= 3:
                example_group = groups_pieces[key]
                break
    return {
        "max_group_size": max_size,
        "is_axis": max_size >= 3,
        "example_group_size3": example_group,
    }


def run_for_n(n):
    print(f"\n{'='*70}")
    print(f"n = {n}")
    print(f"{'='*70}")
    pieces, s = load_registry(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    n_aii = len(aii_v)
    print(f"  Loaded {len(pieces)} pieces from registry-n{n}.json")

    per_var = {}
    axis_vars = []
    for c_idx, av in enumerate(aii_v):
        r = strict_axis_for_var(pieces, c_idx, n_bdi)
        per_var[av] = r
        if r["is_axis"]:
            axis_vars.append(av)

    n_axis = len(axis_vars)
    pred_lower = n + 1

    print(f"\n  STRICT AXIS COUNT: # AXIS = {n_axis}")
    print(f"  Day-71 prediction: # AXIS >= n + 1 = {pred_lower}")
    print(f"  {'CONFIRMED' if n_axis >= pred_lower else 'BELOW PREDICTION'}")
    print(f"\n  Axis vars: {axis_vars}")
    print(f"\n  Per-var diagnostics:")
    for av in aii_v:
        d = per_var[av]
        marker = " AXIS" if d["is_axis"] else ""
        print(f"    {av:<14}  max_3clique_size = {d['max_group_size']}{marker}")

    return {
        "n": n,
        "n_pieces": len(pieces),
        "n_aii_vars": n_aii,
        "strict_n_axis": n_axis,
        "axis_vars": axis_vars,
        "prediction_lower_bound": pred_lower,
        "confirmed": n_axis >= pred_lower,
        "per_var": {av: {
            "max_group_size": d["max_group_size"],
            "is_axis": d["is_axis"],
            "example_3clique": (
                [(name, list(col)) for name, col in d["example_group_size3"]]
                if d["example_group_size3"] else None
            ),
        } for av, d in per_var.items()},
    }


def main():
    results = {}
    for n in [5, 6, 7]:
        results[n] = run_for_n(n)

    # Summary table
    print(f"\n{'='*70}")
    print(f"SUMMARY: strict # AXIS vs Day-71 prediction")
    print(f"{'='*70}")
    print(f"{'n':>3}  {'# pieces':>10}  {'# AXIS':>8}  {'pred (n+1)':>11}  status")
    for n in [5, 6, 7]:
        r = results[n]
        s = "OK" if r["confirmed"] else "BELOW"
        print(f"{n:>3}  {r['n_pieces']:>10}  {r['strict_n_axis']:>8}  "
              f"{r['prediction_lower_bound']:>11}  {s}")

    # Linear growth check
    print(f"\n  Δ(# AXIS) from n=5..7:")
    cnts = [results[n]["strict_n_axis"] for n in [5, 6, 7]]
    deltas = [cnts[i + 1] - cnts[i] for i in range(2)]
    print(f"    counts = {cnts}, Δ = {deltas}")
    if all(d > 0 for d in deltas):
        print(f"    LINEAR GROWTH CONFIRMED (Δ > 0 between consecutive n)")
    else:
        print(f"    NON-MONOTONE -- inspect.")

    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nsaved results.json")


if __name__ == "__main__":
    main()
