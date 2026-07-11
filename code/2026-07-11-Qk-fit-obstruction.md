# Q_k(a, b, c) fit — obstruction note (Day 89)

## Status per k

| k  | Fit? | Total deg | c-values used | Cross-val at c=8 | Source |
|----|------|-----------|---------------|------------------|--------|
| 0  | ✓    | 0         | {4..9}        | 78/78            | Day 88 |
| 1  | ✓    | 2         | {4..9}        | 78/78            | Day 88 |
| 2  | ✓    | 4         | {4..9}        | 78/78            | Day 88 |
| 3  | ✓    | 6         | {4..12}       | 153/153          | Day 88 |
| 4  | ✓    | 8         | {5..14}       | 190/190          | Day 88 |
| 5  | ✓    | 10        | {6..17}       | 253/253          | Day 88 |
| 6  | ✓    | 12        | {6..21}       | 325/325          | Day 89 |
| 7  | ✗ deg > 14 at 1000 samples via mod-p Vandermonde (`2026-07-11-Qk-fit-k7-modp.py`); NB deg 12 (sympy rref, 6214 samples) also inconsistent |
| 8+ | Deferred — total degree ≥ 16, ≥ 969 monomials, expensive |

## The obstruction (k ≥ 7)

For each k ≤ 6 the total degree of Q_k grows by 2 (pattern deg = 2k).
Naively:

- k = 7 → D = 14 → 680 monomials
- k = 8 → D = 16 → 969 monomials
- k = 15 → D = 30 → 5456 monomials

**Empirical deviation at k = 7.** Day 89 mod-p Vandermonde fits
(`2026-07-11-Qk-fit-k7-modp.py`) at both deg 13 (560 mono) and deg 14
(680 mono) returned "under-determined or inconsistent" on 1000 random
samples drawn from a 6214-sample pool over c ∈ {8..19}, a, b ∈ [7, 45].
Either:

  (a) The 1000-sample cap is insufficient at deg 13-14 despite being
      1.5x over-determined nominally (rank deficiency from lattice
      structure), OR
  (b) Q_7 has total degree > 14, breaking the `deg = 2k` pattern.

Discriminating (a) vs (b) needs either (i) a much larger sample pool
(e.g. ab ∈ [7, 80] would give ~10x more samples), or (ii) a rational-
function ansatz that captures higher-c poles.

**Deg 15 mod-p elim.** Killed at ~3:20 min (would take ~110 sec more
per additional degree in pure-Python Gaussian elim mod p). Not
completed this session.

## Path forward

For c = 10, c = 11 witness attempts, we need Q_k at k = 0..2c-1 = 0..19.
Options:

1. **Direct extraction per c.** For each target c, run the c8-extract-hk
   pipeline verbatim at that c. Gives h_k^{(c)}(a, b) for k = 0..2c-1 as
   bivariate polynomials directly (no c-general fit needed). This is
   how the c = 8 sweep was done; costs ~1 minute per c.

2. **Rational-function ansatz.** Q_k(a, b, c) may have poles at small
   integer c that make polynomial fits require larger degree than the
   "true" structural degree. Trying a rational-function ansatz
   Q_k = P_k(a, b, c) / (c(c-1)...(c-K_k)) might collapse the fit
   degree.

3. **Fold Q_k structure.** The factored form of Q_0..Q_6 shows a common
   `c(c-1)(c-2)...(c-⌊(k-1)/2⌋)` prefactor. Dividing this out first,
   then fitting the residual, may reduce degree.

For **c = 8 downstream reuse**, option 1 is already accomplished:
`code/2026-07-11-c8-hk-fits.pkl` contains h_k^{(c=8)} for k = 0..15 as
bivariate polynomials, exactly what the c=8 β'(8) sweep needed.

## Recommendation for LEAN / next-CODE session

Extend Q_k catalog per-c on demand (option 1). The c-general form for
k = 0..6 is sufficient to test the c=10 case for low-k structural
matches; if all six low-k Q's carry the pattern at c=10, that's
strong evidence for the higher-k case too — computable per-c-directly.
