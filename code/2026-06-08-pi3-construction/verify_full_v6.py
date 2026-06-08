"""
v6 — Day-58 PROVE: parity-aware candidates and bigger unions.

Diagnostic showed: many missed BDI lattice points have ODD S with m_23 = 0,
forcing parity from a single source (m_12346) that's pinned to 0.
Need π_3 with an AII variable contributing to S with coefficient 1 (odd contrib).

The level-1 prefix m_2 has coeff 1 in B_1 and 0 in T_1, so coeff 1 in S is
balanced by 2 in P_1.  This gives an "odd S engine" via m_2.

Similarly, odd M_2: M_2 = m_12356 + 2 m_23456 has parity = m_12356 parity,
so already odd-friendly via m_12356.
"""

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full import PROJECTIONS as P2
from verify_full_v3 import PROJECTIONS as P3
from verify_full_v4 import PROJECTIONS as P4
from verify_full_v5 import P5_EXTRA as P5

P6_EXTRA = {
    # P5a: m_2 single-coefficient in S (for odd-S coverage with m_23 = 0)
    "P5a_m2_in_S": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (1, "m_2")],
    },

    # P5b: combine — M_2 doubled via m_23456, S has m_2 single
    "P5b_combined": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (1, "m_2")],
    },

    # P5c: m_23456 single in S
    "P5c_m23456_single_S": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (1, "m_23456")],
    },

    # P5d: R_double_m2345 + m_2 single in S
    "P5d_Rdouble_plus_m2": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345"), (1, "m_23456")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_2345"), (1, "m_2")],
    },

    # P5e: M_2 via m_236 doubled (with m_236 in B_1)
    "P5e_M2_via_236": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_236")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_236")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_23456")],
        "T_2": [(1, "m_1235"), (1, "m_23456")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (1, "m_2")],
    },

    # P5f: m_236 single in S (S = ... + m_236)
    "P5f_m236_single_S": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456"), (1, "m_236")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (1, "m_236")],
    },
}

ALL_PI = {**P2, **P3, **P4, **P5, **P6_EXTRA}


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


def test_union(names, N, verbose=True):
    bdi_pts = enumerate_bdi_n3(N)
    total_image = set()
    bad_total = 0
    for name in names:
        img, bad, n_aii = get_image(name, N)
        if bad > 0:
            bad_total += bad
        total_image |= img
    cov = len(total_image & bdi_pts)
    if verbose:
        print(f"  cov {cov:4d}/{len(bdi_pts):4d} ({100*cov/len(bdi_pts):5.1f}%) "
              f"bad-total {bad_total}  : {names}")
    return cov, len(bdi_pts), total_image & bdi_pts, bdi_pts


def main():
    # First, run singletons of new candidates
    print("=== SINGLE CANDIDATES (new) ===")
    for N in [4, 5, 6]:
        print(f"--- N = {N} ---")
        for name in ["P5a_m2_in_S", "P5b_combined", "P5c_m23456_single_S",
                     "P5d_Rdouble_plus_m2", "P5e_M2_via_236",
                     "P5f_m236_single_S"]:
            test_union([name], N)

    print("\n\n=== UNIONS ===")
    candidate_unions = [
        ["R_double_m2345"],
        ["R_double_m2345", "P5b_combined"],
        ["R_double_m2345", "P4b_M2_S_dbl_23456"],
        ["R_double_m2345", "P4b_M2_S_dbl_23456", "P5b_combined"],
        ["R_double_m2345", "P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236"],
        ["R_double_m2345", "P4b_M2_S_dbl_23456", "P5b_combined", "P4i_M2_23456_S_236"],
        ["R_double_m2345", "P5d_Rdouble_plus_m2", "P4b_M2_S_dbl_23456"],
        ["R_double_m2345", "P5d_Rdouble_plus_m2", "P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236"],
        ["R_double_m2345", "P5d_Rdouble_plus_m2", "P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236", "P5b_combined"],
        ["R_double_m2345", "P5d_Rdouble_plus_m2", "P4b_M2_S_dbl_23456", "P4i_M2_23456_S_236", "P5b_combined", "P5e_M2_via_236", "P5f_m236_single_S"],
    ]
    for N in [4, 5, 6, 7]:
        print(f"\n--- N = {N} ---")
        for names in candidate_unions:
            test_union(names, N)

    # Missing under the biggest union
    print("\n\n=== Missing under biggest union at N=6 ===")
    big = ["R_double_m2345", "P5d_Rdouble_plus_m2", "P4b_M2_S_dbl_23456",
           "P4i_M2_23456_S_236", "P5b_combined", "P5e_M2_via_236",
           "P5f_m236_single_S"]
    cov, total, _, bdi = test_union(big, 6, verbose=False)
    img_union = set()
    for name in big:
        img, _, _ = get_image(name, 6)
        img_union |= img
    missing = bdi - img_union
    print(f"  Missing {len(missing)} of {total}:")
    for q in sorted(missing)[:50]:
        _, M_2, B_1, T_1, B_2, T_2, S = q
        P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
        print(f"   M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S}  P_1={P_1} P_2={P_2}")


if __name__ == "__main__":
    main()
