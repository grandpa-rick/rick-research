"""
Day 93 — Digit-sum + floor model for beta'(c), version 2.

v1 result: no exact integer fit found in [-3,3]^k or [-4,4]^k for the
tested feature subsets. Best residual = 1. This suggests either
(i) the true model needs a wider coefficient range,
(ii) needs case work by c mod 4, OR
(iii) needs floor-like features (not pure digit sums).

Pattern observed in D(c) = beta(c) - beta'(c):
    c:  4  5  6  7  8  9  10 11
    D:  0  4  1  4  0  6  2  6

By c mod 4:
    c%4=0: D(4)=0, D(8)=0            [period-of-8 sees c=4-8 both 0]
    c%4=1: D(5)=4, D(9)=6            [+2 per 4-step]
    c%4=2: D(6)=1, D(10)=2           [+1 per 4-step]
    c%4=3: D(7)=4, D(11)=6           [+2 per 4-step]

Combined pattern:
    - odd c >= 5:      D(c) = 4 + 2*floor((c-1)/8)
    - c ≡ 0 mod 4:     D(c) = floor((c-4)/8)
    - c ≡ 2 mod 4:     D(c) = 1 + floor((c-6)/4)

Check UBs:
    c=12: predict 1;  UB=1                (β'=18)   TIGHT
    c=13: predict 6;  UB=6                (β'=16)   TIGHT
    c=15: predict 6;  UB<=5 (β'<=20, D>=5) LOOSE by 1
    c=17: predict 8;  UB=8                (β'=23)   TIGHT

So the piecewise formula is CONSISTENT with all UBs (D_pred <= UB gives β'_pred >= UB minus?
Actually: UB on β' gives LB on D. D_pred consistent iff D_pred >= D_LB.
    c=12: D_pred=1, D_LB=1   OK
    c=13: D_pred=6, D_LB=6   OK
    c=15: D_pred=6, D_LB=5   OK
    c=17: D_pred=8, D_LB=8   OK
ALL CONSISTENT — piecewise formula plausible at all c in {4..17}.

This script:
    1. Confirms the piecewise formula fits all 8 registered β'(c).
    2. Attempts to unify the three cases into a single formula.
    3. Tests: D(c) = 4*[c odd] + 2*floor((c-1)/8)*[c odd]
                    + floor((c-4)/8)*[c%4==0]
                    + (1 + floor((c-6)/4))*[c%4==2].
    4. Alternative: search for a smaller unified formula using digit
       sums of (c-1), (c-2), floor((c-1)/2) etc.
"""

import itertools
import numpy as np


def s2(n):
    return bin(n).count('1') if n > 0 else 0


def v2(n):
    if n <= 0: return 0
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


BETA_PRIME = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14, 11: 12}
BETA_PRIME_UB = {12: 18, 13: 16, 15: 20, 17: 23}


def beta_ambient(c):
    return 2 * (c - 1) - s2(c - 1)


