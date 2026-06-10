"""
Day 63 CODE Task 2 — Higher-codim (codim-2) wall analysis at N = 12.

The kernel arrangement has:
  - 3 codim-1 walls (rank-1 pairs): m_2 = 0, m_236 = 0, m_23456 = 0.
    These define the 8 sign-pattern strata (sigma in {0,1}^3).
  - 108 rank-2 pairs (codim-2 kernels = dim 7 subspaces).
  - 126 rank-3 pairs (codim-3 kernels = dim 6).

Hypothesis (Day-62 / Day-63 PROVE): within-stratum variance in |I(p)| is fully
explained by higher-codim wall incidence — codim-1-only points hit the stratum
mode value, codim-2-hitting points have lower |I| (extra pair-collisions).

Procedure:
  1. Compute all rank-2 difference matrices D(i, j) and their 9x{n} kernel
     bases.  Two pairs sharing the same kernel subspace are grouped.
  2. For each lattice point p in stratum sigma at N=12, test whether
     D(i, j) p = 0 for any rank-2 pair (i, j).
  3. Histogram |I(p)| split by "codim-2-hit" vs "codim-2-miss".
"""

import sys, time, json
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations

import sympy as sp

sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS


def stratum_sig(p):
    return (
        1 if p["m_2"] > 0 else 0,
        1 if p["m_236"] > 0 else 0,
        1 if p["m_23456"] > 0 else 0,
    )


