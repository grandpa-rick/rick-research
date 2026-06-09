"""
Day 60 toric-quotient analysis.

For each of the 26 pieces of pi_3' (Day-58), extract the LINEAR MAP
AII (9-dim) -> BDI (6-dim, with M_1 = 0 forced).

Then test the toric-quotient hypothesis (Clio Day-58):

Q1.  Is there a T^{n-1} action on AII whose moment map = (T_1, ..., T_{n-1})?
Q2.  Does each piece's kernel contain a rank-(n-1) sublattice that
     acts as 'fiber shifts' of (T_1, T_2)?  Or do different pieces
     give different T^{n-1}-structures (= moment map weights vary)?
Q3.  COMMON kernel = directions in *every* piece's kernel.  If this is
     non-trivial, that's the truly intrinsic 'invariant directions'.

We work over Q (sympy) to get exact answers.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

import sympy as sp
from verify_full_v7 import ALL_PI

AII_VARS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
            "m_2345", "m_1235", "m_1234"]
BDI_VARS = ["M_2", "B_1", "T_1", "B_2", "T_2", "S"]  # M_1 = 0 implicit
CORE_VARS = ["M_2", "P_1", "P_2", "S"]  # core BDI coords


def piece_matrix(spec):
    """Return 6x9 matrix (rows = BDI vars, cols = AII vars) for a piece."""
    A = sp.zeros(6, 9)
    for bi, bdi_var in enumerate(BDI_VARS):
        for coef, av in spec.get(bdi_var, []):
            ai = AII_VARS.index(av)
            A[bi, ai] = coef
    return A


def core_matrix(spec):
    """Return 4x9 matrix for (M_2, P_1, P_2, S) where
       P_1 = 2(B_1 - T_1) and P_2 = P_1 + 2(B_2 - T_2)."""
    A = piece_matrix(spec)
    # rows: M_2 (idx 0), B_1 (1), T_1 (2), B_2 (3), T_2 (4), S (5)
    core = sp.zeros(4, 9)
    core[0, :] = A[0, :]  # M_2
    core[1, :] = 2*(A[1, :] - A[2, :])  # P_1
    core[2, :] = core[1, :] + 2*(A[3, :] - A[4, :])  # P_2
    core[3, :] = A[5, :]  # S
    return core


# Restrict to the 26 pieces from the minimal cover.
MIN_COVER_26 = [
    "R_double_m2345",
    "M2_is_m236",
    "P4o_M2_236_S_m2",
    "P5a_m2_in_S",
    "P7_M2_simple_S_m2_2x23456",
    "P7_21_m23456_M2_S",
    "P7_M2_simple_T_both_236_S_m2",
    "P7_Rdouble_m2_dbl_S",
    "P7_S_mixed_M2_dbl",
    "P7_M2_dbl_T2_via_236",
    "P7_T1_236_T2_23456",
    "P5d_Rdouble_plus_m2",
    "P7_S_mixed_m2_m23456",
    "P7_T1_236_S_mixed",
    "P7_T1_T2_both_236_S_2m2",
    "P7_M2_dbl_236_asym_B1",
    "P7_T12_via_236_S_m2",
    "P7_T21_via_236_S_m2",
    "P7_M2_dbl_T_both_236_S_m23456",
    "P7_T1_1_T2_2_S_simple",
    "P7_12_m2_M2_S",
    "P7_T1_T2_both_via_236",
    "P7_M2_dbl_both_S_dbl_both",  # = "P7_M2_dbl_both_S_mixed" analog
    "P7_M2_dbl_T2_via_236_combo",
    "P7_T1_1_T2_2_via_236",
    "P7_T1_2_T2_1_via_236",
]


def report():
    print("=" * 78)
    print("DAY 60 TORIC QUOTIENT ANALYSIS")
    print("=" * 78)

    # Filter to pieces that exist
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    missing = [name for name in MIN_COVER_26 if name not in ALL_PI]
    print(f"\nPieces analyzed: {len(pieces)}")
    if missing:
        print(f"Missing from ALL_PI: {missing}")

    # 1. Per-piece kernel dimension
    print("\n--- Per-piece full BDI projection kernel ---")
    kernels = []
    for name in pieces:
        A = piece_matrix(ALL_PI[name])
        ns = A.nullspace()
        kernels.append((name, ns))
        print(f"  {name}: rank={A.rank()}, ker_dim={len(ns)}")

    # 2. Check piece P7_M2_dbl_both_S_dbl_both kernel basis
    sample = "P7_M2_dbl_both_S_mixed"
    if sample in ALL_PI:
        print(f"\n--- Sample kernel for {sample} ---")
        A = piece_matrix(ALL_PI[sample])
        print(f"  Matrix shape {A.shape}, rank {A.rank()}")
        ns = A.nullspace()
        print(f"  Kernel dim = {len(ns)}")
        for i, v in enumerate(ns):
            d = {AII_VARS[j]: int(v[j]) for j in range(9) if v[j] != 0}
            print(f"  ker[{i}] = {d}")

    # 3. Common kernel: intersection over all pieces
    print("\n--- Common kernel (intersection over all 26 pieces) ---")
    # The intersection of nullspaces is the nullspace of the stacked matrix.
    big = sp.Matrix.vstack(*[piece_matrix(ALL_PI[name]) for name in pieces])
    print(f"  Stacked matrix shape: {big.shape}, rank: {big.rank()}")
    common_kernel = big.nullspace()
    print(f"  Common kernel dim: {len(common_kernel)}")
    for i, v in enumerate(common_kernel):
        d = {AII_VARS[j]: int(v[j]) for j in range(9) if v[j] != 0}
        print(f"    common_ker[{i}] = {d}")

    # 4. Per-piece core (M_2, P_1, P_2, S) matrices: are they the same across pieces?
    print("\n--- Per-piece core BDI projection (M_2, P_1, P_2, S) ---")
    core_mats = {}
    for name in pieces:
        cm = core_matrix(ALL_PI[name])
        core_mats[name] = cm
    # Show first 3
    for i, name in enumerate(pieces[:5]):
        cm = core_mats[name]
        print(f"  {name}:")
        for r, label in enumerate(CORE_VARS):
            row = cm[r, :]
            terms = []
            for j in range(9):
                c = int(row[j])
                if c != 0:
                    sgn = "+" if c > 0 else "-"
                    val = abs(c)
                    if val == 1:
                        terms.append(f"{sgn}{AII_VARS[j]}")
                    else:
                        terms.append(f"{sgn}{val}*{AII_VARS[j]}")
            print(f"    {label} = {' '.join(terms)}")

    # 5. Common core kernel: directions invariant under ALL core projections
    print("\n--- Common core kernel (over all pieces) ---")
    big_core = sp.Matrix.vstack(*[core_mats[name] for name in pieces])
    print(f"  Stacked core matrix shape: {big_core.shape}, rank: {big_core.rank()}")
    common_core_kernel = big_core.nullspace()
    print(f"  Common core kernel dim: {len(common_core_kernel)}")
    for i, v in enumerate(common_core_kernel):
        d = {AII_VARS[j]: int(v[j]) for j in range(9) if v[j] != 0}
        print(f"    common_core_ker[{i}] = {d}")

    # 6. Pairwise core consistency: do any pieces have the SAME core matrix?
    print("\n--- Pairwise core matrix equality classes ---")
    seen = {}
    for name in pieces:
        key = tuple(tuple(int(c) for c in row) for row in core_mats[name].tolist())
        seen.setdefault(key, []).append(name)
    print(f"  Distinct core matrices: {len(seen)} (out of {len(pieces)} pieces)")
    for j, (k, names) in enumerate(sorted(seen.items())):
        print(f"    class {j}: {len(names)} pieces: {names}")

    # 7. Test the moment-map identity directly on AII coords for one piece
    print("\n--- Moment-map identity P_2 = P_1 + 2(B_2 - T_2) check ---")
    sample = "P7_M2_dbl_both_S_mixed"
    if sample in ALL_PI:
        A = piece_matrix(ALL_PI[sample])
        P_1 = 2*(A[1, :] - A[2, :])
        P_2 = 2*(A[1, :] - A[2, :]) + 2*(A[3, :] - A[4, :])
        # Check P_2 - P_1 - 2(B_2 - T_2) = 0
        residual = P_2 - P_1 - 2*(A[3, :] - A[4, :])
        print(f"  {sample}: residual = {residual.tolist()}")
        print(f"  Trivially zero by definition of P_2.")

    # 8. The T^{n-1} action: identify natural T_1, T_2 'fiber' coords on AII
    # Hypothesis: T_1 -> m_2345, T_2 -> m_1235 (per most pieces).
    print("\n--- T_1 and T_2 as linear functions of AII vars across pieces ---")
    t1_set = set()
    t2_set = set()
    for name in pieces:
        spec = ALL_PI[name]
        t1 = tuple(sorted(tuple(spec.get("T_1", []))))
        t2 = tuple(sorted(tuple(spec.get("T_2", []))))
        t1_set.add(t1)
        t2_set.add(t2)
    print(f"  Distinct T_1 expressions: {len(t1_set)}")
    for t in sorted(t1_set):
        print(f"    T_1 = {t}")
    print(f"  Distinct T_2 expressions: {len(t2_set)}")
    for t in sorted(t2_set):
        print(f"    T_2 = {t}")


if __name__ == "__main__":
    report()
