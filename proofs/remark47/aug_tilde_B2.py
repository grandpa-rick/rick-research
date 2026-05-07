"""
Aug~ involution test for B_2 spin (SA).

Plan:
- Enumerate all (w, π) pairs for a fixed B_2 spin pair (λ, μ).
- Define a candidate involution Φ by "first applicable move":
    Move M_2 (s_2 pairing): pair (w, π) <-> (s_2 w, π') by long-swap on coord 2.
    Move M_1 (s_1 pairing): pair (w, π) <-> (s_1 w, π') by short-swap on coord 1<->2.
- Check that Φ is a well-defined sign-reversing involution.
- Check fixed points all have ℓ(w) even.
"""

from fractions import Fraction
from collections import defaultdict
from itertools import permutations, product


# ==================== B_2 setup ====================

POS_ROOTS_B2 = [
    ((1, -1), 'L'),  # alpha_1
    ((1, 1), 'L'),   # alpha_1 + 2 alpha_2
    ((1, 0), 'S'),   # e_1 = alpha_1 + alpha_2
    ((0, 1), 'S'),   # e_2 = alpha_2
]
RHO_B2 = (Fraction(3, 2), Fraction(1, 2))
RHO_SHARP_B2 = (2, 1)  # rho + sigma


def weyl_B2():
    """Yield (w_func, length, label) for w in W(B_2)."""
    out = []
    pos_roots = [r for r, _ in POS_ROOTS_B2]
    neg_roots = [tuple(-x for x in r) for r in pos_roots]
    for perm in permutations(range(2)):
        for signs in product([1, -1], repeat=2):
            sg = signs
            pm = perm
            def w(v, sg=sg, pm=pm):
                return tuple(sg[i] * v[pm[i]] for i in range(2))
            cnt = sum(1 for r in pos_roots if w(r) in neg_roots)
            label = (perm, signs)
            out.append((w, cnt, label))
    return out


# Identify each W element by (perm, signs)
def w_label_to_func(label):
    perm, signs = label
    return lambda v: tuple(signs[i] * v[perm[i]] for i in range(2))


def s2_w(label):
    """Return label of s_2 * w."""
    perm, signs = label
    # s_2 acts on (v_1, v_2) -> (v_1, -v_2). So (s_2 w)(v) = s_2(w(v)) = (w(v)_1, -w(v)_2).
    # As (perm', signs'): perm' = perm, signs'[0] = signs[0], signs'[1] = -signs[1].
    new_signs = (signs[0], -signs[1])
    return (perm, new_signs)


def s1_w(label):
    """Return label of s_1 * w (where s_1 swaps coords)."""
    perm, signs = label
    # s_1 acts on (v_1, v_2) -> (v_2, v_1).
    # (s_1 w)(v) = s_1(w(v)) = (w(v)_1 swapped) = (signs[1] * v[perm[1]], signs[0] * v[perm[0]])
    # As (perm', signs'): perm' = (perm[1], perm[0]), signs' = (signs[1], signs[0]).
    return ((perm[1], perm[0]), (signs[1], signs[0]))


def length_of_label(label):
    pos_roots = [r for r, _ in POS_ROOTS_B2]
    neg_roots = [tuple(-x for x in r) for r in pos_roots]
    w = w_label_to_func(label)
    return sum(1 for r in pos_roots if w(r) in neg_roots)


# ==================== Kostant partitions ====================

def all_kostant_partitions_B2(beta):
    """Enumerate all Kostant partitions of beta in B_2.
    Returns list of dicts {root_tuple: count}.
    """
    target = tuple(int(x) for x in beta)
    out = []

    def recurse(idx, remaining, partial):
        if idx == len(POS_ROOTS_B2):
            if remaining == (0, 0):
                out.append(dict(partial))
            return
        root, kind = POS_ROOTS_B2[idx]
        # Bound on copies
        max_n = sum(abs(r) for r in remaining) + 2
        for n in range(max_n + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(2))
            # Conservative pruning
            if new_rem[0] < 0 and all(r[0] >= 0 for r, _ in POS_ROOTS_B2[idx + 1:]):
                break
            new_partial = dict(partial)
            if n > 0:
                new_partial[root] = n
            recurse(idx + 1, new_rem, new_partial)

    recurse(0, target, {})
    return out


def bidegree_of_partition(pi):
    """Return (#long, #short)."""
    long_cnt = 0
    short_cnt = 0
    for root, mult in pi.items():
        kind = 'L' if root in {(1, -1), (1, 1)} else 'S'
        if kind == 'L':
            long_cnt += mult
        else:
            short_cnt += mult
    return (long_cnt, short_cnt)


# ==================== Aug~ moves ====================

