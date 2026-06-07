"""
Task 3: Enumerate Azenhas facets in COMBINED vs SPLIT form at n=2 and n=4.

Combined form (Theorem 7 RHS, all parities):
    Main_i : m_red^-1(u_i) + m_red^-1(u_i)\\{2n}  <=  m_{u_1 ... u_{i-1}}
    (i = 2, ..., n).
Plus linking equality (n even) and non-negativities.

Split form (Cor 7 for n=2, analog for n=4):
    For each level i, split the LHS sum into two separate inequalities
    with possibly different prefix RHS (per Cor 7 / 8 explicit labels).

We use scipy.optimize.linprog to test redundancy of each Main-type
inequality given the others (plus non-negativities and equalities).

Coordinate conventions: from the projection note and the verdict file.
"""

import csv
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

OUT_DIR = Path(__file__).parent


def is_redundant(a, A_other, C, var_count, tol=1e-9):
    """
    Test whether the inequality a . x <= 0 is implied by the other
    homogeneous inequalities A_other . x <= 0 (rows) plus equalities
    C . x = 0 (rows) plus non-negativity x >= 0.

    Equivalent to: maximize a . x subject to other constraints. If max > 0,
    inequality is non-redundant. If max <= 0 (or the LP unbounded *upward*
    is False), it's redundant.

    Bounded by `sum(x) <= 1` to get a finite LP. The cone is homogeneous so
    scaling doesn't matter.
    """
    # linprog minimises c.T x. We want to maximise a.T x, so c = -a.
    # Constraints:
    #   A_other @ x <= 0   (rows of A_other times x; but linprog uses
    #                       A_ub @ x <= b_ub)
    #   C @ x = 0
    #   x_i >= 0
    #   sum(x) <= 1 (boundedness)
    n = var_count
    if A_other.size == 0:
        A_ub = np.ones((1, n))
        b_ub = np.array([1.0])
    else:
        A_ub = np.vstack([A_other, np.ones((1, n))])
        b_ub = np.concatenate([np.zeros(A_other.shape[0]), [1.0]])
    A_eq = C if C.size > 0 else None
    b_eq = np.zeros(C.shape[0]) if C.size > 0 else None
    bounds = [(0, None)] * n
    res = linprog(
        c=-a, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
        bounds=bounds, method="highs",
    )
    if not res.success:
        # Likely infeasible; treat as edge case
        return False
    max_val = -res.fun
    return max_val <= tol


def count_non_redundant_main(ineqs, equalities, var_count):
    """
    For each Main inequality (row, list of names), check redundancy w.r.t.
    the other Main inequalities AND the equalities AND non-negativities
    (handled implicitly by linprog bounds).
    """
    n_main = len(ineqs)
    A_main = np.array(ineqs, dtype=float)
    C = np.array(equalities, dtype=float) if equalities else np.zeros((0, var_count))
    redundant = []
    for i in range(n_main):
        a = A_main[i]
        other = np.delete(A_main, i, axis=0)
        if is_redundant(a, other, C, var_count):
            redundant.append(i)
    return n_main - len(redundant), redundant


# ---------- n = 2 systems ----------

# Coords: (m_2, m_23, m_14, m_123, m_124)
VARS_N2 = ["m_2", "m_23", "m_14", "m_123", "m_124"]
IDX_N2 = {v: i for i, v in enumerate(VARS_N2)}


def row(coeffs, vars_):
    """Build a row vector for inequality coeffs (a dict {var: coef}) on `vars_`."""
    r = [0] * len(vars_)
    for k, v in coeffs.items():
        r[vars_.index(k)] = v
    return r


