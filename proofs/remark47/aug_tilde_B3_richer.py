"""
Richer Aug~ involution for B_3 spin (SA), with the FULL bidegree-preserving move set.

For each simple reflection s_i (i = 0, 1, 2) and sub-type, we have a candidate move.
Type B_3 simple roots:
  α_0 = e_0 - e_1  (long)
  α_1 = e_1 - e_2  (long)
  α_2 = e_2        (short)

For a simple reflection s_i corresponding to a long simple α_i = e_i - e_{i+1}:
  c_i = (w·a)[i] - (w·a)[i+1].
  β_{s_i w} - β_w = -c_i α_i.

  We need to realize ±c_i α_i bidegree-preservingly on π. Sub-types:

  (a) short-short swap (the original M_i in aug_tilde_Bn.py):
      For c_i > 0: replace c_i copies of e_i (short) with e_{i+1} (short).
      For c_i < 0: opposite.

  (b) long-long swap with LOW partner p < i:
      For c_i > 0: replace c_i copies of (e_p ± e_i) with (e_p ± e_{i+1}).
        Wait. Let's check: (e_p - e_i) - (e_p - e_{i+1}) = e_{i+1} - e_i = -α_i.
        So replacing (e_p - e_{i+1}) with (e_p - e_i) shifts β by -α_i (subtracts α_i).
        Hmm let's redo carefully.

      We want to subtract c_i α_i = c_i(e_i - e_{i+1}) from β.
      Removing root r and adding root r' shifts β by r' - r. We want r' - r = -α_i.
      So r' = r - α_i = r - e_i + e_{i+1}.
      Options:
        r = e_p + e_i,    r' = e_p + e_{i+1}  (both long, both with low partner p < i)
        r = e_p - e_{i+1} (which is -e_{i+1} + e_p; we have it as +e_p - e_{i+1}),
          r' = e_p - e_i. Wait. r - α_i = e_p - e_{i+1} - e_i + e_{i+1} = e_p - e_i. OK.
          But e_p - e_i with p < i is positive (it's α_p ... + α_{i-1} essentially).
          So replace (e_p - e_{i+1}) with (e_p - e_i).
      So for low partner p < i, we have two sub-sub-types:
        (b+): replace (e_p + e_i) with (e_p + e_{i+1}). [shifts by -α_i, i.e., decrements c_i]
        (b-): replace (e_p - e_{i+1}) with (e_p - e_i). [shifts by -α_i too]

      For c_i < 0, opposite direction.

  (c) long-long swap with HIGH partner q > i+1:
      r' - r = -α_i = -e_i + e_{i+1}.
      Options:
        r = e_i + e_q, r' = e_{i+1} + e_q. Diff = -e_i + e_{i+1} = -α_i. ✓
        r = e_i - e_q, r' = e_{i+1} - e_q. Diff = -e_i + e_{i+1} = -α_i. ✓
      So:
        (c+): replace (e_i + e_q) with (e_{i+1} + e_q).
        (c-): replace (e_i - e_q) with (e_{i+1} - e_q).

For the SHORT simple α_n = e_{n-1} (in our 0-indexed convention, α_2 = e_2 in B_3):
  c_2 = 2 (w·a)[N-1].
  β_{s_2 w} - β_w = -c_2 e_{N-1}.

  We need to subtract c_2 e_{N-1} from β bidegree-preservingly. Sub-types (paired with various partners ?):

  Each swap (e_? + e_{N-1}) <-> (e_? - e_{N-1}) shifts β by ∓ 2 e_{N-1}.
  Need c_2/2 swaps in total. Partners ? = 0, ..., N-2.

So sub-types for short simple are indexed by partner choice.

We allow several priority orders.
"""

from fractions import Fraction
from collections import defaultdict
from itertools import permutations, product


N = 3


# ==================== B_n root setup ====================

def positive_roots_Bn(N):
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
    v = [0] * N
    v[i] = 1
    return tuple(v)


def long_root_minus(N, i, j):
    """e_i - e_j; we expect i < j to give a positive root."""
    v = [0] * N
    v[i] = 1; v[j] = -1
    return tuple(v)


def long_root_plus(N, i, j):
    """e_i + e_j; positive for any i,j with i != j."""
    v = [0] * N
    v[i] = 1; v[j] = 1
    return tuple(v)


def positive_roots_Bn_ordered(N):
    base = positive_roots_Bn(N)
    def keyfn(item):
        r, kind = item
        for k in range(N):
            if r[k] != 0:
                return (k, r)
        return (N, r)
    return sorted(base, key=keyfn)


# ==================== Weyl group W(B_n) ====================

def weyl_Bn(N):
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


def length_of_label(label, N, pos_roots=None):
    if pos_roots is None:
        pos_roots = [r for r, _ in positive_roots_Bn(N)]
    pos_set = set(pos_roots)
    w = w_label_to_func(label, N)
    return sum(1 for r in pos_roots if w(r) not in pos_set)


def s_long_w(label, i, N):
    """Apply simple reflection s_{α_i} on the LEFT: s_i * w. α_i = e_i - e_{i+1}."""
    perm, signs = label
    new_perm = list(perm)
    new_perm[i], new_perm[i + 1] = perm[i + 1], perm[i]
    new_signs = list(signs)
    new_signs[i], new_signs[i + 1] = signs[i + 1], signs[i]
    return (tuple(new_perm), tuple(new_signs))


def s_short_w(label, N):
    """Apply simple reflection s_{α_{N-1}} = (flip last coord) on the LEFT."""
    perm, signs = label
    new_signs = list(signs)
    new_signs[N - 1] = -signs[N - 1]
    return (perm, tuple(new_signs))


# ==================== Kostant partitions ====================

def all_kostant_partitions(beta, N, pos_roots_ordered=None):
    if pos_roots_ordered is None:
        pos_roots_ordered = positive_roots_Bn_ordered(N)
    target = tuple(int(x) for x in beta)
    out = []

    leading_coords = []
    for r, _ in pos_roots_ordered:
        for k in range(N):
            if r[k] != 0:
                leading_coords.append(k)
                break
    boundary = [None] * N
    for k in range(N):
        for i in range(len(pos_roots_ordered)):
            if leading_coords[i] > k:
                boundary[k] = i
                break
        else:
            boundary[k] = len(pos_roots_ordered)

    def recurse(idx, remaining, partial):
        for k in range(N):
            if idx >= boundary[k] and remaining[k] != 0:
                return
        if idx == len(pos_roots_ordered):
            if all(r == 0 for r in remaining):
                out.append(dict(partial))
            return
        root, kind = pos_roots_ordered[idx]
        lc = leading_coords[idx]
        rem_lc = remaining[lc]
        if rem_lc < 0:
            return
        max_n = rem_lc
        for n in range(max_n + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(N))
            new_partial = dict(partial)
            if n > 0:
                new_partial[root] = n
            recurse(idx + 1, new_rem, new_partial)

    recurse(0, target, {})
    return out


