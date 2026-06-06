# Cao-Huang ↔ Rick's Aug~ cross-check at rank 2

**Date:** 2026-05-16.
**Author:** Compute agent for Rick.
**Goal:** Test whether Cao-Huang's bijection (KN_λ(4) ↔ Verma vectors of L(λ) for sp_4) coincides with Rick's implicit (w, π)-to-tableau identification at B_2 short simple, after the C_2 ↔ B_2 short/long-root relabeling.

## TL;DR

- Cao-Huang's Example 4.4 (40 tableaux at λ = ω_1 + 2ω_2 = 3ε_1 + 2ε_2) is fully reconstructed: every label parses to the same (a_1, a_2, a_3, a_4) read off the tableau's row statistics, and the inverse map T_from_a → T regenerates each tableau exactly. 40/40.
- Cao-Huang's bijection and Rick's Aug~ orbit-swap **operate on different objects**. They are **not the same bijection** and there is no natural identification that puts them into 1-1 correspondence at rank 2.
- The disagreement is **structural, not superficial**: Cao-Huang's map sits inside L(λ) (a single irreducible module across all weights); Rick's Aug~ moves between Kostant partitions in Kp(∞) (the U_q(n^−) crystal), shifting weight. They live in different categories.
- Confidence: **HIGH**. The 40-tableau verification is exact; the structural mismatch is forced by the definitions, not by a translation ambiguity.

## Part 1: Reconstruction of Cao-Huang's Example 4.4

### Method

1. Hand-extracted the 40 (label, row1, row2) entries from page 10 of the PDF (image-rendered, the only reliable source — pdftotext mangles the grid).
2. Implemented the statistic readout from Cao-Huang's text (and fixed the obvious typo in the paper: a_4 is *#row-1 entries > bar2* — i.e. the count of bar1's in row 1 — not "> 2" as the paper accidentally writes; Figure 7 confirms the correction).
   - `a_1 = #{row 2 entries > 2}`
   - `a_2 = #{row 1 entries > 1} + #{row 2 entries > bar2}`
   - `a_3 = #{row 1 entries > 2}`
   - `a_4 = #{row 1 entries > bar2}` (i.e. `#{row 1 bar1's}`)
3. Implemented the inverse T_from_a using the three cases of Theorem 4.2 (Figures 7, 8, 9).
4. Parsed each label `f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_λ` into the tuple (a_1, …, a_4) using right-to-left alignment with the pattern (f_2, f_1, f_2, f_1).

### Result: 40/40

All 40 tableaux verify:
- The row-statistics match the parsed label exponents exactly.
- T_from_a(stats(T), 1, 2) returns T.
- The 40 admissible (a_1, ..., a_4) from Cao-Huang's inequalities (3.1) are exactly the 40 distinct quadruples occurring in Example 4.4.

Independent dim-checks (Weyl formula vs |F|):

| λ | shape | dim L(λ) | |F| |
|---|---|---|---|
| 2ω_1 + 0ω_2 | (2,0) | 10 | 10 |
| 0ω_1 + 1ω_2 | (1,1) | 5 | 5 |
| 1ω_1 + 1ω_2 | (2,1) | 16 | 16 |
| 2ω_1 + 1ω_2 | (3,1) | 35 | 35 |
| 1ω_1 + 2ω_2 | (3,2) | 40 | 40 |

All checks pass. **The Cao-Huang bijection is fully captured.**

Full per-entry table is in `check.py` output (stdout from `python3 check.py`).

## Part 2: Rick's B_2 short-simple Aug~ setup

From `/home/agent/projects/proofs/2026-05-14-coideal-commutativity-B2.md` and `b_i_b2.py`:

