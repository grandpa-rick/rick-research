#!/usr/bin/env python3
"""
Universal BDI piece machinery for n=5, 6, 7.

USES THE ACTUAL AII EXTREME RAYS (verified AII feasible and 1-dim extreme).

Note: registry.py's `aii_rays()` is buggy — it lists several "rays" that
are NOT AII feasible (e.g., "long[n]+short[1]" alone violates Main_n
since long[n]=1 > prefix[n-1]=0). We re-derive the correct rays.

BDI ordering:
    M_2, ..., M_{n-1}, B_1, ..., B_{n-1}, T_1, ..., T_{n-1}, S
Total dim = 3n - 3.

Piece columns (from registry.json):
    prefix[1..n], long[1..n], short[1..n_short], (linkLHS at even n)
    n_short = n-1 at even n, n at odd n.

AII feasible region:
    p >= 0
    Main_i: long[i] + short[i] <= prefix[i-1]  for i=2..n
            (at even n, short[n] doesn't exist; effective Main_n: long[n] <= prefix[n-1])
    linkLHS = sum(short[j])  (even n only)

CORRECT AII extreme rays:

    odd n (3n rays):
        1. prefix[i] pure                       (n rays)
        2. long[1] pure                         (1 ray)
        3. short[1] pure                        (1 ray)
        4. prefix[i-1] + long[i]   for i=2..n   (n-1 rays)
        5. prefix[i-1] + short[i]  for i=2..n   (n-1 rays)

    even n (3n-1 rays):
        1. prefix[i] pure                                  (n rays)
        2. long[1] pure                                    (1 ray)
        3. short[1] + linkLHS                              (1 ray)
        4. prefix[i-1] + long[i]   for i=2..n              (n-1 rays)
        5. prefix[i-1] + short[i] + linkLHS for i=2..n-1   (n-2 rays)
"""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path


# ===================================================================
# BDI coords and feasibility
# ===================================================================
def bdi_coords(n: int) -> list[str]:
    cs = [f"M{a}" for a in range(2, n)]
    cs += [f"B{a}" for a in range(1, n)]
    cs += [f"T{a}" for a in range(1, n)]
    cs += ["S"]
    return cs


def bdi_idx(n: int) -> dict[str, int]:
    return {c: i for i, c in enumerate(bdi_coords(n))}


def zero_vec(n: int) -> tuple:
    return tuple([0] * (3 * n - 3))


def vec(n: int, **kw) -> tuple:
    idx = bdi_idx(n)
    v = [0] * (3 * n - 3)
    for k, c in kw.items():
        v[idx[k]] = c
    return tuple(v)


