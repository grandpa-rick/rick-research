"""Experiment 5: q-lift of Identity (A) at d = d_max.

Question: does
  sum_{d_mu = d_max(j)} (-1)^{(mu_2 - mu_3)/2} K_{mu', (2^j)}(q) = 0
hold as a polynomial identity in q?

Here K_{lambda, nu}(q) is the Kostka-Foulkes polynomial, aka K_{lambda,nu}(q) =
  sum over T in SSYT(lambda, nu) of q^{charge(T)}
(Lascoux-Schutzenberger charge statistic).

We compute for j = 3, 5 (odd, small).

STRATEGY. We compute K_{mu', (2^j)}(q) directly by:
  1. Enumerating SSYT of shape mu' with content (2^j) — each of 1, 2, ..., j appears
     exactly twice.
  2. For each SSYT, compute charge = sum of charges of its reading word.
  3. Sum q^{charge}.

Since mu has at most 3 parts, mu' has parts of size at most 3. So SSYT of shape mu'
are columns of size at most 3.
"""

from functools import lru_cache
from sympy import symbols, expand, Integer, Poly, simplify

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
from kostka import kostka_mu_prime_2j, d_mu

q = symbols('q')


# ---- SSYT enumeration ----

def enumerate_ssyt(shape, content):
    """Enumerate all SSYT of given shape with given content.
    shape: tuple of row lengths (weakly decreasing).
    content: tuple of multiplicities.
    Returns list of tableaux as tuples of tuples (rows).
    """
    # Total boxes
    n = sum(shape)
    if sum(content) != n:
        return []
    # Available letters: for content = (c_1, ..., c_r), letter i has multiplicity c_i.
    max_letter = len(content)

    # Fill row by row, left to right, using backtracking.
    rows = [[] for _ in shape]
    remaining = list(content)
    results = []

    def backtrack(row_idx, col_idx):
        # Find next empty cell in row-major order.
        while row_idx < len(shape) and col_idx >= shape[row_idx]:
            row_idx += 1
            col_idx = 0
        if row_idx == len(shape):
            # Complete
            results.append(tuple(tuple(r) for r in rows))
            return
        # Determine valid range for cell (row_idx, col_idx).
        # SSYT: strictly increasing down columns, weakly increasing along rows.
        min_val = 1
        if col_idx > 0:
            min_val = max(min_val, rows[row_idx][col_idx - 1])  # >= left
        if row_idx > 0:
            min_val = max(min_val, rows[row_idx - 1][col_idx] + 1)  # > above
        for v in range(min_val, max_letter + 1):
            if remaining[v - 1] == 0:
                continue
            rows[row_idx].append(v)
            remaining[v - 1] -= 1
            backtrack(row_idx, col_idx + 1)
            rows[row_idx].pop()
            remaining[v - 1] += 1

    backtrack(0, 0)
    return results


# ---- Reading word ----

def reading_word(T):
    """Reading word of tableau T: read rows top-to-bottom, right-to-left within each row
    (Japanese reading).  Actually the standard convention for charge: reverse-column
    reading — but Lascoux-Schutzenberger use a specific reading.  We use the row-reading
    from top-to-bottom, right-to-left in each row (which is the same as reading columns
    bottom-to-top left-to-right for SSYT).

    Convention check: for K_{lambda, mu}(q) = sum q^{charge(w)} over w in words of weight
    mu that rectify to shape lambda under RSK, the charge is defined on words. On SSYTs,
    the natural reading is: reading word of T = concatenation of rows from top to bottom,
    each row read from RIGHT to LEFT.
    """
    w = []
    for row in T:
        for x in reversed(row):
            w.append(x)
    return w


# ---- Charge of a word ----

