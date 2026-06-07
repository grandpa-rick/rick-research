"""
v3: more refined candidates targeting near-100% coverage.
"""

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)


PROJECTIONS = {
    # Strawman §4: linear, M_2 = 0, S = m_12346 + 2 m_1234
    "S4_strawman": {
        "M_1": [], "M_2": [],
        "B_1": [(1, "m_2"), (1, "m_2345")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234")],
    },

    # R: M_2 = m_12356, doubled m_2345 in B_1, m_236 in (B_2, T_2), m_2345 doubled in S
    "R_double_m2345": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345"), (1, "m_23456")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234"), (2, "m_2345")],
    },

    # R': also double m_1235 in B_2, S
    "R_double_both": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345"), (1, "m_23456")],
        "B_2": [(1, "m_23"), (2, "m_1235"), (1, "m_236"), (2, "m_1234")],
        "T_2": [(1, "m_1235"), (1, "m_236"), (1, "m_1234")],
        "S":   [(1, "m_12346"), (2, "m_2345"), (2, "m_1235"), (2, "m_1234")],
    },

    # R'': add m_12356 contribution to S (so M_2 var has both M_2 and S roles)
    "R_M2_in_S": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345"), (1, "m_23456")],
        "B_2": [(1, "m_23"), (2, "m_1235"), (1, "m_236"), (2, "m_1234")],
        "T_2": [(1, "m_1235"), (1, "m_236"), (1, "m_1234")],
        "S":   [(1, "m_12356"), (1, "m_12346"),
                (2, "m_2345"), (2, "m_1235"), (2, "m_1234")],
    },

    # No M_2 = m_12356 entirely in S, m_236 mass for M_2.
    "M2_is_m236": {
        "M_1": [], "M_2": [(1, "m_236")],
        "B_1": [(1, "m_2"), (2, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345"), (1, "m_23456")],
        "B_2": [(1, "m_23"), (2, "m_1235"), (2, "m_1234")],
        "T_2": [(1, "m_1235"), (1, "m_1234")],
        "S":   [(1, "m_12356"), (1, "m_12346"),
                (2, "m_2345"), (2, "m_1235"), (2, "m_1234")],
    },
}


def run_check(name, spec, N):
    aii_pts = enumerate_aii_n3_full(N)
    bdi_pts = enumerate_bdi_n3(N)
    bad = 0
    image = set()
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, _ = bdi_feasible_n3(q)
        if not ok:
            bad += 1
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
    cov = len(image & bdi_pts)
    print(f"  {name:25s}: lands {len(aii_pts)-bad}/{len(aii_pts)} "
          f"({100*(len(aii_pts)-bad)/len(aii_pts):.1f}%), "
          f"cov {cov}/{len(bdi_pts)} ({100*cov/len(bdi_pts):.1f}%)")
    return cov, len(bdi_pts), bad, len(aii_pts)


def main():
    for N in [4, 5, 6, 7]:
        print(f"\n--- N = {N} ---")
        for name, spec in PROJECTIONS.items():
            run_check(name, spec, N)


if __name__ == "__main__":
    main()
