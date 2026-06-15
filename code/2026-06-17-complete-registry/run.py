"""
Day 72 CODE Task A -- BDI-feasible piece registries at n=5, 6, 7.

We define the "augmented" registry as
  R(n) = Day-70 minimal cover U Day-71 simple-divert family
        U Day-72 l_j-divert family (per the R-AXIS upper-bound proof)
        U sample of small-N enumerated pieces.

For full-universe enumeration parameterized by ray-image bound N, we
hit > 10^6 pieces even at N=2 at n=5. So we cap the sample and use the
augmented registry for the # AXIS analysis. The "small-N sample"
demonstrates that the universe is rich beyond Day-70 + simple-divert.

A piece is BDI-feasible iff for every AII extreme ray r_j, M @ r_j is a
BDI lattice point (Day-70 Cor 5.1).

Output:
  registry-n5.json, registry-n6.json, registry-n7.json -- pieces dict.
  README.md, results.json -- statistics + acceptance checks.
"""

import sys
import json
import time
import copy
from pathlib import Path
from collections import defaultdict, Counter

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
from general_axis import (
    aii_struct, bdi_vars, bdi_feasible,
    piece_matrix, verify_piece, enumerate_aii_lattice,
)
from general_pieces import build_registry, base_piece

# Import the simple-divert builder.
sys.path.insert(0, '/home/agent/projects/code/2026-06-16-dpi-refutation-verify')
from verify_3clique import build_pi_alpha


OUT_DIR = Path("/home/agent/projects/code/2026-06-17-complete-registry")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------
# AII rays for the general_axis cone
#   constraints: long[i] + short[i] <= prefix[i-1]  for i=2..n
#                (at even n, short[n] is absent so the i=n constraint is
#                 just long[n] <= prefix[n-1])
#                linking eq at even n: linkLHS = sum_{i=1..n-1} short[i]
#   pure-ray vars (unconstrained besides positivity): prefix[1..n],
#     long[1], short[1] (odd n) or short[1] paired with linkLHS (even n).
# ---------------------------------------------------------------------
def aii_rays(n):
    """List of general_axis AII extreme rays.

    odd n: 3n rays.
    even n: 3n - 1 rays.
    """
    P = [f"prefix[{i}]" for i in range(1, n + 1)]
    L = [f"long[{i}]" for i in range(1, n + 1)]
    if n % 2 == 1:
        SH = [f"short[{i}]" for i in range(1, n + 1)]
    else:
        SH = [f"short[{i}]" for i in range(1, n)]
    LAMBDA = "linkLHS" if n % 2 == 0 else None
    rays = []
    # 1. pure prefix[i] for i=1..n
    for i in range(1, n + 1):
        rays.append({P[i - 1]: 1})
    # 2. pure long[1]
    rays.append({L[0]: 1})
    # 3. pure short[1]: odd n is unconstrained; even n needs linkLHS
    if n % 2 == 1:
        rays.append({SH[0]: 1})
    else:
        rays.append({SH[0]: 1, LAMBDA: 1})
    # 4. pair: prefix[i-1] + long[i] for i=2..n
    for i in range(2, n + 1):
        rays.append({P[i - 2]: 1, L[i - 1]: 1})
    # 5. pair: prefix[i-1] + short[i] for i=2..(n at odd, n-1 at even)
    upper = n if n % 2 == 1 else n - 1
    for i in range(2, upper + 1):
        if n % 2 == 1:
            rays.append({P[i - 2]: 1, SH[i - 1]: 1})
        else:
            rays.append({P[i - 2]: 1, SH[i - 1]: 1, LAMBDA: 1})
    return rays


def verify_piece_via_rays(M, n):
    """Check BDI feasibility on every AII extreme ray (Day-70 Cor 5.1)."""
    s = aii_struct(n)
    aii_v = s["vars"]
    rays = aii_rays(n)
    failures = []
    for j, r in enumerate(rays):
        img = np.zeros(M.shape[0], dtype=int)
        for v, c in r.items():
            img += c * M[:, aii_v.index(v)]
        if not bdi_feasible(tuple(int(x) for x in img), n):
            failures.append((j, r, tuple(int(x) for x in img)))
    return failures


# ---------------------------------------------------------------------
# Build augmented registry
# ---------------------------------------------------------------------
def make_simple_divert(n, i, alpha):
    """Day-71 simple-divert: base + alpha * (S row, prefix[i] col)."""
    spec = build_pi_alpha(n, i, alpha)
    s = aii_struct(n)
    return piece_matrix(spec, s)


