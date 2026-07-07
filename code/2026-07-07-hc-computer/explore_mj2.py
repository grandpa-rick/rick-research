"""More attempts at M_j pattern."""
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
        return None
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


# Values to fit: M_j for (a=11, b=8, c=5), j=0..8
mj_data = [M_j_c5(11, 8, j) for j in range(9)]
print("M_j at (11,8,5):", mj_data)
# [292880896, 106646848, 38842688, 14146448, 5150016, 1873300, 680480, 246680, 89152]

# Try f^(a+t, b+t, c-2t) for various t
print("\nTest M_j against f^shifted-shape:")
for j in range(0, 6):
    mj = mj_data[j]
    tests = [
        (f"f^({11-j},{8-j},{5})", [11-j, 8-j, 5]),
        (f"f^({11+j},{8+j},{5-2*j})", [11+j, 8+j, 5-2*j] if 5-2*j >= 0 else None),
        (f"f^({11},{8},{5-j})", [11, 8, 5-j] if 5-j >= 0 else None),
        (f"f^({11-2*j},{8},{5+j})", [11-2*j, 8, 5+j] if 5+j <= 8 else None),
        (f"f^({11},{8-j},{5-j})", [11, 8-j, 5-j] if 5-j >= 0 else None),
    ]
    print(f"  j={j}: M_j={mj}")
    for name, sh in tests:
        if sh is not None and all(x >= 0 for x in sh):
            sh_sorted = sorted(sh, reverse=True)
            if all(sh_sorted[i] >= sh_sorted[i+1] for i in range(len(sh_sorted)-1)):
                f = hook_length(sh_sorted)
                if f == mj:
                    print(f"    MATCH: {name} = {f}")
                elif f is not None:
                    print(f"    {name} = {f}")

# Look at ratios M_j / M_{j+1}
print("\nRatios M_j / M_{j-1}:")
for j in range(1, 9):
    if mj_data[j-1] and mj_data[j]:
        r = mj_data[j-1] / mj_data[j]
        # Try to identify r as a rational number
        print(f"  M_{j-1}/M_{j} = {mj_data[j-1]}/{mj_data[j]} = {r:.6f}")


# Try: M_j = C(m-j, b-j) * something
print("\nCheck M_j / C(m-j, b-j):")
m = 12
for j in range(0, 6):
    binomial = C(m-j, 8-j)  # C(12-j, 8-j)
    if binomial != 0 and mj_data[j] is not None:
        r = mj_data[j] / binomial
        print(f"  j={j}: M_j={mj_data[j]}, C({m-j},{8-j})={binomial}, ratio={r:.6f}")


# Try: M_j = C(2(m-j), b-j) * something / j!
print("\nCheck M_j / C(2(m-j), b-j):")
for j in range(0, 6):
    binomial = C(24-2*j, 8-j)
    if binomial != 0 and mj_data[j] is not None:
        r = mj_data[j] / binomial
        print(f"  j={j}: M_j={mj_data[j]}, C({24-2*j},{8-j})={binomial}, ratio={r:.6f}")


# Try: M_j = C(2(m-j), b-j) * SYT count of two-row shape
print("\nCheck 2-row f^(?,?): compare to M_j / C(2(m-j), b-j)")
for j in range(0, 6):
    binomial = C(24-2*j, 8-j)
    if binomial and mj_data[j]:
        target = mj_data[j] // binomial if mj_data[j] % binomial == 0 else None
        # Search 2-row f^(p,q) with p+q = 24-2j
        target_size = 24 - 2*j
        if target is not None:
            for p in range(target_size + 1):
                q = target_size - p
                if q < 0 or q > p:
                    continue
                f = hook_length([p, q]) if q > 0 else hook_length([p])
                if f == target:
                    print(f"  j={j}: M_j/binom={target}, f^({p},{q}) = {f} MATCH!")
                    break
            else:
                if target < 10**10:
                    print(f"  j={j}: M_j/binom={target}, no 2-row match")


# Simplest test: is M_j a polynomial in a, b at fixed j (and c)?
# Yes, must be (since Q_5 and H_5 are polynomials). Let me look at the leading behavior.
print("\n=== M_j / j! ===")
for j in range(0, 9):
    if mj_data[j]:
        print(f"  j={j}: M_j = {mj_data[j]}, M_j/j! = {mj_data[j]/factorial(j):.4f}")


# What if M_j is: number of two-row tableaux of some sub-shape?
# Try M_j = C(2(m-j), b-j) * (a+c-j-b-j+1) * something
# Actually the classical formula for 2-row: f^(p,q) = (p-q+1)/(p+1) * C(p+q, q)
# So C(2(m-j), b-j) = C(p+q, q) with p = 2(m-j)-b+j = 2m-2j-b+j = 2m-b-j = a+c-j
#                                       q = b-j
# So C(2(m-j), b-j) = C(a+c-j+b-j, b-j) = C(a+b+c-2j, b-j)
# And (p-q+1) = (a+c-j) - (b-j) + 1 = a+c-b+1
# f^(a+c-j, b-j) = (a+c-b+1)/(a+c-j+1) * C(a+b+c-2j, b-j)

# So maybe M_j = f^(a+c-j, b-j, c-j) or f^(a+c-j, b-j) times something
# Let me test:
print("\n=== Test: M_j = f^(a+c-j, b-j)? (two-row) ===")
a, b, c = 11, 8, 5
for j in range(0, 6):
    p = a + c - j
    q = b - j
    if q < 0 or p < q:
        continue
    if q == 0:
        f = 1  # single row = 1 tableau
    else:
        f = hook_length([p, q])
    print(f"  j={j}: M_j={mj_data[j]}, f^({p},{q})={f}, ratio={mj_data[j]/f if f else 'inf'}")

print("\n=== Test: M_j / C(2(m-j), b-j) as SYT count ===")
for j in range(0, 9):
    if mj_data[j] is None:
        continue
    binomial = C(24-2*j, 8-j)
    if binomial == 0:
        continue
    if mj_data[j] % binomial != 0:
        print(f"  j={j}: M_j % C = {mj_data[j] % binomial} (not integer)")
        continue
    q = mj_data[j] // binomial
    print(f"  j={j}: M_j/C(24-2j,8-j) = {q}")
