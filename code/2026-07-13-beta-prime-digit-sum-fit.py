"""
Day 93 — Digit-sum model for beta'(c).

Iverson 2603.11069 template: v_3(sum C(n,r)^3 * 2^r) = digit-sum formula.
Rowland-Yassawi (arXiv:1505.02302): v_p(Q(c)) for polynomial Q either periodic
or unbounded — kills the five polynomial-in-c fits (D1, D2, D2', E, F1).

So model beta'(c) as a digit-sum expression, not a polynomial.

INPUT DATA — from proofs/registry/beta-prime-mod8.json (verified against source):
    c:   4  5  6  7  8  9  10 11
    b':  4  3  7  6  11 9  14 12

UPPER BOUNDS (checked-sober, from Day-92 witness scan):
    c=12: b' <= 18
    c=13: b' <= 16
    c=15: b' <= 20
    c=17: b' <= 23

NOTE: CODE.md's transcription (b'(c) = c+3) was WRONG. Registry is canonical.
Rick's Day-88 meta-rule: don't fit against a wrong table.
"""

import itertools
import numpy as np
from math import comb


def s2(n):
    """Binary digit sum."""
    return bin(n).count('1')


def v2(n):
    """2-adic valuation."""
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


# ============================================================
# INPUT DATA — from registry
# ============================================================
BETA_PRIME = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14, 11: 12}
BETA_PRIME_UB = {12: 18, 13: 16, 15: 20, 17: 23}


def beta_ambient(c):
    """beta(c) = 2(c-1) - s_2(c-1) — Rick's Kummer floor (registered proved)."""
    return 2 * (c - 1) - s2(c - 1)


# ============================================================
# Feature table
# ============================================================

