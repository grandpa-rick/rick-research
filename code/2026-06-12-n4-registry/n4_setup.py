"""
Day 64 CODE Task 1 — Setup for n=4 piece registry.

Goal: identify the AII variables at n=4 and provide BDI feasibility checks.

Reference: Day-60 dim_gap_verify.aii_structure(4) gives:
  - 12 AII variables: prefix[1..4], long[1..4], short[1..3], linkLHS.
  - Inequalities (Main_i, i=2..n):
      Main_2: long[2] + short[2] <= prefix[1]
      Main_3: long[3] + short[3] <= prefix[2]
      Main_4 (even n, i=n): long[4] <= prefix[3]
  - Equation (Cor 8 linking, even n): linkLHS = short[1] + short[2] + short[3]

BDI at n=4: 9 vars (M_1=0 suppressed):
  M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S
Constraints:
  T_a <= B_a for a=1,2,3
  P_a = sum_{b<=a} 2*(B_b - T_b) >= 0
  M_a <= min(P_{a-1}, P_a) for a=2,3   [P_0 = 0]
  S <= P_3

Engine-role analogy with n=3:
  At n=3:
    prefix[1] = m_2 → AXIS (4 col)
    prefix[2] = m_23 → RIGID (1 col, always B_2)
    prefix[3] = m_236 → AXIS (10 col)
    long[1] = m_23456 → AXIS (9 col)  [the FREE direction]
    long[2] = m_12356 → BINARY (2 col, M_2 ± S)
    long[3] = m_12346 → RIGID (1 col, always S coef 1)
    short[1] = m_2345 → BINARY (2 col)
    short[2] = m_1235 → BINARY (2 col)
    short[3] = m_1234 → BINARY (2 col, S coef 2)

The Day-62 conjecture: at n=4, # AXIS = f(4) = 2. So ONE of
{prefix[1], prefix[n], long[1]} collapses to a non-AXIS role.
"""

import sys
import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational')
from dim_gap_verify import aii_structure


# AII at n=4 (12 vars).
N = 4
STRUCT = aii_structure(N)

AII_VARS = STRUCT["vars"]
# Order: prefix[1..4], long[1..4], short[1..3], linkLHS (indices 0..11)
PREFIX_IDX = STRUCT["prefix_idx"]  # [0,1,2,3]
LONG_IDX = STRUCT["long_idx"]      # [4,5,6,7]
SHORT_IDX = STRUCT["short_idx"]    # [8,9,10]
LINKLHS_IDX = STRUCT["linkLHS_idx"]  # 11
N_VARS = STRUCT["n_vars"]

# BDI vars at n=4.
BDI_VARS = ["M_2", "M_3", "B_1", "T_1", "B_2", "T_2", "B_3", "T_3", "S"]
M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S = range(9)
N_BDI = 9


def bdi_feasible_n4(q):
    """q is a length-9 vector (M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S).
    Return (feasible, error)."""
    M_2v, M_3v, B_1v, T_1v, B_2v, T_2v, B_3v, T_3v, Sv = q
    if any(v < 0 for v in q):
        return False, "non-neg"
    if T_1v > B_1v: return False, "T_1<=B_1"
    if T_2v > B_2v: return False, "T_2<=B_2"
    if T_3v > B_3v: return False, "T_3<=B_3"
    P_1 = 2 * (B_1v - T_1v)
    P_2 = P_1 + 2 * (B_2v - T_2v)
    P_3 = P_2 + 2 * (B_3v - T_3v)
    if P_2 < 0: return False, f"P_2={P_2}<0"
    if P_3 < 0: return False, f"P_3={P_3}<0"
    # M_2 <= min(P_1, P_2); M_3 <= min(P_2, P_3); S <= P_3
    if M_2v > P_1: return False, f"M_2<=P_1: {M_2v}>{P_1}"
    if M_2v > P_2: return False, f"M_2<=P_2"
    if M_3v > P_2: return False, f"M_3<=P_2: {M_3v}>{P_2}"
    if M_3v > P_3: return False, f"M_3<=P_3"
    if Sv > P_3: return False, f"S<=P_3: {Sv}>{P_3}"
    return True, ""


def aii_feasible_n4(p):
    """p: length-12 vector. Return (feasible, error)."""
    if any(v < 0 for v in p):
        return False, "non-neg"
    # Main_2: long[2] + short[2] <= prefix[1]
    if p[LONG_IDX[1]] + p[SHORT_IDX[1]] > p[PREFIX_IDX[0]]:
        return False, "Main_2"
    # Main_3: long[3] + short[3] <= prefix[2]
    if p[LONG_IDX[2]] + p[SHORT_IDX[2]] > p[PREFIX_IDX[1]]:
        return False, "Main_3"
    # Main_4 (even n): long[4] <= prefix[3]
    if p[LONG_IDX[3]] > p[PREFIX_IDX[2]]:
        return False, "Main_4"
    # Linking: linkLHS = short[1] + short[2] + short[3]
    if p[LINKLHS_IDX] != p[SHORT_IDX[0]] + p[SHORT_IDX[1]] + p[SHORT_IDX[2]]:
        return False, "linking"
    return True, ""


def enumerate_aii_lattice(N_max):
    """Enumerate AII lattice points with sum <= N_max."""
    pts = []

    def gen(remaining, depth, current):
        if depth == N_VARS:
            ok, _ = aii_feasible_n4(current)
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
    """spec is a dict {bdi_var: [(coef, aii_var), ...]}. Return 9x12 matrix."""
    M = np.zeros((N_BDI, N_VARS), dtype=int)
    for bv, terms in spec.items():
        bi = BDI_VARS.index(bv)
        for (coef, av) in terms:
            ai = AII_VARS.index(av)
            M[bi, ai] += coef
    return M


def piece_apply(M, p):
    """Apply piece M (9x12) to AII point p (length 12). Returns length-9 q."""
    return tuple(int(np.dot(M[i], p)) for i in range(N_BDI))


def verify_piece(M, sample_pts):
    """Check that piece M sends every AII point in sample_pts to BDI cone."""
    bad = []
    for p in sample_pts:
        q = piece_apply(M, p)
        ok, err = bdi_feasible_n4(q)
        if not ok:
            bad.append((p, q, err))
    return bad


def piece_columns(M):
    """Return list of 12 columns of M (each a 9-tuple)."""
    return [tuple(int(M[r, c]) for r in range(N_BDI)) for c in range(N_VARS)]


if __name__ == "__main__":
    print(f"AII vars (N={N}): {AII_VARS}")
    print(f"BDI vars (N={N}): {BDI_VARS}")
    print(f"# AII vars: {N_VARS}, # BDI vars: {N_BDI}")
    print(f"PREFIX_IDX = {PREFIX_IDX}")
    print(f"LONG_IDX   = {LONG_IDX}")
    print(f"SHORT_IDX  = {SHORT_IDX}")
    print(f"LINKLHS_IDX = {LINKLHS_IDX}")

    # Enumerate small AII lattice
    N_max = 4
    pts = enumerate_aii_lattice(N_max)
    print(f"\n# AII lattice pts at sum <= {N_max}: {len(pts)}")

    # First few pts
    for p in pts[:5]:
        labeled = {AII_VARS[i]: p[i] for i in range(N_VARS) if p[i] != 0}
        print(f"  {labeled}")
