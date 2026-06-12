#!/usr/bin/env python3
"""
Day 67 CODE Task 3 — single-column lemma at n=8.

Extends OQ-PI3-GROWTH branch (a) — currently closed at n ∈ {2,...,7}.
Reuses the general-n machinery from
`code/2026-06-12-single-column-n67/single_column_n67.py`.

Goal: 100 random BDI-feasible lattice samples at n=8, scaled by k ∈ [0,10].
Expect 100/100 (structural: BDI cone closed under nonneg integer scaling).
"""

import sys, json

sys.path.insert(0, "/home/agent/projects/code/2026-06-12-single-column-n67")
from single_column_n67 import test_single_column_n
from pathlib import Path


def main():
    print("=" * 70)
    print("Day 67 CODE Task 3 — Single-column lemma at n=8")
    print("=" * 70)

    results = {}
    for n in [8]:
        results[n] = test_single_column_n(
            n, n_samples=100, N_max=10, k_range=(0, 11), seed=6500 + n
        )

    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    for n in [8]:
        r = results[n]
        print(
            f" n={n}: {r['n_pass']}/{r['n_samples']} pass, "
            f"{r['n_fail']} fail, long[1] free: "
            f"{r['long1_info']['is_free']}"
        )

    out_dir = Path(__file__).parent
    with open(out_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'results.json'}")


if __name__ == "__main__":
    main()
