"""
Day 72 CODE Task A -- Complete BDI-feasible piece registry at n=5, 6.

A 'piece' is a linear map pi: AII -> BDI represented as a (3n-3) x 3n
nonneg integer matrix M. The piece is BDI-feasible iff M sends every
AII-feasible lattice point to a BDI-feasible lattice point. By Day-70
Cor 5.1 (cone -> ray reduction), this is equivalent to: M @ r_j is
BDI-feasible for every AII extreme ray r_j.

We enumerate the FULL universe of pieces with parameter N = ray-image
bound (sum(M @ r_j) <= N for every ray r_j).

At odd n the cone has 3n rays forming a Z-basis, so M is uniquely
determined by its ray images. We enumerate by DFS over rays.

At even n the cone has 3n-1 rays (one degree collapsed by the linking
equation linkLHS = sum(short[i])). The matrix M has 3n columns; we
fix the gauge by enumerating with the linkLHS column free but
canonicalising pieces equivalent on feasible AII points.
"""

import sys
import json
import time
from pathlib import Path
from collections import defaultdict

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
from general_axis import (
    aii_struct, bdi_vars, bdi_feasible,
    piece_matrix, verify_piece, enumerate_aii_lattice
)


# ---------------------------------------------------------------------
# AII rays (Day-70 Thm 4.2 enumeration)
# ---------------------------------------------------------------------
def aii_rays(n):
    """Return list of AII rays as dicts {var_name: coef}.

    odd n: 3n rays. even n: 3n - 1 rays."""
    P = [f"prefix[{i}]" for i in range(1, n + 1)]
    L = [f"long[{i}]" for i in range(1, n + 1)]
    SH = [f"short[{i}]" for i in range(1, n if n % 2 == 0 else n + 1)]
    LAMBDA = "linkLHS" if n % 2 == 0 else None
    rays = []
    # 1. prefix[i] pure (i=1..n)
    for i in range(1, n + 1):
        rays.append({P[i - 1]: 1})
    # 2. long[1] pure
    rays.append({L[0]: 1})
    # 3. short[n] pure (odd n only)
    if n % 2 == 1:
        rays.append({SH[n - 1]: 1})
    # 4. pair: prefix[i-1] + long[i] for i=2..n-1
    for i in range(2, n):
        rays.append({P[i - 2]: 1, L[i - 1]: 1})
    # 5. pair: prefix[n-1] + long[n]
    rays.append({P[n - 2]: 1, L[n - 1]: 1})
    # 6. coupling: long[n] + short[1] (+ linkLHS at even n)
    r = {L[n - 1]: 1, SH[0]: 1}
    if n % 2 == 0:
        r[LAMBDA] = 1
    rays.append(r)
    # 7. for i=2..n-1: prefix[i-1] + long[n] + short[i] (+ linkLHS at even n)
    for i in range(2, n):
        r = {P[i - 2]: 1, L[n - 1]: 1, SH[i - 1]: 1}
        if n % 2 == 0:
            r[LAMBDA] = 1
        rays.append(r)
    return rays


def enumerate_bdi_lattice(n, N_max):
    bv = bdi_vars(n)
    n_bdi = len(bv)
    pts = []

    def gen(remaining, depth, current):
        if depth == n_bdi:
            if bdi_feasible(tuple(current), n):
                pts.append(tuple(current))
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()
    gen(N_max, 0, [])
    return pts


# ---------------------------------------------------------------------
# Pieces enumerator (odd n)
# ---------------------------------------------------------------------
def _build_ray_order(rays, n_aii_vars_total):
    """Return a list of (ray_index, intro_var_name, others_with_coef) such
    that each ray introduces exactly one new AII variable, and the order
    works (each compound ray's other vars are already assigned)."""
    process_order = []
    assigned = set()
    # Solo rays first
    for j, r in enumerate(rays):
        if len(r) == 1:
            v = next(iter(r))
            process_order.append((j, v, {}))
            assigned.add(v)
    # Compound rays
    remaining = [j for j in range(len(rays))
                 if not (len(rays[j]) == 1 and next(iter(rays[j])) in assigned)]
    while remaining:
        next_round = []
        progress = False
        for j in remaining:
            r = rays[j]
            unassigned = [v for v in r if v not in assigned]
            if len(unassigned) == 1:
                iv = unassigned[0]
                others = {v: c for v, c in r.items() if v != iv}
                process_order.append((j, iv, others))
                assigned.add(iv)
                progress = True
            else:
                next_round.append(j)
        if not progress:
            raise RuntimeError(f"Cannot decompose rays: {next_round}")
        remaining = next_round
    return process_order


