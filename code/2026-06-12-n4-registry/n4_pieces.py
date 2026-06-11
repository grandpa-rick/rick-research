"""
Day 64 CODE Task 1 — n=4 piece registry construction.

Construct pieces at n=4 by direct analogy with the n=3 minimal cover.

Variable mnemonics:
  p1 = prefix[1] (analog of m_2)
  p2 = prefix[2] (analog of m_23)
  p3 = prefix[3] (analog of m_236 in the bounded role)
  p4 = prefix[4] (analog of m_236 in the free role — no Main_i bound)
  L1 = long[1]   (analog of m_23456, FREE direction)
  L2 = long[2]   (analog of m_12356, paired with p1 in Main_2)
  L3 = long[3]   (analog of m_12346, paired with p2 in Main_3 [but here it's
                                     long[3]+short[3]<=p2; at n=3 it was the S var])
  L4 = long[4]   (paired with p3 in Main_4 — even n, no short[4])
  s1 = short[1]  (analog of m_2345)
  s2 = short[2]  (analog of m_1235)
  s3 = short[3]  (analog of m_1234)
  Λ  = linkLHS   (equals s1+s2+s3 by linking equation)

The pieces below are constructed by:
  - Routing each prefix to B_i (natural choice)
  - long[2..3] to M_2, M_3 (paired with prefix in Main_i constraints)
  - long[4] to S (analog of long[3]→S at n=3)
  - long[1] to "free engine" (anywhere)
  - short[i] to (B_i, T_i) balanced (engine identity)
  - linkLHS to ??? (test multiple choices)
"""

import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import numpy as np

from n4_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       PREFIX_IDX, LONG_IDX, SHORT_IDX, LINKLHS_IDX,
                       piece_matrix, piece_apply, verify_piece, piece_columns,
                       enumerate_aii_lattice, aii_feasible_n4, bdi_feasible_n4)


# Short var name aliases for spec dicts
P1, P2, P3, P4 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3]
L1, L2, L3, L4 = AII_VARS[4], AII_VARS[5], AII_VARS[6], AII_VARS[7]
S1, S2, S3 = AII_VARS[8], AII_VARS[9], AII_VARS[10]
LAMBDA = AII_VARS[11]

# Define pieces by spec dict {BDI_var: [(coef, AII_var), ...]}
# A piece SPEC is feasible iff it sends every AII p into BDI cone.

PIECES = {}

# Base piece P4o_n4: direct n=3 P4o analog.
PIECES["P4o_n4"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],   # coef 2 on linkLHS (analog of m_1234)
}

# Variant A: L1 (free) goes to B_2 instead of B_1
PIECES["P4o_n4_L1_B2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (1, L1)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant B: L1 goes to B_3
PIECES["P4o_n4_L1_B3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, L1)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant C: L1 (free) goes to S
PIECES["P4o_n4_L1_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA), (1, L1)],
}

# Variant D: L1 doubled in M_3 (analog of n=3 "M_2 doubled by m_23456")
PIECES["P4o_n4_L1_M3dbl"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3), (2, L1)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (2, L1)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant E: P4 (free prefix) routed to B_1 instead of (B_2, T_2)
PIECES["P4o_n4_P4_B1"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, P4)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant F: P4 in (B_3, T_3) instead of (B_2, T_2)
PIECES["P4o_n4_P4_B3T3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, P4)],
    "T_3": [(1, S3), (1, P4)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant G: P4 in S
PIECES["P4o_n4_P4_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA), (1, P4)],
}

# Variant H: P1 doubled in B_1 (so prefix[1] takes two "slots")
# At n=3 there's a "Rdouble_m2_dbl" piece doubling m_2 in B_1.
PIECES["P4o_n4_P1_doubled_B1"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(2, P1), (1, S1), (1, L1)],
    "T_1": [(1, P1), (1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant I: L1 multiplied by 2 in B_1 (doubled engine on free direction)
PIECES["P4o_n4_L1_doubled_B1"] = {
    "M_2": [(1, L2), (2, L1)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (3, L1)],
    "T_1": [(1, S1), (1, L1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant J: linkLHS routed to (B_3, T_3) instead of S
# Test: linkLHS in T_3 (the "balanced" alternative)
PIECES["P4o_n4_Lambda_T_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# Variant K: P1 alternative — sends p1 to (B_1, M_2) split
# i.e., M_2 takes a "p1" piece (instead of just L2)
# This mimics the n=3 piece where m_12356 toggles between M_2 and S, etc.
PIECES["P4o_n4_M2_via_P1"] = {
    "M_2": [(1, L2), (1, P1)],
    "M_3": [(1, L3)],
    "B_1": [(1, S1), (1, L1)],     # P1 not in B_1 here
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA)],
}

# Variant L: long[2] sent to S instead of M_2 (binary L2 like at n=3)
PIECES["P4o_n4_L2_in_S"] = {
    "M_2": [],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4), (2, LAMBDA), (1, L2)],
}


def main():
    # Enumerate AII sample for feasibility verification.
    print("Enumerating AII lattice (N_max=4)...")
    pts = enumerate_aii_lattice(4)
    print(f"# AII points: {len(pts)}")

    print("\nFeasibility check across pieces:")
    feasible_pieces = {}
    for name, spec in PIECES.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, pts)
        if bad:
            print(f"  {name}: INFEASIBLE — {len(bad)} bad pts; first: p={bad[0][0]} q={bad[0][1]} err={bad[0][2]}")
        else:
            print(f"  {name}: feasible at N<=4")
            feasible_pieces[name] = M

    print(f"\n# feasible pieces: {len(feasible_pieces)}/{len(PIECES)}")
    return feasible_pieces, pts


if __name__ == "__main__":
    feasible, pts = main()
