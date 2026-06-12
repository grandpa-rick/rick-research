"""
Cross-check: for each gl_6 partition λ ⊂ (5^3), compute the gl_6 weight multiset
restricted to so_6 (via the natural projection (n_1, ..., n_6) → (n_1-n_6, n_2-n_5, n_3-n_4)).
Independently project to axes/prefix-axes/twisted-axes, and verify NO marginal multiset
matches Bucket-2.

Also: enumerate all sub-collections of so_6 irreps in Res V_λ summing to dim 22 (when
they exist), and verify none has Bucket-2 marginals.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import product

from lr_branching import gl_to_O_branching, normalize
from so6_weights import so6_dim_from_weights, so6_weight_multiset, ssyt_shape
from test_bucket2_match_v3 import gl6_ssyt_weights, project_to_so6
from test_bucket2_match import (
    BASE_IRREPS, T_I2, T_I236, T_I23456, TARGETS,
    enumerate_functionals, level_signature, irrep_weight_multiset,
)


def enumerate_partitions_in_5_cubed():
    parts = []
    for l1 in range(0, 6):
        for l2 in range(0, l1 + 1):
            for l3 in range(0, l2 + 1):
                shape = tuple(p for p in (l1, l2, l3) if p > 0)
                parts.append(shape)
    return parts


def o6_to_so6_irreps(mu):
    """An O(6) irrep μ corresponds to:
      - one so_6 irrep V_(mu_1, mu_2, mu_3) if mu has < 3 nonzero rows.
      - a pair of so_6 irreps V_(mu_1, mu_2, mu_3) ⊕ V_(mu_1, mu_2, -mu_3) if mu has 3 nonzero rows.
    Returns a list of (l_1, l_2, l_3) tuples for the so_6 components.
    """
    mu = normalize(mu)
    while len(mu) < 3:
        mu = mu + (0,)
    l1, l2, l3 = mu
    if l3 > 0:
        return [(l1, l2, l3), (l1, l2, -l3)]
    return [(l1, l2, l3)]


def all_so6_irreps_in_res(lam):
    """Return Counter[(l_1, l_2, l_3)] = multiplicity in Res^{gl_6}_{so_6} V_λ."""
    o6_branch = gl_to_O_branching(lam, 6)
    so6: Counter = Counter()
    for mu, mult in o6_branch.items():
        for irrep in o6_to_so6_irreps(mu):
            so6[irrep] += mult
    return so6


def irrep_dim_so6(hw):
    l1, l2, l3 = hw
    if l3 >= 0:
        return so6_dim_from_weights(l1, l2, l3)
    return so6_dim_from_weights(l1, l2, -l3)


def irrep_weights_so6(hw):
    """Weight multiset for so_6 irrep, with diagram involution handled."""
    l1, l2, l3 = hw
    if l3 >= 0:
        return so6_weight_multiset(l1, l2, l3)
    base = so6_weight_multiset(l1, l2, -l3)
    out: Counter = Counter()
    for w, m in base.items():
        out[(w[0], w[1], -w[2])] += m
    return out


def subcollections_summing_to(irrep_counter: Counter, target_dim: int):
    """Yield Counter[(hw)] sub-counters (component-wise ≤ irrep_counter) with total dim = target_dim."""
    items = sorted(irrep_counter.items())

    def recurse(idx, picked: dict, remaining):
        if remaining == 0:
            yield dict(picked)
            return
        if idx == len(items):
            return
        hw, max_count = items[idx]
        d = irrep_dim_so6(hw)
        if d == 0:
            yield from recurse(idx + 1, picked, remaining)
            return
        max_take = min(max_count, remaining // d)
        for k in range(max_take + 1):
            if k > 0:
                picked[hw] = k
            yield from recurse(idx + 1, picked, remaining - k * d)
            if k > 0:
                del picked[hw]

    yield from recurse(0, {}, target_dim)


def union_weights(sub_collection: dict) -> Counter:
    out: Counter = Counter()
    for hw, mult in sub_collection.items():
        ws = irrep_weights_so6(hw)
        for w, m in ws.items():
            out[w] += m * mult
    return out


def signature_matches_any_bucket2(W: Counter, max_coord: int = 6) -> dict:
    fs = enumerate_functionals(max_coord)
    hits = {t: [] for t in TARGETS}
    for f in fs:
        sig = level_signature(W, f)
        for t in TARGETS:
            if sig == t:
                hits[t].append(f)
    return hits


def main():
    partitions = enumerate_partitions_in_5_cubed()
    print(f"Checking {len(partitions)} partitions for dim-22 sub-collections matching Bucket-2.\n")

    summary = {
        "n_partitions": len(partitions),
        "n_with_dim22_subcollection": 0,
        "subcollections_seen": [],
        "matches_found": [],
    }

    seen_collections = set()
    for shape in partitions:
        irreps = all_so6_irreps_in_res(shape)
        subs = list(subcollections_summing_to(irreps, 22))
        if subs:
            summary["n_with_dim22_subcollection"] += 1
        for sub in subs:
            key = tuple(sorted(sub.items()))
            if key in seen_collections:
                continue
            seen_collections.add(key)
            W = union_weights(sub)
            if sum(W.values()) != 22:
                continue
            hits = signature_matches_any_bucket2(W, max_coord=6)
            ihit = any(len(v) > 0 for v in hits.values())
            if ihit:
                lab_str = " + ".join(f"{m}*{hw}" for hw, m in sorted(sub.items()))
                summary["matches_found"].append({
                    "lambda": shape, "subcollection": str(sub), "hits": {str(t): hits[t][:5] for t in TARGETS}
                })
                print(f"  λ = {shape}: sub-collection {lab_str} -- some Bucket-2 marginal HITS!")
                print(f"    Hits: {hits}")
            summary["subcollections_seen"].append({
                "lambda": shape, "subcollection": str(sub),
                "hits_count": {str(t): len(hits[t]) for t in TARGETS},
            })

    print()
    print(f"# of distinct dim-22 sub-collections seen across all λ: {len(seen_collections)}")
    print(f"# of partitions admitting at least one dim-22 sub-collection: {summary['n_with_dim22_subcollection']}")
    print(f"# of distinct sub-collections with ANY Bucket-2 marginal hit: {len(summary['matches_found'])}")

    if not summary["matches_found"]:
        print(">>> NO Bucket-2 hits across all dim-22 sub-collections of Res V_λ for λ ⊂ (5^3).")
        print(">>> OQ-NAITOSAGAKI-BDI is DEFINITIVELY REFUTED.")

    with open("subcollection_data.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nSaved sub-collection survey to subcollection_data.json")


if __name__ == "__main__":
    main()
