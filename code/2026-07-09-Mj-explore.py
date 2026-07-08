"""Day 85 — M_j exploration.

Goal: identify M_j(a, b, c) for c=5, j>=1 as a symmetric-function object.

Approach:
  1) Tabulate M_j(a, b, 5) exactly by inverting Clio's Lemma 1.
  2) For each (a, b, j), factor M_j and look at prime signatures.
  3) Test if M_j / M_0 depends only on (c, j) [rule out trivial world].
  4) Try candidate Kostka numbers K_{(a,b,5), mu} for various mu.
  5) Try skew hook-content formulas.
"""
from math import factorial, gcd
from fractions import Fraction


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
        for jj in range(li):
            cols[jj] += 1
    hooks = 1
    for i, li in enumerate(lam):
        for jj in range(li):
            arm = li - jj - 1
            leg = cols[jj] - i - 1
            hooks *= (arm + leg + 1)
    return factorial(n) // hooks


def H5(a, b, j):
    """Clio's c=5 heavy quotient — polynomial in (a,b,j)."""
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
    """Clio's Lemma 1 closed form for c=5 — inversion for M_j."""
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


def v2(n):
    if n == 0: return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def small_factor(n, primes=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)):
    """Factor out small primes; return (dict, residue)."""
    if n == 0: return {}, 0
    s = 1 if n > 0 else -1
    n = abs(n)
    fs = {}
    for p in primes:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            fs[p] = e
    return fs, s * n


# ------------------------------------------------------------
# STEP 1: tabulate M_j(a, b, 5) integer values.
# ------------------------------------------------------------

print("=" * 78)
print("STEP 1: M_j(a, b, 5) for j = 0..8 and (a, b) sweep with a+b+c even.")
print("=" * 78)

# Valid partition (a, b, 5) needs a >= b >= 5.
# For c=5, a+b+5 even => a+b odd.
sweeps = []
for a in range(6, 21):
    for b in range(5, min(a, 16) + 1):
        if (a + b + 5) % 2 == 0 and b >= 5 and a >= b:
            sweeps.append((a, b))

# Only keep a few representative shapes for readable output.
main_shapes = [(6, 5), (8, 5), (8, 7), (9, 6), (10, 5), (10, 7), (11, 6),
               (11, 8), (12, 5), (12, 7), (13, 6), (13, 8), (13, 10)]

hdr = "(a, b)  |     j |         M_j       | factored"
print(hdr); print("-" * len(hdr))
Mtable = {}  # (a,b,j) -> M_j
for (a, b) in main_shapes:
    for j in range(0, 9):
        mj = M_j(a, b, j)
        Mtable[(a, b, j)] = mj
        fs, res = small_factor(mj) if mj is not None else ({}, None)
        factored = " * ".join(f"{p}^{e}" for p, e in fs.items()) if fs else ""
        if res not in (1, -1, None):
            factored += f" * {res}"
        print(f"({a:>2},{b:>2}) | {j:>4}  | {str(mj):>18s} | {factored}")

# ------------------------------------------------------------
# STEP 2: Ratio M_j / M_0.
# Test whether it depends only on (c, j) or on (a, b) also.
# ------------------------------------------------------------
print()
print("=" * 78)
print("STEP 2: Ratio M_j / M_0 across (a, b) — same j?")
print("=" * 78)
for j in range(1, 6):
    print(f"\n j = {j}:")
    for (a, b) in main_shapes:
        M0 = Mtable[(a, b, 0)]
        Mj = Mtable[(a, b, j)]
        if M0 is None or Mj is None: continue
        g = gcd(Mj, M0)
        p, q = Mj // g, M0 // g
        print(f"  (a,b)=({a:>2},{b:>2}): M_{j}/M_0 = {p} / {q}  (float={Mj/M0:.6f})")


# ------------------------------------------------------------
# STEP 3: Kostka candidate matching.
# ------------------------------------------------------------
print()
print("=" * 78)
print("STEP 3: Kostka number candidates.")
print("=" * 78)


def transpose(lam):
    lam = [x for x in lam if x > 0]
    if not lam: return []
    m = lam[0]
    return [sum(1 for x in lam if x > i) for i in range(m)]


def dominance(mu, lam):
    """mu <= lam in dominance order (both sorted decreasing)."""
    smu = 0; slam = 0
    for i in range(max(len(mu), len(lam))):
        smu += mu[i] if i < len(mu) else 0
        slam += lam[i] if i < len(lam) else 0
        if smu > slam: return False
    return True


