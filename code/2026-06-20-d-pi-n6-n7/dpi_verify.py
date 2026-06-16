#!/usr/bin/env python3
"""
Day 75 CODE Task A -- D-pi verification at n = 6, 7.

STATEMENT VERIFIED (Day-71 "D-pi", restated cleanly for Day-75):
  For every interior coordinate p_i with 2 <= i <= n - 2, the three
  pieces
      pi_alpha^{(i)} := base + (alpha, p_i) in the S row,  alpha in {0, 1, 2}
  are simultaneously BDI-feasible (verified by Day-70 F1-F4 ray-image
  predicates), and their p_i columns are e_{B_i} + alpha * e_S --
  three distinct routings of p_i, all individually feasible.

This is the "3-clique on the wall {p_i = 0}" used by the Day-71/-72
pivot away from D-pi-as-uniqueness; here we re-verify cleanly at
n = 6, 7 with assert-rich code so the R-AXIS uniform-claim proof
gets a clean computational input.

HOW IT WORKS:
  1. Build base piece spec (Day-70 general_pieces.base_piece).
  2. For each interior i and alpha in {0, 1, 2}: add (alpha, p_i)
     to the S row; build the (3n-3) x 3n piece matrix M.
  3. Check BDI-feasibility on AII lattice points with sum <= n + 1
     (this is more than enough by Day-70 Cor 5.1 cone reduction:
     ray-image feasibility at depth = max ray sum implies global
     feasibility; the deepest ray is the triple-coupling ray of
     sum 3 (odd n) or 4 (even n), and we use n+1 >= max ray sum).
  4. Verify the three p_i columns are exactly e_{B_i} + alpha e_S.
  5. Verify pi_alpha and pi_beta differ ONLY on the p_i column.
  6. Pass iff all three pieces feasible & columns correct &
     distinct.

ACCEPTANCE:
  PASS: D-pi (3-clique form) extends to n = 6 and n = 7.
  FAIL: rigorous falsification -- one of the alpha pieces is
        non-feasible somewhere, or columns don't match.

The Day-71 verifier (verify_3clique.py) already produced these
results; this script is a fresh re-run at n = 6, 7 with clean
output structure for inclusion in the Day-75 PROVE rescue.

OUTPUT: results.json, REPORT.md, stdout table.
"""

from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
from general_axis import (
    aii_struct, bdi_vars, piece_matrix, verify_piece, enumerate_aii_lattice,
)
from general_pieces import base_piece


HERE = Path(__file__).resolve().parent


def aii_prefix_names(struct):
    aii_v = struct["vars"]
    return [aii_v[i] for i in struct["prefix_idx"]]


def build_pi_alpha(n, i, alpha):
    """Build pi_alpha^{(i)} = base piece with (alpha, p_i) added to S row.

    The base piece routes p_i -> B_i (i.e., the p_i column is e_{B_i}).
    Adding (alpha, p_i) to S gives p_i column e_{B_i} + alpha * e_S.
    """
    assert alpha in (0, 1, 2)
    struct = aii_struct(n)
    P = aii_prefix_names(struct)
    spec = copy.deepcopy(base_piece(n))
    if alpha != 0:
        spec.setdefault("S", []).append((alpha, P[i - 1]))
    return spec


def col_of(M, struct, aii_var):
    return M[:, struct["vars"].index(aii_var)]


def label_col(col, n):
    names = bdi_vars(n)
    terms = []
    for j, v in enumerate(col):
        if v == 0:
            continue
        if v == 1:
            terms.append(names[j])
        else:
            terms.append(f"{v}*{names[j]}")
    return " + ".join(terms) if terms else "0"


