"""
Littlewood-Richardson branching gl_n ⊃ O(n).

Multiplicity formula (Littlewood, King):

    [V_λ^{gl_n} : V_μ^{O(n)}] = Σ_δ c^λ_{δ, μ}

where δ ranges over partitions whose conjugate δ' has all even parts (equivalently,
δ has all even column lengths — "even-column partitions"), and c^λ_{δ, μ} is the
ordinary Littlewood-Richardson coefficient.

LR coefficient c^λ_{μ, ν} = number of skew tableaux T of shape λ/μ with content ν
that are LR tableaux (rows weakly inc, cols strictly inc, reverse reading word is
a lattice/Yamanouchi word).

Implemented in pure Python; tested on classical examples.

Rick — Day 66 CODE — 2026-06-12
"""

from __future__ import annotations

from collections import Counter
from typing import Iterator


def conjugate(p: tuple[int, ...]) -> tuple[int, ...]:
    if not p:
        return ()
    n = p[0]
    return tuple(sum(1 for q in p if q > i) for i in range(n))


def is_even_row_partition(p: tuple[int, ...]) -> bool:
    """δ has all parts even (= all even row lengths)."""
    return all(c % 2 == 0 for c in p)


def even_row_partitions_up_to(N: int, max_rows: int) -> list[tuple[int, ...]]:
    """All partitions δ with |δ| ≤ N, ≤ max_rows rows, all parts even.

    For GL_n ⊃ O(n) Littlewood branching: δ runs over these partitions.
    """
    results: list[tuple[int, ...]] = [()]

    def recurse(prev_part: int, total: int, prefix: list[int]):
        if total > N:
            return
        if prefix:
            results.append(tuple(prefix))
        if len(prefix) == max_rows:
            return
        # Each new part is even, ≤ prev_part, ≤ (N - total).
        for p in range(2, min(prev_part, N - total) + 1, 2):
            recurse(p, total + p, prefix + [p])

    recurse(N, 0, [])
    seen = set()
    out = []
    for d in results:
        if d in seen:
            continue
        seen.add(d)
        out.append(d)
    return out


# ---------------------------------------------------------------------------
# Littlewood-Richardson coefficient via skew SSYT enumeration with Yamanouchi
# ---------------------------------------------------------------------------

def skew_cells(lam: tuple[int, ...], mu: tuple[int, ...]) -> list[tuple[int, int]]:
    """Cells in λ but not in μ (with μ ⊂ λ)."""
    cells = []
    nrows = len(lam)
    mu_padded = list(mu) + [0] * (nrows - len(mu))
    for i in range(nrows):
        for j in range(mu_padded[i], lam[i]):
            cells.append((i, j))
    return cells


