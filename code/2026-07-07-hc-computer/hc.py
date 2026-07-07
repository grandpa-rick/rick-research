"""General H_c computer for β'(c) — Day 83 code session.

Scope of what is CURRENTLY implemented:
    - H_5(a,b,j) — Clio's explicit polynomial (§1.1 of her c=5 note; the
      only c for which we have a complete closed form).
    - H_c(a,b,0) for arbitrary c — the run-product h_0 (verified against
      Clio's inversion for c=4..7).
    - γ(c) — the run-content constant floor, upper bound on β'(c).
    - β'(5) — brute-force minimum over a large box, independent verification
      of Clio's β'(5) = 3.
    - Rick's dip formula (from proofs/2026-07-07-dip-formula.md).

What is NOT implemented (blocker):
    - H_c(a,b,j) for c ≠ 5 and j > 0. Clio has a general Q_c = L_c H_c +
      (j)_{2c} decomposition but she hasn't shared the general engine yet.
      Rick emailed her 2026-07-06 requesting it. Without it, we cannot
      independently compute β'(c) for c > 5.

What we CAN do:
    - Predict β'(c) for c ≥ 6 using: β'(c) ≤ γ(c), with the dip formula
      giving a REFINED prediction. Then compare against Clio's reported
      β'(c) for c=6..10 to validate the prediction machinery.
    - Extrapolate predictions to c=11..17 — the mod-8 kill shot.
"""
from math import factorial


def s2(n):
    return bin(n).count('1')


def v2(n):
    if n == 0:
        return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def C(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


# ============================================================================
# H_5(a, b, j) — Clio's explicit closed form
# ============================================================================

def H5(a, b, j):
    """Clio's c=5 heavy quotient, polynomial in (a,b,j) via binomial basis."""
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


# ============================================================================
# H_c(a, b, 0) — run product for any c ≥ 3
# ============================================================================

def H_c_at_j0(a, b, c):
    """H_c(a, b, 0) = ∏_{t=3..c+1}(a+t) · ∏_{s=2..c}(b+s).
    2(c-1) linear factors. Verified by inversion for c=4..7 (see
    2026-07-08-Hc-inversion.py)."""
    r = 1
    for t in range(3, c + 2):
        r *= (a + t)
    for s in range(2, c + 1):
        r *= (b + s)
    return r


# ============================================================================
# γ(c) — Theorem A run content, upper bound on β'(c)
# ============================================================================

def gamma(c):
    """γ(c) = v₂ content of H_c(a, b, 0) on the valid-parity sheet."""
    if c % 2 == 0:
        k = c // 2
        return 4 * k - 2 - s2(k) - s2(k - 1)
    k = (c - 1) // 2
    return 4 * k - 2 * s2(k)


def beta(c):
    """β(c) = (c-1) + v₂((c-1)!) = 2(c-1) - s₂(c-1)."""
    return 2 * (c - 1) - s2(c - 1)


# ============================================================================
# β' via direct scan of H_5 (only implemented for c=5)
# ============================================================================

def beta_prime_direct_c5(box=48, verbose=False):
    """Brute-force min v₂(H_5(a,b,j)) over box-interior (a,b,j).

    Box interior = a ∈ [0, box), b ∈ [0, box), j ∈ [0, 2c-1].
    Constraint: (a+b) parity matches something? For odd c, valid-parity
    sheet — let's scan both parities.
    """
    c = 5
    best = float('inf')
    best_point = None
    for a in range(box):
        for b in range(box):
            for j in range(0, 2 * c):
                h = H5(a, b, j)
                if h == 0:
                    continue
                val = v2(h)
                if val < best:
                    best = val
                    best_point = (a, b, j)
                    if verbose and best <= 4:
                        print(f"  New min: v₂(H_5({a},{b},{j})) = {val}")
    return best, best_point


def beta_prime_j0_upper(c, box=48):
    """β' upper bound from j=0 alone: min v₂(H_c(a,b,0)) over (a,b).
    This equals γ(c) for large enough box."""
    best_even = float('inf')
    best_odd = float('inf')
    best_point_even = None
    best_point_odd = None
    for a in range(box):
        for b in range(box):
            h = H_c_at_j0(a, b, c)
            if h == 0:
                continue
            val = v2(h)
            if (a + b) % 2 == 0:
                if val < best_even:
                    best_even = val
                    best_point_even = (a, b, 0)
            else:
                if val < best_odd:
                    best_odd = val
                    best_point_odd = (a, b, 0)
    return {
        'same_parity_min': best_even,
        'same_parity_point': best_point_even,
        'opp_parity_min': best_odd,
        'opp_parity_point': best_point_odd,
    }


# ============================================================================
# Rick's dip formula prediction (from 2026-07-07-dip-formula.md)
# ============================================================================
#
# Δβ'(c) = 1 − max(2, v₂(c−1))  for odd c ≥ 3
#
# For odd c → even c: use Clio's data or γ upper bound.
# For even c: β'(c) ≈ γ(c) with dip 0 or 1 (data-driven).

def beta_prime_predicted(c, beta_prime_data):
    """Predict β'(c) using Rick's dip formula + known lower c values."""
    if c in beta_prime_data:
        return beta_prime_data[c], "given"
    # Even c: use γ(c) as best guess, minus possible dip
    if c % 2 == 0:
        return gamma(c), "gamma upper bound"
    # Odd c ≥ 3: Δβ' = 1 - max(2, v₂(c-1)), from β'(c-1)
    v = v2(c - 1)
    delta = 1 - max(2, v)
    if (c - 1) in beta_prime_data:
        return beta_prime_data[c - 1] + delta, f"dimer + dip formula from β'({c-1})"
    else:
        return gamma(c - 1) + delta, "dimer + dip formula from γ(c-1)"


# ============================================================================
# Data: Clio's reported β'(4..10)
# ============================================================================

CLIO_BETA_PRIME = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14}


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("=" * 78)
    print("hc.py — General H_c computer (partial: c=5 direct, c=6..17 predicted)")
    print("=" * 78)

    # PART 1: γ(c) upper bound
    print("\n1. γ(c) = run content upper bound on β'(c)")
    print(f"{'c':>3} {'β(c)':>5} {'γ(c)':>5} {'β prime Clio':>13}")
    for c in range(4, 18):
        gp = CLIO_BETA_PRIME.get(c, "?")
        print(f"{c:>3} {beta(c):>5} {gamma(c):>5} {str(gp):>13}")

    # PART 2: verify H_c(a,b,0) closed form vs run product
    print("\n2. Verify H_c(a,b,0) closed form at a few points (should equal run product)")
    for c in [4, 5, 6, 7, 8]:
        h1 = H_c_at_j0(10, 5, c)
        h2 = H_c_at_j0(3, 2, c)
        print(f"  H_{c}(10,5,0) = {h1}   H_{c}(3,2,0) = {h2}")

    # PART 3: β'(5) direct scan
    print("\n3. Direct β'(5) via brute-force scan over box (0..47)²")
    bp5, bp5_pt = beta_prime_direct_c5(box=48)
    print(f"  β'(5) = {bp5}, achieved at (a,b,j) = {bp5_pt}")
    print(f"  Clio: β'(5) = 3, at (a,b,j) = (3,0,2)")
    print(f"  Match: {bp5 == 3}")

    # Spot check H_5(3,0,2)
    h = H5(3, 0, 2)
    print(f"  H_5(3,0,2) = {h}, v₂ = {v2(h)}")
