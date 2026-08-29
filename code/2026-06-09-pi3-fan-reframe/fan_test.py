"""
Day 61 — Fan structure test.

Q1: Are the image cones C_i = pi^(i)(P^AII_5) all equal to P^BDI_3?
    If YES: as REAL cones, all pieces give the same image; the "26-piece"
    distinction must be lattice-level. Then there's no fan in the
    real/rational world.

Q2: If C_i differ, do they form a fan? I.e., for any pair (i,j), is
    C_i cap C_j a common face?

Q3: Even if C_i are all equal, the LATTICE images pi^(i)(Z^9 cap P^AII_5)
    might differ — they're sub-monoids of Z^6 cap P^BDI_3. Compute their
    saturated sub-monoids and check if THEY form a fan-like structure.

This script computes P^BDI_3 rays and tests Q1 first.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
import numpy as np
from itertools import combinations
from verify_full_v7 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS, BDI_VARS


def bdi_rays():
    """Enumerate extreme rays of P^BDI_3.

    Constraints (6 vars: M_2, B_1, T_1, B_2, T_2, S):
      M_2 >= 0
      B_1 >= 0
      T_1 >= 0
      B_2 >= 0
      T_2 >= 0
      S >= 0
      B_1 - T_1 >= 0
      B_2 - T_2 >= 0
      P_1 - M_2 = 2(B_1 - T_1) - M_2 >= 0
      P_2 - S = 2(B_1 - T_1) + 2(B_2 - T_2) - S >= 0
    """
    A_rows = []
    # 6 nonneg
    for i in range(6):
        v = [0]*6; v[i] = 1
        A_rows.append(v)
    # B_1 - T_1 >= 0
    v = [0]*6; v[1] = 1; v[2] = -1
    A_rows.append(v)
    # B_2 - T_2 >= 0
    v = [0]*6; v[3] = 1; v[4] = -1
    A_rows.append(v)
    # P_1 - M_2 >= 0
    v = [0]*6; v[1] = 2; v[2] = -2; v[0] = -1
    A_rows.append(v)
    # P_2 - S >= 0
    v = [0]*6; v[1] = 2; v[2] = -2; v[3] = 2; v[4] = -2; v[5] = -1
    A_rows.append(v)

    n = len(A_rows)  # 10
    rays_set = set()
    for subset in combinations(range(n), 5):  # 6-dim cone, 5 tight per ray
        M = sp.Matrix([A_rows[i] for i in subset])
        ns = M.nullspace()
        if len(ns) != 1:
            continue
        v = ns[0]
        for sign in [1, -1]:
            vv = [sp.Rational(sign * v[j]) for j in range(6)]
            if all(sum(A_rows[i][j] * vv[j] for j in range(6)) >= 0 for i in range(n)):
                from fractions import Fraction
                fracs = [Fraction(str(x)) for x in vv]
                # Normalize
                lcm_denom = 1
                from math import gcd
                from functools import reduce
                for f in fracs:
                    lcm_denom = lcm_denom * f.denominator // gcd(lcm_denom, f.denominator)
                int_vals = [int(f * lcm_denom) for f in fracs]
                g = reduce(gcd, [abs(x) for x in int_vals if x != 0], 0)
                if g > 0:
                    int_vals = [x // g for x in int_vals]
                if any(x != 0 for x in int_vals):
                    rays_set.add(tuple(int_vals))
                break
    return [list(r) for r in rays_set]


def aii_rays():
    """9 extreme rays of P^AII_5."""
    return [
        [0, 1, 0, 0, 0, 0, 0, 0, 1],  # m_23 + m_1234
        [1, 0, 0, 0, 0, 0, 0, 0, 0],  # m_2
        [1, 0, 0, 0, 1, 0, 0, 0, 0],  # m_2 + m_12356
        [0, 1, 0, 0, 0, 1, 0, 0, 0],  # m_23 + m_12346
        [1, 1, 0, 0, 0, 1, 0, 1, 0],  # m_2 + m_23 + m_12346 + m_1235
        [0, 0, 1, 0, 0, 0, 0, 0, 0],  # m_236
        [0, 1, 0, 0, 0, 0, 0, 0, 0],  # m_23
        [0, 1, 0, 0, 0, 1, 1, 0, 0],  # m_23 + m_12346 + m_2345
        [0, 0, 0, 1, 0, 0, 0, 0, 0],  # m_23456
    ]


def piece_image_cone_rays(name, ar):
    A = piece_matrix(ALL_PI[name])
    image_rays = []
    for r in ar:
        v = [sum(int(A[i, j]) * int(r[j]) for j in range(9)) for i in range(6)]
        if any(x != 0 for x in v):
            from math import gcd
            from functools import reduce
            g = reduce(gcd, [abs(x) for x in v if x != 0])
            v = tuple(x // g for x in v)
            image_rays.append(v)
    return image_rays


def cone_dim(rays):
    """Real dim of cone spanned by rays."""
    if not rays:
        return 0
    M = sp.Matrix(rays).T  # 6 x n
    return M.rank()


def cone_contains(rays_outer, rays_inner):
    """Does the cone of `rays_outer` contain each ray of `rays_inner`?

    Use LP: r in cone(rays_outer) iff exists lambda >= 0 with
    sum lambda_i * rays_outer[i] = r.
    """
    from scipy.optimize import linprog
    A_eq = np.array(rays_outer, dtype=float).T  # dim x n
    for r in rays_inner:
        b_eq = np.array(r, dtype=float)
        c = np.zeros(A_eq.shape[1])
        res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)]*A_eq.shape[1],
                      method='highs')
        if not res.success:
            return False
    return True


def main():
    print("=" * 78)
    print("DAY 61 — FAN STRUCTURE TEST IN BDI-SPACE")
    print("=" * 78)

    # Step 1: BDI rays
    print("\nStep 1: Extreme rays of P^BDI_3")
    br = bdi_rays()
    print(f"  # rays: {len(br)}")
    for r in br:
        d = {BDI_VARS[j]: r[j] for j in range(6) if r[j] != 0}
        print(f"    {d}")

    ar = aii_rays()
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]

    # Step 2: For each piece, compute its image cone & check if = P^BDI_3
    print("\nStep 2: Is each C_i = P^BDI_3?")
    all_equal_count = 0
    proper_subset_count = 0
    cone_data = {}
    for name in pieces:
        ic = piece_image_cone_rays(name, ar)
        d = cone_dim(ic)
        # Check if C_i contains all BDI rays
        contains_all = cone_contains(ic, br)
        contained_in_bdi = cone_contains(br, ic)
        if contains_all and contained_in_bdi:
            status = "= P^BDI_3"
            all_equal_count += 1
        elif contained_in_bdi:
            status = "PROPER subset of P^BDI_3"
            proper_subset_count += 1
        elif contains_all:
            status = "CONTAINS P^BDI_3 properly"
        else:
            status = "incomparable"
        cone_data[name] = (ic, d, contains_all, contained_in_bdi)
        print(f"  {name}: dim={d}, status={status}")

    print(f"\nSummary: {all_equal_count} pieces with C_i = P^BDI_3 (as real cones)")
    print(f"         {proper_subset_count} pieces with C_i ⊊ P^BDI_3")

    # Step 3: If all C_i = P^BDI_3, fan structure in BDI is trivial
    if all_equal_count == len(pieces):
        print("\nCONCLUSION: All 26 pieces have C_i = P^BDI_3 as REAL cones.")
        print("            The piece distinction is purely LATTICE-LEVEL.")
        print("            No fan structure in BDI as a polyhedral cone.")
        print("            Distinction must be in lattice sub-monoid structure.")
    elif proper_subset_count > 0:
        print("\nSome pieces have proper-subcone images. Checking fan condition...")
        # Check pairwise intersection condition

    # Step 4: Lattice-level analysis (regardless of step 2 result)
    # For each piece, what's the image sub-monoid generated by lattice rays?
    print("\nStep 3: Lattice image structure")
    # Image sub-monoid: positive lattice span of pi^(i)(extremal AII lattice rays)
    print("  (image rays computed already; sub-monoid = N-span of those)")

    # Step 5: Distinct image-cone facet count
    print("\nStep 4: Facet structure of each C_i")
    # Compute facets of each C_i by finding inequalities
    # Use sympy nullspace of (5-subsets of rays) approach
    for name in pieces[:3]:  # sample first 3
        ic, _, _, _ = cone_data[name]
        print(f"\n  {name}: image rays")
        for r in ic:
            d = {BDI_VARS[j]: r[j] for j in range(6) if r[j] != 0}
            print(f"    {d}")


if __name__ == "__main__":
    main()
