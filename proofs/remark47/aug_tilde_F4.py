"""
Aug~ involution for F_4, the rank-4 doubly-laced exceptional root system.

F_4 facts:
  Rank 4, |W(F_4)| = 1152. 24 positive roots (12 long + 12 short).

Simple roots (0-indexed, Bourbaki-style):
  alpha_0 = e_1 - e_2  (long)         coord (0, 1, -1, 0)
  alpha_1 = e_2 - e_3  (long)         coord (0, 0, 1, -1)
  alpha_2 = e_3        (short)        coord (0, 0, 0, 1)
  alpha_3 = (1/2)(e_0 - e_1 - e_2 - e_3) (short)   coord (1/2, -1/2, -1/2, -1/2)

Long root squared length = 2; short root squared length = 1.
  alpha_i^v  =  alpha_i              if alpha_i long  (|alpha_i|^2 = 2)
  alpha_i^v  =  2 alpha_i            if alpha_i short (|alpha_i|^2 = 1)

Positive roots:
  LONG (12): { e_i +/- e_j : 0 <= i < j <= 3 }
  SHORT (12):
    e_i for i in {0, 1, 2, 3}                     (4 roots)
    (1/2)(e_0 +/- e_1 +/- e_2 +/- e_3)            (8 roots, e_0 sign always +)

rho_F4 = (11/2, 5/2, 3/2, 1/2).

Bigrading: (long-count, short-count) of a Kostant partition.

Aug~ move structure:
  For each simple reflection s_i and (w, pi) with c_i = <w*tilde_a, alpha_i^v> != 0,
  the move accumulates a multiset of s_i-orbit swaps within positive roots.
  Each orbit O on positive roots is one of:
    - a 1-point orbit (the root is fixed by s_i)
    - a 2-point orbit {r, s_i(r)} with pairing.
  For r in a 2-point orbit, the swap r <-> s_i(r) shifts beta by -<r, alpha_i^v> * alpha_i.
  Units per swap = |<r, alpha_i^v>| in {1, 2} (doubly-laced).

  Distribution: {(orbit_tag, direction sign): count} with sum of units (signed) = c_i.

We use a uniform orbit-based representation rather than B/C-style hand-rolled tags.
"""

from fractions import Fraction
from collections import defaultdict, Counter
from itertools import product


# ==================== Root system data ====================

def F4_positive_roots():
    """Return list of (root_tuple_of_Fraction, 'L'/'S')."""
    F = Fraction
    out = []
    # LONG: e_i +/- e_j, 0 <= i < j <= 3
    for i in range(4):
        for j in range(i + 1, 4):
            v = [F(0)] * 4
            v[i] = F(1); v[j] = F(-1)
            out.append((tuple(v), 'L'))
            v = [F(0)] * 4
            v[i] = F(1); v[j] = F(1)
            out.append((tuple(v), 'L'))
    # SHORT: e_i
    for i in range(4):
        v = [F(0)] * 4
        v[i] = F(1)
        out.append((tuple(v), 'S'))
    # SHORT: (1/2)(e_0 +/- e_1 +/- e_2 +/- e_3), with e_0 coeff = +1/2
    half = F(1, 2)
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            for s3 in [1, -1]:
                v = (half, half * s1, half * s2, half * s3)
                out.append((v, 'S'))
    return out


def F4_simple_roots():
    F = Fraction
    half = F(1, 2)
    return [
        ((F(0), F(1), F(-1), F(0)), 'L'),   # alpha_0 = e_1 - e_2
        ((F(0), F(0), F(1), F(-1)), 'L'),   # alpha_1 = e_2 - e_3
        ((F(0), F(0), F(0), F(1)),  'S'),   # alpha_2 = e_3
        ((half, -half, -half, -half), 'S'), # alpha_3 = (1/2)(e_0 - e_1 - e_2 - e_3)
    ]


def root_inner(u, v):
    """Standard inner product."""
    return sum(u[k] * v[k] for k in range(4))


def root_coroot(alpha, kind):
    """Compute alpha^v for the standard normalization.
    Long: |alpha|^2 = 2, so alpha^v = alpha.
    Short: |alpha|^2 = 1, so alpha^v = 2 * alpha.
    """
    if kind == 'L':
        return alpha
    else:
        return tuple(2 * x for x in alpha)


