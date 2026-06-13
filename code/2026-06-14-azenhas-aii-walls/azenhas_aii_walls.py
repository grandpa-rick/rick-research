#!/usr/bin/env python3
"""
Day 69 CODE Task 1 — Azenhas AII wall count verification at n=4,5,6.

Goal: verify Azenhas's heuristic prediction that the number of
independent walls of the AII (GL -> Sp) hive cone grows linearly
~2(n-1), and contrast with Rick's uniform 3-wall count on BDI side.

Strategy:
- Encode Azenhas's Theorem D (n odd) / Theorem E (n even) inequalities
  in the column-multiplicity coordinates from
  proofs/2026-06-12-azenhas-inequalities-read.md  (sourced from
  Azenhas arXiv:2603.16698v5 sec 3, eq. 107 at n=3 + general
  formulas in sec 3 / Theorem D, E).
- ALSO encode the simplified Main_i inequalities currently used in
  code/2026-06-10-dim-gap-n5n6-computational/dim_gap_verify.py
  (`aii_structure`).
- For both encodings, count IRREDUNDANT inequalities (= facets =
  walls) via LP-based redundancy elimination.
- Do the same for the BDI polytope (Rick's framework).
- Tabulate at n=3,4,5,6.

Strict definition: in a system {a_i x <= b_i} + {A_eq x = b_eq},
inequality i is FACET-DEFINING iff
    max{a_i x : a_j x <= b_j for j != i, A_eq x = b_eq, bounding}
is > b_i (strictly).

We use the cone form (b=0) with a bounding -1 <= x_k <= 1 box.
For the BDI cone Rick's polytope also has b=0 so the same LP works.

Output: console + JSON.

References:
- Azenhas 2603.16698v5, sec 3, Theorem D / E.
- proofs/2026-06-12-azenhas-inequalities-read.md
- code/2026-06-10-dim-gap-n5n6-computational/dim_gap_verify.py
"""

from __future__ import annotations
import json
import numpy as np
from pathlib import Path
from scipy.optimize import linprog


# =====================================================================
# Variable scheme & Azenhas inequalities (Theorem D / E)
# =====================================================================
#
# At level n, the variables are column multiplicities (Azenhas
# convention).  The proof note `proofs/2026-06-12-azenhas-inequalities-read.md`
# names them as:
#
#   prefix[k] := m_{u_1 ... u_k}      k = 1..n             (n vars)
#   long[i]   := m_{red^{-1}(u_i)}    i = 1..n             (n vars)
#   short[i]  := m_{red^{-1}(u_i) \ {2n}}  i = 1..n-1 (odd n)  (n-1 vars)
#                                          i = 1..n-1 (even n)  (n-1 vars)
#
# Plus at even n a "linkLHS" variable m_{1..(2n-2)·2n} (one extra),
# and at odd n a "short[n]" variable (the length-(2n-2) column from
# u_n=2n, equal to (1,2,3,...,2n-2)).
#
# Total: 3n variables either way.
#
# The u-sequence (n odd: ends in u_n = 2n; n even: ends in u_n = 2n-1):
#   u_k = 2k    if k is odd
#   u_k = 2k-1  if k is even
# (Source: proofs/2026-06-12-azenhas-inequalities-read.md sec 1c.)
#
# Theorem D (n odd) inequalities, AS USED IN proof note eq.107 at n=3:
#   (97) for i = 2..n-1:
#         long[i] + short[i] <= prefix[i-1]
#   (98) the sandwich at i = n:
#         0 <= long[n] - sum_{i=1}^{n-1} short[i] <= prefix[n-1]
#         (i.e. two inequalities, both involving long[n] and the short
#          vars from i=1..n-1)
#
# Theorem E (n even) inequalities, by structural analogy and the
# linking equality:
#   (97) for i = 2..n-1:
#         long[i] + short[i] <= prefix[i-1]
#   (98) sandwich at i = n:
#         0 <= long[n] - sum_{i=1}^{n-1} short[i] <= prefix[n-1]
#   Linking equation (Cor 8):
#         linkLHS = sum_{i=1}^{n-1} short[i]
#
# Positivity: all variables >= 0.
#
# NOTE: there are two slightly different read of Theorem D/E in the
# literature; the alternative ("aii_structure" in dim_gap_verify.py)
# encodes (97) for i = 2..n, plus a linking equation at even n.
# This drops the (98) lower bound.  Day 67 read used the eq.107 form.
# We will count walls in BOTH conventions and report.
# =====================================================================


