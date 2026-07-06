#!/usr/bin/env python3
"""
Day 2026-07-06 CODE — Strict #AXIS partition into prefix-strict + long-strict
                       extended to n = 10, 11, 12.

Adapts the Day-81 partition.py to higher n. Same coordinate-level definition
(Day-72 Rick convention: an AII coord c is strict-AXIS iff the augmented
registry contains a 3-clique of pieces agreeing everywhere except column c).

Uses:
  - bdi_universal.aii_rays(n)          (parametric on n, sanctioned)
  - build_augmented_registry(n)         (parametric on n)
  - strict_axis_diagnostic (3-clique)   (parametric on n)

Expected under Theorem 10.1 (Rick):
  n=10: 9 prefix-strict + 9 long-strict = 18
  n=11: 10 prefix-strict + 10 long-strict = 20
  n=12: 11 prefix-strict + 11 long-strict = 22

Predicted set-theoretic partition:
  prefix-strict = {prefix[1..n-2], prefix[n]}          |·| = n-1
  long-strict   = {long[1..n-1]}                        |·| = n-1
  non-AXIS       = {prefix[n-1], long[n], short[i], linkLHS}

CSV output columns (same as Day-81):
  - strict_axis_partition_n10_n12.csv        (n, n_prefix_strict, n_long_strict,
                                              n_both, n_neither, total)
  - strict_axis_indexed_n10_n12.csv          (n, coord, category, i_position,
                                              max_group_size, example_summary)
"""
from __future__ import annotations

import sys
import csv
import time
import signal
from pathlib import Path
from collections import defaultdict

# Day-79 bdi_universal — sanctioned rays
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

OUT_DIR = Path("/home/agent/projects/code/2026-07-06-strict-axis-n10-n12")
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
# Parse AII coord names
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
    t_reg = time.time() - t0
    print(f"  built registry: raw={len(reg)} ({t_reg:.1f}s)")

    t0 = time.time()
    feasible = filter_feasible_bu(reg, n)
    t_feas = time.time() - t0
    print(f"  filtered feasible: {len(feasible)} ({t_feas:.1f}s)")

    t0 = time.time()
    deduped = dedup_by_matrix(feasible)
    t_dedup = time.time() - t0
    print(f"  deduped: {len(deduped)} ({t_dedup:.1f}s), rays={len(rays_bu)}")

    t0 = time.time()
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
    t_scan = time.time() - t0
    print(f"  strict-AXIS scan: {len(axis_rows)} coords ({t_scan:.1f}s)")
    total_t = t_reg + t_feas + t_dedup + t_scan
    print(f"  TOTAL n={n}: {total_t:.1f}s")
    return axis_rows, per_var, total_t


def verify_theorem_101_partition(n, axis_rows):
    """Check the predicted set-theoretic partition from Theorem 10.1."""
    predicted_prefix = set([f"prefix[{i}]" for i in range(1, n - 1)]
                           + [f"prefix[{n}]"])
    predicted_long = set([f"long[{i}]" for i in range(1, n)])
    predicted_axis = predicted_prefix | predicted_long

    empirical_prefix = set(r["coord"] for r in axis_rows
                           if r["category"] == "prefix-strict")
    empirical_long = set(r["coord"] for r in axis_rows
                         if r["category"] == "long-strict")
    empirical_axis = empirical_prefix | empirical_long

    pref_ok = predicted_prefix == empirical_prefix
    long_ok = predicted_long == empirical_long
    return {
        "prefix_match": pref_ok,
        "long_match": long_ok,
        "predicted_prefix": sorted(predicted_prefix),
        "predicted_long": sorted(predicted_long),
        "empirical_prefix": sorted(empirical_prefix),
        "empirical_long": sorted(empirical_long),
        "missing_prefix": sorted(predicted_prefix - empirical_prefix),
        "extra_prefix": sorted(empirical_prefix - predicted_prefix),
        "missing_long": sorted(predicted_long - empirical_long),
        "extra_long": sorted(empirical_long - predicted_long),
    }


def main():
    all_rows = []
    per_n_counts = {}
    per_n_verify = {}
    runtimes = {}
    # 15-minute per-n cap
    time_cap_seconds = 15 * 60

    ns_to_run = [10, 11, 12]
    completed = []
    for n in ns_to_run:
        try:
            t_start = time.time()
            rows, per_var, elapsed = run_for_n(n)
            runtimes[n] = elapsed
            all_rows.extend(rows)

            n_pref = sum(1 for r in rows if r["category"] == "prefix-strict")
            n_long = sum(1 for r in rows if r["category"] == "long-strict")
            n_both = 0
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
                  f"expected 2(n-1)={expected}, "
                  f"match={total==expected and n_neither==0}")

            # Verify against Theorem 10.1 predicted partition
            v = verify_theorem_101_partition(n, rows)
            per_n_verify[n] = v
            print(f"  Theorem 10.1 partition check:")
            print(f"    prefix-strict match: {v['prefix_match']}")
            if not v['prefix_match']:
                print(f"      missing from empirical: {v['missing_prefix']}")
                print(f"      extra in empirical: {v['extra_prefix']}")
            print(f"    long-strict match:   {v['long_match']}")
            if not v['long_match']:
                print(f"      missing from empirical: {v['missing_long']}")
                print(f"      extra in empirical: {v['extra_long']}")

            completed.append(n)
            if elapsed > time_cap_seconds:
                print(f"\nWARNING: n={n} took {elapsed:.0f}s (> 15 min cap).")
                print(f"Skipping any higher n.")
                break
        except Exception as e:
            print(f"\nERROR at n={n}: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            break

    # --- CSV 1: partition summary ---
    p1 = OUT_DIR / "strict_axis_partition_n10_n12.csv"
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
    p2 = OUT_DIR / "strict_axis_indexed_n10_n12.csv"
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
    print(f"PARTITION SUMMARY (n = 10, 11, 12)")
    print(f"{'='*70}")
    print(f"{'n':>3} {'pref':>5} {'long':>5} {'both':>5} {'neither':>8} "
          f"{'total':>6} {'expected':>9} {'match':>6} {'time_s':>8}")
    for n in sorted(per_n_counts):
        c = per_n_counts[n]
        m = "YES" if c["match"] else "NO"
        rt = runtimes.get(n, -1)
        print(f"{n:>3} {c['n_prefix_strict']:>5} {c['n_long_strict']:>5} "
              f"{c['n_both']:>5} {c['n_neither']:>8} {c['total']:>6} "
              f"{c['expected_2nm1']:>9} {m:>6} {rt:>8.1f}")

    all_match = all(per_n_counts[n]["match"] for n in per_n_counts)
    all_partition_match = all(
        per_n_verify[n]["prefix_match"] and per_n_verify[n]["long_match"]
        for n in per_n_verify
    )
    print(f"\nCOUNT MATCH (2(n-1)):          "
          f"{'CONFIRMED' if all_match else 'BROKEN'} at n in {completed}")
    print(f"THEOREM 10.1 PARTITION MATCH: "
          f"{'CONFIRMED' if all_partition_match else 'BROKEN'} at n in {completed}")

    if not all_match or not all_partition_match:
        print("\n*** CRITICAL: deviation from Theorem 10.1 detected. ***")


if __name__ == "__main__":
    main()