def bidegree_of_partition(pi, N):
    pos_roots = positive_roots_Bn(N)
    long_set = set(r for r, k in pos_roots if k == 'L')
    short_set = set(r for r, k in pos_roots if k == 'S')
    long_cnt = sum(mult for root, mult in pi.items() if root in long_set)
    short_cnt = sum(mult for root, mult in pi.items() if root in short_set)
    return (long_cnt, short_cnt)


# ==================== Move sub-types ====================

# Each move is keyed by (kind, i, sub-type-tag). It has:
#   - applicability condition
#   - effect on (label, π).
# All produce s_i * w (the new w-label) and a new π with the same bidegree.

# For LONG simple α_i = e_i - e_{i+1} (i in 0..N-2):
#   Sub-type (a): short-short swap.
#       direction: depends on sign of c_i.
#       c_i > 0: remove c_i copies of e_i (short), add c_i copies of e_{i+1} (short).
#       c_i < 0: remove |c_i| copies of e_{i+1} (short), add |c_i| copies of e_i (short).
#
#   Sub-type (b+, p) with p < i: low-partner long-long with + sign.
#       c_i > 0: remove c_i copies of (e_p + e_i), add c_i copies of (e_p + e_{i+1}).
#       c_i < 0: remove |c_i| copies of (e_p + e_{i+1}), add |c_i| copies of (e_p + e_i).
#
#   Sub-type (b-, p) with p < i: low-partner long-long with - sign.
#       c_i > 0: remove c_i copies of (e_p - e_{i+1}), add c_i copies of (e_p - e_i).
#                Wait let me double-check. We need to add -α_i = -e_i + e_{i+1} to β.
#                Remove r (subtract r), add r' (add r'). Net effect: r' - r added to β.
#                Need r' - r = -α_i = -e_i + e_{i+1}.
#                  (e_p - e_i) - (e_p - e_{i+1}) = -e_i + e_{i+1} = -α_i. ✓
#                  So remove (e_p - e_{i+1}), add (e_p - e_i). YES.
#                But wait that ADDS -α_i to β. To go from (w, π) to (s_i w, π'):
#                β shifts by -c_i α_i. If c_i > 0, β decreases by c_i α_i.
#                So we need to add (-c_i α_i) = -c_i (e_i - e_{i+1}) — i.e., the swap r'-r should have sum = -α_i,
#                applied c_i times.
#                Each swap removes 1 (e_p - e_{i+1}), adds 1 (e_p - e_i). So per swap, β decreases by α_i. Need c_i swaps.
#       c_i > 0: remove c_i copies of (e_p - e_{i+1}), add c_i copies of (e_p - e_i).
#       c_i < 0: opposite.
#
#   Sub-type (c+, q) with q > i+1: high-partner with + sign.
#       per swap: remove (e_i + e_q), add (e_{i+1} + e_q). Diff = -α_i. ✓
#   Sub-type (c-, q) with q > i+1: high-partner with - sign.
#       per swap: remove (e_i - e_q), add (e_{i+1} - e_q). Diff = -α_i. ✓
#
# For SHORT simple α_{N-1} = e_{N-1}:
#   c = 2 (w·a)[N-1]; need c/2 swaps.
#   Each sub-type chooses a partner ? in 0..N-2.
#   Sub-type (S, p, sign='plus') with p < N-1:
#       c > 0: remove (e_p + e_{N-1}), add (e_p - e_{N-1}). Diff = -2 e_{N-1}. ✓
#       Need c/2 swaps using this exact partner; applicable iff π has >= c/2 copies of (e_p + e_{N-1}).
#       NOTE: we choose to use a SINGLE partner per move. If a single partner doesn't have enough copies,
#       this sub-type fails and we try another partner.

def all_moves(N):
    """List all (kind, i, subtype_tag) move signatures (PURE single-subtype moves)."""
    moves = []
    # Long simples
    for i in range(N - 1):
        moves.append(('L', i, ('a',)))  # short-short
        for p in range(i):
            moves.append(('L', i, ('b+', p)))
            moves.append(('L', i, ('b-', p)))
        for q in range(i + 2, N):
            moves.append(('L', i, ('c+', q)))
            moves.append(('L', i, ('c-', q)))
    # Short simple
    for p in range(N - 1):
        moves.append(('S', N - 1, ('S', p)))
    return moves


def subtype_donor_receiver(kind, i, subtype, c, N):
    """Return (donor, receiver) roots for a single swap of this subtype, given sign of c."""
    if kind == 'L':
        tag = subtype[0]
        if tag == 'a':
            if c > 0:
                return short_root(N, i), short_root(N, i + 1)
            else:
                return short_root(N, i + 1), short_root(N, i)
        elif tag == 'b+':
            p = subtype[1]
            if c > 0:
                return long_root_plus(N, p, i), long_root_plus(N, p, i + 1)
            else:
                return long_root_plus(N, p, i + 1), long_root_plus(N, p, i)
        elif tag == 'b-':
            p = subtype[1]
            if c > 0:
                return long_root_minus(N, p, i + 1), long_root_minus(N, p, i)
            else:
                return long_root_minus(N, p, i), long_root_minus(N, p, i + 1)
        elif tag == 'c+':
            q = subtype[1]
            if c > 0:
                return long_root_plus(N, i, q), long_root_plus(N, i + 1, q)
            else:
                return long_root_plus(N, i + 1, q), long_root_plus(N, i, q)
        elif tag == 'c-':
            q = subtype[1]
            if c > 0:
                return long_root_minus(N, i, q), long_root_minus(N, i + 1, q)
            else:
                return long_root_minus(N, i + 1, q), long_root_minus(N, i, q)
    else:  # 'S'
        p = subtype[1]
        if c > 0:
            return long_root_plus(N, p, N - 1), long_root_minus(N, p, N - 1)
        else:
            return long_root_minus(N, p, N - 1), long_root_plus(N, p, N - 1)


def subtypes_for_simple(kind, i, N):
    """List subtypes for the simple reflection (kind, i)."""
    if kind == 'L':
        out = [('a',)]
        for p in range(i):
            out.append(('b+', p))
            out.append(('b-', p))
        for q in range(i + 2, N):
            out.append(('c+', q))
            out.append(('c-', q))
        return out
    else:
        return [('S', p) for p in range(N - 1)]


