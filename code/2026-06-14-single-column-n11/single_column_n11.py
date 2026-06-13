#!/usr/bin/env python3
"""
Day 69 CODE Task 2 — single-column lemma at n=10 and n=11.

Extends OQ-PI3-GROWTH branch (a) — currently closed at n in {2,..,9}.
Reuses the general-n machinery from
`code/2026-06-12-single-column-n67/single_column_n67.py`.

Single-column piece pi^(g)(p) := p[long[1]] * g.
Strategy: BDI is a polyhedral cone -> closed under nonneg integer
scaling, so pi^(g) is feasible whenever g is. Verifies by sampling
100 random BDI-feasible lattice points and scaling by k in [0, 10].
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
    print("Day 69 CODE Task 2 -- Single-column lemma at n=10 and n=11")
    print("=" * 72)

    results = {}
    for n in [10, 11]:
        t0 = time.time()
        results[n] = test_single_column_n(
            n, n_samples=100, N_max=10, k_range=(0, 11), seed=6500 + n
        )
        dt = time.time() - t0
        results[n]["wall_seconds"] = dt
        print(f"\n  n={n}: wall {dt:.1f}s")

    print()
    print("=" * 72)
    print("Summary")
    print("=" * 72)
    for n in [10, 11]:
        r = results[n]
        print(
            f" n={n}: {r['n_pass']}/{r['n_samples']} pass, "
            f"{r['n_fail']} fail, long[1] free: "
            f"{r['long1_info']['is_free']}, wall {r['wall_seconds']:.1f}s"
        )

    out_dir = Path(__file__).parent
    with open(out_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'results.json'}")


if __name__ == "__main__":
    main()
