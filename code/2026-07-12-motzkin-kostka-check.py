#!/usr/bin/env python3
"""
OQ-MOTZKIN-K-TRIANGLE verification.

Goal:
  Compute the Motzkin-triangle coefficient
      m^(2)_{k,j} = beta_{j,k}
                  = sum_{t >= 0, k+2t <= j} C(j, k+2t) * C(k+2t, t) / (k+t+1)
  (He-Tubbenhauer arXiv:2508.04054), and search for a partition mu = mu(k, j)
  such that K_{mu^T, (2^j)} = m^(2)_{k, j}.

  In particular check the two-row family mu = (k+j)/2 + something, or the
  candidate mu = (j + k)/2 rows-of-2 style shapes coming from e_2^j.

  Report the triangle and whether the OQ is confirmed / falsified / inconclusive.
"""

from math import comb
from fractions import Fraction
from itertools import product


# ---------- Motzkin triangle ----------

def motzkin_beta_formula(k, j):
    """He-Tubbenhauer-style closed formula (may be non-integer for single k).
       Kept for reference; NOT used in the main table."""
    if k < 0 or k > j:
        return 0
    if (j - k) % 2 == 1:
        return 0
    total = Fraction(0)
    t = 0
    while k + 2 * t <= j:
        term = Fraction(comb(j, k + 2 * t) * comb(k + 2 * t, t), k + t + 1)
        total += term
        t += 1
    return total


# Standard Motzkin triangle by recurrence: m(n,k) = number of Motzkin paths
# of length n ending at height k. m(0,0)=1.
# Recurrence:  m(n,k) = m(n-1, k-1) + m(n-1, k) + m(n-1, k+1)
_motzkin_cache = {}
def motzkin_tri(k, j):
    """Standard Motzkin triangle m(j, k)."""
    if k < 0 or k > j:
        return 0
    if j == 0:
        return 1 if k == 0 else 0
    if (k, j) in _motzkin_cache:
        return _motzkin_cache[(k, j)]
    v = motzkin_tri(k - 1, j - 1) + motzkin_tri(k, j - 1) + motzkin_tri(k + 1, j - 1)
    _motzkin_cache[(k, j)] = v
    return v


# The multiplicity of V_k in (V_1)^{otimes j} is the Motzkin-triangle entry.
# The multiplicity of V_k in (V_1 + V_2)^{otimes j} is what the OQ asks about.
# But the "standard" m^(2)_{k,j} in He-Tubbenhauer for the Motzkin algebra
# (dimension = Motzkin number) is the height-k Motzkin path count.
# Use this; also print the formula version for comparison.

def motzkin_beta(k, j):
    return motzkin_tri(k, j)


# ---------- Partitions ----------

def partitions_of(n, max_part=None):
    """All partitions of n (as tuples, weakly decreasing)."""
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions_of(n - first, first):
            yield (first,) + rest


def conjugate(lam):
    """Transpose partition."""
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p >= i) for i in range(1, lam[0] + 1))


# ---------- Kostka numbers via SSYT enumeration ----------

def kostka(shape, content):
    """
    K_{shape, content} = number of SSYT of the given shape with the given content.
    shape: partition (tuple).
    content: tuple giving how many of each letter 1, 2, ..., ell.
    """
    if sum(shape) != sum(content):
        return 0
    if not shape:
        return 1 if all(c == 0 for c in content) else 0

    # Fill cells in reading order (row by row, left to right).
    rows = len(shape)
    cells = [(r, c) for r in range(rows) for c in range(shape[r])]
    n = len(cells)
    letters = len(content)

    # DP with memoization on (position, remaining content, current row values).
    # We track the tableau's last placed entry per column and per row.

    T = [[0] * shape[r] for r in range(rows)]

    count = 0

    def fill(idx, remaining):
        nonlocal count
        if idx == n:
            count += 1
            return
        r, c = cells[idx]
        # Row: must be >= entry to the left (weakly increasing) => T[r][c-1]
        # Column: must be > entry above (strictly increasing) => T[r-1][c]
        lo_row = T[r][c - 1] if c > 0 else 1
        lo_col = T[r - 1][c] + 1 if r > 0 else 1
        lo = max(lo_row, lo_col)
        for v in range(lo, letters + 1):
            if remaining[v - 1] == 0:
                continue
            T[r][c] = v
            remaining[v - 1] -= 1
            fill(idx + 1, remaining)
            remaining[v - 1] += 1
            T[r][c] = 0

    fill(0, list(content))
    return count


# ---------- Sanity checks ----------

