"""
Find BDI lattice points NOT covered by a given candidate.
List specific tuples to understand structure of the gap.
(Day-58 PROVE diagnostic script.)
"""

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full import PROJECTIONS as P2
from verify_full_v3 import PROJECTIONS as P3
from verify_full_v4 import PROJECTIONS as P4

ALL_PI = {**P2, **P3, **P4}


def find_uncovered(name, N):
    spec = ALL_PI[name]
    aii_pts = enumerate_aii_n3_full(N)
    bdi_pts = enumerate_bdi_n3(N)
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
    covered = image & bdi_pts
    missing = bdi_pts - image
    print(f"\n=== {name} at N={N} ===")
    print(f"  AII pts: {len(aii_pts)}, BDI pts: {len(bdi_pts)}, "
          f"bad: {bad}, cov: {len(covered)}, miss: {len(missing)}")
    # Group missing by features
    print(f"  Sample missing (sorted):")
    for q in sorted(missing)[:25]:
        # (M_1, M_2, B_1, T_1, B_2, T_2, S)
        _, M_2, B_1, T_1, B_2, T_2, S = q
        P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
        flags = []
        if M_2 > B_1 - T_1: flags.append(f"M2>{B_1-T_1}")
        if S > 2*(B_2 - T_2): flags.append(f"S>2m23")
        if T_2 > B_1 - T_1: flags.append(f"T2>B1-T1")
        flags = " ".join(flags)
        print(f"    (M2={M_2}, B1={B_1}, T1={T_1}, B2={B_2}, T2={T_2}, S={S}) "
              f"P_1={P_1} P_2={P_2}  {flags}")


def main():
    for name in ["section_4_aug_M2", "R_double_m2345", "P4a_M2_dbl_23456",
                "P4d_236_in_B2T2"]:
        find_uncovered(name, 4)
    print("\n\n--- N=5 detailed ---")
    find_uncovered("R_double_m2345", 5)
    find_uncovered("P4d_236_in_B2T2", 5)


if __name__ == "__main__":
    main()
