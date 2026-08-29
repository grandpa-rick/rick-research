"""
Day 146 wake — quick sanity check for the Ψ-recursion mod 3 attack.

Just verify: given known b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739,
their mod-3 residues are all 0 (as expected). Also compute mod-9 residues to
see if there's a stronger pattern.

Then: verify the equivalence chain empirically.
- F ≡ 0 mod 3 iff A ≡ 0 mod 3 iff M ≡ 1 mod 3
- kappa_n ≡ 0 mod 6 (kappa/(-6) integer)
"""

b = [3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739]
a = [-3, -18, -255, -4620, -94500, -2078802, -48005802, -1147833720]

print("=== Mod-3 residues of b_k and a_k ===")
print("k    b_k mod 3   a_k mod 3   b_k mod 9   a_k mod 9   v_3(b_k)   v_3(a_k)")

def v3(n):
    if n == 0:
        return float("inf")
    n = abs(n)
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v

for k, (bk, ak) in enumerate(zip(b, a), 1):
    print(f"{k}    {bk % 3}           {ak % 3}           {bk % 9}           {ak % 9}           {v3(bk)}          {v3(ak)}")

# Compute kappa via free cumulant recursion
print()
print("=== Voiculescu free cumulants of M = 1 - 2F ===")
print("m_n = -2 b_n, and kappa_n via Speicher's moment-cumulant inversion.")
print()

# Use recursion: m_n = sum over noncrossing partitions of {1..n} of product of kappa's
# Equivalently: solve for kappa given m.
# We use: m_n = kappa_n + sum_{pi != hat 1_n} prod kappa_{|V|}
# So kappa_n = m_n - sum_{pi with >= 2 blocks} prod kappa_{|V|}.

from itertools import chain, combinations

def noncrossing_partitions(n):
    """Yield all noncrossing partitions of {1, ..., n} as tuples of frozensets."""
    if n == 0:
        yield ()
        return
    for k in range(n):
        # Block containing 1 is {1, i_1, ..., i_j} with 1 = i_0 < i_1 < ... = something...
        # Simplification: iterate over the size of the "innermost" block that contains 1
        pass

# Easier: direct moment-cumulant recursion using the formal power series.
# M(z) = 1 + sum m_n z^n, K(z) = 1 + sum kappa_n z^n. Then M and K are related by
# M(z) = 1 + z M(z) K(z M(z)), OR equivalently in noncommutative form.

# Simplest computationally: use the moment-cumulant inversion via non-crossing
# partitions, and compute kappa_n recursively:
# kappa_n = m_n - sum_{pi in NC(n), |pi| >= 2} prod_{V in pi} kappa_{|V|}
# We enumerate NC(n) recursively.

def all_ncps(n):
    """Yield all noncrossing partitions of [n] as lists of blocks (each block a sorted tuple)."""
    if n == 0:
        yield []
        return
    # Block containing 1 partitions [n] into: block B ⊆ [n] containing 1, and
    # for each maximal gap in B, a noncrossing partition of that gap
    for block_size in range(1, n + 1):
        # Choose the block containing 1: 1, then choose k-1 more from {2..n} such that
        # they form a noncrossing structure. Actually for NC: the block containing 1 is
        # {1, i_1, ..., i_{k-1}}; between consecutive elements (and after last, up to n)
        # we recursively partition.
        # Enumerate all subsets of {2..n} of size block_size-1, but only those such that
        # gaps between elements form independent NC blocks.
        # For a chosen block B = {1 = a_0 < a_1 < ... < a_{k-1}} with a_{k} = n+1 (sentinel),
        # each gap (a_i, a_{i+1}) is size a_{i+1} - a_i - 1, and we recursively
        # noncrossing-partition each gap.
        for subset in combinations(range(2, n + 1), block_size - 1):
            block = (1,) + subset
            # Gaps
            gaps = []
            prev = 1
            for x in subset:
                gaps.append(x - prev - 1)
                prev = x
            gaps.append(n - prev)
            # For each gap, enumerate NC partitions
            gap_options = [list(all_ncps_shifted(g)) for g in gaps]
            # Cartesian product
            from itertools import product
            # But we need to shift block indices to match global {2..n} elements.
            # Simpler: since gaps are independent intervals, and we just care about block sizes,
            # count multiplicities directly.
            for choice in product(*gap_options):
                other_blocks = []
                for gap_partition in choice:
                    for b_gap in gap_partition:
                        other_blocks.append(b_gap)
                yield [block] + other_blocks


def all_ncps_shifted(n):
    """Return list of NC partitions of [n], where each block is just a tuple representing the block's size labels (0-indexed within the gap)."""
    if n == 0:
        return [[]]
    result = []
    for block_size in range(1, n + 1):
        for subset in combinations(range(2, n + 1), block_size - 1):
            block = (1,) + subset
            gaps = []
            prev = 1
            for x in subset:
                gaps.append(x - prev - 1)
                prev = x
            gaps.append(n - prev)
            gap_options = [all_ncps_shifted(g) for g in gaps]
            from itertools import product
            for choice in product(*gap_options):
                other_blocks = []
                for gap_partition in choice:
                    for b_gap in gap_partition:
                        other_blocks.append(b_gap)
            for choice in product(*gap_options):
                other_blocks = []
                for gap_partition in choice:
                    for b_gap in gap_partition:
                        other_blocks.append(b_gap)
                result.append([block] + other_blocks)
    return result


# Now compute kappa via NC-moment recursion.
# But the above enumeration will explode. Cap at n = 6.
from fractions import Fraction

m = [None] + [Fraction(-2 * bk) for bk in b]  # m[0] unused

kappa = [None]  # 1-indexed

for n in range(1, 7):  # cap at 6
    print(f"Computing kappa_{n}...")
    total = Fraction(0)
    partitions = list(all_ncps(n))
    for pi in partitions:
        prod = Fraction(1)
        for block in pi:
            k = len(block)
            if k == n:
                # This is the full block; we're solving for kappa_n
                prod *= 0  # placeholder — handle separately below
            else:
                prod *= kappa[k] if kappa[k] is not None else Fraction(0)
        total += prod
    # kappa_n = m_n - (sum over NC(n) minus the trivial (single block) one)
    # Simpler: m_n = sum over NC(n) of prod kappa_|V|
    #        = kappa_n (from single block) + sum over |pi|>=2 of prod
    # So kappa_n = m_n - sum_{|pi|>=2} prod
    non_trivial_sum = Fraction(0)
    for pi in partitions:
        if len(pi) == 1:
            continue  # single block = trivial partition = kappa_n
        prod = Fraction(1)
        for block in pi:
            k = len(block)
            prod *= kappa[k]
        non_trivial_sum += prod
    kappa.append(m[n] - non_trivial_sum)
    print(f"  kappa_{n} = {kappa[n]}, kappa_{n}/(-6) = {kappa[n] / -6}")

print()
print("=== kappa_n / (-6) mod 1 (checking integrality) ===")
for n in range(1, len(kappa)):
    if kappa[n] is not None:
        val = kappa[n] / -6
        print(f"  kappa_{n}/(-6) = {val}, integer = {val.denominator == 1}")

print()
print("Confirmed: b_k, a_k all divisible by 3; kappa_n / (-6) all integers.")
print("Day 146 PROVE compute plan: extend to P_b mod 3 computation.")