def reflect(v, alpha, alpha_v):
    """s_alpha(v) = v - <v, alpha^v> * alpha."""
    c = root_inner(v, alpha_v)
    return tuple(v[k] - c * alpha[k] for k in range(4))


# ==================== Build Weyl group W(F_4) by BFS ====================

def build_weyl_F4():
    """Return list of (label_str_id, length, w_matrix_action_tuple, w_perm_on_roots).

    Each Weyl element w is represented by its action on each of the 4 simple-root-positions
    (we just store the integer permutation it induces on positive roots, plus its image
    of each of the 4 e_i vectors as a 4-tuple of Fractions).

    To keep things hashable, we store w as a tuple of (image of e_0, image of e_1, image of e_2,
    image of e_3) -- each image is a 4-tuple of Fractions.
    """
    simples = F4_simple_roots()
    pos_roots = F4_positive_roots()
    pos_set = set(r for r, _ in pos_roots)

    F = Fraction
    e_basis = [tuple(F(1 if j == i else 0) for j in range(4)) for i in range(4)]

    # identity
    id_label = tuple(e_basis)
    seen = {id_label: 0}
    layer = [id_label]
    out = [id_label]
    length = 0
    while layer:
        new_layer = []
        for w in layer:
            # Apply each simple reflection on the LEFT: result is s_alpha * w.
            # Action on a vector v: w(v) is computed; left-multiplying by s_alpha just
            # means apply s_alpha to w's image.
            # But w represented as tuple of (w(e_0), w(e_1), w(e_2), w(e_3)).
            # New w' s.t. w'(e_i) = s_alpha(w(e_i)).
            for alpha, kind in simples:
                alpha_v = root_coroot(alpha, kind)
                new_w = tuple(reflect(w[i], alpha, alpha_v) for i in range(4))
                if new_w not in seen:
                    seen[new_w] = length + 1
                    new_layer.append(new_w)
                    out.append(new_w)
        length += 1
        layer = new_layer

    return out, seen


def apply_w(w, v):
    """Apply Weyl element w (stored as tuple of (w(e_0), w(e_1), w(e_2), w(e_3))) to vector v.
    w(v) = sum_i v[i] * w(e_i).
    """
    return tuple(sum(v[i] * w[i][k] for i in range(4)) for k in range(4))


def left_mult_simple(w, simple_idx, simples=None):
    """Compute s_{alpha_{simple_idx}} * w (left multiplication).

    Action: (s_alpha * w)(v) = s_alpha(w(v)).
    Represented: new_w[i] = s_alpha(w[i]).
    """
    if simples is None:
        simples = F4_simple_roots()
    alpha, kind = simples[simple_idx]
    alpha_v = root_coroot(alpha, kind)
    return tuple(reflect(w[i], alpha, alpha_v) for i in range(4))


# ==================== Kostant partitions ====================

# F_4 positive roots have coords in {0, +-1/2, +-1}. To enumerate Kostant partitions
# we need to handle half-integer coords. We multiply by 2 to convert to integer
# coordinates internally.

def F4_pos_roots_doubled():
    """Return list of (doubled root tuple of ints, 'L'/'S'). Each coord is doubled."""
    out = []
    for r, k in F4_positive_roots():
        rd = tuple(int(2 * x) for x in r)
        out.append((rd, k))
    return out


def pos_roots_ordered_doubled():
    """Sort doubled positive roots by leading nonzero coord (for backtracking)."""
    base = F4_pos_roots_doubled()
    def keyfn(item):
        r, kind = item
        for k in range(4):
            if r[k] != 0:
                return (k, kind == 'L', r)  # group by leading coord; L vs S secondary
        return (4, 0, r)
    return sorted(base, key=keyfn)


