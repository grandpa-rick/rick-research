"""
Day 61 — Image cones in BDI-space.

For each piece i, compute C_i := pi^(i)(P^AII_5) as a polyhedral cone in
BDI-space.

Approach: pi^(i) is a linear map AII -> BDI. P^AII_5 is a polyhedral cone
in AII. Its image is a polyhedral cone in BDI (image of a cone under a
linear map is a cone). We can compute the image via:
   C_i = { q in R^6 : exists p in P^AII_5 with pi^(i)(p) = q }
       = { q : exists p with p >= 0 (in AII sense), A_AII p >= 0, pi^(i)(p) = q }

We compute C_i as a "V-representation" by projecting the rays of P^AII_5
through pi^(i), then convex-hulling.

P^AII_5 is a 9-dim cone. We need its extreme rays first.

ALTERNATIVE (more direct): for each pair (i, j), check whether
C_i cap C_j is a face of both.

We use scipy / polytope tools.

KEY FACT: each pi^(i) has rank 6. The image C_i is a 6-dim cone in
6-dim BDI space. So generically C_i = (a region of) the BDI cone.

QUESTION: is C_i = P^BDI_3 for all i? Or do different pieces produce
different subsets of P^BDI_3?

If C_i are all distinct, then the cover structure is meaningful. If
C_i = P^BDI_3 for all i, then any single piece would suffice for
surjectivity — but we know it doesn't (different LATTICE points need
different pieces). So the difference must be in the LATTICE structure
of the image, not the rational/real image.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
import numpy as np
from verify_full_v7 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS, BDI_VARS


def aii_rays():
    """Compute extreme rays of P^AII_5 as a 9-dim cone.

    AII inequalities:
      - 9 nonneg: m_X >= 0
      - Main_2: m_2 - m_12356 - m_1235 >= 0
      - Main_3: m_23 - m_12346 - m_1234 >= 0
      - Sing_L: m_12346 - m_1235 - m_2345 >= 0
      - Sing_R: m_23 + m_1235 + m_2345 - m_12346 >= 0

    Use cdd or pycddlib if available; otherwise manual.
    """
    # Manually enumerate extreme rays.
    # Variables (in order): m_2, m_23, m_236, m_23456, m_12356, m_12346, m_2345, m_1235, m_1234

    # Strategy: a 9-dim cone in R^9 with 13 inequalities. At each extreme
    # ray, exactly 8 of the 13 inequalities are tight (rank 8 deficiency
    # from 9-dim).

    # Use a small library. Try pycddlib via apt.
    try:
        import cdd
    except ImportError:
        print("WARNING: cdd not available, using brute-force ray enumeration")
        return brute_force_rays()

    # H-rep: cdd uses (b | A) with A x <= b... but we have A x >= 0 (i.e., -A x <= 0).
    # cdd convention: M = [b | -A] for b - Ax >= 0.
    A = []
    # 9 nonneg
    for i in range(9):
        row = [0]*10
        row[i+1] = 1
        A.append(row)
    # Main_2
    row = [0]*10
    row[1+0] = 1; row[1+4] = -1; row[1+7] = -1  # m_2 - m_12356 - m_1235
    A.append(row)
    # Main_3
    row = [0]*10
    row[1+1] = 1; row[1+5] = -1; row[1+8] = -1  # m_23 - m_12346 - m_1234
    A.append(row)
    # Sing_L: m_12346 - m_1235 - m_2345 >= 0
    row = [0]*10
    row[1+5] = 1; row[1+7] = -1; row[1+6] = -1
    A.append(row)
    # Sing_R: m_23 + m_1235 + m_2345 - m_12346 >= 0
    row = [0]*10
    row[1+1] = 1; row[1+7] = 1; row[1+6] = 1; row[1+5] = -1
    A.append(row)

    mat = cdd.matrix_from_array(A, rep_type=cdd.RepType.INEQUALITY)
    poly = cdd.polyhedron_from_matrix(mat)
    gens = cdd.copy_generators(poly)
    rays = []
    for row in gens.array:
        if row[0] == 0:
            # ray
            rays.append([row[i+1] for i in range(9)])
    return rays


def brute_force_rays():
    """Enumerate rays by iterating over 8-subsets of 13 inequalities."""
    from itertools import combinations
    # Inequality matrix: 13 x 9. We want rays = directions in nullspace
    # of any 8-subset of these, where the remaining 5 evaluate to > 0
    # (or 0 if higher-codim).
    A_rows = []
    # 9 nonneg
    for i in range(9):
        v = [0]*9
        v[i] = 1
        A_rows.append(v)
    # Main_2
    v = [0]*9; v[0] = 1; v[4] = -1; v[7] = -1
    A_rows.append(v)
    # Main_3
    v = [0]*9; v[1] = 1; v[5] = -1; v[8] = -1
    A_rows.append(v)
    # Sing_L
    v = [0]*9; v[5] = 1; v[7] = -1; v[6] = -1
    A_rows.append(v)
    # Sing_R
    v = [0]*9; v[1] = 1; v[7] = 1; v[6] = 1; v[5] = -1
    A_rows.append(v)

    rays_set = set()
    for subset in combinations(range(13), 8):
        # Build submatrix
        M = sp.Matrix([A_rows[i] for i in subset])
        ns = M.nullspace()
        if len(ns) != 1:
            continue
        v = ns[0]
        # Check signs in other 5 inequalities
        signs_pos = []
        for i in range(13):
            if i in subset: continue
            val = sum(A_rows[i][j] * v[j] for j in range(9))
            signs_pos.append(val)
        # If all >= 0, this is the ray (positive direction); also try negation
        from sympy import Rational
        for sign in [1, -1]:
            vv = [sign * v[j] for j in range(9)]
            if all(sum(A_rows[i][j] * vv[j] for j in range(9)) >= 0 for i in range(13)):
                # Normalize: divide by gcd
                from math import gcd
                from functools import reduce
                num_vals = [int(x) if x.is_integer else x for x in vv]
                # Check rational
                try:
                    int_vals = [int(x * 1) for x in vv]
                    # Find common denominator
                    from fractions import Fraction
                    fracs = [Fraction(str(x)) for x in vv]
                    lcm_denom = 1
                    for f in fracs:
                        lcm_denom = lcm_denom * f.denominator // gcd(lcm_denom, f.denominator)
                    int_vals = [int(f * lcm_denom) for f in fracs]
                    g = reduce(gcd, [abs(x) for x in int_vals if x != 0], 0)
                    if g > 0:
                        int_vals = [x // g for x in int_vals]
                    rays_set.add(tuple(int_vals))
                except Exception:
                    pass
                break
    return [list(r) for r in rays_set]


def piece_image_rays(name, aii_rays_list):
    """Compute image rays in BDI-space by applying pi^(i) to AII rays."""
    A = piece_matrix(ALL_PI[name])  # 6 x 9
    image_rays = []
    for r in aii_rays_list:
        # A @ r as column
        v = [sum(int(A[i, j]) * int(r[j]) for j in range(9)) for i in range(6)]
        if any(x != 0 for x in v):
            # Normalize
            from math import gcd
            from functools import reduce
            g = reduce(gcd, [abs(x) for x in v if x != 0])
            v = [x // g for x in v]
            image_rays.append(tuple(v))
    return list(set(image_rays))


def main():
    print("=" * 78)
    print("DAY 61 — IMAGE CONES IN BDI-SPACE")
    print("=" * 78)

    # Step 1: AII extreme rays
    print("\nStep 1: Computing extreme rays of P^AII_5...")
    rays = aii_rays()
    print(f"  # extreme rays: {len(rays)}")
    if len(rays) < 30:
        for r in rays:
            d = {AII_VARS[j]: r[j] for j in range(9) if r[j] != 0}
            print(f"    {d}")

    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]

    # Step 2: For each piece, image rays
    print("\nStep 2: Image rays per piece...")
    piece_image_set = {}
    for name in pieces:
        irays = piece_image_rays(name, rays)
        piece_image_set[name] = set(irays)
        print(f"  {name}: {len(irays)} image rays")

    # Step 3: Compare images
    print("\nStep 3: Distinct image-ray sets")
    seen = {}
    for name in pieces:
        key = frozenset(piece_image_set[name])
        seen.setdefault(key, []).append(name)
    print(f"  Distinct image-ray sets: {len(seen)}")
    for j, (k, names) in enumerate(seen.items()):
        print(f"    set {j} ({len(k)} rays): pieces = {names}")

    # Step 4: Union of all image rays
    print("\nStep 4: Union of all image rays")
    all_image_rays = set()
    for name in pieces:
        all_image_rays |= piece_image_set[name]
    print(f"  Total distinct image rays across all 26 pieces: {len(all_image_rays)}")

    # Step 5: How many of these rays are in P^BDI_3 (lattice cone)?
    # P^BDI_3 cone: M_1=0, T_a, B_a-T_a, P_1-M_2, P_2-S all >= 0.
    # Variables: (M_2, B_1, T_1, B_2, T_2, S)
    print("\nStep 5: BDI cone facets check on image rays")
    in_bdi = 0
    for r in all_image_rays:
        M_2, B_1, T_1, B_2, T_2, S = r
        P_1 = 2*(B_1 - T_1)
        P_2 = P_1 + 2*(B_2 - T_2)
        if T_1 >= 0 and T_2 >= 0 and (B_1 - T_1) >= 0 and (B_2 - T_2) >= 0 \
           and (P_1 - M_2) >= 0 and (P_2 - S) >= 0 and M_2 >= 0 and S >= 0:
            in_bdi += 1
    print(f"  Image rays inside P^BDI_3: {in_bdi}/{len(all_image_rays)}")

    # Print first 20 distinct image rays
    print("\n  Sample image rays (M_2, B_1, T_1, B_2, T_2, S):")
    for r in sorted(all_image_rays)[:20]:
        print(f"    {r}")


if __name__ == "__main__":
    main()
