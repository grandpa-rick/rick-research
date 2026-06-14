"""
Day 70 CODE Task A — General-n AXIS count machinery (n=6, n=7).

Lifts the n=5 scaffold (code/2026-06-13-n5-axis-count/) to arbitrary n.

The AII polytope at level n:
  vars: prefix[1..n], long[1..n], short[1..n-1] + linkLHS  (n even)
                                 short[1..n]               (n odd)
  ineqs: long[i] + short[i] <= prefix[i-1]  for i=2..n
                                             (at even n, i=n: short[n]
                                              doesn't exist, row is
                                              long[n] <= prefix[n-1])
  eq (even n): linkLHS = sum_{i=1..n-1} short[i]
  all vars >= 0.

The BDI polytope at level n:
  vars: M_2..M_{n-1}, B_1..B_{n-1}, T_1..T_{n-1}, S    (3n-3 vars)
  ineqs: T_a >= 0, B_a >= 0, T_a <= B_a, M_a >= 0, S >= 0,
         M_a <= P_{a-1}, M_a <= P_a (a=2..n-1),
         S <= P_{n-1},
         P_a := 2 sum_{b<=a}(B_b - T_b) >= 0.

Piece = linear map AII -> BDI with nonneg integer entries.

A piece is BDI-feasible if for every AII-feasible lattice point p, M @ p
is BDI-feasible.

This module exposes:
- aii_struct(n): structure dict (vars, prefix_idx, long_idx, short_idx,
                                  linkLHS_idx, ineq matrix, eq matrix)
- bdi_vars(n): list of BDI var names
- aii_feasible(p, n): bool
- bdi_feasible(q, n): bool
- enumerate_aii_lattice(n, N_max): generate AII lattice pts with sum<=N_max
- piece_matrix(spec, n): build (3n-3) x len(aii_vars) matrix from spec
- verify_piece(M, n, samples): list of failures
- analyze_axis(pieces_dict, n, samples): col counts, rank distribution,
                                          rank-1 walls, AXIS count.
"""

from __future__ import annotations
import numpy as np
from collections import Counter


def aii_struct(n):
    """Return AII structure dict for level n."""
    vars_list = []
    prefix_idx = []
    long_idx = []
    short_idx = []
    linkLHS_idx = None

    for i in range(1, n + 1):
        vars_list.append(f"prefix[{i}]")
        prefix_idx.append(len(vars_list) - 1)
    for i in range(1, n + 1):
        vars_list.append(f"long[{i}]")
        long_idx.append(len(vars_list) - 1)
    if n % 2 == 0:
        for i in range(1, n):
            vars_list.append(f"short[{i}]")
            short_idx.append(len(vars_list) - 1)
        vars_list.append("linkLHS")
        linkLHS_idx = len(vars_list) - 1
    else:
        for i in range(1, n + 1):
            vars_list.append(f"short[{i}]")
            short_idx.append(len(vars_list) - 1)

    n_vars = len(vars_list)
    assert n_vars == 3 * n, (n, n_vars)

    return {
        "n": n,
        "vars": vars_list,
        "n_vars": n_vars,
        "prefix_idx": prefix_idx,
        "long_idx": long_idx,
        "short_idx": short_idx,
        "linkLHS_idx": linkLHS_idx,
    }


def bdi_vars(n):
    names = []
    for a in range(2, n):
        names.append(f"M_{a}")
    for a in range(1, n):
        names.append(f"B_{a}")
    for a in range(1, n):
        names.append(f"T_{a}")
    names.append("S")
    assert len(names) == 3 * n - 3
    return names