def D_pred_piecewise(c):
    """Piecewise formula derived above."""
    if c % 2 == 1:  # odd
        return 4 + 2 * ((c - 1) // 8)
    elif c % 4 == 0:
        return (c - 4) // 8
    elif c % 4 == 2:
        return 1 + (c - 6) // 4
    else:
        raise ValueError


print("=" * 70)
print("Piecewise formula test on registered β'(c) at c ∈ {4..11}")
print("=" * 70)
print(f"{'c':>3} {'β(c)':>5} {'β_prime':>8} {'D_true':>7} {'D_pred':>7} {'match':>6}")
all_match = True
for c in sorted(BETA_PRIME.keys()):
    b, bp = beta_ambient(c), BETA_PRIME[c]
    D_true = b - bp
    D_pred = D_pred_piecewise(c)
    match = D_true == D_pred
    all_match = all_match and match
    print(f"{c:>3} {b:>5} {bp:>8} {D_true:>7} {D_pred:>7} {'YES' if match else 'NO':>6}")

print()
print(f"All 8 registered values match: {'YES' if all_match else 'NO'}")

print()
print("=" * 70)
print("UB consistency at c ∈ {12, 13, 15, 17}")
print("=" * 70)
print(f"{'c':>3} {'β(c)':>5} {'β_prime UB':>11} {'D_LB':>5} {'D_pred':>7} {'β_pred':>7} {'consistent':>11}")
all_ub_ok = True
for c in sorted(BETA_PRIME_UB.keys()):
    b, ub = beta_ambient(c), BETA_PRIME_UB[c]
    D_LB = b - ub  # UB on β' -> LB on D
    D_pred = D_pred_piecewise(c)
    bp_pred = b - D_pred
    consistent = bp_pred <= ub  # our predicted β' must be <= empirical UB
    all_ub_ok = all_ub_ok and consistent
    print(f"{c:>3} {b:>5} {ub:>11} {D_LB:>5} {D_pred:>7} {bp_pred:>7} "
          f"{'YES' if consistent else 'NO':>11}")

print()
print(f"All UBs consistent: {'YES' if all_ub_ok else 'NO'}")


# ============================================================
# ATTEMPTED UNIFICATION
# ============================================================
print()
print("=" * 70)
print("Attempted unified formula")
print("=" * 70)


# Formula A: D(c) uses features that vanish or scale by parity.
# Odd c contributes 4, even ≡ 2 mod 4 contributes 1, even ≡ 0 mod 4 contributes 0.
# These pattern as: floor((c mod 4 + 1) / 2)?
#   c mod 4 = 0 -> floor((0+1)/2) = 0
#   c mod 4 = 1 -> floor(2/2) = 1
#   c mod 4 = 2 -> floor(3/2) = 1
#   c mod 4 = 3 -> floor(4/2) = 2  (WRONG — odd c always gives 4)
# Odd contribution isn't 2*(mod4). Try:
#   parity indicator: 4*[c odd] + 1*[c ≡ 2 mod 4] + 0*[c ≡ 0 mod 4]
# The remaining growth term:
#   odd c: 2*floor((c-1)/8)
#   c ≡ 2 mod 4: floor((c-6)/4)   (grows +1 per 4-step)
#   c ≡ 0 mod 4: floor((c-4)/8)   (grows +1 per 8-step)
#
# floor((c-6)/4) at c ≡ 2 mod 4 is exactly (c-6)/4 = (c-2)/4 - 1 = k-1 where c=4k+2, so k = (c-2)/4.
# Growth: at c=6: k=1, gives 0; c=10: k=2, gives 1; c=14: k=3, gives 2.

def D_pred_variant_B(c):
    """Odd c and c ≡ 2 mod 4 have the SAME floor increment factor 2/8. If we
    force c ≡ 0 mod 4 to also match via floor((c-4)/8), that's the current
    piecewise formula. Try to unify: D(c) = base(c mod 4) + floor((c - offset(c mod 4)) / period(c mod 4))
    where the period differs by 2x for the c ≡ 2 mod 4 case."""
    return None


# ============================================================
# Alternative: search for unified formula with ONLY digit-sum features
# but wider coeff range.
# ============================================================
print()
print("Wider search: D(c) integer linear combo of extended features, coefs [-4, 4]")

CS = sorted(BETA_PRIME.keys())
targets = np.array([beta_ambient(c) - BETA_PRIME[c] for c in CS])

def extended_features(c):
    return {
        'c': c,
        'c%4==0': int(c % 4 == 0),
        'c%4==1': int(c % 4 == 1),
        'c%4==2': int(c % 4 == 2),
        'c%4==3': int(c % 4 == 3),
        's2(c)': s2(c),
        's2(c-1)': s2(c-1),
        's2(c-1)//8': (c-1)//8,
        '(c-4)//8': max((c-4)//8, 0),
        '(c-6)//4': max((c-6)//4, 0),
        'floor(c/4)': c // 4,
        'floor((c-1)/4)': (c-1) // 4,
        'floor((c-1)/8)': (c-1) // 8,
        'v2(c-1)': v2(c-1),
        's2(cm1_div_2)': s2((c-1)//2),
        's2(cm1_div_4)': s2((c-1)//4),
    }

SUBSETS = [
    ['c%4==1', 'c%4==3', 'c%4==2', 'floor((c-1)/8)'],
    ['c%4==1', 'c%4==3', 'c%4==2', '(c-4)//8', 'floor((c-1)/8)'],
    ['c%4==1', 'c%4==3', 'c%4==2', 'floor((c-1)/8)', '(c-4)//8', '(c-6)//4'],
    ['c%4==1', 'c%4==3', 'v2(c-1)', 'floor((c-1)/8)', '(c-6)//4'],
]

# For each subset, brute-force integer coefs in [-4, 4]
RANGE = range(-4, 5)
exact_hits = []
for feats in SUBSETS:
    F = np.array([[extended_features(c)[f] for f in feats] + [1] for c in CS])
    n = len(feats) + 1
    if 9 ** n > 5_000_000:  # skip huge
        print(f"  (skip {feats}: too large search space {9**n})")
        continue
    for coefs in itertools.product(RANGE, repeat=n):
        pred = F @ np.array(coefs)
        if np.all(pred == targets):
            exact_hits.append((feats, coefs))
            print(f"  EXACT: coefs = {dict(zip(feats + ['const'], coefs))}")

if not exact_hits:
    print("  No exact fit found in [-4,4]^k on tested subsets.")

# ============================================================
# FINAL: write out and verify the winning piecewise formula
# ============================================================
print()
print("=" * 70)
print("Extrapolation: β'(c) via piecewise formula, c = 4..25")
print("=" * 70)
print(f"{'c':>3} {'β(c)':>5} {'D_pred':>7} {'β_pred':>7} {'known/UB':>18}")
for c in range(4, 26):
    b = beta_ambient(c)
    D_pred = D_pred_piecewise(c)
    bp_pred = b - D_pred
    note = ''
    if c in BETA_PRIME:
        note = f"known={BETA_PRIME[c]}, {'OK' if bp_pred == BETA_PRIME[c] else 'BAD'}"
    elif c in BETA_PRIME_UB:
        note = f"UB<={BETA_PRIME_UB[c]}, {'OK' if bp_pred <= BETA_PRIME_UB[c] else 'BAD'}"
    print(f"{c:>3} {b:>5} {D_pred:>7} {bp_pred:>7} {note:>18}")
