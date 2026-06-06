"""
Richer Aug~ involution for C_3 = sp(6), with the FULL bidegree-preserving move set.

C_3 = Sp(6) root system:
  simple roots: alpha_0 = e_0 - e_1 (short), alpha_1 = e_1 - e_2 (short), alpha_2 = 2 e_2 (long).
  positive roots:
    SHORT: {e_i - e_j : i<j} u {e_i + e_j : i<j}   -- 6 short
    LONG:  {2 e_i : 0<=i<=2}                       -- 3 long
  rho = (3, 2, 1).
  |W(C_3)| = 48 (signed permutations, same as W(B_3)).

Convention (mirror of B_3):
  ('S', i) for i = 0, ..., N-2  --  short EXCHANGE simple (swaps coords i, i+1).
  ('L', N-1)                    --  long  FLIP     simple (flips last coord).

Subtypes (per simple):
  ('S', i)  alpha_i = e_i - e_{i+1} short:
    Each swap shifts beta by some integer multiple of -alpha_i.
    (LL,):       remove (2 e_i),       add (2 e_{i+1});     2-unit swap.
    (b+, p) p<i: remove (e_p + e_i),    add (e_p + e_{i+1}); 1-unit.
    (b-, p) p<i: remove (e_p - e_{i+1}),add (e_p - e_i);     1-unit.
    (c+, q) q>i+1: remove (e_i + e_q),  add (e_{i+1} + e_q); 1-unit.
    (c-, q) q>i+1: remove (e_i - e_q),  add (e_{i+1} - e_q); 1-unit.
    (Sign reverses when c_i < 0.)
  ('L', N-1)  alpha_{N-1} = 2 e_{N-1} long:
    (S, p) p<N-1: remove (e_p + e_{N-1}), add (e_p - e_{N-1}); 1-unit (shift -alpha_{N-1} = -2 e_{N-1}).
    (Sign reverses when c_{N-1} < 0.)

The c-value:
  ('S', i): c = (wa)[i] - (wa)[i+1]              = <wa, alpha_i^v>   (alpha_i short, alpha_i^v = alpha_i).
  ('L', N-1): c = (wa)[N-1]                       = <wa, alpha_{N-1}^v> (alpha_{N-1} long, alpha_{N-1}^v = e_{N-1}).

A distribution is {subtype: count_of_swaps_of_this_subtype}.
Constraint: sum(count * units(subtype)) = |c|, with count <= pi[donor].
"""

from fractions import Fraction
from collections import defaultdict
from itertools import permutations, product


N = 3


# ==================== C_n root setup ====================

def positive_roots_Cn(N):
    """List of (root_tuple, 'L'/'S') for C_n positive roots."""
    roots = []
    # Short: e_i - e_j, i < j
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N; v[i] = 1; v[j] = -1
            roots.append((tuple(v), 'S'))
    # Short: e_i + e_j, i < j
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N; v[i] = 1; v[j] = 1
            roots.append((tuple(v), 'S'))
    # Long: 2 e_i
    for i in range(N):
        v = [0] * N; v[i] = 2
        roots.append((tuple(v), 'L'))
    return roots


def positive_roots_Cn_ordered(N):
    base = positive_roots_Cn(N)
    def keyfn(item):
        r, kind = item
        for k in range(N):
            if r[k] != 0:
                return (k, r)
        return (N, r)
    return sorted(base, key=keyfn)


def long_2e(N, i):
    """2 e_i."""
    v = [0] * N; v[i] = 2
    return tuple(v)


def short_minus(N, i, j):
    """e_i - e_j; expect i < j for positive."""
    v = [0] * N; v[i] = 1; v[j] = -1
    return tuple(v)


def short_plus(N, i, j):
    """e_i + e_j; positive for any i != j."""
    v = [0] * N; v[i] = 1; v[j] = 1
    return tuple(v)


# ==================== Weyl group W(C_n) = signed permutations ====================