def enumerate_pieces_odd(n, ray_img_bound, verbose=False, max_pieces=None):
    """Enumerate all BDI-feasible pieces at odd n with each ray image
    sum <= ray_img_bound. Returns list of matrices."""
    assert n % 2 == 1
    s = aii_struct(n)
    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    n_aii = s["n_vars"]
    rays = aii_rays(n)
    assert len(rays) == 3 * n

    order = _build_ray_order(rays, n_aii)
    aii_idx = {v: i for i, v in enumerate(aii_v)}

    bdi_lattice = enumerate_bdi_lattice(n, ray_img_bound)
    if verbose:
        print(f"  # BDI lattice pts (sum<={ray_img_bound}): {len(bdi_lattice)}")

    # Pre-convert to numpy
    bdi_arrs = [np.array(p, dtype=int) for p in bdi_lattice]

    # Bucket bdi_arrs by ascending sum, for early pruning of ray_image
    # when known has high sum
    bdi_by_sum_lb = defaultdict(list)
    for arr in bdi_arrs:
        bdi_by_sum_lb[int(arr.sum())].append(arr)

    M = np.zeros((n_bdi, n_aii), dtype=int)
    pieces = []

    def dfs(pos):
        if max_pieces is not None and len(pieces) >= max_pieces:
            return
        if pos == len(order):
            pieces.append(M.copy())
            return
        _, iv_name, others_with_coef = order[pos]
        iv_idx = aii_idx[iv_name]
        # Compute "known part" of ray image
        known = np.zeros(n_bdi, dtype=int)
        for v_name, c in others_with_coef.items():
            known += c * M[:, aii_idx[v_name]]
        known_sum = int(known.sum())
        # Ray image must have sum <= bound and >= known componentwise
        # New column = ray_image - known.
        # Iterate over candidate ray images:
        # since ray_image_sum >= known_sum and <= ray_img_bound,
        # filter by sum first.
        for s_total in range(known_sum, ray_img_bound + 1):
            for ray_arr in bdi_by_sum_lb.get(s_total, []):
                # Check ray_arr >= known componentwise
                if np.any(ray_arr < known):
                    continue
                M[:, iv_idx] = ray_arr - known
                dfs(pos + 1)
                if max_pieces is not None and len(pieces) >= max_pieces:
                    M[:, iv_idx] = 0
                    return
        M[:, iv_idx] = 0

    t0 = time.time()
    dfs(0)
    dt = time.time() - t0
    if verbose:
        print(f"  enumerated {len(pieces)} pieces in {dt:.2f}s")
    return pieces, order


