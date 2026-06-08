"""
v4: doubling-via-m_23456 candidates.

Key insight (Day 58 deep work): the §4 strawman + R_double_m2345 hit a
factor-of-2 ceiling on (M_2, S) because every m_X that 'wants to double'
is in fact Main_i-bounded by m_{u_{i-1}}.  EXCEPT m_23456, which is
the level-1 Cor 6 column and is COMPLETELY FREE in AII (no Main_i
constraint).  So m_23456 is the right doubling-engine for M_2 and S.

Candidates here all use m_23456 as a doubling-engine into M_2 and S,
trying to close the M_2 <= P_1 and S <= P_2 gaps.
"""

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)


PROJECTIONS = {
    # P4a: just M_2 doubled via m_23456.
    "P4a_M2_dbl_23456": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234")],
    },

    # P4b: also S doubled via m_23456.
    "P4b_M2_S_dbl_23456": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_23456")],
    },

    # P4c: also S doubled via m_2345 too.
    "P4c_M2_S_dbl_both": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_23456"), (2, "m_2345")],
    },

    # P4d: also m_236 absorbed into B_2/T_2 to help when T_2 is big.
    "P4d_236_in_B2T2": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_23456"), (2, "m_2345")],
    },

    # P4e: m_236 doubled in M_2 too (so we have two free engines)
    # but careful: m_236 needs to land in cone.
    # m_236 is free, so M_2 += 2 m_236 could violate M_2 <= P_1 unless we
    # also add m_236 to B_1.  Try it:
    "P4e_236_in_M2_B1": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456"), (2, "m_236")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456"), (1, "m_236")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_23456"), (2, "m_2345")],
    },

    # P4f: combine - m_236 in both B_1 (for M_2 cap) and ALSO in B_2/T_2 chain.
    # No that double-counts.  Just try P4d as the best.

    # P4g: kitchen sink — use every free var doubled into S.
    "P4g_kitchen_sink": {
        "M_1": [], "M_2": [(1, "m_12356"), (2, "m_23456"), (2, "m_236")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456"), (1, "m_236")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_23456"),
                (2, "m_2345"), (2, "m_1235")],
    },
}


def run_check(name, spec, N):
    aii_pts = enumerate_aii_n3_full(N)
    bdi_pts = enumerate_bdi_n3(N)
    bad = 0
    image = set()
    bad_reasons = {}
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, reason = bdi_feasible_n3(q)
        if not ok:
            bad += 1
            bad_reasons[reason] = bad_reasons.get(reason, 0) + 1
            continue
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
    cov = len(image & bdi_pts)
    n_aii = len(aii_pts)
    print(f"  {name:25s}: lands {n_aii-bad}/{n_aii} "
          f"({100*(n_aii-bad)/n_aii:5.1f}%), "
          f"cov {cov:4d}/{len(bdi_pts):4d} "
          f"({100*cov/len(bdi_pts):5.1f}%)")
    if bad and bad_reasons:
        # Show top reason
        top = max(bad_reasons.items(), key=lambda x: x[1])
        print(f"      top fail: {top[0]} ({top[1]}x)")
    return cov, len(bdi_pts), bad, n_aii


def main():
    for N in [4, 5, 6, 7, 8]:
        print(f"\n--- N = {N} ---")
        for name, spec in PROJECTIONS.items():
            run_check(name, spec, N)


if __name__ == "__main__":
    main()
