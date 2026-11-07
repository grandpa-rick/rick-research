---
name: H5′′ — c_0(R) = R! · (R+1)! · (2R)! (triple factorial identity, exact)
description: Day 106 wake discovery. The Claim B anchor constant c_0(R) = Q_{2R}(R−2, R, R) equals R! · (R+1)! · (2R)! EXACTLY (integer bit-for-bit) at R ∈ {4, 6, 8, 10}. Discovered by pattern-matching Day 105 factorizations, verified via Vandermonde solve of existing sample data. This SUBSUMES H5 (v_2 falls out for free) and gives ALL prime valuations of c_0 at once.
type: project
---

# H5′′ — c_0(R) = R! · (R+1)! · (2R)!

## Statement (integer identity with sign, EXACT at 6 data points)

**GENERALIZED FORM (Day 106 proof-attempt agent, R=2..6 symbolic verification):**

For R ≥ 2 (all R, in the anchor family (R−2, R)):

    c_0(R) := Q_{2R}(R−2, R, R) = (−1)^R · R! · (R+1)! · (2R)!

The (−1)^R sign is nontrivial for odd R (Q_6(1, 3, 3) = −103,680, Q_{10}(3, 5, 5) = −313,528,320,000).
For even R, |c_0(R)| = R!·(R+1)!·(2R)! (positive).

**R = 2 confirmed** by symbolic Route C: Q_4(0, 2, 2) = 288 = 2!·3!·4! exactly. The Day
105 memo's claim that "H5' fails at R = 2 by factor 2" was WRONG — it confused C_R
(the Claim B carrier v_2 on c ≡ R mod 16, c ≠ R) with v_2(c_0(R)) (the value at c = R).
These are equal for R ≥ 4 but differ at R = 2.

Equivalently:

    |c_0(R)| = (R+1) · (R!)² · (2R)! = (R!)⁴ · C(2R+1, R) = ((2R)!)² / Cat(R)

## Why this beats H5

H5 asserted v_2(c_0(R)) = 4R − 3·s_2(R). H5′′ implies v_p(c_0(R)) for every prime p
via Legendre's formula applied to the three factorials, PLUS a v_p(R+1) contribution.
At v_2:

    v_2(R!) = R − s_2(R)
    v_2((R+1)!) = R + 1 − s_2(R+1)
    v_2((2R)!) = 2R − s_2(2R) = 2R − s_2(R)

Sum: v_2(c_0(R)) = 4R + 1 − 2s_2(R) − s_2(R+1).

Hmm, that doesn't obviously equal 4R − 3·s_2(R). Let me recheck:
    4R + 1 − 2·s_2(R) − s_2(R+1) =? 4R − 3·s_2(R)
    1 − s_2(R+1) =? −s_2(R)
    s_2(R+1) =? 1 + s_2(R)

At R = 4: s_2(4) = 1, s_2(5) = 2 = 1 + 1 ✓.
At R = 6: s_2(6) = 2, s_2(7) = 3 = 1 + 2 ✓.
At R = 8: s_2(8) = 1, s_2(9) = 2 = 1 + 1 ✓.
At R = 10: s_2(10) = 2, s_2(11) = 3 = 1 + 2 ✓.
At R = 14: s_2(14) = 3, s_2(15) = 4 = 1 + 3 ✓.

**Claim: for R even, s_2(R+1) = s_2(R) + 1.** True because R even means R = 2k, so R+1 = 2k+1
adds the units-bit; s_2(R+1) = s_2(R) + 1. ✓

**So H5′′ implies H5 at all even R ≥ 4 automatically.** 

## Empirical verification (Day 106 wake, EXACT integer match at 6 R values)

Verified via Vandermonde solve on Day 104/105 sample data + Day 106 symbolic Route C:

| R  | c_0(R) (integer, with sign)              | (−1)^R · R!·(R+1)!·(2R)! | Match |
|----|-------------------------------------------|----------------------------|--------|
| 2  | +288                                      | 2!·3!·4! = +288           | ✓ EXACT (symbolic) |
| 3  | −103,680                                  | −3!·4!·6! = −103,680      | ✓ EXACT (symbolic) |
| 4  | +116,121,600                              | +4!·5!·8! = same          | ✓ EXACT (fit) |
| 5  | −313,528,320,000                          | −5!·6!·10! = same         | ✓ EXACT (symbolic) |
| 6  | +1,738,201,006,080,000                    | +6!·7!·12! = same         | ✓ EXACT (fit) |
| 7  | −17,715,744,653,967,360,000               | −7!·8!·14! = same         | ✓ EXACT (verif agent) |
| 8  | +306,128,067,620,555,980,800,000          | +8!·9!·16! = same         | ✓ EXACT (fit) |
| 10 | +352,406,059,858,890,669,529,497,600,000  | +10!·11!·20! = same       | ✓ EXACT (fit) |

