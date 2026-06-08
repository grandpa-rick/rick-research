"""
Algorithmic piece construction: for each missing BDI point, try to find
an integer-PL piece hitting it via systematic enumeration.

KEY IDEA.  A linear piece pi : AII -> BDI is given by a 9x7 nonneg integer
coefficient matrix (M=coeffs in {0,1,2,3,4}). Each column corresponds to
one AII var X; the column is the image pi(e_X) in BDI.

For pi to "land in cone", the column pi(e_X) must:
- be in P^BDI_3 itself (i.e., satisfy T_a <= B_a, M_2 <= 2(B_1-T_1),
  S <= 2(B_1-T_1) + 2(B_2-T_2), M_1 = 0, all >= 0).
- if X is a CONSTRAINED AII var (with Main_2, Main_3, Singleton), then
  the contribution to BDI from X must be compensated by other vars
  such that the AII LP holds.

For pi to be SURJECTIVE on a target q in BDI lattice: there exist nonneg
integer (a_X) in the AII polytope such that sum a_X * pi(e_X) = q.

Approach: build pieces by selecting a "BASIS SUBSET" of AII vars and
choosing columns for each (in BDI cone), checking land-in-cone overall.

For practical use, restrict to pieces using FREE vars (m_2, m_{23456},
m_{236}, m_{12356} subject to Main_2) plus the standard level-2 + Singleton
vars with their canonical contributions.
"""

import sys
from itertools import product
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3,
                          enumerate_bdi_n3, apply_pi)
from verify_full_v9 import ALL_PI as REGISTRY_V9, get_image


# Standard "context" coefficients for the level-2 + Singleton AII vars.
# These are kept fixed across all pieces; only the FREE-VAR contributions
# vary.
CONTEXT_COEFS = {
    # m_23: contributes 1 to B_2 only (standard).
    "m_23":    {"B_2": 1},
    # m_2345: contributes 1 to B_1 and 1 to T_1 (Singleton-balanced).
    "m_2345":  {"B_1": 1, "T_1": 1},
    # m_1235: contributes 1 to B_2 and 1 to T_2 (Singleton).
    "m_1235":  {"B_2": 1, "T_2": 1},
    # m_12346: contributes 1 to S (standard for Main_3 + Singleton interplay).
    "m_12346": {"S": 1},
    # m_1234: contributes 2 to S (mass conservation).
    "m_1234":  {"S": 2},
}

# Free vars: m_2, m_{12356} (bounded by m_2), m_{23456}, m_{236}.
FREE_VARS = ["m_2", "m_12356", "m_23456", "m_236"]


def bdi_cone_check(col):
    """Check if a column (BDI vector) is in P^BDI_3."""
    M_1, M_2, B_1, T_1, B_2, T_2, S = col
    if M_1 != 0: return False
    if any(v < 0 for v in col): return False
    if T_1 > B_1 or T_2 > B_2: return False
    P_1 = 2*(B_1 - T_1)
    P_2 = P_1 + 2*(B_2 - T_2)
    if M_2 > P_1 or M_2 > P_2 or S > P_2: return False
    return True


def make_piece(free_cols):
    """Build a piece spec dict from a dict of free-var columns.
    free_cols: {var: (M_1, M_2, B_1, T_1, B_2, T_2, S) tuple}."""
    spec = {Y: [] for Y in ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]}
    # context
    for var, contrib in CONTEXT_COEFS.items():
        for Y, c in contrib.items():
            spec[Y].append((c, var))
    # free
    bdi_keys = ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]
    for var, col in free_cols.items():
        for Y, c in zip(bdi_keys, col):
            if c != 0:
                spec[Y].append((c, var))
    return spec


def piece_lands_in_cone(spec, N=4):
    """Check land-in-cone on small N."""
    aii_pts = enumerate_aii_n3_full(N)
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, _ = bdi_feasible_n3(q)
        if not ok:
            return False
    return True


def piece_image(spec, N):
    """Compute image of piece at N."""
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
    return image, bad


def construct_for_target(target):
    """Try to construct a piece hitting target = (M_1=0, M_2, B_1, T_1,
    B_2, T_2, S) using simple constructions.
    Strategy: try to express target as a single column (in BDI cone)
    on m_{23456}, then verify."""
    M_1, M_2, B_1, T_1, B_2, T_2, S = target
    col = (M_1, M_2, B_1, T_1, B_2, T_2, S)
    if not bdi_cone_check(col):
        return None
    # Piece supported entirely on m_{23456}: pi(m_23456 = 1) = target.
    free_cols = {"m_23456": col}
    spec = make_piece(free_cols)
    if piece_lands_in_cone(spec, N=4):
        return ("m_23456_alone", spec)
    return None


def main():
    # Find missing at N=11, 12, 13, 15
    print("Finding missing points at N=11..15...")
    missing_by_N = {}
    pieces_all = list(REGISTRY_V9.keys())
    for N in [11, 12, 13, 14, 15]:
        bdi_pts = enumerate_bdi_n3(N)
        union = set()
        for name in pieces_all:
            img, _, _ = get_image(name, N)
            union |= img
        missing = sorted(bdi_pts - union)
        missing_by_N[N] = missing
        print(f"  N={N}: {len(missing)} missing")

    # All missing across all N
    all_missing = set()
    for N in missing_by_N:
        for q in missing_by_N[N]:
            all_missing.add(q)
    print(f"Total unique missing: {len(all_missing)}")

    # For each missing point, try to construct a piece
    successes = []
    failures = []
    for q in sorted(all_missing):
        result = construct_for_target(q)
        if result is not None:
            successes.append((q, result))
        else:
            failures.append(q)

    print(f"\nSuccessful constructions: {len(successes)}")
    print(f"Failed constructions: {len(failures)}")

    if failures:
        print(f"\nFirst 10 failures:")
        for q in failures[:10]:
            _, M_2, B_1, T_1, B_2, T_2, S = q
            P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
            print(f"  M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S} P_1={P_1} P_2={P_2}")

    # Test: with these constructed pieces, what's coverage at N=11..15?
    print(f"\n=== With single-column pieces added ===")
    new_specs = {}
    for q, (kind, spec) in successes:
        name = f"auto_{q[1]}_{q[2]}_{q[3]}_{q[4]}_{q[5]}_{q[6]}"
        new_specs[name] = spec

    print(f"Added {len(new_specs)} new auto-constructed pieces.")

    # Verify coverage
    for N in [11, 12, 13, 14, 15]:
        bdi_pts = enumerate_bdi_n3(N)
        union = set()
        for name in pieces_all:
            img, _, _ = get_image(name, N)
            union |= img
        # add new
        for name, spec in new_specs.items():
            img, _ = piece_image(spec, N)
            union |= img
        cov = len(union & bdi_pts)
        pct = 100 * cov / len(bdi_pts)
        print(f"  N={N}: {cov}/{len(bdi_pts)} = {pct:.2f}%")


if __name__ == "__main__":
    main()
