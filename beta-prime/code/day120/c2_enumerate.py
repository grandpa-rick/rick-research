"""Enumerate SSYT of shape (2l, l+1+r, l+1-r)' with content (2^{2l+1}),
sliced by the SKIPPED LABEL in column 1.

mu = (2l, l+1+r, l+1-r), so mu' has:
  col 1 length = 3 (all three parts nonempty)
  col 2 length = 3 (all mu_i >= 2)
  col 3 length = # with mu_i >= 3
  col c for c >= 4: varies
  ...

Wait — mu has 3 parts (3-part partition), so mu' has AT MOST 3 in each column, and rows of mu' are of length AT MOST 3. And there are mu_1 = 2l columns.

So mu' is a partition with 2l parts, each of size <= 3.
Specifically: mu' has some parts of size 3, some of size 2, some of size 1.

# parts of mu' of size 3 = # cols c of mu with c <= mu_3 = # cols in "full" region = mu_3
# parts of mu' of size 2 = mu_2 - mu_3
# parts of mu' of size 1 = mu_1 - mu_2

So mu' = (3^{mu_3}, 2^{mu_2 - mu_3}, 1^{mu_1 - mu_2})
      = (3^{l+1-r}, 2^{2r}, 1^{l-1-r})   [for even spine mu = (2l, l+1+r, l+1-r)]

So mu' has (l+1-r) + 2r + (l-1-r) = 2l parts. Good.

Now mu' is a SHAPE with 2l rows, and content (2^{2l+1}).
Rows have length 3, 2, or 1.

We fill row-by-row: row entries weakly increasing, columns strictly increasing.

Since content has 2l+1 distinct labels (each with multiplicity 2), and we have 2l ROWS (i.e., 2l
different "column 1" entries by column-strict), one label is unique to column 2 or 3 (i.e., both
copies of that label appear NOT in column 1).

Actually wait — column 1 of mu' has 2l entries, strictly increasing, from 2l+1 possible distinct labels.
So exactly one label is SKIPPED from column 1.

Since each label has multiplicity 2:
- The skipped label appears 2 times, both in columns 2 or 3 (or one in col 2, one in col 3).
- The 2l chosen labels each appear 1 more time (in column 2 or 3).

Wait but we ALSO have row weak-increase constraint: within a row, entries weakly increase.
So row = (col1, col2, col3) with col1 <= col2 <= col3 (weakly, with column-strict from above).

Let me enumerate directly for small cases.
"""

import itertools


def make_mu_prime(l, r):
    """mu' = (3^{l+1-r}, 2^{2r}, 1^{l-1-r})."""
    parts = []
    parts += [3] * (l + 1 - r)
    parts += [2] * (2 * r)
    parts += [1] * (l - 1 - r)
    return [p for p in parts if p > 0]


def enumerate_ssyt(shape, content):
    """Enumerate SSYT of given shape and content by direct recursion."""
    n_rows = len(shape)
    N_labels = len(content)
    # tab[i] = list of entries in row i so far
    def go(row_idx, prev_row, rem):
        if row_idx == n_rows:
            yield []
            return
        row_len = shape[row_idx]
        for row in fill_row(row_len, 0, prev_row, 1, list(rem)):
            for rest in go(row_idx + 1, row, [c for c in rem_after_row(rem, row)]):
                yield [row] + rest

    def rem_after_row(rem, row):
        r2 = list(rem)
        for v in row:
            r2[v-1] -= 1
        return r2

    def fill_row(row_len, pos, prev_row, min_val, rem):
        if pos == row_len:
            yield []
            return
        for v in range(min_val, N_labels + 1):
            if rem[v-1] <= 0:
                continue
            # column-strict: v must be > prev_row[pos] (if exists)
            if pos < len(prev_row) and v <= prev_row[pos]:
                continue
            # row weak-increase: v >= min_val (already ensured)
            new_rem = list(rem)
            new_rem[v-1] -= 1
            for rest in fill_row(row_len, pos + 1, prev_row, v, new_rem):
                yield [v] + rest
    yield from go(0, [], content)


def count_by_skipped(l, r):
    """Count SSYT and slice by skipped label in column 1."""
    shape = make_mu_prime(l, r)
    content = [2] * (2*l + 1)
    counts = {}
    total = 0
    for tab in enumerate_ssyt(shape, content):
        col1 = [row[0] for row in tab]
        # which label(s) are NOT in col1?
        skipped = [v for v in range(1, 2*l+2) if v not in col1]
        s = tuple(skipped)  # should be size 1 unless something weird
        counts[s] = counts.get(s, 0) + 1
        total += 1
    return total, counts


def survey():
    print("=== SSYT counts by skipped label ===\n")
    for l in range(2, 7):
        for r in range(l):
            total, counts = count_by_skipped(l, r)
            skip_dist = sorted(counts.items())
            print(f"l={l}, r={r}: total K={total}")
            for s, c in skip_dist:
                print(f"    skipped {s}: count {c}")
            print()


if __name__ == "__main__":
    survey()
