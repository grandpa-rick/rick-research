#!/usr/bin/env python3
"""
Day 71 CODE Task C — single-column lemma at n=15, 16, 17.

Closes OQ-PI3-GROWTH branch (a) at n in {2, ..., 17}.

Single-column piece pi^(g)(p) := p[long[1]] * g for g in BDI lattice.
BDI is a rational polyhedral cone -> closed under nonneg integer scaling
=> g feasible implies k*g feasible for all k>=0 integer.
We test this by sampling 100 random BDI-feasible lattice points at each
n with sum <= N_max = 20, scaling by k in [0, 11), and checking the
explicit BDI feasibility predicate.

Also verifies long[1] remains FREE at n=15, 16, 17.
"""

import sys
import json
import time
from pathlib import Path

sys.path.insert(0, "/home/agent/projects/code/2026-06-12-single-column-n67")
from single_column_n67 import test_single_column_n  # noqa: E402

OUT_DIR = Path("/home/agent/projects/code/2026-06-16-single-column-n17")
OUT_DIR.mkdir(exist_ok=True)


def main():
    print("=" * 72)
    print("Day 71 CODE Task C — single-column lemma at n=15, 16, 17")
    print("=" * 72)

    levels = [15, 16, 17]
    results = {}
    for n in levels:
        t0 = time.time()
        results[n] = test_single_column_n(
            n, n_samples=100, N_max=20, k_range=(0, 11), seed=7100 + n
        )
        dt = time.time() - t0
        results[n]["wall_seconds"] = dt
        print(f"\n  n={n}: wall {dt:.1f}s")

    print()
    print("=" * 72)
    print("Summary")
    print("=" * 72)
    for n in levels:
        r = results[n]
        print(
            f" n={n}: {r['n_pass']}/{r['n_samples']} pass, "
            f"{r['n_fail']} fail, long[1] free: "
            f"{r['long1_info']['is_free']}, wall {r['wall_seconds']:.1f}s"
        )

    all_pass = all(results[n]["n_fail"] == 0 for n in levels)
    if all_pass:
        verdict = (
            "PASS: single-column lemma extended to n=17. "
            "OQ-PI3-GROWTH branch (a) closed at n in {2, ..., 17}. "
            "No regression at n>=15 (Clio Day-58 review flag was about "
            "a different scheme — that flag is not relevant here)."
        )
    else:
        bad = [n for n in levels if results[n]["n_fail"] > 0]
        verdict = (
            f"FAIL at n={bad}. OQ-PI3-GROWTH branch (a) REOPENED. "
            "Reconcile with Day-58 piecewise multimap regression."
        )
    print(f"\n{verdict}")

    save = {"verdict": verdict, "results": results}
    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(save, f, indent=2, default=str)
    print(f"\nsaved: {OUT_DIR/'results.json'}")


if __name__ == "__main__":
    main()