def verify_for_n(n, report_rows):
    """Verify D-pi 3-clique at level n. Returns (n_pass, n_fail, details)."""
    struct = aii_struct(n)
    P = aii_prefix_names(struct)
    bdi_names = bdi_vars(n)
    aii_pts = enumerate_aii_lattice(struct, n + 1)

    interior = list(range(2, n - 1))  # i in {2, ..., n-2}

    n_pass = 0
    n_fail = 0
    details = {"n": n, "n_aii_pts": len(aii_pts), "interior": interior,
               "by_i": {}}

    for i in interior:
        mats = {}
        feas_results = {}
        col_strs = {}
        per_alpha = {}

        for alpha in (0, 1, 2):
            spec = build_pi_alpha(n, i, alpha)
            M = piece_matrix(spec, struct)
            bad = verify_piece(M, struct, aii_pts)
            n_bad = len(bad)
            mats[alpha] = M
            feas_results[alpha] = n_bad
            col = col_of(M, struct, P[i - 1])
            col_strs[alpha] = label_col(col, n)

            # Column should equal e_{B_i} + alpha * e_S exactly.
            expected = np.zeros(len(bdi_names), dtype=int)
            expected[bdi_names.index(f"B_{i}")] = 1
            expected[bdi_names.index("S")] = alpha
            col_ok = bool(np.array_equal(col, expected))

            # For alpha > 0: difference from canonical (alpha=0) must
            # live entirely in the p_i column.
            if alpha == 0:
                diff_ok = True
                diff_str = "(canonical)"
            else:
                D = M - mats[0]
                p_i_idx = struct["vars"].index(P[i - 1])
                support_cols = [c for c in range(D.shape[1])
                                if np.any(D[:, c] != 0)]
                diff_ok = (support_cols == [p_i_idx])
                diff_str = "YES" if diff_ok else f"NO (cols={support_cols})"

            piece_pass = (n_bad == 0) and col_ok and diff_ok
            n_pass += int(piece_pass)
            n_fail += int(not piece_pass)
            row = {
                "n": n, "i": i, "alpha": alpha,
                "n_aii_pts_tested": len(aii_pts),
                "n_infeasible_images": n_bad,
                "feasible": (n_bad == 0),
                "p_i_col_label": col_strs[alpha],
                "p_i_col_correct": col_ok,
                "diff_from_alpha0_only_on_p_i": diff_ok if alpha else None,
                "pass": piece_pass,
            }
            per_alpha[alpha] = row
            report_rows.append(row)

        # Distinctness of three p_i columns (a 3-clique requires three
        # distinct routings of p_i).
        col0 = col_of(mats[0], struct, P[i - 1])
        col1 = col_of(mats[1], struct, P[i - 1])
        col2 = col_of(mats[2], struct, P[i - 1])
        three_distinct = (not np.array_equal(col0, col1)
                          and not np.array_equal(col0, col2)
                          and not np.array_equal(col1, col2))
        details["by_i"][i] = {
            "three_pieces_feasible": all(
                per_alpha[a]["feasible"] for a in (0, 1, 2)),
            "three_columns_distinct": three_distinct,
            "p_i_col_labels": [col_strs[a] for a in (0, 1, 2)],
            "per_alpha": per_alpha,
        }
        if not three_distinct:
            n_fail += 1  # Distinctness failure (would never happen,
                          # but guard against any future change to
                          # build_pi_alpha).

    return n_pass, n_fail, details


def main():
    report_rows = []
    all_details = {}

    print("=" * 76)
    print("Day 75 CODE Task A -- D-pi 3-clique verification at n = 6, 7")
    print("=" * 76)

    overall_pass = True
    summary_per_n = {}

    for n in (6, 7):
        print(f"\n--- n = {n} ---")
        n_pass, n_fail, details = verify_for_n(n, report_rows)
        n_interior = len(details["interior"])
        n_pieces_expected = 3 * n_interior
        all_details[f"n={n}"] = details
        ok = (n_fail == 0)
        overall_pass = overall_pass and ok
        print(f"  interior i:           {details['interior']}")
        print(f"  AII lattice pts:      {details['n_aii_pts']}")
        print(f"  pieces tested:        {n_pieces_expected}  ({n_interior} i x 3 alpha)")
        print(f"  passing pieces:       {n_pass}")
        print(f"  failing pieces:       {n_fail}")
        print(f"  3-cliques verified:   {sum(1 for v in details['by_i'].values() if v['three_pieces_feasible'] and v['three_columns_distinct'])}/{n_interior}")
        print(f"  verdict:              {'PASS' if ok else 'FAIL'}")
        summary_per_n[f"n={n}"] = {
            "n_interior": n_interior,
            "n_pieces_tested": n_pieces_expected,
            "n_pass": n_pass,
            "n_fail": n_fail,
            "verdict": "PASS" if ok else "FAIL",
        }

    # Print full table.
    print("\n" + "=" * 76)
    print("Full table:")
    print("=" * 76)
    header = (f"{'n':>3} | {'i':>2} | {'alpha':>5} | {'feasible?':>9}"
              f" | {'pi^{p_i}':>14} | {'diff p_i only?':>14}")
    sep = "-" * len(header)
    print(header)
    print(sep)
    for row in report_rows:
        feas = "YES" if row["feasible"] else f"NO({row['n_infeasible_images']})"
        diff = "(canon.)" if row["alpha"] == 0 else (
            "YES" if row["diff_from_alpha0_only_on_p_i"] else "NO")
        print(f"{row['n']:>3} | {row['i']:>2} | {row['alpha']:>5} |"
              f" {feas:>9} | {row['p_i_col_label']:>14} | {diff:>14}")

    print(sep)
    verdict = "PASS" if overall_pass else "FAIL"
    print(f"\nOVERALL: {verdict}  "
          f"({'D-pi (3-clique form) extends to n=6 AND n=7.' if overall_pass else 'See failures above.'})")

    # Save results.
    out = {
        "task": "Day 75 CODE Task A -- D-pi verification at n = 6, 7",
        "statement": ("For each interior i in {2,...,n-2} and "
                       "alpha in {0,1,2}, the piece pi_alpha^{(i)} = base "
                       "+ (alpha, p_i) on the S row is BDI-feasible; the "
                       "three p_i columns are e_{B_i} + alpha * e_S and "
                       "are pairwise distinct."),
        "overall_verdict": verdict,
        "summary_per_n": summary_per_n,
        "rows": report_rows,
        "by_n_details": {k: {**v, "by_i": {
            str(i): vv for i, vv in v["by_i"].items()
        }} for k, v in all_details.items()},
    }
    with open(HERE / "results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {HERE/'results.json'}")


if __name__ == "__main__":
    main()
