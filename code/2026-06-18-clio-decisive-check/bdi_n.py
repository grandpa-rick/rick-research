#!/usr/bin/env python3
"""
General BDI / piece machinery for any n (odd or even).

BDI ordering (registry convention):
    M_2, M_3, ..., M_{n-1}, B_1, ..., B_{n-1}, T_1, ..., T_{n-1}, S
Total dim = (n-2) + 2(n-1) + 1 = 3n - 3. (Same as Day-72.)

Piece columns:
    p_1, ..., p_n         (prefix columns, n of them)
    l_1, ..., l_n         (long columns, n of them)
    s_1, ..., s_{n-1}     (short columns, n-1 of them, since linkLHS gauged out)

Total columns = 3n - 1.

In linkLHS = 0 gauge (even n), short[j] absorbed linkLHS contribution
into s_j (j=1..n-1).

AII extreme rays (per Day-70 Thm 4.2):
    1. p_j pure for j=1..n
    2. l_1 pure
    3. s_1 pure  (= short[1] + linkLHS gauged, or pure short[n] at odd n)
    4. p_{j-1} + l_j for j=2..n
    5. p_{j-1} + s_j for j=2..{n-1}

Total = n + 1 + 1 + (n-1) + (n-2) = 3n - 1 rays. Each ray-image must be BDI.

This module is INDEPENDENT of the existing infrastructure (it just
re-encodes the rules cleanly for the decisive-check workflow).
"""
from __future__ import annotations
from itertools import product


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
    """Check BDI feasibility at level n."""
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


# ====================================================================
# Piece machinery
# ====================================================================
def p_cols(n: int) -> list[str]:
    return [f"p{j}" for j in range(1, n + 1)]


def l_cols(n: int) -> list[str]:
    return [f"l{j}" for j in range(1, n + 1)]


def s_cols(n: int) -> list[str]:
    return [f"s{j}" for j in range(1, n)]  # s_1..s_{n-1}


def all_cols(n: int) -> list[str]:
    return p_cols(n) + l_cols(n) + s_cols(n)


def gen_set(n: int, piece: dict) -> list[tuple]:
    """The 3n - 1 ray-image generators of `piece` in linkLHS = 0 gauge.

    Rays:
      1. p_j for j=1..n              (n rays)
      2. l_1                          (1 ray)
      3. s_1 (short[1]+linkLHS gauged at even n; pure short at odd n)
                                      (1 ray)
      4. p_{j-1} + l_j for j=2..n    (n-1 rays)
      5. p_{j-1} + s_j for j=2..n-1  (n-2 rays)
    Total = n + 1 + 1 + n - 1 + n - 2 = 3n - 1.
    """
    g = []
    for j in range(1, n + 1):
        g.append(piece[f"p{j}"])
    g.append(piece["l1"])
    g.append(piece["s1"])
    for j in range(2, n + 1):
        g.append(add(piece[f"p{j-1}"], piece[f"l{j}"]))
    for j in range(2, n):
        g.append(add(piece[f"p{j-1}"], piece[f"s{j}"]))
    assert len(g) == 3 * n - 1, (len(g), 3 * n - 1)
    return g


def check_F(n: int, piece: dict) -> bool:
    """All ray images BDI?"""
    return all(is_BDI(n, g) for g in gen_set(n, piece))


def zero_piece(n: int) -> dict:
    """All-zero piece (trivially F-feasible)."""
    Z = zero_vec(n)
    return {c: Z for c in all_cols(n)}


def piece_to_human(n: int, piece: dict) -> dict:
    """Convert each column tuple to a dict of nonzero coords."""
    coords = bdi_coords(n)
    return {
        col: {c: piece[col][i] for i, c in enumerate(coords) if piece[col][i] != 0}
        for col in all_cols(n)
        if any(x != 0 for x in piece[col])
    }


# ====================================================================
# Semigroup membership (for verification beyond single-ray witnesses)
# ====================================================================
def semigroup_membership(n: int, point: tuple, generators: list[tuple],
                        max_coef: int = 4) -> bool:
    """Test whether `point` lies in the nonneg integer semigroup spanned
    by `generators`.

    Conservative bounded search up to `max_coef` per generator.
    """
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


# ====================================================================
# Target lattice point
# ====================================================================
def target_point(n: int, i: int, alpha: int) -> tuple:
    """T = e_{B_i} + alpha * e_S in BDI at level n."""
    return add(vec(n, **{f"B{i}": 1}), scale(alpha, vec(n, S=1)))


# ====================================================================
# Quick sanity checks
# ====================================================================
def _self_check():
    for n in (5, 6, 7):
        coords = bdi_coords(n)
        assert len(coords) == 3 * n - 3, (n, len(coords), 3 * n - 3)
        Z = zero_piece(n)
        assert check_F(n, Z), f"zero piece must be F-feasible at n={n}"
        # interior i = 3, target = e_{B_3} + 2 e_S
        T = target_point(n, 3, 2)
        assert is_BDI(n, T), f"target must be BDI at n={n}"
    print("bdi_n._self_check() passed.")


if __name__ == "__main__":
    _self_check()