- B_2 conventions: α_1 = ε_1 − ε_2 (long), α_2 = ε_2 (short). Positive roots: β_{1,1}=α_1, β_{1,2}=α_1+α_2 (= ε_1, short, fixed by s_2), γ_{1,2}=α_1+2α_2 (= ε_1+ε_2, long), β_{2,2}=α_2 (short).
- Convex order from w_0 = s_1 s_2 s_1 s_2: β_{1,1} ≺ β_{1,2} ≺ γ_{1,2} ≺ β_{2,2}.
- s_i-orbits on Φ^+:
  - {β_{1,2}, β_{2,2}} under s_1 (short-short pair, k(1)=1).
  - {β_{1,1}, γ_{1,2}} under s_2 (long-long pair, k(2)=2).
- Aug~_i is the *orbit-swap*: e-direction increments the chain-top counter and decrements the chain-bottom (or vice versa for f-direction). It lives on **Kostant partitions** π ∈ Kp(∞) of n^−.

The operator Aug~_2 (B_2 *short* simple, i.e. simple root α_2 of B_2) acts as
  c_{γ_{1,2}} → c_{γ_{1,2}} − 1, c_{β_{1,1}} → c_{β_{1,1}} + 1,
which is a *weight-changing* move: it shifts the underlying weight by γ_{1,2} − β_{1,1} = 2α_2 = 2ε_2.

## Part 3: The comparison

### What I was asked

"Apply both bijections at C_2 ≅ B_2 to a small common λ. Are the underlying tableau-to-Verma-vector identifications the same bijection, or different?"

### What I found

**They are not bijections of the same kind.** Specifically:

1. **Cao-Huang.** A bijection
   KN_λ(4) ⇄ { (a_1, ..., a_4) admissible by (3.1) } ⇄ { f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_λ } ⊂ L(λ).
   *Single weight-graded direct sum L(λ) = ⊕_μ L(λ)_μ; both sides equinumerous at each weight; bijection is intra-L(λ).*
   Reduced word fixed: w_0 = r_1 r_2 r_1 r_2.

2. **Rick's Aug~.** An *operator* on the crystal Kp(∞) = B(∞), shifting weight by 2α_2 (B_2 short simple), implementing an orbit-swap on root multiplicities.
   Kp(∞) is the crystal of U_q(n^−); it parameterizes a PBW basis (with multiplicity in each weight, no fixed λ). It is *bigger* than L(λ): #{π ∈ Kp(∞) : wt(π) = lλ − μ} ≥ dim L(λ)_μ.

   Concrete data for λ = 3ε_1 + 2ε_2 (from `check.py`):

   | weight μ | dim L(λ)_μ = #a-tuples | #π ∈ Kp(∞) | overcount |
   |---|---|---|---|
   | (3, 2) | 1 | 1 | 0 |
   | (2, 1) | 2 | 3 | +1 |
   | (1, 0) | 3 | 6 | +3 |
   | (0, −1) | 3 | 10 | +7 |
   | (−1, −2) | 2 | 15 | +13 |
   | (−3, −2) | 1 | 26 | +25 |

   Total: 40 a-tuples vs 226 π-tuples over the 24 weights. **The two parameter sets do not biject.**

3. **No natural map.** Even if one fixed a sub-locus of Kp(∞) that hits L(λ) bijectively (e.g. via a Kashiwara cut-off), the resulting parameter would be a Kostant partition π = (c_{β_{1,1}}, c_{β_{1,2}}, c_{γ_{1,2}}, c_{β_{2,2}}), whose entries are PBW exponents. Cao-Huang's (a_1, ..., a_4) are *not* PBW exponents: they are LMNP "monomial in simple-root vectors" exponents along the reduced word w_0 = r_1 r_2 r_1 r_2. The two differ by Lusztig straightening, with lower-order corrections that are precisely the q(Y) coefficients of Cao-Huang's Proposition 5.4 (the column-strict tail). At rank 2 these corrections are non-trivial — they appear as soon as a_2 ≥ 2 or a_4 ≥ 1.

4. **Short/long swap is not the obstacle.** Even after the C_2 ↔ B_2 short/long swap (Cao-Huang α_1 ↔ Rick α_2, Cao-Huang α_2 ↔ Rick α_1, and reduced word r_1 r_2 r_1 r_2 ↔ s_2 s_1 s_2 s_1), the structural mismatch persists because it is about *which side L(λ) sits on* (rep-theory vs crystal of n^−), not about labeling conventions.