def enumerate_mixed_moves(label, pi, w_tilde_a, kind, i, N, subtype_priority=None):
    """Enumerate all valid 'mixed-subtype' moves for the simple reflection (kind, i).

    Each move is a multiset of subtype usages summing to |c_i| total swaps (or |c_half| for short simple),
    with each subtype having enough donor in π.

    Returns list of dicts: each dict maps subtype -> count. Sorted by some canonical order.
    """
    if kind == 'L':
        c = w_tilde_a[i] - w_tilde_a[i + 1]
        if c == 0:
            return []
        n_total = abs(c)
    else:
        c_half = w_tilde_a[N - 1]
        if c_half == 0:
            return []
        n_total = abs(c_half)
        c = c_half  # sign

    subtypes = subtypes_for_simple(kind, i, N)
    if subtype_priority is not None:
        subtypes = [s for s in subtype_priority if s in subtypes]

    # For each subtype, find donor and how many copies are in π.
    capacity = {}
    donor_of = {}
    receiver_of = {}
    for st in subtypes:
        donor, recv = subtype_donor_receiver(kind, i, st, c, N)
        capacity[st] = pi.get(donor, 0)
        donor_of[st] = donor
        receiver_of[st] = recv

    # Enumerate distributions: assignments {st: n_st} with sum n_st = n_total, n_st <= capacity[st].
    out = []
    sts_list = subtypes

    def recurse(idx, remaining, partial):
        if idx == len(sts_list):
            if remaining == 0:
                out.append(dict(partial))
            return
        st = sts_list[idx]
        cap = capacity[st]
        max_take = min(cap, remaining)
        for n in range(max_take + 1):
            if n > 0:
                partial[st] = n
            recurse(idx + 1, remaining - n, partial)
            if n > 0:
                del partial[st]

    recurse(0, n_total, {})
    return out


def apply_mixed_move(label, pi, w_tilde_a, kind, i, distribution, N):
    """Apply a mixed move: distribution is dict {subtype: count}. Returns (new_label, new_pi)."""
    if kind == 'L':
        c = w_tilde_a[i] - w_tilde_a[i + 1]
    else:
        c = w_tilde_a[N - 1]
    new_pi = dict(pi)
    for st, n in distribution.items():
        donor, recv = subtype_donor_receiver(kind, i, st, c, N)
        new_pi[donor] = new_pi.get(donor, 0) - n
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[recv] = new_pi.get(recv, 0) + n
    if kind == 'L':
        new_label = s_long_w(label, i, N)
    else:
        new_label = s_short_w(label, N)
    return (new_label, new_pi)


def try_move(label, pi, w_tilde_a, kind, i, subtype, N):
    """Try the move (kind, i, subtype) on (label, pi). Returns (new_label, new_pi) or None."""
    if kind == 'L':
        c = w_tilde_a[i] - w_tilde_a[i + 1]
        if c == 0:
            return None
        n_swaps = abs(c)
        # Determine donor/receiver based on subtype and sign of c
        tag = subtype[0]
        if tag == 'a':
            if c > 0:
                donor = short_root(N, i)
                receiver = short_root(N, i + 1)
            else:
                donor = short_root(N, i + 1)
                receiver = short_root(N, i)
        elif tag == 'b+':
            p = subtype[1]
            assert p < i
            if c > 0:
                donor = long_root_plus(N, p, i)
                receiver = long_root_plus(N, p, i + 1)
            else:
                donor = long_root_plus(N, p, i + 1)
                receiver = long_root_plus(N, p, i)
        elif tag == 'b-':
            p = subtype[1]
            assert p < i
            if c > 0:
                donor = long_root_minus(N, p, i + 1)
                receiver = long_root_minus(N, p, i)
            else:
                donor = long_root_minus(N, p, i)
                receiver = long_root_minus(N, p, i + 1)
        elif tag == 'c+':
            q = subtype[1]
            assert q > i + 1
            if c > 0:
                donor = long_root_plus(N, i, q)
                receiver = long_root_plus(N, i + 1, q)
            else:
                donor = long_root_plus(N, i + 1, q)
                receiver = long_root_plus(N, i, q)
        elif tag == 'c-':
            q = subtype[1]
            assert q > i + 1
            if c > 0:
                donor = long_root_minus(N, i, q)
                receiver = long_root_minus(N, i + 1, q)
            else:
                donor = long_root_minus(N, i + 1, q)
                receiver = long_root_minus(N, i, q)
        else:
            return None
        if pi.get(donor, 0) < n_swaps:
            return None
        new_pi = dict(pi)
        new_pi[donor] -= n_swaps
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
        new_label = s_long_w(label, i, N)
        return (new_label, new_pi)
    else:  # 'S'
        c_half = w_tilde_a[N - 1]
        if c_half == 0:
            return None
        n_swaps = abs(c_half)
        tag = subtype[0]
        assert tag == 'S'
        p = subtype[1]
        assert p < N - 1
        if c_half > 0:
            donor = long_root_plus(N, p, N - 1)
            receiver = long_root_minus(N, p, N - 1)
        else:
            donor = long_root_minus(N, p, N - 1)
            receiver = long_root_plus(N, p, N - 1)
        if pi.get(donor, 0) < n_swaps:
            return None
        new_pi = dict(pi)
        new_pi[donor] -= n_swaps
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
        new_label = s_short_w(label, N)
        return (new_label, new_pi)


# ==================== Priority orders ====================

def priority_lex(N):
    """P_lex: lex over (i, subtype-rank) where (a) < (b+,p ascending) ~ (b-,p ascending) < (c+,q ascending) ~ (c-,q ascending)."""
    out = []
    # Sort by i first
    for i in range(N - 1):
        out.append(('L', i, ('a',)))
    # Then short simple
    out.append(('S', N - 1, ('S', 0)))
    for p in range(1, N - 1):
        out.append(('S', N - 1, ('S', p)))
    # Then long simples with non-(a) subtypes
    for i in range(N - 1):
        for p in range(i):
            out.append(('L', i, ('b+', p)))
            out.append(('L', i, ('b-', p)))
        for q in range(i + 2, N):
            out.append(('L', i, ('c+', q)))
            out.append(('L', i, ('c-', q)))
    return out


def priority_short_first(N):
    """Prefer short simple s_{N-1} first (across partner choices), then long."""
    out = []
    for p in range(N - 1):
        out.append(('S', N - 1, ('S', p)))
    for i in range(N - 1):
        out.append(('L', i, ('a',)))
        for p in range(i):
            out.append(('L', i, ('b+', p)))
            out.append(('L', i, ('b-', p)))
        for q in range(i + 2, N):
            out.append(('L', i, ('c+', q)))
            out.append(('L', i, ('c-', q)))
    return out