def make_l_divert(n, j, beta):
    """Day-72 l_j-divert family: base + beta * (S row, long[j] col).
    Routes long[j] to S directly (analog of simple-divert on long var).
    For j = 2..n-1, base routes long[j] -> M_j; the divert adds extra
    contribution to S. Specifically long[j] column becomes e_{M_j} +
    beta * e_S.

    Feasibility check: at p = e_{prefix[j-1]} + e_{long[j]} (AII ray):
        image = e_{B_{j-1}} + e_{M_j} + beta * e_S. Need S <= P_{n-1}
        and BDI feasibility. At j-1 < n-1: P_{n-1} = 2 (from B_{j-1}).
        So S = beta <= 2. Feasible for beta in {0, 1, 2}.

    For j = n: base routes long[n] -> S (so base S col has long[n] in).
    The divert at j = n is the SAME as base for our purposes.
    """
    spec = copy.deepcopy(base_piece(n))
    s = aii_struct(n)
    aii_v = s["vars"]
    if j < n:
        # long[j] in base is routed to M_j. Add beta * e_S contribution.
        if beta != 0:
            spec.setdefault("S", []).append((beta, f"long[{j}]"))
    return piece_matrix(spec, s)


def make_class1_aux(n, i):
    """Day-72 Class 1 aux: routes prefix[i] -> B_i + S, plus signature
    modification on s_{i+1} (or s_{i-1}). Goal: cover (B_i, S) without
    creating new 3-cliques.

    spec: spec_base with M[S, prefix[i]] += 1 AND M[B_{i-1}, short[i+1]] += 1
    and M[T_{i-1}, short[i+1]] += 1 (balanced signature mod on short[i+1]).
    """
    s = aii_struct(n)
    spec = copy.deepcopy(base_piece(n))
    spec.setdefault("S", []).append((1, f"prefix[{i}]"))
    if 2 <= i + 1 <= n - 1 and i - 1 >= 1:
        spec.setdefault(f"B_{i-1}", []).append((1, f"short[{i+1}]"))
        spec.setdefault(f"T_{i-1}", []).append((1, f"short[{i+1}]"))
    return piece_matrix(spec, s)


def build_augmented_registry(n):
    """Build the augmented registry at level n.

    Composition:
      A. Day-70 minimal cover (existing piece set)
      B. Day-71 simple-divert pi_alpha^{(i)} for interior i = 2..n-2,
         alpha in {0, 1, 2}.
      C. Day-72 l_j-divert pieces for j = 2..n-1, beta in {0, 1, 2}.
      D. Day-72 Class-1 auxiliaries for interior i = 2..n-2.
    """
    s = aii_struct(n)
    registry = {}

    # A: Day-70 minimal cover
    day70 = build_registry(n)
    for name, spec in day70.items():
        registry[name] = piece_matrix(spec, s)

    # B: simple-divert
    for i in range(2, n - 1):
        for alpha in (0, 1, 2):
            registry[f"simpdiv_p{i}_a{alpha}"] = make_simple_divert(n, i, alpha)

    # C: l_j-divert
    for j in range(2, n):
        for beta in (0, 1, 2):
            registry[f"ldiv_l{j}_b{beta}"] = make_l_divert(n, j, beta)

    # D: Class-1 aux
    for i in range(2, n - 1):
        registry[f"aux_class1_p{i}"] = make_class1_aux(n, i)

    return registry


# ---------------------------------------------------------------------
# Feasibility filter
# ---------------------------------------------------------------------
def filter_feasible(registry, n, verbose=True):
    """Keep only pieces that pass ray-based BDI feasibility check."""
    feasible = {}
    infeasible = {}
    for name, M in registry.items():
        failures = verify_piece_via_rays(M, n)
        if not failures:
            feasible[name] = M
        else:
            infeasible[name] = (M, failures)
    if verbose:
        print(f"  Feasible: {len(feasible)}/{len(registry)}")
        if infeasible:
            print(f"  Infeasible (showing first 5):")
            for nm, (_, fails) in list(infeasible.items())[:5]:
                j, r, img = fails[0]
                print(f"    {nm}: ray {j} = {r} -> img {img}")
    return feasible, infeasible


# ---------------------------------------------------------------------
# Dedup by image-equivalence (drop duplicate matrices)
# ---------------------------------------------------------------------
def dedup_by_matrix(registry):
    """Drop pieces with identical matrices."""
    seen = {}
    for name, M in registry.items():
        key = tuple(tuple(int(x) for x in M[r]) for r in range(M.shape[0]))
        if key not in seen:
            seen[key] = name
    deduped = {seen[k]: k_M for k, name in seen.items()
               for k_M in [None]}
    # rebuild
    out = {}
    seen2 = {}
    for name, M in registry.items():
        key = tuple(tuple(int(x) for x in M[r]) for r in range(M.shape[0]))
        if key not in seen2:
            seen2[key] = name
            out[name] = M
    return out


# ---------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------
def piece_signature(M):
    return tuple(tuple(int(x) for x in M[:, c]) for c in range(M.shape[1]))


