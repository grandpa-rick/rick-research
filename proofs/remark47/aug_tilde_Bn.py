"""
Aug~ involution test for general B_n spin (SA).

Refined (SA) conjecture: for spin λ DOMINANT and DOMINANT spin μ, KL_{λ,μ}^{B_n}(q,t) has nonneg coefs,
proved by Aug~ involution on (w, π) pairs.

Aug~ rule (proposed):
  For each (w, π), find the smallest simple reflection s_i (in some priority order)
  such that the "move M_i" applies.

  Move M_i: pair (w, π) <-> (s_i w, π') where π' is obtained from π by elementary swaps
  realizing β_{s_i w} - β_w = -c_i α_i bidegree-preservingly.

  c_i = <w·a, α_i^v>.

  - For long simple α_i = e_i - e_{i+1} (i = 1, ..., n-1):
      If c_i > 0: π → π' by replacing c_i copies of short e_i with short e_{i+1}.
                  Applicable if π has ≥ c_i copies of e_i.
      If c_i < 0: π → π' by replacing |c_i| copies of e_{i+1} with e_i.
                  Applicable if π has ≥ |c_i| copies of e_{i+1}.

  - For short simple α_n = e_n:
      c_n = 2 (w·a)_n. Always even.
      If c_n > 0: π → π' by replacing c_n/2 copies of (e_? + e_n) with (e_? - e_n)
                  (any partner ?). Each swap subtracts 2 e_n.
                  Applicable if π has ≥ c_n/2 copies total of long roots (e_? + e_n).
      If c_n < 0: π → π' by replacing |c_n|/2 copies of (e_? - e_n) with (e_? + e_n).
                  Applicable if π has ≥ |c_n|/2 copies total of long roots (e_? - e_n).

For partner choice in long-swap (when α is short): we need to pick WHICH (e_? - e_n) or (e_? + e_n)
to swap. To make the move involutory, pick a canonical choice (e.g., smallest index ?).
"""

from fractions import Fraction
from collections import defaultdict
from itertools import permutations, product


# ==================== B_n setup (parameterized by N) ====================

def positive_roots_Bn(N):
    """Return list of (root_tuple, kind) where kind in {'L','S'}.
    Long: e_i - e_j (i<j), e_i + e_j (i<j).  Short: e_i.
    """
    roots = []
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = 1; v[j] = -1
            roots.append((tuple(v), 'L'))
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = 1; v[j] = 1
            roots.append((tuple(v), 'L'))
    for i in range(N):
        v = [0] * N
        v[i] = 1
        roots.append((tuple(v), 'S'))
    return roots


def short_root(N, i):
    """Return short root e_i."""
    v = [0] * N
    v[i] = 1
    return tuple(v)


def long_root_minus(N, i, j):
    """Return e_i - e_j (assume i<j)."""
    v = [0] * N
    v[i] = 1; v[j] = -1
    return tuple(v)


def long_root_plus(N, i, j):
    """Return e_i + e_j (assume i<j)."""
    v = [0] * N
    v[i] = 1; v[j] = 1
    return tuple(v)


def rho_sharp(N):
    """Return rho^sharp = (N, N-1, ..., 1)."""
    return tuple(N - i for i in range(N))


# ==================== Weyl group W(B_n) ====================

def weyl_Bn(N):
    """Yield (w_func, length, label) for w in W(B_n)."""
    pos_roots = [r for r, _ in positive_roots_Bn(N)]
    pos_set = set(pos_roots)
    out = []
    for perm in permutations(range(N)):
        for signs in product([1, -1], repeat=N):
            sg = signs
            pm = perm
            def w(v, sg=sg, pm=pm, N=N):
                return tuple(sg[i] * v[pm[i]] for i in range(N))
            cnt = sum(1 for r in pos_roots if w(r) not in pos_set)
            label = (perm, signs)
            out.append((w, cnt, label))
    return out


def w_label_to_func(label, N):
    perm, signs = label
    return lambda v, perm=perm, signs=signs, N=N: tuple(signs[i] * v[perm[i]] for i in range(N))


def length_of_label(label, N):
    pos_roots = [r for r, _ in positive_roots_Bn(N)]
    pos_set = set(pos_roots)
    w = w_label_to_func(label, N)
    return sum(1 for r in pos_roots if w(r) not in pos_set)


