"""Test whether M_0(a,b,c) = f^(a,b,c) from Clio's Lemma 1 for c=5.

If yes, and if H_c has a natural inverse expression via M_j and hook-length
numbers, we might be able to compute v_2(H_c(a,b,j)) without knowing H_c
explicitly for c != 5.

Sanity-check the M_0 = f^lambda identity at multiple (a, b, 5) shapes.
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


def hook_length(lam):
    """f^λ by hook-length formula."""
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


def M0_via_H5(a, b):
    """M_0(a, b, 5) via Clio's Lemma 1 (c=5)."""
    c = 5
    j = 0
    m = (a + b + c) // 2
    N = 2 * (m - j)
    Q5 = (a - 3) * (b - 4) * H5(a, b, j)  # C(0,10) = 0 so no tip term
    den = 120 * (a + 6 - j)
    for i in range(1, 6):
        den *= (b + i - j)
    num = C(N, b - j) * (a - b + 1) * Q5
    if num % den != 0:
        return None
    return num // den


# Sanity: Clio said f^(13,13,6) = 230,814,869,760. Verify via hook.
f_1313_6 = hook_length([13, 13, 6])
print(f"f^(13,13,6) = {f_1313_6}, Clio said 230,814,869,760, match={f_1313_6 == 230814869760}")


# Test M_0(a, b, 5) vs f^(a, b, 5)
print("\nTesting M_0(a, b, 5) vs f^(a, b, 5) for various (a, b):")
print(f"{'(a,b)':>10s} | {'f^(a,b,5)':>16s} | {'M_0(a,b,5)':>16s} | match")
print("-" * 65)
for a in range(5, 16):
    for b in range(5, min(a + 1, 12)):
        if (a + b + 5) % 2 != 0:
            continue
        try:
            f_lam = hook_length([a, b, 5])
        except Exception:
            continue
        M0 = M0_via_H5(a, b)
        match = "yes" if M0 == f_lam else "NO"
        print(f"{'(' + str(a) + ',' + str(b) + ')':>10s} | {f_lam:16d} | {str(M0):>16s} | {match}")


# If M_0 = f^lambda, we can back out v_2(H_5(a,b,0)) from f^lambda:
# H_5(a,b,0) = h_0(a,b) = (a+3)(a+4)(a+5)(a+6)(b+2)(b+3)(b+4)(b+5)
# So v_2(H_5(a,b,0)) is directly computable from the run products.
# The min over (a,b) at j=0 is:
print("\nmin v_2(H_5(a,b,0)) over a,b in [0,32]:")
min_v = min(v2(H5(a, b, 0)) for a in range(32) for b in range(32))
print(f"  = {min_v}  (compare to β'(5)=3; min over j > 0 gets lower)")


# CRUCIAL: v_2(f^lambda) = v_2 of a specific hook-length quotient.
# If M_0 = f^lambda and M_0 relates to H_5 via a fixed denominator/numerator,
# then v_2(f^lambda) = v_2(M_0) determines v_2(H_5(a,b,0)) up to known offsets.
# This lets us TEST whether the same trick works for c > 5:
# v_2(f^(a,b,c)) - correction = v_2(H_c(a,b,0))?
print("\nProbe: v_2(f^(a,b,c)) at (a,b,c) = (3, 0, c) for c=4..12:")
for c in range(4, 13):
    if (3 + 0 + c) % 2 != 0:
        print(f"  c={c}: skip (a+b+c odd)")
        continue
    try:
        f_lam = hook_length([3, 0, c]) if 0 <= c <= 3 else None
        # partition rows must be non-increasing >= 0; (3,0,c) with c > 3 is bad
        # so this isn't a valid shape. Use (3+c, c, c) or something instead.
        continue
    except Exception:
        continue

# Better probe: at c=5, β'(5) = 3 at (a,b,j)=(3,0,2). What's the corresponding
# partition and its f^λ?
# Actually the "shape" comment `λ=({a},{b},5)` means the partition is (a,b,c)
# with a,b,c the three rows. But (3,0,5) is not a partition (rows must be
# non-increasing). So (a,b) in Rick's H_5 code is NOT partition rows.
# It's just polynomial arguments.
print("\nRick's (a, b) in H_5 are polynomial args, not partition rows.")
print("So M_0 = f^λ identity uses different partition labeling.")
print("Cannot directly back out β' from f^λ without knowing the labeling.")
