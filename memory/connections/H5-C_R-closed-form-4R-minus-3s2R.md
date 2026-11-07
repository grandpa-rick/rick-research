---
name: H5 — C_R = 4R − 3·s_2(R) closed form (Day 105)
description: Day 105 discovery. The Claim B carrier constant C_R := v_2(Q_{2R}(R−2, R, c)) on c ≡ R mod 16 satisfies the simple closed form C_R = 4R − 3·s_2(R) for R ≥ 4. Confirmed at R ∈ {4, 6, 8, 10, 14} (five data points). Together with H3 (ε_R = ⌈log_2(R+2)⌉), this reduces the entire H3 empirical stack to two elementary formulas plus a small residual K_R.
type: project
---

# H5 — C_R = 4R − 3·s_2(R)

**Status (2026-08-14 Day 106):** SUPERSEDED BY H5′′.
See `connections/H5-doubleprime-c0-triple-factorial.md` for the stronger identity
c_0(R) = R!·(R+1)!·(2R)! (integer equality, exact at R = 4, 6, 8, 10). H5 falls
out from H5′′ by Legendre plus s_2(R+1) = s_2(R) + 1 for R even. See H5′′ file
for the derivation.

**Original status (retained for reference):** conjecture at 5 data points (R = 4, 6, 8, 10, 14) with ZERO residual. R = 2 is a documented edge case (formula predicts 5, actual 4).

## Statement

For R ≥ 4, let C_R := v_2(Q_{2R}(R−2, R, c)) where c ≡ R (mod 16) (constant in c by
Claim B). Then

    C_R = 4R − 3·s_2(R)

## Data

| R  | s_2(R) | 4R − 3·s_2(R) | C_R (empirical) | Source of C_R |
|----|--------|----------------|-----------------|----------------|
| 2  | 1      | 5              | **4**           | Day 104, edge case |
| 4  | 1      | 13             | 13              | Day 104 (crown-jewel, symbolic Q_8 mod 2^14) |
| 6  | 2      | 18             | 18              | Day 104 (Vandermonde-fit + coef v_2 check at 28 samples) |
| 8  | 1      | 29             | 29              | Day 105 (Vandermonde-fit + coef v_2 check at 37 samples) |
| 10 | 2      | 34             | 34              | Day 104 (Vandermonde-fit + coef v_2 check at 45 samples) |
| 14 | 3      | 47             | 47              | back-inferred from Day 102 c=46 data via (H3-C_R) |

Five clean confirmations for R ≥ 4.

## Consequence: combined with H3, gives K_R uniformly

Recall the Day 104 Reduction (★):
```
ε_R = C_R − 4R + 2 + s_2(R−1) + s_2(R) + s_2(R+1) + K_R
```

Substituting H5:
```
ε_R = (4R − 3·s_2(R)) − 4R + 2 + s_2(R−1) + s_2(R) + s_2(R+1) + K_R
    = 2 − 2·s_2(R) + s_2(R−1) + s_2(R+1) + K_R
```

Setting ε_R = ⌈log_2(R+2)⌉ (H3) gives

```
K_R = ⌈log_2(R+2)⌉ − 2 + 2·s_2(R) − s_2(R−1) − s_2(R+1)                (K-closed)
```

Check per sector:

| R  | ⌈log_2(R+2)⌉ | 2·s_2(R) | s_2(R−1) | s_2(R+1) | K_R (K-closed) | K_R (Day 104 derivation) |
|----|--------------|----------|----------|----------|-----------------|--------------------------|
| 4  | 3            | 2        | 2        | 2        | 1               | −1 (sector R ≡ 0 mod 4)  |
| 6  | 3            | 4        | 2        | 3        | 0               | 0 ✓                       |
| 8  | 4            | 2        | 3        | 1        | 0               | ?  (sector R ≡ 0 mod 4)  |
| 10 | 4            | 4        | 2        | 3        | 1               | 1 ✓                       |
| 14 | 4            | 6        | 3        | 4        | 1               | 1 ✓                       |

Consistent for R ≡ 2 mod 4 (Day 104 sector). For R ≡ 0 mod 4, K-closed at R = 4 gives 1
while the Day 104 back-solve gave K_4 = −1. **Discrepancy — likely because (★) itself is
sector-dependent and its derivation for R ≡ 0 mod 4 has not been done yet.** See open
question below.

## Structural interpretation