def priority_morris(N):
    """Prefer the move that decreases the first coordinate of β.

    For long simple s_i with c_i > 0: applying decreases (w·a)[i] (i.e., first coord if i=0).
    For long simple s_i with c_i < 0: applying increases.
    For short s_{N-1} with c > 0: doesn't change first coord (only last coord changes).

    Heuristic interpretation: prefer s_0 (long, swaps coords 0 and 1) when c_0 > 0.
    Order: s_0 forward, s_1 forward, ..., s_{N-2} forward, s_{N-1}, then reverse moves.

    But sub-type also matters. Convention: try (a) first, then (b)/(c) within each (i).
    """
    out = []
    # i = 0, 1, ..., N-2: long simples in order (so s_0 first)
    for i in range(N - 1):
        out.append(('L', i, ('a',)))
        for p in range(i):
            out.append(('L', i, ('b+', p)))
            out.append(('L', i, ('b-', p)))
        for q in range(i + 2, N):
            out.append(('L', i, ('c+', q)))
            out.append(('L', i, ('c-', q)))
    for p in range(N - 1):
        out.append(('S', N - 1, ('S', p)))
    return out


def priority_descent(N):
    """Like P_lex but ONLY consider moves where ℓ(s_i w) < ℓ(w) (right descents)."""
    # We can't precompute this without w; this is filtered at apply time.
    return priority_lex(N)


def priority_long_first(N):
    """Prefer long simples first (i = N-2 down to 0), then short. Within each i, (a) first."""
    out = []
    for i in range(N - 2, -1, -1):
        out.append(('L', i, ('a',)))
        for p in range(i):
            out.append(('L', i, ('b+', p)))
            out.append(('L', i, ('b-', p)))
        for q in range(i + 2, N):
            out.append(('L', i, ('c+', q)))
            out.append(('L', i, ('c-', q)))
    for p in range(N - 1):
        out.append(('S', N - 1, ('S', p)))
    return out


def priority_subtype_a_first(N):
    """Prefer subtype (a) for ALL i first, then short, then b/c."""
    out = []
    for i in range(N - 1):
        out.append(('L', i, ('a',)))
    for p in range(N - 1):
        out.append(('S', N - 1, ('S', p)))
    for i in range(N - 1):
        for p in range(i):
            out.append(('L', i, ('b+', p)))
            out.append(('L', i, ('b-', p)))
        for q in range(i + 2, N):
            out.append(('L', i, ('c+', q)))
            out.append(('L', i, ('c-', q)))
    return out


def priority_high_first(N):
    """Prefer high-partner moves first. (Speculative)"""
    out = []
    for i in range(N - 1):
        for q in range(i + 2, N):
            out.append(('L', i, ('c+', q)))
            out.append(('L', i, ('c-', q)))
        out.append(('L', i, ('a',)))
        for p in range(i):
            out.append(('L', i, ('b+', p)))
            out.append(('L', i, ('b-', p)))
    for p in range(N - 1):
        out.append(('S', N - 1, ('S', p)))
    return out


PRIORITY_REGISTRY = {
    'P_lex': priority_lex,
    'P_short_first': priority_short_first,
    'P_morris': priority_morris,
    'P_descent': priority_descent,
    'P_long_first': priority_long_first,
    'P_subtype_a_first': priority_subtype_a_first,
    'P_high_first': priority_high_first,
}


# ==================== Apply Aug~ ====================

def is_right_descent(label, kind, i, N, pos_roots=None):
    """ℓ(s_i w) < ℓ(w) iff w^{-1}(α_i) is a negative root, where α_i is the chosen simple root."""
    if kind == 'L':
        # α_i = e_i - e_{i+1}
        # We want to know if s_i*w has length < length of w. By definition of left action,
        # ℓ(s_i w) = ℓ(w) - 1 iff s_i is a *left* descent of w iff w^{-1}(α_i) < 0.
        # Equivalently iff α_i applied as left-mult shortens w iff w sends some positive root α with w(α) = α_i? No.
        # The standard fact: s_i is a left descent iff s_i*w has shorter length iff w^{-1}(α_i) < 0.
        perm, signs = label
        # Compute w^{-1}(α_i):
        # w(v) = (signs[k] v[perm[k]])_k. So w^{-1}: if w(u) = v, then u[perm[k]] = signs[k] v[k]
        # i.e., u[m] = signs[perm^{-1}(m)] v[perm^{-1}(m)].
        # Let inv[m] = perm^{-1}(m) (i.e., inv[perm[k]] = k).
        inv = [0] * N
        for k in range(N):
            inv[perm[k]] = k
        # w^{-1}(α_i) = w^{-1}(e_i) - w^{-1}(e_{i+1})
        # w^{-1}(e_i): u[m] = signs[inv[m]] (e_i)[inv[m]] = signs[inv[m]] * (1 if inv[m]==i else 0)
        # i.e., u has +signs[k] at position perm[k] where k = i. So u = signs[i] * e_{perm[i]} actually no wait.
        # Let's just compute directly: define w_inv as a function.
        # If w(perm, signs) is v -> (signs[k] v[perm[k]])_k, the inverse signed permutation has
        # perm^{-1} = inv, signs^{-1}[k] = signs[inv[k]].
        # Indeed: w_inv(v) where w_inv has perm_inv = inv and signs_inv[k] = signs[inv[k]].
        # Apply: w(w_inv(v))[k] = signs[k] * w_inv(v)[perm[k]] = signs[k] * signs_inv[perm[k]] * v[inv[perm[k]]]
        #                      = signs[k] * signs[inv[perm[k]]] * v[k] = signs[k]*signs[k]*v[k] = v[k]. ✓
        signs_inv = tuple(signs[inv[k]] for k in range(N))
        # w^{-1}(e_i) has at coord k: signs_inv[k] * (e_i)[inv[k]] = signs_inv[k] if inv[k]==i else 0
        # i.e., nonzero at k = perm[i], with value signs_inv[perm[i]] = signs[inv[perm[i]]] = signs[i].
        # So w^{-1}(e_i) = signs[i] * e_{perm[i]}.
        # Similarly w^{-1}(e_{i+1}) = signs[i+1] * e_{perm[i+1]}.
        u = [0] * N
        u[perm[i]] += signs[i]
        u[perm[i + 1]] -= signs[i + 1]
        u = tuple(u)
        # Is u a negative root?
        if pos_roots is None:
            pos_roots = set(r for r, _ in positive_roots_Bn(N))
        neg_roots = set(tuple(-x for x in r) for r in pos_roots)
        return u in neg_roots
    else:  # 'S'
        # α_{N-1} = e_{N-1}
        perm, signs = label
        # w^{-1}(e_{N-1}) = signs[N-1] * e_{perm[N-1]}
        u = [0] * N
        u[perm[N - 1]] = signs[N - 1]
        u = tuple(u)
        if pos_roots is None:
            pos_roots = set(r for r, _ in positive_roots_Bn(N))
        neg_roots = set(tuple(-x for x in r) for r in pos_roots)
        return u in neg_roots


