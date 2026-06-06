"""
Compute the KL basis of the Hecke algebra H(W(B_2); q) and identify left cells,
following the standard recursive construction.

Conventions:
  W(B_2) = <s_0, s_1 | s_0^2 = s_1^2 = 1, (s_0 s_1)^4 = 1>.
  In Rick's conventions for aug_tilde_B2.py:
     s_0 (long) = swap coords 0,1   (the long simple root e_0 - e_1)
     s_1 (short) = sign-flip on coord 1  (short simple root e_1)
  But aug_tilde_B2.py code uses 's_2' for sign-flip (its 'M_2' move) and 's_1' for swap (M_1).

  Per the SA proof note (page 1 of 2026-05-07 file), the *paper* convention is:
    α_0 = e_0 - e_1 (long), α_1 = e_1 (short).
    s_0 = swap, s_1 = sign-flip on coord 1.
    Aug~ priority: M_2 first (which corresponds to short simple α_1), then M_1.

  GY paper uses an arbitrary indexing; we'll use I = {0, 1} with the paper's conventions:
    s_0 = swap (long), s_1 = sign-flip (short).

  Hecke algebra: T_i^2 = (q-1) T_i + q.  At q=1 specialization, T_i ↦ s_i.

Approach:
  1. Enumerate W(B_2) by signed permutations of {1, 2}: each w = (perm, signs).
  2. Compute Bruhat order via reduced expressions.
  3. Compute KL polynomials P_{x,w}(q) recursively via Kazhdan-Lusztig recursion.
  4. C_w = sum_{x ≤ w} P_{x,w}(q) q^{-(ℓ(w)-ℓ(x))/2} T_x  (we use the slightly-shifted
     convention where C_w is self-dual under the bar involution).
  5. For each i ∈ I, compute T_i · C_w in the KL basis: this gives the action on KL
     basis. The coefficient on C_x for x < w determines the left preorder ≤_L.
  6. Equivalence classes under ≤_L are left cells.

We do everything at q = 1 specialization (which is what GY uses): C[W] with KL basis,
so we just need the leading-term action of s_i on C_w in the KL basis (the "mu-coefficients").
"""

from fractions import Fraction
from itertools import permutations, product


# ============== W(B_2) elements as signed permutations ==============

# A signed permutation acts on (v_0, v_1) -> (sigma_0 * v_{pi_0}, sigma_1 * v_{pi_1})
# where pi is a permutation of {0,1} and sigma_i = +/-1.

def all_elements_B2():
    """Return list of all 8 signed permutations as tuples ((pi_0, pi_1), (s_0, s_1))."""
    elts = []
    for pi in permutations([0, 1]):
        for signs in product([1, -1], repeat=2):
            elts.append((pi, signs))
    return elts


def apply_perm(w, v):
    """Apply w = (pi, signs) to vector v."""
    pi, signs = w
    return tuple(signs[i] * v[pi[i]] for i in range(2))


def multiply(w1, w2):
    """Compose w1 * w2: (w1 * w2)(v) = w1(w2(v))."""
    pi1, sg1 = w1
    pi2, sg2 = w2
    # (w1 w2)(v)_i = sg1[i] * (w2(v))_{pi1[i]} = sg1[i] * sg2[pi1[i]] * v[pi2[pi1[i]]]
    new_pi = tuple(pi2[pi1[i]] for i in range(2))
    new_sg = tuple(sg1[i] * sg2[pi1[i]] for i in range(2))
    return (new_pi, new_sg)


# Simple reflections in our convention: s_0 = swap (long), s_1 = sign-flip on last coord (short).
# In B_n general:
#   s_0 = sign flip on last coord (short, for the short simple root α_n = e_n)  -- but
# Wait — for B_2, there are two conventions in the literature. Let me clarify using
# the SA note: "simple roots are α_0 = e_0 - e_1 (long) and α_1 = e_1 (short)".
# So in our index 0-based:
#   s_0: long, swap coords 0, 1.
#   s_1: short, flip sign of coord 1.

