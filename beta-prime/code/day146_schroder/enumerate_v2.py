"""
Try more weight/sign conventions for Schroder trees vs Rick's b_k.

Rick's b_k: 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739

Also consider a_k := -b_k + sum_{i+j=k} b_i b_j so (1-2F)^2 = 1 + 4A:
  a_k = -3, -18, -255, -4620, -94500, -2078802, -48005802, -1147833720

Novelli-Thibon 2511.18366 Catalan specialization gives (1-2xg)^2 = 1 - 4x
  i.e. g(x) = C(x) = sum Catalan numbers = 1 + x + 2x^2 + 5x^3 + 14x^4 + ...

Under negation x -> -x, matches Rick: F(τ) = -A_Catalan(-τ) kind of thing?
No: b_1 = 3, not 1. There's a factor.

Let me try: Rick's b_k as Schroder tree weights with edge weights (leaf weights)
being some quantity, or where each internal node of arity r contributes some
polynomial in r.
"""

from functools import lru_cache


def schroder_trees_by_leaves(n):
    if n == 1:
        yield ()
        return
    for r in range(2, n + 1):
        for comp in compositions(n, r):
            children_lists = [list(schroder_trees_by_leaves(nn)) for nn in comp]
            yield from _combine(children_lists)


def compositions(n, r):
    if r == 1:
        yield (n,)
        return
    for first in range(1, n - r + 2):
        for rest in compositions(n - first, r - 1):
            yield (first,) + rest


def _combine(lists):
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
    if tree == ():
        return []
    return [len(tree)] + [a for c in tree for a in internal_arities(c)]


def num_internals(tree):
    if tree == ():
        return 0
    return 1 + sum(num_internals(c) for c in tree)


b = [3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739]
a_seq = [-3, -18, -255, -4620, -94500, -2078802, -48005802, -1147833720]


def enumerate_and_report(name, weight_fn, target_seq, n_max=6):
    print(f"\n=== {name} ===")
    for n in range(1, n_max + 1):
        s = 0
        for t in schroder_trees_by_leaves(n):
            s += weight_fn(t)
        target_str = ""
        for i, val in enumerate(target_seq, 1):
            if s == val:
                target_str = f"  == target[{i}]"
            elif s == -val:
                target_str = f"  == -target[{i}]"
        print(f"  n={n}: sum = {s}{target_str}")


# Convention A: e_r = -1 for all r >= 2, sign by internal-node count (Day 145 dream)
def weight_A(tree):
    i_count = num_internals(tree)
    arities = internal_arities(tree)
    w = (-1)**(i_count - 1) if i_count > 0 else 1
    for a in arities:
        w *= -1  # e_r = -1
    return w


enumerate_and_report("Convention A: e_r=-1, sign (-1)^(i-1)", weight_A, b)


# Convention B: e_r = (-1)^r for r >= 2 (Day 145 dream literal)
def weight_B(tree):
    arities = internal_arities(tree)
    w = 1
    for a in arities:
        w *= (-1)**a
    return w


enumerate_and_report("Convention B: e_r=(-1)^r, no extra sign", weight_B, b)


# Convention C: e_r = 3 for r=2, and something for higher (naive guess)
def weight_C(tree):
    arities = internal_arities(tree)
    w = 1
    for a in arities:
        w *= 3 if a == 2 else 1  # b_1 = 3, so binary trees only for n=2 leaves
    return w


enumerate_and_report("Convention C: e_2=3, e_r=1 else", weight_C, b)


# Convention D: e_r = (some Rick formula)
# From Day 133: mu_n = (-1)^(n-1) * (n^2 - 1) / n for M(T)
# Let's try e_r = (r^2 - 1) / r ... but that's rational
def weight_D(tree):
    arities = internal_arities(tree)
    from fractions import Fraction
    w = Fraction(1)
    for a in arities:
        w *= Fraction((-1)**(a-1) * (a*a - 1), a)
    return w


enumerate_and_report("Convention D: e_r = (-1)^(r-1) (r^2-1)/r (Rick's mu_r)", weight_D, b)


# Convention E: n indexing is by internal nodes, not leaves
# Schroder tree with i internal nodes has i+1 leaves (for binary) up to more
# Let's re-enumerate by internal-node count

def by_internals(i):
    """Yield all Schroder trees with exactly i internal nodes."""
    for n in range(1, 2 * i + 2):  # rough leaf range
        for t in schroder_trees_by_leaves(n):
            if num_internals(t) == i:
                yield t


def enumerate_by_internals(name, weight_fn, target_seq, i_max=6):
    print(f"\n=== {name} (index by internal count) ===")
    for i in range(1, i_max + 1):
        s = 0
        for t in by_internals(i):
            s += weight_fn(t)
        target_str = ""
        for j, val in enumerate(target_seq, 1):
            if s == val:
                target_str = f"  == target[{j}]"
            elif s == -val:
                target_str = f"  == -target[{j}]"
        print(f"  i={i}: sum = {s}{target_str}")


enumerate_by_internals("Convention B by internals: e_r=(-1)^r", weight_B, b, i_max=5)


# Also, maybe Rick's b_k relates to trees with n+1 leaves and specific weight
def enumerate_shift_and_test(shift, name, weight_fn, target_seq, n_max=6):
    print(f"\n=== {name} (leaves index shifted by {shift}) ===")
    for n in range(1 + shift, n_max + 1 + shift):
        s = 0
        for t in schroder_trees_by_leaves(n):
            s += weight_fn(t)
        target_str = ""
        for i, val in enumerate(target_seq, 1):
            if s == val:
                target_str = f"  == target[{i}] (k=n-{shift})"
            elif s == -val:
                target_str = f"  == -target[{i}] (k=n-{shift})"
        print(f"  n={n}: sum = {s}{target_str}")


# Convention F: weight = (-1)^{i(t)-1} * (extra factor per leaf)
# Try leaves contributing 3 each
def weight_F(tree, leaf_weight=3):
    if tree == ():
        return leaf_weight
    return sum(  # arbitrary sum
        1
    )  # placeholder — this convention needs more thought


# Print sanity check
print("\n=== Sanity: little Schroder (should be 1,1,3,11,45,197) ===")
def w1(t): return 1
enumerate_and_report("weight=1", w1, [1, 1, 3, 11, 45, 197, 903, 4279])
