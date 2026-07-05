#!/usr/bin/env python3
"""
Day 2026-07-05 CODE — Strict #AXIS partition into prefix-strict + long-strict.

GOAL
====
For each n in {5, 6, 7, 8, 9}:
  1. Enumerate strict-AXIS coordinates (Day-72 Rick convention:
     an AII coord c is strict-AXIS iff the augmented registry contains
     a 3-clique of pieces agreeing everywhere except column c).
  2. Partition strict-AXIS coordinates into:
       prefix-strict: c is prefix[i] for some i
       long-strict:   c is long[j]   for some j
       both:          impossible by construction (a coord is prefix XOR long
                      XOR short XOR linkLHS) — always 0
       neither:       strict-AXIS coords not of prefix/long form
                      (empirically 0 in prior runs)
  3. Write CSVs and a per-ray-like table.

CLARIFICATION ON "strict-AXIS ray" vs "strict-AXIS coord"
=========================================================
The task prompt uses "strict-AXIS ray" and "escape from Im(pi_base)".
That framing does NOT match the codebase: Day 80 Theorem 9.2 proved
that EVERY AII extreme ray supports a single-column witness with image
in Im(pi_base), so no ray "escapes Im(pi_base)" — under the
counterpositive, 0 rays would be strict-AXIS. The expected counts
(4+4, 5+5, ..., 8+8 = 2(n-1)) match the Day-72 strict-AXIS *coordinate*
count, per code/2026-06-17-strict-axis/README.md.

I therefore interpret the task as: partition the strict-AXIS COORDINATES
(the 2(n-1) count) into prefix-strict + long-strict. Each strict-AXIS
coord is naturally associated with its "i-index" (prefix[i] -> i,
long[j] -> j), which fills the i_position column.

PIPELINE
========
1. Build augmented registry (Day-72 Rick pipeline) at each n.
2. Filter via bdi_universal AII rays.
3. Dedup by piece matrix.
4. For each AII coord c, compute strict-AXIS status by 3-clique test.
5. Partition axis vars by prefix / long / other.
6. Emit CSVs.
"""
from __future__ import annotations

import sys
import csv
import time
from pathlib import Path
from collections import defaultdict

# Day-79 bdi_universal — correct rays
sys.path.insert(0, '/home/agent/projects/code/2026-06-19-droppability-n7-boundary')
import bdi_universal as bu  # noqa: E402

# Augmented-registry builder + strict-AXIS infrastructure
sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
sys.path.insert(0, '/home/agent/projects/code/2026-06-17-complete-registry')

from general_axis import (  # noqa: E402
    aii_struct, bdi_vars, piece_matrix,
)
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location(
    "day72_registry_run",
    "/home/agent/projects/code/2026-06-17-complete-registry/run.py")
_day72 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day72)
build_augmented_registry = _day72.build_augmented_registry
dedup_by_matrix = _day72.dedup_by_matrix

OUT_DIR = Path("/home/agent/projects/code/2026-07-05-strict-axis-partition")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------
# Ray-feasibility using bdi_universal
# ---------------------------------------------------------------------
def piece_dict_from_matrix(M, n):
    s = aii_struct(n)
    aii_v = s["vars"]
    piece = {}
    for c, name in enumerate(aii_v):
        piece[name] = tuple(int(M[r, c]) for r in range(M.shape[0]))
    return piece


def verify_piece_via_universal(M, n):
    piece = piece_dict_from_matrix(M, n)
    rays = bu.aii_rays(n)
    for r in rays:
        img = bu.ray_image(piece, r)
        if not bu.is_BDI(n, img):
            return False
    return True


def filter_feasible_bu(registry, n):
    return {name: M for name, M in registry.items()
            if verify_piece_via_universal(M, n)}


# ---------------------------------------------------------------------
# Strict AXIS 3-clique test on a coordinate
# ---------------------------------------------------------------------
def column_of(M, c, n_bdi):
    return tuple(int(M[r, c]) for r in range(n_bdi))


def strict_axis_diagnostic(pieces_dict, c_idx, n_bdi):
    """Return (is_axis, max_group_size, example_witness_columns)."""
    groups = defaultdict(set)
    n_aii = next(iter(pieces_dict.values())).shape[1]
    for name, M in pieces_dict.items():
        key = tuple(column_of(M, c, n_bdi) for c in range(n_aii) if c != c_idx)
        groups[key].add(column_of(M, c_idx, n_bdi))
    max_size = 0
    example = None
    for cols in groups.values():
        if len(cols) > max_size:
            max_size = len(cols)
            example = sorted(cols)
    return max_size >= 3, max_size, example