def all_kostant_partitions_F4(beta):
    """Enumerate decompositions of beta (a 4-tuple of Fractions or ints) as
    non-negative integer sums of F_4 positive roots.

    beta is expected to have coordinates in (1/2)Z. We work in doubled coords (multiply by 2).
    """
    pos_ord = pos_roots_ordered_doubled()
    # Double beta:
    beta_d = tuple(int(2 * Fraction(x)) for x in beta)

    out = []

    def recurse(idx, remaining, partial):
        if idx == len(pos_ord):
            if all(r == 0 for r in remaining):
                out.append(dict(partial))
            return
        root, kind = pos_ord[idx]
        # Try 0, 1, 2, ... copies of root.
        # Find max n by remaining coords.
        max_n = None
        for k in range(4):
            if root[k] > 0:
                cap = remaining[k] // root[k] if remaining[k] >= 0 else -1
                if cap < 0:
                    return  # can't reach 0 in this coord
                if max_n is None or cap < max_n:
                    max_n = cap
            elif root[k] < 0:
                # remaining[k] - n*root[k] = remaining[k] + n*|root[k]| -- always increases
                # but we need final to be 0; that constrains via other roots.
                pass
        if max_n is None:
            max_n = 0  # root is zero vector? shouldn't happen
        # Prune: if remaining has negative coord that we can't pull back, skip.
        # (We can be more aggressive but this is OK.)
        for n in range(max_n + 1):
            new_rem = tuple(remaining[k] - n * root[k] for k in range(4))
            # Early skip if any coord that no future root touches positively is nonzero.
            new_partial = dict(partial)
            if n > 0:
                # Store undoubled root for downstream pi processing
                root_undoubled = tuple(Fraction(x, 2) for x in root)
                new_partial[root_undoubled] = n
            recurse(idx + 1, new_rem, new_partial)

    recurse(0, beta_d, {})
    return out


# ==================== Bidegree ====================

def bidegree_of_partition(pi):
    """(long_count, short_count) for a Kostant partition pi."""
    long_set = set(r for r, k in F4_positive_roots() if k == 'L')
    # We compare pi-keys against this set; they are tuples of Fractions.
    long_cnt = 0
    short_cnt = 0
    for root, mult in pi.items():
        if root in long_set:
            long_cnt += mult
        else:
            short_cnt += mult
    return (long_cnt, short_cnt)


# Cache long_set globally
_LONG_SET = set(r for r, k in F4_positive_roots() if k == 'L')
_POS_SET = set(r for r, _ in F4_positive_roots())


def bidegree_of_partition_fast(pi):
    long_cnt = 0
    short_cnt = 0
    for root, mult in pi.items():
        if root in _LONG_SET:
            long_cnt += mult
        else:
            short_cnt += mult
    return (long_cnt, short_cnt)


# ==================== Simple reflection orbits on positive roots ====================

def compute_orbit_data():
    """For each simple reflection s_i (i = 0..3), compute its orbit decomposition on
    positive roots.

    Returns: dict simple_idx -> list of orbit entries.
    Each orbit entry: dict {
        'roots': tuple of root tuples in the orbit (size 1 or 2),
        'units': units per swap (|<r, alpha_i^v>|),
        'tag': a canonical orbit tag (string or tuple, unique among orbits for this s_i).
    }
    Note: the orbit containing alpha_i itself (which gets mapped to -alpha_i, OUT of
    positive roots) is treated as a 1-point orbit and NOT usable for swap moves;
    we exclude it.
    """
    simples = F4_simple_roots()
    pos_roots = [r for r, _ in F4_positive_roots()]
    pos_set = _POS_SET

    out = {}
    for si, (alpha, kind) in enumerate(simples):
        alpha_v = root_coroot(alpha, kind)
        # Build orbit pairs
        orbits = []
        seen = set()
        for r in pos_roots:
            if r in seen:
                continue
            sr = reflect(r, alpha, alpha_v)
            c = root_inner(r, alpha_v)
            if sr == r:
                # 1-pt orbit, fixed
                orbits.append({'roots': (r,), 'units': 0, 'tag': ('fix', r)})
                seen.add(r)
            elif sr not in pos_set:
                # r gets sent out of positive roots; r must be alpha_i itself
                # (only the simple root itself flips to negative under s_i in any
                # crystallographic root system).
                orbits.append({'roots': (r,), 'units': 0, 'tag': ('flip', r)})
                seen.add(r)
            else:
                # 2-pt orbit
                # canonical ordering: put root with c>0 first (then r is donor when c>0)
                if c > 0:
                    pair = (r, sr)
                else:
                    pair = (sr, r)
                units = abs(int(c))
                orbits.append({
                    'roots': pair,
                    'units': units,
                    'tag': ('swap', pair),
                })
                seen.add(r)
                seen.add(sr)
        # Filter to only the swap orbits (the ones we use)
        swap_orbits = [o for o in orbits if o['tag'][0] == 'swap']
        out[si] = swap_orbits
    return out