def make_vars(n):
    """Return (var_names, prefix_idx, long_idx, short_idx, linkLHS_idx).

    Indexes are into a flat var list of length 3n.
    short has n-1 entries when n is even, n entries when n is odd
    (the extra one being short[n] = red^{-1}(u_n) \ {2n}).
    At even n there is one linkLHS variable.
    """
    vars_list = []
    prefix_idx = []
    for k in range(1, n + 1):
        vars_list.append(f"prefix[{k}]")
        prefix_idx.append(len(vars_list) - 1)
    long_idx = []
    for i in range(1, n + 1):
        vars_list.append(f"long[{i}]")
        long_idx.append(len(vars_list) - 1)
    short_idx = []
    if n % 2 == 0:
        for i in range(1, n):
            vars_list.append(f"short[{i}]")
            short_idx.append(len(vars_list) - 1)
        vars_list.append("linkLHS")
        linkLHS_idx = len(vars_list) - 1
    else:
        for i in range(1, n + 1):
            vars_list.append(f"short[{i}]")
            short_idx.append(len(vars_list) - 1)
        linkLHS_idx = None
    assert len(vars_list) == 3 * n, (n, len(vars_list))
    return vars_list, prefix_idx, long_idx, short_idx, linkLHS_idx


def azenhas_system_TheoremDE_strict(n):
    """
    Strict Azenhas Theorem D/E system, in the eq.107 reading:
      (97) for i = 2..n-1 : long[i] + short[i] <= prefix[i-1]
      (98) i = n sandwich : 0 <= long[n] - sum_{i=1..n-1} short[i] <= prefix[n-1]
      Plus positivity x_k >= 0 for all vars.
      Plus linking eq at even n: linkLHS = sum_{i=1..n-1} short[i].
    Returns (A_ub, b_ub, A_eq, b_eq, labels, n_vars) where labels names each
    inequality row.
    """
    vars_list, prefix_idx, long_idx, short_idx, linkLHS_idx = make_vars(n)
    n_vars = len(vars_list)
    A_ub_rows = []
    labels = []

    # (97) for i = 2..n-1
    for i in range(2, n):
        row = [0.0] * n_vars
        row[long_idx[i - 1]] = 1.0           # long[i]
        row[short_idx[i - 1]] = 1.0          # short[i]   (i indexes 1..n-1 here)
        row[prefix_idx[i - 2]] = -1.0        # -prefix[i-1]
        A_ub_rows.append(row)
        labels.append(f"(97) i={i}: long[{i}]+short[{i}]<=prefix[{i-1}]")

    # (98) sandwich at i = n
    # Lower bound: -long[n] + sum_{j=1..n-1} short[j] <= 0
    row_lo = [0.0] * n_vars
    row_lo[long_idx[n - 1]] = -1.0
    for j in range(1, n):
        row_lo[short_idx[j - 1]] = 1.0
    A_ub_rows.append(row_lo)
    labels.append(f"(98)L i={n}: sum_short[1..{n-1}] <= long[{n}]")

    # Upper bound: long[n] - sum_{j=1..n-1} short[j] <= prefix[n-1]
    row_up = [0.0] * n_vars
    row_up[long_idx[n - 1]] = 1.0
    for j in range(1, n):
        row_up[short_idx[j - 1]] = -1.0
    row_up[prefix_idx[n - 2]] = -1.0
    A_ub_rows.append(row_up)
    labels.append(f"(98)U i={n}: long[{n}]-sum_short[1..{n-1}]<=prefix[{n-1}]")

    # positivity: -x_k <= 0
    for k, name in enumerate(vars_list):
        row = [0.0] * n_vars
        row[k] = -1.0
        A_ub_rows.append(row)
        labels.append(f"pos {name} >= 0")

    A_ub = np.array(A_ub_rows, dtype=float)
    b_ub = np.zeros(A_ub.shape[0])

    # equations at even n
    A_eq_rows = []
    if n % 2 == 0:
        row = [0.0] * n_vars
        row[linkLHS_idx] = 1.0
        for j in range(1, n):
            row[short_idx[j - 1]] = -1.0
        A_eq_rows.append(row)
    A_eq = (np.array(A_eq_rows, dtype=float)
            if A_eq_rows else np.zeros((0, n_vars)))
    b_eq = np.zeros(A_eq.shape[0])

    return A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list


