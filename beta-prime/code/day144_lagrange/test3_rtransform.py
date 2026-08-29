"""
TEST 3: R-transform / free cumulant exploration.
M(τ) = 1 - 2F(τ). Then M(0) = 1, and M² = 1 + 4A.

In free probability, if μ has moments m_n = ∫ x^n dμ, the moment generating series
M_μ(z) = 1 + sum_{n>=1} m_n z^n satisfies M_μ(z) = 1 + z R(z M_μ(z)) where R(z) = sum κ_n z^n
is the R-transform (sum of free cumulants).

Alternatively the Cauchy transform G_μ(z) = 1/z + sum m_n/z^{n+1}, and R(z) = G^{-1}(z) - 1/z.

Here M(τ) = 1 + m_1 τ + m_2 τ² + ... with m_k = -2 b_k. Let's use free-cumulant recovery:
m_1 = κ_1
m_2 = κ_2 + κ_1²
m_3 = κ_3 + 3κ_1 κ_2 + κ_1³
m_n = sum over non-crossing partitions of {1..n} of product of κ_{block size}.

Compute κ_1..κ_7 from m_1..m_7.
"""
from sympy import Rational, symbols, Poly, expand, series, Symbol
from itertools import combinations

# Non-crossing partitions of {1..n}
def noncrossing_partitions(n):
    """Yield all non-crossing partitions of {0..n-1}."""
    if n == 0:
        yield []
        return
    # DP: for each n, non-crossing partitions can be built by choosing block containing 1
    # A non-crossing partition of [n] can be recursively described.
    # We generate all partitions and filter for non-crossing.
    # Easier: enumerate all set partitions then check non-crossing.
    def set_partitions(items):
        if len(items) == 0:
            yield []
            return
        if len(items) == 1:
            yield [items]
            return
        first = items[0]
        for rest_partition in set_partitions(items[1:]):
            # add first as own block
            yield [[first]] + rest_partition
            # add first to each existing block
            for i in range(len(rest_partition)):
                new_part = [list(b) for b in rest_partition]
                new_part[i] = [first] + new_part[i]
                yield new_part
    def is_noncrossing(part):
        # Sort each block
        blocks = [sorted(b) for b in part]
        # For every pair of blocks, check no crossing
        for i in range(len(blocks)):
            for j in range(i+1, len(blocks)):
                B1, B2 = blocks[i], blocks[j]
                # crossing if there exist a<b<c<d with a,c in B1, b,d in B2 (or swap)
                for a in B1:
                    for c in B1:
                        if a >= c: continue
                        for b in B2:
                            for d in B2:
                                if b >= d: continue
                                if a < b < c < d:
                                    return False
                                if b < a < d < c:
                                    return False
        return True
    for part in set_partitions(list(range(n))):
        if is_noncrossing(part):
            yield part

# moments
b_vals = [3, 27, 417, 7851, 164124, 3661389, 85384566]
m = [None] + [Rational(-2 * b) for b in b_vals]  # m[0] unused, m[k] for k=1..7
# m_k = -2 b_k

# Free cumulants κ_1..κ_7
kappa = [None] * 8  # kappa[1..7]

for n in range(1, 8):
    # m_n = sum over noncrossing partitions of [n] of prod kappa_{block size}
    # Isolate kappa_n (partition = one big block)
    s = Rational(0)
    for part in noncrossing_partitions(n):
        if len(part) == 1:
            continue  # this is the kappa_n term
        prod = Rational(1)
        for block in part:
            prod *= kappa[len(block)]
        s += prod
    kappa[n] = m[n] - s
    print(f"m_{n} = {m[n]}, κ_{n} = {kappa[n]}")

# Also test: maybe kappa_n has nicer pattern than m_n
# If κ_n = 0 for n >= some N, μ is a free convolution power.
print("\nFree cumulants κ_1..κ_7:")
for n in range(1, 8):
    print(f"  κ_{n} = {kappa[n]}")

# Try: maybe κ_n = -2 c_{n-1} · something?
# Compare with c_i = 3, 9, 58/3, ...