# ==================== c-value at simple reflection ====================

def get_c_value(w_tilde_a, simple_idx, simples=None):
    """Compute c_i = <w * tilde_a, alpha_i^v>."""
    if simples is None:
        simples = F4_simple_roots()
    alpha, kind = simples[simple_idx]
    alpha_v = root_coroot(alpha, kind)
    c = root_inner(w_tilde_a, alpha_v)
    # Integer check
    return c


# ==================== Move enumeration ====================

def list_all_simple_moves(w, pi, w_tilde_a, orbit_data, simples=None):
    """Enumerate all valid Aug~ moves from (w, pi).

    For each simple_idx i in {0, 1, 2, 3}:
      c = <w*tilde_a, alpha_i^v>. If c == 0, skip.
      For each swap orbit O = (r1, r2) with units u, we can pick:
        - k_minus copies of forward swap (r1 -> r2) shifting beta by -u*alpha_i
        - k_plus copies of backward swap (r2 -> r1) shifting beta by +u*alpha_i
        with k_minus + k_plus <= 1 in canonical orbit-uses (NO: actually two directions
        cannot both happen for the same orbit, since they cancel; we allow one or the
        other).
      Constraint: sum_O u_O * (k_minus(O) - k_plus(O)) = c.
      Capacities: k_minus(O) <= pi[donor when c>0], k_plus(O) <= pi[donor when c<0].

    Returns list of ((simple_idx, distribution), (new_w, new_pi)) tuples.
    Distribution dict: {(orbit_tag, sign): count} with sign in {'+', '-'}.
    """
    if simples is None:
        simples = F4_simple_roots()
    out = []
    for si in range(len(simples)):
        c = get_c_value(w_tilde_a, si, simples)
        if c == 0:
            continue
        # c must be an integer (in our integer-lift setup); convert
        if isinstance(c, Fraction):
            if c.denominator != 1:
                continue  # this should not happen if tilde_a is chosen so c is integer
            c = int(c)
        orbits = orbit_data[si]
        # For each orbit, (donor_minus, recv_minus) = direction shifting beta by -u*alpha (forward)
        # We canonicalize so that orbit['roots'] = (r1, r2) with c(r1) > 0, so:
        #   forward swap '-' (when c > 0): donor = r1, receiver = r2  (this REDUCES c by u, shifts beta by -u*alpha)
        #   backward swap '+': donor = r2, receiver = r1               (this INCREASES c by u, shifts beta by +u*alpha)
        # Net constraint: sum_O u_O * (k_minus(O) - k_plus(O)) = c
        n_orbits = len(orbits)

        # Per orbit, three options: skip, use '-' with count n, use '+' with count n.
        results = []

        def recurse(idx, remaining, partial):
            if idx == n_orbits:
                if remaining == 0:
                    results.append(dict(partial))
                return
            orb = orbits[idx]
            r1, r2 = orb['roots']
            u = orb['units']
            cap_minus = pi.get(r1, 0)
            cap_plus = pi.get(r2, 0)
            tag = orb['tag']
            # Option A: skip
            recurse(idx + 1, remaining, partial)
            # Option B: '-' direction, n in 1..cap_minus
            for n in range(1, cap_minus + 1):
                partial[(tag, '-')] = n
                recurse(idx + 1, remaining - n * u, partial)
                del partial[(tag, '-')]
            # Option C: '+' direction, n in 1..cap_plus
            for n in range(1, cap_plus + 1):
                partial[(tag, '+')] = n
                recurse(idx + 1, remaining + n * u, partial)
                del partial[(tag, '+')]

        recurse(0, c, {})

        new_w = left_mult_simple(w, si, simples)
        for d in results:
            new_pi = dict(pi)
            for (tag, sign), n in d.items():
                # tag is ('swap', (r1, r2))
                _, pair = tag
                r1, r2 = pair
                if sign == '-':
                    donor, receiver = r1, r2
                else:
                    donor, receiver = r2, r1
                new_pi[donor] = new_pi.get(donor, 0) - n
                if new_pi[donor] == 0:
                    del new_pi[donor]
                new_pi[receiver] = new_pi.get(receiver, 0) + n
            out.append(((si, d), (new_w, new_pi)))
    return out


