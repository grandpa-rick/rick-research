"""
so_6 weight multisets via the exceptional iso so_6 ≅ sl_4.

so_6 irrep with highest weight (l_1, l_2, l_3), l_1 >= l_2 >= l_3 >= 0 (non-spinor),
corresponds to sl_4 (= A_3) irrep with partition

    λ_sl_4 = (l_1 + l_2, l_1 + l_3, l_2 + l_3, 0).

We enumerate sl_4 SSYT (column-strict, weakly-row-increasing tableaux with entries in
{1,2,3,4}) of that shape; each tableau gives a gl_4 weight (n_1, n_2, n_3, n_4) =
counts of 1,2,3,4. We convert to an so_6 weight via the orthogonal change of basis
that matches the Dynkin-diagram iso α_1^{D_3}↔α_2^{A_3}, α_2^{D_3}↔α_1^{A_3},
α_3^{D_3}↔α_3^{A_3}:

    a = (n_1 + n_2 - n_3 - n_4) / 2
    b = (n_1 - n_2 + n_3 - n_4) / 2
    c = (-n_1 + n_2 + n_3 - n_4) / 2

Sanity-checked on the vector rep (l_1, l_2, l_3) = (1, 0, 0): the 6 SSYTs of shape (1,1)
in alphabet [4] give the 6 weights {±e_i}, as expected.

Rick — Day 66 CODE — 2026-06-12
"""

from __future__ import annotations

from collections import Counter
from typing import Iterator


def ssyt_shape(shape: tuple[int, ...], alphabet_size: int) -> Iterator[list[list[int]]]:
    """Enumerate semistandard Young tableaux of given shape with entries in {1,...,alphabet_size}.

    Rows weakly increase L->R; columns strictly increase top->bottom.

    Yields each tableau as a list of rows.
    """
    rows = len(shape)
    if rows == 0:
        yield []
        return
    cells = [(i, j) for i in range(rows) for j in range(shape[i])]

    def recurse(idx: int, T: list[list[int]]) -> Iterator[list[list[int]]]:
        if idx == len(cells):
            yield [row[:] for row in T]
            return
        i, j = cells[idx]
        # Row constraint: T[i][j] >= T[i][j-1] (weakly)
        lower_row = T[i][j - 1] if j > 0 else 1
        # Column constraint: T[i][j] > T[i-1][j] (strictly)
        lower_col = (T[i - 1][j] + 1) if i > 0 else 1
        lo = max(lower_row, lower_col)
        for v in range(lo, alphabet_size + 1):
            T[i].append(v)
            yield from recurse(idx + 1, T)
            T[i].pop()

    T0 = [[] for _ in range(rows)]
    yield from recurse(0, T0)


def gl4_weight_multiset(shape: tuple[int, ...]) -> Counter:
    """Counter[(n_1, n_2, n_3, n_4)] = multiplicity of weight in V_shape^{gl_4}."""
    if any(s < 0 for s in shape) or any(shape[i] < shape[i + 1] for i in range(len(shape) - 1)):
        raise ValueError(f"shape {shape} is not a partition")
    counter: Counter = Counter()
    for T in ssyt_shape(shape, 4):
        n = [0, 0, 0, 0]
        for row in T:
            for v in row:
                n[v - 1] += 1
        counter[tuple(n)] += 1
    return counter


