"""
Day 73 CODE Task A -- Class 3 + Class 4 auxiliaries at n = 5.

CONTEXT (Day-72 PROVE §4.3):
  Class 1 (R-double aux, BDI gap {B_i, S}): 3 cases, verified Day-72.
  Class 2 (free-tail-shift aux, BDI gap {B_i, 2S}): 3 cases, verified
    Day-72.
  Class 3 (misaligned {M_j, B_i} for i != j-1): ~9 cases, sketched.
  Class 4 (cross-modify {B_i, T_i}, i=2,3): 2 cases, sketched.

This script:
  1. Enumerate all Class-3 aux pieces (one per misaligned (M_j, B_i)).
  2. Enumerate Class-4 aux pieces ({B_2, T_2} and {B_3, T_3}).
  3. Verify each is BDI-feasible on every AII ray.
  4. Verify each has the predicted image: image at the targeted AII point
     equals the targeted BDI gap point modulo "extra" content.
  5. Verify UNIQUE signatures: no two aux have the same "differs-from-
     base" column set.
  6. Verify Lemma 4.3: combined registry (AXIS + Class 1 + 2 + 3 + 4)
     has NO new 3-clique on a non-AXIS wall.

CONSTRUCTION (Class 3):
  For misaligned pair (M_j, B_i), i in {1..4}, j in {2..4}, i != j-1:
    Use l_{i+1} as the engine.  Rewire l_{i+1} col so M_{i+1} row
    becomes 0 and M_j row becomes 1.  Hence at p = e_{p_i} + e_{l_{i+1}}
    (AII-feasible since l_{i+1} = 1 <= p_i = 1), image = e_{B_i} +
    e_{M_j}.

    To keep signature UNIQUE, also flip a balanced (B_k, T_k) entry on
    a unique adjacent s_k.

CONSTRUCTION (Class 4):
  For (B_i, T_i), i in {2, 3}: zero out p_{i-1} and l_i columns of base.
  Then at p = e_{p_{i-1}} + e_{s_i}: image = base s_i col = e_{B_i} +
  e_{T_i}.  (Signature: (p_{i-1}, l_i), pair zero.)
"""

from __future__ import annotations

import sys
import json
import copy
import itertools
from pathlib import Path
from collections import defaultdict

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-15-axis-n6-n7-count')
sys.path.insert(0, '/home/agent/projects/code/2026-06-17-complete-registry')

from general_axis import (
    aii_struct, bdi_vars, bdi_feasible, piece_matrix,
)
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "day72_registry_run",
    "/home/agent/projects/code/2026-06-17-complete-registry/run.py")
_day72 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day72)
aii_rays = _day72.aii_rays
build_augmented_registry = _day72.build_augmented_registry
filter_feasible = _day72.filter_feasible

from general_pieces import base_piece


N = 5
OUT_DIR = Path("/home/agent/projects/code/2026-06-18-class34-aux-n5")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------
# Piece construction helpers
# ---------------------------------------------------------------------
def spec_to_matrix(spec, n):
    s = aii_struct(n)
    return piece_matrix(spec, s)


def zero_col_spec(spec, aii_var):
    """Remove every term referring to `aii_var` from spec."""
    out = {}
    for bv, terms in spec.items():
        kept = [t for t in terms if t[1] != aii_var]
        if kept:
            out[bv] = kept
    return out


def set_col_spec(spec, aii_var, bdi_dict):
    """Set the column for `aii_var` to `bdi_dict` ({bdi_var: coef})."""
    out = zero_col_spec(spec, aii_var)
    for bv, coef in bdi_dict.items():
        if coef != 0:
            out.setdefault(bv, []).append((coef, aii_var))
    return out


# ---------------------------------------------------------------------
# Class 3: misaligned (M_j, B_i)
# ---------------------------------------------------------------------
def build_class3_aux(j, i, signature_var):
    """Class-3 aux for misaligned (M_j, B_i), i != j-1.
    Uses l_{i+1} engine and a unique signature on s_k (signature_var)."""
    n = N
    spec = copy.deepcopy(base_piece(n))
    # Rewire l_{i+1}: zero out base routing (which is M_{i+1} for i+1 in
    # 2..n-1, or S for i+1 = n).  Then set l_{i+1} col = e_{M_j}.
    l_engine = f"long[{i+1}]"
    spec = set_col_spec(spec, l_engine, {f"M_{j}": 1})

    # Add unique signature on signature_var: balanced extra (B_k, T_k)
    # pair, with k chosen to keep feasibility.
    if signature_var is not None:
        sk = signature_var  # AII var name (e.g. "short[2]")
        # Add a balanced contribution: B_a += 1, T_a += 1 for chosen a.
        # `signature_aii` maps each signature_var to an (a) it adds to.
        # We pick a different a per pair to ensure unique signatures.
        # See `class3_pairs_with_signatures` below.
        pass  # signature applied via the caller
    return spec