def s_long_w(label, i, N):
    """Return label of s_{α_i} * w, where α_i = e_i - e_{i+1} (long simple, i = 0..N-2)."""
    perm, signs = label
    # s_α swaps coords i and i+1 of input vector. So (s_α w)(v) = s_α(w(v)).
    # If w(v) = (signs[k] * v[perm[k]])_k, then (s_α w)(v) = swap coords i and i+1 of w(v):
    #   coord k of result = signs[k] v[perm[k]] for k != i, i+1
    #   coord i of result = signs[i+1] v[perm[i+1]]
    #   coord i+1 of result = signs[i] v[perm[i]]
    # As (perm', signs'):
    new_perm = list(perm)
    new_perm[i], new_perm[i + 1] = perm[i + 1], perm[i]
    new_signs = list(signs)
    new_signs[i], new_signs[i + 1] = signs[i + 1], signs[i]
    return (tuple(new_perm), tuple(new_signs))


def s_short_w(label, N):
    """Return label of s_{α_n} * w, where α_n = e_n (short simple, last coord)."""
    perm, signs = label
    # s_α flips last coord. (s_α w)(v) = (..., -w(v)[N-1]).
    new_signs = list(signs)
    new_signs[N - 1] = -signs[N - 1]
    return (perm, tuple(new_signs))


# ==================== Kostant partitions ====================

def all_kostant_partitions(beta, N, pos_roots_ordered=None):
    """Enumerate all Kostant partitions of beta.

    Uses ordering: group A (first coord = 1), group B (first coord = 0, second = 1), etc.
    After group A, remaining[0] must be 0 (no later root contributes to coord 0).
    Same for B (coord 1), C (coord 2), ...
    """
    if pos_roots_ordered is None:
        pos_roots_ordered = positive_roots_Bn_ordered(N)
    target = tuple(int(x) for x in beta)
    out = []

    # Compute leading-coord boundaries: idx after which coord k must be 0
    # leading_boundaries[k] = first idx i such that pos_roots_ordered[i][0][k] != 0 ends
    # Actually: coord k must be 0 after processing all roots whose leading nonzero coord is k or earlier.
    # leading_coord(root) = first k with root[k] != 0
    leading_coords = []
    for r, _ in pos_roots_ordered:
        for k in range(N):
            if r[k] != 0:
                leading_coords.append(k)
                break
    # boundary[k] = first idx where leading_coord > k (i.e., all roots with leading = k have been processed)
    boundary = [None] * N
    for k in range(N):
        for i in range(len(pos_roots_ordered)):
            if leading_coords[i] > k:
                boundary[k] = i
                break
        else:
            boundary[k] = len(pos_roots_ordered)

    def recurse(idx, remaining, partial):
        # Hard pruning: at boundary[k], remaining[k] must be 0
        for k in range(N):
            if idx >= boundary[k] and remaining[k] != 0:
                return
        if idx == len(pos_roots_ordered):
            if all(r == 0 for r in remaining):
                out.append(dict(partial))
            return
        root, kind = pos_roots_ordered[idx]
        # Loose bound: max_n based on the leading coord of root.
        # All roots with leading coord = k have root[k] = 1.
        # So sum of n_α for α with leading coord k ≤ remaining at coord k after previous groups.
        # Per-root bound: n ≤ remaining[leading_coords[idx]] (if positive).
        lc = leading_coords[idx]
        rem_lc = remaining[lc]
        if rem_lc < 0:
            return  # impossible: remaining at coord lc is already negative, can't be made 0 by adding more
        max_n = rem_lc  # since each copy of α adds 1 to coord lc
        for n in range(max_n + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(N))
            new_partial = dict(partial)
            if n > 0:
                new_partial[root] = n
            recurse(idx + 1, new_rem, new_partial)

    recurse(0, target, {})
    return out


def positive_roots_Bn_ordered(N):
    """Order positive roots so that group A (first coord = 1), B (first coord = 0, second = 1),
    etc. for efficient enumeration."""
    base = positive_roots_Bn(N)
    # Sort by (descending of first nonzero coord position, then by "shape")
    # Actually just sort by negation of position of first nonzero coord (so first-coord-1 first)
    def keyfn(item):
        r, kind = item
        # leading nonzero position
        for k in range(N):
            if r[k] != 0:
                return (k, r)
        return (N, r)
    return sorted(base, key=keyfn)