def try_move_s2(w_label, pi, w_tilde_a):
    """Try move M_2: long-swap. Pair (w, π) <-> (s_2 w, π').

    β_{s_2 w} - β_w = -2 (w·a)_2 e_2.

    If (w·a)_2 > 0: subtract 2*(w·a)_2 e_2 from β.
       Move on π: replace (e_1+e_2) with (e_1-e_2), (w·a)_2 times.
       Applicable if π has >= (w·a)_2 copies of (e_1+e_2).

    If (w·a)_2 < 0: add 2*|(w·a)_2| e_2 to β.
       Move on π: replace (e_1-e_2) with (e_1+e_2), |(w·a)_2| times.
       Applicable if π has >= |(w·a)_2| copies of (e_1-e_2).

    Returns (new_w_label, new_pi) if applicable, else None.
    """
    coord_2 = w_tilde_a[1]
    if coord_2 == 0:
        return None
    if coord_2 > 0:
        n_swaps = coord_2
        donor = (1, 1)  # remove (e_1 + e_2)
        receiver = (1, -1)  # add (e_1 - e_2)
    else:
        n_swaps = -coord_2
        donor = (1, -1)  # remove (e_1 - e_2)
        receiver = (1, 1)  # add (e_1 + e_2)
    if pi.get(donor, 0) < n_swaps:
        return None
    new_pi = dict(pi)
    new_pi[donor] = new_pi[donor] - n_swaps
    if new_pi[donor] == 0:
        del new_pi[donor]
    new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
    return (s2_w(w_label), new_pi)


def try_move_s1(w_label, pi, w_tilde_a):
    """Try move M_1: short-swap. Pair (w, π) <-> (s_1 w, π').

    β_{s_1 w} - β_w = -((w·a)_1 - (w·a)_2) (e_1 - e_2) = -c (e_1 - e_2)
        where c = (w·a)_1 - (w·a)_2.

    If c > 0: subtract c (e_1 - e_2) from β.
       Move on π: replace e_1 with e_2, c times.
       Applicable if π has >= c copies of e_1 short.

    If c < 0: add |c| (e_1 - e_2) to β.
       Move on π: replace e_2 with e_1, |c| times.
       Applicable if π has >= |c| copies of e_2 short.

    Returns (new_w_label, new_pi) if applicable, else None.
    """
    c = w_tilde_a[0] - w_tilde_a[1]
    if c == 0:
        return None
    if c > 0:
        n_swaps = c
        donor = (1, 0)  # remove e_1
        receiver = (0, 1)  # add e_2
    else:
        n_swaps = -c
        donor = (0, 1)  # remove e_2
        receiver = (1, 0)  # add e_1
    if pi.get(donor, 0) < n_swaps:
        return None
    new_pi = dict(pi)
    new_pi[donor] = new_pi[donor] - n_swaps
    if new_pi[donor] == 0:
        del new_pi[donor]
    new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
    return (s1_w(w_label), new_pi)


def apply_aug_tilde(w_label, pi, tilde_a, priority='s2_first'):
    """Apply one step of Aug~. Returns (new_w_label, new_pi) or None if fixed point.

    Priority order: try s_2 first, then s_1 (or vice versa).
    """
    w_func = w_label_to_func(w_label)
    w_tilde_a = w_func(tilde_a)
    moves = []
    if priority == 's2_first':
        moves = [(try_move_s2, 's2'), (try_move_s1, 's1')]
    else:
        moves = [(try_move_s1, 's1'), (try_move_s2, 's2')]
    for move_fn, name in moves:
        result = move_fn(w_label, pi, w_tilde_a)
        if result is not None:
            return result, name
    return None, None


# ==================== Test on a specific pair ====================

def kostant_partitions_at_bidegree(beta, target_bidegree):
    """Return list of Kostant partitions of beta with given bidegree."""
    all_pis = all_kostant_partitions_B2(beta)
    return [pi for pi in all_pis if bidegree_of_partition(pi) == target_bidegree]