# ---------------------------------------------------------------------
# Parse AII coord names like "prefix[3]" or "long[5]" or "short[2]"
# ---------------------------------------------------------------------
def parse_coord(name: str):
    if name.startswith("prefix["):
        return ("prefix", int(name[len("prefix["):-1]))
    if name.startswith("long["):
        return ("long", int(name[len("long["):-1]))
    if name.startswith("short["):
        return ("short", int(name[len("short["):-1]))
    if name == "linkLHS":
        return ("linkLHS", 0)
    return ("other", 0)


def classify(family: str) -> str:
    if family == "prefix":
        return "prefix-strict"
    if family == "long":
        return "long-strict"
    return "neither"


# ---------------------------------------------------------------------
# Per-n driver
# ---------------------------------------------------------------------
def run_for_n(n):
    print(f"\n{'='*70}")
    print(f"n = {n}")
    print(f"{'='*70}")
    s = aii_struct(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    rays_bu = bu.aii_rays(n)

    t0 = time.time()
    reg = build_augmented_registry(n)
    feasible = filter_feasible_bu(reg, n)
    deduped = dedup_by_matrix(feasible)
    print(f"  registry: raw={len(reg)}, feasible={len(feasible)}, "
          f"deduped={len(deduped)}, rays={len(rays_bu)} "
          f"({time.time()-t0:.1f}s)")

    axis_rows = []
    per_var = {}
    for c_idx, av in enumerate(aii_v):
        is_ax, max_sz, example = strict_axis_diagnostic(deduped, c_idx, n_bdi)
        per_var[av] = {"is_axis": is_ax, "max_group_size": max_sz,
                       "example_cols": example}
        if is_ax:
            family, ii = parse_coord(av)
            cat = classify(family)
            example_summary = f"3 cols on wall {av}=0: {example[:3]}"
            axis_rows.append({
                "n": n, "coord": av, "category": cat,
                "i_position": ii, "max_group_size": max_sz,
                "example": example_summary,
            })
    return axis_rows, per_var


def main():
    all_rows = []
    per_n_counts = {}
    per_n_pervar = {}

    for n in (5, 6, 7, 8, 9):
        rows, per_var = run_for_n(n)
        all_rows.extend(rows)
        per_n_pervar[n] = per_var

        n_pref = sum(1 for r in rows if r["category"] == "prefix-strict")
        n_long = sum(1 for r in rows if r["category"] == "long-strict")
        n_both = 0  # by construction
        n_neither = sum(1 for r in rows if r["category"] == "neither")
        total = len(rows)
        expected = 2 * (n - 1)
        per_n_counts[n] = {
            "n_prefix_strict": n_pref,
            "n_long_strict": n_long,
            "n_both": n_both,
            "n_neither": n_neither,
            "total": total,
            "expected_2nm1": expected,
            "match": total == expected and n_neither == 0,
        }
        print(f"  strict-AXIS: prefix={n_pref}, long={n_long}, "
              f"both=0, neither={n_neither}, total={total}, "
              f"expected 2(n-1)={expected}, match={total==expected}")

    # --- CSV 1: partition summary ---
    p1 = OUT_DIR / "strict_axis_partition.csv"
    with open(p1, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "n_prefix_strict", "n_long_strict",
                    "n_both", "n_neither", "total"])
        for n in sorted(per_n_counts):
            c = per_n_counts[n]
            w.writerow([n, c["n_prefix_strict"], c["n_long_strict"],
                        c["n_both"], c["n_neither"], c["total"]])
    print(f"\nWrote CSV: {p1}")

    # --- CSV 2: indexed rows (per strict-AXIS coord) ---
    p2 = OUT_DIR / "strict_axis_indexed.csv"
    with open(p2, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "coord", "category", "i_position",
                    "max_group_size", "example_summary"])
        for r in all_rows:
            w.writerow([r["n"], r["coord"], r["category"], r["i_position"],
                        r["max_group_size"], r["example"]])
    print(f"Wrote CSV: {p2}")

    # --- console summary ---
    print(f"\n{'='*70}")
    print(f"PARTITION SUMMARY")
    print(f"{'='*70}")
    print(f"{'n':>3} {'pref':>5} {'long':>5} {'both':>5} {'neither':>8} "
          f"{'total':>6} {'expected':>9} {'match':>6}")
    for n in sorted(per_n_counts):
        c = per_n_counts[n]
        m = "YES" if c["match"] else "NO"
        print(f"{n:>3} {c['n_prefix_strict']:>5} {c['n_long_strict']:>5} "
              f"{c['n_both']:>5} {c['n_neither']:>8} {c['total']:>6} "
              f"{c['expected_2nm1']:>9} {m:>6}")

    all_match = all(per_n_counts[n]["match"] for n in per_n_counts)
    print(f"\nHEADLINE: (n-1) prefix-strict + (n-1) long-strict "
          f"partition: {'CONFIRMED' if all_match else 'BROKEN'} for "
          f"n in {{5,6,7,8,9}}")


if __name__ == "__main__":
    main()
