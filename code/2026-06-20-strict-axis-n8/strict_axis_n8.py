#!/usr/bin/env python3
"""
Day 75 CODE Task C (stretch) -- Strict #AXIS at n = 8.

GOAL:
  Confirm strict #AXIS = 2(n-1) = 14 at n = 8 using the augmented
  registry (Day-72 cover + Day-71 simple-divert + Day-72 l_j-divert
  + Class-1 aux).

NOTE:
  Day-73 already verified n = 8 AND n = 9 (see
  `code/2026-06-18-strict-axis-n8-n9/`). This Day-75 run is a clean
  re-verification at n = 8 in the dedicated directory CODE.md asks
  for. We also include n = 5 as a regression guard.

ACCEPTANCE: PASS = strict #AXIS at n = 8 is 14; AXIS var set =
  {p_1, ..., p_{n-2}, p_n, l_1, ..., l_{n-1}}.
"""

from __future__ import annotations
import json
import sys
import importlib.util
from pathlib import Path

sys.path.insert(0, '/home/agent/projects/code/2026-06-18-strict-axis-n8-n9')

_spec = importlib.util.spec_from_file_location(
    "day73_strict_axis",
    "/home/agent/projects/code/2026-06-18-strict-axis-n8-n9/strict_axis.py")
_day73 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day73)

HERE = Path(__file__).resolve().parent


def main():
    print("=" * 76)
    print("Day 75 CODE Task C (stretch) -- Strict #AXIS at n = 8")
    print("=" * 76)

    results = {}

    # Regression: n=5 should still give 8.
    print("\n[regression] n = 5 (should give strict #AXIS = 8)")
    r5 = _day73.run_for_n(5)
    assert r5["strict_n_axis"] == 8, (
        f"REGRESSION FAIL at n=5: got {r5['strict_n_axis']}, expected 8")
    results[5] = r5

    # Target: n=8 should give 14.
    print("\n[target] n = 8 (should give strict #AXIS = 14)")
    r8 = _day73.run_for_n(8)
    results[8] = r8

    expected_n8 = 14
    expected_set_n8 = set(_day73.predicted_axis_vars(8))
    got_n8 = r8["strict_n_axis"]
    got_set_n8 = set(r8["axis_vars"])

    count_ok = (got_n8 == expected_n8)
    set_ok = (got_set_n8 == expected_set_n8)

    print(f"\n  TARGET: strict #AXIS at n=8 = {got_n8} (expected {expected_n8})")
    print(f"          Match: {'YES' if count_ok else 'NO'}")
    print(f"          Var-set match: {'YES' if set_ok else 'NO'}")

    verdict = "PASS" if count_ok and set_ok else "FAIL"

    print("\n" + "=" * 76)
    print(f"VERDICT: {verdict} -- 2(n-1) extrapolation confirmed at n=8" if verdict == "PASS"
          else f"VERDICT: {verdict}")
    print("=" * 76)

    out = {
        "task": "Day 75 CODE Task C (stretch) -- strict #AXIS at n = 8",
        "verdict": verdict,
        "n5_regression": {
            "strict_n_axis": r5["strict_n_axis"],
            "expected": 8,
            "ok": r5["strict_n_axis"] == 8,
        },
        "n8_target": {
            "strict_n_axis": got_n8,
            "expected": expected_n8,
            "count_match": count_ok,
            "var_set_match": set_ok,
            "axis_vars": r8["axis_vars"],
            "predicted_axis_vars": r8["predicted_axis_vars"],
            "missing_predicted": r8["missing_predicted"],
            "extra_unpredicted": r8["extra_unpredicted"],
            "n_pieces": r8["n_pieces"],
        },
    }
    with open(HERE / "results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE/'results.json'}")


if __name__ == "__main__":
    main()
