"""Debug: check h_k^{(4)} at various (a, b) and see if the formula
   h_1 = -12(a+3)(a+4)(b+2)(b+3) holds throughout.
"""
from math import factorial
from fractions import Fraction


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def Cn(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def hook_length_lambda(lam):
    n = sum(lam)
    if lam[0] == 0:
        return 1 if all(l == 0 for l in lam) else 0
    a = lam[0]
    cols = [0] * a
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


def M_j_sym(a, b, c, j):
    tables = {
        0: [((0, 0, 0), 1)],
        1: [((1, 1, 0), 1)],
        2: [((2, 2, 0), 1), ((2, 1, 1), 1)],
        3: [((3, 3, 0), 1), ((3, 2, 1), 2), ((2, 2, 2), 1)],
        4: [((4, 4, 0), 1), ((4, 3, 1), 3), ((4, 2, 2), 2), ((3, 3, 2), 3)],
        5: [((5, 5, 0), 1), ((5, 4, 1), 4), ((5, 3, 2), 5), ((4, 4, 2), 6),
            ((4, 3, 3), 5)],
    }
    if j == 0:
        return hook_length_lambda((a, b, c)) if (a >= b >= c >= 0) else 0
    if j not in tables:
        return None
    xs = (a + 2, b + 1, c)
    n = a + b + c
    if n < 2 * j:
        return 0
    total = Fraction(0)
    for mu, k in tables[j]:
        ks = [mu[jj] + (2 - jj) for jj in range(3)]
        def fall(x, kk):
            p = 1
            for i in range(kk):
                p *= (x - i)
            return p
        M = [[fall(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        det = (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
             - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
             + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))
        f_lam_mu_num = factorial(n - 2*j) * det
        f_lam_mu_den = factorial(a+2) * factorial(b+1) * factorial(c)
        total += Fraction(k * f_lam_mu_num, f_lam_mu_den)
    if total.denominator != 1:
        return None
    return int(total)


def H_c_template(a, b, c, j):
    N = a + b + c - 2*j
    if N < 0 or (b - j) < 0 or (b - j) > N:
        return None
    Mj = M_j_sym(a, b, c, j)
    if Mj is None:
        return None
    prod_bij = 1
    for i in range(1, c+1):
        prod_bij *= (b + i - j)
    CNbj = Cn(N, b - j)
    if CNbj == 0 or (a - b + 1) == 0 or (a - c + 2) == 0 or (b - c + 1) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    val = Fraction(numer_A, CNbj * (a - b + 1)) + factorial(2*c) * Cn(j, 2*c)
    h = val / Fraction((a - c + 2) * (b - c + 1))
    if h.denominator == 1:
        return int(h)
    return None


def extract_h_k(a, b, c, jmax):
    Hs = []
    for j in range(jmax + 1):
        h = H_c_template(a, b, c, j)
        if h is None:
            return None
        Hs.append(h)
    hks = []
    for k in range(jmax + 1):
        val = Hs[k]
        for kk in range(k):
            val -= hks[kk] * Cn(k, kk)
        hks.append(val)
    return hks


# Debug h_1: check if it fits -12(a+3)(a+4)(b+2)(b+3)
def h1_conj(a, b): return -12*(a+3)*(a+4)*(b+2)*(b+3)

print("Testing h_1 fit at c=4:")
for a in range(4, 22):
    for b in range(4, a + 1):
        if (a + b) % 2 != 0:
            continue
        hks = extract_h_k(a, b, 4, jmax=5)
        if hks is None:
            print(f"  ({a}, {b}): extraction FAILED")
            continue
        got = hks[1]
        expected = h1_conj(a, b)
        marker = "" if got == expected else " MISMATCH"
        if got != expected or a in (4, 5, 21, 20, 18, 14, 15):
            print(f"  ({a}, {b}): h_1 = {got}, expected = {expected}{marker}")
