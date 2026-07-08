"""For c=5, compute M_j(a,b,5) via Clio's Lemma 1 for j > 0 and see if it
equals f^(some shifted shape). Test:

- f^(a-j, b-j, 5) [shift both first two rows by j]
- f^(a, b, 5-2j)  [shrink third row]
- f^(a+j, b+j, 5-2j)
- f^(a-j, b-j, 5) with truncation
- etc.
"""
from math import factorial


def C(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def hook_length(lam):
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    n = sum(lam)
    cols = [0] * lam[0]
    for i, li in enumerate(lam):
        for j in range(li):
            cols[j] += 1
    hooks = 1
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = cols[j] - i - 1
            hooks *= (arm + leg + 1)
    return factorial(n) // hooks


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


def M_j(a, b, c, j):
    """Clio's Lemma 1 closed form, c=5."""
    assert c == 5
    m = (a + b + c) // 2
    N = 2 * (m - j)
    Q5 = (a - 3) * (b - 4) * H5(a, b, j) - factorial(10) * C(j, 10)
    den = 120 * (a + 6 - j)
    for i in range(1, 6):
        den *= (b + i - j)
    num = C(N, b - j) * (a - b + 1) * Q5
    if den == 0:
        return None
    if num % den != 0:
        return None
    return num // den


# Test: M_j(a, b, 5) vs various candidate shape formulas.
print("Testing M_j(a, b, 5) for j > 0 vs candidate shapes:")
print(f"{'(a,b,j)':>10s} | {'M_j':>15s} | {'f(a-j,b-j,5)':>15s} | {'f(a,b,5-2j)':>15s} | {'f(a-j,b,5-j)':>15s} | {'f(a-2j,b-j,5)':>15s}")
print("-" * 100)
for (a, b) in [(11, 8), (13, 10), (14, 11), (15, 12)]:
    for j in range(0, 6):
        try:
            m = M_j(a, b, 5, j)
        except Exception:
            m = None
        # Candidate 1: shape (a-j, b-j, 5)
        try:
            l1 = [a - j, b - j, 5]
            if l1[0] >= l1[1] >= l1[2] > 0:
                f1 = hook_length(l1)
            else:
                f1 = None
        except Exception:
            f1 = None
        # Candidate 2: shape (a, b, 5-2j)
        try:
            l2 = [a, b, 5 - 2 * j]
            if l2[0] >= l2[1] >= l2[2] > 0:
                f2 = hook_length(l2)
            else:
                f2 = None
        except Exception:
            f2 = None
        # Candidate 3: shape (a-j, b, 5-j)
        try:
            l3 = [a - j, b, 5 - j]
            if l3[0] >= l3[1] >= l3[2] > 0:
                f3 = hook_length(l3)
            else:
                f3 = None
        except Exception:
            f3 = None
        # Candidate 4: shape (a-2j, b-j, 5)
        try:
            l4 = [a - 2 * j, b - j, 5]
            if l4[0] >= l4[1] >= l4[2] > 0:
                f4 = hook_length(l4)
            else:
                f4 = None
        except Exception:
            f4 = None
        print(f"{'(' + str(a) + ',' + str(b) + ',' + str(j) + ')':>10s} | {str(m):>15s} | {str(f1):>15s} | {str(f2):>15s} | {str(f3):>15s} | {str(f4):>15s}")


# Look for the pattern: what's M_j / M_0 as a function of j?
print("\nRatio M_j / M_0 for (a,b)=(11,8):")
a, b, c = 11, 8, 5
M0 = M_j(a, b, c, 0)
for j in range(0, 6):
    Mj = M_j(a, b, c, j)
    if Mj is not None and M0 != 0:
        # Print as reduced fraction if possible
        from math import gcd
        g = gcd(Mj, M0)
        print(f"  j={j}: M_j = {Mj}, M_j/M_0 = {Mj//g}/{M0//g}")


# Another angle: what if M_j corresponds to a plethysm or Kostka number?
# Try: M_j = K_{lambda, mu} where lambda = (a, b, c) and mu depends on j.
# For j=0, mu = (1^N) gives K = f^lambda. For j=1, maybe mu = (2, 1^(N-2))?
# That would give Kostka = number of SYT with descent at 1 (?).
# Let's just look at the numerics.