# ---------------------------------------------------------------------
# Pieces enumerator (even n)
# ---------------------------------------------------------------------
def enumerate_pieces_even(n, ray_img_bound, verbose=False, max_pieces=None):
    """At even n the cone has 3n-1 rays and 3n vars (linkLHS is a gauge
    direction). We enumerate with linkLHS column fixed to 0 (canonical
    gauge), which uniquely determines the rest from ray images."""
    assert n % 2 == 0
    s = aii_struct(n)
    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    n_aii = s["n_vars"]
    rays = aii_rays(n)
    assert len(rays) == 3 * n - 1

    # GAUGE FIX: linkLHS column = 0.
    # Then short[i] in compound rays (which contain linkLHS) reduces to
    # the same formula as odd n's triple rays without linkLHS.
    # Effectively, set linkLHS column = 0 and absorb it into short[i].

    # Process order: similar to odd n. linkLHS is in ALL the triple/quad
    # rays, so we'd treat it as already "assigned" to 0 from the start.

    # Build order with linkLHS pre-assigned to 0.
    aii_idx = {v: i for i, v in enumerate(aii_v)}
    linkLHS_idx = aii_idx["linkLHS"]

    # Modify _build_ray_order to handle pre-assigned vars
    pre_assigned = {"linkLHS"}
    process_order = []
    assigned = set(pre_assigned)
    # Solo rays first (linkLHS has no solo ray so all real solos process)
    for j, r in enumerate(rays):
        if len(r) == 1:
            v = next(iter(r))
            if v not in assigned:
                process_order.append((j, v, {}))
                assigned.add(v)
    # Compound rays
    remaining = [j for j in range(len(rays))
                 if not (len(rays[j]) == 1 and next(iter(rays[j])) in assigned)
                 and j not in [po[0] for po in process_order]]
    while remaining:
        next_round = []
        progress = False
        for j in remaining:
            r = rays[j]
            unassigned = [v for v in r if v not in assigned]
            if len(unassigned) == 1:
                iv = unassigned[0]
                others = {v: c for v, c in r.items() if v != iv}
                process_order.append((j, iv, others))
                assigned.add(iv)
                progress = True
            else:
                next_round.append(j)
        if not progress:
            raise RuntimeError(f"Cannot decompose rays: {next_round}")
        remaining = next_round
    assert len(assigned) == n_aii, (len(assigned), n_aii)

    bdi_lattice = enumerate_bdi_lattice(n, ray_img_bound)
    if verbose:
        print(f"  # BDI lattice pts (sum<={ray_img_bound}): {len(bdi_lattice)}")
    bdi_arrs = [np.array(p, dtype=int) for p in bdi_lattice]
    bdi_by_sum_lb = defaultdict(list)
    for arr in bdi_arrs:
        bdi_by_sum_lb[int(arr.sum())].append(arr)

    M = np.zeros((n_bdi, n_aii), dtype=int)
    # M[:, linkLHS_idx] = 0 by initialization

    pieces = []

    def dfs(pos):
        if max_pieces is not None and len(pieces) >= max_pieces:
            return
        if pos == len(process_order):
            pieces.append(M.copy())
            return
        _, iv_name, others_with_coef = process_order[pos]
        iv_idx = aii_idx[iv_name]
        known = np.zeros(n_bdi, dtype=int)
        for v_name, c in others_with_coef.items():
            known += c * M[:, aii_idx[v_name]]
        known_sum = int(known.sum())
        for s_total in range(known_sum, ray_img_bound + 1):
            for ray_arr in bdi_by_sum_lb.get(s_total, []):
                if np.any(ray_arr < known):
                    continue
                M[:, iv_idx] = ray_arr - known
                dfs(pos + 1)
                if max_pieces is not None and len(pieces) >= max_pieces:
                    M[:, iv_idx] = 0
                    return
        M[:, iv_idx] = 0

    t0 = time.time()
    dfs(0)
    dt = time.time() - t0
    if verbose:
        print(f"  enumerated {len(pieces)} pieces in {dt:.2f}s")
    return pieces, process_order


# ---------------------------------------------------------------------
# Helper: piece -> JSON (cols by AII var)
# ---------------------------------------------------------------------
def piece_to_dict(M, n):
    s = aii_struct(n)
    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    return {aii_v[c]: [int(M[r, c]) for r in range(n_bdi)]
            for c in range(M.shape[1])}


def piece_signature(M):
    """Hashable signature (tuple of tuples)."""
    return tuple(tuple(int(x) for x in M[:, c]) for c in range(M.shape[1]))