def weyl_Cn(N):
    pos_roots = [r for r, _ in positive_roots_Cn(N)]
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


def s_exch_w(label, i, N):
    """Apply simple exchange reflection s_{alpha_i} (alpha_i = e_i - e_{i+1}) on the LEFT."""
    perm, signs = label
    new_perm = list(perm)
    new_perm[i], new_perm[i + 1] = perm[i + 1], perm[i]
    new_signs = list(signs)
    new_signs[i], new_signs[i + 1] = signs[i + 1], signs[i]
    return (tuple(new_perm), tuple(new_signs))


def s_flip_w(label, N):
    """Apply simple flip reflection s_{alpha_{N-1}} (alpha_{N-1} = 2 e_{N-1}) on the LEFT."""
    perm, signs = label
    new_signs = list(signs)
    new_signs[N - 1] = -signs[N - 1]
    return (perm, tuple(new_signs))


def length_of_label(label, N, pos_roots=None):
    if pos_roots is None:
        pos_roots = [r for r, _ in positive_roots_Cn(N)]
    pos_set = set(pos_roots)
    w = w_label_to_func(label, N)
    return sum(1 for r in pos_roots if w(r) not in pos_set)


# ==================== Kostant partitions ====================

def all_kostant_partitions(beta, N, pos_roots_ordered=None):
    """Enumerate all decompositions of beta as non-negative integer sums of C_n positive roots."""
    if pos_roots_ordered is None:
        pos_roots_ordered = positive_roots_Cn_ordered(N)
    target = tuple(int(x) for x in beta)
    out = []

    leading_coords = []
    leading_vals = []
    for r, _ in pos_roots_ordered:
        for k in range(N):
            if r[k] != 0:
                leading_coords.append(k)
                leading_vals.append(r[k])
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
        lv = leading_vals[idx]
        rem_lc = remaining[lc]
        if rem_lc < 0:
            return
        # how many copies of root: each adds lv to coord lc, plus changes to other coords
        max_n = rem_lc // lv  # we cannot exceed rem_lc/lv
        for n in range(max_n + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(N))
            new_partial = dict(partial)
            if n > 0:
                new_partial[root] = n
            recurse(idx + 1, new_rem, new_partial)

    recurse(0, target, {})
    return out


def bidegree_of_partition(pi, N):
    """Compute (long_count, short_count) for a Kostant partition pi."""
    pos_roots = positive_roots_Cn(N)
    long_set = set(r for r, k in pos_roots if k == 'L')
    short_set = set(r for r, k in pos_roots if k == 'S')
    long_cnt = sum(mult for root, mult in pi.items() if root in long_set)
    short_cnt = sum(mult for root, mult in pi.items() if root in short_set)
    return (long_cnt, short_cnt)


# ==================== Move subtype structure (C_n) ====================

def subtypes_for_simple(kind, i, N):
    """List subtypes for the simple reflection (kind, i) in C_n."""
    if kind == 'S':  # short exchange simple alpha_i = e_i - e_{i+1}
        out = [('LL',)]
        for p in range(i):
            out.append(('b+', p))
            out.append(('b-', p))
        for q in range(i + 2, N):
            out.append(('c+', q))
            out.append(('c-', q))
        return out
    elif kind == 'L':  # long flip simple alpha_{N-1} = 2 e_{N-1}
        return [('S', p) for p in range(N - 1)]
    else:
        raise ValueError(f"Unknown kind {kind}")


def subtype_units_per_swap(kind, i, subtype, N):
    """How many alpha_i units does ONE swap of this subtype contribute? 1 or 2."""
    if kind == 'S':
        if subtype[0] == 'LL':
            return 2
        else:
            return 1
    elif kind == 'L':
        return 1
    else:
        raise ValueError


