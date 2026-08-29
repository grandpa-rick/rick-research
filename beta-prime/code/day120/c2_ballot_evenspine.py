"""C2: Even-parity spine Kostka at d_max, for odd j = 2l+1.

Even spine shapes: mu^{(m),even} = (3^{l+1-m}, 2^{2m}, 1^{l-1-m})
  m ranges over values for which each block-count is non-negative:
    l+1-m >= 0  (m <= l+1)
    2m >= 0     (m >= 0)
    l-1-m >= 0  (m <= l-1)
  So m in {0, 1, ..., l-1} PLUS the boundary cases where the 1's or 2's block collapses.
  Actually if l-1-m < 0, we drop the 1's block. But then the shape is (3^{l+1-m}, 2^{2m}).
  If 2m = 0, we drop the 2's block.

Content: (2^{2l+1}) — 2l+1 labels each appearing twice, total 4l+2 boxes.

Shape size check: 3(l+1-m) + 2*(2m) + 1*(l-1-m) = 3l+3-3m + 4m + l-1-m = 4l+2. Good.

Conjugate mu': column 1 has length = # nonempty rows = (l+1-m) + 2m + (l-1-m) = 2l.
  So mu' has parts summing to 4l+2, first part = 2l.

Column lengths of mu':
  col 1: (l+1-m) + 2m + (l-1-m) = 2l  (length of first block, i.e. total rows)
  col 2: (l+1-m) + 2m = l+1+m
  col 3: l+1-m

Column-strict tableau on mu' = row-strict on mu equivalent to SSYT of mu'.
Column 1 has length 2l but we have 2l+1 distinct labels; so exactly ONE label is skipped in column 1.

Ballot-type combinatorics:
  Column 1 must have 2l distinct labels in strictly increasing order (since it's a column).
  So we pick 2l labels out of 2l+1 (one label is skipped) — but each label has multiplicity 2 in content.
  So the skipped label goes elsewhere (both copies), and each of the 2l chosen labels has 1 remaining copy.

Let s be the skipped label (s in {1, ..., 2l+1}).
Then column 1 = the 2l labels other than s, in order.
Remaining labels for columns 2 and 3: {label i, multiplicity: 2 if i=s, 1 otherwise}.
Column 2 has length l+1+m, column 3 has length l+1-m.
Total remaining = 2l+2, i.e., column 2 length + column 3 length = (l+1+m) + (l+1-m) = 2l+2. Good.

Now we need to fill columns 2 and 3 with a column-strict SSYT of the "residual shape".
The residual shape (after removing column 1) is mu' with column 1 stripped, which has row lengths
(mu'_i - 1) for each row where mu'_i >= 1. Actually think of it as: rows 1..2l have length mu_i - 1.
  Row i has length (mu_i - 1) if mu_i >= 1.

Let me re-parametrize by rows. Rows:
  row 1..(l+1-m): length 3
  row (l+2-m)..(l+1+m): length 2   [wait, rows (l+2-m) through (l+1+m) — that's 2m rows]
  row (l+2+m)..(2l): length 1      [that's l-1-m rows]

After removing column 1 (one box from each row):
  rows 1..(l+1-m): length 2
  rows (l+2-m)..(l+1+m): length 1
  rows (l+2+m)..(2l): length 0

The residual shape is (2^{l+1-m}, 1^{2m}). This has 2(l+1-m) + 2m = 2l+2 boxes. Good.

We need a column-strict tableau of shape (2^{l+1-m}, 1^{2m}) with:
  - Each label in {1..2l+1} \ {s} appears exactly 1 time
  - Label s appears exactly 2 times
Additionally, in column 1 of the residual (which corresponds to column 2 of mu'),
  we still need column-strict (increasing down); and rows are weakly increasing.
  Also we need consistency with the original column 1 = labels {1..2l+1}\{s} in order.

Let's think about ORIGINAL column 2 and column 3 of mu' as columns of length (l+1+m) and (l+1-m).

Constraint from column-strict: within column, strictly increasing.
Constraint from row-weakly increasing: In each row of mu, row entries weakly increasing.

For row i (which has 3 or 2 or 1 entries), entries are weakly increasing.
Since column 1 entries are all distinct, and column 2 entries are all distinct,
row i has: col1[i], col2[i] (if exists), col3[i] (if exists), weakly increasing.

Let's think of this in terms of PATHS / lattice paths, as with ballot.
--------------
Let's just compute the Kostkas for small l, m and look at the values.
"""