def test_aug_tilde_on_pair(lam, mu, priority='s2_first', verbose=True):
    """Test Aug~ on a single B_2 spin pair."""
    tilde_a = tuple(lam[i] + RHO_B2[i] for i in range(2))
    b = tuple(mu[i] + RHO_B2[i] for i in range(2))
    if any(not isinstance(x, int) and x.denominator != 1 for x in tilde_a + b):
        # Convert to int if integer-valued
        if all(x.denominator == 1 for x in tilde_a + b):
            tilde_a = tuple(int(x) for x in tilde_a)
            b = tuple(int(x) for x in b)
        else:
            raise ValueError(f"tilde_a or b not integer: {tilde_a}, {b}")
    tilde_a = tuple(int(x) for x in tilde_a)
    b = tuple(int(x) for x in b)

    if verbose:
        print(f"\n=== B_2 spin pair λ={lam}, μ={mu} ===")
        print(f"  tilde_a = {tilde_a}, b = {b}")

    weyl = weyl_B2()
    # All (w, π) pairs
    items = []  # list of (w_label, length, pi, bidegree)
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        if beta_w[0] < 0:
            continue
        pis = all_kostant_partitions_B2(beta_w)
        for pi in pis:
            bd = bidegree_of_partition(pi)
            items.append((label, length, pi, bd))

    # Apply Aug~ to each item
    matched = {}  # item_idx -> partner_idx (for involution)
    fixed_points = []
    for idx, (label, length, pi, bd) in enumerate(items):
        result, move_name = apply_aug_tilde(label, pi, tilde_a, priority=priority)
        if result is None:
            fixed_points.append(idx)
        else:
            new_label, new_pi = result
            # Find partner in items
            partner_idx = None
            for j, (lbl, lng, p, b_) in enumerate(items):
                if lbl == new_label and p == new_pi:
                    partner_idx = j
                    break
            if partner_idx is None:
                if verbose:
                    print(f"  ERROR: no partner found for item {idx}: w={label}, pi={pi}, bd={bd}")
                    print(f"    expected partner: w={new_label}, pi={new_pi}")
                return False
            matched[idx] = partner_idx

    # Check involution
    for idx, partner in matched.items():
        if matched.get(partner) != idx:
            if verbose:
                print(f"  ERROR: involution fails. idx={idx} -> {partner}, but {partner} -> {matched.get(partner)}")
            return False
        # Check parity flip
        l1 = items[idx][1]
        l2 = items[partner][1]
        if (l1 + l2) % 2 != 1:
            if verbose:
                print(f"  ERROR: parity not flipped: {l1} vs {l2}")
            return False
        # Check bidegree preserved
        if items[idx][3] != items[partner][3]:
            if verbose:
                print(f"  ERROR: bidegree not preserved: {items[idx][3]} vs {items[partner][3]}")
            return False

    # Check fixed points all even-length
    bad_fp = []
    for idx in fixed_points:
        if items[idx][1] % 2 != 0:
            bad_fp.append(idx)

    if verbose:
        print(f"  Total items: {len(items)}, matched pairs: {len(matched) // 2}, fixed points: {len(fixed_points)}")
        if bad_fp:
            print(f"  ❌ FAIL: {len(bad_fp)} odd-length fixed points!")
            for idx in bad_fp:
                lbl, lng, pi, bd = items[idx]
                print(f"    w={lbl}, length={lng}, pi={pi}, bidegree={bd}")
        else:
            print(f"  ✓ All fixed points have even length")
            # Compute KL from fixed points
            fp_bidegrees = defaultdict(int)
            for idx in fixed_points:
                bd = items[idx][3]
                fp_bidegrees[bd] += 1
            kl_str = " + ".join(f"{c}*q^{i}t^{j}" for (i, j), c in sorted(fp_bidegrees.items()))
            print(f"  KL (from fixed pts) = {kl_str}")

    return len(bad_fp) == 0


# ==================== Main ====================

def main():
    F = Fraction
    half = F(1, 2)

    # Test all dominant spin pairs
    test_pairs = []
    for l1 in range(5):
        for l2 in range(l1 + 1):
            lam = (l1 + half, l2 + half)
            for m1 in range(l1 + 1):
                for m2 in range(m1 + 1):
                    mu = (m1 + half, m2 + half)
                    test_pairs.append((lam, mu))
    print(f"Testing {len(test_pairs)} dominant spin pairs in B_2 with λ_1 ≤ 9/2 ...")
    failures = []
    for lam, mu in test_pairs:
        ok = test_aug_tilde_on_pair(lam, mu, priority='s2_first', verbose=False)
        if not ok:
            failures.append((lam, mu))
            print(f"FAIL (s2_first): λ={lam}, μ={mu}")
            test_aug_tilde_on_pair(lam, mu, priority='s2_first', verbose=True)
    print(f"\nDominant: {len(failures)}/{len(test_pairs)} failures")

    # Also test non-dominant μ (just spin)
    print("\nTesting NON-dominant spin μ pairs ...")
    nondom_pairs = []
    for l1 in range(5):
        for l2 in range(l1 + 1):
            lam = (l1 + half, l2 + half)
            # μ ranges over half-integers in some box
            for m1_int in range(-l1 - 2, l1 + 3):
                for m2_int in range(-l1 - 2, l1 + 3):
                    mu = (m1_int + half, m2_int + half)
                    nondom_pairs.append((lam, mu))
    print(f"Testing {len(nondom_pairs)} (λ, μ) pairs (μ may be non-dominant) ...")
    nondom_fail = []
    for lam, mu in nondom_pairs:
        ok = test_aug_tilde_on_pair(lam, mu, priority='s2_first', verbose=False)
        if not ok:
            nondom_fail.append((lam, mu))
    print(f"Non-dominant: {len(nondom_fail)}/{len(nondom_pairs)} failures")
    if nondom_fail:
        for lam, mu in nondom_fail[:10]:
            print(f"  FAIL: λ={lam}, μ={mu}")
            test_aug_tilde_on_pair(lam, mu, priority='s2_first', verbose=True)
            print()
        # Try the alternate priority
        print("\nRetrying failed pairs with priority 's1_first' ...")
        retry_fail = []
        for lam, mu in nondom_fail:
            ok = test_aug_tilde_on_pair(lam, mu, priority='s1_first', verbose=False)
            if not ok:
                retry_fail.append((lam, mu))
        print(f"With s1_first: {len(retry_fail)}/{len(nondom_fail)} still fail")


if __name__ == "__main__":
    main()