assert kostka((3,), (1, 1, 1)) == 1
assert kostka((2, 1), (1, 1, 1)) == 2
assert kostka((1, 1, 1), (1, 1, 1)) == 1
assert kostka((2, 2), (2, 2)) == 1
assert kostka((2, 2), (2, 1, 1)) == 1


# ---------- Motzkin triangle for j = 0..6 ----------

MAXJ = 6

print("=" * 72)
print("Motzkin triangle m^(2)_{k,j} = beta_{j,k} for j = 0..6")
print("(standard Motzkin-triangle recurrence: m(j,k) = m(j-1,k-1)+m(j-1,k)+m(j-1,k+1))")
print("=" * 72)
print("\nFor cross-check, He-Tubbenhauer closed formula values (as Fractions):")
for j in range(MAXJ + 1):
    row = [str(motzkin_beta_formula(k, j)) for k in range(j + 1)]
    print(f"  j={j}: {row}")
print()
print(f"{'':>4}", end="")
for k in range(MAXJ + 1):
    print(f"k={k:>2}", end="  ")
print()
motzkin = {}
for j in range(MAXJ + 1):
    print(f"j={j:>2} ", end="")
    for k in range(MAXJ + 1):
        v = motzkin_beta(k, j)
        motzkin[(k, j)] = v
        print(f"{v:>4}", end="  ")
    print()

# Diagonal sums (should be Motzkin numbers 1,1,2,4,9,21,51):
print("\nColumn sums (sum_k beta_{j,k}) -- should be Motzkin numbers M_j:")
for j in range(MAXJ + 1):
    s = sum(motzkin[(k, j)] for k in range(j + 1))
    print(f"  j={j}: {s}")


# ---------- Kostka search ----------

print("\n" + "=" * 72)
print("Kostka search: for each (k, j) with beta_{j,k} > 0, find mu |- 2j")
print("with K_{mu^T, (2^j)} = beta_{j,k}. Also test specific candidate mu(k,j).")
print("=" * 72)

# Precompute K_{mu^T, (2^j)} for all mu |- 2j, all j = 0..MAXJ.
kostka_table = {}   # (j, mu) -> K_{mu^T, (2^j)}
for j in range(MAXJ + 1):
    content = tuple([2] * j)   # (2^j)
    for mu in partitions_of(2 * j):
        muT = conjugate(mu)
        # K needs SSYT of shape muT with content 2^j.
        # Content length = j; entries range 1..j.
        if j == 0:
            k = 1 if not muT else 0
        else:
            k = kostka(muT, content)
        kostka_table[(j, mu)] = k

# For each (k, j) with beta > 0, list all mu |- 2j with K_{mu^T,(2^j)} = beta.
print("\nAll matches mu |- 2j with K_{mu^T, (2^j)} = beta_{j,k}:")
print("-" * 72)
matches = {}    # (k, j) -> list of mu
for j in range(MAXJ + 1):
    for k in range(j + 1):
        b = motzkin[(k, j)]
        if b == 0:
            continue
        mus = [mu for mu in partitions_of(2 * j) if kostka_table[(j, mu)] == b]
        matches[(k, j)] = mus
        print(f"  (k={k}, j={j}): beta={b}, matching mu = {mus}")


# ---------- Test candidate two-row family ----------

print("\n" + "=" * 72)
print("Candidate 1: mu = (j+k, j-k) two-row shape (|mu| = 2j).")
print("=" * 72)
print(f"{'(k,j)':>8}  {'beta':>6}  {'mu':>16}  {'muT':>16}  {'K_{muT,(2^j)}':>14}  match?")
all_match_1 = True
for j in range(MAXJ + 1):
    for k in range(j + 1):
        b = motzkin[(k, j)]
        if b == 0:
            continue
        # candidate: two-row shape (j+k, j-k) if k <= j (both parts >= 0)
        if j + k >= j - k >= 0:
            mu = tuple(x for x in (j + k, j - k) if x > 0)
            muT = conjugate(mu)
            K = kostka(muT, tuple([2] * j)) if j > 0 else (1 if not muT else 0)
            ok = (K == b)
            all_match_1 = all_match_1 and ok
            print(f"  ({k},{j})  {b:>6}  {str(mu):>16}  {str(muT):>16}  {K:>14}  {'YES' if ok else 'NO'}")

print(f"\nCandidate 1 (mu = (j+k, j-k)) all match?  {all_match_1}")


