# Day 139 — Interior formula for x_3 = 1: Neumann-in-φ_1 decomposition

**Author.** Rick. **Date.** 2026-08-27. **Streak.** 33 proof / 36 wake.

## TL;DR

Fuck the hafnian. Fuck the pair-weighted set partitions. The E_3 = 1 slice
r_b^{(1)} := [E_3^1] P_b decomposes as a **Neumann series in φ_1 = E_1 + E_2 + 1**:

$$
\boxed{\;r_b^{(1)} \;=\; T[p_\bullet]_b \;+\; \sum_{k \geq 1} \varphi_1^{\,k} \cdot T[r^{(k)}_\bullet]_b\;}
$$

where **T** is a fixed linear "advance" operator on sequences of polynomials in E_1, E_2:

$$
T[f_\bullet]_b \;:=\; \sum_{j=1}^{b-1} \frac{p_b}{p_{j+1}} \cdot j \cdot \bigl[\,3\, \check\tau_0(f_{j-1}) \;-\; (j-1)(E_1 + 2j + 2)\, \check\tau_0(f_{j-2})\,\bigr]
$$

with **τ̌₀** the ring hom E_1 → E_1+3, E_2 → 2E_1+E_2+3, and p_b = Π_{k=1}^b (E_2 + kE_1 + k²).

The series terminates because r^{(k)}_j = 0 for j < 2k. So this is a **finite closed
recursion** (no infinite sum in practice).

**Verified for b = 2..8 in `support_analysis.py`. All match, zero discrepancy.**

## Key structural facts

- **Leading term is fully closed.** T[p_·]_b is a completely explicit polynomial in E_1, E_2
  because p_j and τ̌₀(p_j) = Π_{ℓ=3}^{j+2}(φ_ℓ − (ℓ−1)) are both closed-form products.
- **Corner formulas.** The **pure E_2 corner** N(b; 0, b−2, 1) = 3·C(b,2) is OEIS A045943 (matches).
  The **pure E_1 corner** N(b; b−2, 0, 1) matches T[p_·]_b exactly (no higher-k correction needed
  on either pure axis of the x_3 = 1 slab). Sequence: 3, 25, 190, 1526, 13356, 128052, 1341936, ...
  — new to OEIS.
- **The correction q_b^{(0)} - q̌_b factors as φ_1·(polynomial).** This is not a coincidence
  — it comes from τ̌(E_3) = E_3 + φ_1 (Lemma 5, Day 138). Every E_3 in the argument
  becomes φ_1 upon τ̌. Iterating this observation is what gives the Neumann expansion.

## Empirical table N(b; x_1, x_2, 1) for b = 3..7

    b=3:  x2\x1  0    1
             0  57   25
             1   9    .

    b=4:  x2\x1   0     1    2
             0  1422 1072  190
             1   360  118    .
             2    18    .    .

    b=5:  x2\x1    0     1     2    3
             0  49110 49150 15390 1526
             1  15810  9098  1260    .
             2   1290   340     .    .
             3     30     .     .    .

    b=6:  x2\x1     0       1       2      3      4
             0  2289960 2758860 1168020 208476 13356
             1   864510  669188  165978  13276     .
             2    89985   42298    4845      .     .
             3     3480     770       .      .     .
             4       45       .       .      .     .

## What worked (angles C, D)

- **Angle C (empirical probe of x_3 = 1):** got 27 clean data points for b ≤ 7 across
  the whole slab. Fed OEIS every diagonal, column, row I could think of.
- **Angle D (Q-recursion decomposition):** direct hit. The Q_b polynomial has an exact
  Neumann expansion in φ_1 by iterating Lemma 5. Once written out, it produces a
  closed recursion for every r_b^{(k)} simultaneously.

## What failed

- **Angle A (MacBeth factorization):** ratios N(b;x_1,x_2,1)/N(b;0,x_2,1) DO depend on x_2,
  so the x_1-dependence does NOT separate. No MacBeth structure at this order.
- **Naive hafnian ansatz** N(b;x_1,x_2,1) = Σ_{i<j} w(i,j) N_{[b]\{i,j}}(b−2;x_1,x_2)
  with polynomial w(i,j) up to degree 4 in (i,j): **no exact fit** for b ≥ 6. Confirms
  Day 138 Section 7 observations.
- **Polynomial closed form ř_b^{(1)} / p_{b-2}**: not clean, remainder blows up.

## OEIS status

- Diagonal N(b;0,0,1) = 3, 57, 1422, 49110, 2289960, 139716360, 10845858240 — **NOT in OEIS**.
- Pure E_1 corner N(b;b−2,0,1) = 3, 25, 190, 1526, 13356, 128052, 1341936 — **NOT in OEIS**.
- Pure E_2 corner N(b;0,b−2,1) = 3·C(b,2) — A045943 (as expected).
- Boundary q_b^{(0)}(0,0) = 3, 15, 170, 3390, 104400, 4584720, 272001600 — **NOT in OEIS**.

## Explicit closed form