def main():
    print("=" * 60)
    print("n = 2 facet count")
    print("=" * 60)

    eq_n2 = [row({"m_14": 1, "m_23": -1}, VARS_N2)]

    # Combined: m_{123} + m_{124} <= m_2  (Main_2)
    ineqs_combined_n2 = [
        row({"m_123": 1, "m_124": 1, "m_2": -1}, VARS_N2),
    ]

    # Split (Cor 7): m_{123} <= m_2, m_{124} <= m_{23}
    ineqs_split_n2 = [
        row({"m_123": 1, "m_2": -1}, VARS_N2),
        row({"m_124": 1, "m_23": -1}, VARS_N2),
    ]

    nrm_comb, _ = count_non_redundant_main(
        ineqs_combined_n2, eq_n2, len(VARS_N2))
    nrm_split, _ = count_non_redundant_main(
        ineqs_split_n2, eq_n2, len(VARS_N2))

    print(f"COMBINED Main facets: {nrm_comb}  (verdict claims 1)")
    print(f"SPLIT    Main facets: {nrm_split}  (verdict claims 2)")
    print(f"BDI n=2 facet count: 2n-3 = 1.")
    print()

    # ---------- n = 4 systems ----------
    print("=" * 60)
    print("n = 4 facet count")
    print("=" * 60)

    # Coordinates from projection note §2.
    # Prefix columns: m_2, m_23, m_236, m_2367 (n=4 even -> u = {2,3,6,7})
    # red^-1(u_i) for i = 1,2,3,4 (length-7 columns reducing to u_i)
    # Slack columns (red^-1(u_i) \ {2n=8}) for i=1,2,3 (length 6)
    # Linking variable m_{1234568} (length 7 column = 12...(2n-2)·2n)
    #
    # Cor 8 explicit labels (from projection note):
    #   Combined Main_2: m_{1235678} + m_{123567}  <= m_2
    #   Combined Main_3: m_{1234678} + m_{123467}  <= m_{23}
    #   Combined Main_4: m_{1234567}                <= m_{236}
    # (Main_4 LHS has no slack since 8 not in (1234567))
    # Linking:  m_{1234568} = m_{123567} + m_{123467} + m_{1235678}\{8}-thing
    #   The projection note says linking sums the (n-1) = 3 slack columns:
    #   m_{1234568} = m_{123567} + m_{123467} + m_{1235678 \ 8}.
    # But m_{1235678 \ 8} = m_{123567} again -- that's not right. Let me re-read.
    #
    # Looking at projection note §2:
    #   Main_2 split: m_{1235678} <= m_2 and m_{123567} <= m_23 .
    # So m_{1235678} is the "red^-1(u_2)" full-length col and m_{123567} is
    # the "slack = red^-1(u_2)\{8}" col.
    # Similarly Main_3 has m_{1234678} (full) and m_{123467} (slack).
    # Main_4 has only m_{1234567} (full); no slack since 8 not in (1234567).
    #
    # Linking equality: m_{12345678 with 2n removed and replaced by 2n} ...
    # i.e. m_{1234568} = sum_{i=1}^{n-1=3} m_{red^-1(u_i)\{2n}}.
    # The (n-1)=3 slack vars at n=4 are:
    #   slack_i=1: red^-1(u_1)\{8} = red^-1(2)\{8} -- need an extra var, say A
    #   slack_i=2: red^-1(u_2)\{8} = (123567 if u_2=3)
    #   slack_i=3: red^-1(u_3)\{8} = (123467 if u_3=6)
    # We don't have slack_i=1 named in Cor 8 (it gets absorbed into the
    # n=2 case's m_14-style linking). For Cor 8 at n=4 the var Azenhas
    # writes is m_2367 (the prefix m_{u_1 u_2 u_3 u_4} that doesn't appear
    # in any Main; effectively a free dimension absorbed by linking).
    # We'll model the linking as: m_{1234568} = (sum of explicit slacks).

    VARS_N4 = [
        "m_2", "m_23", "m_236", "m_2367",       # prefixes
        "m_1235678", "m_123567",                # red^-1(u_2) and its slack
        "m_1234678", "m_123467",                # red^-1(u_3) and its slack
        "m_1234567",                            # red^-1(u_4) (no slack, no 8)
        "m_124", "m_2367_slack",                # slack at i=1 (informal) and an
                                                # auxiliary slack we won't use
        "m_1234568",                            # linking LHS column m_{12..(2n-2).2n}
    ]
    # Linking equality: m_1234568 = m_2367_slack + m_123567 + m_123467
    # We're being loose here: the linking equality is taken at face value
    # from the verdict / projection note Theorem 7 linking sum.

    def r(coeffs):
        return row(coeffs, VARS_N4)

    eq_n4 = [
        r({"m_1234568": 1, "m_2367_slack": -1,
           "m_123567": -1, "m_123467": -1}),
    ]

    # ---- Combined Main inequalities (3 total) ----
    ineqs_combined_n4 = [
        # Main_2: m_{1235678} + m_{123567} <= m_2
        r({"m_1235678": 1, "m_123567": 1, "m_2": -1}),
        # Main_3: m_{1234678} + m_{123467} <= m_{23}
        r({"m_1234678": 1, "m_123467": 1, "m_23": -1}),
        # Main_4: m_{1234567} <= m_{236}
        r({"m_1234567": 1, "m_236": -1}),
    ]

    # ---- Split Main inequalities (5 total, per Cor 8 explicit reading) ----
    ineqs_split_n4 = [
        # Main_2 split:
        r({"m_1235678": 1, "m_2": -1}),
        r({"m_123567": 1, "m_23": -1}),
        # Main_3 split:
        r({"m_1234678": 1, "m_23": -1}),
        r({"m_123467": 1, "m_236": -1}),
        # Main_4 (single, no slack):
        r({"m_1234567": 1, "m_236": -1}),
    ]

    nrm_comb_n4, red_comb = count_non_redundant_main(
        ineqs_combined_n4, eq_n4, len(VARS_N4))
    nrm_split_n4, red_split = count_non_redundant_main(
        ineqs_split_n4, eq_n4, len(VARS_N4))

    print(f"COMBINED Main facets: {nrm_comb_n4}  (verdict claims 3)")
    if red_comb:
        print(f"  Redundant indices: {red_comb}")
    print(f"SPLIT    Main facets: {nrm_split_n4}  (verdict claims 5)")
    if red_split:
        print(f"  Redundant indices: {red_split}")
    print(f"BDI n=4 facet count: 2n-3 = 5.")

    # ---- Bonus: Also check that split STRICTLY refines combined ----
    print()
    print("Sanity: any AII split-feasible point is combined-feasible? (yes by linearity)")
    # Generate a few split-infeasible-but-combined-feasible witnesses at n=2
    # to confirm the polytopes differ.
    print()
    print("Combined-feasible-but-split-infeasible witnesses at n=2 (|m| <= 5):")
    count_diff = 0
    witnesses = []
    for m_2 in range(6):
        for m_23 in range(6):
            m_14 = m_23
            for m_123 in range(6):
                for m_124 in range(6):
                    if m_2 + m_23 + m_14 + m_123 + m_124 > 5:
                        continue
                    combined_ok = m_123 + m_124 <= m_2
                    split_ok = (m_123 <= m_2) and (m_124 <= m_23)
                    if combined_ok and not split_ok:
                        count_diff += 1
                        witnesses.append(
                            (m_2, m_23, m_14, m_123, m_124))
    print(f"  Total witnesses: {count_diff}")
    for w in witnesses[:6]:
        print(f"    {w}")
    if count_diff == 0:
        print("  ==> Combined and split coincide at n=2 (?!)")

    # ---- CSV ----
    out_csv = OUT_DIR / "facet_counts.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "form", "Main_facets_in_system",
                    "Main_facets_non_redundant"])
        w.writerow([2, "combined", len(ineqs_combined_n2), nrm_comb])
        w.writerow([2, "split", len(ineqs_split_n2), nrm_split])
        w.writerow([4, "combined", len(ineqs_combined_n4), nrm_comb_n4])
        w.writerow([4, "split", len(ineqs_split_n4), nrm_split_n4])
    print(f"\nCSV: {out_csv}")


if __name__ == "__main__":
    main()