def lr_coefficient(lam: tuple[int, ...], mu: tuple[int, ...], nu: tuple[int, ...]) -> int:
    """LR coefficient c^lam_{mu, nu}. Number of LR skew tableaux of shape lam/mu, content nu."""
    if sum(lam) != sum(mu) + sum(nu):
        return 0
    if any(mu[i] > lam[i] if i < len(lam) else mu[i] > 0 for i in range(len(mu))):
        return 0
    if not nu:
        # Need lam == mu
        return 1 if lam == mu else 0  # consider trailing zeros
    cells = skew_cells(lam, mu)
    if not cells:
        return 1 if not nu else 0
    nrows = len(lam)
    ncols = max(lam) if lam else 0
    n_alphabet = len(nu)

    # Track tableau values; enumerate row by row, left to right.
    # Bookkeeping: prev_val[i] = value at (i, j-1); above_val[j] = value at (i-1, j).
    # For Yamanouchi: read reverse reading word (right-to-left in each row, top to bottom)
    # and check that at every prefix, count(i) >= count(i+1) for each i.
    # The reverse reading word is just the reading word reversed; equivalently scan rows
    # top-to-bottom but right-to-left in each row.

    # We'll enumerate cells in reverse reading order: in each row, right to left; rows top to bottom.
    # That way the Yamanouchi (lattice) condition becomes: at every step, the prefix has
    # count(i) ≥ count(i+1) for all i.
    # But we also need the tableau constraints: row weakly increasing L→R, col strictly inc.

    # Implementation:
    # Order cells in reverse reading order: for r = 0,..,nrows-1: cells in row r in DECREASING j.
    # When filling cell (r, j), the cells to the LEFT in same row (smaller j) are NOT YET filled.
    # And the cells ABOVE in same col (smaller r) are ALREADY filled.
    # Row constraint: T[r][j] >= T[r][j-1]; reversed: when we fill (r,j), we haven't filled
    # (r,j-1) yet, so we can only check this when we fill (r,j-1) later. Equivalently:
    # we need T[r][j-1] <= T[r][j], so the right-side cell upper-bounds the next left cell.
    # Easier: fill row by row left to right, then check Yamanouchi at the end.
    # But the row-by-row approach makes Yamanouchi check expensive.

    # Use the standard rev-reading enumeration. Process rows top to bottom, within each row
    # process cells right to left. Maintain row_max[r] = current min value allowed at next
    # left cell (i.e., the last value we placed, since L→R is weakly increasing means R→L is
    # weakly decreasing). Maintain col_used[c] (the value above in col c that was placed in
    # an upper row).

    # Group cells per row (in skew shape) in reverse order:
    row_cells: dict[int, list[int]] = {}
    for (r, c) in cells:
        row_cells.setdefault(r, []).append(c)
    for r in row_cells:
        row_cells[r].sort(reverse=True)  # right to left

    # Above-value per column: pre-populate with values in mu region? But μ is empty content
    # for our purposes — we only fill skew cells. Column strictness: skew tableau must satisfy
    # T[r][c] > T[r-1][c] where (r-1, c) is filled (either in mu = no constraint, or skew = filled).
    # Cells in mu have no entry, so only matters between consecutive skew cells in same column.

    # For row constraints, similar.

    # Implementation:
    row_max_so_far: dict[int, int | None] = {r: None for r in row_cells}  # value placed just-right in this row
    col_above: dict[int, int | None] = {}  # value placed above in same column (in skew region)

    nu_remaining = list(nu)

    # Build the ordered fill sequence: cells in (row asc, col desc) order
    fill_seq = []
    for r in sorted(row_cells.keys()):
        for c in row_cells[r]:
            fill_seq.append((r, c))

    # Yamanouchi-checked content counts (cumulative)
    yam_counts = [0] * n_alphabet
    count = [0]

    def recurse(idx: int) -> int:
        if idx == len(fill_seq):
            return 1
        r, c = fill_seq[idx]
        # Allowed values: 1..n_alphabet
        total = 0
        # Row constraint: T[r][c] <= T[r][c+1] when (r, c+1) exists in skew.
        # We process right-to-left, so the cell to the right was placed already (row_max_so_far[r]).
        # We need T[r][c] <= row_max_so_far[r] (if defined).
        upper_bound_row = row_max_so_far.get(r)
        # Col constraint: T[r][c] > T[r-1][c] (if (r-1, c) is in skew or above).
        lower_bound_col = col_above.get(c, 0) + 1
        # Available values that don't violate Yamanouchi.
        for v in range(lower_bound_col, n_alphabet + 1):
            if upper_bound_row is not None and v > upper_bound_row:
                continue
            # Yamanouchi: after this value, count(v-1) >= count(v) and count(v-2) >= count(v-1) etc up to index 0.
            # Equivalent to: yam_counts[v-1] >= yam_counts[v] + 1? wait
            # The condition: at any prefix in reverse reading word, count of i ≥ count of i+1 for all i.
            # After placing value v, new yam_counts[v-1] += 1. Need yam_counts[v-2] >= yam_counts[v-1] (=new value)
            # for v ≥ 2.
            if v >= 2 and yam_counts[v - 2] < yam_counts[v - 1] + 1:
                continue
            # Also need to not exceed nu_remaining.
            if nu_remaining[v - 1] <= 0:
                continue
            # Place and recurse.
            old_row_max = row_max_so_far[r]
            had_col_above = c in col_above
            old_col_above = col_above.get(c)
            row_max_so_far[r] = v
            col_above[c] = v
            nu_remaining[v - 1] -= 1
            yam_counts[v - 1] += 1
            total += recurse(idx + 1)
            yam_counts[v - 1] -= 1
            nu_remaining[v - 1] += 1
            if had_col_above:
                col_above[c] = old_col_above
            else:
                del col_above[c]
            row_max_so_far[r] = old_row_max
        return total

    return recurse(0)


# ---------------------------------------------------------------------------
# Branching gl_n ⊃ O(n)
# ---------------------------------------------------------------------------

def normalize(p) -> tuple[int, ...]:
    p = tuple(p)
    while p and p[-1] == 0:
        p = p[:-1]
    return p


