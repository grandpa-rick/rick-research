"""
Day 70 verification — Theorem 4.2 (Feasibility Ray-Characterisation)
sanity check.

For each piece in the n=5 27-piece registry, compute:
  (a) Direct feasibility: pi(p) in P^BDI for all AII lattice p with
      sum <= 5.
  (b) Ray feasibility: F1-F4 conditions on columns of pi.

Verify (a) matches (b).
"""

import sys
from pathlib import Path
sys.path.insert(0, '/home/agent/projects/code/2026-06-13-n5-axis-count')

import numpy as np
from n5_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS,
                       piece_matrix, verify_piece, enumerate_aii_lattice,
                       piece_apply, bdi_feasible_n5)
from n5_pieces import PIECES


def column(M, j):
    """Return the j-th column of M as a length-N_BDI tuple."""
    return tuple(int(M[r, j]) for r in range(N_BDI))


def add_cols(u, v):
    return tuple(u[i] + v[i] for i in range(N_BDI))


def in_p_bdi(v):
    """Check if v in P^BDI."""
    ok, _ = bdi_feasible_n5(v)
    return ok


# AII coord indices at n=5 (15 vars)
# Prefix: indices 0-4 (p_1,...,p_5)
# Long:   indices 5-9 (l_1,...,l_5)
# Short:  indices 10-14 (s_1,...,s_5)
P_IDX = list(range(5))
L_IDX = list(range(5, 10))
S_IDX = list(range(10, 15))


def ray_feasible(M):
    """Apply Theorem 4.2 (F1-F4) to piece matrix M."""

    # F1: pi^{p_j} in P^BDI for j = 1, ..., 5
    for j in range(5):
        col = column(M, P_IDX[j])
        if not in_p_bdi(col):
            return False, f"F1 at p_{j+1}: column {col} not in P^BDI"

    # F4: pi^{l_1}, pi^{s_1} in P^BDI
    col_l1 = column(M, L_IDX[0])
    if not in_p_bdi(col_l1):
        return False, f"F4 at l_1: column {col_l1} not in P^BDI"
    col_s1 = column(M, S_IDX[0])
    if not in_p_bdi(col_s1):
        return False, f"F4 at s_1: column {col_s1} not in P^BDI"

    # F2: pi^{p_{j-1}} + pi^{l_j} in P^BDI for j = 2, ..., 5
    for j in range(2, 6):  # j = 2, ..., 5
        col_p = column(M, P_IDX[j-2])  # p_{j-1}
        col_l = column(M, L_IDX[j-1])  # l_j
        s = add_cols(col_p, col_l)
        if not in_p_bdi(s):
            return False, f"F2 at j={j}: p_{j-1} + l_{j} = {s} not in P^BDI"

    # F3: pi^{p_{j-1}} + pi^{s_j} in P^BDI for j = 2, ..., 5
    for j in range(2, 6):
        col_p = column(M, P_IDX[j-2])
        col_s = column(M, S_IDX[j-1])
        s = add_cols(col_p, col_s)
        if not in_p_bdi(s):
            return False, f"F3 at j={j}: p_{j-1} + s_{j} = {s} not in P^BDI"

    return True, ""


def main():
    print("Day 70 verification — Theorem 4.2 (Feasibility Ray-Char) at n=5")
    print("=" * 70)

    pts = enumerate_aii_lattice(5)
    print(f"# AII lattice pts (sum<=5): {len(pts)}")

    direct_feasible = []
    direct_infeasible = []
    ray_feasible_set = []
    ray_infeasible = []

    for name, spec in PIECES.items():
        M = piece_matrix(spec)
        bad = verify_piece(M, pts)
        direct_ok = (len(bad) == 0)
        ray_ok, ray_err = ray_feasible(M)

        if direct_ok:
            direct_feasible.append(name)
        else:
            direct_infeasible.append((name, len(bad), bad[0][2]))

        if ray_ok:
            ray_feasible_set.append(name)
        else:
            ray_infeasible.append((name, ray_err))

    print(f"\nDirect feasibility: {len(direct_feasible)} feasible, {len(direct_infeasible)} infeasible")
    print(f"Ray feasibility:    {len(ray_feasible_set)} feasible, {len(ray_infeasible)} infeasible")

    # Cross-check
    direct_set = set(direct_feasible)
    ray_set = set(ray_feasible_set)

    if direct_set == ray_set:
        print(f"\n[PASS] Direct and Ray feasibility AGREE on all {len(PIECES)} pieces.")
        return 0
    else:
        only_direct = direct_set - ray_set
        only_ray = ray_set - direct_set
        print(f"\n[FAIL] Mismatch detected:")
        print(f"  Direct-only: {only_direct}")
        print(f"  Ray-only: {only_ray}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