def azenhas_system_aii_structure(n):
    """
    The alternative encoding used by the existing
    `aii_structure` function in dim_gap_verify.py:
      (97) for i = 2..n : long[i] + short[i] <= prefix[i-1]
        (at even n: at i=n short[n] doesn't exist; row is just long[n] <= prefix[n-1])
      Plus positivity.
      Plus linking eq at even n.
    Returns same tuple as above.
    """
    vars_list, prefix_idx, long_idx, short_idx, linkLHS_idx = make_vars(n)
    n_vars = len(vars_list)
    A_ub_rows = []
    labels = []

    for i in range(2, n + 1):
        row = [0.0] * n_vars
        row[long_idx[i - 1]] = 1.0
        if n % 2 == 1 or i < n:
            row[short_idx[i - 1]] = 1.0
        row[prefix_idx[i - 2]] = -1.0
        A_ub_rows.append(row)
        if n % 2 == 1 or i < n:
            labels.append(f"Main_{i}: long[{i}]+short[{i}]<=prefix[{i-1}]")
        else:
            labels.append(f"Main_{i}: long[{i}]<=prefix[{i-1}]")

    for k, name in enumerate(vars_list):
        row = [0.0] * n_vars
        row[k] = -1.0
        A_ub_rows.append(row)
        labels.append(f"pos {name} >= 0")

    A_ub = np.array(A_ub_rows, dtype=float)
    b_ub = np.zeros(A_ub.shape[0])

    A_eq_rows = []
    if n % 2 == 0:
        row = [0.0] * n_vars
        row[linkLHS_idx] = 1.0
        for j in range(1, n):
            row[short_idx[j - 1]] = -1.0
        A_eq_rows.append(row)
    A_eq = (np.array(A_eq_rows, dtype=float)
            if A_eq_rows else np.zeros((0, n_vars)))
    b_eq = np.zeros(A_eq.shape[0])

    return A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list


# =====================================================================
# BDI polytope (Rick's framework)
# =====================================================================
def bdi_system(n):
    """
    BDI inequalities at level n (Rick).
    Vars: M_2..M_{n-1}, B_1..B_{n-1}, T_1..T_{n-1}, S    (3n-3 vars)
    Inequalities (M_1 = 0 forced):
       T_a >= 0, B_a >= 0,  T_a <= B_a            (a = 1..n-1)
       P_a := 2*sum_{b<=a}(B_b - T_b) >= 0        (a = 1..n-1)
       M_a >= 0, M_a <= P_{a-1}, M_a <= P_a       (a = 2..n-1)  (M_1=0 enforced; not a var)
       S >= 0, S <= P_{n-1}
    """
    names = []
    for a in range(2, n):
        names.append(f"M_{a}")
    M_idx = {a: i for a, i in zip(range(2, n), range(0, n - 2))}
    nB0 = n - 2
    for a in range(1, n):
        names.append(f"B_{a}")
    B_idx = {a: nB0 + a - 1 for a in range(1, n)}
    nT0 = nB0 + (n - 1)
    for a in range(1, n):
        names.append(f"T_{a}")
    T_idx = {a: nT0 + a - 1 for a in range(1, n)}
    S_idx = nT0 + (n - 1)
    names.append("S")
    n_vars = len(names)
    assert n_vars == 3 * n - 3, (n, n_vars)

    def make_zero():
        return [0.0] * n_vars

    A_ub_rows = []
    labels = []

    # T_a >= 0  ==>  -T_a <= 0
    for a in range(1, n):
        row = make_zero()
        row[T_idx[a]] = -1.0
        A_ub_rows.append(row)
        labels.append(f"T_{a} >= 0")
    # B_a >= 0
    for a in range(1, n):
        row = make_zero()
        row[B_idx[a]] = -1.0
        A_ub_rows.append(row)
        labels.append(f"B_{a} >= 0")
    # T_a <= B_a  ==>  T_a - B_a <= 0
    for a in range(1, n):
        row = make_zero()
        row[T_idx[a]] = 1.0
        row[B_idx[a]] = -1.0
        A_ub_rows.append(row)
        labels.append(f"T_{a} <= B_{a}")
    # P_a >= 0  ==>  -2*sum_{b<=a}(B_b - T_b) <= 0
    for a in range(1, n):
        row = make_zero()
        for b in range(1, a + 1):
            row[B_idx[b]] += -2.0
            row[T_idx[b]] += 2.0
        A_ub_rows.append(row)
        labels.append(f"P_{a} >= 0")
    # M_a >= 0  ==>  -M_a <= 0
    for a in range(2, n):
        row = make_zero()
        row[M_idx[a]] = -1.0
        A_ub_rows.append(row)
        labels.append(f"M_{a} >= 0")
    # M_a <= P_{a-1}, M_a <= P_a
    for a in range(2, n):
        # M_a - P_{a-1} <= 0 :  M_a - 2*sum_{b<=a-1}(B-T) <= 0
        row = make_zero()
        row[M_idx[a]] = 1.0
        for b in range(1, a):
            row[B_idx[b]] += -2.0
            row[T_idx[b]] += 2.0
        A_ub_rows.append(row)
        labels.append(f"M_{a} <= P_{a-1}")
        # M_a - P_a <= 0
        row = make_zero()
        row[M_idx[a]] = 1.0
        for b in range(1, a + 1):
            row[B_idx[b]] += -2.0
            row[T_idx[b]] += 2.0
        A_ub_rows.append(row)
        labels.append(f"M_{a} <= P_{a}")
    # S >= 0
    row = make_zero()
    row[S_idx] = -1.0
    A_ub_rows.append(row)
    labels.append("S >= 0")
    # S <= P_{n-1}
    row = make_zero()
    row[S_idx] = 1.0
    for b in range(1, n):
        row[B_idx[b]] += -2.0
        row[T_idx[b]] += 2.0
    A_ub_rows.append(row)
    labels.append(f"S <= P_{n-1}")

    A_ub = np.array(A_ub_rows, dtype=float)
    b_ub = np.zeros(A_ub.shape[0])
    A_eq = np.zeros((0, n_vars))
    b_eq = np.zeros(0)
    return A_ub, b_ub, A_eq, b_eq, labels, n_vars, names