def make_class3_aux(j, i, sig_short, sig_bt_a):
    """Class-3 aux: misaligned (M_j, B_i) with unique-signature
    modification (sig_short, sig_bt_a):
      add (1, sig_short) to B_{sig_bt_a} and T_{sig_bt_a}.
    """
    n = N
    spec = copy.deepcopy(base_piece(n))
    l_engine = f"long[{i+1}]"
    if i + 1 < n:
        # base l_{i+1} col = e_{M_{i+1}}; replace with e_{M_j}
        spec = set_col_spec(spec, l_engine, {f"M_{j}": 1})
    else:
        # i+1 == n: base l_n col = e_S; replace with e_{M_j}
        spec = set_col_spec(spec, l_engine, {f"M_{j}": 1})
    # Apply signature: balanced (B_a, T_a) added on sig_short col.
    if sig_short is not None:
        spec.setdefault(f"B_{sig_bt_a}", []).append((1, sig_short))
        spec.setdefault(f"T_{sig_bt_a}", []).append((1, sig_short))
    return spec


# ---------------------------------------------------------------------
# Class 4: cross-modify {B_i, T_i}
# ---------------------------------------------------------------------
def make_class4_aux(i):
    """Class-4 aux for (B_i, T_i), i in {2, 3}.
    Zero out p_{i-1} col and l_i col of base."""
    n = N
    spec = copy.deepcopy(base_piece(n))
    spec = zero_col_spec(spec, f"prefix[{i-1}]")
    spec = zero_col_spec(spec, f"long[{i}]")
    return spec


# ---------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------
def verify_ray_feasibility(M, n):
    """Check BDI-feasibility on every AII ray (Day-70 Cor 5.1)."""
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


def column_signature(M, base_M, n):
    """Return tuple of AII vars where M's column != base_M's column."""
    s = aii_struct(n)
    aii_v = s["vars"]
    diff = []
    for c, av in enumerate(aii_v):
        if not np.array_equal(M[:, c], base_M[:, c]):
            diff.append(av)
    return tuple(diff)


def target_image(M, target_aii_pt, n):
    """Return image of target_aii_pt = dict {aii_var: count} under M.
    Used to verify aux hits the targeted BDI gap point."""
    s = aii_struct(n)
    aii_v = s["vars"]
    img = np.zeros(M.shape[0], dtype=int)
    for v, c in target_aii_pt.items():
        img += c * M[:, aii_v.index(v)]
    return tuple(int(x) for x in img)


def find_3cliques_on_walls(pieces_dict, n):
    """Find all 3-cliques (a, b, c) such that a, b, c pairwise differ
    on the SAME single AII column.  Return list of (a, b, c, axis)."""
    s = aii_struct(n)
    aii_v = s["vars"]
    n_aii = len(aii_v)
    names = list(pieces_dict.keys())
    mats = pieces_dict
    triples = []
    for a, b, c in itertools.combinations(names, 3):
        Ma, Mb, Mc = mats[a], mats[b], mats[c]
        cols_ab = [j for j in range(n_aii) if not np.array_equal(Ma[:, j], Mb[:, j])]
        cols_bc = [j for j in range(n_aii) if not np.array_equal(Mb[:, j], Mc[:, j])]
        cols_ac = [j for j in range(n_aii) if not np.array_equal(Ma[:, j], Mc[:, j])]
        if (len(cols_ab) == 1 and len(cols_bc) == 1 and len(cols_ac) == 1
                and cols_ab == cols_bc == cols_ac):
            col = cols_ab[0]
            cs = {tuple(Ma[:, col]), tuple(Mb[:, col]), tuple(Mc[:, col])}
            if len(cs) == 3:
                triples.append((a, b, c, aii_v[col]))
    return triples


