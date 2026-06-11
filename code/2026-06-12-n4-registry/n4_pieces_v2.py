"""
Day 64 CODE Task 1 — n=4 piece registry v2.

V1 finding: 'coef 2 on linkLHS' pattern (from n=3 m_1234 → S coef 2)
DOES NOT WORK at n=4. Reason: linkLHS = s1+s2+s3 spans 3 LEVELS;
the level-n RHS bound (Main_4: L4 <= p3) only covers L4, not s1+s2+s3.

NEW HYPOTHESIS for n=4 S source:
  S = 1 * L4 only (long[4] coef 1)
  No coef-2 boost; the linkLHS is BALANCED elsewhere.

Test:
  S only sourced from L4.
  linkLHS routed to balanced (B_a, T_a) for some a.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       piece_matrix, verify_piece, piece_columns,
                       enumerate_aii_lattice)

P1, P2, P3, P4 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3]
L1, L2, L3, L4 = AII_VARS[4], AII_VARS[5], AII_VARS[6], AII_VARS[7]
S1, S2, S3 = AII_VARS[8], AII_VARS[9], AII_VARS[10]
LAMBDA = AII_VARS[11]

PIECES = {}

# ---------------------------------------------------------------------
# Base piece: simplest natural routing
# ---------------------------------------------------------------------
# Engine roles:
#   p1 → B_1, p2 → B_2, p3 → B_3        (prefix to B-engines)
#   s1 → (B_1, T_1), s2 → (B_2, T_2), s3 → (B_3, T_3)  (shorts balanced)
#   L2 → M_2 (Main_2 partner)
#   L3 → M_3 (Main_3 partner)
#   L4 → S   (Main_4 partner)
#   L1 → free direction; default B_1
#   p4 → free; default (B_2, T_2) balanced
#   linkLHS → balanced (B_3, T_3) (no S contribution!)
PIECES["P4_base"] = {
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

# linkLHS → (B_1, T_1) balanced
PIECES["P4_Lambda_in_BT1"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, LAMBDA)],
    "T_1": [(1, S1), (1, LAMBDA)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4)],
}

# linkLHS → (B_2, T_2) balanced
PIECES["P4_Lambda_in_BT2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (1, LAMBDA)],
    "T_2": [(1, S2), (1, P4), (1, LAMBDA)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "S":   [(1, L4)],
}

# L1 → B_2 (free direction routed to level 2)
PIECES["P4_L1_B2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (1, L1)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L1 → B_3 (free direction routed to level 3)
PIECES["P4_L1_B3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (1, L1)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L1 → S (free direction)
PIECES["P4_L1_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4), (1, L1)],
}

# p4 → B_3 (instead of B_2)
PIECES["P4_P4_B3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (1, P4)],
    "T_3": [(1, S3), (1, LAMBDA), (1, P4)],
    "S":   [(1, L4)],
}

# p4 → (B_1, T_1) balanced
PIECES["P4_P4_BT1"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, P4)],
    "T_1": [(1, S1), (1, P4)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# p4 → S
PIECES["P4_P4_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4), (1, P4)],
}

# p1 → M_2 (toggle: M_2 sourced from P1 instead of L2)
# Then L2 → S
PIECES["P4_P1_in_M2"] = {
    "M_2": [(1, P1), (1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, S1), (1, L1)],  # P1 doesn't go to B_1 in this version
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L2 → S (binary route, L2 not in M_2)
PIECES["P4_L2_in_S"] = {
    "M_2": [],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4), (1, L2)],
}

# L3 → S (binary route, L3 not in M_3)
PIECES["P4_L3_in_S"] = {
    "M_2": [(1, L2)],
    "M_3": [],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4), (1, L3)],
}

# L1 doubled at M_2 + B_1
PIECES["P4_L1_M2dbl"] = {
    "M_2": [(1, L2), (2, L1)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (3, L1)],  # need B_1 - T_1 high
    "T_1": [(1, S1), (1, L1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L1 doubled at M_3 (analog of M_2 doubled but at level 3)
PIECES["P4_L1_M3dbl"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3), (2, L1)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (2, L1)],
    "T_3": [(1, S3), (1, LAMBDA), (1, L1)],
    "S":   [(1, L4)],
}

# p4 in (T_1) only (asymmetric — should fail unless balanced)
# Try p4 in T_1 with balancing
PIECES["P4_P4_T1_only"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1), (1, P4)],  # p4 in T_1 (unbalanced)
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# All long[4] options: try L4 → B_3 instead of S? No, L4 must contribute to S
# since long[4] is paired with p3 via Main_4. Let me also try L4 only at S.

# p3 → (B_3, T_3) balanced (different from B_3 only)
PIECES["P4_P3_balanced"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, P3), (1, S3), (1, LAMBDA)],  # P3 balanced in BT3
    "S":   [(1, L4)],
}


def main():
    pts = enumerate_aii_lattice(4)
    print(f"# AII points at N<=4: {len(pts)}")

    feasible = {}
    infeasible = {}
    for name, spec in PIECES.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, pts)
        if bad:
            infeasible[name] = (M, bad)
        else:
            feasible[name] = M

    print(f"\nFeasible: {len(feasible)}/{len(PIECES)}")
    print(f"Feasible piece names:")
    for name in feasible:
        print(f"  {name}")
    if infeasible:
        print(f"\nInfeasible piece names (first failure):")
        for name, (M, bad) in infeasible.items():
            p, q, err = bad[0]
            labeled = {AII_VARS[i]: p[i] for i in range(N_VARS) if p[i] != 0}
            print(f"  {name}: at p={labeled} got q={q}, err={err}")

    return feasible, pts


if __name__ == "__main__":
    main()