def charge_of_word(w):
    """Charge of a word w with partition content (weakly decreasing content).
    Definition (Lascoux-Schutzenberger):
      1. If content is a partition mu, extract standard subwords iteratively.
      2. For each standard subword sw = (a_1, ..., a_n) (permutation of 1..n),
         assign indices: index(a_1) = 0; index(a_{i+1}) = index(a_i) + (0 if
         a_{i+1} > a_i else 1).  Wait — need to be careful.

    Standard recipe (from Sage docs / literature):
      Given a word w with partition content, decompose w into standard subwords
      by picking off, from right to left, the smallest letter not yet chosen at
      each step (making one "standard subword" per letter of the largest part).
      Actually let me use the direct algorithm.

    Algorithm (Butler / LS, following Macdonald):
      Given w with partition content mu = (mu_1 >= mu_2 >= ...),
      1. If content is not a partition, charge is 0 or undefined.
      2. Otherwise, extract mu_r "standard subwords" (r = number of parts):
         a. Scan w from RIGHT to LEFT.
         b. First pass: mark the rightmost 1. From that position, scanning left
            (cyclically wrapping), find the next 2, then 3, etc.  Result: a
            standard subword containing one copy of each letter 1..r.
         c. Remove marked letters; repeat.
      3. For each standard subword of length k, its charge is the sum over
         positions i = 2, ..., k of (index of i-th element), where indices are
         assigned as follows: start reading the standard subword from position
         of "1" going right (cyclically). Then index(1) = 0, and each subsequent
         letter j+1 gets index(j) if it appears after j (in cyclic reading order),
         else index(j) + 1.

    This is the standard "cyclic" definition of charge.

    See e.g. Macdonald, "Symmetric Functions and Hall Polynomials", 2nd ed, III.6.
    """
    from collections import Counter
    cnt = Counter(w)
    # Content must be a partition
    parts = sorted(cnt.values(), reverse=True)
    # Extract standard subwords
    remaining = list(w)  # work with mutable list
    total_charge = 0
    r = max(cnt.keys()) if cnt else 0
    while remaining:
        # Extract one standard subword of length r (contains one of each 1..r)
        # Scan RIGHT to LEFT, cyclic; pick 1 first, then 2, ... , r.
        n = len(remaining)
        # Find rightmost 1
        indices_taken = []  # indices into remaining
        # Start: find rightmost 1.
        pos = None
        for i in range(n - 1, -1, -1):
            if remaining[i] == 1:
                pos = i
                break
        if pos is None:
            break  # no more 1's — can't continue standard subwords
        indices_taken.append(pos)
        # Now for letter = 2, 3, ..., find next occurrence scanning LEFT from pos-1
        # cyclically.
        current_pos = pos
        for letter in range(2, r + 1):
            # Scan cyclically going LEFT from current_pos - 1
            found = None
            for step in range(1, n + 1):
                i = (current_pos - step) % n
                if remaining[i] == letter and i not in indices_taken:
                    found = i
                    break
            if found is None:
                break
            indices_taken.append(found)
            current_pos = found
        if len(indices_taken) < r:
            # Standard subword incomplete — content wasn't rectangular, need to
            # handle. In our case content = (2^j), letters 1..j each appearing 2x,
            # so content IS rectangular (partition (2,2,...,2)), and standard
            # subwords should always be complete.
            break
        # Compute charge of this standard subword.
        # The subword is read in cyclic order starting from position of "1".
        # Sort indices_taken so they align with the letters 1, 2, ..., r (since
        # we appended in order).
        # letter i has position indices_taken[i-1] in remaining.
        # Charge: start with index(1) = 0. For i = 2..r, index(i) = index(i-1) +
        # (1 if letter i is to the LEFT of letter i-1 in the word — equivalently,
        # if we had to "wrap around" — else 0).
        # More precisely: index(i) - index(i-1) = 1 if the LEFT-cyclic scan from
        # letter i-1's position to letter i's position wrapped around, else 0.
        # But actually the convention is even simpler: index(i) = index(i-1) + 1
        # if position(i) > position(i-1) (in linear order), else index(i) = index(i-1).
        # Wait, I need to double check.
        #
        # Standard formulation (e.g., Sage's charge on words):
        #   Given a standard word w = (w_1, w_2, ..., w_n) which is a permutation of
        #   1..n, its charge is sum_{i=1}^{n} c(i) where c(i) = c(i-1) + 1 if i
        #   comes AFTER i-1 in w (i.e., position of i is > position of i-1), else
        #   c(i) = c(i-1); with c(1) = 0.
        # WAIT — that's for a linear word (permutation).
        # But we extracted using cyclic scanning; the resulting standard subword's
        # letters are at certain positions in `remaining`. The linear positions of
        # letters 1, 2, ..., r are indices_taken[0], indices_taken[1], ...
        #
        # For charge of a standard word (permutation), the standard definition is:
        #   Read the word LEFT to RIGHT. For each letter i (2 <= i <= n), let pos(i)
        #   be its position. c(1) = 0. c(i) = c(i-1) + 1 if pos(i) < pos(i-1) else
        #   c(i-1).  [Some sources: c(i) = c(i-1) + 1 if pos(i) > pos(i-1) else
        #   c(i-1) + 0.  Sign conventions vary — need to fix by testing K((n),
        #   (1^n))(q) = 1 or [n]_q!.]
        #
        # Let me use the convention from Macdonald III.6.5:
        #   For a standard word w (permutation of {1,...,n}), the charge is:
        #     c(w) = sum_{i=1}^{n} index_w(i)
        #   where index_w(i) is defined as follows: index_w(1) = 0, and for
        #   i > 1, index_w(i) = index_w(i-1) if i appears to the RIGHT of i-1 in w,
        #   and index_w(i) = index_w(i-1) + 1 if i appears to the LEFT of i-1 in w.
        # (This is what Sage does.)
        pos_of = {i + 1: indices_taken[i] for i in range(len(indices_taken))}
        idx = 0
        subword_charge = 0
        for letter in range(2, r + 1):
            if pos_of[letter] < pos_of[letter - 1]:
                idx += 1
            subword_charge += idx
        total_charge += subword_charge
        # Remove the marked letters
        for i in sorted(indices_taken, reverse=True):
            remaining.pop(i)
    return total_charge


