"""Explore M_j structure: compute M_j from Clio's H_5 formula for many (a,b,j)
and try to identify a combinatorial interpretation.

Hypothesis to test: M_j = f^μ for some j-shifted shape μ derived from (a,b,c).
"""
from math import factorial


def C(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def hook_length(lam):
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    if any(lam[i] < lam[i+1] for i in range(len(lam)-1)):
        return None  # not a partition
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


def M_j_c5(a, b, j):
    """Clio's c=5 closed form."""
    m2 = a + b + 5
    if m2 % 2 != 0:
        return None
    m = m2 // 2
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


# STEP 1: Compute M_j for many (a, b, j) and print
print("=" * 78)
print("M_j values (c=5) — looking for combinatorial pattern")
print("=" * 78)

# Try shape (a,b,5) = (11, 8, 5): a+b+c = 24, even
a, b, c = 11, 8, 5
print(f"\n(a,b,c) = ({a},{b},{c}), size = {a+b+c}, m = {(a+b+c)//2}")
print(f"f^({a},{b},{c}) = {hook_length([a,b,c])} (should equal M_0)")
print(f"{'j':>3} | {'M_j':>15} | ratio M_j/M_0")
prev = None
for j in range(0, 10):
    mj = M_j_c5(a, b, j)
    if mj is None:
        print(f"{j:>3} | undefined")
        continue
    ratio = mj / M_j_c5(a, b, 0) if M_j_c5(a, b, 0) else 0
    print(f"{j:>3} | {mj:>15} | {ratio:.6f}")


# STEP 2: Test hypothesis M_j = f^(a-j, b-j, c)
print("\n" + "=" * 78)
print("Hypothesis: M_j = f^(a-j, b-j, c)?")
print("=" * 78)
a, b, c = 11, 8, 5
for j in range(0, 6):
    mj = M_j_c5(a, b, j)
    try:
        f_shifted = hook_length([a-j, b-j, c])
    except:
        f_shifted = None
    print(f"j={j}: M_j = {mj}, f^({a-j},{b-j},{c}) = {f_shifted}, "
          f"ratio = {mj/f_shifted if f_shifted else 'N/A'}")


# STEP 3: Test hypothesis M_j = f^(a, b, c-2j)
print("\n" + "=" * 78)
print("Hypothesis: M_j = f^(a, b, c-2j)?")
print("=" * 78)
for j in range(0, 3):
    mj = M_j_c5(a, b, j)
    try:
        f_shifted = hook_length([a, b, c - 2*j])
    except:
        f_shifted = None
    print(f"j={j}: M_j = {mj}, f^({a},{b},{c-2*j}) = {f_shifted}")


# STEP 4: Test hypothesis M_j = f^(a-j, b, c-j)
print("\n" + "=" * 78)
print("Hypothesis: M_j = f^(a-j, b, c-j)? (row shifts distributed)")
print("=" * 78)
for j in range(0, 6):
    mj = M_j_c5(a, b, j)
    try:
        parts = sorted([a-j, b, c-j], reverse=True)
        if all(p >= 0 for p in parts):
            f_shifted = hook_length(parts)
        else:
            f_shifted = None
    except:
        f_shifted = None
    print(f"j={j}: M_j = {mj}, f^({a-j},{b},{c-j}) = {f_shifted}")


# STEP 5: More flexible search: try various shapes with n = a+b+c-2j (constant descent)
print("\n" + "=" * 78)
print("Search: shape sizes = a+b+c - 2j (removing 2j boxes each step)")
print("=" * 78)
n_full = a + b + c  # 24
# Look at M_j and check if it factors as combination of SYT counts
for j in [1, 2, 3]:
    mj = M_j_c5(a, b, j)
    target_size = n_full - 2*j
    print(f"j={j}: M_j = {mj}, target 3-row shape size {target_size}")
    # Enumerate 3-row shapes (p, q, r) with p >= q >= r >= 0, p+q+r = target_size
    for p in range(target_size + 1):
        for q in range(min(p, target_size - p) + 1):
            r = target_size - p - q
            if r < 0 or r > q:
                continue
            f = hook_length([p, q, r]) if r > 0 else hook_length([p, q]) if q > 0 else hook_length([p])
            if f == mj:
                print(f"    MATCH: f^({p},{q},{r}) = {f}")
