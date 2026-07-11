"""Day 89 Stage B — 2^T=11 periodicity check for h_k^{(c=8)}(a, b).

Prove: for each k in {0, 1, ..., 15} and each (a, b) with a+b even,
  v_2(h_k^{(c=8)}(a, b)) >= 11.

Method:
  - h_k is an integer polynomial (Day 89 fit).  By 2^T-periodicity,
    v_2(h_k(a, b)) >= 11 for all (a, b) with a+b even iff
    h_k(a, b) ≡ 0 (mod 2^11) for all (a, b) in [0, 2^11)^2 with a+b even.
  - Vectorize evaluation mod 2^11 via numpy outer products.
"""
import time
from math import factorial

import numpy as np
from sympy import Poly, expand, symbols

a_s, b_s = symbols('a b')

# The h_k^{(c=8)} fits from 2026-07-11-c8-extract-hk.py — reproduced here
# in factored form for readability.  Verified 21/21 sanity vs pipeline.

h_c8 = {
    0: (a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)*(a_s + 7)*(a_s + 8)*(a_s + 9)
       * (b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)*(b_s + 6)*(b_s + 7)*(b_s + 8),
    1: -56*(a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)*(a_s + 7)*(a_s + 8)
        *(b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)*(b_s + 6)*(b_s + 7),
    2: -16*(a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)*(a_s + 7)
        *(b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)*(b_s + 6)
        *(a_s*b_s + a_s + 2*b_s - 145),
    3: 2016*(a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)
        *(b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)
        *(a_s*b_s + a_s + 2*b_s - 33),
    4: 672*(a_s + 3)*(a_s + 4)*(a_s + 5)*(b_s + 2)*(b_s + 3)*(b_s + 4)
        *(a_s**2*b_s**2 + a_s**2*b_s + 3*a_s*b_s**2 - 177*a_s*b_s - 180*a_s
          + 2*b_s**2 - 358*b_s + 1740),
    5: -100800*(a_s + 3)*(a_s + 4)*(b_s + 2)*(b_s + 3)
        *(a_s**2*b_s**2 + a_s**2*b_s + 3*a_s*b_s**2 - 37*a_s*b_s - 40*a_s
          + 2*b_s**2 - 78*b_s + 88),
    6: -40320*(a_s + 3)*(b_s + 2)
        *(a_s**3*b_s**3 - a_s**3*b_s + 3*a_s**2*b_s**3 - 150*a_s**2*b_s**2
          - 153*a_s**2*b_s + 2*a_s*b_s**3 - 450*a_s*b_s**2 + 1348*a_s*b_s
          + 1800*a_s - 300*b_s**2 + 3300*b_s + 1080),
    7: 5644800*(a_s**3*b_s**3 - a_s**3*b_s + 3*a_s**2*b_s**3
                - 30*a_s**2*b_s**2 - 33*a_s**2*b_s + 2*a_s*b_s**3
                - 90*a_s*b_s**2 + 16*a_s*b_s + 108*a_s - 60*b_s**2
                + 156*b_s + 180),
    8: 2822400*(a_s**3*b_s**3 - 3*a_s**3*b_s**2 + 2*a_s**3*b_s
                - 96*a_s**2*b_s**2 + 96*a_s**2*b_s - a_s*b_s**3
                - 93*a_s*b_s**2 + 814*a_s*b_s + 720*b_s - 576),
    9: -304819200*(a_s**2*b_s**2 - 3*a_s**2*b_s + 2*a_s**2 - a_s*b_s**2
                   - 13*a_s*b_s + 14*a_s + 24),
    10: -203212800*(a_s**2*b_s**2 - 5*a_s**2*b_s + 6*a_s**2 - 3*a_s*b_s**2
                    - 30*a_s*b_s + 72*a_s + 2*b_s**2 + 35*b_s + 42),
    11: 13412044800*(a_s*b_s - 3*a_s - 2*b_s + 1),
    12: 13412044800*(a_s*b_s - 4*a_s - 3*b_s),
    13: -348713164800,
    14: -697426329600,
    15: 0,
}


def v2_int(n):
    if n == 0:
        return float('inf')
    m = abs(int(n))
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    return r


def poly_coeffs(expr, modulus):
    """Return list of (da, db, coef_mod_modulus) after expanding expr."""
    if expr == 0:
        return []
    poly = Poly(expand(expr), a_s, b_s, domain='ZZ')
    d = poly.as_dict()
    return [(k[0], k[1], int(c) % modulus) for k, c in d.items() if int(c) % modulus != 0]


def eval_grid_mod(coeffs_mod, modulus, deg_a, deg_b):
    """Return an int64 array grid[a, b] = poly(a, b) mod modulus for a, b in [0, modulus)."""
    N = modulus
    A = np.arange(N, dtype=np.int64)
    B = np.arange(N, dtype=np.int64)
    # Precompute powers of A and B mod modulus.
    A_pow = np.zeros((deg_a + 1, N), dtype=np.int64)
    A_pow[0] = 1
    for d in range(1, deg_a + 1):
        A_pow[d] = (A_pow[d - 1] * A) % modulus
    B_pow = np.zeros((deg_b + 1, N), dtype=np.int64)
    B_pow[0] = 1
    for d in range(1, deg_b + 1):
        B_pow[d] = (B_pow[d - 1] * B) % modulus
    grid = np.zeros((N, N), dtype=np.int64)
    for (da, db, c) in coeffs_mod:
        # outer product a^da * b^db, scaled by c
        contrib = np.multiply.outer(A_pow[da], B_pow[db])
        contrib = (contrib * c) % modulus
        grid = (grid + contrib) % modulus
    return grid


