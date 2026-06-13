"""
Day 68 CODE Task 1 — n=5 piece registry.

Strategy: mirror the n=4 v3 base + variants + R-double family, but lifted
to n=5. The n=5 polytope is odd (no Cor-8 linking eq); structurally
analogous to n=3.

Base piece (the "obvious" routing):
  p_i -> B_i  for i=1..4 (prefix to B-engines, level i)
  p_5 -> free direction (default: balanced in (B_2, T_2))
  L_1 -> free direction (default: B_1)
  L_2 -> M_2  (Main_2 partner)
  L_3 -> M_3  (Main_3 partner)
  L_4 -> M_4  (Main_4 partner)
  L_5 -> S    (Main_5 partner)
  s_i -> (B_i, T_i) balanced for i=1..4
  s_5 -> ???  (the "Singleton" var, analog of m_1234 at n=3)
              At n=3 the analog had S coef 2 in one variant -> BINARY.

Variants:
  - p_5 routed through different (B,T) pairs and S
  - L_1 routed through different B-engines, M-cells, S
  - L_1 with high coefficient (analog of M_2 doubled at n=4)
  - s_5 routed with S coef 2 (binary partner)

R-double family at n=5: the n=3/n=4 R-double family doubles s_1 in (B_1, T_1),
adds L_1 to T_1, sends 2*s_i to S (and an alpha*p_1 contribution to S).
The natural n=5 generalisation:
  R-double_n5_alpha:
    B_1: P1 + 2*S1 + L1
    T_1: S1 + L1
    S:   L5 + 2*S1 + 2*S(?) + alpha*P1
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from n5_setup import (AII_VARS, BDI_VARS, N_VARS, N_BDI,
                       piece_matrix, verify_piece, enumerate_aii_lattice)

P1, P2, P3, P4, P5 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3], AII_VARS[4]
L1, L2, L3, L4, L5 = AII_VARS[5], AII_VARS[6], AII_VARS[7], AII_VARS[8], AII_VARS[9]
S1, S2, S3, S4, S5 = AII_VARS[10], AII_VARS[11], AII_VARS[12], AII_VARS[13], AII_VARS[14]

PIECES = {}

# ---------------------------------------------------------------------
# BASE piece
# ---------------------------------------------------------------------
PIECES["P5_base"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

# ---------------------------------------------------------------------
# Variants of P5 routing (free prefix direction)
# ---------------------------------------------------------------------
PIECES["P5_P5_in_BT1"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, P5)],
    "T_1": [(1, S1), (1, P5)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_in_BT3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, P5)],
    "T_3": [(1, S3), (1, P5)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_in_BT4"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4), (1, P5)],
    "T_4": [(1, S4), (1, P5)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_in_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5), (1, P5)],
}

PIECES["P5_P5_dbl_BT2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (2, P5)],
    "T_2": [(1, S2), (2, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_split_BT2_BT3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3), (1, P5)],
    "T_3": [(1, S3), (1, P5)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_in_M2"] = {
    "M_2": [(1, L2), (1, P5)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1), (1, P5)],  # need P_1 >= M_2
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_in_M3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3), (1, P5)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, P5)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_P5_in_M4"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4), (1, P5)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2)],
    "T_2": [(1, S2)],
    "B_3": [(1, P3), (1, S3), (1, P5)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4), (1, P5)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

# ---------------------------------------------------------------------
# Variants of L1 routing (free long direction)
# ---------------------------------------------------------------------
PIECES["P5_L1_in_B2"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5), (1, L1)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_in_B3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3), (1, L1)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_in_B4"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4), (1, L1)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_in_S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5), (1, L1)],
}

PIECES["P5_L1_M2only"] = {
    # L1 → M_2 (and still in B_1 for P_1 coverage)
    "M_2": [(1, L2), (1, L1)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_M3"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3), (1, L1)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5), (1, L1)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_M4"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4), (1, L1)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5), (1, L1)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3), (1, L1)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_M2dbl"] = {
    # L1 doubled at M_2; need B_1 high
    "M_2": [(1, L2), (2, L1)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (3, L1)],
    "T_1": [(1, S1), (1, L1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

PIECES["P5_L1_BT2"] = {
    # L1 in (B_2, T_2) balanced
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5), (1, L1)],
    "T_2": [(1, S2), (1, P5), (1, L1)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4)],
    "T_4": [(1, S4)],
    "S":   [(1, L5)],
}

# ---------------------------------------------------------------------
# Variants of s_5 (the "Singleton" var, analog of m_1234 at n=3)
# ---------------------------------------------------------------------
# At n=3, m_1234 = short[3] had a binary partner: in some pieces it sat
# in S with coef 2. The natural lift to n=5: s_5 → 2*S in some variants.
PIECES["P5_s5_2S"] = {
    "M_2": [(1, L2)],
    "M_3": [(1, L3)],
    "M_4": [(1, L4)],
    "B_1": [(1, P1), (1, S1), (1, L1)],
    "T_1": [(1, S1)],
    "B_2": [(1, P2), (1, S2), (1, P5)],
    "T_2": [(1, S2), (1, P5)],
    "B_3": [(1, P3), (1, S3)],
    "T_3": [(1, S3)],
    "B_4": [(1, P4), (1, S4), (1, S5)],
    "T_4": [(1, S4)],
    "S":   [(1, L5), (2, S5)],
}

# ---------------------------------------------------------------------
# R-double family at n=5 (alpha ∈ {0, 1, 2})
# ---------------------------------------------------------------------
def make_r_double_n5(alpha):
    """Lift of the n=4 R-double. Doubles S1 in B_1, adds L1 to T_1,
    sends s1 with coef 2 and s_{n-1}=s_3 with coef 2 to S, with
    alpha*P1 in S.

    Sanity: at n=4 R-double had B_1: P1 + 2*S1 + L1; T_1: S1 + L1;
                                S: L4 + 2*S3 + 2*S1 + alpha*P1.
    At n=5 the analog: lift level-3 (= last non-S level in n=4) to
    level-4 (= last non-S level in n=5). So S gets 2*S4 (not 2*S3) +
    2*S1, and S column gains the analog S coef extras.
    """
    return {
        "M_2": [(1, L2)],
        "M_3": [(1, L3)],
        "M_4": [(1, L4)],
        "B_1": [(1, P1), (2, S1), (1, L1)],
        "T_1": [(1, S1), (1, L1)],
        "B_2": [(1, P2), (1, S2), (1, P5)],
        "T_2": [(1, S2), (1, P5)],
        "B_3": [(1, P3), (1, S3)],
        "T_3": [(1, S3)],
        "B_4": [(1, P4), (1, S4)],
        "T_4": [(1, S4)],
        "S":   [(1, L5), (2, S4), (2, S1), (alpha, P1)],
    }


for alpha in (0, 1, 2):
    PIECES[f"Rdouble_alpha{alpha}"] = make_r_double_n5(alpha)


# Level-2 R-double-like family (s_2 doubled, 2*s_2 in S, beta*p1 in S).
# This is a parallel R-double mechanism at a different level.
def make_r_double_level2(beta):
    return {
        "M_2": [(1, L2)],
        "M_3": [(1, L3)],
        "M_4": [(1, L4)],
        "B_1": [(1, P1), (1, S1), (1, L1)],
        "T_1": [(1, S1)],
        "B_2": [(1, P2), (2, S2), (1, P5)],
        "T_2": [(1, S2), (1, P5)],
        "B_3": [(1, P3), (1, S3)],
        "T_3": [(1, S3)],
        "B_4": [(1, P4), (1, S4)],
        "T_4": [(1, S4)],
        "S":   [(1, L5), (2, S2), (beta, P1)],
    }


for beta in (0, 1, 2):
    PIECES[f"Rdouble_lv2_beta{beta}"] = make_r_double_level2(beta)


# Level-3 R-double-like family
def make_r_double_level3(gamma):
    return {
        "M_2": [(1, L2)],
        "M_3": [(1, L3)],
        "M_4": [(1, L4)],
        "B_1": [(1, P1), (1, S1), (1, L1)],
        "T_1": [(1, S1)],
        "B_2": [(1, P2), (1, S2), (1, P5)],
        "T_2": [(1, S2), (1, P5)],
        "B_3": [(1, P3), (2, S3)],
        "T_3": [(1, S3)],
        "B_4": [(1, P4), (1, S4)],
        "T_4": [(1, S4)],
        "S":   [(1, L5), (2, S3), (gamma, P1)],
    }


for gamma in (0, 1, 2):
    PIECES[f"Rdouble_lv3_gamma{gamma}"] = make_r_double_level3(gamma)


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
        print(f"  ✓ {name}")
    if infeasible:
        print(f"\nInfeasible (first failure):")
        for name, (M, bad) in infeasible.items():
            p, q, err = bad[0]
            labeled = {AII_VARS[i]: p[i] for i in range(N_VARS) if p[i] != 0}
            print(f"  ✗ {name}: p={labeled} → q={q}, err={err}")

    return feasible, pts


if __name__ == "__main__":
    main()