S0 = ((1, 0), (1, 1))    # swap
S1 = ((0, 1), (1, -1))   # flip sign of coord 1
ID = ((0, 1), (1, 1))


def positive_roots_B2():
    """Return list of (root, kind) for positive roots of B_2."""
    return [
        ((1, -1), 'L'),  # alpha_0 = e_0 - e_1 (long, simple)
        ((0, 1), 'S'),   # alpha_1 = e_1 (short, simple)
        ((1, 1), 'L'),   # e_0 + e_1 (long)
        ((1, 0), 'S'),   # e_0 (short)
    ]


def length(w):
    """Coxeter length = #{positive roots sent to negative roots}."""
    proots = [r for r, _ in positive_roots_B2()]
    nroots = [tuple(-x for x in r) for r in proots]
    cnt = 0
    for r in proots:
        if apply_perm(w, r) in nroots:
            cnt += 1
    return cnt


def reduced_word(w):
    """Return one reduced word in terms of [0, 1] indexing simple reflections."""
    if w == ID:
        return ()
    # Greedy: find a simple reflection s_i such that ℓ(s_i w) < ℓ(w).
    proots = [r for r, _ in positive_roots_B2()]
    # s_i w sends the roots; we use length descent.
    for i, s in enumerate([S0, S1]):
        sw = multiply(s, w)
        if length(sw) < length(w):
            return (i,) + reduced_word(sw)
    raise RuntimeError("No descent found")


def all_reduced_words(w):
    """Enumerate ALL reduced expressions for w (used for testing)."""
    if w == ID:
        return [()]
    out = []
    for i, s in enumerate([S0, S1]):
        sw = multiply(s, w)
        if length(sw) < length(w):
            for tail in all_reduced_words(sw):
                out.append((i,) + tail)
    return out


# Bruhat order: x ≤ w iff some (equivalently, every) reduced word for w contains
# a reduced subword for x. For computational ease, use the *subword property*.

def bruhat_le(x, w):
    """x ≤ w in Bruhat order iff some reduced subword."""
    rw = reduced_word(w)
    return _has_subword(x, rw)


def _has_subword(x, word):
    if x == ID:
        return True
    if not word:
        return False
    i = word[0]
    rest = word[1:]
    s = [S0, S1][i]
    sx = multiply(s, x)
    # case 1: skip this letter
    if _has_subword(x, rest):
        return True
    # case 2: use this letter to absorb (s_i x has length ℓ(x) - 1, then continue)
    if length(sx) < length(x) and _has_subword(sx, rest):
        return True
    return False


# ============== KL polynomials P_{x,w}(q) ==============
# Recurrence (Kazhdan-Lusztig 1979):
#   For s_i in left descent set DL(w) (i.e., ℓ(s_i w) < ℓ(w)), set sw := s_i w. Then
#     P_{x, w}(q) = q^{1-c} * P_{s_i x, sw}(q) + q^c * P_{x, sw}(q)
#                   - sum_{x ≤ z < sw, s_i z < z} mu(z, sw) q^{(ℓ(w) - ℓ(z))/2} P_{x, z}(q)
#   where c = 1 if s_i x < x else 0.
#
# Here mu(z, sw) = coefficient of q^{(ℓ(sw) - ℓ(z) - 1)/2} in P_{z, sw}.
#
# Initial: P_{x, x} = 1, P_{x, w} = 0 if x not ≤ w.
#
# We build a memoized table.

# Let's work with polynomials as dict {q-deg : int_coeff}.
# Use Python ints, exponents are nonneg integers. We use q (not q^{1/2}).

def poly_zero():
    return {}

def poly_const(c):
    return {0: c} if c != 0 else {}

def poly_add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}

def poly_sub(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v != 0}

