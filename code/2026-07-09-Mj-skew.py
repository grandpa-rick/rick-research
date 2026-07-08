"""Test whether M_j(a, b, c) = f^{(a,b,c)/(j,j)} via Aitken's determinant.

Hypothesis: M_j = number of SYT of skew shape (a, b, c) / (j, j, 0).

Aitken's formula:
    f^{λ/μ} = |λ/μ|! · det [ 1/((λ_i - μ_j - i + j)!) ]_{i,j}

with the convention that 1/n! = 0 if n < 0.
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
    """1/n! as Fraction, or 0 if n < 0."""
    if n < 0:
        return Fraction(0)
    return Fraction(1, factorial(n))


def f_skew(lam, mu):
    """Aitken's determinant formula for f^{lam/mu} — number of standard skew
    tableaux."""
    r = len(lam)
    mu = list(mu) + [0] * (r - len(mu))
    # Check lam/mu valid.
    for i in range(r):
        if lam[i] < mu[i]:
            return 0
    n = sum(lam) - sum(mu)
    # Aitken: f^{lam/mu} = n! · det[1/((lam_i - mu_j - i + j)!)]_{ij}
    mat = [[inv_fact(lam[i] - mu[j] - i + j) for j in range(r)] for i in range(r)]

    # Compute determinant (3x3 by cofactor, or general via Bareiss)
    def det(m):
        n_ = len(m)
        if n_ == 1: return m[0][0]
        if n_ == 2: return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        if n_ == 3:
            a = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            b = m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            c = m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            return a - b + c
        raise NotImplementedError

    d = det(mat)
    res = factorial(n) * d
    if res.denominator != 1:
        return None  # bug
    return res.numerator


# --------------------------------------------------------------------
# TEST: M_j vs f^{(a,b,c)/(j,j,0)} at c = 5.
# --------------------------------------------------------------------
c = 5
print("Test: M_j(a, b, 5) vs f^{(a,b,5)/(j,j,0)}")
print(f"{'shape':>10s} {'j':>3s} | {'M_j':>15s} | {'f^{(a,b,5)/(j,j,0)}':>20s} | match")
print("-" * 72)
for (a, b) in [(6, 5), (7, 6), (8, 5), (8, 7), (9, 6), (10, 5), (10, 7),
               (11, 8), (12, 5), (13, 10)]:
    if (a + b + 5) % 2 != 0: continue
    if a < b or b < 5: continue
    for j in range(0, 6):
        m = M_j(a, b, j)
        if m is None: continue
        try:
            fs = f_skew([a, b, 5], [j, j, 0])
        except Exception as e:
            fs = f"err: {e}"
        match = "yes" if m == fs else "NO"
        print(f"({a:>2},{b:>2}) {j:>3d} | {str(m):>15s} | {str(fs):>20s} | {match}")


print()
print("Alternate skew: (a, b, c)/(2j, 0, 0) — remove 2j from top row.")
print(f"{'shape':>10s} {'j':>3s} | {'M_j':>15s} | {'f^{(a,b,5)/(2j,0,0)}':>22s} | match")
print("-" * 72)
for (a, b) in [(6, 5), (7, 6), (8, 5), (10, 5), (11, 8)]:
    if (a + b + 5) % 2 != 0: continue
    for j in range(0, 6):
        m = M_j(a, b, j)
        if m is None: continue
        try:
            fs = f_skew([a, b, 5], [2 * j, 0, 0])
        except Exception:
            fs = None
        match = "yes" if m == fs else "NO"
        print(f"({a:>2},{b:>2}) {j:>3d} | {str(m):>15s} | {str(fs):>22s} | {match}")


print()
print("Alt: (a, b, c)/(j, 0, 0) — remove j from top row only.")
for (a, b) in [(6, 5), (8, 5), (10, 5), (8, 7)]:
    for j in range(0, 6):
        m = M_j(a, b, j)
        if m is None: continue
        try:
            fs = f_skew([a, b, 5], [j, 0, 0])
        except Exception:
            fs = None
        print(f"  ({a},{b}) j={j}: M={m}, f^skew(j,0,0) = {fs}, match={m == fs}")


print()
print("Alt: (a, b, c)/(0, 0, j) — remove j from bottom row.")
for (a, b) in [(6, 5), (8, 5), (10, 5), (8, 7)]:
    for j in range(0, 4):
        m = M_j(a, b, j)
        if m is None: continue
        try:
            fs = f_skew([a, b, 5], [0, 0, j])
        except Exception:
            fs = None
        print(f"  ({a},{b}) j={j}: M={m}, f^skew(0,0,j) = {fs}, match={m == fs}")


print()
print("Alt: (a, b, c)/(0, j, j) — remove j from rows 2 and 3.")
for (a, b) in [(6, 5), (8, 5), (10, 5), (8, 7)]:
    for j in range(0, 4):
        m = M_j(a, b, j)
        if m is None: continue
        try:
            fs = f_skew([a, b, 5], [0, j, j])
        except Exception:
            fs = None
        print(f"  ({a},{b}) j={j}: M={m}, f^skew(0,j,j) = {fs}, match={m == fs}")
