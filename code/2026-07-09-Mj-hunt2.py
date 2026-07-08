"""M_j identification — round 2.

Key clue from round 1: M_j/M_0 depends on (a, b), so M_j is NOT constant*M_0.
So M_j has combinatorial structure depending on the shape.

CANDIDATES to test:
  (A) M_j = f^(a, b, c, 1^j)     — add j boxes as a vertical strip below
  (B) M_j = f^(a, b, c, 2^j) etc.
  (C) M_j = K_{(a,b,c), μ} for μ = (2^j, 1^{n-2j})  — j pairs of equal elements
  (D) M_j = K_{(a,b,c), μ} for μ = (n-j, 1^j)  — 1-hook with big first part
  (E) M_j = f^(a, b+j, c-j)    or   f^(a+j, b, c-j)   etc.
  (F) M_j = number of SYT of shape (a,b,c) with exactly j pairs (i, i+1) in same row
  (G) M_j = f^(a,b,c) · C(N, 2j) / something  — descent count
"""
from math import factorial


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
    if den == 0:
        return None
    if num % den != 0:
        return None
    return num // den


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


def is_partition(lam):
    lam = [x for x in lam if x != 0]
    if any(x < 0 for x in lam): return False
    for i in range(len(lam) - 1):
        if lam[i] < lam[i+1]: return False
    return True


# Build M_j table.
c = 5
shapes = []
for a in range(5, 21):
    for b in range(5, min(a, 16) + 1):
        if (a + b + 5) % 2 == 0 and a >= b >= 5:
            shapes.append((a, b))

Mtable = {}
for (a, b) in shapes:
    for j in range(0, 10):
        Mtable[(a, b, j)] = M_j(a, b, j)


# Candidate list — parametric.
def cand_A(a, b, c, j): return hook_length([a, b, c] + [1] * j)  # (a,b,c,1^j)


def cand_B(a, b, c, j):
    if j == 0: return hook_length([a, b, c])
    if 2 <= c:
        return hook_length([a, b, c] + [2] * j)
    return None


def cand_E(a, b, c, j):
    lam = [a, b + j, c - j]
    if is_partition(lam): return hook_length(lam)
    return None


def cand_E2(a, b, c, j):
    lam = [a - j, b, c + j]
    if is_partition(lam): return hook_length(lam)
    return None


def cand_E3(a, b, c, j):
    """f^(a-j, b, c) — remove j from row 1."""
    lam = [a - j, b, c]
    if is_partition(lam) and c > 0: return hook_length(lam)
    return None


def cand_E4(a, b, c, j):
    """f^(a, b-j, c+j)."""
    lam = [a, b - j, c + j]
    if is_partition(lam) and lam[2] > 0: return hook_length(lam)
    return None


def cand_H(a, b, c, j):
    """f^(a-j, b, c) * something."""
    if a - j >= b >= c: return hook_length([a - j, b, c])
    return None


# Test.
print("=" * 90)
print("Testing candidate shape formulas M_j = f^{shape(a,b,c,j)}")
print("=" * 90)
print(f"{'shape':>10s} {'j':>3s} | {'M_j':>18s} | "
      f"{'A:f(a,b,c,1^j)':>18s} | {'B:f(a,b,c,2^j)':>18s} | "
      f"{'E:f(a,b+j,c-j)':>18s} | {'E2':>15s} | {'E4':>15s}")
print("-" * 120)
for (a, b) in [(6, 5), (7, 6), (8, 5), (8, 7), (9, 6), (10, 5), (10, 7),
               (11, 8), (13, 10), (12, 5)]:
    if (a + b + c) % 2 != 0: continue
    for j in range(0, 6):
        m = Mtable.get((a, b, j))
        if m is None: continue
        fA = cand_A(a, b, c, j)
        fB = cand_B(a, b, c, j) if c >= 2 else None
        fE = cand_E(a, b, c, j)
        fE2 = cand_E2(a, b, c, j)
        fE4 = cand_E4(a, b, c, j)
        print(f"({a:>2},{b:>2}) {j:>3d} | {m:>18d} | {str(fA):>18s} | "
              f"{str(fB):>18s} | {str(fE):>18s} | {str(fE2):>15s} | {str(fE4):>15s}")


# ----------------------------------------------------------------------
# Systematic Kostka search — via direct enumeration.
# ----------------------------------------------------------------------
def gen_partitions(n, k_min=0, first_max=None):
    """Generate all partitions of n."""
    if n == 0:
        yield ()
        return
    if first_max is None:
        first_max = n
    for first in range(min(first_max, n), 0, -1):
        for rest in gen_partitions(n - first, k_min, first):
            yield (first,) + rest


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
    """K_{λ, μ}."""
    lam = [x for x in lam if x > 0]
    mu = list(mu)
    while mu and mu[-1] == 0: mu.pop()
    if sum(lam) != sum(mu): return 0
    if not dominance(mu, lam): return 0

    rows = len(lam)
    n = sum(lam)
    positions = [(i, jj) for i in range(rows) for jj in range(lam[i])]

    def count(pos_idx, filled, remain):
        if pos_idx == n:
            return 1
        i, jj = positions[pos_idx]
        total = 0
        min_val = 1
        if jj > 0:
            min_val = max(min_val, filled[(i, jj - 1)])
        if i > 0:
            min_val = max(min_val, filled[(i - 1, jj)] + 1)
        for v in range(min_val, len(mu) + 1):
            if remain[v - 1] > 0:
                filled[(i, jj)] = v
                remain[v - 1] -= 1
                total += count(pos_idx + 1, filled, remain)
                remain[v - 1] += 1
                del filled[(i, jj)]
        return total

    return count(0, {}, list(mu))


print()
print("=" * 90)
print("Systematic Kostka search: brute-force all mu partitions of n for small shapes.")
print("=" * 90)

# For each small shape, enumerate all partitions mu of n and check K_{lam, mu} == M_j.
for (a, b) in [(6, 5), (7, 6), (8, 5), (8, 7)]:
    if (a + b + c) % 2 != 0: continue
    lam = (a, b, c)
    n = sum(lam)
    print(f"\nlam = {lam}, n = {n}")

    # Compute Kostka for all mus of n, up to some cutoff.
    mu_to_k = {}
    for mu in gen_partitions(n):
        # Only consider mus with parts <= a (dominance necessary)
        if mu[0] > a: continue
        if len(mu) > n: continue
        k = kostka(list(lam), list(mu))
        if k > 0:
            mu_to_k[mu] = k

    print(f"  {len(mu_to_k)} nonzero Kostka numbers for lam.")
    for j in range(0, 6):
        target = Mtable.get((a, b, j))
        if target is None: continue
        matches = [mu for mu, k in mu_to_k.items() if k == target]
        # Trim to top 5 for readability
        display = matches[:5] if matches else []
        print(f"  j = {j}: M_j = {target}, {len(matches)} Kostka matches: {display}")