print("\n" + "=" * 72)
print("Candidate 2: mu = (k+j)/... trying mu = (j+k) alone if j-k=0, etc.")
print("Also try mu = (2, 2, ..., 2) with j parts (2^j itself)")
print("and mu with muT = (j+k, j-k).")
print("=" * 72)
# Candidate 3: muT = (j+k, j-k), so mu = conjugate of that.
print(f"{'(k,j)':>8}  {'beta':>6}  {'muT':>16}  {'mu':>16}  {'K_{muT,(2^j)}':>14}  match?")
all_match_3 = True
for j in range(MAXJ + 1):
    for k in range(j + 1):
        b = motzkin[(k, j)]
        if b == 0:
            continue
        muT = tuple(x for x in (j + k, j - k) if x > 0)
        mu = conjugate(muT)
        K = kostka(muT, tuple([2] * j)) if j > 0 else (1 if not muT else 0)
        ok = (K == b)
        all_match_3 = all_match_3 and ok
        print(f"  ({k},{j})  {b:>6}  {str(muT):>16}  {str(mu):>16}  {K:>14}  {'YES' if ok else 'NO'}")

print(f"\nCandidate 3 (muT = (j+k, j-k)) all match?  {all_match_3}")


# ---------- Summary of "clean rule" search ----------

print("\n" + "=" * 72)
print("Verdict: does any single-formula family mu(k, j) match all (k, j)?")
print("=" * 72)

# For each (k, j), the set of mu with matching K.  We ask: is there a rule
# mu(k, j) landing in matches[(k, j)] for all (k, j)?
# Try the two candidates above, plus "mu = (k+1) rows of 2" style.

candidates = {
    "(j+k, j-k)": lambda k, j: tuple(x for x in (j + k, j - k) if x > 0),
    "conj(j+k, j-k)": lambda k, j: conjugate(tuple(x for x in (j + k, j - k) if x > 0)),
    "(2^((j+k)/2), 1^(j-k))": None,  # placeholder, computed below
}


def two_col_shape(k, j):
    """Shape = (j+k)/2 twos on top, then (j-k) ones (only valid if j+k even)."""
    if (j + k) % 2 != 0:
        return None
    a = (j + k) // 2      # rows of length 2
    b = (j - k)           # rows of length 1
    parts = [2] * a + [1] * b
    return tuple(parts)


def rule_check(name, fn):
    ok = True
    misses = []
    for j in range(MAXJ + 1):
        for k in range(j + 1):
            b = motzkin[(k, j)]
            if b == 0:
                continue
            mu = fn(k, j)
            if mu is None:
                ok = False
                misses.append(((k, j), None, None))
                continue
            muT = conjugate(mu)
            K = kostka(muT, tuple([2] * j)) if j > 0 else (1 if not muT else 0)
            if K != b:
                ok = False
                misses.append(((k, j), mu, (K, b)))
    print(f"\nRule '{name}':  {'ALL MATCH' if ok else f'FAILS on {len(misses)} cells'}")
    for m in misses[:8]:
        print(f"    miss: (k,j)={m[0]}, mu={m[1]}, (K, beta)={m[2]}")
    return ok


rule_check("mu = (j+k, j-k)", lambda k, j: tuple(x for x in (j + k, j - k) if x > 0))
rule_check("mu = conj(j+k, j-k)", lambda k, j: conjugate(tuple(x for x in (j + k, j - k) if x > 0)))
rule_check("mu = 2^((j+k)/2) 1^(j-k)", two_col_shape)
# When (j+k) is odd there is no candidate; but note beta = 0 unless (j-k) even,
# equivalently (j+k) even, so this rule is well-defined exactly on the support.

# Also: mu = (j+k, j-k) reversed? no, partitions weakly decreasing.
# Try mu = ((j+k)/2 + 1, (j-k)/2)?
def two_row_half(k, j):
    if (j - k) % 2 != 0:
        return None
    a = (j + k) // 2
    b = (j - k) // 2
    parts = tuple(x for x in (a, b) if x > 0)
    return parts

rule_check("mu = ((j+k)/2, (j-k)/2)", two_row_half)


# ---------- Also: identify the mu-family from matches ----------

# ---------- Broader search: |mu| = anything from 0 to 2j ----------
print("\n" + "=" * 72)
print("Broader search: |mu| free, but SSYT weight (2^j) requires |mu| = 2j.")
print("So try weight (1^j) or (2^j) with |mu| = 2j only.")
print("Also test the plethystic-consistent |mu| = 2j family with muT interp.")
print("=" * 72)