# ---------------------------------------------------------------------
# Class 3 enumeration: all misaligned (M_j, B_i) at n=5
# ---------------------------------------------------------------------
def class3_pairs():
    """All (j, i) with j in {2..n-1}, i in {1..n-1}, i != j-1.

    For each pair, choose a UNIQUE signature (sig_short, sig_bt_a) so
    that no two aux pieces share the same signature.
    """
    pairs = []
    # Assign signature based on pair index for uniqueness.
    sig_options = []
    # The signature is (s_k, BT_a) — pick k != engine adjacency and
    # a in {1..n-1}.  We'll just pick k = j (so s_j-mod), a = i.
    # Two pairs differ iff (j, i) differ, so this gives unique sigs.
    for j in range(2, N):       # j = 2, 3, 4
        for i in range(1, N):   # i = 1, 2, 3, 4
            if i == j - 1:      # aligned, skip
                continue
            sig_short = f"short[{j}]"
            sig_bt_a = i  # in {1..4}
            pairs.append((j, i, sig_short, sig_bt_a))
    return pairs


# ---------------------------------------------------------------------
# Test target images for each pair
# ---------------------------------------------------------------------
def target_aii_for_class3(j, i):
    """At p = e_{p_i} + e_{l_{i+1}}, image should be e_{B_i} + e_{M_j}
    if i+1 <= n-1 (engine is interior l), OR something analogous if
    i+1 = n.

    Returns the AII point and the expected BDI image (gap point + extras).
    """
    n = N
    aii_pt = {f"prefix[{i}]": 1, f"long[{i+1}]": 1}
    # The expected image at this AII point depends on the signature too,
    # but base parts: p_i -> B_i, modified l_{i+1} -> M_j.
    bdi_pt = {f"B_{i}": 1, f"M_{j}": 1}
    return aii_pt, bdi_pt


def bdi_gap_point_feasible(j, i, n):
    """Is the BDI lattice point e_{M_j} + e_{B_i} itself BDI-feasible?
    Needed because if NOT, no piece can hit it -- the Class-3 pair is
    vacuous (no aux needed for this 'gap')."""
    bv = bdi_vars(n)
    q = [0] * len(bv)
    q[bv.index(f"M_{j}")] = 1
    q[bv.index(f"B_{i}")] = 1
    return bdi_feasible(tuple(q), n)