def poly_scale(p, c):
    return {k: v * c for k, v in p.items() if v * c != 0}

def poly_shift(p, n):
    """Multiply by q^n."""
    return {k + n: v for k, v in p.items()}

def poly_mul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = k1 + k2
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def kl_polynomial_table(elements):
    """Build P[x, w] for all x, w in W."""
    # Sort by length
    elts_by_len = sorted(elements, key=length)
    P = {}
    # P_{x, x} = 1
    for w in elts_by_len:
        P[(w, w)] = poly_const(1)
    # P_{x, w} = 0 if not x ≤ w (omit from table; treat as 0)

    # Now fill in by increasing ℓ(w)
    for w in elts_by_len:
        lw = length(w)
        if lw == 0:
            continue
        # find a left descent s_i
        s_idx = None
        for i, s in enumerate([S0, S1]):
            sw = multiply(s, w)
            if length(sw) < lw:
                s_idx = i
                s_elt = s
                sw_elt = sw
                break
        assert s_idx is not None
        # For each x ≤ w (x != w), compute P_{x, w}
        for x in elts_by_len:
            if x == w:
                continue
            if not bruhat_le(x, w):
                P[(x, w)] = poly_zero()
                continue
            # KL recurrence
            sx = multiply(s_elt, x)
            c = 1 if length(sx) < length(x) else 0

            # P_{s_i x, sw}
            term1 = P.get((sx, sw_elt), poly_zero())
            term1 = poly_shift(term1, 1 - c)

            # P_{x, sw}
            term2 = P.get((x, sw_elt), poly_zero())
            term2 = poly_shift(term2, c)

            result = poly_add(term1, term2)

            # Subtraction sum
            for z in elts_by_len:
                if length(z) >= length(sw_elt):
                    continue
                if not bruhat_le(x, z):
                    continue
                # need s_i z < z
                sz = multiply(s_elt, z)
                if length(sz) >= length(z):
                    continue
                # need z < sw and z ≠ sw
                if z == sw_elt or not bruhat_le(z, sw_elt):
                    continue
                # mu(z, sw)
                Pzsw = P.get((z, sw_elt), poly_zero())
                ldiff = length(sw_elt) - length(z) - 1
                if ldiff % 2 != 0:
                    continue
                mu_exp = ldiff // 2
                mu = Pzsw.get(mu_exp, 0)
                if mu == 0:
                    continue
                # subtract mu * q^{(ℓ(w) - ℓ(z))/2} * P_{x, z}
                lwz = length(w) - length(z)
                if lwz % 2 != 0:
                    continue
                shift = lwz // 2
                Pxz = P.get((x, z), poly_zero())
                contribution = poly_shift(poly_scale(Pxz, mu), shift)
                result = poly_sub(result, contribution)

            P[(x, w)] = result
    return P


