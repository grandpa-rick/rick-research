#!/usr/bin/env python3
"""
Task 3: Enumerate ALL F-feasible 2-column witness pieces with T in image.

For each (n, i, alpha):
    enumerate F-feasible pieces with <= 2 nonzero columns, such that
    T = e_{B_i} + alpha e_S is in the joint ray-image semigroup of
    that single witness piece.

Classify into "families" by (col_A, col_B) (the columns used).

Then for each (n, i, alpha) compare to Day-78's three known families:
  - pure-prefix: prefix[i] = T (single column = carrier-shape)
  - lifted-long: prefix[1] = e_{B_i}, long[2] = alpha e_S
  - lifted-short: prefix[1] = e_{B_i}, short[2] = alpha e_S

Find any NEW witness families and propose a canonical witness.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from bdi_universal import (
    bdi_coords, vec, add, scale, zero_vec, zero_piece, piece_columns,
    target_point, coord_dict, is_BDI,
    aii_rays, ray_image, gen_set, check_F,
    joint_generators, joint_image_set,
)


def small_BDI_lattice(n: int, max_sum: int) -> list[tuple]:
    """All BDI feasible lattice points with coord-sum <= max_sum."""
    dim = 3 * n - 3
    pts = []

    def gen(remaining, depth, current):
        if depth == dim:
            v = tuple(current)
            if is_BDI(n, v):
                pts.append(v)
            return
        for k in range(remaining + 1):
            current.append(k)
            gen(remaining - k, depth + 1, current)
            current.pop()

    gen(max_sum, 0, [])
    return pts


def candidate_values(n: int, T: tuple) -> list[tuple]:
    """Restricted set of plausible values: supported on B_i and S coords."""
    dim = 3 * n - 3
    candidates = set()
    candidates.add(tuple([0] * dim))
    nonzero_coords = [k for k, t in enumerate(T) if t > 0]
    i_coord = nonzero_coords[0]
    s_coord = nonzero_coords[1]
    alpha = T[s_coord]

    for bi in range(alpha + 2):
        for sv in range(alpha + 2):  # tighter S bound
            v = [0] * dim
            v[i_coord] = bi
            v[s_coord] = sv
            if bi == 0 and sv == 0:
                continue
            if bi + sv > 1 + alpha:  # stay ≤ T_sum
                continue
            t = tuple(v)
            if is_BDI(n, t):
                candidates.add(t)
    return sorted(candidates, key=lambda v: (sum(v), v))


def build_two_col_piece(n: int, col_A: str, val_A: tuple,
                        col_B: str, val_B: tuple) -> dict:
    p = zero_piece(n)
    p[col_A] = val_A
    if col_B is not None:
        p[col_B] = val_B
    return p


def witness_image(n: int, piece: dict, max_sum: int) -> set:
    """Joint ray-image semigroup of single witness, up to max_sum."""
    gens = list(set(gen_set(n, piece)))
    return joint_image_set(gens, n, max_sum=max_sum)


def enumerate_witnesses(n: int, i: int, alpha: int,
                         max_image_sum: int = 5) -> list[dict]:
    """Enumerate F-feasible 1- or 2-column witness pieces with T in image."""
    T = target_point(n, i, alpha)
    cols = piece_columns(n)
    cands = candidate_values(n, T)

    # Restrict candidate columns to those naturally arising in 2-col witnesses.
    # All columns are eligible.
    seen_sigs = set()  # (col_A, col_B, val_A, val_B) frozen signature
    witnesses = []

    # 1-column witnesses
    for col_A in cols:
        for val_A in cands:
            if val_A == tuple([0] * (3 * n - 3)):
                continue
            piece = build_two_col_piece(n, col_A, val_A, None, None)
            if not check_F(n, piece):
                continue
            img = witness_image(n, piece, max_image_sum)
            if T in img:
                sig = (col_A, None, val_A, None)
                if sig in seen_sigs:
                    continue
                seen_sigs.add(sig)
                witnesses.append({
                    "kind": "1-col",
                    "col_A": col_A, "val_A_coords": coord_dict(n, val_A),
                    "col_B": None, "val_B_coords": None,
                    "n_nonzero_cols": 1,
                })

    # 2-column witnesses (col_A < col_B by index in piece_columns order)
    for ia, col_A in enumerate(cols):
        for ib in range(ia + 1, len(cols)):
            col_B = cols[ib]
            for val_A in cands:
                if val_A == tuple([0] * (3 * n - 3)):
                    continue
                for val_B in cands:
                    if val_B == tuple([0] * (3 * n - 3)):
                        continue
                    piece = build_two_col_piece(n, col_A, val_A, col_B, val_B)
                    if not check_F(n, piece):
                        continue
                    img = witness_image(n, piece, max_image_sum)
                    if T in img:
                        sig = (col_A, col_B, val_A, val_B)
                        if sig in seen_sigs:
                            continue
                        seen_sigs.add(sig)
                        witnesses.append({
                            "kind": "2-col",
                            "col_A": col_A, "val_A_coords": coord_dict(n, val_A),
                            "col_B": col_B, "val_B_coords": coord_dict(n, val_B),
                            "n_nonzero_cols": 2,
                        })
    return witnesses


def classify_witness_family(w: dict) -> str:
    """Map a witness to a family label."""
    a = w["col_A"]
    b = w.get("col_B")
    if b is None:
        return f"1col_{a}"
    if a.startswith("prefix[") and b.startswith("long["):
        return f"pref{a[7:-1]}_long{b[5:-1]}"
    if a.startswith("prefix[") and b.startswith("short["):
        return f"pref{a[7:-1]}_short{b[6:-1]}"
    if a.startswith("prefix[") and b.startswith("prefix["):
        return f"prefpair_{a[7:-1]}_{b[7:-1]}"
    if a.startswith("long[") and b.startswith("short["):
        return f"long{a[5:-1]}_short{b[6:-1]}"
    return f"OTHER_{a}_{b}"


def main():
    import sys as _sys
    out = {"by_case": []}
    cases = []
    # n=6 interior — small subset
    cases.append((6, 3, 1))
    cases.append((6, 3, 2))
    # n=7 interior
    cases.append((7, 3, 1))
    cases.append((7, 3, 2))
    cases.append((7, 4, 1))
    cases.append((7, 4, 2))

    for (n, i, alpha) in cases:
        print(f"\n=== n={n}, i={i}, alpha={alpha} ===", flush=True)
        T = target_point(n, i, alpha)
        ws = enumerate_witnesses(n, i, alpha, max_image_sum=5)
        fams = {}
        for w in ws:
            f = classify_witness_family(w)
            fams.setdefault(f, []).append(w)
        print(f"  Total witnesses: {len(ws)}", flush=True)
        print(f"  Families: {len(fams)}", flush=True)
        # Top 8 families by count
        for f in sorted(fams.keys(), key=lambda x: -len(fams[x]))[:8]:
            print(f"    {f}: {len(fams[f])} witnesses", flush=True)
        case_rec = {
            "n": n, "i": i, "alpha": alpha,
            "T_coords": coord_dict(n, T),
            "n_witnesses_total": len(ws),
            "n_families": len(fams),
            "families": [{"name": f, "count": len(fams[f]),
                          "examples": fams[f][:3]} for f in fams],
        }
        out["by_case"].append(case_rec)

    with open(HERE / "task3_witness_families" / "results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote task3_witness_families/results.json")


if __name__ == "__main__":
    main()
