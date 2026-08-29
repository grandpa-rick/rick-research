"""Day 101 — verify the key sublemmas and G3 inequalities for k = 4, 5, 6.

Main sublemma (X-carries): For X >= 1 and M >= 1 with e = v_2(M), nu = v_2(X):
    carries(X, 2M - 1) >= max(0, e - nu + 1).

Also, we derived:
    carries_b(b+1, 4m-3) = 1 + carries(b/2, 2m-1)  [for b even]
    carries_a(a+2, 4m-3) = 1 + carries((a+1)/2, 2m-1)  [for a odd]
    carries_a(a+2, 4m-3) = carries((a+2)/2, 2(m-1))  [for a even]
    carries_b(b+1, 4m-3) = carries((b+1)/2, 2(m-1))  [for b odd]

For k=5: L = 4m-4 = 4(m-1). Target v_2(S_5) + carries >= 4.
  v_2(term1) = 2 + T_1, v_2(term2) = 4 + e (exactly).
  Case A (T_1 <= 1+e): v_2(S_5) = 2 + T_1, need carries + T_1 >= 2. T_1 >= 2 always. Trivial.
  Case B (T_1 >= 3+e): v_2(S_5) >= 4+e >= 4. Trivial.
  Case R (T_1 = 2+e): v_2(S_5) >= 4+e >= 4. Trivial.
  Edge case: a=0=b (Case E) or a=b=1 (Case O): f_1 = 0, v_2(S_5) = 4+e. Trivial.

For k=6: L = 4m-5 = 4(m-2) + 3. Bits 0, 1 both = 1.
  v_2(Q_6) + carries >= 7 + e. v_2(Q_6) = 3+e + v_2(S_6). So need v_2(S_6) + carries >= 4.
  Claim: v_2(S_6) >= 3 always on shell. Then need carries >= 1.
  Shell: bit 0 chain gives carries >= 1. So closes.
"""

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

def s2(n):
    return bin(n).count('1') if n > 0 else 0

def carries(x, y):
    return s2(x) + s2(y) - s2(x + y)


print("=" * 78)
print("Sublemma X-carries: carries(X, 2M-1) >= max(0, v_2(M) - v_2(X) + 1)")
print("=" * 78)
fail = 0
tight_count = 0
for M in range(1, 40):
    e = v2(M)
    for X in range(1, 40):
        nu = v2(X)
        pred = max(0, e - nu + 1)
        actual = carries(X, 2*M - 1)
        if actual < pred:
            fail += 1
            if fail < 5:
                print(f"  FAIL: X={X}, M={M}, nu={nu}, e={e}: pred={pred}, actual={actual}")
        if actual == pred:
            tight_count += 1
print(f"  Grid X, M in [1, 40): {'ALL PASS' if fail == 0 else f'{fail} fails'}. Tight cases: {tight_count}")