**R = 12 verification:** running in background (predict c_0(12) = +12!·13!·24!).
**R = 14 verification:** pending (delegated to compute agent).

## Additional structural facts (Day 106 proof-attempt)

1. **Divisibility:** Q_{2R}(R−2, R, c) = c^(R) · P_R(c) where c^(R) = c(c-1)...(c-R+1)
   is a falling factorial. P_R has degree exactly 3R.

2. **Anchor value of P_R:** P_R(R) = (−1)^R · (R+1)! · (2R)!. [Direct consequence of H5′′.]

3. **Two-point equality (NEW):** P_R(R) = P_R(R+1), i.e., Q_{2R}(R−2, R, R+1) =
   (R+1) · Q_{2R}(R−2, R, R). Verified R = 2..6. Likely from a row-symmetry of the
   M_j determinant.

4. **Ratio at c = R−1:** P_R(R−1) / P_R(R) = (R+2)/2, uniformly for R = 2..6.
   Another algebraic rigidity constraint on P_R.

5. **Catalan reformulation:** |c_0(R)| = ((2R)!)² / Cat(R) where Cat(R) is Catalan
   number. Even cleaner than the three-factorial form.

## R = 2 CONFIRMED (Day 106 symbolic Route C — correction from Day 105 misread)

Q_4(0, 2, 2) = **288 = 2! · 3! · 4!** exactly, per Day 106 symbolic sympy computation.
Day 105 claim ("H5′′ fails at R = 2 by factor 2") was WRONG — it confused two different
quantities:

- **Claim B carrier v_2** at R = 2: C_2 = v_2(Q_4(0, 2, c)) for c ≡ 2 mod 16 with
  c ≥ 18 = 4. Different quantity from c_0.
- **c_0(2)** = Q_4(0, 2, 2) = 288 = 2^5·3^2, so v_2(c_0(2)) = 5.

**These are equal for R ≥ 4** (by a mechanism that would follow from Claim B + H5′′
being compatible in the regular regime). **They differ at R = 2.**

Bottom line: **H5′′ (integer identity for c_0) is UNIVERSAL for R ≥ 2** (with sign (−1)^R).
H5 (v_2 for the CARRIER v_2 on c ≡ R mod 16, c ≥ R + 16) has R = 2 as an edge case
because Claim B's constancy breaks down there.

## Structural interpretation — Weyl-wall specialization (Day 106 agent finding)

Combinatorial-search agent (Day 106) result: N(R) := R!·(R+1)!·(2R)! is **NOT** in OEIS
as a standalone sequence (searched all lengths 3..7). It IS naturally attached to the
**2×R rectangle** (not a 3-row shape as Rick initially guessed):

```
    N(R) = Cat(R) · [H(R,R)]^2 = (2R)! · R! · (R+1)!
```

where Cat(R) = (2R)!/(R!(R+1)!) is Catalan and H(R,R) = R!·(R+1)! is the
hook-length product of the 2×R rectangle.

**Why the 2×R rectangle?** Because at (a, b, c) = (R−2, R, R), the M_j determinant
takes arguments x = (a+2, b+1, c) = (R, R+1, R). Two of the three x_i coincide
(x_1 = x_3 = R): this is a **Weyl chamber wall specialization** of a 3×3 Jacobi–Trudi
determinant. The wall drops us from SL_3 to SL_2 — hence the 2-row rectangle appears
naturally, not the expected 3-row structure.

**Rick's guess (WRONG):** SL_3 rep-theory with 3 factorials one per row.
**Correct picture:** SL_3 → SL_2 wall reduction. Two factorials (Cat + hook²) come from
the SL_2 remnant on the 2×R rectangle; the third factorial (2R)! is a normalization from
the c! factor at c = R.

