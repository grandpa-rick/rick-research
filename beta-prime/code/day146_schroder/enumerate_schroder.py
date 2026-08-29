"""
Enumerate Schröder trees (plane rooted trees, all internal nodes of arity >= 2)
by number of leaves, and compute weight sums under generic (e_n) values.

A Schröder tree with n leaves has:
  - n leaves
  - some number of internal nodes v_1, ..., v_k
  - each internal node has arity >= 2 (>= 2 children)

Generating function: super-Catalan / small Schröder / large Schröder depending on
convention. Under the specialization e_n = 1 for all n (each internal node
contributing 1), the sum over Schröder trees with n leaves equals the
(n-1)th large Schröder number: 1, 1, 3, 11, 45, 197, 903, ...

Under Novelli-Thibon / Josuat-Verges style, each internal node of arity r
contributes weight e_r (where e_r is the r-th elementary symmetric function
or a variable).

Rick's conjecture: b_k = |Sum_{t: |leaves(t)| = k+1 (or k)} prod_v e_{arity(v)}|
                        evaluated at e_n = (-1)^n.

Let me enumerate carefully and print a few small cases to make sure I have
the right object BEFORE the research agent returns with the exact formula.
"""

from functools import lru_cache


def schroder_trees_by_leaves(n):
    """Yield all Schröder trees with n leaves, represented as tuples.
    A leaf is (). An internal node with children c_1, ..., c_r (r >= 2) is
    (c_1, ..., c_r) — a tuple of length r >= 2.
    """
    if n == 1:
        yield ()
        return
    # Choose r = number of children of root, r in {2, ..., n}.
    # Then choose ordered compositions n = n_1 + ... + n_r with n_i >= 1.
    # Then recursively enumerate subtrees.
    for r in range(2, n + 1):
        for comp in compositions(n, r):
            children_lists = [list(schroder_trees_by_leaves(nn)) for nn in comp]
            yield from _combine(children_lists)


def compositions(n, r):
    """Ordered compositions of n into r positive parts."""
    if r == 1:
        yield (n,)
        return
    for first in range(1, n - r + 2):
        for rest in compositions(n - first, r - 1):
            yield (first,) + rest


def _combine(lists):
    """Cartesian product yielding tuples."""
    if not lists:
        yield ()
        return
    if len(lists) == 1:
        for x in lists[0]:
            yield (x,)
        return
    head, *tail = lists
    for x in head:
        for rest in _combine(tail):
            yield (x,) + rest


def internal_arities(tree):
    """Return the multiset (as list) of arities of internal nodes in tree."""
    if tree == ():
        return []
    return [len(tree)] + [a for c in tree for a in internal_arities(c)]


def weight(tree, e_values):
    """Weight = product of e_{arity(v)} over internal nodes v."""
    w = 1
    for a in internal_arities(tree):
        w *= e_values.get(a, 0)
    return w


def sum_over_leaves(n, e_values):
    """Sum of weights of all Schröder trees with n leaves."""
    s = 0
    for t in schroder_trees_by_leaves(n):
        s += weight(t, e_values)
    return s


def large_schroder(n):
    """Sanity check: large Schröder numbers 1, 1, 3, 11, 45, 197, ...
    (OEIS A006318) with r_n = number of Schröder paths.
    Actually we're counting Schröder trees; let me just compute at e_n=1 and see."""
    e_ones = {r: 1 for r in range(2, n + 2)}
    return sum_over_leaves(n, e_ones)


if __name__ == "__main__":
    print("=== Sanity: Schröder tree count with e_n = 1 (all arities weight 1) ===")
    for n in range(1, 9):
        cnt = large_schroder(n)
        print(f"  n={n} leaves: {cnt}")

    # A001003 (little Schröder / super-Catalan): 1, 1, 3, 11, 45, 197, 903, 4279, ...
    # A006318 (large Schröder):                 1, 2, 6, 22, 90, 394, 1806, ...
    # With arity >= 2 constraint, sum with e_n=1 should give little Schröder = A001003.

    print()
    print("=== Rick's target: e_n = (-1)^n for n >= 2 ===")
    e_alt = {r: (-1)**r for r in range(2, 12)}
    print(f"  e_values used: {e_alt}")
    for n in range(1, 9):
        s = sum_over_leaves(n, e_alt)
        print(f"  n={n} leaves: sum = {s}")

    print()
    print("=== Rick's b_k values ===")
    b = [3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739]
    for i, bk in enumerate(b, 1):
        print(f"  b_{i} = {bk}")

    print()
    print("=== Comparison — do any Schröder tree sums match up to sign/normalization? ===")
    for n in range(1, 9):
        s = sum_over_leaves(n, e_alt)
        for i, bk in enumerate(b, 1):
            if abs(s) == bk:
                print(f"  MATCH: n={n} leaves gives sum={s}, |sum|={abs(s)} = b_{i}")
            if s and bk % s == 0 and abs(bk // s) < 100:
                print(f"  RATIO: n={n} leaves sum={s} divides b_{i}={bk}, ratio={bk//s}")
