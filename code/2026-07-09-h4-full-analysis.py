"""Day 87 - Full analysis of H_4: extract h_k^{(4)}, verify min v_2 = 4.

Approach:
  - Extract h_k^{(4)}(a,b) from template inversion for many (a,b) with valid parity.
  - Attempt polynomial fits for each h_k^{(4)}(a,b).
  - Empirically test whether v_2(h_k * C(j,k)) >= 4 for all (a,b,j) with valid parity.
  - Locate min v_2(H_4) achievers.
"""
from math import factorial
from fractions import Fraction
from collections import Counter, defaultdict


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def C(n, k):
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
    """M_j(a,b,c) via Sym-side formula."""
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
    """H_c(a,b,j) via template inversion."""
    N = a + b + c - 2*j
    if N < 0 or (b - j) < 0 or (b - j) > N:
        return None
    Mj = M_j_sym(a, b, c, j)
    if Mj is None:
        return None
    prod_bij = 1
    for i in range(1, c+1):
        prod_bij *= (b + i - j)
    CNbj = C(N, b - j)
    if CNbj == 0 or (a - b + 1) == 0 or (a - c + 2) == 0 or (b - c + 1) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    val = Fraction(numer_A, CNbj * (a - b + 1)) + factorial(2*c) * C(j, 2*c)
    h = val / Fraction((a - c + 2) * (b - c + 1))
    if h.denominator == 1:
        return int(h)
    return None


def extract_h_k_from_H_c(a, b, c, jmax):
    """Given H_c(a,b,j) for j=0,...,jmax, solve for h_k^{(c)}(a,b) for k=0..jmax."""
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
            val -= hks[kk] * C(k, kk)
        hks.append(val)
    return hks


# ============================================================
# Brute-force min v_2(H_4) with valid parity constraint
# ============================================================
def brute_min_v2_H4_valid():
    print("=" * 60)
    print("Empirical min v_2(H_4) with valid parity a+b even, a>=b>=4")
    print("=" * 60)
    minv = float('inf')
    achievers = []
    dist = Counter()
    # H_4 has 2c=8 as (2c)!, so C(j, 8) starts at j=8. Sample j = 0..12.
    for a in range(4, 22):
        for b in range(4, a + 1):
            if (a + b) % 2 != 0:
                continue
            # Compute H_4 via extracted polynomial
            hks = extract_h_k_from_H_c(a, b, 4, jmax=5)
            if hks is None:
                continue
            # Wait - we need to know all h_k up to k = 2c-1 = 7 to compute H_4 for j>=6
            # For now, sample only j=0..5
            for j in range(0, 6):
                h = H_c_template(a, b, 4, j)
                if h is None or h == 0:
                    continue
                v = v2(h)
                dist[v] += 1
                if v < minv:
                    minv = v
                    achievers = [(a, b, j, h)]
                elif v == minv:
                    achievers.append((a, b, j, h))
    print(f"  min v_2(H_4) = {minv}")
    print(f"  # achievers: {len(achievers)}")
    for a, b, j, h in achievers[:15]:
        print(f"    (a,b,j)=({a},{b},{j}): H_4 = {h}, v_2 = {v2(h)}")
    print(f"  v_2 distribution: {dict(sorted(dist.items()))}")


# ============================================================
# Also try (a, b) < c (Rick's convention allows this in Day 84 formula)
# For c=5, the min was at (3, 0, 2) — a, b < c=5.
# Same for c=4? Try (a, b) small.
# ============================================================
def brute_H4_polynomial(a_max=20, b_max=20, j_max=12):
    """Compute H_4 via extracted polynomial coefficients evaluated at large (a,b)
    then substituted with small (a,b).

    Alternative: since H_4 is a polynomial in (a,b,j) of some fixed degree,
    if we know its coefficients we can evaluate anywhere.

    For now, use symbolic H_4 via extrapolated h_k^{(4)} at each (a, b).
    """
    print("=" * 60)
    print("H_4 min v_2 via extended sampling to small (a,b) < c")
    print("=" * 60)
    # We need h_k^{(4)} as a polynomial in (a, b). Fit it.
    # Sample H_4 at many (a, b, j) with a >= b >= c=4 valid, and use polynomial fit.
    #
    # For h_k^{(4)}(a, b): its degree in (a, b) can be inferred from c=5 case.
    # At c=5, h_0 is degree 8, h_1 is degree 6, h_2 is degree 5 (through the -20 factor
    # times deg-3 poly times deg-2 poly times deg-2 bracket). Hmm let me just fit.
    pass


if __name__ == "__main__":
    brute_min_v2_H4_valid()