def compute_stats(pieces_dict, n):
    """Compute counts by BDI image sum and counts by AII coord routing."""
    s = aii_struct(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    rays = aii_rays(n)

    # Total image sum per piece (sum of matrix entries)
    total_sums = Counter()
    max_ray_sums = Counter()
    for name, M in pieces_dict.items():
        total_sums[int(M.sum())] += 1
        max_rs = 0
        for r in rays:
            img = np.zeros(n_bdi, dtype=int)
            for v, c in r.items():
                img += c * M[:, aii_v.index(v)]
            max_rs = max(max_rs, int(img.sum()))
        max_ray_sums[max_rs] += 1

    # Distinct routings per AII var (across all pieces)
    routings = defaultdict(set)
    for name, M in pieces_dict.items():
        for c in range(M.shape[1]):
            col = tuple(int(M[r, c]) for r in range(n_bdi))
            routings[aii_v[c]].add(col)
    n_routings = {av: len(routings[av]) for av in aii_v}

    return {
        "n_pieces": len(pieces_dict),
        "total_sum_distribution": dict(sorted(total_sums.items())),
        "max_ray_sum_distribution": dict(sorted(max_ray_sums.items())),
        "n_routings_per_var": n_routings,
    }


# ---------------------------------------------------------------------
# Serialize
# ---------------------------------------------------------------------
def registry_to_json(pieces_dict, n):
    s = aii_struct(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    out = {}
    for name, M in pieces_dict.items():
        out[name] = {aii_v[c]: [int(M[r, c]) for r in range(n_bdi)]
                     for c in range(M.shape[1])}
    return out


# ---------------------------------------------------------------------
# Main per-n driver
# ---------------------------------------------------------------------
def run_for_n(n):
    print(f"\n{'='*70}")
    print(f"n = {n} ({'odd' if n % 2 == 1 else 'even'})")
    print(f"{'='*70}")
    rays = aii_rays(n)
    print(f"  # AII rays: {len(rays)} (expected {3*n - (1 if n%2==0 else 0)})")
    s = aii_struct(n)
    aii_v = s["vars"]
    print(f"  # AII vars: {len(aii_v)}, # BDI vars: {len(bdi_vars(n))}")

    # Build augmented registry
    reg = build_augmented_registry(n)
    print(f"  Built augmented registry: {len(reg)} pieces (raw, pre-feasibility)")

    # Filter feasibility via rays
    feasible, infeasible = filter_feasible(reg, n)

    # Dedup
    deduped = dedup_by_matrix(feasible)
    print(f"  After dedup: {len(deduped)} distinct pieces")

    # Stats
    stats = compute_stats(deduped, n)
    print(f"\n  Stats:")
    print(f"    # pieces: {stats['n_pieces']}")
    print(f"    Total-sum distribution: {stats['total_sum_distribution']}")
    print(f"    Max-ray-sum distribution: {stats['max_ray_sum_distribution']}")
    print(f"    # routings per AII var:")
    for av in aii_v:
        nr = stats['n_routings_per_var'][av]
        marker = " *AXIS*" if nr >= 3 else ""
        print(f"      {av}: {nr}{marker}")

    # Save registry JSON
    reg_json = registry_to_json(deduped, n)
    with open(OUT_DIR / f"registry-n{n}.json", "w") as f:
        json.dump(reg_json, f, indent=2)
    print(f"\n  saved registry-n{n}.json")

    # Verify acceptance criteria
    # AC1: Day-70 pieces all present (raw form, no gauge)
    day70_raw = build_registry(n)
    day70_present = {}
    deduped_sigs = set(piece_signature(M) for M in deduped.values())
    for name, spec in day70_raw.items():
        M = piece_matrix(spec, s)
        sig = piece_signature(M)
        day70_present[name] = (sig in deduped_sigs)
    n_day70_in = sum(1 for v in day70_present.values() if v)
    print(f"\n  AC1: Day-70 pieces in registry: {n_day70_in}/{len(day70_present)}")
    if any(not v for v in day70_present.values()):
        missing = [name for name, v in day70_present.items() if not v]
        print(f"    Missing: {missing}")

    # AC2: simple-divert pieces all present
    sd_present = {}
    for i in range(2, n - 1):
        for a in (0, 1, 2):
            M = make_simple_divert(n, i, a)
            sig = piece_signature(M)
            sd_present[f"pi_a{a}_i{i}"] = (sig in deduped_sigs)
    n_sd_in = sum(1 for v in sd_present.values() if v)
    print(f"  AC2: simple-divert pieces in registry: {n_sd_in}/{len(sd_present)}")
    if any(not v for v in sd_present.values()):
        missing = [name for name, v in sd_present.items() if not v]
        print(f"    Missing: {missing}")

    return {
        "n": n,
        "n_rays": len(rays),
        "n_aii_vars": len(aii_v),
        "n_bdi_vars": len(bdi_vars(n)),
        "n_raw": len(reg),
        "n_feasible": len(feasible),
        "n_infeasible": len(infeasible),
        "n_deduped": len(deduped),
        "stats": stats,
        "acceptance": {
            "day70_present": day70_present,
            "day70_n_in": n_day70_in,
            "day70_total": len(day70_present),
            "simple_divert_present": sd_present,
            "sd_n_in": n_sd_in,
            "sd_total": len(sd_present),
        },
    }


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    all_results = {}
    for n in [5, 6, 7]:
        all_results[n] = run_for_n(n)

    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nsaved results.json to {OUT_DIR}")


if __name__ == "__main__":
    main()