def kostka_foulkes(shape, content):
    """K_{shape, content}(q) = sum_{T in SSYT(shape, content)} q^{charge(reading(T))}."""
    total = Integer(0)
    for T in enumerate_ssyt(shape, content):
        w = reading_word(T)
        c = charge_of_word(w)
        total += q ** c
    return expand(total)


def transpose(shape):
    """Transpose partition."""
    if not shape:
        return ()
    n = shape[0]
    out = []
    for i in range(n):
        col = sum(1 for r in shape if r > i)
        out.append(col)
    return tuple(out)


def all_mu_3parts(twoj):
    for m1 in range(twoj + 1):
        for m2 in range(min(m1, twoj - m1) + 1):
            m3 = twoj - m1 - m2
            if m3 > m2 or m3 < 0:
                continue
            yield (m1, m2, m3)


def kostka_foulkes_mu_prime_2j(mu, j):
    """K_{mu', (2^j)}(q)."""
    mu_p = transpose(mu)
    content = tuple([2] * j)
    return kostka_foulkes(mu_p, content)


# ---- Verification against classical Kostka ----

def verify_classical_limit():
    print("Verify K(q=1) = classical K for a few (mu, j):")
    for mu in [(2, 1, 1), (3, 2, 1), (4, 3, 3), (5, 3, 2), (5, 5, 0)]:
        j = sum(mu) // 2
        if sum(mu) % 2 != 0:
            continue
        Kq = kostka_foulkes_mu_prime_2j(mu, j)
        K_cls = kostka_mu_prime_2j(mu)
        val_at_1 = expand(Kq.subs(q, 1))
        marker = "OK" if val_at_1 == K_cls else "!!! MISMATCH"
        print(f"  mu={mu}, j={j}: K(q) = {Kq}, K(1)={val_at_1}, classical K = {K_cls}  {marker}")


def check_q_lift_identity_A(j, d):
    """Alternating sum of Kostka-Foulkes:
    sum_{mu: d_mu = d, mu_2 - mu_3 even} (-1)^{(mu_2 - mu_3)/2} K_{mu', (2^j)}(q)
    """
    twoj = 2 * j
    total = Integer(0)
    terms = []
    for mu in all_mu_3parts(twoj):
        if d_mu(mu) != d:
            continue
        if (mu[1] - mu[2]) % 2 != 0:
            continue
        sign = (-1) ** ((mu[1] - mu[2]) // 2)
        Kq = kostka_foulkes_mu_prime_2j(mu, j)
        total += sign * Kq
        terms.append((mu, sign, Kq))
    total = expand(total)
    return total, terms


def check_q_lift_identity_B(j, d):
    """Alternating sum for odd-parity family:
    sum_{mu: d_mu = d, mu_2 - mu_3 odd} (-1)^{(mu_2 - mu_3 - 1)/2} * ((mu_2 - mu_3 + 1)/2) * K_{mu', (2^j)}(q)
    """
    twoj = 2 * j
    total = Integer(0)
    terms = []
    for mu in all_mu_3parts(twoj):
        if d_mu(mu) != d:
            continue
        if (mu[1] - mu[2]) % 2 != 1:
            continue
        sign = (-1) ** ((mu[1] - mu[2] - 1) // 2)
        wt = (mu[1] - mu[2] + 1) // 2
        Kq = kostka_foulkes_mu_prime_2j(mu, j)
        total += sign * wt * Kq
        terms.append((mu, sign, wt, Kq))
    total = expand(total)
    return total, terms


def main():
    print("=" * 70)
    print("Sanity: K(q=1) matches classical K")
    print("=" * 70)
    verify_classical_limit()

    print()
    print("=" * 70)
    print("Kostka-Foulkes q-lift of Identity (A) at d = d_max")
    print("=" * 70)
    for j in [1, 3, 5]:
        d = j + j // 2
        total, terms = check_q_lift_identity_A(j, d)
        print(f"\nj={j}, d = d_max = {d} (odd-family Identity A):")
        for mu, sign, Kq in terms:
            print(f"  mu={mu}, sign={sign:+d}: K(q) = {Kq}")
        marker = "ZERO" if total == 0 else f"NONZERO = {total}"
        print(f"  Alternating sum = {marker}")

    print()
    print("=" * 70)
    print("Kostka-Foulkes q-lift of Identity (B) at d = d_max")
    print("=" * 70)
    for j in [1, 3, 5]:
        d = j + j // 2
        total, terms = check_q_lift_identity_B(j, d)
        print(f"\nj={j}, d = d_max = {d} (odd-family Identity B):")
        for mu, sign, wt, Kq in terms:
            print(f"  mu={mu}, sign={sign:+d}, wt={wt}: K(q) = {Kq}")
        marker = "ZERO" if total == 0 else f"NONZERO = {total}"
        print(f"  Alternating sum = {marker}")


if __name__ == "__main__":
    main()
