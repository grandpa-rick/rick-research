#!/usr/bin/env python3
"""
Day 70 CODE Task B — single-column lemma at n=12, 13, 14.

Extends OQ-PI3-GROWTH branch (a) — currently closed at n in {2,..,11}
(Day 69 CODE Task 2).

Single-column piece pi^(g)(p) := p[long[1]] * g. BDI is a polyhedral
cone -> closed under nonneg integer scaling, so pi^(g) is feasible
whenever g is. Verifies by sampling 100 random BDI-feasible lattice
points and scaling by k in [0, 10].
"""

import sys
import json
import time
from pathlib import Path

sys.path.insert(
    0, "/home/agent/projects/code/2026-06-12-single-column-n67"
)
from single_column_n67 import test_single_column_n  # noqa: E402


def main():
    print("=" * 72)
    print("Day 70 CODE Task B -- Single-column lemma at n=12, 13, 14")
    print("=" * 72)

    results = {}
    for n in [12, 13, 14]:
        t0 = time.time()
        results[n] = test_single_column_n(
            n, n_samples=100, N_max=12, k_range=(0, 11), seed=7000 + n
        )
        dt = time.time() - t0
        results[n]["wall_seconds"] = dt
        print(f"\n  n={n}: wall {dt:.1f}s")

    print()
    print("=" * 72)
    print("Summary")
    print("=" * 72)
    for n in [12, 13, 14]:
        r = results[n]
        print(
            f" n={n}: {r['n_pass']}/{r['n_samples']} pass, "
            f"{r['n_fail']} fail, long[1] free: "
            f"{r['long1_info']['is_free']}, wall {r['wall_seconds']:.1f}s"
        )

    # Overall verdict
    all_pass = all(results[n]["n_fail"] == 0 for n in [12, 13, 14])
    if all_pass:
        verdict = (
            "PASS: single-column lemma extended to n=14. "
            "OQ-PI3-GROWTH branch (a) closed at n in {2,..,14}."
        )
    else:
        bad = [n for n in [12, 13, 14] if results[n]["n_fail"] > 0]
        verdict = (
            f"FAIL at n={bad}. OQ-PI3-GROWTH branch (a) REOPENED. "
            "Re-examine Day-58 piecewise multimap."
        )
    print(f"\n{verdict}")

    out_dir = Path(__file__).parent
    save = {"verdict": verdict, "results": results}
    with open(out_dir / "results.json", "w") as f:
        json.dump(save, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'results.json'}")


if __name__ == "__main__":
    main()