def aii_feasible(p, struct):
    n = struct["n"]
    prefix_idx = struct["prefix_idx"]
    long_idx = struct["long_idx"]
    short_idx = struct["short_idx"]
    linkLHS_idx = struct["linkLHS_idx"]
    if any(v < 0 for v in p):
        return False
    # Main_i: long[i] + short[i] <= prefix[i-1] for i=2..n.
    for i in range(2, n + 1):
        L = p[long_idx[i - 1]]
        SH = 0
        if i - 1 < len(short_idx) and (n % 2 == 1 or i < n):
            SH = p[short_idx[i - 1]]
        P_im1 = p[prefix_idx[i - 2]]
        if L + SH > P_im1:
            return False
    # Linking eq at even n.
    if n % 2 == 0:
        lhs = p[linkLHS_idx]
        rhs = sum(p[short_idx[j]] for j in range(n - 1))
        if lhs != rhs:
            return False
    return True


def bdi_feasible(q, n):
    names = bdi_vars(n)
    if len(q) != len(names):
        raise ValueError(f"q has {len(q)} entries, expected {len(names)}")
    idx = {nm: i for i, nm in enumerate(names)}
    if any(v < 0 for v in q):
        return False
    for a in range(1, n):
        if q[idx[f"T_{a}"]] > q[idx[f"B_{a}"]]:
            return False
    P = {0: 0}
    for a in range(1, n):
        P[a] = P[a - 1] + 2 * (q[idx[f"B_{a}"]] - q[idx[f"T_{a}"]])
        if P[a] < 0:
            return False
    for a in range(2, n):
        Ma = q[idx[f"M_{a}"]]
        if Ma > P[a - 1] or Ma > P[a]:
            return False
    if q[idx["S"]] > P[n - 1]:
        return False
    return True


def enumerate_aii_lattice(struct, N_max):
    """Enumerate AII lattice points with sum <= N_max.

    For even n, the linkLHS variable is determined by the short[i],
    so we enumerate free vars and compute linkLHS.
    """
    n = struct["n"]
    n_vars = struct["n_vars"]
    prefix_idx = struct["prefix_idx"]
    long_idx = struct["long_idx"]
    short_idx = struct["short_idx"]
    linkLHS_idx = struct["linkLHS_idx"]

    pts = []

    if n % 2 == 1:
        # All 3n vars are free; check ineqs only.
        def gen(remaining, depth, current):
            if depth == n_vars:
                if aii_feasible(current, struct):
                    pts.append(tuple(current))
                return
            for v in range(remaining + 1):
                current.append(v)
                gen(remaining - v, depth + 1, current)
                current.pop()

        gen(N_max, 0, [])
    else:
        # 3n - 1 free vars (omit linkLHS); compute linkLHS = sum(short).
        # Enumerate by index list: 0..n_vars-1 except linkLHS_idx.
        free_idx = [i for i in range(n_vars) if i != linkLHS_idx]
        # Use budget that allows linkLHS too: budget on free vars is N_max
        # minus what linkLHS will absorb. But linkLHS = sum(short), so sum
        # of all vars is (free sum) + sum(short).
        # Simplification: enumerate free vars with budget N_max // 2 ?
        # safer: enumerate free with budget B, then linkLHS adds sum(short),
        # so cap free sum at N_max - sum(short_already). Use index-based
        # backtracking with running short sum.
        def gen(remaining, idx_pos, current_full):
            if idx_pos == len(free_idx):
                # set linkLHS = sum of short
                lhs = sum(current_full[short_idx[j]] for j in range(n - 1))
                current_full[linkLHS_idx] = lhs
                # Total sum constraint: linkLHS adds lhs; we already paid
                # for the free vars, but linkLHS is "extra" - cap on total
                # sum <= N_max means free sum + lhs <= N_max, i.e.,
                # (N_max - remaining) + lhs <= N_max, so lhs <= remaining.
                if lhs > remaining:
                    current_full[linkLHS_idx] = 0
                    return
                if aii_feasible(current_full, struct):
                    pts.append(tuple(current_full))
                current_full[linkLHS_idx] = 0
                return
            slot = free_idx[idx_pos]
            for v in range(remaining + 1):
                current_full[slot] = v
                gen(remaining - v, idx_pos + 1, current_full)
                current_full[slot] = 0

        current_full = [0] * n_vars
        gen(N_max, 0, current_full)

    return pts