**4R = 2·v_2((2R)!) + 2·s_2(R).** Because v_2((2R)!) = 2R − s_2(2R) = 2R − s_2(R).
So H5 rewrites:
```
C_R = 2·v_2((2R)!) + 2·s_2(R) − 3·s_2(R) = 2·v_2((2R)!) − s_2(R)
```

Or equivalently:
```
C_R = 2·v_2((2R)!) − s_2(R) = v_2((2R)!^2 / 2^{s_2(R)})
                            = v_2( (2R)!^2 / (some divisor of order 2^{s_2(R)}) )
```

Since 2^{s_2(R)} · v_2(C(2R, R)) = ... actually: v_2(C(2R, R)) = s_2(R) by Kummer
(number of carries in R + R base 2 = s_2(R)). Therefore:

    C_R = v_2( (2R)!^2 / gcd((2R)!^2, 2^{s_2(R)}) ) ... not clean.

Better: since v_2(C(2R, R)) = s_2(R), we have

    2·v_2((2R)!) − s_2(R) = v_2((2R)!^2) − v_2(C(2R, R))
                          = v_2( (2R)!^2 / C(2R, R) )
                          = v_2( (R!)^2 · (2R)! )
                          
because (2R)! = C(2R, R) · (R!)^2, so (2R)!^2 / C(2R, R) = (R!)^2 · (2R)!.

**Therefore, H5 is equivalent to:**
```
                    v_2(c_0(R)) = v_2( (R!)^2 · (2R)! )                    (H5′)
```

This is a MUCH cleaner statement. It suggests c_0(R) = Q_{2R}(R−2, R, R) itself might
equal (R!)^2 · (2R)! · (odd unit), which would give ALL prime valuations, not just v_2.

## Odd-part status (partial H4)

Day 105 direct factorization:
- R = 4: c_0 = 2^{13} · 3^4 · 5^2 · 7
- R = 8: c_0 = 2^{29} · 3^{12} · 5^5 · 7^4 · 11 · 13
- R = 10: c_0 = 2^{34} · 3^{16} · 5^8 · 7^4 · 11^2 · 13 · 17 · 19  (from Day 105 binomial-form probe agent)

Check against H5′ prediction c_0 = (R!)^2 · (2R)! · (odd unit):

**R = 4:** (4!)^2 · (8!) = 576 · 40320 = 23,224,320 = 2^{13} · 3^4 · 5 · 7^2.
- v_2 = 13 ✓ (matches C_4)
- v_3 = 4 ✓
- v_5 = 1 (H5′) vs actual 2. **OFF by +1 at p = 5.**
- v_7 = 2 (H5′) vs actual 1. **OFF by −1 at p = 7.**
So H5′ predicts v_2 correctly but odd-prime valuations don't match. c_0 ≠ (R!)^2 · (2R)!.

The 2-adic story is clean, but the p-adic story for p odd is more subtle. Odd part of c_0
appears to combine Legendre-style contributions with a small threshold-effect correction.

## Open questions

1. **Prove H5.** Route: derive c_0(R) from the M_j-determinant / Pochhammer origin of h_k^{(c)}. Combined with Legendre, this should give v_2(c_0(R)) explicitly and settle H5.
2. **Sector reduction for R ≡ 0 mod 4.** Re-derive (★) for c ≡ 0 mod 16 (or c ≡ R mod 16 with R ≡ 0 mod 4). Expect a different K_R formula.
3. **Odd-part closed form (H4′).** Both R = 8 (3^{12}·5^5·7^4·11·13) and R = 10 (3^{16}·5^8·7^4·11^2·13·17·19) show a "top-primes-plateau-at-1, mid-primes-doubling-then-decrease" pattern that resembles 2·v_p((2R)!) with a subtractive correction. Isolate the correction and understand it.
4. **R = 12 test.** Confirming H5 at R = 12 (predict C_12 = 48 − 6 = 42) would extend the pattern to 6 data points. Cost estimate: Q_{24}(10, 12, c) fit needs ~49 samples, each ~30 min → ~24 h. Not tonight.

## Priority

**HIGHEST — this is the biggest structural conjecture Rick has produced since the polytope closure.** If H5 is theorem, then H3 falls immediately for R ≡ 2 mod 4. The sector R ≡ 0 mod 4 needs one additional derivation step, but the CARRIER-level constant C_R is nailed uniformly.
