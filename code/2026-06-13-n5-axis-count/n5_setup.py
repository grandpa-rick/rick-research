"""
Day 68 CODE Task 1 — Setup for n=5 piece registry.

Goal: build the AII / BDI machinery at n=5 (odd) and provide BDI
feasibility checks for piece verification. This is the structural twin
of n3 (also odd, no Cor-8 linking eq) and the analog of the n4 setup.

AII at n=5 (15 vars, no linkLHS since n is odd):
  prefix[1..5], long[1..5], short[1..5]
Inequalities (Main_i, i=2..5):
  long[i] + short[i] <= prefix[i-1]
short[1] is free (no Main_i mentions it).

BDI at n=5 (12 vars, M_1 = 0 suppressed):
  M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S
Constraints:
  T_a <= B_a for a=1..4
  P_a = sum_{b<=a} 2*(B_b - T_b) >= 0
  M_a <= min(P_{a-1}, P_a) for a=2,3,4    [P_0 = 0]
  S <= P_4
"""

import sys
import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational')
from dim_gap_verify import aii_structure


N = 5
STRUCT = aii_structure(N)

AII_VARS = STRUCT["vars"]
PREFIX_IDX = STRUCT["prefix_idx"]   # [0, 1, 2, 3, 4]
LONG_IDX = STRUCT["long_idx"]       # [5, 6, 7, 8, 9]
SHORT_IDX = STRUCT["short_idx"]     # [10, 11, 12, 13, 14]
LINKLHS_IDX = STRUCT["linkLHS_idx"] # None (odd n)
N_VARS = STRUCT["n_vars"]           # 15

# BDI vars at n=5.
BDI_VARS = ["M_2", "M_3", "M_4", "B_1", "T_1", "B_2", "T_2", "B_3", "T_3", "B_4", "T_4", "S"]
M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S = range(12)
N_BDI = 12


def bdi_feasible_n5(q):
    """q is length-12: (M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S).
    Return (feasible, error)."""
    (M_2v, M_3v, M_4v,
     B_1v, T_1v, B_2v, T_2v, B_3v, T_3v, B_4v, T_4v, Sv) = q
    if any(v < 0 for v in q):
        return False, "non-neg"
    if T_1v > B_1v: return False, "T_1<=B_1"
    if T_2v > B_2v: return False, "T_2<=B_2"
    if T_3v > B_3v: return False, "T_3<=B_3"
    if T_4v > B_4v: return False, "T_4<=B_4"
    P_1 = 2 * (B_1v - T_1v)
    P_2 = P_1 + 2 * (B_2v - T_2v)
    P_3 = P_2 + 2 * (B_3v - T_3v)
    P_4 = P_3 + 2 * (B_4v - T_4v)
    if P_2 < 0: return False, f"P_2={P_2}<0"
    if P_3 < 0: return False, f"P_3={P_3}<0"
    if P_4 < 0: return False, f"P_4={P_4}<0"
    if M_2v > P_1: return False, f"M_2<=P_1: {M_2v}>{P_1}"
    if M_2v > P_2: return False, f"M_2<=P_2"
    if M_3v > P_2: return False, f"M_3<=P_2: {M_3v}>{P_2}"
    if M_3v > P_3: return False, f"M_3<=P_3"
    if M_4v > P_3: return False, f"M_4<=P_3: {M_4v}>{P_3}"
    if M_4v > P_4: return False, f"M_4<=P_4"
    if Sv > P_4: return False, f"S<=P_4: {Sv}>{P_4}"
    return True, ""


def aii_feasible_n5(p):
    """p: length-15 vector. Return (feasible, error)."""
    if any(v < 0 for v in p):
        return False, "non-neg"
    # Main_2..Main_5: long[i] + short[i] <= prefix[i-1]
    for i in range(2, N + 1):
        if p[LONG_IDX[i-1]] + p[SHORT_IDX[i-1]] > p[PREFIX_IDX[i-2]]:
            return False, f"Main_{i}"
    # No linking equation at odd n.
    return True, ""


def enumerate_aii_lattice(N_max):
    """Enumerate AII lattice points with sum <= N_max."""
    pts = []

    def gen(remaining, depth, current):
        if depth == N_VARS:
            ok, _ = aii_feasible_n5(current)
            if ok:
                pts.append(tuple(current))
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()

    gen(N_max, 0, [])
    return pts


def piece_matrix(spec):
    """spec: {bdi_var: [(coef, aii_var), ...]}. Return 12x15 matrix."""
    M = np.zeros((N_BDI, N_VARS), dtype=int)
    for bv, terms in spec.items():
        bi = BDI_VARS.index(bv)
        for (coef, av) in terms:
            ai = AII_VARS.index(av)
            M[bi, ai] += coef
    return M


def piece_apply(M, p):
    return tuple(int(np.dot(M[i], p)) for i in range(N_BDI))


def verify_piece(M, sample_pts):
    bad = []
    for p in sample_pts:
        q = piece_apply(M, p)
        ok, err = bdi_feasible_n5(q)
        if not ok:
            bad.append((p, q, err))
    return bad


def piece_columns(M):
    return [tuple(int(M[r, c]) for r in range(N_BDI)) for c in range(N_VARS)]


if __name__ == "__main__":
    print(f"AII vars (N={N}): {AII_VARS}")
    print(f"BDI vars (N={N}): {BDI_VARS}")
    print(f"# AII vars: {N_VARS}, # BDI vars: {N_BDI}")
    print(f"PREFIX_IDX = {PREFIX_IDX}")
    print(f"LONG_IDX   = {LONG_IDX}")
    print(f"SHORT_IDX  = {SHORT_IDX}")
    print(f"LINKLHS_IDX = {LINKLHS_IDX}")

    for N_max in [3, 4]:
        pts = enumerate_aii_lattice(N_max)
        print(f"\n# AII lattice pts at sum <= {N_max}: {len(pts)}")