def apply_aug_tilde(label, pi, tilde_a, N, priority_list, descent_only=False):
    """OLD: try pure moves in priority order."""
    w_func = w_label_to_func(label, N)
    w_tilde_a = w_func(tilde_a)
    pos_roots_set = set(r for r, _ in positive_roots_Bn(N))
    for kind, i, subtype in priority_list:
        if descent_only:
            if not is_right_descent(label, kind, i, N, pos_roots_set):
                continue
        res = try_move(label, pi, w_tilde_a, kind, i, subtype, N)
        if res is not None:
            return res, (kind, i, subtype)
    return (None, None), None


def apply_aug_tilde_mixed(label, pi, tilde_a, N, simple_priority, subtype_priority_fn=None,
                          descent_only=False, simple_pri_mode='order'):
    """Try MIXED moves: for each simple reflection (in priority order), pick a canonical mixed distribution.

    simple_priority: either a list of (kind, i) pairs OR (if simple_pri_mode != 'order') a callable.
    simple_pri_mode:
        'order': simple_priority is a fixed list; iterate in that order.
        'max_c': dynamically pick simple reflection with largest |c|, breaking ties by simple_priority list.
        'min_c': pick smallest nonzero |c|.

    subtype_priority_fn(kind, i, N): returns list of subtypes in priority order.
    """
    w_func = w_label_to_func(label, N)
    w_tilde_a = w_func(tilde_a)
    pos_roots_set = set(r for r, _ in positive_roots_Bn(N))

    if simple_pri_mode == 'order':
        order = list(simple_priority)
    else:
        # Compute |c| for each simple reflection, then sort.
        candidates = []
        for kind, i in simple_priority:
            if kind == 'L':
                c = w_tilde_a[i] - w_tilde_a[i + 1]
            else:
                c = w_tilde_a[N - 1]
            if c == 0:
                continue
            if descent_only and not is_right_descent(label, kind, i, N, pos_roots_set):
                continue
            candidates.append((abs(c), simple_priority.index((kind, i)), kind, i))
        if simple_pri_mode == 'max_c':
            candidates.sort(key=lambda x: (-x[0], x[1]))
        elif simple_pri_mode == 'min_c':
            candidates.sort(key=lambda x: (x[0], x[1]))
        order = [(k, i) for (_, _, k, i) in candidates]

    for kind, i in order:
        if simple_pri_mode == 'order' and descent_only:
            if not is_right_descent(label, kind, i, N, pos_roots_set):
                continue
        if kind == 'L':
            c = w_tilde_a[i] - w_tilde_a[i + 1]
        else:
            c = w_tilde_a[N - 1]
        if c == 0:
            continue
        n_total = abs(c)

        if subtype_priority_fn is None:
            subtypes = subtypes_for_simple(kind, i, N)
        else:
            subtypes = subtype_priority_fn(kind, i, N)

        capacity = {}
        for st in subtypes:
            donor, recv = subtype_donor_receiver(kind, i, st, c, N)
            capacity[st] = pi.get(donor, 0)

        remaining = n_total
        distribution = {}
        for st in subtypes:
            if remaining <= 0:
                break
            take = min(capacity[st], remaining)
            if take > 0:
                distribution[st] = take
                remaining -= take

        if remaining > 0:
            continue
        new_label, new_pi = apply_mixed_move(label, pi, w_tilde_a, kind, i, distribution, N)
        return (new_label, new_pi), (kind, i, distribution)
    return (None, None), None


# Subtype priority functions
def subtype_priority_lex(kind, i, N):
    """(a) first, then (b+,p) ascending p, (b-,p) ascending p, (c+,q) ascending q, (c-,q) ascending q."""
    out = []
    if kind == 'L':
        out.append(('a',))
        for p in range(i):
            out.append(('b+', p))
        for p in range(i):
            out.append(('b-', p))
        for q in range(i + 2, N):
            out.append(('c+', q))
        for q in range(i + 2, N):
            out.append(('c-', q))
    else:
        for p in range(N - 1):
            out.append(('S', p))
    return out


def subtype_priority_a_first(kind, i, N):
    return subtype_priority_lex(kind, i, N)


def subtype_priority_high_first(kind, i, N):
    """(c) first, then (a), then (b)."""
    out = []
    if kind == 'L':
        for q in range(i + 2, N):
            out.append(('c+', q))
        for q in range(i + 2, N):
            out.append(('c-', q))
        out.append(('a',))
        for p in range(i):
            out.append(('b+', p))
        for p in range(i):
            out.append(('b-', p))
    else:
        for p in range(N - 1):
            out.append(('S', p))
    return out


def subtype_priority_low_first(kind, i, N):
    """(b) first, then (a), then (c)."""
    out = []
    if kind == 'L':
        for p in range(i):
            out.append(('b+', p))
        for p in range(i):
            out.append(('b-', p))
        out.append(('a',))
        for q in range(i + 2, N):
            out.append(('c+', q))
        for q in range(i + 2, N):
            out.append(('c-', q))
    else:
        for p in range(N - 1):
            out.append(('S', p))
    return out


def simple_priority_short_first(N):
    out = [('S', N - 1)]
    for i in range(N - 1):
        out.append(('L', i))
    return out


def simple_priority_lex(N):
    out = []
    for i in range(N - 1):
        out.append(('L', i))
    out.append(('S', N - 1))
    return out


def simple_priority_long_first(N):
    out = []
    for i in range(N - 2, -1, -1):
        out.append(('L', i))
    out.append(('S', N - 1))
    return out


def simple_priority_morris(N):
    """s_0 first (so s_0 favored when it shrinks first coord), then s_1, ..., s_{N-2}, then short."""
    out = []
    for i in range(N - 1):
        out.append(('L', i))
    out.append(('S', N - 1))
    return out


SIMPLE_PRIORITY_REGISTRY = {
    'short_first': simple_priority_short_first,
    'lex': simple_priority_lex,
    'long_first': simple_priority_long_first,
    'morris': simple_priority_morris,
}

SUBTYPE_PRIORITY_REGISTRY = {
    'a_first': subtype_priority_a_first,
    'high_first': subtype_priority_high_first,
    'low_first': subtype_priority_low_first,
}


# ==================== Test framework ====================