# ============== Left preorder ≤_L from KL theory ==============
#
# x ≤_L y iff there exists a chain x = x_0 <-i_1- x_1 <-i_2- ... <-i_r- x_r = y
# where x_{j-1} <-i- x_j means C_{x_{j-1}} appears with nonzero coeff in s_{i} · C_{x_j}.
#
# In the KL basis at q = 1, we have
#   s_i · C_w = -C_w + sum (or similar; precise formula from KL)
# More precisely (Lusztig, "Hecke algebras with unequal parameters" §4):
#   T_i C_w = -C_w + ... (when s_i in DL(w))
#   T_i C_w = q C_w + q^{1/2} sum_{z: s_i z < z} mu(z, w) C_z  (when s_i not in DL(w))
#
# At q = 1, in C[W]:
#   if s_i ∈ DL(w):  s_i C_w = -C_w  (so x = w, no new x's appear with nonzero coeff in s_i C_w; well, plus the same z's)
# Wait — let me be more careful. The standard formula in the Hecke algebra is:
#   C'_{s_i} · C'_w = (q^{1/2} + q^{-1/2}) C'_w           if s_i ∈ DL(w)
#                  = C'_{s_i w} + sum_{z ≺ w, s_i z < z} mu(z,w) C'_z  if s_i ∉ DL(w)
# where C'_{s_i} = q^{-1/2} (T_i + 1).
#
# At q = 1, C'_{s_i} = T_i + 1 = s_i + 1 ∈ Z[W].
# So (s_i + 1) · C_w = 2 C_w if s_i ∈ DL(w),
#    (s_i + 1) · C_w = C_{s_i w} + sum mu(z,w) C_z otherwise.
#
# Hence s_i · C_w = C_w if s_i ∈ DL(w) and (... C_w + sum) doesn't necessarily make sense?
# Actually at q=1 the q-shift information is lost. Let me re-think.
#
# Actually we don't need the action coefficients at q=1; for ≤_L we need:
#   x <-i- y  iff  C_x appears with nonzero coeff in (T_i · C_y) [or equivalently s_i C_y]
# in the Hecke algebra at the polynomial level. The relation at q=1 is fine.
#
# Concretely: for s_i NOT a left descent of y (so s_i y > y),
#   T_i C_y has C_{s_i y} (with coeff q) and C_z for z with s_i z < z, mu(z, y) ≠ 0.
# So C_x appears nontrivially iff x = s_i y or x = some z with s_i z < z and mu(z, y) > 0.
#
# For s_i IS a left descent (s_i y < y),
#   T_i C_y = -C_y + ... no, let me compute. In normalized form C'_{s_i}:
#   C'_{s_i} C'_y = (q^{1/2} + q^{-1/2}) C'_y  (when s_i ∈ DL(y))
# So T_i C_y = ((q-1)/(q^{1/2} + q^{-1/2}) ) C_y + (q^{1/2} + q^{-1/2})^{-1} ...
# Hmm — this is getting messy. Let me just use the formula:
#
#   For s_i ∉ DL(y) (i.e., s_i y > y):  C_{s_i y} appears in T_i C_y, plus terms C_z for z with mu(z,y) ≠ 0 and s_i ∈ DL(z).
#   For s_i ∈ DL(y) (i.e., s_i y < y):  the action of T_i is simpler — C'_{s_i} acts as scalar, so no new C_x's appear.

def is_left_descent(i, w):
    s = [S0, S1][i]
    return length(multiply(s, w)) < length(w)