# =====================================================================
# Facet (irredundant) count
# =====================================================================
def is_facet(A_ub, b_ub, A_eq, b_eq, i, tol=1e-7, box=1.0):
    """Test whether inequality i of A_ub x <= b_ub is facet-defining
    (irredundant) modulo the rest of the system + equations.

    Method: LP max a_i x   s.t.   a_j x <= b_j (j != i),  A_eq x = b_eq,
                                 -box <= x_k <= box  for each k.
    If max > b_i (with tol), facet-defining.  Else redundant.
    """
    M, n = A_ub.shape
    mask = np.ones(M, dtype=bool)
    mask[i] = False
    A_others = A_ub[mask]
    b_others = b_ub[mask]
    c = -A_ub[i]
    bounds = [(-box, box)] * n
    A_eq_arg = A_eq if A_eq.shape[0] else None
    b_eq_arg = b_eq if A_eq.shape[0] else None
    res = linprog(c, A_ub=A_others, b_ub=b_others,
                  A_eq=A_eq_arg, b_eq=b_eq_arg,
                  bounds=bounds, method='highs')
    if res.status != 0:
        return None, res.message
    max_val = -res.fun
    return (max_val > b_ub[i] + tol), max_val


def count_facets(A_ub, b_ub, A_eq, b_eq, labels, tol=1e-7, box=1.0):
    M = A_ub.shape[0]
    flags = []
    maxes = []
    for i in range(M):
        flag, mv = is_facet(A_ub, b_ub, A_eq, b_eq, i, tol=tol, box=box)
        flags.append(flag)
        maxes.append(mv)
    facet_labels = [lab for lab, f in zip(labels, flags) if f]
    redund_labels = [lab for lab, f in zip(labels, flags) if not f]
    return {
        "total_ineqs": M,
        "n_facets": int(sum(1 for f in flags if f)),
        "n_redundant": int(sum(1 for f in flags if f is False)),
        "facet_labels": facet_labels,
        "redundant_labels": redund_labels,
        "max_vals": [float(m) if m is not None else None for m in maxes],
    }


