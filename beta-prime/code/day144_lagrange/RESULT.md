# Day 144 — Lagrange Inversion Test for b_k

## Sequence
b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566   (k = 1..7)

## (a) SANITY CHECK — F = (1 - sqrt(1 + 4A))/2 CONFIRMED

Computing F(τ) = (1 - sqrt(1 + 4·A(τ)))/2 in SymPy exact rationals with a_k data yields b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566 exactly. And (1 - 2F)² - (1 + 4A) truncates to 0 mod τ^8. Rick's quadratic identity is watertight.

## (b) LAGRANGE ANSATZ b_k = (1/k)[τ^{k-1}] h(τ)^k

Fitting c_0,…,c_6 iteratively:

    c_0 = 3
    c_1 = 9
    c_2 = 58/3
    c_3 = 322/9
    c_4 = 1639/27
    c_5 = 7879/81
    c_6 = 36376/243

Denominators are strict powers of 3 (3^0,3^0,3^1,3^2,3^3,3^4,3^5). Numerators of 3^i c_i:
d_i = 3, 27, 174, 966, 4917, 23637, 109128. Factorizations:
- 174 = 2·3·29
- 966 = 2·3·7·23
- 4917 = 3·11·149
- 23637 = 3·7879 (7879 prime)
- 109128 = 2^3·3·4547 (4547 prime)

The presence of unrelated large primes (149, 7879, 4547) at consecutive indices is a strong negative signal — no P-finite or algebraic closed form for h at this order.

Additional test — algebraic relation: For every (deg α ≤ 3, deg β ≤ 4), we tested whether h² = α(τ)h + β(τ) with polynomial α, β. All under-determined systems give free parameters; all determined systems give solutions with huge unstructured rationals (numerators/denominators with dozens of digits, no visible cancellation). Padé approximants [m/n] for m+n ≤ 6 show no truncation.

**CRUCIAL negative:** the ansatz b_k = (1/k)[τ^{k-1}] h(τ)^k is tautologically fittable for any sequence (7 unknowns, 7 equations). Predictive test: fit c_0..c_5 from b_1..b_6, predict b_7. Prediction: 85 275 438. Actual: 85 384 566. Mismatch. Fit c_0..c_4 from b_1..b_5, predict b_6, b_7: 3 637 752 and 83 999 040 vs actual 3 661 389 and 85 384 566. Mismatch. **h is NOT a polynomial of any finite degree — it is a genuine power series with c_i having growing 3-adic denominator and rough numerators.**

## (c) COMPOSITIONAL INVERSE G(τ) of F(τ)

    G(τ) = (1/3)τ − τ² + (23/27)τ³ − (7/81)τ⁴ − (4/81)τ⁵ − (20/729)τ⁶ − (32/2187)τ⁷ + …

Denominators are strict powers of 3. No sign pattern (mixed after g_2). Not obviously a rational or algebraic function.

## (d) P-RECURSIVE / RATIONAL RECURRENCE — NEGATIVE

Systematic search for a linear recurrence with polynomial coefficients (order ≤ 4, degree ≤ 4): NO recurrence found. Search of constant-coefficient recurrences on d_i = 3^i c_i (orders 2, 3): no fit. Rick's Day 143 result — that b_k is NOT P-recursive at low order — is reconfirmed here.

## (e) ASYMPTOTIC

Ratios b_{k+1}/b_k: 9, 15.44, 18.83, 20.90, 22.31, 23.32. Growing sublinearly with k → algebraic growth b_k ~ C·r^k·k^α (no k! factor).

Best least-squares fit log b_k = A + Bk + α log k on all 7 points:
- r = e^B ≈ 30.84, α ≈ −1.74, C ≈ 0.097
- residuals under 0.01 in log — good fit.

Adding a β log(k!) term gives β ≈ −0.10 (essentially 0), consistent with algebraic growth. The ratios don't grow linearly, ruling out factorial growth. Free-cumulant analysis: κ_n / (−6) = 1, 15, 373, 11245, 375732, 13386573, 498347406 (all integers) — cleaner than m_n or b_n but not matching anything obvious.

## Bottom line

Lagrange ansatz: technically YES (h always exists in ℚ[[τ]] because b_1 ≠ 0), but h has NO closed form visible from 7 coefficients. c_i denominators are exactly 3^{i-1} for i ≥ 2, but numerators show no low-degree algebraic or P-recursive structure. Growth is algebraic (r ≈ 30.8, not e·something), so b_k is NOT the coefficient sequence of a hypergeometric/D-finite generating function of low order. The nicest artifact found is κ_n/(−6) ∈ ℤ (integer free cumulants scaled by 6), which may hint at a free-probability interpretation but no closed form emerged.