def subtype_donor_receiver(kind, i, subtype, c, N):
    """Return (donor, receiver) roots for ONE swap of this subtype, given the sign of c."""
    if kind == 'S':
        tag = subtype[0]
        if tag == 'LL':
            if c > 0:
                return long_2e(N, i), long_2e(N, i + 1)
            else:
                return long_2e(N, i + 1), long_2e(N, i)
        elif tag == 'b+':
            p = subtype[1]
            if c > 0:
                return short_plus(N, p, i), short_plus(N, p, i + 1)
            else:
                return short_plus(N, p, i + 1), short_plus(N, p, i)
        elif tag == 'b-':
            p = subtype[1]
            if c > 0:
                return short_minus(N, p, i + 1), short_minus(N, p, i)
            else:
                return short_minus(N, p, i), short_minus(N, p, i + 1)
        elif tag == 'c+':
            q = subtype[1]
            if c > 0:
                return short_plus(N, i, q), short_plus(N, i + 1, q)
            else:
                return short_plus(N, i + 1, q), short_plus(N, i, q)
        elif tag == 'c-':
            q = subtype[1]
            if c > 0:
                return short_minus(N, i, q), short_minus(N, i + 1, q)
            else:
                return short_minus(N, i + 1, q), short_minus(N, i, q)
        else:
            raise ValueError(f"Bad subtype tag {tag} for S")
    elif kind == 'L':  # flip
        tag = subtype[0]
        assert tag == 'S'
        p = subtype[1]
        if c > 0:
            return short_plus(N, p, N - 1), short_minus(N, p, N - 1)
        else:
            return short_minus(N, p, N - 1), short_plus(N, p, N - 1)
    else:
        raise ValueError


def get_c_value(label, w_tilde_a, kind, i, N):
    if kind == 'S':
        return w_tilde_a[i] - w_tilde_a[i + 1]
    elif kind == 'L':
        return w_tilde_a[N - 1]
    else:
        raise ValueError


def apply_distribution(label, pi, w_tilde_a, kind, i, distribution, N):
    """Apply a distribution = {subtype: count_of_swaps_of_this_subtype}. Returns (new_label, new_pi)."""
    c = get_c_value(label, w_tilde_a, kind, i, N)
    new_pi = dict(pi)
    for st, n in distribution.items():
        donor, recv = subtype_donor_receiver(kind, i, st, c, N)
        new_pi[donor] = new_pi.get(donor, 0) - n
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[recv] = new_pi.get(recv, 0) + n
    if kind == 'S':
        new_label = s_exch_w(label, i, N)
    else:
        new_label = s_flip_w(label, N)
    return (new_label, new_pi)