def kostka(lam, mu):
    """Compute K_{lambda, mu} = number of SSYT of shape lambda and content mu.
    Use recursion via Pieri: K_{lam, mu} = number of SSYT of shape lam s.t.
    n_i(SSYT) = mu_i. Direct SSYT enumeration for small shapes.
    """
    lam = [x for x in lam if x > 0]
    mu = [x for x in mu if x > 0]
    if sum(lam) != sum(mu): return 0
    if not dominance(mu, lam): return 0

    # Generate SSYT of shape lam with content mu.
    rows = len(lam)
    n = sum(lam)
    # Fill positions in reading order (row-major).
    positions = [(i, j) for i in range(rows) for j in range(lam[i])]

    # remaining[k] = number of k+1's still available
    def count(pos_idx, filled):
        if pos_idx == n:
            return 1
        i, j = positions[pos_idx]
        total = 0
        # Values allowed: > entry above (if j < lam[i-1]) and >= entry left (if j > 0)
        # But content constraint: mu counts.
        min_val = 1
        if j > 0:
            # SSYT: rows weakly increasing
            min_val = max(min_val, filled[(i, j - 1)])
        if i > 0:
            # SSYT: columns strictly increasing
            min_val = max(min_val, filled[(i - 1, j)] + 1)
        for v in range(min_val, len(mu) + 1):
            if filled['_remain'][v - 1] > 0:
                filled[(i, j)] = v
                filled['_remain'][v - 1] -= 1
                total += count(pos_idx + 1, filled)
                filled['_remain'][v - 1] += 1
                del filled[(i, j)]
        return total

    remain = list(mu)
    filled = {'_remain': remain}
    return count(0, filled)


# Quick sanity: K_{(a,b,c), (1^n)} = f^(a,b,c)?
print("\nSanity: K_{(a,b,c), (1^n)} vs f^(a,b,c)")
for (a, b, c) in [(3, 2, 1), (4, 2, 1), (3, 2, 2), (2, 2, 2)]:
    n = a + b + c
    k1 = kostka([a, b, c], [1] * n)
    fl = hook_length([a, b, c])
    print(f"  lam=({a},{b},{c}): K_(lam, 1^n) = {k1}, f^lam = {fl}, match={k1 == fl}")


# Try candidate mu's for M_j.
print("\nSearching Kostka mu candidates for M_j(a,b,5), c=5.")

# We consider (a, b) small enough for Kostka enumeration to finish.
small_shapes = [(6, 5), (7, 6), (8, 5), (8, 7)]
for (a, b) in small_shapes:
    lam = [a, b, 5]
    n = a + b + 5
    print(f"\n  lam = ({a}, {b}, 5), |lam| = {n}")
    M_vals = {j: Mtable[(a, b, j)] for j in range(0, 5)}
    print(f"    M_j values: {M_vals}")

    # For each j, search all mu of size n with two nonzero parts, hook, etc.
    for j in range(0, 5):
        target = M_vals[j]
        if target is None: continue
        matches = []
        # Enumerate candidate mu shapes.
        # (n - k, 1^k) hooks
        for k in range(0, n):
            mu = [n - k] + [1] * k
            if kostka(lam, mu) == target:
                matches.append(("hook", mu))
        # (n - k, k) two-part
        for k in range(0, n // 2 + 1):
            if n - k >= k:
                mu = [n - k, k] if k > 0 else [n]
                if kostka(lam, mu) == target:
                    matches.append(("two-part", mu))
        # (n - 2k, 2^k)
        for k in range(0, n // 2 + 1):
            if n - 2 * k >= 2:
                mu = [n - 2 * k] + [2] * k
                if kostka(lam, mu) == target:
                    matches.append(("(n-2k, 2^k)", mu))
        # (n - 2j, 2, 1^{2j-2}) if j > 0
        if 2 * j >= 2 and n - 2 * j >= 2:
            mu = [n - 2 * j, 2] + [1] * (2 * j - 2)
            if kostka(lam, mu) == target:
                matches.append(("(n-2j,2,1^(2j-2))", mu))
        # (n - j, 1^j) — j-hook
        if n >= j:
            mu = [n - j] + [1] * j
            if kostka(lam, mu) == target:
                matches.append(("(n-j,1^j)", mu))
        print(f"    j = {j}: target = {target}, matches = {matches[:3]}")