5. **What Aug~ would need to be a Cao-Huang move.** For Aug~ to act *within* a single L(λ) (i.e., to be a relabeling map between Verma vectors), it would have to preserve weight. Rick's Aug~ at B_2 short simple does *not* preserve weight: it shifts by 2α_2. So even in principle Aug~ is not "the bijection at fixed λ" — it is at best a generator of moves *between* Cao-Huang's bijections for *different* λ, which is not what Cao-Huang constructs.

### Verdict

**NO** — Cao-Huang's bijection at C_2 does **not** agree with Rick's implicit bijection at B_2 short simple after short/long relabeling. The disagreement is **structural**:

- Cao-Huang's map is a parameter-set bijection at *fixed* weight λ between two equinumerous parameterizations of L(λ).
- Rick's Aug~ is a *weight-shifting operator* on Kp(∞) ⊃⊃ L(λ).

These are different kinds of mathematical objects. There is no "bijection" of Rick's that can be matched against Cao-Huang's, because Aug~ is not a bijection — it is a (q,t)-graded differential / orbit-swap operator on a strictly larger object (the U_q(n^−) crystal).

The 40-element finite check still has *some* informational value:
- It confirms Cao-Huang's monomial PBW-style basis is realized exactly by 40 a-tuples and 40 KN tableaux at λ = ω_1+2ω_2.
- It shows that *even within a single weight space*, the count of Kostant partitions in Kp(∞) overcounts dim L(λ)_μ — so any candidate identification "Aug~-target tableau in Kp(∞)" → "Cao-Huang vector in L(λ)" is many-to-one, not 1-1.

### What would still be worth doing (out of scope here)

1. **Braid-move transition matrix.** Compute the change-of-basis from Cao-Huang's monomial basis for w_0 = r_1 r_2 r_1 r_2 to the same monomial basis for w_0' = r_2 r_1 r_2 r_1 (the other reduced word). This is a square 40 × 40 unipotent transition; its non-zero entries are *candidates* for what an "Aug~ for rep-theory" should be. The structure of this matrix at rank 2 is the closest analogue, on the rep-theory side, of Rick's 6 net moves. The braid relation r_1 r_2 r_1 r_2 = r_2 r_1 r_2 r_1 *is* the m_{12}=4 / three-strand-style relation Rick has been chasing, and this transition matrix is where one should look for a finite confirmation.

2. **Marginally-large cut-off in Kp(∞).** Restrict Kp(∞) to the marginally-large locus (Hong-Lee / Salisbury–Tingley) so it bijects with B(L(λ)). On this locus, Aug~ becomes a partial operator with a well-defined image inside L(λ). Then ask: does Aug~ define a graph on KN_λ(4) (via the CST bridge Ψ) whose edges are recognizable from Cao-Huang's combinatorics? This is *the* meaningful finite check, but requires implementing Ψ at B_2 and is bigger than the 40-element verification asked for here.

## Confidence

**HIGH.** The 40-element verification is exact and the structural mismatch is not a translation artifact: it is forced by the fact that Aug~ shifts weight while Cao-Huang's bijection is at fixed weight. The C_2 ↔ B_2 root-swap was carefully tracked and does not resolve the mismatch.

## Files

- Code: `/home/agent/projects/proofs/2026-05-16-cao-huang-cross-check/check.py`
- This writeup: `/home/agent/projects/proofs/2026-05-16-cao-huang-cross-check/result.md`
- Source notes (Cao-Huang reading): `/home/agent/projects/memory/reading/papers/2026-05-16-cao-huang-2604-19490-notes.md`
- Rick's B_2 Aug~ note: `/home/agent/projects/proofs/2026-05-14-coideal-commutativity-B2.md`
- Rick's B_2 Aug~ code: `/home/agent/projects/proofs/remark47/coideal_check/b_i_b2.py`
