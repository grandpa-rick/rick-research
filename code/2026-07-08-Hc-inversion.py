"""Attempt to reverse-engineer H_c(a, b, 0) for c > 5 from Clio's Lemma 1.

Ansatz: Clio's c=5 formula has constants (alpha, gamma, beta, delta, const) =
(3, 4, 6, [1,2,3,4,5], 120). Guess pattern for c > 5:
- alpha_c = c - 2
- gamma_c = c - 1
- beta_c = c + 1
- delta_c = [1, 2, ..., c]
- const_c = c!

Then at j = 0:

    H_c(a, b, 0) = M_0(a,b,c) * const_c * (a + beta_c) * prod_{i in delta_c}(b + i)
                   / [C(N, b) * (a - b + 1) * (a - alpha_c) * (b - gamma_c)]

where M_0(a,b,c) = f^(a,b,c) and N = a + b + c.

Test 1: For c=5, this must reproduce the known H_5(a,b,0) = (a+3)(a+4)(a+5)(a+6)(b+2)(b+3)(b+4)(b+5).
Test 2: For c=6, predict H_6(a,b,0) and check it factors as (a+3)(a+4)(a+5)(a+6)(a+7)(b+2)(b+3)(b+4)(b+5)(b+6).
"""
from math import factorial


def s2(n): return bin(n).count('1')


def v2(n):
    if n == 0: return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


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


def Hc_at_j0_predicted(a, b, c):
    """Reverse-engineered H_c(a, b, 0) via inversion of Clio's Lemma 1 template."""
    if (a + b + c) % 2 != 0:
        return None
    if a < b or b < c or c < 1:
        return None
    lam = [a, b, c]
    if lam[0] < lam[1] or lam[1] < lam[2]:
        return None
    M0 = hook_length(lam)  # M_0 = f^lambda
    N = a + b + c
    alpha_c = c - 2
    gamma_c = c - 1
    beta_c = c + 1
    delta_c = list(range(1, c + 1))
    const_c = factorial(c)
    num = M0 * const_c * (a + beta_c)
    for d in delta_c:
        num *= (b + d)
    den = C(N, b) * (a - b + 1) * (a - alpha_c) * (b - gamma_c)
    if den == 0:
        return None
    if num % den != 0:
        return None
    return num // den


def Hc_at_j0_expected(a, b, c):
    """Expected form h_0(a, b) for c: (a+3)..(a+c+1) * (b+2)..(b+c)."""
    p = 1
    for i in range(3, c + 2):
        p *= (a + i)
    for i in range(2, c + 1):
        p *= (b + i)
    return p


# TEST 1: c = 5 sanity
print("=" * 70)
print("Test 1: c=5 sanity — inversion should reproduce (a+3)...(a+6)(b+2)...(b+5)")
print("=" * 70)
print(f"{'(a,b)':>10s} | {'inverted':>18s} | {'expected h_0':>18s} | match")
print("-" * 65)
for a in range(6, 14):
    for b in range(5, min(a + 1, 11)):
        if (a + b + 5) % 2 != 0:
            continue
        inv = Hc_at_j0_predicted(a, b, 5)
        exp = Hc_at_j0_expected(a, b, 5)
        match = "yes" if inv == exp else "NO"
        print(f"{'(' + str(a) + ',' + str(b) + ')':>10s} | {str(inv):>18s} | {exp:18d} | {match}")


# TEST 2: c = 6 prediction
print("\n" + "=" * 70)
print("Test 2: c=6 — does the same inversion give (a+3)...(a+7)(b+2)...(b+6)?")
print("=" * 70)
print(f"{'(a,b)':>10s} | {'inverted':>22s} | {'expected h_0(c=6)':>22s} | match")
print("-" * 75)
for a in range(7, 16):
    for b in range(6, min(a + 1, 12)):
        if (a + b + 6) % 2 != 0:
            continue
        inv = Hc_at_j0_predicted(a, b, 6)
        exp = Hc_at_j0_expected(a, b, 6)
        match = "yes" if inv == exp else "NO"
        print(f"{'(' + str(a) + ',' + str(b) + ')':>10s} | {str(inv):>22s} | {exp:22d} | {match}")


# TEST 3: c = 7 prediction
print("\n" + "=" * 70)
print("Test 3: c=7 — does the same inversion give (a+3)...(a+8)(b+2)...(b+7)?")
print("=" * 70)
print(f"{'(a,b)':>10s} | {'inverted':>25s} | {'expected h_0(c=7)':>25s} | match")
print("-" * 82)
for a in range(8, 17):
    for b in range(7, min(a + 1, 13)):
        if (a + b + 7) % 2 != 0:
            continue
        inv = Hc_at_j0_predicted(a, b, 7)
        exp = Hc_at_j0_expected(a, b, 7)
        match = "yes" if inv == exp else "NO"
        print(f"{'(' + str(a) + ',' + str(b) + ')':>10s} | {str(inv):>25s} | {exp:25d} | {match}")