# Verify carries formulas
print()
print("=" * 78)
print("carries_a and carries_b formulas at L = 4m-3 (k=4)")
print("=" * 78)
fail = 0
for m in range(1, 20):
    L = 4*m - 3
    if L < 1: continue
    for a in range(0, 32, 2):  # a even
        # carries_a(a+2, L) = carries((a+2)/2, 2(m-1))
        pred = carries((a+2)//2, 2*(m-1)) if m >= 1 else 0
        actual = carries(a+2, L)
        if actual != pred:
            fail += 1
            if fail < 3:
                print(f"  FAIL a even: m={m}, a={a}: pred={pred}, actual={actual}")
    for a in range(1, 32, 2):  # a odd
        # carries_a(a+2, L) = 1 + carries((a+1)/2, 2m-1)
        pred = 1 + carries((a+1)//2, 2*m - 1)
        actual = carries(a+2, L)
        if actual != pred:
            fail += 1
            if fail < 3:
                print(f"  FAIL a odd: m={m}, a={a}: pred={pred}, actual={actual}")
    for b in range(0, 32, 2):  # b even
        # carries_b(b+1, L) = 1 + carries(b/2, 2m-1)  [b=0 -> carries(0,...) = 0 -> total 1]
        pred = 1 + carries(b//2, 2*m - 1) if b >= 2 else 1
        actual = carries(b+1, L)
        # Note: for b=0, b/2=0, carries(0, 2m-1) = s_2(0) + s_2(2m-1) - s_2(2m-1) = 0
        pred = 1 + carries(b//2, 2*m - 1)
        if actual != pred:
            fail += 1
            if fail < 3:
                print(f"  FAIL b even: m={m}, b={b}: pred={pred}, actual={actual}")
    for b in range(1, 32, 2):  # b odd
        # carries_b(b+1, L) = carries((b+1)/2, 2(m-1))
        pred = carries((b+1)//2, 2*(m-1))
        actual = carries(b+1, L)
        if actual != pred:
            fail += 1
            if fail < 3:
                print(f"  FAIL b odd: m={m}, b={b}: pred={pred}, actual={actual}")
print(f"  {'ALL PASS' if fail == 0 else f'{fail} fails'}")


# --- k = 5 sanity check
print()
print("=" * 78)
print("k=5: Verify v_2(term1) = 2 + T_1, v_2(term2) = 4 + e, and target closure")
print("=" * 78)

def S5_val(a, b, m):
    A = a + 2
    B = b + 1
    term1 = 60 * A * B * (A - 1) * (B - 1)
    term2 = -16 * m * (2*m - 1) * (4*m - 1) * (10 * A * B - (2*m - 1) * (4*m - 3) * (4*m + 1))
    return term1 + term2

def v2_h5(a, b, c):
    m = (c - 2) // 4
    L = c - 1 - 5
    if L < 0: return None
    v2_Lfact = L - s2(L)
    v2_pocha = v2_Lfact + carries(a + 2, L)
    v2_pochb = v2_Lfact + carries(b + 1, L)
    v2_pre = v2(c) + v2(c - 1) + v2(c - 2) + v2(c - 3)
    S = S5_val(a, b, m)
    if S == 0:
        return None
    v2_Q = v2_pre + v2(S)
    return v2_pocha + v2_pochb + v2_Q

def target(c):
    m = (c - 2) // 4
    return 8*m + 1 - 2*s2(m) - v2(m)

fail = 0; oks = 0; tight = 0
for m in range(1, 30):
    c = 4*m + 2
    if c - 1 - 5 < 0: continue
    for a in range(0, 32):
        for b in range(0, 32):
            if (a + b) % 2 != 0: continue
            v = v2_h5(a, b, c)
            if v is None: continue
            if v < target(c):
                fail += 1
                if fail < 3:
                    print(f"  FAIL k=5: m={m}, a={a}, b={b}: v={v}, target={target(c)}")
            else:
                oks += 1
                if v == target(c): tight += 1
print(f"  k=5: {oks} pass, {fail} fail, {tight} tight")


# --- k = 6 direct verification: v_2(S_6) >= 3 always on shell?
print()
print("=" * 78)
print("k=6: Direct verification of v_2(S_6(a, b, c)) >= 3 on shell (a+b even)")
print("=" * 78)

def S6_val(a, b, c):
    """Compute S_6 = Q_6 / [-c(c-2)(c-1)]."""
    # From the polynomial in a, b, c:
    return (
        120*a**3*b**3 - 120*a**3*b + 360*a**2*b**3
        - 180*a**2*b**2*c**3 + 1800*a**2*b**2*c**2 - 5940*a**2*b**2*c + 6480*a**2*b**2
        - 180*a**2*b*c**3 + 1800*a**2*b*c**2 - 5940*a**2*b*c + 6120*a**2*b
        + 240*a*b**3
        - 540*a*b**2*c**3 + 5400*a*b**2*c**2 - 17820*a*b**2*c + 19440*a*b**2
        + 30*a*b*c**6 - 630*a*b*c**5 + 5430*a*b*c**4 - 25110*a*b*c**3 + 66900*a*b*c**2 - 98460*a*b*c + 62400*a*b
        + 30*a*c**6 - 630*a*c**5 + 5430*a*c**4 - 24570*a*c**3 + 61500*a*c**2 - 80640*a*c + 43200*a
        - 360*b**2*c**3 + 3600*b**2*c**2 - 11880*b**2*c + 12960*b**2
        + 60*b*c**6 - 1260*b*c**5 + 10860*b*c**4 - 49500*b*c**3 + 126600*b*c**2 - 173160*b*c + 99360*b
        - c**9 + 33*c**8 - 474*c**7 + 3942*c**6 - 21189*c**5 + 77157*c**4 - 191456*c**3 + 311988*c**2 - 300960*c + 129600
    )

min_v2_S6 = 10**9
min_config = None
for m in range(1, 30):
    c = 4*m + 2
    for a in range(0, 32):
        for b in range(0, 32):
            if (a + b) % 2 != 0: continue
            S = S6_val(a, b, c)
            if S == 0: continue
            vS = v2(S)
            if vS < min_v2_S6:
                min_v2_S6 = vS
                min_config = (m, a, b, S)
print(f"  Min v_2(S_6) on shell: {min_v2_S6} at (m, a, b, S) = {min_config}")

# Now verify k=6 target inequality (which requires v_2(S_6) + carries >= 4)
fail = 0; oks = 0
for m in range(1, 30):
    c = 4*m + 2
    L = c - 1 - 6
    if L < 0: continue
    v2_Lfact = L - s2(L)
    v2_pre = v2(c) + v2(c - 2) + v2(c - 1)  # from Q_6 = -c(c-2)(c-1) S_6
    for a in range(0, 32):
        for b in range(0, 32):
            if (a + b) % 2 != 0: continue
            S = S6_val(a, b, c)
            if S == 0: continue
            v2_Q = v2_pre + v2(S)
            ca = carries(a+2, L)
            cb = carries(b+1, L)
            v = 2*v2_Lfact + ca + cb + v2_Q
            if v < target(c):
                fail += 1
                if fail < 5:
                    print(f"  FAIL k=6: m={m}, a={a}, b={b}: v={v}, target={target(c)}, v_2(S_6)={v2(S)}, carries={ca+cb}")
            else:
                oks += 1
print(f"  k=6: {oks} pass, {fail} fail")