def bidegree_of_partition(pi, N):
    """Return (#long, #short)."""
    pos_roots = positive_roots_Bn(N)
    long_set = set(r for r, k in pos_roots if k == 'L')
    short_set = set(r for r, k in pos_roots if k == 'S')
    long_cnt = sum(mult for root, mult in pi.items() if root in long_set)
    short_cnt = sum(mult for root, mult in pi.items() if root in short_set)
    return (long_cnt, short_cnt)


# ==================== Aug~ moves ====================

def try_long_simple_move(label, pi, w_tilde_a, i, N):
    """Try move M_i: pair (w, π) <-> (s_α_i w, π') for long simple α_i = e_i - e_{i+1}.

    c = (w·a)[i] - (w·a)[i+1].

    If c > 0 (i.e., w^{-1} α_i > 0; ℓ(s_α w) = ℓ(w) + 1):
        subtract c α_i from β; in π, replace c copies of short e_i with e_{i+1}.
        Applicable iff π has >= c copies of e_i (short).

    If c < 0:
        add |c| α_i to β; in π, replace |c| copies of short e_{i+1} with e_i.
        Applicable iff π has >= |c| copies of e_{i+1}.
    """
    c = w_tilde_a[i] - w_tilde_a[i + 1]
    if c == 0:
        return None
    if c > 0:
        n_swaps = c
        donor = short_root(N, i)
        receiver = short_root(N, i + 1)
    else:
        n_swaps = -c
        donor = short_root(N, i + 1)
        receiver = short_root(N, i)
    if pi.get(donor, 0) < n_swaps:
        return None
    new_pi = dict(pi)
    new_pi[donor] = new_pi[donor] - n_swaps
    if new_pi[donor] == 0:
        del new_pi[donor]
    new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
    new_label = s_long_w(label, i, N)
    return (new_label, new_pi)


def try_short_simple_move(label, pi, w_tilde_a, N, partner_pref='smallest'):
    """Try move M_n: pair (w, π) <-> (s_α_n w, π') for short simple α_n = e_n.

    c = 2 (w·a)[N-1].

    If c > 0:
        subtract c α_n = c e_n from β; need to subtract via long-swap "+ to -".
        Each swap (e_? + e_n) -> (e_? - e_n) subtracts 2 e_n.
        Need c/2 swaps.
        Applicable iff π has >= c/2 copies (in total) of (e_? + e_n).
        Choose partner '?' canonically.

    If c < 0: opposite.
    """
    c_half = w_tilde_a[N - 1]  # so 2 c_half = c
    if c_half == 0:
        return None
    if c_half > 0:
        n_swaps = c_half
        donor_kind = 'plus'  # remove (e_? + e_n)
        receiver_kind = 'minus'
    else:
        n_swaps = -c_half
        donor_kind = 'minus'  # remove (e_? - e_n)
        receiver_kind = 'plus'

    # Find candidate (e_? + e_n) or (e_? - e_n) roots in π
    if donor_kind == 'plus':
        donors = [(long_root_plus(N, i, N - 1), long_root_minus(N, i, N - 1)) for i in range(N - 1)]
    else:
        donors = [(long_root_minus(N, i, N - 1), long_root_plus(N, i, N - 1)) for i in range(N - 1)]

    # Total count of donor-type roots
    available = [(d, r, pi.get(d, 0)) for d, r in donors]
    total = sum(c for _, _, c in available)
    if total < n_swaps:
        return None

    # Need to pick which roots to swap. For involution to work, choose canonically.
    # E.g., always swap smallest-indexed donors first.
    # Sort donors by partner index ascending.
    if partner_pref == 'smallest':
        # available is already in ascending order of partner index ?
        pass
    elif partner_pref == 'largest':
        available = list(reversed(available))

    new_pi = dict(pi)
    remaining_swaps = n_swaps
    for donor_root, recv_root, cnt in available:
        if remaining_swaps <= 0:
            break
        take = min(cnt, remaining_swaps)
        if take <= 0:
            continue
        new_pi[donor_root] = new_pi.get(donor_root, 0) - take
        if new_pi[donor_root] == 0:
            del new_pi[donor_root]
        new_pi[recv_root] = new_pi.get(recv_root, 0) + take
        remaining_swaps -= take

    new_label = s_short_w(label, N)
    return (new_label, new_pi)