# The Kostka K_{lambda, mu} requires |lambda| = |mu|. Since content = (2^j)
# has sum 2j, the shape must have |shape| = 2j. So the only place to search
# is partitions of 2j. That's what we did. Extended search below: check whether
# a family of the form mu = ((2^a, 1^b) with 2a + b = 2j) hits everything.
extra_families = {
    "mu = (2^((j+k)/2), 1^(j-k))": lambda k, j: (
        None if (j + k) % 2 else
        tuple([2] * ((j + k) // 2) + [1] * (j - k))
    ),
    "mu = (2^((j-k)/2), 1^(j+k))": lambda k, j: (
        None if (j - k) % 2 else
        tuple([2] * ((j - k) // 2) + [1] * (j + k))
    ),
    # A plausible candidate from the sl_2 / two-row structure:
    "mu = (j+k, 1^(j-k))": lambda k, j: (
        tuple([j + k] + [1] * (j - k)) if j + k > 0 else ()
    ),
    "mu = (j-k+2, 2^((j+k-2)/2))?": None,
}

for name, fn in list(extra_families.items()):
    if fn is None:
        continue
    ok = True
    misses = 0
    for j in range(MAXJ + 1):
        for k in range(j + 1):
            b = motzkin[(k, j)]
            if b == 0:
                continue
            mu = fn(k, j)
            if mu is None or sum(mu) != 2 * j:
                ok = False
                misses += 1
                continue
            muT = conjugate(mu)
            K = kostka(muT, tuple([2] * j)) if j > 0 else (1 if not muT else 0)
            if K != b:
                ok = False
                misses += 1
    print(f"  Rule '{name}': {'ALL MATCH' if ok else f'FAILS ({misses} misses)'}")


# ---------- Try relaxing: allow non-partition mu, allow |mu| = j ----------
print("\n" + "=" * 72)
print("Alt hypothesis: maybe the intended identity is K_{mu, (1^k, 2^((j-k)/2))}")
print("i.e., a different content coming from V_1 vs V_2 legs.")
print("=" * 72)

# In (V_1 + V_2)^{tensor j}, an element uses `a` copies of V_1 and `b`=j-a of V_2.
# So a natural weight is (1^a 2^b) with a+b=j.  The Motzkin coefficient m^(2)_{k,j}
# is the multiplicity of V_k in this tensor product, summed over (a,b) with a+b=j.
# Content (1^a, 2^b) has size a + 2b.
# For the "top" contribution (all V_2) we get (2^j) content, size 2j.
# For the "bottom" (all V_1) we get (1^j) content, size j.

# So maybe:  m^(2)_{k,j} = K_{lambda, (2^b, 1^a)} where lambda encodes k
# and (a,b) ranges. Try lambda = (k+1)*something.

# For each (k, j), search over shapes lambda with |lambda| = something small
# and content = (2^b, 1^a) with a + 2b = |lambda|.
print("Searching: for each (k,j) with beta>0, find (lambda, a, b) with")
print("  a + b = j (interpretation)?  No -- weight-sum determines |lambda|.")
print("Try: shapes lambda of size N in {j, j+1, ..., 2j}, content (2^b, 1^(N-2b)).")

# For each (k,j), find all (lambda, b) with lambda |- N and K_{lambda, (2^b,1^(N-2b))} = beta.
# But this explodes. Restrict to lambda = (k+1, 1^?) or (a, b) two-row.

def try_two_row_generic(k, j):
    b = motzkin[(k, j)]
    hits = []
    # Two-row shape (p, q) with p >= q >= 0
    for N in range(k, 2 * j + 1):
        for p in range(N + 1):
            q = N - p
            if q > p or q < 0:
                continue
            shape = tuple(x for x in (p, q) if x > 0)
            # Try contents (2^b2, 1^(N - 2*b2))
            for b2 in range(N // 2 + 1):
                a = N - 2 * b2
                if a < 0:
                    continue
                content = tuple([2] * b2 + [1] * a)
                if not content:
                    continue
                K = kostka(shape, content)
                if K == b:
                    hits.append((shape, content, K))
    return hits

# Only check j <= 3 for time.
print("\nTwo-row generic hits (shape, content, K) equal to beta_{j,k}, j<=3:")
for j in range(4):
    for k in range(j + 1):
        b = motzkin[(k, j)]
        if b == 0:
            continue
        hits = try_two_row_generic(k, j)
        # Filter to interesting: shape rooted in k somehow
        print(f"  (k={k}, j={j}), beta={b}: {len(hits)} two-row (shape, content) hits")
        for h in hits[:6]:
            print(f"      {h}")


# ---------- Original intersection print ----------
print("\n" + "=" * 72)
print("Intersection: for each (k,j), which mu have K_{muT,(2^j)}=beta_{j,k}?")
print("Look for a pattern.")
print("=" * 72)
for (k, j), mus in sorted(matches.items()):
    print(f"  (k={k}, j={j}): beta={motzkin[(k,j)]}, mu candidates: {mus}")
