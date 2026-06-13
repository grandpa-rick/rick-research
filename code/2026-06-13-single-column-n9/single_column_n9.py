#!/usr/bin/env python3
"""
Day 68 CODE Task 2 — single-column lemma at n=9.

Extends OQ-PI3-GROWTH branch (a) — currently closed at n ∈ {2,...,8}.
Reuses the general-n machinery from
`code/2026-06-12-single-column-n67/single_column_n67.py`.

Single-column piece π^(g)(p) := p[long[1]] * g.
Strategy: BDI is a polyhedral cone → closed under nonneg integer
scaling, so π^(g) is feasible whenever g is. Verifies by sampling 100
random BDI-feasible lattice points at n=9 and scaling by k ∈ [0, 10].
"""

import sys, json
from pathlib import Path

sys.path.insert(0, "/home/agent/projects/code/2026-06-12-single-column-n67")
from single_column_n67 import test_single_column_n


def main():
    print("=" * 70)
    print("Day 68 CODE Task 2 — Single-column lemma at n=9")
    print("=" * 70)

    results = {}
    for n in [9]:
        results[n] = test_single_column_n(
            n, n_samples=100, N_max=10, k_range=(0, 11), seed=6500 + n
        )

    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    for n in [9]:
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
