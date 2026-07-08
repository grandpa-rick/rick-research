"""Consequences of M_j identification:

If M_j(a, b, c) = sum_mu K_{mu^T, (2^j)} * f^{(a,b,c)/mu} holds for ALL c
(the natural extrapolation from checked-sober c-uniformity of Lemma 1
template), then we can compute:

  H_c(a, b, j) = c! * (a+c+1-j) * prod_{i=1..c}(b+i-j) * M_j /
                  [C(N, b-j) * (a-b+1) * (a-c+2) * (b-c+1)]

(no tip needed when j < 2c) and thus compute beta'(c) directly.

Sanity check: at c = 5, does the formula reproduce H_5? YES by construction
(M_j was derived from H_5 inversion). But we can verify at c = 5 for some
(a, b, j).

Extension to c > 5: reproduce Clio's beta'(c) at c = 6, 7, 8, 9, 10?
"""
from math import factorial
from fractions import Fraction
from collections import defaultdict


def C(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def inv_fact(n):
    if n < 0: return Fraction(0)
    return Fraction(1, factorial(n))


def f_skew_poly(lam, mu):
    """Aitken determinant f^{lam/mu} — treats lam, mu as tuples of ints
    (may be non-partitions). Returns int or None."""
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
    if r == 3:
        a = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
        b_ = mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
        c_ = mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
        d = a - b_ + c_
    else:
        raise NotImplementedError
    res = factorial(n) * d
    if res.denominator != 1:
        return None
    return res.numerator


def add_vertical_2_strip(mu):
    mu = list(mu) + [0, 0, 0, 0]
    results = []
    r = 4
    for i1 in range(r):
        new_mu_1 = mu[:]
        new_mu_1[i1] += 1
        if i1 > 0 and new_mu_1[i1] > new_mu_1[i1-1]:
            continue
        for i2 in range(i1 + 1, r):
            new_mu_2 = new_mu_1[:]
            new_mu_2[i2] += 1
            if new_mu_2[i2] > new_mu_2[i2-1]:
                continue
            result = tuple(x for x in new_mu_2 if x > 0)
            results.append(result)
    return results


def e_2_power_schur(j, max_rows=3):
    current = defaultdict(int)
    current[tuple()] = 1
    for _ in range(j):
        new = defaultdict(int)
        for mu, coef in current.items():
            if coef == 0: continue
            for nu in add_vertical_2_strip(mu):
                new[nu] += coef
        current = new
    return {mu: c for mu, c in current.items() if len(mu) <= max_rows}


def M_j_formula(a, b, c, j):
    """M_j via skew tableau formula, valid for partitions (a, b, c) with
    a >= b >= c >= 1."""
    expansion = e_2_power_schur(j, max_rows=3)
    total = 0
    for mu, coef in expansion.items():
        total += coef * f_skew_poly([a, b, c], list(mu))
    return total


def H_c_from_M(a, b, c, j):
    """Reconstruct H_c(a, b, j) from M_j via Clio's Lemma 1 template.

    H_c * (a-c+2)(b-c+1) - (2c)! C(j, 2c)
       = M_j * c! * (a+c+1-j) * prod(b+i-j)_{i=1..c} / [C(N, b-j) * (a-b+1)]

    So H_c = { M_j * c! * (a+c+1-j) * prod * C(N, b-j)(a-b+1) inverse ... }

    Actually rearranging:
    C(N, b-j) * (a-b+1) * [(a-c+2)(b-c+1) H_c - (2c)! C(j, 2c)]
       = c! * (a+c+1-j) * prod_{i=1..c}(b+i-j) * M_j

    So H_c = { c! * (a+c+1-j) * prod * M_j / [C(N, b-j)(a-b+1)] + (2c)! C(j, 2c) } / [(a-c+2)(b-c+1)]
    """
    N = a + b + c - 2 * j
    M = M_j_formula(a, b, c, j)
    prod_b = 1
    for i in range(1, c + 1):
        prod_b *= (b + i - j)
    num_M = factorial(c) * (a + c + 1 - j) * prod_b * M
    den_M = C(N, b - j) * (a - b + 1)
    if den_M == 0: return None
    if num_M % den_M != 0:
        return Fraction(num_M, den_M) + factorial(2 * c) * C(j, 2 * c)
    q = num_M // den_M + factorial(2 * c) * C(j, 2 * c)
    den2 = (a - c + 2) * (b - c + 1)
    if den2 == 0: return None
    if q % den2 != 0:
        return Fraction(q, den2)
    return q // den2


def v2(n):
    if n == 0: return float('inf')
    if isinstance(n, Fraction):
        return v2(n.numerator) - v2(n.denominator)
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


# Sanity: reproduce H_5 for known partitions.
def H5_true(a, b, j):
    """Clio's explicit H_5 polynomial (used for our M_j identity)."""
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


print("Sanity: at c=5, does formula-based H_5 match Clio's polynomial?")
print(f"{'(a,b,j)':>10s} | {'true H_5':>18s} | {'formula H_5':>18s} | match")
print("-" * 65)
for (a, b) in [(8, 5), (10, 5), (11, 8), (13, 10)]:
    if (a + b + 5) % 2 != 0: continue
    for j in range(0, 5):
        true = H5_true(a, b, j)
        pred = H_c_from_M(a, b, 5, j)
        match = "yes" if true == pred else "NO"
        print(f"({a},{b},{j}) | {true:>18d} | {str(pred):>18s} | {match}")


# Now extend to c = 6, 7, 8, 9, 10 and compute beta'(c).
# For each c, sweep (a, b, j) with a >= b >= c (and (a+b+c) even for our
# problem — although the (a, b) don't strictly need to be partition-valid
# for the polynomial extension; we'll sweep integer values).
print()
print("Extending to c > 5: compute min v_2(H_c(a, b, j)) over (a, b, j).")
print("Warning: formula assumes M_j = skew-SYT sum; conjecture at c > 5.")

# Do this simulation carefully — only for (a, b, c) that ARE valid partitions.
# Else the SYT interpretation breaks.
clio_data = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14}
print(f"\nClio's β'(c): {clio_data}")
print(f"\nWith c-uniformity assumption, our formula for c ≥ 5:")
for c in range(5, 11):
    min_v = float('inf')
    argmin = None
    # Sweep valid partition arguments.
    for a in range(c, c + 20):
        for b in range(c, min(a, c + 15) + 1):
            for j in range(0, 2 * c):
                if a < b or b < c: continue
                # For proper valid partition, use SYT-count formula.
                try:
                    H = H_c_from_M(a, b, c, j)
                except Exception:
                    continue
                if H is None: continue
                if isinstance(H, Fraction) and H.denominator != 1:
                    continue  # not integer, skip
                Hi = int(H) if isinstance(H, Fraction) else H
                if Hi == 0: continue
                v = v2(abs(Hi))
                if v < min_v:
                    min_v = v
                    argmin = (a, b, j)
    print(f"  c = {c}: min v_2 = {min_v} at {argmin} — Clio's β'({c}) = {clio_data.get(c)}")