# ---------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------
def compute_stats(pieces, n, label=""):
    """Stats: counts by image sum (per ray); counts by AII coord routing."""
    s = aii_struct(n)
    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    n_aii = s["n_vars"]
    rays = aii_rays(n)
    aii_idx = {v: i for i, v in enumerate(aii_v)}

    # Image sum per piece (for the "total" sum = sum of all entries)
    total_sums = []
    for M in pieces:
        total_sums.append(int(M.sum()))
    sum_counter = defaultdict(int)
    for s_ in total_sums:
        sum_counter[s_] += 1

    # Max ray image sum per piece
    max_ray_sums = []
    for M in pieces:
        max_rs = 0
        for r in rays:
            ray_image = np.zeros(n_bdi, dtype=int)
            for v_name, c in r.items():
                ray_image += c * M[:, aii_idx[v_name]]
            max_rs = max(max_rs, int(ray_image.sum()))
        max_ray_sums.append(max_rs)

    # # distinct routings per AII var
    routings_per_var = {}
    for c, av in enumerate(aii_v):
        cols = set()
        for M in pieces:
            cols.add(tuple(int(M[r, c]) for r in range(n_bdi)))
        routings_per_var[av] = len(cols)

    return {
        "label": label,
        "n_pieces": len(pieces),
        "total_sum_distribution": dict(sorted(sum_counter.items())),
        "max_ray_sum_distribution": dict(sorted(
            (k, max_ray_sums.count(k))
            for k in sorted(set(max_ray_sums))
        )),
        "routings_per_aii_var": routings_per_var,
    }


# ---------------------------------------------------------------------
# Acceptance checks
# ---------------------------------------------------------------------
def load_day70_registry(n):
    """Load the Day-70 registry as a dict {name: M_matrix}."""
    if n == 5:
        reg_path = Path("/home/agent/projects/code/2026-06-13-n5-axis-count/n5_registry.json")
    else:
        reg_path = Path(f"/home/agent/projects/code/2026-06-15-axis-n6-n7-count/n{n}_registry.json")
    with open(reg_path) as f:
        reg = json.load(f)
    s = aii_struct(n)
    aii_v = s["vars"]
    bv = bdi_vars(n)
    n_bdi = len(bv)
    n_aii = s["n_vars"]
    pieces = {}
    for name, cols in reg.items():
        M = np.zeros((n_bdi, n_aii), dtype=int)
        for av_name, col in cols.items():
            c = aii_v.index(av_name)
            for r in range(n_bdi):
                M[r, c] = col[r]
        pieces[name] = M
    return pieces


def build_simple_divert(n, i, alpha):
    """Build the Day-71 simple-divert piece pi_alpha^{(i)} = base + (alpha,
    p_i) added to S column."""
    sys.path.insert(0, '/home/agent/projects/code/2026-06-16-dpi-refutation-verify')
    from verify_3clique import build_pi_alpha
    s = aii_struct(n)
    spec = build_pi_alpha(n, i, alpha)
    return piece_matrix(spec, s)


