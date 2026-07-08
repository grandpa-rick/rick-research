"""Test whether M_j equals sum of f^{lam/mu} over specific inner shapes mu.

Key finding round 3: M_1(a,b,5) = f^{(a,b,5)/(1,1,0)} exactly.

Hypothesis for j = 2: M_2 = f^{lam/(2,2,0)} + f^{lam/(2,1,1)}, based on
  M_2(6,5,5) = 6336 = 3762 + 2574 = f^{(6,5,5)/(2,2,0)} + f^{(6,5,5)/(2,1,1)}.
"""
from math import factorial
from fractions import Fraction


def C(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def H5(a, b, j):
    h0 = (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5)
    h1 = -20*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4)
    h2 = -10*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 22)
    h3 = 360*(a+3)*(b+2)*(a*b + a + 2*b - 2)
    h4 = 240*(a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a + 2*b*b - 34*b - 24)
    h5 = -7200*(a*b + b - 2)
    h6 = -7200*(a*b - a - 6)
    h7 = 100800
    h8 = 201600
    hs = [h0, h1, h2, h3, h4, h5, h6, h7, h8]
    return sum(hs[k] * C(j, k) for k in range(9))


def M_j(a, b, j, c=5):
    assert c == 5
    m = (a + b + c) // 2
    N = 2 * (m - j)
    Q5 = (a - 3) * (b - 4) * H5(a, b, j) - factorial(10) * C(j, 10)
    den = 120 * (a + 6 - j)
    for i in range(1, 6):
        den *= (b + i - j)
    num = C(N, b - j) * (a - b + 1) * Q5
    if den == 0: return None
    if num % den != 0: return None
    return num // den


def inv_fact(n):
    if n < 0: return Fraction(0)
    return Fraction(1, factorial(n))


def f_skew(lam, mu):
    r = len(lam)
    mu = list(mu) + [0] * (r - len(mu))
    for i in range(r):
        if lam[i] < mu[i]:
            return 0
    # Check mu is a partition (weakly decreasing).
    for i in range(r - 1):
        if mu[i] < mu[i+1]:
            return 0
    n = sum(lam) - sum(mu)
    if n < 0: return 0
    mat = [[inv_fact(lam[i] - mu[j] - i + j) for j in range(r)] for i in range(r)]
    a = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
    b = mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
    c = mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
    d = a - b + c
    res = factorial(n) * d
    if res.denominator != 1:
        return None
    return res.numerator


def gen_partitions_at_most(n, k):
    """All partitions of n with at most k parts."""
    if n == 0:
        yield ()
        return
    if k == 0: return
    for first in range(n, 0, -1):
        for rest in gen_partitions_le(n - first, first, k - 1):
            yield (first,) + rest


def gen_partitions_le(n, max_val, max_parts):
    if n == 0:
        yield ()
        return
    if max_parts == 0: return
    for first in range(min(n, max_val), 0, -1):
        for rest in gen_partitions_le(n - first, first, max_parts - 1):
            yield (first,) + rest


# --------------------------------------------------------------------
# Test: M_j = sum over partitions mu of 2j (with ≤ 3 parts) of f^{lam/mu}.
# --------------------------------------------------------------------
c = 5
print("Test: M_j vs sum_mu f^{lam/mu} for mu ⊢ 2j with ≤ 3 parts.")
print(f"{'shape':>8s} {'j':>3s} | {'M_j':>15s} | {'sum':>15s} | match | mu contributions")
print("-" * 90)
for (a, b) in [(6, 5), (7, 6), (8, 5), (8, 7), (10, 5), (11, 8), (13, 10)]:
    if (a + b + 5) % 2 != 0: continue
    for j in range(0, 6):
        m = M_j(a, b, j)
        if m is None: continue
        # Sum over all partitions of 2j.
        total = 0
        contribs = []
        for mu in list(gen_partitions_at_most(2 * j, 3)):
            fs = f_skew([a, b, 5], mu)
            if fs and fs > 0:
                total += fs
                contribs.append((mu, fs))
        if 2 * j == 0:
            total = M_j(a, b, 0)  # single empty term
            contribs = [((), total)]
        match = "yes" if m == total else "NO"
        print(f"({a},{b}) {j:>3d} | {m:>15d} | {total:>15d} | {match:>5s} | {contribs[:3]}")
