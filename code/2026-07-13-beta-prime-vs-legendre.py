"""
Day 93 — β'(c) vs elementary Legendre LB.

Per CODE.md secondary: check β'(c) vs 2·v_2((c-1)!) + v_2(c) + v_2(c-1).
This is a proposed F2/LB_1 formula. If β'(c) − LB has a clean pattern,
that pattern is where c-uniformity of β'(c) hides.

Also compare to 2·v_2((c-2)!) + v_2(c) + v_2(c-1) (F2 as per registry).

By Legendre, v_2(n!) = n − s_2(n).
"""

from math import factorial


def s2(n):
    return bin(n).count('1') if n > 0 else 0


def v2(n):
    if n == 0: return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def v2_factorial(n):
    """v_2(n!) = n − s_2(n) via Legendre."""
    if n <= 0: return 0
    return n - s2(n)


BETA_PRIME = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14, 11: 12}
BETA_PRIME_UB = {12: 18, 13: 16, 15: 20, 17: 23}


def beta_ambient(c):
    return 2 * (c - 1) - s2(c - 1)


def LB_F2_c_minus_1(c):
    """2·v_2((c-1)!) + v_2(c) + v_2(c-1)."""
    v2c = v2(c) if c % 2 == 0 else 0
    v2cm1 = v2(c - 1) if (c - 1) % 2 == 0 else 0
    return 2 * v2_factorial(c - 1) + v2c + v2cm1


def LB_F2_c_minus_2(c):
    """2·v_2((c-2)!) + v_2(c) + v_2(c-1)  (registry: F2 = LB_1)."""
    v2c = v2(c) if c % 2 == 0 else 0
    v2cm1 = v2(c - 1) if (c - 1) % 2 == 0 else 0
    return 2 * v2_factorial(c - 2) + v2c + v2cm1


print("=" * 78)
print("β'(c) vs Legendre-based LB candidates")
print("=" * 78)
print(f"{'c':>3} {'β(c)':>5} {'β_prime':>8} {'LB_F2(c-1)':>11} {'LB_F2(c-2)':>11} "
      f"{'β-LB(c-1)':>10} {'β_prime-LB(c-1)':>15} {'β_prime-LB(c-2)':>15}")
for c in sorted(set(list(BETA_PRIME.keys()) + list(BETA_PRIME_UB.keys()))):
    b = beta_ambient(c)
    bp = BETA_PRIME.get(c, None)
    bp_ub = BETA_PRIME_UB.get(c, None)
    lb1 = LB_F2_c_minus_1(c)
    lb2 = LB_F2_c_minus_2(c)
    if bp is not None:
        print(f"{c:>3} {b:>5} {bp:>8} {lb1:>11} {lb2:>11} "
              f"{b-lb1:>10} {bp-lb1:>15} {bp-lb2:>15}")
    else:
        print(f"{c:>3} {b:>5} {'<=' + str(bp_ub):>8} {lb1:>11} {lb2:>11} "
              f"{b-lb1:>10} "
              f"{('<=' + str(bp_ub-lb1)):>15} "
              f"{('<=' + str(bp_ub-lb2)):>15}")

# ============================================================
# Now the piecewise formula found in v2 fit
# ============================================================
print()
print("=" * 78)
print("β'(c) piecewise formula vs the elementary LBs")
print("=" * 78)


def D_pred(c):
    if c % 2 == 1:
        return 4 + 2 * ((c - 1) // 8)
    elif c % 4 == 0:
        return (c - 4) // 8
    else:  # c % 4 == 2
        return 1 + (c - 6) // 4


print(f"{'c':>3} {'β(c)':>5} {'D_pred':>7} {'β_pred':>7} {'LB_F2':>7} {'gap':>6} "
      f"{'c mod 4':>8}")
for c in range(4, 30):
    b = beta_ambient(c)
    D = D_pred(c)
    bp_pred = b - D
    lb1 = LB_F2_c_minus_1(c)
    gap = bp_pred - lb1
    print(f"{c:>3} {b:>5} {D:>7} {bp_pred:>7} {lb1:>7} {gap:>6} {c%4:>8}")

# ============================================================
# Compute β' − LB_F2(c-2) for the F2/LB_1 setting per registry
# ============================================================
print()
print("β'(c) − 2·v_2((c-2)!) at registered c:")
for c in sorted(BETA_PRIME.keys()):
    bp = BETA_PRIME[c]
    lb = 2 * v2_factorial(c - 2)
    print(f"  c={c}: β'={bp}, 2·v_2((c-2)!)={lb}, diff={bp - lb}")

print()
print("β'(c) − β(c-1) at registered c (dimer-law residual):")
for c in sorted(BETA_PRIME.keys()):
    if c - 1 < 3: continue
    bp = BETA_PRIME[c]
    bcm1 = beta_ambient(c - 1)
    print(f"  c={c}: β'({c})={bp}, β({c-1})={bcm1}, diff={bp - bcm1}")

# ============================================================
# β' via digit-sum recomposition of piecewise formula
# ============================================================
# The piecewise formula for D can be recast:
#   D(c) = odd(c) * (4 + 2*floor((c-1)/8))
#        + [c%4==2] * (1 + floor((c-6)/4))
#        + [c%4==0] * floor((c-4)/8)
#
# floor((c-1)/8) counts the number of powers of 2^3 that fit in c-1.
# It IS related to digit sums, but obliquely: floor((c-1)/8) has recursion
#   floor((c-1)/8) = s_2(c-1) - s_2((c-1) mod 8) if you extract just the
#   number of "set bits above position 3".
# We do NOT get a pure s_2 formula, but the floor is a proxy for
#   (c - low_3_bits(c)) / 8.
print()
print("Cross-check: floor((c-1)/8) via digit decomposition")
for c in range(4, 25):
    high_bits = (c - 1) >> 3
    low_3 = (c - 1) & 7
    print(f"  c={c}: (c-1)={c-1:>6b} = {(c-1)>>3:>3}*8 + {low_3}, "
          f"floor/8={high_bits}, s_2(c-1)={s2(c-1)}, s_2((c-1)>>3)={s2(high_bits)}")