def check_inclusion(my_pieces, target_pieces_dict, n, label=""):
    """Check that each target piece is in my_pieces."""
    my_sigs = set(piece_signature(M) for M in my_pieces)
    results = {}
    for name, M in target_pieces_dict.items():
        sig = piece_signature(M)
        results[name] = (sig in my_sigs)
    n_in = sum(1 for v in results.values() if v)
    return {
        "label": label,
        "n_target": len(target_pieces_dict),
        "n_in_registry": n_in,
        "missing": [name for name, v in results.items() if not v],
    }


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    out_dir = Path("/home/agent/projects/code/2026-06-17-complete-registry")
    out_dir.mkdir(exist_ok=True)

    all_runs = {}

    # First sanity-check AII rays.
    for n in [5, 6, 7]:
        rays = aii_rays(n)
        expected = 3 * n - (1 if n % 2 == 0 else 0)
        print(f"n={n}: # rays = {len(rays)} (expected {expected})  "
              f"{'OK' if len(rays) == expected else 'MISMATCH'}")
        assert len(rays) == expected

    # n=5
    print(f"\n{'='*70}")
    print(f"n = 5 (odd)")
    print(f"{'='*70}")
    day70_n5 = load_day70_registry(5)
    n5_runs = {}
    for N in [2, 3, 4]:
        print(f"\n--- n=5, ray_img_bound = {N} ---")
        pieces, order = enumerate_pieces_odd(5, N, verbose=True,
                                              max_pieces=200_000)
        st = compute_stats(pieces, 5, label=f"n=5, N={N}")
        # Coverage check
        cov_day70 = check_inclusion(pieces, day70_n5, 5,
                                     "Day-70 n=5 registry")
        sd_pieces = {f"pi_a{a}_i{i}": build_simple_divert(5, i, a)
                     for i in range(2, 5 - 1) for a in (0, 1, 2)}
        cov_sd = check_inclusion(pieces, sd_pieces, 5,
                                   "Day-71 simple-divert n=5")
        n5_runs[N] = {
            "stats": st,
            "coverage_day70": cov_day70,
            "coverage_simple_divert": cov_sd,
        }
        print(f"  -> Day-70 covered: {cov_day70['n_in_registry']}/{cov_day70['n_target']}")
        if cov_day70["missing"]:
            print(f"     missing: {cov_day70['missing'][:5]}")
        print(f"  -> Simple-divert covered: {cov_sd['n_in_registry']}/{cov_sd['n_target']}")
        if cov_sd["missing"]:
            print(f"     missing: {cov_sd['missing'][:5]}")

    all_runs["n5"] = n5_runs

    # n=6
    print(f"\n{'='*70}")
    print(f"n = 6 (even, gauge linkLHS=0)")
    print(f"{'='*70}")
    day70_n6 = load_day70_registry(6)
    n6_runs = {}
    for N in [2, 3, 4]:
        print(f"\n--- n=6, ray_img_bound = {N} ---")
        pieces, order = enumerate_pieces_even(6, N, verbose=True,
                                                max_pieces=200_000)
        st = compute_stats(pieces, 6, label=f"n=6, N={N}")
        # Note: Day-70 pieces have linkLHS != 0 in general. We need to
        # gauge them down. The gauge transform: linkLHS col -> 0,
        # short[i] col -> short[i] col + linkLHS col for each i in 1..n-1.
        # (since linkLHS = sum(short[i]), adding v to linkLHS is the same
        # as adding v to each short[i] on feasible points.)
        # Wait, that's not right. Let me think.
        # If linkLHS = sum_i short[i], and M' = M with linkLHS col reduced
        # by v and short[i] cols increased by v for each i, then on
        # feasible p:
        # M'p = Mp + (sum_i short[i] - linkLHS) * v = Mp.
        # So M' is gauge-equivalent.
        # Therefore, to canonicalize: set new_linkLHS_col = 0; then
        # for each short[i] col: new_short[i] = old_short[i] + old_linkLHS.
        def gauge_to_zero_linkLHS(M):
            s = aii_struct(6)
            aii_v = s["vars"]
            llh_idx = aii_v.index("linkLHS")
            short_idxs = [aii_v.index(f"short[{i}]") for i in range(1, 6)]
            llh_col = M[:, llh_idx].copy()
            M2 = M.copy()
            M2[:, llh_idx] = 0
            for si in short_idxs:
                M2[:, si] = M2[:, si] + llh_col
            return M2
        day70_n6_gauged = {name: gauge_to_zero_linkLHS(M)
                            for name, M in day70_n6.items()}
        cov_day70 = check_inclusion(pieces, day70_n6_gauged, 6,
                                     "Day-70 n=6 registry (gauged)")
        sd_pieces_raw = {f"pi_a{a}_i{i}": build_simple_divert(6, i, a)
                          for i in range(2, 6 - 1) for a in (0, 1, 2)}
        sd_pieces_gauged = {name: gauge_to_zero_linkLHS(M)
                             for name, M in sd_pieces_raw.items()}
        cov_sd = check_inclusion(pieces, sd_pieces_gauged, 6,
                                   "Day-71 simple-divert n=6 (gauged)")
        n6_runs[N] = {
            "stats": st,
            "coverage_day70": cov_day70,
            "coverage_simple_divert": cov_sd,
        }
        print(f"  -> Day-70 covered: {cov_day70['n_in_registry']}/{cov_day70['n_target']}")
        if cov_day70["missing"]:
            print(f"     missing: {cov_day70['missing'][:5]}")
        print(f"  -> Simple-divert covered: {cov_sd['n_in_registry']}/{cov_sd['n_target']}")
        if cov_sd["missing"]:
            print(f"     missing: {cov_sd['missing'][:5]}")

    all_runs["n6"] = n6_runs

    # Save
    with open(out_dir / "results.json", "w") as f:
        json.dump(all_runs, f, indent=2, default=str)
    print(f"\nsaved results.json to {out_dir}")


if __name__ == "__main__":
    main()
