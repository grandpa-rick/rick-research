"""
Q3 (Clio, 2026-06-07): at n >= 4 EVEN, is the column m_{12...(2n-2)·2n}
of the AII polytope a FREE polytope variable, or DETERMINED by the
sp_{2n}-HW criterion (the linking equation)?

At n = 4, this column is m_{1234568} (= {1,2,3,4,5,6,8}, missing 7).
Per the Azenhas Cor 8 description in
`proofs/azenhas-bdi-bridge/enum_full.py`, the linking equation reads
  m_{1234568} = m_{234567} + m_{123567} + m_{123467}
and m_{1234568} appears in NO other inequality.

Two competing hypotheses about the polytope dimension at n=4:

(F) "free": linking equation is NOT imposed (or only effective on a
    measure-zero subset). Then m_{1234568} is genuinely free. The AII
    polytope has 12 free variables, dim = 12. Versus BDI dim = 9 →
    gap = 3 (matches Clio's "n-1" conjecture at n=4).

(D) "determined": linking equation IS imposed as an equality. Then
    m_{1234568} is determined by the three slacks. AII dim = 11 vs BDI
    dim = 9 → gap = 2 (a different reduction).

This script tests (F) vs (D) by:

(i) Computing the affine hull dim of the polytope, treating the
    linking equation literally (i.e. as written).
(ii) Computing the dim WITHOUT the linking equation, for contrast.
(iii) Reporting the BDI dim at n=4 for the gap comparison.
(iv) Optionally: empirical lattice-count growth at small N (slow).
"""

import numpy as np
import sys


# -------- AII at n=4: 12 variables, 1 linking equation + several inequalities

# Variable order:
#   0: m_2
#   1: m_23
#   2: m_236
#   3: m_2367
#   4: m_2345678     (red^-1(u_1) = red^-1(2))
#   5: m_1235678     (red^-1(u_2) = red^-1(3))
#   6: m_1234678     (red^-1(u_3) = red^-1(6))
#   7: m_1234567     (red^-1(u_4) = red^-1(7))
#   8: m_234567      (slack: red^-1(2)\{8})
#   9: m_123567      (slack: red^-1(3)\{8})
#  10: m_123467      (slack: red^-1(6)\{8})
#  11: m_1234568     (linking LHS)

NAMES = ["m_2", "m_23", "m_236", "m_2367",
         "m_2345678", "m_1235678", "m_1234678", "m_1234567",
         "m_234567", "m_123567", "m_123467", "m_1234568"]


def aii_constraints_n4(with_linking=True):
    """
    Return (A_ineq, b_ineq, A_eq, b_eq) where the polytope is
      {x ≥ 0 : A_ineq @ x ≤ b_ineq, A_eq @ x = b_eq}.
    Cor 8 inequalities at n=4:
      m_1235678 + m_123567 ≤ m_2                (M2_inequality)
      0 ≤ m_1234678 + m_123467 ≤ m_23           (two: lower trivial)
      0 ≤ m_1234567 ≤ m_236                     (upper bound)
    Linking eq:
      m_1234568 = m_234567 + m_123567 + m_123467
    All vars ≥ 0 (handled separately).
    """
    n = 12
    A_ineq = []
    b_ineq = []
    # m_1235678 + m_123567 - m_2 ≤ 0
    row = [0] * n
    row[5] = 1; row[9] = 1; row[0] = -1
    A_ineq.append(row); b_ineq.append(0)
    # m_1234678 + m_123467 - m_23 ≤ 0
    row = [0] * n
    row[6] = 1; row[10] = 1; row[1] = -1
    A_ineq.append(row); b_ineq.append(0)
    # m_1234567 - m_236 ≤ 0
    row = [0] * n
    row[7] = 1; row[2] = -1
    A_ineq.append(row); b_ineq.append(0)

    A_eq = []
    b_eq = []
    if with_linking:
        # m_1234568 - m_234567 - m_123567 - m_123467 = 0
        row = [0] * n
        row[11] = 1; row[8] = -1; row[9] = -1; row[10] = -1
        A_eq.append(row); b_eq.append(0)

    return (np.array(A_ineq, dtype=float),
            np.array(b_ineq, dtype=float),
            np.array(A_eq, dtype=float) if A_eq else np.zeros((0, n)),
            np.array(b_eq, dtype=float))


def affine_hull_dim(A_eq, n_vars, A_ineq, b_ineq):
    """
    Affine hull dim of polytope. Hull dim = n_vars - rank(equations),
    but inequalities that are ALWAYS tight (i.e. inequality forced to
    equality by the rest of the system) also reduce the affine hull dim.

    Compute via: find a point in the (relative) interior; check rank of
    the binding constraint matrix.

    For our use, just rank(A_eq) gives an upper bound; full-dim minus
    that is the polytope dim assuming no inequality is always tight.

    Here the inequalities are clearly not always tight (the variables
    have slack), so dim = n_vars - rank(A_eq).
    """
    if A_eq.shape[0] == 0:
        return n_vars
    r = np.linalg.matrix_rank(A_eq)
    return n_vars - r


