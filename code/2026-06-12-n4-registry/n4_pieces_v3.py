"""
Day 64 CODE Task 1 — n=4 piece registry v3.

Extend v2 with more piece variants to test robustness of the AXIS = 2 result.

Variations explored:
  - more L1 routings (different BDI homes for free direction)
  - more p4 routings (free prefix)
  - L1 doubled in various places (high-coefficient pieces)
  - p4 splits between levels
  - combinations
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from n4_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       piece_matrix, verify_piece, enumerate_aii_lattice)

P1, P2, P3, P4 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3]
L1, L2, L3, L4 = AII_VARS[4], AII_VARS[5], AII_VARS[6], AII_VARS[7]
S1, S2, S3 = AII_VARS[8], AII_VARS[9], AII_VARS[10]
LAMBDA = AII_VARS[11]

from n4_pieces_v2 import PIECES as PIECES_V2
PIECES = dict(PIECES_V2)  # copy

# More variants...

# L1 doubled at M_3 + B_3 (no T_3 contribution, no longer cancels)
# Requires careful B-T balance to satisfy P_3 ≥ M_3.
PIECES["P4_L1_M3dbl_b3dbl"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3), (2, L1)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (2, L1)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (2, L1)],
    "T_3": [(1, S3), (1, LAMBDA), (1, L1)],
    "S":   [(1, L4)],
}

# L1 doubled at M_2 + M_3 simultaneously
PIECES["P4_L1_M2M3dbl"] = {
    "M_2": [(1, L2), (2, L1)],
    "M_3": [(1, L3), (2, L1)],
    "B_1": [(1, P1), (1, S1), (3, L1)],
    "T_1": [(1, S1), (1, L1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (2, L1)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (2, L1)],
    "T_3": [(1, S3), (1, LAMBDA), (1, L1)],
    "S":   [(1, L4)],
}

# L1 in T_2 (not B_2) — but needs balancing. Try L1 in M_2 + T_2 doubled
# Actually L1 → (M_2 +1, T_2 +1) gives M_2 = 1 but P_2 contribution = -2. Fail.
# Skip.

# p4 → M_2 (test if free prefix can source M_2)
# Need p4 not to overflow P_1; but p4 is unbounded, so this might fail
PIECES["P4_P4_in_M2"] = {
    "M_2": [(1, L2), (1, P4)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, P4)],
    "T_1": [(1, S1)],  # don't put p4 in T_1 since M_2 needs P_1 high
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# p4 → M_3
PIECES["P4_P4_in_M3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3), (1, P4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (1, P4)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L1 → M_2 only (not in B_1)
PIECES["P4_L1_M2only"] = {
    "M_2": [(1, L2), (1, L1)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],   # L1 must still appear in B_1 for P_1 cover
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L1 in M_2 + M_3 simultaneously (with appropriate B coverage)
PIECES["P4_L1_M2M3"] = {
    "M_2": [(1, L2), (1, L1)],
    "M_3": [(1, L3), (1, L1)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (1, L1)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA), (1, L1)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# p4 doubled in (B_2 + T_2 = same coef on both)... try p4 with coef 2
PIECES["P4_P4_dbl_BT2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (2, P4)],
    "T_2": [(1, S2), (2, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# L1 high-coef multiple destinations
PIECES["P4_L1_M2dbl_p4_T2"] = {
    "M_2": [(1, L2), (2, L1)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (3, L1)],
    "T_1": [(1, S1), (1, L1)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# Test: L1 → T_2 ?
# Try L1 in (B_2, T_2) balanced (then B_2-T_2 = 0)
PIECES["P4_L1_BT2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P4), (1, L1)],
    "T_2": [(1, S2), (1, P4), (1, L1)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
    "S":   [(1, L4)],
}

# p4 in (B_1, T_1) and (B_2, T_2) split
PIECES["P4_P4_BT1_BT2_split"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, P4)],
    "T_1": [(1, S1), (1, P4)],
    "B_2": [(1, P2), (1, S2), (1, P4)],
    "T_2": [(1, S2), (1, P4)],
    "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
    "T_3": [(1, S3), (1, LAMBDA)],
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
    for name in feasible:
        print(f"  {name}")
    print(f"\nInfeasible:")
    for name, (M, bad) in infeasible.items():
        p, q, err = bad[0]
        labeled = {AII_VARS[i]: p[i] for i in range(N_VARS) if p[i] != 0}
        print(f"  {name}: p={labeled} q={q} err={err}")

    return feasible, pts


if __name__ == "__main__":
    main()