def collect_items(lam, mu, N):
    """Return (tilde_a, b, items=[(label, length, pi, bidegree), ...])."""
    rho = tuple(Fraction(2 * N - 1 - 2 * i, 2) for i in range(N))
    tilde_a_frac = tuple(Fraction(lam[i]) + rho[i] for i in range(N))
    b_frac = tuple(Fraction(mu[i]) + rho[i] for i in range(N))
    if not all(x.denominator == 1 for x in tilde_a_frac + b_frac):
        return None, None, None
    tilde_a = tuple(int(x) for x in tilde_a_frac)
    b = tuple(int(x) for x in b_frac)
    weyl = weyl_Bn(N)
    pos_roots_ord = positive_roots_Bn_ordered(N)
    items = []
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(N))
        if beta_w[0] < 0:
            continue
        if sum(beta_w) < 0:
            continue
        pis = all_kostant_partitions(beta_w, N, pos_roots_ord)
        for pi in pis:
            bd = bidegree_of_partition(pi, N)
            items.append((label, length, pi, bd))
    return tilde_a, b, items


def test_aug_tilde_on_pair(lam, mu, N, priority_list=None, descent_only=False, verbose=False,
                           simple_priority=None, subtype_priority_fn=None, use_mixed=False,
                           mode='injection', simple_pri_mode='order'):
    """Run Aug~ on (λ, μ).

    mode='injection': test that map odd→even (defined by Aug~ on odd items) is a bidegree-preserving INJECTION.
    mode='involution': test that Aug~ on ALL items is a sign-reversing involution with even-length fixed points.
    """
    tilde_a, b, items = collect_items(lam, mu, N)
    if items is None:
        return None
    matched = {}  # odd -> even (in injection mode); both ways (in involution mode)
    fixed_points = []
    move_used = {}
    for idx, (label, length, pi, bd) in enumerate(items):
        if mode == 'injection' and length % 2 == 0:
            continue  # Only apply Aug~ on odd items
        if use_mixed:
            result, move_info = apply_aug_tilde_mixed(
                label, pi, tilde_a, N, simple_priority, subtype_priority_fn=subtype_priority_fn,
                descent_only=descent_only, simple_pri_mode=simple_pri_mode)
        else:
            result, move_info = apply_aug_tilde(label, pi, tilde_a, N, priority_list, descent_only=descent_only)
        if result == (None, None):
            fixed_points.append(idx)
        else:
            new_label, new_pi = result
            partner_idx = None
            for j, (lbl, lng, p, bd_j) in enumerate(items):
                if lbl == new_label and p == new_pi:
                    partner_idx = j
                    break
            if partner_idx is None:
                fixed_points.append(idx)
                if verbose:
                    print(f"  Item {idx} applied move {move_info} but partner not in items! "
                          f"w={label}, pi={pi}, bd={bd}, target=(lbl={new_label}, pi={new_pi})")
                continue
            matched[idx] = partner_idx
            move_used[idx] = move_info

    fail_examples = []
    if mode == 'injection':
        # Check: every odd has a match (injective into even), bidegree-preserving, parity-flipping.
        all_odd = [idx for idx, (lbl, lng, pi, bd) in enumerate(items) if lng % 2 == 1]
        unmatched = [idx for idx in all_odd if idx not in matched]
        odd_targets = list(matched.values())
        is_injection = len(set(odd_targets)) == len(odd_targets)
        n_collisions = 0
        if not is_injection:
            from collections import Counter
            cnt = Counter(odd_targets)
            for tgt, c in cnt.items():
                if c > 1:
                    odds_to_tgt = [k for k, v in matched.items() if v == tgt]
                    n_collisions += 1
                    fail_examples.append({
                        'type': 'collision',
                        'target': tgt,
                        'target_item': items[tgt],
                        'odds': odds_to_tgt,
                        'odd_items': [items[o] for o in odds_to_tgt],
                        'moves_used': [move_used.get(o) for o in odds_to_tgt],
                    })
        for idx in unmatched:
            fail_examples.append({
                'type': 'unmatched_odd',
                'idx': idx,
                'item': items[idx],
            })
        for idx, partner in matched.items():
            if (items[idx][1] + items[partner][1]) % 2 != 1:
                fail_examples.append({'type': 'parity', 'idx': idx, 'partner': partner,
                                      'item': items[idx], 'partner_item': items[partner]})
            if items[idx][3] != items[partner][3]:
                fail_examples.append({'type': 'bidegree', 'idx': idx, 'partner': partner,
                                      'item': items[idx], 'partner_item': items[partner]})
        is_complete = is_injection and not unmatched and \
            all((items[idx][1] + items[partner][1]) % 2 == 1 and items[idx][3] == items[partner][3]
                for idx, partner in matched.items())
        return {
            'is_complete': is_complete,
            'is_injection': is_injection,
            'n_unmatched': len(unmatched),
            'n_collisions': n_collisions,
            'fail_examples': fail_examples[:5],
            'n_items': len(items),
            'n_odd': len(all_odd),
            'n_matched': len(matched),
        }
    else:  # involution mode
        is_involution = True
        for idx, partner in matched.items():
            if matched.get(partner) != idx:
                is_involution = False
                fail_examples.append({
                    'type': 'not-self-inverse',
                    'idx': idx, 'partner': partner,
                    'item': items[idx], 'partner_item': items[partner],
                    'partner_partner': items[matched[partner]] if matched.get(partner) is not None else None,
                    'move_used': move_used.get(idx),
                    'move_used_partner': move_used.get(partner),
                })
            if (items[idx][1] + items[partner][1]) % 2 != 1:
                is_involution = False
            if items[idx][3] != items[partner][3]:
                is_involution = False
        bad_fp = [idx for idx in fixed_points if items[idx][1] % 2 != 0]
        is_complete = is_involution and not bad_fp
        return {
            'is_complete': is_complete,
            'is_involution': is_involution,
            'odd_fixed_points': [items[idx] for idx in bad_fp],
            'fail_examples': fail_examples[:5],
            'n_items': len(items),
            'n_matched': len(matched) // 2,
            'n_fixed': len(fixed_points),
            'n_odd_fixed': len(bad_fp),
        }


def enumerate_dominant_spin_pairs(max_lam1_int, N):
    """Enumerate dominant spin pairs (λ, μ) with λ_1 ≤ max_lam1_int + 1/2."""
    F = Fraction
    half = F(1, 2)
    pairs = []
    if N == 3:
        for l1 in range(max_lam1_int + 1):
            for l2 in range(l1 + 1):
                for l3 in range(l2 + 1):
                    lam = (l1 + half, l2 + half, l3 + half)
                    for m1 in range(l1 + 1):
                        for m2 in range(m1 + 1):
                            for m3 in range(m2 + 1):
                                mu = (m1 + half, m2 + half, m3 + half)
                                pairs.append((lam, mu))
    return pairs