# ---------------------------------------------------------------------
# Build augmented registry + Class 3/4 aux, run analysis
# ---------------------------------------------------------------------
def main():
    print(f"\n{'='*70}")
    print(f"Day 73 CODE Task A — Class 3 + Class 4 aux enumeration at n=5")
    print(f"{'='*70}")

    n = N
    s = aii_struct(n)
    aii_v = s["vars"]
    n_bdi = len(bdi_vars(n))
    base_M = piece_matrix(base_piece(n), s)

    results = {
        "class3": [],
        "class4": [],
        "feasibility_summary": {},
        "signature_uniqueness": None,
        "three_clique_check": None,
    }

    # -----------------------------------------------------------------
    # Class 3
    # -----------------------------------------------------------------
    print(f"\n--- Class 3: misaligned (M_j, B_i) for i != j-1 ---")
    pairs = class3_pairs()
    print(f"  # pairs to enumerate: {len(pairs)} (expected 9)")

    # Pre-check: which gap points are even BDI-feasible?
    print(f"\n  Pre-check: which gap points e_{{M_j}} + e_{{B_i}} are BDI-feasible?")
    feasible_pairs = []
    vacuous_pairs = []
    for (j, i, sig_short, sig_bt_a) in pairs:
        if bdi_gap_point_feasible(j, i, n):
            feasible_pairs.append((j, i, sig_short, sig_bt_a))
            print(f"    (M_{j}, B_{i}): BDI-feasible -> aux needed")
        else:
            vacuous_pairs.append((j, i))
            print(f"    (M_{j}, B_{i}): NOT BDI-feasible (M_{j}=1 > P_{j-1}=0 "
                  f"when i > j-1) -> vacuous (no cover needed)")
    print(f"  -> {len(feasible_pairs)} genuine Class-3 cases; "
          f"{len(vacuous_pairs)} vacuous (no aux possible since gap point "
          f"is itself infeasible).")

    class3_aux = {}
    for (j, i, sig_short, sig_bt_a) in feasible_pairs:
        name = f"AUXc3_M{j}B{i}"
        spec = make_class3_aux(j, i, sig_short, sig_bt_a)
        M = spec_to_matrix(spec, n)
        fails = verify_ray_feasibility(M, n)
        sig = column_signature(M, base_M, n)
        # Target image:
        ai, bi = target_aii_for_class3(j, i)
        img = target_image(M, ai, n)
        # Did we hit {M_j, B_i} (possibly + extras)?
        bdi_var_idx = {v: k for k, v in enumerate(bdi_vars(n))}
        has_M_j = img[bdi_var_idx[f"M_{j}"]] >= 1
        has_B_i = img[bdi_var_idx[f"B_{i}"]] >= 1

        status = "OK" if not fails else "INFEASIBLE"
        print(f"  {name}: sig = {sig}, image at p_{i}+l_{i+1} = {img}, "
              f"feas = {status}, hits ({{M_{j}, B_{i}}}) = "
              f"{has_M_j and has_B_i}")
        if fails:
            for k, (rj, r, im) in enumerate(fails[:2]):
                print(f"    fail ray {rj} = {r} -> img {im}")

        results["class3"].append({
            "name": name,
            "j": j, "i": i,
            "signature": list(sig),
            "image_at_target_aii": list(img),
            "feasible": not fails,
            "hits_target_pair": has_M_j and has_B_i,
            "n_failures": len(fails),
        })
        if not fails:
            class3_aux[name] = M

    results["class3_vacuous_pairs"] = [
        {"j": j, "i": i,
         "reason": f"BDI gap point e_M{j}+e_B{i} infeasible since M_{j}=1 > P_{j-1}=0 (i={i} > j-1={j-1})"}
        for (j, i) in vacuous_pairs
    ]

    # -----------------------------------------------------------------
    # Class 4
    # -----------------------------------------------------------------
    print(f"\n--- Class 4: cross-modify (B_i, T_i) for i in {{2, 3}} ---")
    class4_aux = {}
    for i in [2, 3]:
        name = f"AUXc4_B{i}T{i}"
        spec = make_class4_aux(i)
        M = spec_to_matrix(spec, n)
        fails = verify_ray_feasibility(M, n)
        sig = column_signature(M, base_M, n)
        # Target: p = e_{p_{i-1}} + e_{s_i}.  Need AII feasibility:
        # Main_i: l_i + s_i = 0 + 1 = 1 <= p_{i-1} = 1 ✓.
        ai = {f"prefix[{i-1}]": 1, f"short[{i}]": 1}
        img = target_image(M, ai, n)
        bdi_var_idx = {v: k for k, v in enumerate(bdi_vars(n))}
        has_Bi_Ti = img[bdi_var_idx[f"B_{i}"]] >= 1 and \
                    img[bdi_var_idx[f"T_{i}"]] >= 1
        # Stronger: image is EXACTLY e_{B_i} + e_{T_i} (no extras)?
        expected = [0] * n_bdi
        expected[bdi_var_idx[f"B_{i}"]] = 1
        expected[bdi_var_idx[f"T_{i}"]] = 1
        exact_hit = tuple(expected) == img

        status = "OK" if not fails else "INFEASIBLE"
        print(f"  {name}: sig = {sig}, image at p_{i-1}+s_{i} = {img}, "
              f"feas = {status}, EXACT hit = {exact_hit}")

        results["class4"].append({
            "name": name,
            "i": i,
            "signature": list(sig),
            "image_at_target_aii": list(img),
            "feasible": not fails,
            "exact_target_hit": exact_hit,
            "n_failures": len(fails),
        })
        if not fails:
            class4_aux[name] = M

    # -----------------------------------------------------------------
    # Signature uniqueness
    # -----------------------------------------------------------------
    print(f"\n--- Signature uniqueness across all class 3+4 aux ---")
    all_sigs = {}
    for r in results["class3"] + results["class4"]:
        sig = tuple(r["signature"])
        all_sigs.setdefault(sig, []).append(r["name"])
    duplicates = {sig: names for sig, names in all_sigs.items()
                  if len(names) > 1}
    if duplicates:
        print(f"  DUPLICATE signatures:")
        for sig, names in duplicates.items():
            print(f"    {sig}: {names}")
    else:
        print(f"  All {len(all_sigs)} signatures unique ✓")
    results["signature_uniqueness"] = {
        "n_distinct_signatures": len(all_sigs),
        "n_aux_pieces": sum(len(v) for v in all_sigs.values()),
        "duplicates": {str(k): v for k, v in duplicates.items()},
    }

    # -----------------------------------------------------------------
    # 3-clique check (Lemma 4.3)
    # -----------------------------------------------------------------
    print(f"\n--- 3-clique check (Lemma 4.3) ---")
    print(f"  Build combined registry = AXIS + Class 1 + Class 2 + Class 3 + Class 4")

    # Build augmented registry at n=5 (AXIS + Class 1 + Class 2)
    aug_reg = build_augmented_registry(n)
    feasible, _ = filter_feasible(aug_reg, n, verbose=False)
    print(f"  augmented registry: {len(feasible)} feasible pieces")

    # Add Class 3 and 4
    combined = dict(feasible)
    for name, M in class3_aux.items():
        combined[name] = M
    for name, M in class4_aux.items():
        combined[name] = M
    print(f"  combined registry: {len(combined)} pieces "
          f"(+{len(class3_aux)} class3, +{len(class4_aux)} class4)")

    # AXIS variables (Day-72 prediction): {p_1, p_2, p_3, p_5, l_1, l_2, l_3, l_4}
    axis_vars = {"prefix[1]", "prefix[2]", "prefix[3]", "prefix[5]",
                 "long[1]", "long[2]", "long[3]", "long[4]"}
    triples = find_3cliques_on_walls(combined, n)
    by_wall = defaultdict(list)
    for (a, b, c, wall) in triples:
        by_wall[wall].append((a, b, c))
    print(f"  # 3-cliques: {len(triples)}")
    print(f"  Walls hit: {set(by_wall.keys())}")
    non_axis_walls = {w: ts for w, ts in by_wall.items() if w not in axis_vars}
    print(f"  # 3-cliques on NON-AXIS walls: "
          f"{sum(len(ts) for ts in non_axis_walls.values())}")
    if non_axis_walls:
        print(f"  *** VIOLATIONS of Lemma 4.3: non-AXIS walls with 3-cliques:")
        for w, ts in non_axis_walls.items():
            print(f"      {w}: {len(ts)} triples; e.g. {ts[0]}")
    else:
        print(f"  Lemma 4.3 VERIFIED: every 3-clique is on an AXIS wall ✓")

    results["three_clique_check"] = {
        "n_pieces": len(combined),
        "n_class3_added": len(class3_aux),
        "n_class4_added": len(class4_aux),
        "n_3cliques": len(triples),
        "walls_hit": sorted(by_wall.keys()),
        "axis_vars": sorted(axis_vars),
        "non_axis_walls_violating_lemma43": {
            w: [list(t) for t in ts] for w, ts in non_axis_walls.items()
        },
        "lemma_4_3_verified": len(non_axis_walls) == 0,
    }

    # -----------------------------------------------------------------
    # Headline
    # -----------------------------------------------------------------
    print(f"\n{'='*70}")
    print(f"HEADLINE:")
    n3 = len(results["class3"])
    n3_feasible = sum(1 for r in results["class3"] if r["feasible"])
    n3_hits = sum(1 for r in results["class3"] if r["hits_target_pair"])
    n3_vacuous = len(results["class3_vacuous_pairs"])
    n4 = len(results["class4"])
    n4_feasible = sum(1 for r in results["class4"] if r["feasible"])
    n4_exact = sum(1 for r in results["class4"] if r["exact_target_hit"])
    print(f"  Class 3: {n3_feasible}/{n3} feasible, {n3_hits}/{n3} hit target pair")
    print(f"  Class 3: {n3_vacuous} VACUOUS pairs (BDI gap point itself infeasible)")
    print(f"  Class 4: {n4_feasible}/{n4} feasible, {n4_exact}/{n4} exact target hit")
    print(f"  Unique signatures: "
          f"{'YES' if not duplicates else f'NO ({len(duplicates)} dups)'}")
    lemma43 = results["three_clique_check"]["lemma_4_3_verified"]
    print(f"  Lemma 4.3 (no new 3-cliques on non-AXIS walls): "
          f"{'VERIFIED' if lemma43 else 'BROKEN'}")
    print(f"{'='*70}")

    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nsaved results to {OUT_DIR / 'results.json'}")


if __name__ == "__main__":
    main()