def so6_weight_from_gl4(n: tuple[int, int, int, int]) -> tuple[int, int, int] | tuple[float, float, float]:
    """Convert gl_4 weight to so_6 weight via the D_3 = A_3 iso."""
    n1, n2, n3, n4 = n
    a2 = n1 + n2 - n3 - n4
    b2 = n1 - n2 + n3 - n4
    c2 = -n1 + n2 + n3 - n4
    # For non-spinor so_6 irreps (lifted from V_λ^{gl_6}), these will be even.
    if a2 % 2 == 0 and b2 % 2 == 0 and c2 % 2 == 0:
        return (a2 // 2, b2 // 2, c2 // 2)
    return (a2 / 2, b2 / 2, c2 / 2)


def so6_partition_to_sl4(l1: int, l2: int, l3: int) -> tuple[int, int, int, int]:
    """so_6 highest weight (l_1, l_2, l_3) -> sl_4 partition (l_1+l_2, l_1+l_3, l_2+l_3, 0)."""
    return (l1 + l2, l1 + l3, l2 + l3, 0)


def so6_weight_multiset(l1: int, l2: int, l3: int) -> Counter:
    """Weight multiset of V_{(l_1,l_2,l_3)}^{so_6} as Counter[(a, b, c)]."""
    assert l1 >= l2 >= l3 >= 0, f"need l1>=l2>=l3>=0, got ({l1},{l2},{l3})"
    sl4_partition = so6_partition_to_sl4(l1, l2, l3)
    # Drop trailing zeros for SSYT generator
    while sl4_partition and sl4_partition[-1] == 0:
        sl4_partition = sl4_partition[:-1]
    gl4 = gl4_weight_multiset(sl4_partition)
    so6: Counter = Counter()
    for n, mult in gl4.items():
        w = so6_weight_from_gl4(n)
        so6[w] += mult
    return so6


def so6_dim_from_weights(l1: int, l2: int, l3: int) -> int:
    """Dim of V_{(l1,l2,l3)}^{so_6} via Weyl dimension formula (D_3)."""
    # Positive roots of D_3 in R^3: e_i ± e_j for i<j.
    pos_roots = [
        (1, -1, 0), (1, 1, 0),  # e_1 ± e_2
        (1, 0, -1), (1, 0, 1),  # e_1 ± e_3
        (0, 1, -1), (0, 1, 1),  # e_2 ± e_3
    ]
    rho = (2, 1, 0)
    lr = (l1 + rho[0], l2 + rho[1], l3 + rho[2])
    num = 1
    den = 1
    for a in pos_roots:
        num *= lr[0] * a[0] + lr[1] * a[1] + lr[2] * a[2]
        den *= rho[0] * a[0] + rho[1] * a[1] + rho[2] * a[2]
    assert num % den == 0, f"dim formula failed on ({l1},{l2},{l3}): {num}/{den}"
    return num // den


def axis_marginals(weights: Counter) -> dict[str, list[int]]:
    """Compute axis-marginal (level-set count) multisets, sorted.

    Returns a dict of named marginals for the standard so_6 axis projections.
    """
    axes = {
        "e1": (1, 0, 0),
        "e2": (0, 1, 0),
        "e3": (0, 0, 1),
        "e1+e2": (1, 1, 0),
        "e1+e2+e3": (1, 1, 1),
        # Diagram-involution-twisted (σ_0 swap 1↔3):
        "e3+e1": (1, 0, 1),  # same as e1+e3 because (a,b,c)·(1,0,1) = a+c
        # Spinor swap on full vector:
        "e1-e3": (1, 0, -1),
    }
    out: dict[str, list[int]] = {}
    for name, f in axes.items():
        hist: Counter = Counter()
        for w, mult in weights.items():
            val = f[0] * w[0] + f[1] * w[1] + f[2] * w[2]
            hist[val] += mult
        sorted_vals = sorted(hist.values())
        out[name] = sorted_vals
    return out


if __name__ == "__main__":
    # Sanity: vector rep
    W = so6_weight_multiset(1, 0, 0)
    print("Vector rep (1,0,0):")
    for w, m in sorted(W.items()):
        print(f"  {w}: {m}")
    print(f"  dim = {sum(W.values())} (formula gives {so6_dim_from_weights(1, 0, 0)})")
    print()

    # Adjoint of so_6 = (1,1,0). Should have dim 15.
    W = so6_weight_multiset(1, 1, 0)
    print(f"(1,1,0) (adjoint?): dim = {sum(W.values())}, formula = {so6_dim_from_weights(1,1,0)}")

    # Symmetric square (2,0,0), dim should be 20.
    W = so6_weight_multiset(2, 0, 0)
    print(f"(2,0,0): dim = {sum(W.values())}, formula = {so6_dim_from_weights(2,0,0)}")

    # (2,1,0): dim should be 64.
    W = so6_weight_multiset(2, 1, 0)
    print(f"(2,1,0): dim = {sum(W.values())}, formula = {so6_dim_from_weights(2,1,0)}")

    # (1,1,1): dim 10 in so_6? Let me check via formula.
    W = so6_weight_multiset(1, 1, 1)
    print(f"(1,1,1): dim = {sum(W.values())}, formula = {so6_dim_from_weights(1,1,1)}")