def main():
    print("# Q3: is m_{1234568} a free polytope variable at AII n=4?")
    print()
    print("## Variable list (12 vars)")
    for i, name in enumerate(NAMES):
        print(f"  x[{i:2d}] = {name}")
    print()

    # Test (D): with linking equation as written
    A_ineq, b_ineq, A_eq, b_eq = aii_constraints_n4(with_linking=True)
    dim_with = affine_hull_dim(A_eq, len(NAMES), A_ineq, b_ineq)
    print(f"## With linking equation (Cor 8 as stated)")
    print(f"  Number of variables: {len(NAMES)}")
    print(f"  Number of equality constraints: {A_eq.shape[0]} (rank {np.linalg.matrix_rank(A_eq) if A_eq.shape[0] else 0})")
    print(f"  Inequality constraints: {A_ineq.shape[0]}")
    print(f"  Affine hull dim of polytope: {dim_with}")
    print()

    # Test (F): without linking equation
    A_ineq2, b_ineq2, A_eq2, b_eq2 = aii_constraints_n4(with_linking=False)
    dim_without = affine_hull_dim(A_eq2, len(NAMES), A_ineq2, b_ineq2)
    print(f"## Without linking equation (hypothetical)")
    print(f"  Affine hull dim of polytope: {dim_without}")
    print()

    # BDI at n=4
    print(f"## BDI polytope at n=4")
    print(f"  Variables: M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S (9 vars, M_1=0)")
    print(f"  Inequalities only (no equations between vars), so dim = 9.")
    print()

    print(f"## Dimension gap dim(AII) - dim(BDI)")
    print(f"  (D) With linking imposed:    {dim_with} - 9 = {dim_with - 9}")
    print(f"  (F) Without linking:         {dim_without} - 9 = {dim_without - 9}")
    print()

    print(f"## Clio's n-1 conjecture at n=4")
    print(f"  Conjecture: gap = n - 1 = 3.")
    print(f"  → Matches (F) (without linking).")
    print(f"  → Does NOT match (D) (with linking, gap = 2).")
    print()

    # Decisive part: is the linking equation imposed by the
    # SAME polytope that gives the right Ehrhart count?
    # I.e. is the linking equation a redundant statement, or does it
    # cut down the lattice count?
    # Cross-check: enumerate small N with and without linking; compare.

    print("## Empirical lattice count at small N (with vs without linking eq)")
    print()
    # 11-12 free vars enumeration is heavy; use very small N.
    counts_with = []
    counts_without = []
    for N in [0, 1, 2, 3]:
        c_with = enumerate_aii_n4(N, with_linking=True)
        c_without = enumerate_aii_n4(N, with_linking=False)
        counts_with.append(c_with)
        counts_without.append(c_without)
        ratio = c_without / c_with if c_with else None
        print(f"  N={N}: with_linking={c_with}, without_linking={c_without}, "
              f"ratio={ratio:.3f}" if c_with else f"  N={N}: ...")

    # If counts differ, linking is a real constraint that reduces lattice
    # count → (D). If they agree, linking is redundant → (F).
    diff_total = sum(b - a for a, b in zip(counts_with, counts_without))
    print()
    if diff_total > 0:
        print("Verdict: linking equation IS a genuine constraint (with-linking < without-linking).")
        print("         m_{1234568} is DETERMINED. Dim gap = 2 (not Clio's n-1 = 3).")
    else:
        print("Verdict: linking equation is REDUNDANT (counts match).")
        print("         m_{1234568} is FREE de facto. Dim gap = 3 (matches Clio's n-1).")


def enumerate_aii_n4(N, with_linking=True):
    """
    Enumerate AII n=4 lattice points with weight ≤ N (sum of all 12
    variables ≤ N). Direct nested loops.

    Constraints (Cor 8 split):
      m_1235678 + m_123567 ≤ m_2
      m_1234678 + m_123467 ≤ m_23
      m_1234567 ≤ m_236
      (m_1234568 = m_234567 + m_123567 + m_123467  if with_linking)
      all vars ≥ 0
    """
    count = 0
    # Outer loop order chosen to prune aggressively.
    for m_2 in range(N + 1):
        for m_23 in range(N + 1 - m_2):
            for m_236 in range(N + 1 - m_2 - m_23):
                for m_2367 in range(N + 1 - m_2 - m_23 - m_236):
                    s4 = m_2 + m_23 + m_236 + m_2367
                    for m_2345678 in range(N + 1 - s4):
                        s5 = s4 + m_2345678
                        # m_1235678 in [0, m_2], + m_123567 ≤ m_2
                        for m_1235678 in range(min(m_2, N - s5) + 1):
                            for m_123567 in range(min(m_2 - m_1235678, N - s5 - m_1235678) + 1):
                                s7 = s5 + m_1235678 + m_123567
                                for m_1234678 in range(min(m_23, N - s7) + 1):
                                    for m_123467 in range(min(m_23 - m_1234678, N - s7 - m_1234678) + 1):
                                        s9 = s7 + m_1234678 + m_123467
                                        for m_1234567 in range(min(m_236, N - s9) + 1):
                                            s10 = s9 + m_1234567
                                            # m_234567 free ≥ 0, weight ≤ remaining
                                            # m_1234568 free or determined
                                            rem = N - s10
                                            if with_linking:
                                                # m_1234568 = m_234567 + m_123567 + m_123467
                                                # Weight contrib = m_234567 + m_1234568 = m_234567 + (m_234567 + m_123567 + m_123467)
                                                #                = 2 m_234567 + m_123567 + m_123467
                                                fixed = m_123567 + m_123467
                                                # We need 2 m_234567 + fixed ≤ rem → m_234567 ≤ (rem - fixed)/2
                                                if rem - fixed < 0:
                                                    continue
                                                count += (rem - fixed) // 2 + 1
                                            else:
                                                # m_234567 ≥ 0 and m_1234568 ≥ 0 free, sum ≤ rem
                                                if rem < 0: continue
                                                count += (rem + 1) * (rem + 2) // 2
    return count


if __name__ == "__main__":
    main()
