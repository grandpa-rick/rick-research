"""Nail down M_j(a, b, c) / M_0(a, b, c) as a rational function.

Established (algebraically, verified by hand):

    M_1 / M_0 = [(a+c+1)(b+c) - c(c-1)] / [n(n-1)]

where n = a + b + c. For c = 5, this is [(a+6)(b+5) - 20] / [(a+b+4)(a+b+5)].

Now determine P_j := M_j/M_0 · (n)_{2j} as an explicit polynomial in (a, b, c).
Test conjecture: P_j is a polynomial of total degree 2j in (a, b), with
c-dependent coefficients.

We only have c = 5 numerics. So we fit P_j(a, b) at c = 5 as a polynomial
of total degree 2j in (a, b), and look for structure.
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


def falling(n, k):
    r = 1
    for i in range(k):
        r *= (n - i)
    return r


# Build P_j(a, b) = M_j/M_0 · (n)_{2j} for c = 5 as Fractions.
c = 5


def get_P_frac(a, b, j):
    M0 = M_j(a, b, 0)
    Mj = M_j(a, b, j)
    if M0 is None or Mj is None: return None
    n = a + b + c
    fall = falling(n, 2 * j)
    return Fraction(Mj * fall, M0)


# Verify integer (should be).
print("Verify P_j(a, b, 5) is integer:")
for (a, b) in [(6, 5), (8, 5), (10, 5), (12, 5), (8, 7), (10, 7)]:
    for j in range(0, 6):
        p = get_P_frac(a, b, j)
        if p is None: continue
        is_int = (p.denominator == 1)
        print(f"  (a,b,j)=({a},{b},{j}): P_j = {p} (integer={is_int})")


# ------------------------------------------------------------
# Fit P_j(a, b, 5) as polynomial of total degree 2j in (a, b).
# ------------------------------------------------------------
print()
print("=" * 78)
print("Fit P_j(a, b, 5) as polynomial in (a, b) of total degree 2j.")
print("=" * 78)


def monomials(deg):
    """All (i, j) with i + j <= deg, listed."""
    ms = []
    for total in range(deg + 1):
        for i in range(total + 1):
            ms.append((i, total - i))
    return ms


def fit_poly(points, deg):
    """Given list of ((a, b), value), fit polynomial of total degree deg via
    exact Gaussian elimination. Picks linearly independent rows greedily."""
    mons = monomials(deg)
    n = len(mons)

    # Build big matrix.
    A = []
    yv = []
    pts = []
    for (aa, bb), v in points:
        row = [Fraction(aa ** i * bb ** k) for (i, k) in mons]
        A.append(row)
        yv.append(Fraction(v))
        pts.append((aa, bb))

    if len(A) < n:
        return None, None, "not enough points"

    # Greedy row selection to build nonsingular square system.
    used = []
    Areduced = []  # RREF of Asq
    yreduced = []
    pivots = []  # column indices already pivoted

    for r_idx in range(len(A)):
        # Try adding row r_idx to see if it's independent of current pivots.
        row = A[r_idx][:]
        y = yv[r_idx]
        # Eliminate against existing pivots.
        for i, pc in enumerate(pivots):
            if row[pc] != 0:
                f = row[pc] / Areduced[i][pc]
                for k in range(n):
                    row[k] -= f * Areduced[i][k]
                y -= f * yreduced[i]
        # Find first nonzero.
        pc = None
        for k in range(n):
            if row[k] != 0:
                pc = k; break
        if pc is None:
            # Consistent: pred should equal y (which is 0).
            if y != 0:
                return None, None, f"inconsistent at pts[{r_idx}]"
            continue
        used.append(r_idx)
        Areduced.append(row)
        yreduced.append(y)
        pivots.append(pc)
        if len(pivots) == n:
            break

    if len(pivots) < n:
        return None, None, "underdetermined (rank deficient)"

    # Back-substitute to find coefs.
    coefs = [Fraction(0)] * n
    for i in reversed(range(n)):
        pc = pivots[i]
        s = yreduced[i]
        for k in range(n):
            if k != pc and coefs[k] != 0:
                s -= Areduced[i][k] * coefs[k]
        coefs[pc] = s / Areduced[i][pc]

    # Verify all points.
    ok = True
    for r in range(len(A)):
        pred = sum(coefs[i] * A[r][i] for i in range(n))
        if pred != yv[r]:
            ok = False; break

    return coefs, ok, "OK"


# For c = 5.
c = 5
for j in range(0, 5):
    pts = []
    # Sweep of (a, b) points.
    for a in range(5, 22):
        for b in range(5, min(a, 18) + 1):
            if (a + b + c) % 2 != 0: continue
            p = get_P_frac(a, b, j)
            if p is None: continue
            pts.append(((a, b), p))
    deg = 2 * j
    coefs, ok, msg = fit_poly(pts, deg)
    if coefs is None:
        print(f"j = {j}: fit failed: {msg} ({len(pts)} available).")
        continue
    mons = monomials(deg)
    terms = []
    for m, cf in zip(mons, coefs):
        if cf == 0: continue
        i, k = m
        s = ""
        if cf != 1: s = str(cf)
        if i > 0: s += f" a^{i}" if i > 1 else " a"
        if k > 0: s += f" b^{k}" if k > 1 else " b"
        terms.append(s.strip())
    print(f"\n j = {j} (deg {deg}, fit ok = {ok}):")
    print(f"    P_{j}(a, b, 5) = " + " + ".join(terms))