def run_priority(priority_name, N, max_lam1_int, descent_only=False, verbose_first_n=2):
    """Run a (pure-subtype) priority order on all pairs and return results."""
    priority_fn = PRIORITY_REGISTRY[priority_name]
    priority_list = priority_fn(N)
    pairs = enumerate_dominant_spin_pairs(max_lam1_int, N)
    n_pairs = len(pairs)
    n_complete = 0
    n_involution = 0
    n_failed = 0
    failures = []
    for lam, mu in pairs:
        res = test_aug_tilde_on_pair(lam, mu, N, priority_list=priority_list, descent_only=descent_only)
        if res is None:
            continue
        if res['is_complete']:
            n_complete += 1
        elif res['is_involution']:
            n_involution += 1
            failures.append((lam, mu, res))
        else:
            n_failed += 1
            failures.append((lam, mu, res))
    return {
        'priority_name': priority_name,
        'descent_only': descent_only,
        'n_pairs': n_pairs,
        'n_complete': n_complete,
        'n_involution_only': n_involution,
        'n_failed': n_failed,
        'failures': failures[:verbose_first_n],
        'all_failures_count': len(failures),
    }


def run_mixed_priority(simple_pri_name, subtype_pri_name, N, max_lam1_int,
                       descent_only=False, verbose_first_n=2, mode='injection',
                       simple_pri_mode='order'):
    """Run a (simple, subtype) MIXED priority pair on all pairs."""
    simple_pri = SIMPLE_PRIORITY_REGISTRY[simple_pri_name](N)
    subtype_pri_fn = SUBTYPE_PRIORITY_REGISTRY[subtype_pri_name]
    pairs = enumerate_dominant_spin_pairs(max_lam1_int, N)
    n_complete = 0
    n_failed = 0
    failures = []
    for lam, mu in pairs:
        res = test_aug_tilde_on_pair(
            lam, mu, N, simple_priority=simple_pri,
            subtype_priority_fn=subtype_pri_fn, use_mixed=True,
            descent_only=descent_only, mode=mode, simple_pri_mode=simple_pri_mode)
        if res is None:
            continue
        if res['is_complete']:
            n_complete += 1
        else:
            n_failed += 1
            failures.append((lam, mu, res))
    return {
        'priority_name': f"{simple_pri_name}/{subtype_pri_name}/{simple_pri_mode}",
        'descent_only': descent_only,
        'mode': mode,
        'n_pairs': len(pairs),
        'n_complete': n_complete,
        'n_failed': n_failed,
        'failures': failures[:verbose_first_n],
        'all_failures_count': len(failures),
    }


# ==================== Observational mode ====================

def list_applicable_moves(label, pi, tilde_a, N, all_moves_list):
    """For (label, pi), return all moves that apply (don't pick by priority)."""
    w_func = w_label_to_func(label, N)
    w_tilde_a = w_func(tilde_a)
    out = []
    for kind, i, subtype in all_moves_list:
        res = try_move(label, pi, w_tilde_a, kind, i, subtype, N)
        if res is not None:
            out.append(((kind, i, subtype), res))
    return out


def observational_scan(N, max_lam1_int):
    """Scan all dominant spin pairs and odd-length items.
    For each odd item, list applicable PURE moves and report stats:
      - distribution of #applicable moves (per item)
      - items with 0 moves: a true obstruction in the PURE move set
    """
    pairs = enumerate_dominant_spin_pairs(max_lam1_int, N)
    moves_list = all_moves(N)
    move_count_distribution = defaultdict(int)
    items_with_zero_moves = []
    items_with_one_move = []

    for lam, mu in pairs:
        tilde_a, b, items = collect_items(lam, mu, N)
        if items is None:
            continue
        for label, length, pi, bd in items:
            if length % 2 == 0:
                continue
            applicable = list_applicable_moves(label, pi, tilde_a, N, moves_list)
            move_count_distribution[len(applicable)] += 1
            if len(applicable) == 0:
                items_with_zero_moves.append((lam, mu, label, length, pi, bd))
            elif len(applicable) == 1:
                items_with_one_move.append((lam, mu, label, length, pi, bd, applicable[0][0]))
    return {
        'distribution': dict(move_count_distribution),
        'zero_move_items': items_with_zero_moves,
        'one_move_items_count': len(items_with_one_move),
    }


def observational_scan_mixed(N, max_lam1_int):
    """Scan all odd items: count applicable SIMPLE REFLECTIONS (with mixed subtypes).

    Returns:
       distribution of (# of applicable simple reflections), per odd item.
       items with 0 applicable simple reflections (genuine obstruction).
    """
    pairs = enumerate_dominant_spin_pairs(max_lam1_int, N)
    distribution = defaultdict(int)
    zero_items = []
    for lam, mu in pairs:
        tilde_a, b, items = collect_items(lam, mu, N)
        if items is None:
            continue
        for label, length, pi, bd in items:
            if length % 2 == 0:
                continue
            w_func = w_label_to_func(label, N)
            w_tilde_a = w_func(tilde_a)
            applicable_simples = []
            for kind, i in [('L', i) for i in range(N - 1)] + [('S', N - 1)]:
                # Check if any mixed move applies for (kind, i): total capacity >= |c|
                if kind == 'L':
                    c = w_tilde_a[i] - w_tilde_a[i + 1]
                else:
                    c = w_tilde_a[N - 1]
                if c == 0:
                    continue
                n_total = abs(c)
                total_cap = 0
                for st in subtypes_for_simple(kind, i, N):
                    donor, _ = subtype_donor_receiver(kind, i, st, c, N)
                    total_cap += pi.get(donor, 0)
                if total_cap >= n_total:
                    applicable_simples.append((kind, i))
            distribution[len(applicable_simples)] += 1
            if len(applicable_simples) == 0:
                zero_items.append((lam, mu, label, length, pi, bd))
    return {'distribution': dict(distribution), 'zero_items': zero_items}


