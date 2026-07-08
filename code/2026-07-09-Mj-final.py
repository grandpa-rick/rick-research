"""FINAL VERIFICATION: M_j(a, b, c) = sum_mu [s_mu : e_2^j] * f^{lam/mu}
where the sum is over partitions mu ⊢ 2j with ≤ 3 rows, and
[s_mu : e_2^j] = K_{mu^T, (2^j)} = coefficient of s_mu in e_2^j.

Test:
  1) Compute [s_mu : e_2^j] via Pieri iteration for j = 1..6.
  2) Check M_j(a, b, 5) = sum over mu with ≤ 3 rows of coef * f^{(a,b,5)/mu}.
"""
from math import factorial
from fractions import Fraction
from collections import defaultdict


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


def M_j(a, b, j):
    m = (a + b + 5) // 2
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
    for i in range(r - 1):
        if mu[i] < mu[i+1]:
            return 0
    n = sum(lam) - sum(mu)
    if n < 0: return 0
    if n == 0: return 1
    mat = [[inv_fact(lam[i] - mu[j] - i + j) for j in range(r)] for i in range(r)]
    a = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
    b_ = mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
    c_ = mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
    d = a - b_ + c_
    res = factorial(n) * d
    if res.denominator != 1:
        return None
    return res.numerator


def add_vertical_2_strip(mu):
    """Return list of ν obtained by adding a vertical 2-strip to mu."""
    mu = list(mu) + [0, 0, 0, 0]  # pad
    results = []
    r = 4  # up to 4 rows in intermediate, we'll restrict later
    # Try all ways to add 2 cells, one per row.
    for i1 in range(r):
        # Can add at row i1: new cell at col mu[i1] + 1.
        # But must satisfy shape constraint (row i1's new length ≤ row i1-1's length).
        new_mu_1 = mu[:]
        new_mu_1[i1] += 1
        # Check partition
        if i1 > 0 and new_mu_1[i1] > new_mu_1[i1-1]:
            continue
        for i2 in range(i1 + 1, r):
            new_mu_2 = new_mu_1[:]
            new_mu_2[i2] += 1
            if new_mu_2[i2] > new_mu_2[i2-1]:
                continue
            # Trim trailing zeros
            result = tuple(x for x in new_mu_2 if x > 0)
            results.append(result)
    return results


def e_2_power_schur(j, max_rows=None):
    """Compute e_2^j in Schur basis (dict mu -> coef).
    Optional max_rows filters mu to at most max_rows nonzero parts."""
    current = defaultdict(int)
    current[tuple()] = 1
    for _ in range(j):
        new = defaultdict(int)
        for mu, coef in current.items():
            if coef == 0: continue
            for nu in add_vertical_2_strip(mu):
                new[nu] += coef
        current = new
    if max_rows is not None:
        return {mu: c for mu, c in current.items() if len(mu) <= max_rows}
    return dict(current)


# Test: e_2^j in Schur basis for j = 1..6.
print("=" * 78)
print("Verifying e_2^j Schur expansion — restricted to ≤ 3 rows.")
print("=" * 78)
for j in range(1, 7):
    expansion = e_2_power_schur(j, max_rows=3)
    total = sum(expansion.values())
    print(f"j = {j}: (sum={total}) {sorted(expansion.items())}")


# Now test: M_j(a, b, 5) = sum_mu coef * f^{(a,b,5)/mu}.
print()
print("=" * 78)
print("VERIFY: M_j(a, b, 5) = sum_mu [s_mu : e_2^j] * f^{(a,b,5)/mu}")
print("=" * 78)
print(f"{'shape':>8s} {'j':>3s} | {'M_j':>18s} | {'formula':>18s} | match")
print("-" * 78)
ok_count = 0
total = 0
for a in range(5, 22):
    for b in range(5, min(a, 18) + 1):
        if (a + b + 5) % 2 != 0: continue
        if a < b or b < 5: continue
        for j in range(0, 7):
            m = M_j(a, b, j)
            if m is None: continue
            expansion = e_2_power_schur(j, max_rows=3)
            pred = 0
            for mu, coef in expansion.items():
                pred += coef * f_skew([a, b, 5], list(mu))
            match = m == pred
            if match:
                ok_count += 1
            else:
                print(f"({a:>2},{b:>2}) {j:>3d} | {m:>18d} | {pred:>18d} | {match}")
            total += 1
print(f"\nOverall: {ok_count}/{total} matches.")