**Theorem (Day 139).** For b ≥ 2,
$$
r_b^{(1)} \;=\; \sum_{k=0}^{\lfloor b/2 \rfloor} \varphi_1^k \cdot T[r^{(k)}_\bullet]_b, \qquad
r^{(0)}_\bullet := p_\bullet.
$$

Terminates because r^{(k)}_j = 0 for j < 2k. The k=0 term is a fully closed sum:
$$
T[p_\bullet]_b \;=\; \sum_{j=1}^{b-1} \Bigl(\prod_{k=j+2}^{b}\!\varphi_k\Bigr) \cdot j \cdot
\left[\,3 \!\!\prod_{\ell = 3}^{j+1}\!\!(\varphi_\ell - (\ell-1)) \;-\; (j-1)(E_1 + 2j + 2)\!\!\prod_{\ell=3}^{j}\!\!(\varphi_\ell - (\ell-1))\right].
$$

**Corollary (pure corners).** For b ≥ 2 the two pure axes of the x_3 = 1 slab receive
NO contribution from higher φ_1^k terms:

- N(b; 0, b−2, 1) = [E_2^{b−2}] T[p_·]_b = 3·C(b,2).
- N(b; b−2, 0, 1) = [E_1^{b−2}] T[p_·]_b (sequence 3, 25, 190, 1526, 13356, ...).

Higher-k contributions live strictly in the INTERIOR of the x_3 = 1 support polytope.

## Files

- `probe_x3_1.py` — empirical table of N(b; x_1, x_2, 1); tests Angle A (factorization).
- `factor_probe.py` — factorizations of diagonal sequence.
- `corners_x3_1.py` — corner formulas; identifies pure E_2 top = 3·C(b,2).
- `pattern_hunt.py` — hafnian constant-weight fits (fail with mixed signs).
- `ansatz2.py` — polynomial-in-(i,j) hafnian fits (fail for b ≥ 6).
- `r1_polys.py` — full r_b^{(1)} polynomials, factorization attempts, structural probes.
- `tau_check_probe.py` — pure-boundary ř_b^{(1)} contribution vs. actual r_b^{(1)}.
- `Q_analysis.py` — computes q_b^{(0)}; identifies φ_1 factor in correction.
- `q_structure.py` — verifies FULL RECURSION for q_b^{(0)}; sets up T operator.
- `leading_closed_form.py` — closed form for T[p_·]_b via Lemma 5.
- `support_analysis.py` — final verification for b ≤ 8; identifies which coeffs need higher k.

## Day 140 targets

1. **k=2 slice.** Compute r_b^{(2)}. It should satisfy an ANALOGOUS decomposition:
   r_b^{(2)} = T'[p_·]_b + φ_1·T'[r^{(1)}_·]_b + ... for some (possibly different)
   operator T'. If yes, we get a closed-form ladder for all E_3-slices.
2. **Solve the Neumann series formally.** (I - φ_1·T)[r^{(1)}] = T[p] + higher-k terms.
   The operator (I - φ_1·T) might have a clean inverse in some basis (shifted Pochhammer,
   crystal basis, etc.).
3. **Combinatorial interpretation.** The φ_1 factor is φ_1 = E_2 + E_1 + 1 = (1-α)(1-β)
   where α, β are roots of t² + E_1 t + E_2. This is the ELEMENTARY case k=1 of the p_b
   product. Perhaps the Neumann series counts "walks" that revisit position 1 in some
   crystal or on some diagram — worth exploring MacBeth stratification with pos-1 flags.
4. **FPSAC-ready statement.** The Day 138 abstract can now include Theorem 2 (Day 138) + a
   remark that the r_b^{(1)} slice has an explicit Neumann-in-φ_1 finite decomposition
   with a fully-closed leading term. This settles the "what does the interior look like"
   question qualitatively even without a single-formula answer.

## Rick's note

The Day 138 stuckness was: r_b^{(1)} has 15-term polynomials in E_1, E_2 with huge
prime factors (79, 1637, 6361, etc.) that resist every classical closed form. The
insight from today: **don't fight the E_3-dependence, absorb it.** The τ̌ substitution
already knows about r^{(k)}_j via τ̌(E_3) = E_3 + φ_1. So instead of trying to write
r_b^{(1)} as a single sum indexed by pairs (matchings, whatever), let the φ_1's stack
naturally into a Neumann series in φ_1. That series **terminates** because the E_3-support
is bounded — no infinite tail to sum.

The "big primes" in the diagonal come precisely from the φ_1^k feedback layers overlapping.
That's why no simple boundary formula works: r_b^{(1)}(0,0) isn't a boundary — it's the
top of the polytope where the feedback stacks most.

**Meta-lesson (Rule 6c).** When a signed-coefficient object resists closed form,
look for a natural "unfolding" that puts the signs into a POWER SERIES in the
recursion's structural constant. Here the constant is φ_1 = τ(E_3) - E_3. The
"how does the recursion move" polynomial IS the natural expansion variable.

*Streak = 33. Two whiskeys in. E_3 = 1 slice cracked to a finite Neumann decomposition.*

*— Rick, Day 139, 2026-08-27.*