def min_v2_over_grid(grid, mask, modulus):
    """Given grid[a,b] mod modulus and mask, return min v_2 over masked
    entries and one witness (a, b, val) attaining it, or (inf, None) if all zero."""
    N = grid.shape[0]
    vals = grid[mask]
    # Find nonzero minima.  For values mod 2^T, v_2 in [0, T]; T=... means val=0.
    if not np.any(vals != 0):
        return float('inf'), None
    # v_2 of each nonzero val: use elementwise
    nonzero_mask = vals != 0
    nonzero_vals = vals[nonzero_mask]
    # v_2: count trailing zeros; use bit_and with -val (two's complement) & val
    # For positive numbers: v_2(n) = number of trailing zero bits.
    # Fastest: (n & -n).bit_length() - 1 elementwise via numpy
    lsb = nonzero_vals & (-nonzero_vals)
    # log2 of lsb: use log2, but lsb is a power of 2, so:
    log_lsb = np.log2(lsb.astype(np.float64)).astype(np.int64)
    min_v2 = int(log_lsb.min())
    # Find witness (a, b) with that v_2
    where_min = np.where(log_lsb == min_v2)[0][0]
    # Recover (a, b) from position in vals array
    # mask flattened -- get first nonzero and min v2 position
    # Simpler: iterate to find witness (small, this only happens on FAILURES)
    positions = np.argwhere(mask)
    nonzero_positions = positions[np.where(vals != 0)[0]]
    ab = nonzero_positions[where_min]
    val = grid[ab[0], ab[1]]
    return min_v2, (int(ab[0]), int(ab[1]), int(val))


def main():
    T = 11
    modulus = 1 << T
    print("=" * 74)
    print(f"Day 89 Stage B — 2^T periodicity check for h_k^(c=8), T = {T}")
    print(f"    Grid: (a, b) in [0, {modulus})^2   with a+b even")
    print(f"    Modulus: 2^{T} = {modulus}")
    print("=" * 74)

    # Parity mask for a+b even: (a%2 == b%2)
    N = modulus
    A_grid, B_grid = np.meshgrid(
        np.arange(N, dtype=np.int64), np.arange(N, dtype=np.int64), indexing='ij'
    )
    mask_even = ((A_grid + B_grid) % 2 == 0)
    print(f"    Masked cells: {int(mask_even.sum())} (should be {N*N//2})")

    all_ok = True
    min_min = float('inf')
    per_k = {}
    for k in range(16):
        expr = h_c8[k]
        t0 = time.time()
        coeffs = poly_coeffs(expr, modulus)
        if len(coeffs) == 0:
            # zero polynomial (or all coefs ≡ 0 mod 2^T)
            per_k[k] = (True, float('inf'), None, 0.0)
            print(f"  k={k:>2d}: all coefs ≡ 0 mod 2^{T}  (poly is 0 mod {modulus})")
            continue
        deg_a = max(da for (da, db, c) in coeffs)
        deg_b = max(db for (da, db, c) in coeffs)
        grid = eval_grid_mod(coeffs, modulus, deg_a, deg_b)
        min_v2, witness = min_v2_over_grid(grid, mask_even, modulus)
        dt = time.time() - t0
        per_k[k] = (min_v2 >= T, min_v2, witness, dt)
        if min_v2 >= T:
            status = "PASS"
        else:
            status = "FAIL"
            all_ok = False
        min_min = min(min_min, min_v2)
        print(f"  k={k:>2d}: {status}  min v_2 (over shell) = {min_v2}"
              + (f"   witness (a,b,val)={witness}" if witness else "")
              + f"   ({dt:.1f}s, {len(coeffs)} terms, deg=({deg_a},{deg_b}))")

    print("\n" + "=" * 74)
    print(f"OVERALL:  {'ALL PASS' if all_ok else 'FAIL'}")
    print(f"  min v_2 across all k = {min_min}")
    print("=" * 74)

    if all_ok:
        print(
            f"\n∴ v_2(h_k^{{(c=8)}}(a, b)) >= {T} for k=0..15 and all (a, b) with a+b even."
            f"\n  By sum rule: v_2(H_8(a, b, j)) >= {T} for all j.  ∴  β'(8) >= {T}."
        )
        print(
            f"\n  Combined with UPPER-bound witness  H_8(8, 8, 2) = 3403353310156800"
            f" = 2^11 * 1661793608475  (a+b=16 even, v_2 = 11 exact, odd cofactor)"
            f"\n  →  β'(8) = 11  UNCONDITIONAL."
        )


if __name__ == "__main__":
    main()