def main(max_lam1_int=4, mode='injection'):
    print("=" * 70)
    print(f"Mode: {mode} (max_lam1_int={max_lam1_int}, i.e., λ_1 ≤ {max_lam1_int}+1/2)")
    print("=" * 70)
    print()

    print("=" * 70)
    print("Step 1: Observational scan (PURE moves) — distribution of #applicable")
    print("=" * 70)
    obs = observational_scan(N, max_lam1_int=max_lam1_int)
    print(f"PURE-move distribution: {obs['distribution']}")
    print(f"# odd items with 0 PURE-applicable moves: {len(obs['zero_move_items'])}")
    print()

    print("=" * 70)
    print("Step 2: Observational scan (MIXED) — applicable simple reflections per odd item")
    print("=" * 70)
    obsm = observational_scan_mixed(N, max_lam1_int=max_lam1_int)
    print(f"MIXED simple-reflection distribution: {obsm['distribution']}")
    print(f"# odd items with 0 MIXED-applicable simple reflections: {len(obsm['zero_items'])}")
    if obsm['zero_items']:
        print("FAIL: still incomplete. Examples:")
        for lam, mu, label, length, pi, bd in obsm['zero_items'][:5]:
            print(f"  λ={lam}, μ={mu}, w={label}, len={length}, π={pi}, bd={bd}")
        return
    print()

    print("=" * 70)
    print("Step 3: Run MIXED priority orders")
    print("=" * 70)
    results = {}
    combos = []
    for simple_pri in ['short_first', 'lex', 'long_first', 'morris']:
        for sub_pri in ['a_first', 'high_first', 'low_first']:
            for descent_only in [False, True]:
                for sp_mode in ['order', 'max_c', 'min_c']:
                    combos.append((simple_pri, sub_pri, descent_only, sp_mode))
    for simple_pri, sub_pri, descent_only, sp_mode in combos:
        tag = f"simple={simple_pri}/sub={sub_pri}/{sp_mode}" + ('/descent' if descent_only else '')
        res = run_mixed_priority(simple_pri, sub_pri, N,
                                 max_lam1_int=max_lam1_int,
                                 descent_only=descent_only,
                                 verbose_first_n=2,
                                 mode=mode,
                                 simple_pri_mode=sp_mode)
        results[tag] = res
        print(f"--- {tag} ---")
        print(f"  pairs={res['n_pairs']}, complete={res['n_complete']}, failed={res['n_failed']}")
        if res['failures']:
            lam, mu, fres = res['failures'][0]
            print(f"  First failure: λ={lam}, μ={mu}")
            if mode == 'injection':
                print(f"    n_odd={fres['n_odd']}, n_matched={fres['n_matched']}, "
                      f"n_unmatched={fres['n_unmatched']}, n_collisions={fres['n_collisions']}")
            if fres['fail_examples']:
                fe = fres['fail_examples'][0]
                print(f"    First fail type={fe.get('type')}")
                if fe.get('type') == 'collision':
                    print(f"      target={fe['target_item']}")
                    for o, m in zip(fe['odd_items'], fe['moves_used']):
                        print(f"      odd item: {o}; move used: {m}")
                elif fe.get('type') == 'unmatched_odd':
                    print(f"      odd: {fe['item']}")
    return results


# ==================== Bipartite injection (oracle / existence test) ====================

def list_all_simple_moves(label, pi, w_tilde_a, N):
    """Return list of (move_info, (new_label, new_pi)) for ALL valid mixed moves over all simple reflections."""
    out = []
    for kind, i in [('L', i) for i in range(N - 1)] + [('S', N - 1)]:
        if kind == 'L':
            c = w_tilde_a[i] - w_tilde_a[i + 1]
        else:
            c = w_tilde_a[N - 1]
        if c == 0:
            continue
        n_total = abs(c)
        # Enumerate ALL valid distributions over all subtypes
        subtypes = subtypes_for_simple(kind, i, N)
        capacities = {}
        for st in subtypes:
            donor, _ = subtype_donor_receiver(kind, i, st, c, N)
            capacities[st] = pi.get(donor, 0)
        # Recursively enumerate distributions
        results = []
        sts = list(subtypes)
        def recurse(idx, remaining, partial):
            if idx == len(sts):
                if remaining == 0:
                    results.append(dict(partial))
                return
            st = sts[idx]
            cap = capacities[st]
            for n in range(min(cap, remaining) + 1):
                if n > 0:
                    partial[st] = n
                recurse(idx + 1, remaining - n, partial)
                if n > 0:
                    del partial[st]
        recurse(0, n_total, {})
        for d in results:
            new_label, new_pi = apply_mixed_move(label, pi, w_tilde_a, kind, i, d, N)
            out.append(((kind, i, d), (new_label, new_pi)))
    return out


def bipartite_injection_exists(lam, mu, N):
    """Test whether a bidegree-preserving injection from odds to evens EXISTS.
    Uses bipartite matching (Hopcroft-Karp).

    Returns True if injection exists, False otherwise.
    """
    tilde_a, b, items = collect_items(lam, mu, N)
    if items is None:
        return None
    # For each odd item, list all even items reachable by ANY single simple reflection move (mixed).
    odd_to_evens = {}  # odd_idx -> set of even_idx
    item_lookup = {(lbl, frozenset(pi.items())): idx for idx, (lbl, lng, pi, bd) in enumerate(items)}
    for idx, (label, length, pi, bd) in enumerate(items):
        if length % 2 != 1:
            continue
        w_func = w_label_to_func(label, N)
        w_tilde_a = w_func(tilde_a)
        moves = list_all_simple_moves(label, pi, w_tilde_a, N)
        evens = set()
        for move_info, (new_label, new_pi) in moves:
            tgt_idx = item_lookup.get((new_label, frozenset(new_pi.items())))
            if tgt_idx is not None and items[tgt_idx][1] % 2 == 0 and items[tgt_idx][3] == bd:
                evens.add(tgt_idx)
        odd_to_evens[idx] = evens

    # Bipartite matching: Hopcroft-Karp simplified (Hungarian or naive aug paths).
    pair_odd = {}  # odd -> even
    pair_even = {}  # even -> odd
    def try_aug(odd, visited):
        for ev in odd_to_evens.get(odd, []):
            if ev in visited:
                continue
            visited.add(ev)
            if ev not in pair_even or try_aug(pair_even[ev], visited):
                pair_odd[odd] = ev
                pair_even[ev] = odd
                return True
        return False
    odds = sorted(odd_to_evens.keys())
    matched = 0
    for o in odds:
        if try_aug(o, set()):
            matched += 1
    return matched == len(odds)


def test_oracle(N, max_lam1_int):
    """Verify ORACLE (bipartite matching) gives an injection for every dominant spin pair."""
    pairs = enumerate_dominant_spin_pairs(max_lam1_int, N)
    n_yes = 0
    n_no = 0
    fails = []
    for lam, mu in pairs:
        ok = bipartite_injection_exists(lam, mu, N)
        if ok is None:
            continue
        if ok:
            n_yes += 1
        else:
            n_no += 1
            fails.append((lam, mu))
    return {'n_yes': n_yes, 'n_no': n_no, 'fails': fails}


if __name__ == "__main__":
    main()