from math import comb
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
from kostka import kostka_mu_prime_2j


def make_even_spine(l, m):
    """mu^{(m),even} = (3^{l+1-m}, 2^{2m}, 1^{l-1-m})."""
    a = l + 1 - m
    b = 2 * m
    c = l - 1 - m
    parts = []
    if a > 0:
        parts += [3] * a
    if b > 0:
        parts += [2] * b
    if c > 0:
        parts += [1] * c
    return tuple(parts)


def conjugate(mu):
    if not mu:
        return ()
    return tuple(sum(1 for x in mu if x > i) for i in range(mu[0]))


def compute_kostka_evenspine(l, m):
    """K_{mu^{(m),even}', (2^{2l+1})}."""
    shape = make_even_spine(l, m)
    mu = conjugate(shape)
    return kostka_mu_prime_2j(mu)


def valid_m_range(l):
    """m values such that mu^{(m),even} is a valid partition with content (2^{2l+1}).
    We need a = l+1-m >= 0, b = 2m >= 0, c = l-1-m >= 0.
    But even when c < 0 (i.e., m > l-1, i.e., m = l or m = l+1) or a = 0,
    the shape might still exist as a partition of 4l+2.
    Let's check when |shape| = 4l+2 requires:
      3(l+1-m) + 4m + (l-1-m) = 4l+2  always (if all nonneg).
    If we allow c < 0, we're not adding those rows, so |shape| = 3(l+1-m) + 4m.
    That equals 4l+2 iff 3l+3-3m+4m = 4l+2 iff m = l-1. So c=0 gives right size at m=l-1.
    We must have c >= 0 and a >= 0 and b >= 0.
    So m in {0, 1, ..., l-1} (when l >= 1), plus we should check m = l, l+1?
    """
    return list(range(max(0, 0), l))  # m = 0, 1, ..., l-1


def survey():
    print("=== Even-parity spine Kostkas, C2 case (odd j = 2l+1) ===\n")
    for l in range(1, 8):
        j = 2*l + 1
        print(f"l = {l} (j = {j}):")
        for m in valid_m_range(l):
            shape = make_even_spine(l, m)
            K = compute_kostka_evenspine(l, m)
            # For comparison, ballot-like combos
            # Guess 1: sum over "skipped label" s of some binomial
            # Guess 2: comb(2l+1, l-m) - comb(2l+1, l-m-1) ??? — that would be j = 2l+1 case
            # or perhaps we get (2l+1) * (ballot with l-1?) — try both.
            print(f"  m={m}, shape={shape}, K={K}")
        print()


def survey_with_alternating():
    print("=== Alternating sum A_even(l) ===\n")
    for l in range(1, 12):
        j = 2*l + 1
        total = 0
        for m in valid_m_range(l):
            shape = make_even_spine(l, m)
            K = compute_kostka_evenspine(l, m)
            # sign = (-1)^{(mu_2 - mu_3)/2}
            # In our shape: mu_2 = 3 if l+1-m >= 2, else other cases
            # Actually mu here has parts labeled: mu[0], mu[1], mu[2]
            # But the shape may collapse. Let's look at rows 1,2,3 of the shape.
            if len(shape) < 2:
                continue
            mu2 = shape[1] if len(shape) > 1 else 0
            mu3 = shape[2] if len(shape) > 2 else 0
            assert (mu2 - mu3) % 2 == 0, f"Not even parity at l={l}, m={m}"
            sign = (-1) ** ((mu2 - mu3) // 2)
            total += sign * K
        expected = (-1)**(l+1)
        ok = "OK" if total == expected else f"!!! got {total}, expected {expected}"
        print(f"l = {l}: A_even = {total}, expected (-1)^(l+1) = {expected}  {ok}")


if __name__ == "__main__":
    survey()
    survey_with_alternating()
