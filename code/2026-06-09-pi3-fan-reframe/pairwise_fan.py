"""
Day 61 — Pairwise fan condition test.

For each pair (i, j) of pieces, check if dim(C_i cap C_j) < 6 (=
intersection is on the boundary, fan-compatible) or = 6 (= 6-dim overlap,
NOT fan).

Method: a 6-dim intersection has a non-empty INTERIOR. Pick a relative
interior point of C_i (centroid of rays) and check if it's in the
interior of C_j.

If interior of C_i intersects interior of C_j, then C_i cap C_j has
dim 6.

Let dim(C_i cap C_j) = 6 for many pairs => NOT a fan in BDI either.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import numpy as np
from scipy.optimize import linprog
from verify_full_v7 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, BDI_VARS

AII_RAYS = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
]


def piece_image_rays(name):
    import sympy as sp
    A = piece_matrix(ALL_PI[name])
    image_rays = []
    for r in AII_RAYS:
        v = [sum(int(A[i, j]) * int(r[j]) for j in range(9)) for i in range(6)]
        if any(x != 0 for x in v):
            image_rays.append(tuple(v))
    return image_rays


def is_in_cone(point, rays):
    """Check if `point` is in the cone of `rays` via LP."""
    A_eq = np.array(rays, dtype=float).T  # 6 x n
    c = np.zeros(A_eq.shape[1])
    res = linprog(c, A_eq=A_eq, b_eq=np.array(point, dtype=float),
                  bounds=[(0, None)]*A_eq.shape[1], method='highs')
    return res.success


def is_in_interior(point, rays):
    """Check if `point` is in relative interior of the cone of `rays`.

    Use: x in rel int iff x = sum a_i r_i with all a_i > 0
    Maximize min(a_i) s.t. sum a_i r_i = point, a_i >= 0.
    If min > 0, in interior.

    Equivalent: solve LP max t s.t. sum a_i r_i = x, a_i >= t.
    """
    n = len(rays)
    # Variables: a_1, ..., a_n, t. Maximize t.
    # Constraints: sum a_i r_i = x (6 eq); a_i - t >= 0 (n ineq, i.e., -a_i + t <= 0)
    c = np.zeros(n + 1)
    c[-1] = -1  # minimize -t = maximize t
    A_eq = np.zeros((6, n + 1))
    A_eq[:, :n] = np.array(rays, dtype=float).T
    b_eq = np.array(point, dtype=float)
    A_ub = np.zeros((n, n + 1))
    for i in range(n):
        A_ub[i, i] = -1  # -a_i
        A_ub[i, -1] = 1  # +t
    b_ub = np.zeros(n)
    # a_i >= 0, t free (but we'll allow negative)
    bounds = [(0, None)]*n + [(None, None)]
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    if not res.success:
        return False
    t_val = -res.fun
    return t_val > 1e-6


def centroid_point(rays):
    """Compute interior point = sum of all rays."""
    return [sum(r[i] for r in rays) for i in range(6)]


def main():
    print("=" * 78)
    print("DAY 61 — PAIRWISE FAN CONDITION TEST IN BDI-SPACE")
    print("=" * 78)

    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    piece_rays = {name: piece_image_rays(name) for name in pieces}

    # Interior points
    centroids = {name: centroid_point(piece_rays[name]) for name in pieces}

    # Verify centroids ARE in interior
    print("\nVerifying centroids in interior of own cone...")
    bad = 0
    for name in pieces:
        if not is_in_interior(centroids[name], piece_rays[name]):
            print(f"  WARNING: {name} centroid not in interior of own cone")
            bad += 1
    print(f"  Centroids in interior: {len(pieces) - bad}/{len(pieces)}")

    # Pairwise: does centroid of C_i lie in C_j (interior)?
    print("\nPairwise overlap counts (interior intersections)...")
    overlap_count = 0
    contains_count_per_piece = {name: 0 for name in pieces}
    overlaps = []  # list of (i, j) pairs with interior overlap
    for i_name in pieces:
        c_i = centroids[i_name]
        for j_name in pieces:
            if j_name == i_name:
                continue
            if is_in_interior(c_i, piece_rays[j_name]):
                overlap_count += 1
                contains_count_per_piece[j_name] += 1
                overlaps.append((i_name, j_name))

    print(f"\n  Total ordered pairs with C_j containing centroid of C_i: {overlap_count}")
    print(f"  Out of {len(pieces)*(len(pieces)-1)} ordered pairs total")

    print("\n  Containment count per piece (how many other centroids it contains):")
    for name in sorted(pieces, key=lambda n: -contains_count_per_piece[n]):
        print(f"    {name}: contains {contains_count_per_piece[name]} other centroid(s)")

    # Symmetric pairs (both contain each other's centroid)
    print("\nMUTUAL interior overlap (both contain each other's centroid):")
    mutual = 0
    for (a, b) in overlaps:
        if (b, a) in overlaps and a < b:
            mutual += 1
    print(f"  Mutual interior-overlap pairs: {mutual}")

    # CONCLUSION
    print("\nCONCLUSION:")
    if overlap_count == 0:
        print("  NO interior overlaps. The 26 image cones MIGHT form a fan!")
        print("  (Need to additionally verify intersections are common faces.)")
    else:
        print(f"  {overlap_count} interior overlaps detected.")
        print("  The image cones do NOT form a fan in BDI-space.")
        print("  Many pieces share 6-dim interior regions => piece selection is")
        print("  ambiguous on those regions => no canonical fan structure.")


if __name__ == "__main__":
    main()