def apply_aug_tilde(label, pi, tilde_a, N, priority=None):
    """Apply one step. Returns (new_label, new_pi, move_name) or (None, None, None)."""
    w_func = w_label_to_func(label, N)
    w_tilde_a = w_func(tilde_a)
    if priority is None:
        # Default: short simple first (s_n), then long simples in order s_1, s_2, ..., s_{n-1}
        priority = [('S', N - 1)] + [('L', i) for i in range(N - 1)]
    for kind, i in priority:
        if kind == 'L':
            res = try_long_simple_move(label, pi, w_tilde_a, i, N)
        else:
            res = try_short_simple_move(label, pi, w_tilde_a, N)
        if res is not None:
            return res, (kind, i)
    return None, None


# ==================== Test framework ====================

def test_injection_on_pair(lam, mu, N, priority=None, verbose=True):
    """Test that Phi := 'smallest-i swap from odd' is an INJECTION from odd to even, bidegree-preserving.

    For (SA): need injection, not full involution.
    """
    rho = tuple(Fraction(2 * N - 1 - 2 * i, 2) for i in range(N))
    tilde_a_frac = tuple(Fraction(lam[i]) + rho[i] for i in range(N))
    b_frac = tuple(Fraction(mu[i]) + rho[i] for i in range(N))
    if not all(x.denominator == 1 for x in tilde_a_frac + b_frac):
        return None
    tilde_a = tuple(int(x) for x in tilde_a_frac)
    b = tuple(int(x) for x in b_frac)

    weyl = weyl_Bn(N)
    items = []
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(N))
        if beta_w[0] < 0:
            continue
        if sum(beta_w) < 0:
            continue
        pis = all_kostant_partitions(beta_w, N)
        for pi in pis:
            bd = bidegree_of_partition(pi, N)
            items.append((label, length, pi, bd))

    # For each ODD-length item, apply Phi (any valid swap that increments parity)
    # and check it's an injection (different odd items -> different even items)
    odd_to_even = {}
    odd_unmatched = []
    for idx, (label, length, pi, bd) in enumerate(items):
        if length % 2 == 0:
            continue
        result, _ = apply_aug_tilde(label, pi, tilde_a, N, priority=priority)
        if result is None:
            odd_unmatched.append(idx)
            continue
        new_label, new_pi = result
        partner_idx = None
        for j, (lbl, lng, p, b_) in enumerate(items):
            if lbl == new_label and p == new_pi and lng % 2 == 0:
                partner_idx = j
                break
        if partner_idx is None:
            odd_unmatched.append(idx)
            continue
        # Check bidegree preserved
        if items[partner_idx][3] != bd:
            odd_unmatched.append(idx)
            continue
        odd_to_even[idx] = partner_idx

    # Check injection: no two odds map to same even
    even_targets = list(odd_to_even.values())
    is_injection = len(set(even_targets)) == len(even_targets)
    is_complete = len(odd_unmatched) == 0

    if verbose:
        print(f"\n=== B_{N} spin pair λ={lam}, μ={mu} ===")
        print(f"  tilde_a={tilde_a}, b={b}")
        print(f"  Total items: {len(items)}, odd: {sum(1 for x in items if x[1]%2==1)}")
        print(f"  Odd matched: {len(odd_to_even)}, unmatched: {len(odd_unmatched)}")
        if not is_injection:
            print(f"  ❌ NOT INJECTION (collisions)")
            from collections import Counter
            cnt = Counter(even_targets)
            for tgt, c in cnt.items():
                if c > 1:
                    odds = [k for k, v in odd_to_even.items() if v == tgt]
                    print(f"    Even {tgt} hit by odds {odds}")
                    print(f"      Even item: w={items[tgt][0]}, π={items[tgt][2]}, bd={items[tgt][3]}")
                    for o in odds:
                        print(f"      Odd item: w={items[o][0]}, π={items[o][2]}, bd={items[o][3]}")
        elif not is_complete:
            print(f"  ❌ NOT COMPLETE (some odds unmatched)")
            for o in odd_unmatched[:3]:
                print(f"    Unmatched: w={items[o][0]}, π={items[o][2]}, bd={items[o][3]}")
        else:
            print(f"  ✓ Phi is a complete injection")
    return is_injection and is_complete


