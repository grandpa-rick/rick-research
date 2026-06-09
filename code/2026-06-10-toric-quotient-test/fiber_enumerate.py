"""
Day 60 Task 3 (c): Fiber enumerate — for each BDI lattice point g at
small N, enumerate the AII preimage fibers and classify their structure.

If the toric-quotient hypothesis were true, each BDI fiber would be a
T^3-orbit of a single AII point. We test this empirically:

  - For each BDI point g (|g| ≤ N), count #{AII pts x : pi(x) = g for some
    piece pi}.
  - Group AII points by which piece(s) they come from.
  - Look at within-piece fiber structure: is it a 3-dim torus orbit?
    (We verified one example in moment_map_check.py; here we do it
    systematically.)

  - For BDI points NOT hit by any piece, identify what's missing.

Output: enumeration tables for small N + structural classification.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

import numpy as np
import sympy as sp
from collections import defaultdict, Counter
from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, enumerate_bdi_n3, apply_pi

AII_VARS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
            "m_2345", "m_1235", "m_1234"]
BDI_VARS = ["M_2", "B_1", "T_1", "B_2", "T_2", "S"]


def piece_matrix(spec):
    A = sp.zeros(6, 9)
    for bi, bv in enumerate(BDI_VARS):
        for c, av in spec.get(bv, []):
            A[bi, AII_VARS.index(av)] = c
    return A


def piece_kernel(spec):
    """Integer kernel basis. List of 9-tuples."""
    A = piece_matrix(spec)
    ker = A.nullspace()
    out = []
    for v in ker:
        denom = 1
        for x in v:
            denom = sp.lcm(denom, sp.fraction(x)[1])
        vint = tuple(int(x * denom) for x in v)
        out.append(vint)
    return out


def main():
    print("=" * 72)
    print("Day 60 Task 3(c): Fiber enumerate at n=3")
    print("=" * 72)
    print()

    # For each N, enumerate BDI lattice points and AII preimages.
    for N in [6, 8, 10]:
        print(f"--- N = {N} ---")
        bdi_pts = enumerate_bdi_n3(N)  # set of 7-tuples (M_1=0, M_2, B_1, T_1, B_2, T_2, S)
        aii_pts = enumerate_aii_n3_full(N)

        # Cache: image of each AII point under each piece.
        # For speed, organize by piece.
        # For each AII pt, find which pieces map it to a feasible BDI pt
        # and what that BDI pt is.
        bdi_to_pieces = defaultdict(set)  # bdi -> set of (piece, aii)
        for ai, p in enumerate(aii_pts):
            for pname, spec in ALL_PI.items():
                q = apply_pi(spec, p)
                ok, _ = bdi_feasible_n3(q)
                if not ok: continue
                g_key = (q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"])
                bdi_to_pieces[g_key].add((pname, tuple(p[v] for v in AII_VARS)))

        # Coverage
        covered = 0
        missing = []
        for q in bdi_pts:
            g_key = q[1:]  # drop M_1=0
            if g_key in bdi_to_pieces:
                covered += 1
            else:
                missing.append(g_key)
        print(f"  BDI lattice pts: {len(bdi_pts)}")
        print(f"  Covered: {covered}, missing: {len(missing)}")

        # Within-piece fiber size distribution
        fiber_size_dist = Counter()
        n_pieces_dist = Counter()
        for g_key, sets in bdi_to_pieces.items():
            pieces_hitting = set(p for p, _ in sets)
            n_pieces_dist[len(pieces_hitting)] += 1
            for pname in pieces_hitting:
                pts_under_p = sum(1 for p, x in sets if p == pname)
                fiber_size_dist[pts_under_p] += 1

        print(f"  Within-piece fiber size dist (Counter): "
              f"{dict(sorted(fiber_size_dist.items())[:8])}...")
        print(f"  # pieces hitting g dist: "
              f"{dict(sorted(n_pieces_dist.items())[:8])}...")
        print()

    # Detailed look at N=10 covered vs missing
    print("=" * 72)
    print("--- Detailed fiber analysis at N = 10 ---")
    print("=" * 72)
    N = 10
    bdi_pts = enumerate_bdi_n3(N)
    aii_pts = enumerate_aii_n3_full(N)

    bdi_to_pieces = defaultdict(lambda: defaultdict(set))  # g -> piece -> set of aii
    for p in aii_pts:
        for pname, spec in ALL_PI.items():
            q = apply_pi(spec, p)
            ok, _ = bdi_feasible_n3(q)
            if not ok: continue
            g_key = (q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"])
            bdi_to_pieces[g_key][pname].add(tuple(p[v] for v in AII_VARS))

    # Sample: fiber sizes for first 6 BDI pts (in some order).
    sample_bdis = list(bdi_to_pieces.keys())[:6]
    for g in sample_bdis:
        pieces = bdi_to_pieces[g]
        total_aii = set()
        for s in pieces.values():
            total_aii.update(s)
        print(f"  g = {g}: # pieces = {len(pieces)}, "
              f"|fiber (union)| = {len(total_aii)}")
        for pname, s in list(pieces.items())[:2]:
            print(f"    {pname}: {len(s)} AII pts under this piece")

    # Connection to N=11 issue: which BDI pts at N=11 are missing?
    print()
    print("=" * 72)
    print("--- N = 11 missing analysis ---")
    print("=" * 72)
    N = 11
    bdi_pts = enumerate_bdi_n3(N)
    aii_pts = enumerate_aii_n3_full(N)

    bdi_to_pieces = defaultdict(set)
    for p in aii_pts:
        for pname, spec in ALL_PI.items():
            q = apply_pi(spec, p)
            ok, _ = bdi_feasible_n3(q)
            if not ok: continue
            g_key = (q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"])
            bdi_to_pieces[g_key].add(pname)

    missing = []
    for q in bdi_pts:
        g_key = q[1:]
        if g_key not in bdi_to_pieces:
            missing.append(g_key)
    print(f"  BDI lattice pts at N=11: {len(bdi_pts)}")
    print(f"  Missing under 94-piece registry: {len(missing)}")
    print(f"  Missing list (first 20):")
    for g in missing[:20]:
        # Compute T_1 : T_2 ratio
        t1, t2 = g[2], g[4]
        ratio = f"{t1}:{t2}" if t2 else f"{t1}:0"
        print(f"    g (M_2,B_1,T_1,B_2,T_2,S) = {g}, T_1:T_2 = {ratio}")

    # Look at T_1:T_2 ratios in missing
    ratios = Counter()
    for g in missing:
        t1, t2 = g[2], g[4]
        if t2 == 0:
            ratios[("any", 0)] += 1
        elif t1 == 0:
            ratios[(0, "any")] += 1
        else:
            from math import gcd
            d = gcd(t1, t2)
            ratios[(t1//d, t2//d)] += 1
    print()
    print(f"  T_1:T_2 ratio distribution in missing:")
    for r, c in ratios.most_common():
        print(f"    {r}: {c}")


if __name__ == "__main__":
    main()
