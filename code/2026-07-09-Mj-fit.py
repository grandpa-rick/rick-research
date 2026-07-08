"""M_j hypothesis-testing via linear algebra.

CONFIRMED: M_1 = f^{lam/(1,1)}.
CONFIRMED: M_2 = f^{lam/(2,2)} + f^{lam/(2,1,1)}.
UNCLEAR: M_3 = which combination?

Strategy: for each j, fit M_j at multiple (a, b) as sum_mu c_mu · f^{lam/mu}
with mu ⊢ 2j, ≤ 3 parts, integer coefficients c_mu.
Look for coefficients uniform in (a, b) — that's the identification.
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
    for i in range(r - 1):
        if mu[i] < mu[i+1]:
            return 0
    n = sum(lam) - sum(mu)
    if n < 0: return 0
    if n == 0: return 1  # empty shape
    mat = [[inv_fact(lam[i] - mu[j] - i + j) for j in range(r)] for i in range(r)]
    a = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
    b_ = mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
    c_ = mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
    d = a - b_ + c_
    res = factorial(n) * d
    if res.denominator != 1:
        return None
    return res.numerator


def gen_partitions_le(n, max_val, max_parts):
    if n == 0:
        yield ()
        return
    if max_parts == 0: return
    for first in range(min(n, max_val), 0, -1):
        for rest in gen_partitions_le(n - first, first, max_parts - 1):
            yield (first,) + rest


def partitions_of(n, max_parts):
    yield from gen_partitions_le(n, n, max_parts)


# --------------------------------------------------------------------
# For a given j, fit coefficients c_mu such that
#     M_j(a, b, 5) = sum_mu c_mu · f^{(a,b,5)/mu}
# with mu ranging over partitions of 2j with ≤ 3 parts.
# --------------------------------------------------------------------

c = 5

def fit_coefs(j, shapes):
    """Fit c_mu such that M_j(a, b) = sum c_mu · f^{(a,b,c)/mu} across shapes.
    Return the dict of {mu: c_mu} or None if inconsistent."""
    mus = list(partitions_of(2 * j, 3))
    print(f"    Candidate mus (|mu|={2*j}, ≤ 3 parts): {mus}")

    # Build system.
    A = []
    yv = []
    for (a, b) in shapes:
        if (a + b + c) % 2 != 0: continue
        m = M_j(a, b, j)
        if m is None: continue
        row = [Fraction(f_skew([a, b, 5], list(mu))) for mu in mus]
        A.append(row)
        yv.append(Fraction(m))

    if len(A) < len(mus):
        return None, "not enough shapes"

    # Gauss elim to find rank/consistency.
    n = len(mus)
    Aug = [A[i][:] + [yv[i]] for i in range(len(A))]
    pivots = []
    row_used = []
    for i in range(len(Aug)):
        row = Aug[i][:]
        for k, pc in enumerate(pivots):
            if row[pc] != 0:
                f = row[pc] / Aug[row_used[k]][pc]
                for kk in range(n + 1):
                    row[kk] -= f * Aug[row_used[k]][kk]
        pc = None
        for k in range(n):
            if row[k] != 0:
                pc = k; break
        if pc is None:
            # If row[n] != 0 → inconsistent
            if row[n] != 0:
                return None, f"inconsistent"
            continue
        Aug[i] = row
        pivots.append(pc)
        row_used.append(i)

    if len(pivots) < n:
        return None, f"underdetermined (rank {len(pivots)} < {n})"

    coefs = [Fraction(0)] * n
    for i in reversed(range(n)):
        pc = pivots[i]
        s = Aug[row_used[i]][n]
        for k in range(n):
            if k != pc and coefs[k] != 0:
                s -= Aug[row_used[i]][k] * coefs[k]
        coefs[pc] = s / Aug[row_used[i]][pc]

    # Verify.
    for r in range(len(A)):
        pred = sum(coefs[i] * A[r][i] for i in range(n))
        if pred != yv[r]:
            return None, "verify failed"

    return dict(zip(mus, coefs)), "OK"


# Test many shapes.
shapes = []
for a in range(5, 22):
    for b in range(5, min(a, 18) + 1):
        if (a + b + 5) % 2 == 0 and a >= b >= 5:
            shapes.append((a, b))

for j in range(0, 6):
    print(f"\n--- j = {j} ---")
    result, status = fit_coefs(j, shapes)
    print(f"    fit status: {status}")
    if result is not None:
        # Round to integers if very close.
        cleaned = {}
        for mu, cf in result.items():
            if cf == int(cf):
                cleaned[mu] = int(cf)
            else:
                cleaned[mu] = cf
        # Print only nonzero.
        print(f"    nonzero coefs: " + ", ".join(f"{mu} → {c_}" for mu, c_ in cleaned.items() if c_ != 0))