def gl_to_O_branching(lam: tuple[int, ...], n: int) -> dict[tuple[int, ...], int]:
    """Return dict μ → multiplicity in Res^{gl_n}_{O(n)} V_λ.

    μ ranges over partitions with at most n rows (more precisely, with the constraint
    μ'_1 + μ'_2 ≤ n; but for n = 6 and ≤ 3 rows this is always satisfied).
    """
    lam = normalize(lam)
    nrows_max = n
    even_row_deltas = even_row_partitions_up_to(sum(lam), n)
    # Candidate μ: partitions with |μ| ≤ |λ|, fitting in n rows.
    out: Counter = Counter()
    for delta in even_row_deltas:
        if any(delta[i] > lam[i] if i < len(lam) else delta[i] > 0 for i in range(len(delta))):
            continue
        target_size = sum(lam) - sum(delta)
        # Enumerate all partitions μ with |μ| = target_size and at most n rows and parts ≤ lam[0].
        max_part = lam[0] if lam else 0
        for mu in enumerate_partitions(target_size, n, max_part):
            c = lr_coefficient(lam, delta, mu)
            if c > 0:
                out[mu] += c
    return dict(out)


def enumerate_partitions(N: int, max_rows: int, max_part: int) -> Iterator[tuple[int, ...]]:
    """All partitions of N with at most max_rows rows and parts ≤ max_part."""
    def recurse(rem: int, prev: int, cur: list[int]):
        if rem == 0:
            yield tuple(cur)
            return
        if len(cur) == max_rows:
            return
        for v in range(min(prev, rem), 0, -1):
            yield from recurse(rem - v, v, cur + [v])
    if N == 0:
        yield ()
        return
    yield from recurse(N, min(N, max_part), [])


# ---------------------------------------------------------------------------
# Sanity tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # LR sanity: c^{(2,1)}_{(1), (1,1)} should be 1.
    # And c^{(2,2)}_{(1,1), (1,1)} = 1.
    print("LR sanity checks:")
    print(f"  c^(2,1)_(1, 11) = {lr_coefficient((2,1), (1,), (1,1))}  (expect 1)")
    print(f"  c^(2,2)_(11, 11) = {lr_coefficient((2,2), (1,1), (1,1))}  (expect 1)")
    print(f"  c^(2,2)_(1, 11) = {lr_coefficient((2,2), (1,), (2,1))}  (expect 0 ... actually let me think)")
    # c^(2,2)_(1, (2,1)): skew shape (2,2)/(1) has 3 cells: (1,2), (2,1), (2,2). Need content (2,1).
    # Filling: must have 2 ones and 1 two. (1,2)=?, (2,1)=?, (2,2)=?
    # Row: (1,2) only cell in row 1, so any value (1 or 2 allowed).
    # If T[1][2] = 1: then T[2][1] < T[1][2]? No, column strictness: T[2][2] > T[1][2]=1 so T[2][2] ≥ 2.
    # Row 2: T[2][1] ≤ T[2][2]. So T[2][1] ≤ T[2][2].
    # Content (2,1) = two 1s, one 2.
    # Case T[1][2]=1, then need one more 1 and one 2 in row 2. So {T[2][1], T[2][2]} = {1, 2} with 1 ≤ 2. So T[2][1]=1, T[2][2]=2. Reading word right-to-left, top-to-bottom: 1, 2, 1. Reverse: 1, 2, 1. Check lattice: positions: 1 → counts (1,0) OK; 12 → counts (1,1) OK; 121 → counts (2,1) OK. Yes LR.
    # Case T[1][2]=2: then T[2][2] > 2, but max is 2 since content is (2,1). Invalid.
    # So one LR tableau, c = 1.
    print(f"  c^(2,2)_(1, (2,1)) = {lr_coefficient((2,2), (1,), (2,1))}  (expect 1)")
    print()

    # gl_6 ⊃ O(6) for λ = (1,1): expect V_λ → adj(O(6)) = V_{(1,1)}^{O(6)} only, mult 1.
    print("Branching tests gl_6 ⊃ O(6):")
    branch = gl_to_O_branching((1, 1), 6)
    print(f"  λ=(1,1): {branch}  (expect {{(1,1): 1}})")
    # λ = (2): symmetric square = V_(2) + V_(0) (trace), so should branch to V_(2)^O(6) + V_()^O(6).
    branch = gl_to_O_branching((2,), 6)
    print(f"  λ=(2): {branch}  (expect {{(2,): 1, (): 1}})")
    # λ = (1): vector rep, branches to V_(1)^O(6) only.
    branch = gl_to_O_branching((1,), 6)
    print(f"  λ=(1): {branch}  (expect {{(1,): 1}})")
    # λ = (2,1): branches?
    # gl_6 (2,1) has dim 70. O(6) decomposition: V_(2,1)^O(6) + V_(1)^O(6).
    # V_(2,1)^O(6) has dim 64 (= so_6 (2,1,0)); V_(1)^O(6) has dim 6. 64+6 = 70. ✓
    branch = gl_to_O_branching((2, 1), 6)
    print(f"  λ=(2,1): {branch}  (expect {{(2,1): 1, (1,): 1}})")