def p_vec(p):
    return [p[v] for v in AII_VARS]


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    Ms = [piece_matrix(ALL_PI[name]) for name in pieces]

    # Find all rank-2 difference matrices and their kernel SUBSPACES.
    # Two pairs with identical kernels = same codim-2 wall.
    rank2_pairs = []  # list of (i, j, D_as_numpy_matrix)
    print("Scanning pairs for rank-2 differences...")
    for i, j in combinations(range(len(Ms)), 2):
        D = Ms[i] - Ms[j]
        if D.rank() == 2:
            rank2_pairs.append((i, j, D))
    print(f"  {len(rank2_pairs)} rank-2 pairs found.")

    # Convert each D to integer form and store the 2 ROWS that span the
    # row space (used to test D p = 0).
    # We can simplify: store the row reduction of D, and use 2 independent
    # linear forms l_1, l_2 such that ker D = ker {l_1 = l_2 = 0}.
    rank2_forms = []
    for i, j, D in rank2_pairs:
        # rref gives independent rows = the 2 linear forms
        R, pivots = D.T.rref()  # column ops by transposing
        # Easier: compute D.rref() row-wise then take the 2 nonzero rows
        Rr, _ = D.rref()
        forms = []
        for r in range(D.rows):
            row = [int(Rr[r, k]) for k in range(9)]
            if any(row):
                forms.append(tuple(row))
        # Normalize: scale to integers (rref gives rationals)
        forms = forms[:2]
        rank2_forms.append((i, j, forms))

    # Group by SUBSPACE: pairs whose 2-form span is identical define the same wall.
    # Test equivalence by canonicalizing: stack and reduce to a canonical form.
    def canonical_subspace(forms):
        M = sp.Matrix(forms)
        Rr, _ = M.rref()
        rows = []
        for r in range(Rr.rows):
            row = tuple(Rr[r, k] for k in range(9))
            if any(row):
                rows.append(row)
        return tuple(rows)

    wall_groups = defaultdict(list)
    for i, j, forms in rank2_forms:
        key = canonical_subspace(forms)
        wall_groups[key].append((i, j))
    print(f"  {len(wall_groups)} distinct codim-2 wall subspaces "
          f"(from {len(rank2_pairs)} pairs).")

    # Convert wall keys to numpy-int testable forms.
    walls = []  # list of (2 linear forms as lists of int)
    for key, pairs_in_wall in wall_groups.items():
        forms = []
        for row in key:
            # row may contain Rational
            row_int = [int(c) if c.q == 1 else c for c in row]
            forms.append(row_int)
        walls.append((forms, pairs_in_wall))

    # Need integer-valued tests: scale rational rows by their LCD.
    integer_walls = []
    for forms, pairs_in_wall in walls:
        ifs = []
        for row in forms:
            denoms = [int(c.q) if hasattr(c, "q") else 1 for c in row]
            from math import lcm
            L = 1
            for d in denoms:
                L = lcm(L, d)
            ints = []
            for c in row:
                if hasattr(c, "q"):
                    ints.append(int(c * L))
                else:
                    ints.append(int(c) * L)
            ifs.append(ints)
        integer_walls.append((ifs, pairs_in_wall))

    print(f"\nIntegerised: {len(integer_walls)} walls ready for testing.")

    # Now enumerate AII points at N = 12.
    N = 12
    print(f"\nEnumerating AII lattice points at N = {N}...")
    t0 = time.time()
    aii_pts = enumerate_aii_n3_full(N)
    print(f"  {len(aii_pts)} points in {time.time()-t0:.1f}s")

    # For each p, compute (a) sigma stratum, (b) |I(p)|, (c) which codim-2
    # walls it hits (as a set of indices into `integer_walls`).
    print("Computing per-point stats...")
    t0 = time.time()
    per_point = []  # (sig, |I|, frozenset of wall indices hit)
    for p in aii_pts:
        sig = stratum_sig(p)
        # |I|
        I = set()
        for name in pieces:
            q = apply_pi(ALL_PI[name], p)
            ok, _ = bdi_feasible_n3(q)
            if not ok:
                continue
            I.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))
        nI = len(I)
        # Wall incidence
        pv = p_vec(p)
        hits = []
        for w_idx, (forms, _) in enumerate(integer_walls):
            on = True
            for row in forms:
                s = sum(c * pv[k] for k, c in enumerate(row))
                if s != 0:
                    on = False
                    break
            if on:
                hits.append(w_idx)
        per_point.append((sig, nI, tuple(hits)))
    print(f"  {time.time()-t0:.1f}s")

    # Per-stratum analysis: split |I| histogram between codim-2-hitting and
    # codim-2-only-codim-1 points.
    by_stratum = defaultdict(lambda: defaultdict(Counter))
    for sig, nI, hits in per_point:
        bucket = "codim2_hit" if hits else "codim2_miss"
        by_stratum[sig][bucket][nI] += 1

    sigs = sorted(by_stratum)
    print(f"\n=== Per-stratum |I| histogram split: codim-2-MISS vs HIT (N={N}) ===\n")
    for sig in sigs:
        sig_str = "".join(str(s) for s in sig)
        miss = by_stratum[sig]["codim2_miss"]
        hit  = by_stratum[sig]["codim2_hit"]
        n_miss = sum(miss.values())
        n_hit  = sum(hit.values())
        print(f"--- sigma = {sig_str}  (miss={n_miss}, hit={n_hit}) ---")
        print(f"  codim-2 MISS |I| histogram: {dict(sorted(miss.items()))}")
        print(f"  codim-2 HIT  |I| histogram: {dict(sorted(hit.items()))}")
        # Mode of miss group = "generic" stratum value
        if miss:
            mode_miss = miss.most_common(1)[0][0]
            print(f"  Generic (miss) MODE: {mode_miss}")
        if hit:
            mode_hit = hit.most_common(1)[0][0]
            print(f"  Wall (hit)     MODE: {mode_hit}")
        print()

    # Number of distinct walls hit, per stratum
    wall_count_dist = defaultdict(Counter)
    for sig, nI, hits in per_point:
        wall_count_dist[sig][len(hits)] += 1
    print("\n=== # codim-2 walls hit per point, by stratum ===")
    for sig in sigs:
        sig_str = "".join(str(s) for s in sig)
        print(f"  {sig_str}: {dict(sorted(wall_count_dist[sig].items()))}")

    # Save
    out_path = Path("codim2_walls_result.json")
    # Make serializable
    ser = {
        "N": N,
        "n_walls": len(integer_walls),
        "n_rank2_pairs": len(rank2_pairs),
        "by_stratum": {
            "".join(str(s) for s in sig): {
                "miss": dict(by_stratum[sig]["codim2_miss"]),
                "hit": dict(by_stratum[sig]["codim2_hit"]),
            }
            for sig in sigs
        },
        "wall_count_dist": {
            "".join(str(s) for s in sig): dict(wall_count_dist[sig])
            for sig in sigs
        },
    }
    out_path.write_text(json.dumps(ser, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