def add(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def scale(c: int, v: tuple) -> tuple:
    return tuple(c * x for x in v)


def P_a(n: int, a: int, v: tuple) -> int:
    """P_a = 2 sum_{b<=a}(B_b - T_b)."""
    idx = bdi_idx(n)
    return 2 * sum(v[idx[f"B{b}"]] - v[idx[f"T{b}"]] for b in range(1, a + 1))


def is_BDI(n: int, v: tuple) -> bool:
    idx = bdi_idx(n)
    if any(x < 0 for x in v):
        return False
    for a in range(1, n):
        if v[idx[f"T{a}"]] > v[idx[f"B{a}"]]:
            return False
        if P_a(n, a, v) < 0:
            return False
    for a in range(2, n):
        if v[idx[f"M{a}"]] > min(P_a(n, a - 1, v), P_a(n, a, v)):
            return False
    if v[idx["S"]] > P_a(n, n - 1, v):
        return False
    return True


# ===================================================================
# Piece columns (uses registry.json names directly)
# ===================================================================
def piece_columns(n: int) -> list[str]:
    cols = [f"prefix[{j}]" for j in range(1, n + 1)]
    cols += [f"long[{j}]" for j in range(1, n + 1)]
    n_short = n if n % 2 == 1 else n - 1
    cols += [f"short[{j}]" for j in range(1, n_short + 1)]
    if n % 2 == 0:
        cols += ["linkLHS"]
    return cols


def zero_piece(n: int) -> dict:
    Z = zero_vec(n)
    return {c: Z for c in piece_columns(n)}


# ===================================================================
# Actual AII extreme rays per registry.py convention
# ===================================================================
def aii_rays(n: int) -> list[dict]:
    """Return CORRECT AII extreme rays as list of {col_name: coef} dicts.

    Derived directly from the AII feasibility constraints:
        - p >= 0
        - long[i] + short[i] <= prefix[i-1] for i=2..n
        - linkLHS = sum(short[j])  (even n only)

    odd n  → 3n rays.
    even n → 3n-1 rays.
    """
    rays = []
    # 1. prefix[i] pure for i=1..n
    for i in range(1, n + 1):
        rays.append({f"prefix[{i}]": 1})
    # 2. long[1] pure
    rays.append({"long[1]": 1})
    # 3. short[1] pure (or short[1]+linkLHS at even)
    r3 = {"short[1]": 1}
    if n % 2 == 0:
        r3["linkLHS"] = 1
    rays.append(r3)
    # 4. prefix[i-1] + long[i] for i=2..n
    for i in range(2, n + 1):
        rays.append({f"prefix[{i-1}]": 1, f"long[{i}]": 1})
    # 5. prefix[i-1] + short[i] for i=2..n at odd, i=2..n-1 at even
    if n % 2 == 1:
        for i in range(2, n + 1):
            rays.append({f"prefix[{i-1}]": 1, f"short[{i}]": 1})
    else:
        for i in range(2, n):
            r = {f"prefix[{i-1}]": 1, f"short[{i}]": 1, "linkLHS": 1}
            rays.append(r)
    return rays


def ray_image(piece: dict, ray: dict) -> tuple:
    """Compute image of a ray (linear combination of cols) on a piece."""
    n = max([len(piece[c]) for c in piece])  # dim
    dim = n
    result = tuple([0] * dim)
    for col_name, coef in ray.items():
        col = piece[col_name]
        result = tuple(result[k] + coef * col[k] for k in range(dim))
    return result


def gen_set(n: int, piece: dict) -> list[tuple]:
    """Return list of ray-image tuples for piece, using actual AII rays."""
    rays = aii_rays(n)
    return [ray_image(piece, r) for r in rays]


def check_F(n: int, piece: dict) -> bool:
    """All actual AII ray-images BDI feasible?"""
    return all(is_BDI(n, g) for g in gen_set(n, piece))


# ===================================================================
# Registry loading
# ===================================================================
REG_PATHS = {
    5: "/home/agent/projects/code/2026-06-17-complete-registry/registry-n5.json",
    6: "/home/agent/projects/code/2026-06-17-complete-registry/registry-n6.json",
    7: "/home/agent/projects/code/2026-06-17-complete-registry/registry-n7.json",
}


def load_registry(n: int) -> dict:
    """Load registry-n*.json. Each piece is dict {col_name: tuple}."""
    with open(REG_PATHS[n]) as f:
        reg = json.load(f)
    pieces = {}
    for name, cols_dict in reg.items():
        piece = {col: tuple(vec) for col, vec in cols_dict.items()}
        pieces[name] = piece
    return pieces


# ===================================================================
# Target lattice point + utilities
# ===================================================================
def target_point(n: int, i: int, alpha: int) -> tuple:
    """T = e_{B_i} + alpha * e_S in BDI at level n."""
    return add(vec(n, **{f"B{i}": 1}), scale(alpha, vec(n, S=1)))


def coord_dict(n: int, v: tuple) -> dict:
    coords = bdi_coords(n)
    return {c: v[k] for k, c in enumerate(coords) if v[k]}


# ===================================================================
# Joint image semigroup (BFS up to coord-sum cap)
# ===================================================================
def joint_generators(pieces_iter, n: int) -> list[tuple]:
    gens = set()
    for piece in pieces_iter:
        for g in gen_set(n, piece):
            gens.add(g)
    return list(gens)


def joint_image_set(generators: list[tuple], n: int, max_sum: int) -> set:
    dim = 3 * n - 3
    Z = tuple([0] * dim)
    image = {Z}
    frontier = {Z}
    nonzero_gens = [g for g in generators if any(x > 0 for x in g)]
    while frontier:
        new_frontier = set()
        for v in frontier:
            for g in nonzero_gens:
                w = tuple(v[k] + g[k] for k in range(dim))
                if sum(w) <= max_sum and w not in image:
                    image.add(w)
                    new_frontier.add(w)
        frontier = new_frontier
    return image


def semigroup_membership(n: int, point: tuple, generators: list[tuple],
                         max_coef: int = 6) -> bool:
    """Recursive bounded membership in semigroup."""
    dim = 3 * n - 3
    gens = [g for g in generators if any(x > 0 for x in g)]
    N = len(gens)
    cache: dict = {}

    def rec(idx: int, remaining: tuple) -> bool:
        if all(x == 0 for x in remaining):
            return True
        if idx == N:
            return False
        key = (idx, remaining)
        if key in cache:
            return cache[key]
        g = gens[idx]
        max_c = max_coef
        for k in range(dim):
            if g[k] > 0:
                max_c = min(max_c, remaining[k] // g[k])
        for c in range(max_c, -1, -1):
            new_rem = tuple(remaining[k] - c * g[k] for k in range(dim))
            if any(x < 0 for x in new_rem):
                continue
            if rec(idx + 1, new_rem):
                cache[key] = True
                return True
        cache[key] = False
        return False

    return rec(0, point)


# ===================================================================
# Self-check
# ===================================================================
def _self_check():
    for n in (5, 6, 7):
        coords = bdi_coords(n)
        assert len(coords) == 3 * n - 3, (n, len(coords))
        Z = zero_piece(n)
        assert check_F(n, Z), f"zero piece must be F-feasible at n={n}"
        T = target_point(n, 3, 2)
        assert is_BDI(n, T), f"target must be BDI at n={n}"
        n_rays = 3 * n if n % 2 == 1 else 3 * n - 1
        assert len(aii_rays(n)) == n_rays, (n, len(aii_rays(n)), n_rays)

    # Registry F-feasibility
    for n in (5, 6, 7):
        pieces = load_registry(n)
        n_ok = sum(1 for p in pieces.values() if check_F(n, p))
        print(f"  n={n}: {n_ok}/{len(pieces)} pieces F-feasible "
              f"(actual AII rays)")
        assert n_ok == len(pieces), f"n={n}: only {n_ok}/{len(pieces)} F-feasible"
    print("bdi_universal._self_check() passed.")


if __name__ == "__main__":
    _self_check()