def test_aug_tilde_on_pair(lam, mu, N, priority=None, verbose=True):
    """Test Aug~ on a single B_n spin pair."""
    rho = tuple(Fraction(2 * N - 1 - 2 * i, 2) for i in range(N))
    tilde_a_frac = tuple(Fraction(lam[i]) + rho[i] for i in range(N))
    b_frac = tuple(Fraction(mu[i]) + rho[i] for i in range(N))
    if not all(x.denominator == 1 for x in tilde_a_frac + b_frac):
        if verbose:
            print(f"  SKIP: tilde_a or b not integer (not spin pair?). tilde_a={tilde_a_frac}, b={b_frac}")
        return None
    tilde_a = tuple(int(x) for x in tilde_a_frac)
    b = tuple(int(x) for x in b_frac)

    if verbose:
        print(f"\n=== B_{N} spin pair λ={lam}, μ={mu} ===")
        print(f"  tilde_a = {tilde_a}, b = {b}")

    weyl = weyl_Bn(N)
    items = []
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(N))
        if beta_w[0] < 0:
            continue
        # Optimization: skip if beta_w has any "obvious" negative
        if sum(beta_w) < 0:
            continue
        pis = all_kostant_partitions(beta_w, N)
        for pi in pis:
            bd = bidegree_of_partition(pi, N)
            items.append((label, length, pi, bd))

    matched = {}
    fixed_points = []
    for idx, (label, length, pi, bd) in enumerate(items):
        result, move_info = apply_aug_tilde(label, pi, tilde_a, N, priority=priority)
        if result is None:
            fixed_points.append(idx)
        else:
            new_label, new_pi = result
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
                lbl_a, lng_a, pi_a, bd_a = items[idx]
                lbl_b, lng_b, pi_b, bd_b = items[partner]
                lbl_c, lng_c, pi_c, bd_c = items[matched.get(partner, 0)] if matched.get(partner) is not None else (None,)*4
                print(f"  ERROR: involution fails. idx={idx} -> {partner}, but {partner} -> {matched.get(partner)}")
                print(f"    [{idx}] w={lbl_a}, len={lng_a}, π={pi_a}, bd={bd_a}")
                print(f"    [{partner}] w={lbl_b}, len={lng_b}, π={pi_b}, bd={bd_b}")
                if lbl_c:
                    print(f"    [{matched[partner]}] w={lbl_c}, len={lng_c}, π={pi_c}, bd={bd_c}")
            return False
        if (items[idx][1] + items[partner][1]) % 2 != 1:
            if verbose:
                print(f"  ERROR: parity not flipped: {items[idx][1]} vs {items[partner][1]}")
            return False
        if items[idx][3] != items[partner][3]:
            if verbose:
                print(f"  ERROR: bidegree not preserved")
            return False

    bad_fp = [idx for idx in fixed_points if items[idx][1] % 2 != 0]

    if verbose:
        print(f"  Total items: {len(items)}, paired: {len(matched) // 2}, fixed: {len(fixed_points)}")
        if bad_fp:
            print(f"  ❌ FAIL: {len(bad_fp)} odd-length fixed points")
            for idx in bad_fp[:5]:
                lbl, lng, pi, bd = items[idx]
                print(f"    w={lbl}, length={lng}, pi={pi}, bidegree={bd}")
        else:
            print(f"  ✓ All fixed points even-length")

    return len(bad_fp) == 0


def main_B3():
    F = Fraction
    half = F(1, 2)
    N = 3
    test_pairs = []
    for l1 in range(4):
        for l2 in range(l1 + 1):
            for l3 in range(l2 + 1):
                lam = (l1 + half, l2 + half, l3 + half)
                for m1 in range(l1 + 1):
                    for m2 in range(m1 + 1):
                        for m3 in range(m2 + 1):
                            mu = (m1 + half, m2 + half, m3 + half)
                            test_pairs.append((lam, mu))
    print(f"Testing INJECTION Phi on {len(test_pairs)} dominant spin pairs in B_3 with λ_1 ≤ 7/2 ...")
    failures = []
    for lam, mu in test_pairs:
        ok = test_injection_on_pair(lam, mu, N, verbose=False)
        if ok is False:
            failures.append((lam, mu))
    print(f"\nB_3 dominant injection: {len(failures)}/{len(test_pairs)} failures")
    if failures:
        print("\nFirst 5 failures:")
        for lam, mu in failures[:5]:
            test_injection_on_pair(lam, mu, N, verbose=True)


if __name__ == "__main__":
    main_B3()