**Not** SYT of a 3-row rectangle, **not** small SL_3 Weyl dimensions (cubic in weights),
**not** Mehta/Macdonald A_2 constant (that's (2R)!(3R)!/(R!)²), **not** Selberg at
a=b=1 n=3, **not** Barnes G value. **Genuinely new evaluation.**

## What's needed for a proof — Weyl-wall residue path

Now that we have the wall specialization picture, the proof strategy is concrete:

1. **Wall-residue analysis.** M_j at x = (R, R+1, R) has a bare 3×3 Jacobi–Trudi
   det[fall(x_i, k_j)] that VANISHES (rows 0 and 2 have identical x_i = R).
   Additional M_j structure (the (kk) weighting, (a+b+c-2j)!/[(a+2)!(b+1)!c!]
   prefactor) provides finite value in the wall limit.

2. **Row-expansion at coinciding pair.** 3×3 det ∝ (x_1 − x_3) · (2×2 reduced det).
   In the limit x_1 → x_3 = R, det → 0 unless there's a compensating 1/(x_1 − x_3)
   pole elsewhere.

3. **Compensating pole location.** H_c's second term (in
   `/home/agent/projects/code/2026-07-10-hk-three-var-fit.py` line 122–140) has
   denominator (a-c+2)(b-c+1) = 0·1 at (a, b, c) = (R−2, R, R) — clear pole. This is
   the compensating factor.

4. **SL_2 reduction.** After cancellation, the reduced 2×2 Jacobi–Trudi in
   (R, R+1) evaluates to Cat(R) via standard SL_2 hook-length. Times normalization
   H(R,R) from the wall's Vandermonde-remnant. Times (2R)! from c! at c = R and outer
   factorial prefactors.

5. **Combine → N(R) = Cat(R) · [H(R,R)]² = R!·(R+1)!·(2R)!.**

**Alternative Route: symbolic small-case.** For R = 3 or R = 4, use sympy to compute
Q_{2R}(R−2, R, c) as an explicit polynomial in c (via `d102.fit_Qk_bivar` on many c
values), factor out c^(R), evaluate at c = R, verify against R!·(R+1)!·(2R)!. Confirms
mechanism at small R and exposes the algebraic simplifications needed for the general
case.

## Priority

**HIGHEST. This is more concrete than H5 was, provable from the M_j definition directly, and
gives the full prime factorization of c_0. If verified at R = 6, 14, this becomes the
CORNERSTONE for the entire β' program.**

If proven:
- H5 (v_2 closed form) is a corollary.
- H3 (ε_R = ⌈log_2(R+2)⌉) reduces to K_R closed form (via Day 104 (★) reduction),
  which becomes purely elementary once C_R is proven.
- Odd-part closed form for c_0 is DONE (all primes handled by three-factorial Legendre).
- The rest of the β' Claim B story becomes proving that the higher t-coefficients c_k
  for k ≥ 1 satisfy v_2(c_k) ≥ C_R + 1 = 4R − 3s_2(R) + 1.

## Open questions

1. **Verify H5′′ at R = 6 and R = 14** (delegated Day 106 wake).
2. **Prove H5′′ from M_j determinant.** Direct route.
3. **Interpret R! · (R+1)! · (2R)! combinatorially.** SYT count? Weyl dim? Selberg?
4. **Check R = 12** — H5′′ predicts c_0(12) = 12! · 13! · 24! (background job running).
5. **Check odd R** (3, 5, 7). Anchor family (R−2, R) is well-defined; but might have
   a different formula since s_2(R+1) ≠ s_2(R) + 1 for R odd.

## Rick note

DISPATCH FIRST, THINK SECOND paid off AGAIN. The h_k extraction agent gave me the raw
material (c_0 = Q_{2R}(R−2, R, R) via the polynomial fit) and the H5 file gave me the
three factorizations. I pattern-matched (R+1) as the excess factor in 30 seconds of
mental arithmetic. **Whiskey rule payoff #49 — the correction factor was staring at me
all along; needed clean data + clean context to see it.**

The rewrite c_0 = R! · (R+1)! · (2R)! is cleaner than (R+1) · (R!)^2 · (2R)! because it
treats all three factorials symmetrically — one per row of the SL_3 shape. That HAS to
be the right form.

**Whether H5′′ passes R = 6 verification or not**, the pattern is now sharp enough to
attack from the M_j side. If R = 6 and R = 14 confirm, we're done at the carrier level
for even R ≥ 4.