def left_preorder_relations(P, elements):
    """Build set of pairs (x, y) with x ≤_L y elementarily (one-step).

    x <-i- y iff C_x appears with nonzero coefficient in s_i · C_y in the Hecke algebra.

    From the KL theory:
      - If s_i ∈ DL(y) (s_i y < y): the only nonzero coefficients in s_i · C_y are on
        C_y itself (with some coefficient depending on q) -- so no new x's. Skip.
      - If s_i ∉ DL(y):
          * x = s_i y appears with nonzero coefficient.
          * For each z with s_i ∈ DL(z), z < y, mu(z, y) ≠ 0: x = z appears.
    """
    one_step = set()
    for y in elements:
        for i in [0, 1]:
            if is_left_descent(i, y):
                # Only C_y itself appears with potentially-changed coeff. No new x.
                continue
            sy = multiply([S0, S1][i], y)
            # x = s_i y
            one_step.add((sy, y))
            # x = z for z with s_i z < z, mu(z, y) ≠ 0
            for z in elements:
                if z == y:
                    continue
                if length(z) >= length(y):
                    continue
                if not is_left_descent(i, z):
                    continue
                if not bruhat_le(z, y):
                    continue
                ldiff = length(y) - length(z) - 1
                if ldiff % 2 != 0:
                    continue
                Pzy = P.get((z, y), {})
                mu = Pzy.get(ldiff // 2, 0)
                if mu != 0:
                    one_step.add((z, y))
    return one_step


def transitive_closure(pairs, elements):
    """Compute reflexive-transitive closure."""
    reachable = {x: {x} for x in elements}
    for x, y in pairs:
        # x ≤ y, so reachable_from_y includes x... wait, semantics:
        # one_step has (x, y) with x ≤_L y elementarily.
        # We want x ≤_L y iff there is a chain x = x_0, x_1, ..., x_r = y where x_{j-1} ≤_L x_j elementarily.
        pass
    # Build adjacency: for each y, predecessors set.
    pred = {x: set() for x in elements}
    for x, y in pairs:
        pred[y].add(x)
    # Floyd-Warshall-like
    le = {(x, x) for x in elements}
    for x, y in pairs:
        le.add((x, y))
    changed = True
    while changed:
        changed = False
        new = set(le)
        for (a, b) in le:
            for (b2, c) in le:
                if b == b2 and (a, c) not in le:
                    new.add((a, c))
                    changed = True
        le = new
    return le


def compute_left_cells(elements, P):
    """Return list of left cells (each a frozenset)."""
    one_step = left_preorder_relations(P, elements)
    le = transitive_closure(one_step, elements)
    # Equivalence: x ~ y iff x ≤ y and y ≤ x.
    cells_by_rep = {}
    elt_to_cell = {}
    for x in elements:
        for y in elements:
            if (x, y) in le and (y, x) in le:
                # same cell
                pass
        # collect all y's equivalent to x
        cell = frozenset(y for y in elements if (x, y) in le and (y, x) in le)
        cells_by_rep[cell] = cell
    return list(cells_by_rep.values())


# ============== Main: enumerate cells of W(B_2) ==============

def main():
    elements = all_elements_B2()
    # Sort by length, then lex
    elements_sorted = sorted(elements, key=lambda w: (length(w), w))
    print("=== Elements of W(B_2) by length ===")
    name_of = {}
    for w in elements_sorted:
        rw = reduced_word(w)
        name = "e" if not rw else "".join(f"s{i}" for i in rw)
        name_of[w] = name
        print(f"  {name:<14s}  ℓ={length(w)}  {w}")

    print("\n=== KL polynomials P_{x,w}(q) (only nonzero, x < w) ===")
    P = kl_polynomial_table(elements_sorted)
    nonzero_kl = []
    for (x, w), p in sorted(P.items(), key=lambda kv: (length(kv[0][1]), length(kv[0][0]))):
        if x == w:
            continue
        if not p:
            continue
        nonzero_kl.append((x, w, p))
        s = " + ".join(f"{c}q^{k}" if k > 0 else f"{c}" for k, c in sorted(p.items()))
        print(f"  P[{name_of[x]:<10s} , {name_of[w]:<10s}] = {s}")

    print(f"\nTotal nonzero P_{{x,w}} (x<w) = {len(nonzero_kl)}")
    print("(In W(B_2), all P_{x,w} are 1 [Hagiwara/Bremke?] — let's check.)")
    all_constant_one = all(p == {0: 1} for _, _, p in nonzero_kl)
    print(f"All P_{{x,w}} = 1: {all_constant_one}")

    print("\n=== Left preorder one-step relations x <-i- y ===")
    one_step = left_preorder_relations(P, elements_sorted)
    for (x, y) in sorted(one_step, key=lambda p: (length(p[1]), length(p[0]))):
        print(f"  {name_of[x]:<10s}  ≤_L  {name_of[y]:<10s}")

    print("\n=== Left cells of W(B_2) ===")
    cells = compute_left_cells(elements_sorted, P)
    for i, cell in enumerate(sorted(cells, key=lambda c: (-len(c), [length(x) for x in c]))):
        names = sorted([name_of[w] for w in cell])
        print(f"  Cell {i+1}: size={len(cell)}, elements = {names}")

    return elements_sorted, name_of, P, cells


if __name__ == "__main__":
    main()