def features(c):
    """Return dict of digit-sum / valuation features at c."""
    return {
        'c':          c,
        's2(c)':      s2(c),
        's2(c-1)':    s2(c-1),
        's2(c+1)':    s2(c+1),
        's2(c-2)':    s2(c-2) if c >= 2 else 0,
        'v2(c)':      v2(c) if c % 2 == 0 else 0,
        'v2(c-1)':    v2(c-1) if (c-1) % 2 == 0 else 0,
        's2(cm1_div_4)':  s2((c-1)//4) if c >= 1 else 0,
        's2(c_choose_2)': s2(c*(c-1)//2),
        # Iverson-style: s_2(m) - m appears via Legendre v_2(m!) = m - s_2(m).
        # For sum C(n,r)^k a^r style valuations, expect terms like
        # k*(s_2(r) + s_2(n-r) - s_2(n)) = k * (# carries in r+(n-r) base 2).
        # For our beta', see if s_2(c-1) - s_2(floor((c-1)/2)) helps.
        's2(c-1)-s2((c-1)//2)': s2(c-1) - s2((c-1)//2),
        's2(c) mod 2': s2(c) % 2,
        # c mod 4 indicator flags
        'c%4==0': int(c % 4 == 0),
        'c%4==1': int(c % 4 == 1),
        'c%4==2': int(c % 4 == 2),
        'c%4==3': int(c % 4 == 3),
    }


CS = sorted(BETA_PRIME.keys())
print("=" * 70)
print("Registry beta'(c) table (canonical)")
print("=" * 70)
print(f"{'c':>3} {'beta(c)':>8} {'beta_prime':>11} {'D(c)':>6} " +
      ' '.join(f"{k:>18}" for k in features(4).keys()))
for c in CS:
    b = beta_ambient(c)
    bp = BETA_PRIME[c]
    D = b - bp
    feats = features(c)
    print(f"{c:>3} {b:>8} {bp:>11} {D:>6} " +
          ' '.join(f"{v:>18}" for v in feats.values()))

print()
print(f"{'c (UB)':>6} {'beta(c)':>8} {'b_prime_UB':>11} {'D_lower':>8}")
for c in sorted(BETA_PRIME_UB.keys()):
    b = beta_ambient(c)
    bp_ub = BETA_PRIME_UB[c]
    D_lower = b - bp_ub  # UB on b' -> LB on D
    print(f"{c:>6} {b:>8} {bp_ub:>11} {D_lower:>8}")

# ============================================================
# FIT: search integer linear combinations of features
# ============================================================
# Model:  D(c) = sum_i alpha_i * f_i(c)  +  const
# Fit over c in {4..11} (8 data points). Coefficients in [-3, 3].

print()
print("=" * 70)
print("Fit D(c) as integer linear combo of features (coeffs in [-3, 3])")
print("=" * 70)

# Choose small feature subsets and search integer coefficients.
FEATURE_SUBSETS = [
    ['s2(c)', 's2(c-1)'],
    ['s2(c)', 's2(c-1)', 's2(c+1)'],
    ['s2(c)', 's2(c-1)', 'v2(c-1)'],
    ['s2(c-1)', 'v2(c-1)'],
    ['s2(c-1)-s2((c-1)//2)', 'v2(c-1)'],
    ['s2(cm1_div_4)', 'v2(c-1)'],
    ['s2(cm1_div_4)', 's2(c-1)', 'v2(c-1)'],
    ['s2(c-1)', 's2(c+1)', 'v2(c-1)'],
    ['s2(c_choose_2)', 's2(c)'],
    ['c%4==1', 'c%4==3', 'v2(c-1)'],
    ['c%4==0', 'c%4==1', 'c%4==2', 'c%4==3', 'v2(c-1)'],
    ['c%4==1', 'c%4==3', 'v2(c-1)', 's2(cm1_div_4)'],
]

RANGE = range(-3, 4)  # -3..3 inclusive

D_data = {c: beta_ambient(c) - BETA_PRIME[c] for c in CS}
targets = np.array([D_data[c] for c in CS])

best_fits = []

for feats_used in FEATURE_SUBSETS:
    n_coefs = len(feats_used) + 1  # +1 for constant term
    F = np.array([[features(c)[f] for f in feats_used] + [1] for c in CS])
    exact_hits = []
    # brute-force integer coefficient search
    for coefs in itertools.product(RANGE, repeat=n_coefs):
        pred = F @ np.array(coefs)
        residuals = targets - pred
        if np.all(residuals == 0):
            exact_hits.append(coefs)
    if exact_hits:
        for coefs in exact_hits:
            print(f"  EXACT FIT: {dict(zip(feats_used + ['const'], coefs))}")
            best_fits.append((feats_used, coefs))

if not best_fits:
    print("  No exact integer fit found in [-3,3]^k for the tested subsets.")
    print()
    print("  Best least-squares fits (real coefficients, subset by subset):")
    for feats_used in FEATURE_SUBSETS:
        F = np.array([[features(c)[f] for f in feats_used] + [1] for c in CS], dtype=float)
        sol, res, rank, sv = np.linalg.lstsq(F, targets.astype(float), rcond=None)
        pred = F @ sol
        max_res = np.max(np.abs(targets - pred))
        rounded = np.round(sol).astype(int)
        pred_r = F @ rounded
        max_res_int = int(np.max(np.abs(targets - pred_r)))
        print(f"    {feats_used}: lstsq coefs={sol.round(3).tolist()}, "
              f"max_res={max_res:.3f}; rounded={rounded.tolist()}, "
              f"max_res_int={max_res_int}")

# ============================================================
# FIT: search DIRECTLY for beta'(c), not D(c)
# ============================================================
print()
print("=" * 70)
print("Fit beta'(c) directly as integer linear combo of features")
print("=" * 70)

bp_targets = np.array([BETA_PRIME[c] for c in CS])

# Include a wider set of atomic features here; add multiples of c.
BP_FEATURE_SUBSETS = [
    ['c', 's2(c)'],
    ['c', 's2(c-1)'],
    ['c', 's2(c)', 's2(c-1)'],
    ['c', 's2(c-1)', 's2(c+1)'],
    ['c', 's2(c)', 'v2(c-1)'],
    ['c', 's2(c-1)', 'v2(c-1)'],
    ['c', 's2(c)', 's2(c-1)', 'v2(c-1)'],
    ['c', 's2(c-1)-s2((c-1)//2)'],
    ['c', 's2(cm1_div_4)', 'v2(c-1)'],
    ['c', 's2(cm1_div_4)', 's2(c-1)'],
    ['c', 's2(cm1_div_4)'],
]

BP_RANGE = range(-4, 5)  # -4..4 inclusive

exact_bp_fits = []
for feats_used in BP_FEATURE_SUBSETS:
    n_coefs = len(feats_used) + 1
    F = np.array([[features(c)[f] for f in feats_used] + [1] for c in CS])
    for coefs in itertools.product(BP_RANGE, repeat=n_coefs):
        pred = F @ np.array(coefs)
        if np.all(bp_targets - pred == 0):
            exact_bp_fits.append((feats_used, coefs))
            print(f"  EXACT FIT: beta'(c) = " +
                  ' + '.join(f"{coefs[i]}*{feats_used[i]}" for i in range(len(feats_used))) +
                  f" + {coefs[-1]}")

if not exact_bp_fits:
    print("  No exact integer fit found in [-4,4]^k for the tested subsets on beta'(c) directly.")
    for feats_used in BP_FEATURE_SUBSETS:
        F = np.array([[features(c)[f] for f in feats_used] + [1] for c in CS], dtype=float)
        sol, res, rank, sv = np.linalg.lstsq(F, bp_targets.astype(float), rcond=None)
        pred = F @ sol
        max_res = np.max(np.abs(bp_targets - pred))
        rounded = np.round(sol).astype(int)
        pred_r = F @ rounded
        max_res_int = int(np.max(np.abs(bp_targets - pred_r)))
        print(f"    {feats_used}: lstsq coefs={sol.round(3).tolist()}, "
              f"max_res={max_res:.3f}; rounded={rounded.tolist()}, "
              f"max_res_int={max_res_int}")


# ============================================================
# Consistency check against UBs
# ============================================================
if exact_bp_fits:
    print()
    print("=" * 70)
    print("UB consistency check for exact beta'(c) fits at c=12,13,15,17")
    print("=" * 70)
    for feats_used, coefs in exact_bp_fits:
        preds_ub = {}
        for c in sorted(BETA_PRIME_UB.keys()):
            pred = sum(coefs[i] * features(c)[feats_used[i]] for i in range(len(feats_used))) + coefs[-1]
            preds_ub[c] = pred
        formula = ' + '.join(f"{coefs[i]}*{feats_used[i]}" for i in range(len(feats_used))) + f" + {coefs[-1]}"
        print(f"\n  Formula: beta'(c) = {formula}")
        all_ok = True
        for c in sorted(BETA_PRIME_UB.keys()):
            ub = BETA_PRIME_UB[c]
            pred = preds_ub[c]
            ok = pred <= ub
            all_ok = all_ok and ok
            flag = "OK" if ok else "FAIL"
            print(f"    c={c}: predict {pred}, UB={ub}  [{flag}]")
        print(f"  Overall UB consistency: {'PASS' if all_ok else 'FAIL'}")

if exact_bp_fits:
    print()
    print("=" * 70)
    print("Extrapolation to c=12..17 (for future reference)")
    print("=" * 70)
    for feats_used, coefs in exact_bp_fits:
        formula = ' + '.join(f"{coefs[i]}*{feats_used[i]}" for i in range(len(feats_used))) + f" + {coefs[-1]}"
        print(f"\n  Formula: beta'(c) = {formula}")
        for c in range(4, 20):
            pred = sum(coefs[i] * features(c)[feats_used[i]] for i in range(len(feats_used))) + coefs[-1]
            known = ''
            if c in BETA_PRIME:
                known = f"  (known: {BETA_PRIME[c]}, {'OK' if pred == BETA_PRIME[c] else 'MISMATCH'})"
            elif c in BETA_PRIME_UB:
                known = f"  (UB: <={BETA_PRIME_UB[c]}, {'OK' if pred <= BETA_PRIME_UB[c] else 'FAIL'})"
            print(f"    c={c}: {pred}{known}")
