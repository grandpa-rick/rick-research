"""
v2: explore candidates for surjective pi_3' beyond the §4 strawman.

We test:
- §4 strawman (baseline, lands in cone, ~17-39% coverage).
- Candidate L: doubling slacks at both levels.
- Candidate O: m_23 enters B_2 with coeff 2, T_2 with coeff 1.
- Variants where M_2 = m_12356 (to free up an axis).
"""

import csv
from pathlib import Path
from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)


PROJECTIONS = {
    "section_4_strawman": {
        "M_1": [], "M_2": [],
        "B_1": [(1, "m_2"), (1, "m_2345")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234")],
    },

    "section_4_with_M2": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_2345")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234")],
    },

    # Candidate L: slack doubling at both levels.
    "L_doubling": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_23456"), (2, "m_2345")],
        "T_1": [(1, "m_23456"), (1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_236"), (2, "m_1235"), (2, "m_1234")],
        "T_2": [(1, "m_236"), (1, "m_1235"), (1, "m_1234")],
        "S":   [(1, "m_12346"), (2, "m_2345"), (2, "m_1235"), (2, "m_1234")],
    },

    # Candidate O: m_23 in B_2 with coeff 2, T_2 with coeff 1.
    "O_m23_doubled": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_23456"), (1, "m_2345")],
        "T_1": [(1, "m_23456")],
        "B_2": [(2, "m_23"), (1, "m_236"), (1, "m_1235")],
        "T_2": [(1, "m_23"), (1, "m_236"), (-1, "m_1234")],
        "S":   [(1, "m_12346"), (2, "m_2345"), (2, "m_1235"), (2, "m_1234")],
    },

    # Variation: only doubling m_2345, m_1234 in S (level-1 and -3 slacks).
    "O_v2": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_23456"), (1, "m_2345")],
        "T_1": [(1, "m_23456")],
        "B_2": [(2, "m_23"), (1, "m_236"), (1, "m_1235")],
        "T_2": [(1, "m_23"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_2345"), (2, "m_1234")],
    },

    # Try Σ-based doubling: Σ := m_12346 - m_1235 - m_2345 in [0, m_23].
    "Sigma_doubling": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_23456"), (1, "m_2345"), (1, "m_1235")],
        "T_1": [(1, "m_23456")],
        "B_2": [(2, "m_23"), (1, "m_236"), (-1, "m_2345"), (-1, "m_1235")],
        "T_2": [(1, "m_23"), (1, "m_236"), (-1, "m_2345"), (-1, "m_1235"), (-1, "m_1234")],
        "S":   [(3, "m_12346"), (-2, "m_2345"), (-2, "m_1235"), (2, "m_1234")],
    },
}


def run_check(name, spec, N, verbose=False):
    aii_pts = enumerate_aii_n3_full(N)
    n_aii = len(aii_pts)
    bad = []
    image = set()
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, reason = bdi_feasible_n3(q)
        if not ok:
            bad.append((p, q, reason))
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))

    n_bad = len(bad)
    bdi_pts = enumerate_bdi_n3(N)
    cov = len(image & bdi_pts)
    print(f"  {name:25s}: AII={n_aii}, lands {n_aii-n_bad}/{n_aii} "
          f"({100*(n_aii-n_bad)/n_aii:.1f}%), cov={cov}/{len(bdi_pts)} "
          f"({100*cov/len(bdi_pts):.1f}%)")
    if verbose and bad:
        for p, q, reason in bad[:3]:
            print(f"     bad p={p}, q={q}, reason={reason}")
    return n_aii, n_bad, len(bdi_pts), cov


def main():
    for N in [4, 5, 6]:
        print(f"\n--- N = {N} ---")
        for name, spec in PROJECTIONS.items():
            run_check(name, spec, N)


if __name__ == "__main__":
    main()
