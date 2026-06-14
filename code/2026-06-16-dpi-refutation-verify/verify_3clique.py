"""
Day 70 PROVE — Conjecture D-pi refutation: 3-clique verification.

For each n in {5, 6, 7} and each interior i (1 < i < n-1), construct
three pieces pi_alpha (alpha in {0, 1, 2}) where pi_alpha is the base
piece MODIFIED so the p_i column equals e_{B_i} + alpha * e_S.

Check:
  (A) Each pi_alpha is BDI-feasible on AII lattice points with sum <= n+1.
  (B) pi_alpha and pi_beta differ ONLY on the p_i column.
  (C) The three p_i columns are distinct.

If all three checks pass for every (n, i), the 3-clique on the wall
{p_i = 0} refutes Conjecture D-pi.
"""

from __future__ import annotations
import sys
import copy
from pathlib import Path

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')

from general_axis import (
    aii_struct, bdi_vars, piece_matrix, verify_piece, enumerate_aii_lattice,
)
from general_pieces import base_piece


def _aii_names(struct):
    aii_v = struct["vars"]
    n = struct["n"]
    P = [aii_v[i] for i in struct["prefix_idx"]]
    return P


def build_pi_alpha(n, i, alpha):
    """Build pi_alpha = base piece with (alpha, p_i) added to S row.

    The base piece routes p_i -> B_i (i.e., the p_i column is e_{B_i}).
    Adding (alpha, p_i) to the S spec makes the p_i column e_{B_i} + alpha*e_S.
    """
    struct = aii_struct(n)
    P = _aii_names(struct)
    spec = copy.deepcopy(base_piece(n))
    if alpha != 0:
        spec.setdefault("S", []).append((alpha, P[i - 1]))
    return spec


def col_of(M, struct, aii_var):
    return M[:, struct["vars"].index(aii_var)]


def col_label(col, n):
    """Render a column as a sum of basis vectors."""
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


def verify_for_n(n, results_rows, summary):
    struct = aii_struct(n)
    P = _aii_names(struct)
    deep_pts = enumerate_aii_lattice(struct, n + 1)
    interior = list(range(2, n - 1))  # i in {2, ..., n-2}

    for i in interior:
        # Build the three pieces.
        mats = {}
        feas_results = {}
        col_strs = {}
        for alpha in (0, 1, 2):
            spec = build_pi_alpha(n, i, alpha)
            M = piece_matrix(spec, struct)
            bad = verify_piece(M, struct, deep_pts)
            mats[alpha] = M
            feas_results[alpha] = len(bad)
            col = col_of(M, struct, P[i - 1])
            col_strs[alpha] = col_label(col, n)

            # Verify col equals e_{B_i} + alpha*e_S
            names = bdi_vars(n)
            expected = np.zeros(len(names), dtype=int)
            expected[names.index(f"B_{i}")] = 1
            expected[names.index("S")] = alpha
            col_ok = bool(np.array_equal(col, expected))

            if alpha == 0:
                diff_str = "(canonical)"
            else:
                # Compare to canonical (alpha=0) matrix on all columns
                # except p_i.
                D = M - mats[0]
                p_i_idx = struct["vars"].index(P[i - 1])
                # Support of D should be entirely on column p_i_idx.
                support_cols = [c for c in range(D.shape[1])
                                if np.any(D[:, c] != 0)]
                only_pi = (support_cols == [p_i_idx])
                diff_str = "YES" if only_pi else f"NO (support cols={support_cols})"

            feas_str = "YES" if feas_results[alpha] == 0 else f"NO ({feas_results[alpha]})"
            ok_overall = (feas_results[alpha] == 0) and col_ok and (
                alpha == 0 or diff_str == "YES")
            if not ok_overall:
                summary["failures"].append((n, i, alpha, feas_str, col_strs[alpha], diff_str, col_ok))
            else:
                summary["passes"].append((n, i, alpha))
            results_rows.append((n, i, alpha, feas_str, col_strs[alpha], diff_str))

        # Additionally check distinctness of three p_i columns.
        col0 = col_of(mats[0], struct, P[i - 1])
        col1 = col_of(mats[1], struct, P[i - 1])
        col2 = col_of(mats[2], struct, P[i - 1])
        distinct = (not np.array_equal(col0, col1)
                    and not np.array_equal(col0, col2)
                    and not np.array_equal(col1, col2))
        if not distinct:
            summary["failures"].append((n, i, "distinct", "FAIL", "", "", False))


def main():
    out_dir = Path("/home/agent/projects/code/2026-06-16-dpi-refutation-verify")
    out_dir.mkdir(exist_ok=True)

    results_rows = []
    summary = {"passes": [], "failures": []}

    for n in (5, 6, 7):
        print(f"\n--- n = {n} ---")
        verify_for_n(n, results_rows, summary)

    # Print table.
    header = f"{'n':>3} | {'i':>3} | {'alpha':>5} | {'feasible?':>10} | {'pi^{p_i}':>14} | {'diff on p_i only?':>20}"
    sep = "-" * len(header)
    print()
    print(header)
    print(sep)
    for n, i, alpha, feas, col, diff in results_rows:
        print(f"{n:>3} | {i:>3} | {alpha:>5} | {feas:>10} | {col:>14} | {diff:>20}")

    # Summary.
    print()
    if not summary["failures"]:
        # Group passing (n, i) for which all three alpha passed.
        pass_set = set()
        ni_to_alphas = {}
        for n, i, alpha in summary["passes"]:
            ni_to_alphas.setdefault((n, i), set()).add(alpha)
        cliques = [f"(n={n}, i={i})" for (n, i), a in ni_to_alphas.items()
                   if a == {0, 1, 2}]
        msg = ("3-clique on {p_i = 0} verified for: "
               + ", ".join(cliques))
        print(msg)
        verdict = msg
    else:
        msg = "REFUTED at: " + "; ".join(
            f"n={f[0]}, i={f[1]}, alpha={f[2]}, feas={f[3]}, col={f[4]}, diff={f[5]}"
            for f in summary["failures"])
        print(msg)
        verdict = msg

    # Save results.txt
    with open(out_dir / "results.txt", "w") as f:
        f.write("Conjecture D-pi 3-clique refutation verification\n")
        f.write("=" * 70 + "\n\n")
        f.write(header + "\n")
        f.write(sep + "\n")
        for n, i, alpha, feas, col, diff in results_rows:
            f.write(f"{n:>3} | {i:>3} | {alpha:>5} | {feas:>10} | {col:>14} | {diff:>20}\n")
        f.write("\n")
        f.write(verdict + "\n")

    print(f"\nWrote {out_dir/'results.txt'}")


if __name__ == "__main__":
    main()