# =====================================================================
# Main runner
# =====================================================================
def run_for_n(n):
    print(f"\n{'='*72}\n  n = {n}\n{'='*72}")
    out = {"n": n}

    # AII (strict Azenhas Theorem D/E)
    A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = (
        azenhas_system_TheoremDE_strict(n)
    )
    print(f"\n  [AII strict (eq.107 reading)]"
          f"  n_vars={n_vars}, ineqs={A_ub.shape[0]}, eqs={A_eq.shape[0]}")
    res = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    print(f"    facets: {res['n_facets']}    redundant: {res['n_redundant']}")
    print(f"    facet labels:")
    for L in res["facet_labels"]:
        print(f"      [facet]  {L}")
    out["AII_strict"] = {**res, "n_vars": n_vars}

    # AII (existing aii_structure encoding)
    A_ub2, b_ub2, A_eq2, b_eq2, labels2, n_vars2, vars_list2 = (
        azenhas_system_aii_structure(n)
    )
    print(f"\n  [AII aii_structure (Day-60 simplified)]"
          f"  n_vars={n_vars2}, ineqs={A_ub2.shape[0]}, eqs={A_eq2.shape[0]}")
    res2 = count_facets(A_ub2, b_ub2, A_eq2, b_eq2, labels2)
    print(f"    facets: {res2['n_facets']}    redundant: {res2['n_redundant']}")
    print(f"    facet labels:")
    for L in res2["facet_labels"]:
        print(f"      [facet]  {L}")
    out["AII_aii_structure"] = {**res2, "n_vars": n_vars2}

    # BDI
    A_ub3, b_ub3, A_eq3, b_eq3, labels3, n_vars3, vars_list3 = bdi_system(n)
    print(f"\n  [BDI (Rick)]"
          f"  n_vars={n_vars3}, ineqs={A_ub3.shape[0]}, eqs={A_eq3.shape[0]}")
    res3 = count_facets(A_ub3, b_ub3, A_eq3, b_eq3, labels3)
    print(f"    facets: {res3['n_facets']}    redundant: {res3['n_redundant']}")
    print(f"    facet labels:")
    for L in res3["facet_labels"]:
        print(f"      [facet]  {L}")
    out["BDI"] = {**res3, "n_vars": n_vars3}

    return out


def main():
    print("=" * 72)
    print("Day 69 CODE Task 1 -- Azenhas AII wall count verification")
    print("=" * 72)

    results = {}
    for n in [3, 4, 5, 6, 7, 8]:
        results[n] = run_for_n(n)

    # Final table
    print("\n" + "=" * 72)
    print(" SUMMARY TABLE  (AII facets, BDI facets, Azenhas heuristic)")
    print("=" * 72)
    print(f" {'n':>2}  {'AII strict':>11}  {'AII aii_str':>12} "
          f"{'BDI walls':>10}  {'Azenhas 2(n-1)':>14}  parity")
    rows = []
    for n in [3, 4, 5, 6, 7, 8]:
        r = results[n]
        f1 = r["AII_strict"]["n_facets"]
        f2 = r["AII_aii_structure"]["n_facets"]
        f3 = r["BDI"]["n_facets"]
        pred = 2 * (n - 1)
        rows.append((n, f1, f2, f3, pred))
        print(f" {n:>2}  {f1:>11}  {f2:>12}  {f3:>10}  "
              f"{pred:>14}  {'odd ' if n % 2 else 'even'}")

    # Finite-difference check
    print("\n  Finite differences (period-2 finite diff for quasipoly):")
    for series_name, idx in [
        ("AII strict", 1), ("AII aii_str", 2),
        ("BDI", 3),  ("predict 2(n-1)", 4),
    ]:
        vals = [r[idx] for r in rows]
        d1 = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        d2_odd = [vals[i + 2] - vals[i]
                  for i in range(len(vals) - 2) if rows[i][0] % 2 == 1]
        d2_even = [vals[i + 2] - vals[i]
                   for i in range(len(vals) - 2) if rows[i][0] % 2 == 0]
        print(f"    {series_name:>16}: vals={vals}  d1={d1}  "
              f"d2_odd-step={d2_odd}  d2_even-step={d2_even}")

    out_dir = Path(__file__).parent
    with open(out_dir / "azenhas_aii_walls_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'azenhas_aii_walls_results.json'}")


if __name__ == "__main__":
    main()
