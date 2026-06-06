"""
verify_convex_order.py — Verify that Rick's chain-factor convex order on the
chain+singleton positive roots of B_n is genuinely convex.

A linear order < on R^+ is *convex* iff for every binary decomposition
β = β_1 + β_2 with β_1, β_2 ∈ R^+, we have either β_1 < β < β_2 or
β_2 < β < β_1 (i.e., β is strictly between β_1 and β_2).

Equivalently: the set of roots > some cut, and the set of roots < some cut,
are each closed under addition (within R^+).

Convex order ⇔ exists reduced expression for w_0 such that the order is
the standard one from that reduced expression.
"""

from itertools import product, combinations


def chain_singleton_roots(n):
    """Return all chain + singleton positive roots of B_n as 2-tuples (i, j)
    representing E_i + ε E_j with ε ∈ {-1, +1} (and j == n for chain roots),
    or just (i,) for singleton E_i (i == n).

    We represent every root as a tuple (a_1, ..., a_n) of integer coefficients
    in the E_i basis."""
    roots = []
    # Chain roots: E_a - E_n, E_a, E_a + E_n for a = 1..n-1.
    for a in range(1, n):
        roots.append(tuple([0]*(a-1) + [1] + [0]*(n-a-1) + [-1]))  # E_a - E_n
        roots.append(tuple([0]*(a-1) + [1] + [0]*(n-a-1) + [0]))   # E_a
        roots.append(tuple([0]*(a-1) + [1] + [0]*(n-a-1) + [1]))   # E_a + E_n
    # Singleton: E_n
    roots.append(tuple([0]*(n-1) + [1]))
    return roots


def chain_factor_order_index(root, n):
    """Rick's chain-factor order: chain a's bot, mid, top, then chain a+1, ..., then singleton.
    Returns an integer rank (lower = earlier)."""
    # Decompose root: find chain index a or 'sing'.
    if root[-1] == 0 and any(root[a] != 0 for a in range(n-1)):
        # E_a (mid of chain a)
        a = [i for i in range(n-1) if root[i] != 0][0] + 1
        return 3*(a-1) + 1
    elif root[-1] == -1:
        # E_a - E_n (bot of chain a)
        a = [i for i in range(n-1) if root[i] == 1][0] + 1
        return 3*(a-1) + 0
    elif root[-1] == 1 and any(root[a] != 0 for a in range(n-1)):
        # E_a + E_n (top of chain a)
        a = [i for i in range(n-1) if root[i] == 1][0] + 1
        return 3*(a-1) + 2
    elif root[-1] == 1 and all(root[a] == 0 for a in range(n-1)):
        # E_n (singleton)
        return 3*(n-1)
    else:
        raise ValueError(f"Unexpected root {root}")


def is_convex_order(roots, order_fn, n):
    """Check convexity: for every β = β_1 + β_2 with β, β_1, β_2 ∈ R^+,
    rank(β) is strictly between rank(β_1) and rank(β_2)."""
    root_set = set(roots)
    ranks = {r: order_fn(r, n) for r in roots}
    for b1, b2 in combinations(roots, 2):
        b_sum = tuple(b1[i] + b2[i] for i in range(n))
        if b_sum in root_set:
            r1, r2, rs = ranks[b1], ranks[b2], ranks[b_sum]
            lo, hi = min(r1, r2), max(r1, r2)
            if not (lo < rs < hi):
                print(f"  VIOLATION at B_{n}: {b1} + {b2} = {b_sum}")
                print(f"     ranks: {r1}, {r2}, sum={rs}; needed lo < sum < hi.")
                return False
    return True


def test_convexity(n_max=5):
    for n in range(2, n_max + 1):
        roots = chain_singleton_roots(n)
        if is_convex_order(roots, chain_factor_order_index, n):
            print(f"B_{n} chain-factor order on chain+singleton roots: CONVEX ✓")
        else:
            print(f"B_{n} chain-factor order on chain+singleton roots: NOT CONVEX ✗")


if __name__ == '__main__':
    test_convexity(n_max=6)