def list_pure_moves(w, pi, w_tilde_a, orbit_data, simples=None):
    """Pure moves: single orbit, single direction."""
    if simples is None:
        simples = F4_simple_roots()
    out = []
    for si in range(len(simples)):
        c = get_c_value(w_tilde_a, si, simples)
        if c == 0:
            continue
        if isinstance(c, Fraction):
            if c.denominator != 1:
                continue
            c = int(c)
        orbits = orbit_data[si]
        sign = '-' if c > 0 else '+'
        new_w = left_mult_simple(w, si, simples)
        for orb in orbits:
            r1, r2 = orb['roots']
            u = orb['units']
            n_units = abs(c)
            if n_units % u != 0:
                continue
            n_swaps = n_units // u
            if c > 0:
                donor, receiver = r1, r2
            else:
                donor, receiver = r2, r1
            if pi.get(donor, 0) < n_swaps:
                continue
            new_pi = dict(pi)
            new_pi[donor] = new_pi.get(donor, 0) - n_swaps
            if new_pi[donor] == 0:
                del new_pi[donor]
            new_pi[receiver] = new_pi.get(receiver, 0) + n_swaps
            dist = {(orb['tag'], sign): n_swaps}
            out.append(((si, dist), (new_w, new_pi)))
    return out


# ==================== Basis assembly ====================

def collect_items(lam, mu, weyl=None, orbit_data=None):
    """Return (tilde_a, b, items=[(label_w, length, pi, bidegree), ...]) for (lam, mu).
    rho_F4 = (11/2, 5/2, 3/2, 1/2).
    lam and mu are 4-tuples of Fractions (or convertible).
    """
    F = Fraction
    rho = (F(11, 2), F(5, 2), F(3, 2), F(1, 2))
    tilde_a = tuple(F(lam[i]) + rho[i] for i in range(4))
    b = tuple(F(mu[i]) + rho[i] for i in range(4))
    if weyl is None:
        weyl, seen = build_weyl_F4()
    items = []
    for w in weyl:
        wa = apply_w(w, tilde_a)
        beta_w = tuple(wa[k] - b[k] for k in range(4))
        # beta_w must be a sum of positive roots
        # All positive roots have all coords in (1/2)Z; that's automatic.
        # Skip if any obviously impossible? we just enumerate.
        # Length
        length = sum(1 for r in [rt for rt, _ in F4_positive_roots()]
                     if apply_w(w, r) not in _POS_SET)
        # Enumerate Kostant partitions
        pis = all_kostant_partitions_F4(beta_w)
        for pi in pis:
            bd = bidegree_of_partition_fast(pi)
            items.append((w, length, pi, bd))
    return tilde_a, b, items


def length_of_w(w):
    """Number of positive roots r such that w(r) is negative."""
    return sum(1 for r in [rt for rt, _ in F4_positive_roots()]
               if apply_w(w, r) not in _POS_SET)


# ==================== Smoke tests ====================

if __name__ == "__main__":
    print("=" * 60)
    print("F_4 root system sanity")
    print("=" * 60)
    pr = F4_positive_roots()
    print(f"# positive roots: {len(pr)} (expect 24)")
    nL = sum(1 for _, k in pr if k == 'L')
    nS = sum(1 for _, k in pr if k == 'S')
    print(f"  long: {nL} (expect 12); short: {nS} (expect 12)")
    print()
    print("Building W(F_4) by BFS...")
    weyl, seen = build_weyl_F4()
    print(f"|W(F_4)| = {len(weyl)} (expect 1152)")
    print()
    print("Length distribution:")
    Lens = Counter(seen.values())
    print(f"  {sorted(Lens.items())}")
    print(f"  max length = {max(Lens)}")
    print()
    print("Computing orbit data...")
    od = compute_orbit_data()
    for si in range(4):
        print(f"  s_{si}: {len(od[si])} swap orbits; "
              f"units present: {sorted(set(o['units'] for o in od[si]))}")
        # break down by units
        units_counts = Counter(o['units'] for o in od[si])
        print(f"    units distribution: {dict(units_counts)}")
    print()
    print("Sanity: rho check. rho_F4 = (11/2, 5/2, 3/2, 1/2)")
    F = Fraction
    rho_calc = [F(0), F(0), F(0), F(0)]
    for r, _ in pr:
        for k in range(4):
            rho_calc[k] += r[k]
    rho_calc = tuple(x / 2 for x in rho_calc)
    print(f"  computed rho = {rho_calc}")