def piece_matrix(spec, struct):
    """spec: {bdi_var: [(coef, aii_var), ...]}.
    Returns (3n-3) x n_vars int matrix."""
    n = struct["n"]
    aii_v = struct["vars"]
    bdi_v = bdi_vars(n)
    n_bdi = len(bdi_v)
    M = np.zeros((n_bdi, struct["n_vars"]), dtype=int)
    for bv, terms in spec.items():
        bi = bdi_v.index(bv)
        for (coef, av) in terms:
            ai = aii_v.index(av)
            M[bi, ai] += coef
    return M


def piece_apply(M, p):
    return tuple(int(np.dot(M[i], p)) for i in range(M.shape[0]))


def verify_piece(M, struct, sample_pts):
    n = struct["n"]
    bad = []
    for p in sample_pts:
        q = piece_apply(M, p)
        if not bdi_feasible(q, n):
            bad.append((p, q))
    return bad


def analyze_axis(feasible, struct, label="", min_axis_collisions=3):
    """Run the rank-1 wall / AXIS analysis.

    A variable is AXIS iff its coordinate hyperplane is a rank-1 wall
    with >= min_axis_collisions piece-pair collisions.
    """
    aii_v = struct["vars"]
    n_aii = struct["n_vars"]
    names = list(feasible.keys())
    mats = [feasible[nm] for nm in names]
    n_pieces = len(names)
    n_bdi = mats[0].shape[0]

    # Column-type counts per AII variable
    cols_per_var = {av: set() for av in aii_v}
    for M in mats:
        for i in range(n_aii):
            c = tuple(int(M[r, i]) for r in range(n_bdi))
            cols_per_var[aii_v[i]].add(c)

    col_counts = {av: len(cols_per_var[av]) for av in aii_v}
    rigid = [av for av in aii_v if col_counts[av] == 1]
    binary = [av for av in aii_v if col_counts[av] == 2]
    axis_by_colcount = [av for av in aii_v if col_counts[av] >= 3]

    # Rank-1 piece-pair walls
    rank_counter = Counter()
    rank1_walls = {}
    for i in range(n_pieces):
        for j in range(i + 1, n_pieces):
            D = mats[i] - mats[j]
            if np.all(D == 0):
                continue
            r = int(np.linalg.matrix_rank(D))
            rank_counter[r] += 1
            if r == 1:
                nz_rows = [k for k in range(n_bdi) if not np.all(D[k] == 0)]
                r0 = nz_rows[0]
                pivot_col = next(c for c in range(n_aii) if D[r0, c] != 0)
                scale = D[r0, pivot_col]
                v = D[r0, :] / scale
                v_tuple = tuple(round(x, 9) for x in v)
                first_nz = next((x for x in v_tuple if x != 0), 1)
                if first_nz < 0:
                    v_tuple = tuple(-x for x in v_tuple)
                rank1_walls.setdefault(v_tuple, []).append((names[i], names[j]))

    axis_strict = []
    for v, pairs in rank1_walls.items():
        v_nz = [(aii_v[k], v[k]) for k in range(len(v)) if v[k] != 0]
        if len(v_nz) == 1 and len(pairs) >= min_axis_collisions:
            axis_strict.append((v_nz[0][0], len(pairs)))

    return {
        "label": label,
        "n_pieces": n_pieces,
        "col_counts": col_counts,
        "rigid": rigid,
        "binary": binary,
        "axis_by_colcount": axis_by_colcount,
        "axis_by_walls": [av for av, _ in axis_strict],
        "axis_pair_counts": dict(axis_strict),
        "n_axis": len(axis_strict),
        "rank_distribution": {int(k): int(v) for k, v in rank_counter.items()},
        "rank1_walls_summary": [
            {
                "wall_coords": [(aii_v[k], v[k]) for k in range(len(v))
                                 if v[k] != 0],
                "n_pair_collisions": len(pairs),
            }
            for v, pairs in sorted(rank1_walls.items(),
                                    key=lambda kv: -len(kv[1]))
        ],
    }