def list_all_simple_moves(label, pi, w_tilde_a, N, allow_opposite=True):
    """All valid Aug~ moves: for each simple reflection (kind, i), enumerate all
    multisets of orbit swaps that net-shift beta by -c*alpha_i, respecting pi-donor
    capacities.  If allow_opposite=True, swaps within one s_i may go in BOTH directions
    (forward/backward), giving cancellations.  This is needed for type C_n to realize
    the BGG-Verma differential at fixed bidegree because of mixed-unit subtypes
    (LL=2-unit + b/c=1-unit within one s_i).

    Distribution data type: dict {(subtype, sign): count}, where sign is '+' or '-'.
      '-' direction (forward when c>0): donor = subtype_donor_receiver(kind, i, st, +1, N)[0]
      '+' direction (forward when c<0): donor = subtype_donor_receiver(kind, i, st, -1, N)[0]
    Net shift in alpha_i units:
      sum_st units(st) * (count(st, '+') - count(st, '-')) = -c.

    For backward-compat: simple PURE distributions are also reported as {subtype: count}
    (single-direction, single-subtype).
    """
    out = []
    simples = [('S', j) for j in range(N - 1)] + [('L', N - 1)]
    for kind, i in simples:
        c = get_c_value(label, w_tilde_a, kind, i, N)
        if c == 0:
            continue
        subtypes = subtypes_for_simple(kind, i, N)
        # For each subtype, get '-' donor (with c=+1) and '+' donor (with c=-1).
        donor_minus = {}
        donor_plus = {}
        for st in subtypes:
            donor_minus[st], _ = subtype_donor_receiver(kind, i, st, +1, N)
            donor_plus[st], _ = subtype_donor_receiver(kind, i, st, -1, N)
        capacities_minus = {st: pi.get(donor_minus[st], 0) for st in subtypes}
        capacities_plus = {st: pi.get(donor_plus[st], 0) for st in subtypes}
        units_of = {st: subtype_units_per_swap(kind, i, st, N) for st in subtypes}

        # Enumerate (k_minus_st, k_plus_st) for each subtype, with k_minus_st-k_plus_st
        # weighted by units(st) summing to c.
        if allow_opposite:
            # Per subtype st, pick one of:
            #   (A) k_minus = 0, k_plus = 0   (don't use st)
            #   (B) k_minus = n (n in 1..cap_minus[st]), k_plus = 0   (-direction)
            #   (C) k_minus = 0, k_plus = n (n in 1..cap_plus[st])    (+direction)
            # Constraint: sum_st (k_minus - k_plus) * units(st) = c.
            results = []
            sts = list(subtypes)
            n_sts = len(sts)

            def recurse_dir(idx, remaining, partial):
                if idx == n_sts:
                    if remaining == 0:
                        results.append(dict(partial))
                    return
                st = sts[idx]
                u = units_of[st]
                cap_m = capacities_minus[st]
                cap_p = capacities_plus[st]
                # Option (A): skip
                recurse_dir(idx + 1, remaining, partial)
                # Option (B): k_minus = n, contributes +n*u to "remaining" reduction.
                for n in range(1, cap_m + 1):
                    partial[(st, '-')] = n
                    recurse_dir(idx + 1, remaining - n * u, partial)
                    del partial[(st, '-')]
                # Option (C): k_plus = n, contributes -n*u.
                for n in range(1, cap_p + 1):
                    partial[(st, '+')] = n
                    recurse_dir(idx + 1, remaining + n * u, partial)
                    del partial[(st, '+')]

            recurse_dir(0, c, {})

            for d in results:
                new_pi = dict(pi)
                for (st, sg), n in d.items():
                    if sg == '-':
                        donor = donor_minus[st]
                        receiver = subtype_donor_receiver(kind, i, st, +1, N)[1]
                    else:
                        donor = donor_plus[st]
                        receiver = subtype_donor_receiver(kind, i, st, -1, N)[1]
                    new_pi[donor] = new_pi.get(donor, 0) - n
                    if new_pi[donor] == 0:
                        del new_pi[donor]
                    new_pi[receiver] = new_pi.get(receiver, 0) + n
                if kind == 'S':
                    new_label = s_exch_w(label, i, N)
                else:
                    new_label = s_flip_w(label, N)
                out.append(((kind, i, d), (new_label, new_pi)))
        else:
            # Old behavior: single-direction, multiple subtypes possible.
            n_units = abs(c)
            capacities = {}
            for st in subtypes:
                donor, _ = subtype_donor_receiver(kind, i, st, c, N)
                capacities[st] = pi.get(donor, 0)
            results = []
            sts = list(subtypes)

            def recurse(idx, remaining_units, partial):
                if idx == len(sts):
                    if remaining_units == 0:
                        results.append(dict(partial))
                    return
                st = sts[idx]
                cap = capacities[st]
                u = units_of[st]
                max_n = min(cap, remaining_units // u)
                for n in range(max_n + 1):
                    if n > 0:
                        partial[st] = n
                    recurse(idx + 1, remaining_units - n * u, partial)
                    if n > 0:
                        del partial[st]

            recurse(0, n_units, {})
            for d in results:
                new_label, new_pi = apply_distribution(label, pi, w_tilde_a, kind, i, d, N)
                out.append(((kind, i, d), (new_label, new_pi)))
    return out


# ==================== Basis enumeration ====================

def collect_items(lam, mu, N):
    """Return (tilde_a, b, items=[(label, length, pi, bidegree), ...]) for (lam, mu).
    Uses rho_C = (N, N-1, ..., 1).

    Supports integer or spin (half-integer) lam, mu.  tilde_a and b are stored as
    tuples of Fraction; beta_w = w(tilde_a) - b is checked to be integer (and is then
    converted to int tuple before passing to all_kostant_partitions).
    """
    rho = tuple(Fraction(N - i) for i in range(N))
    tilde_a = tuple(Fraction(lam[i]) + rho[i] for i in range(N))
    b = tuple(Fraction(mu[i]) + rho[i] for i in range(N))
    # tilde_a, b must have the same fractional part (else beta is not integer).
    if not all((tilde_a[i] - b[i]).denominator == 1 for i in range(N)):
        return None, None, None
    weyl = weyl_Cn(N)
    pos_roots_ord = positive_roots_Cn_ordered(N)
    items = []
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w_frac = tuple(wa[i] - b[i] for i in range(N))
        if not all(x.denominator == 1 for x in beta_w_frac):
            continue
        beta_w = tuple(int(x) for x in beta_w_frac)
        if beta_w[0] < 0:
            continue
        if sum(beta_w) % 2 != 0:
            continue
        if sum(beta_w) < 0:
            continue
        pis = all_kostant_partitions(beta_w, N, pos_roots_ord)
        for pi in pis:
            bd = bidegree_of_partition(pi, N)
            items.append((label, length, pi, bd))
    return tilde_a, b, items


# ==================== Dominant pair enumeration ====================

def enumerate_dominant_spin_pairs(max_lam1_int, N):
    """Dominant spin pairs (lambda, mu) with lambda_1 <= max_lam1_int + 1/2."""
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


def enumerate_dominant_integer_pairs(max_lam1, N):
    """Dominant integer pairs (lambda, mu) with lambda_1 <= max_lam1, lambda_3 >= 0."""
    pairs = []
    if N == 3:
        for l1 in range(max_lam1 + 1):
            for l2 in range(l1 + 1):
                for l3 in range(l2 + 1):
                    lam = (Fraction(l1), Fraction(l2), Fraction(l3))
                    for m1 in range(l1 + 1):
                        for m2 in range(m1 + 1):
                            for m3 in range(m2 + 1):
                                mu = (Fraction(m1), Fraction(m2), Fraction(m3))
                                pairs.append((lam, mu))
    return pairs


# ==================== Bipartite injection (oracle) ====================

def bipartite_injection_exists(lam, mu, N):
    """Test whether a bidegree-preserving injection from odds to evens EXISTS."""
    tilde_a, b, items = collect_items(lam, mu, N)
    if items is None:
        return None
    odd_to_evens = {}
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

    pair_odd = {}
    pair_even = {}
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


def test_oracle_spin(N, max_lam1_int):
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
    # Smoke tests.
    print("=" * 60)
    print("C_3 root system sanity")
    print("=" * 60)
    pr = positive_roots_Cn(3)
    print(f"# positive roots: {len(pr)} (expect 9)")
    short = [r for r, k in pr if k == 'S']
    long_ = [r for r, k in pr if k == 'L']
    print(f"  short: {len(short)} (expect 6)")
    print(f"  long:  {len(long_)} (expect 3)")
    for r, k in pr:
        print(f"  {r}  {k}")
    print()
    weyl = weyl_Cn(3)
    print(f"# Weyl elements: {len(weyl)} (expect 48)")
    print()
    # Length distribution
    from collections import Counter
    length_distrib = Counter(lng for _, lng, _ in weyl)
    print(f"Length distribution: {sorted(length_distrib.items())}")
    print()
    # Kostant partitions of a simple element
    pp = all_kostant_partitions((2, 0, 0), 3)
    print(f"Kostant partitions of (2,0,0) (= 2 e_0): {len(pp)} (expect 2: as 2*(e_0-e_1) + 2*(e_1-e_2)+...?? Actually = 2*(2 e_0)/something. Let me check.)")
    for p in pp:
        print(f"  {p}")
