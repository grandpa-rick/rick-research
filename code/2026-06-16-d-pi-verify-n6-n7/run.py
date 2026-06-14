#!/usr/bin/env python3
"""
Day 71 CODE Task A — Verify Conjecture D-pi at n=6 and n=7.

Statement (within the Day-70 minimal-cover registry):
  for every interior prefix coord p_i with 1 < i < n-1, all pieces in
  the registry route p_i identically (i.e. the column M[:, idx(p_i)]
  is the same vector across all pieces).

Method:
  Load Day-70 n=6 and n=7 registries. For each interior i, collect
  the set of distinct routing columns over the 36 (n=6) / 44 (n=7)
  feasible pieces. Conjecture D-pi predicts exactly 1.

We also cross-check the D-pi-refutation-verify (Day-70+) result:
  pieces with routing B_i + S, B_i + 2S are individually BDI-feasible,
  but they are NOT in the Day-70 minimal-cover registry (because the
  registry only includes pieces from the structural base + R-double
  family, which by construction keeps p_i routing canonical). So
  D-pi in the restricted "registry" sense is consistent with the
  3-clique refutation in the "all feasible" sense — the registry is
  a strict subset of all feasible pieces.

Output:
  results.json — full per-i routing analysis at n=6, 7.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, "/home/agent/projects/code/2026-06-15-axis-n6-n7-count")
from general_axis import aii_struct, bdi_vars  # noqa: E402


REG_DIR = Path("/home/agent/projects/code/2026-06-15-axis-n6-n7-count")
OUT_DIR = Path("/home/agent/projects/code/2026-06-16-d-pi-verify-n6-n7")
OUT_DIR.mkdir(exist_ok=True)


def labelled_col(col, bdi_names):
    """Convert a column (list of ints) -> dict {bdi_name: coef}."""
    return {bdi_names[i]: c for i, c in enumerate(col) if c != 0}


def analyze_n(n):
    """Analyze D-pi conjecture at level n.

    Returns dict with per-interior-i routing summary.
    """
    reg_path = REG_DIR / f"n{n}_registry.json"
    with open(reg_path) as f:
        reg = json.load(f)
    n_pieces = len(reg)
    bdi_names = bdi_vars(n)
    n_bdi = len(bdi_names)

    # Interior prefix coords: 1 < i < n-1, i.e. i in {2, ..., n-2}.
    interior_is = list(range(2, n - 1))

    per_i = {}
    for i in interior_is:
        key = f"prefix[{i}]"
        routings = {}   # column tuple -> list of piece names
        for piece_name, cols in reg.items():
            col = tuple(cols[key])
            assert len(col) == n_bdi, (piece_name, key, len(col), n_bdi)
            routings.setdefault(col, []).append(piece_name)
        per_i[i] = {
            "n_distinct_routings": len(routings),
            "routings": [
                {
                    "column": list(col),
                    "labelled": labelled_col(col, bdi_names),
                    "n_pieces": len(names),
                    "example_pieces": names[:5],
                }
                for col, names in routings.items()
            ],
            "d_pi_holds": (len(routings) == 1),
        }

    # Also check boundary cases (i = 1 and i = n-1, n) for the record.
    # i = 1 is AXIS (R-double family) so multiple routings expected.
    # i = n is AXIS (free prefix) so multiple routings expected.
    boundary_summary = {}
    for i in [1, n - 1, n]:
        key = f"prefix[{i}]"
        routings = {}
        for piece_name, cols in reg.items():
            col = tuple(cols[key])
            routings.setdefault(col, []).append(piece_name)
        boundary_summary[i] = {
            "n_distinct_routings": len(routings),
            "is_axis_or_rigid": ("AXIS" if len(routings) > 1
                                 else "RIGID"),
        }

    interior_dpi_holds = all(per_i[i]["d_pi_holds"] for i in interior_is)

    return {
        "n": n,
        "n_pieces": n_pieces,
        "n_bdi": n_bdi,
        "interior_is": interior_is,
        "per_interior_i": per_i,
        "boundary_summary": boundary_summary,
        "d_pi_verdict": (
            "VERIFIED" if interior_dpi_holds else "REFUTED"
        ),
    }


def main():
    print("=" * 72)
    print("Day 71 CODE Task A — Conjecture D-pi at n=6, 7")
    print("=" * 72)

    all_results = {}
    for n in [6, 7]:
        print(f"\n--- n = {n} ---")
        r = analyze_n(n)
        all_results[n] = r
        print(f" n_pieces (registry): {r['n_pieces']}")
        print(f" interior i (1 < i < n-1): {r['interior_is']}")
        for i in r["interior_is"]:
            d = r["per_interior_i"][i]
            tag = "OK" if d["d_pi_holds"] else "FAIL"
            print(f"  i={i}: # distinct routings = "
                  f"{d['n_distinct_routings']} [{tag}]")
            if not d["d_pi_holds"]:
                for rt in d["routings"]:
                    print(f"    routing {rt['labelled']} "
                          f"({rt['n_pieces']} pieces)")
        print(f" Verdict: D-pi {r['d_pi_verdict']}")
        print(f" Boundary (sanity check):")
        for i, s in r["boundary_summary"].items():
            print(f"  i={i} ({s['is_axis_or_rigid']}): "
                  f"# routings = {s['n_distinct_routings']}")

    # Save
    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nsaved: {OUT_DIR/'results.json'}")

    # Overall verdict
    overall = all(all_results[n]["d_pi_verdict"] == "VERIFIED"
                  for n in [6, 7])
    print("\n" + "=" * 72)
    print("OVERALL VERDICT")
    print("=" * 72)
    if overall:
        print("Conjecture D-pi VERIFIED at n=6 and n=7 within the")
        print("Day-70 minimal-cover registry. Interior prefix coords are")
        print("RIGID (single routing across all registry pieces).")
        print()
        print("Caveat: the 3-clique refutation work (Day-70+)")
        print("(code/2026-06-16-dpi-refutation-verify/) shows that")
        print("pieces with routing B_i + S, B_i + 2*S are individually")
        print("BDI-feasible. They are NOT in the registry. D-pi as")
        print("stated holds; if the registry is expanded to all feasible")
        print("pieces, the unique-routing claim fails.")
    else:
        print("Conjecture D-pi REFUTED. See per-i routing breakdown.")
        print("PROVE session must pivot.")


if __name__ == "__main__":
    main()
