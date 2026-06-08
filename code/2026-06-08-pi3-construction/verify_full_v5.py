"""
v5: UNION of multiple linear pi_3 maps.

A piecewise-linear pi_3' is just a function whose image is a union of
linear-piece images.  For surjectivity, we don't need a single linear pi_3;
we need (image1 ∪ image2 ∪ ...) ⊇ BDI lattice points.

Each piece must land in BDI cone (since the piece's image at any AII point
must be in BDI for the map to be well-defined).

This script tests UNIONS of candidates from v3 and v4.
"""

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full import PROJECTIONS as P2
from verify_full_v3 import PROJECTIONS as P3
from verify_full_v4 import PROJECTIONS as P4

# Define a few additional candidates for v5
P5_EXTRA = {
    # P4i analog: m_23456 for M_2 (doubled), m_236 for S (doubled, in B_1)
    "P4i_M2_23456_S_236": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456"), (1, "m_236")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_236")],
    },

    # P4o: m_236 for M_2 (doubled, in B_1), m_2 for S (already in B_1)
    "P4o_M2_236_S_m2": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_236")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_236")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_23456")],
        "T_2": [(1, "m_1235"), (1, "m_23456")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_2")],
    },

    # P4p: P4b but m_236 absorbed into B_2/T_2 to help with high T_2 cases
    "P4p_236_in_B2T2": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_23456")],
    },

    # P4q: similar but m_2345 doubled in S too
    "P4q_double_all": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_2345"), (2, "m_23456")],
    },
}

ALL_PI = {**P2, **P3, **P4, **P5_EXTRA}


def get_image(name, N):
    spec = ALL_PI[name]
    aii_pts = enumerate_aii_n3_full(N)
    image = set()
    bad = 0
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, _ = bdi_feasible_n3(q)
        if not ok:
            bad += 1
            continue
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
    return image, bad, len(aii_pts)


def test_union(names, N):
    bdi_pts = enumerate_bdi_n3(N)
    total_image = set()
    for name in names:
        img, bad, n_aii = get_image(name, N)
        if bad > 0:
            print(f"  WARNING: {name} has {bad}/{n_aii} land-in-cone fails")
        total_image |= img
    cov = len(total_image & bdi_pts)
    print(f"  UNION{names}: cov {cov}/{len(bdi_pts)} ({100*cov/len(bdi_pts):.1f}%)")
    return cov, len(bdi_pts)


def diagnostic_missing(names, N):
    bdi_pts = enumerate_bdi_n3(N)
    total_image = set()
    for name in names:
        img, _, _ = get_image(name, N)
        total_image |= img
    missing = bdi_pts - total_image
    return missing


def main():
    candidate_unions = [
        ["section_4_aug_M2"],
        ["R_double_m2345"],
        ["P4a_M2_dbl_23456"],
        ["P4b_M2_S_dbl_23456"],
        ["P4i_M2_23456_S_236"],
        ["P4o_M2_236_S_m2"],
        ["P4p_236_in_B2T2"],
        ["P4q_double_all"],
        # Unions:
        ["P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236"],
        ["P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236", "R_double_m2345"],
        ["P4b_M2_S_dbl_23456", "P4p_236_in_B2T2"],
        ["P4p_236_in_B2T2", "P4i_M2_23456_S_236"],
        ["P4q_double_all", "P4i_M2_23456_S_236"],
        ["P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236", "P4o_M2_236_S_m2"],
    ]
    for N in [4, 5, 6, 7]:
        print(f"\n--- N = {N} ---")
        for names in candidate_unions:
            test_union(names, N)

    print("\n\n--- Missing under best union at N=5 ---")
    miss = diagnostic_missing(
        ["P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236", "P4o_M2_236_S_m2"], 5)
    for q in sorted(miss)[:30]:
        _, M_2, B_1, T_1, B_2, T_2, S = q
        P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
        print(f"   M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S}  P_1={P_1} P_2={P_2}")


if __name__ == "__main__":
    main()
