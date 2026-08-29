---
title: Day 112 — (⋆⋆⋆) status: reduction FAILS as stated; H_c cancellation is the real mechanism
status: NEGATIVE at S_j-level; (⋆⋆) at H_c-level still empirically true; needs new proof strategy
---

# Sub-sub-claim (⋆⋆⋆) — status report

## Precise statement (from T-verification writeup)

The T-verification writeup (`/home/agent/projects/proofs/2026-08-19-day112-T-verification.md`,
line 141–146) formulates (⋆⋆⋆) as:

> *(⋆⋆⋆)* The coefficient $[a^{i - i_P} b^{k - i_Q}] S_j(a, b, c)$ has $j$-degree $\leq p_S$,
> where $S_j = ds_j/V$ and $p_S = 2j - [(i-i_P) + (k-i_Q)]$.

Since $(i - i_P, k - i_Q)$ are fixed exponents (for fixed slot $(i,k)$ and fixed $(i_P, i_Q)$),
the natural reparameterization is
$$u := c - 1 - i - p_P, \qquad v := c - 1 - k - p_Q$$
(both constants for fixed choices), giving $u + v = p_S$ and the exponents
$(i - i_P, k - i_Q) = (j - u, j - v)$. So (⋆⋆⋆) becomes:

**(⋆⋆⋆)ʹ**  Define $C_{u,v}(j) := [a^{j-u} b^{j-v}] S_j$. Then $j\text{-deg}(C_{u,v}) \leq u + v$.

## Empirical verification of (⋆⋆⋆)ʹ — extended to $R = 6$

**Script:** `/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify-v2.py`.
**Log:** `/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify-v2.txt`.

For $c = 25$, $j = 1, \ldots, 16$, we computed $C_{u,v}(j)$ at every slot $(u, v)$ with
$u + v \leq 6$ and fit each as a polynomial in $j$. Results:

| $r = u + v$ | slot $(u, v)$ | observed $j$-deg | bound $r$ |
|-------------|---------------|------------------|-----------|
| 0 | $(0,0)$              | 0  | 0  ✓ |
| 1 | $(0,1), (1,0)$       | 2  | 1  **VIOLATION** |
| 2 | $(0,2), (1,1), (2,0)$| 4  | 2  **VIOLATION** |
| 3 | all                  | 6  | 3  **VIOLATION** |
| 4 | all                  | 8  | 4  **VIOLATION** |
| 5 | all                  | 10 | 5  **VIOLATION** |
| 6 | $(0,6),(6,0)$: 10; $(1,5),(5,1)$: 11; $(2,4),(3,3),(4,2)$: 12 | 12 | 6 **VIOLATION** |

**Observed pattern:** $j\text{-deg}(C_{u,v}) = 2(u + v)$ (with the outermost slots at $r = 6$
dropping slightly to $10$–$11$, presumably a finite-sample artifact of the fit or a genuine
edge effect requiring more $j$ samples).

**Conclusion:** (⋆⋆⋆) as stated in the T-verification writeup is **empirically FALSE**.
The $j$-degree of the raw coefficient $C_{u,v}(j)$ is $\sim 2(u+v)$, not $\leq u + v$.

Explicit examples ($c = 25$):
- $C_{0,1}(j) = j(2c + 1 - j)/2 = j(51 - j)/2$, degree exactly $2$ (bound was $1$).
- $C_{1,1}(j)$ at $c = 25$ is $j(j^3 - 104 j^2 + 2603 j - 2300)/4$, degree exactly $4$
  (bound was $2$).

## Where the reduction breaks

Rick's H_c-level claim (⋆⋆) — that the coefficient of a fixed $a^i b^k$ slot in
$H_c(a, b, j) = P_j(a) Q_j(b) S_j$ has $j$-degree $\leq d = \text{TOP} - i - k$ — is
**empirically TRUE** (verified for $R = 2, 3, 4, 5$ at 91 slots, zero violations; see
`2026-08-19-T-sub-claim-verify.txt`). The reduction chain was:

1. $[a^{i_P}] P_j$ has $j$-degree $\leq p_P$. ✓ (this is the elementary-symmetric fact)
2. $[b^{i_Q}] Q_j$ has $j$-degree $\leq p_Q$. ✓
3. **(⋆⋆⋆)** $[a^{i-i_P} b^{k-i_Q}] S_j$ has $j$-degree $\leq p_S$. **✗**

Steps 1, 2, 3 combined would give product $j$-degree $\leq p_P + p_Q + p_S = d$, hence
(⋆⋆). But step 3 is false: the true bound is $\leq 2 p_S$, so the naive product bound
is $p_P + p_Q + 2 p_S$, which can exceed $d$ when $p_S > 0$.

**Yet (⋆⋆) still holds.** So there must be **substantial cancellation** in the
$(i_P, i_Q)$-convolution summing over the elementary-symmetric coefficients of the
Pochhammer factors and the S_j slot coefficients. The leading-in-$j$ piece of
$C_{j-\text{shift}, \ldots}$ must cancel against the Pochhammer's leading-in-$j$ piece.

## $\kappa_\mu$ combinatorics — enumeration

For fixed $\mu_3 = r$ and $\mu_2 = r + s$, $\mu_1 = 2j - 2r - s$, we tabulated
$\kappa_\mu$ (script `2026-08-19-star-star-star-verify.py`, section
`enumerate_kappa_by_mu3`). Empirical $j$-degrees:

| $r$ | $s$ | first $\kappa_\mu$ samples | $j$-deg fit |
|-----|-----|----------------------------|-------------|
| 0 | any $s$ | single sample (unique $\mu = (j,j,0)$, $\kappa = 1$) | 0 |
| 1 | 0..4 | 1, 2, 3, 4, 5 (at $j = s + 2$) | 0–1 |
| 2 | 0 | 1, 2 (at $j = 3, 4$) | 1 |
| 2 | 4 | 15, 20 (at $j = 7, 8$) | 1 |
| 3 | 0 | 5, 5 (at $j = 5, 6$) | 0 |
| 3 | 1..4 | polynomial-in-$j$ | 1 |
| 4 | 0..4 | polynomial-in-$j$ | 2 |

**Conjecture (still standing):** $\kappa_\mu$ for $\mu = (2j-2r-s, r+s, r) \in \mathcal{S}_j$
is a polynomial in $j$ of degree $\leq r$ (empirically $\leq \lfloor r/2 \rfloor + \varepsilon$
in the tested range — very likely the correct sharp bound is $\lfloor r/2 \rfloor$).

**Combinatorial interpretation:** $\kappa_\mu$ counts vertical-2-strip walks
$\emptyset \to \mu$ of length $j$. Each step adds two cells (one per column-index chosen
from $\{1, 2, 3\}$ under the partition constraint). To end with $\mu_3 = r$, exactly $r$
of the $j$ steps must have added a cell to row 3. The remaining $j - r$ steps distribute
between rows 1 and 2. The $\binom{j}{r}$-like factor for the placement of the "row-3 steps"
is a polynomial in $j$ of degree $r$; the residual walk arithmetic can reduce this to
degree $\leq \lfloor r/2 \rfloor$ or so by parity constraints.

## What DOES seem to be true (revised conjecture)

The relation between $S_j$'s coefficients and the higher-degree cancellation in H_c
suggests a stronger combined statement:

**(⋆⋆) at H_c level** (holds empirically): every $[a^i b^k]$ coefficient of $H_c(a,b,j)$
has $j$-degree $\leq \text{TOP} - i - k$.

**Refined pattern:** $j\text{-deg}([a^i b^k] H_c) = 2 \min(p, q)$, where
$p = (c-1) - i$, $q = (c-1) - k$ (displacements from corner). This is $\leq p + q = d$
and always even.

**Structural mechanism** (not proved): the cancellation must come from a
Newton-interpolation-type identity that relates the elementary symmetric
polynomials $e_i(3, 4, \ldots, c+1-j)$ in the Pochhammer expansion to the
shifted-Schur coefficients $\kappa_\mu \cdot s^*_\mu$ in $S_j$. Concretely,
the top-$j$-degree part of $C_{u,v}(j)$ must be a specific polynomial in $(u, v, c)$
that gets annihilated by the elementary-symmetric contributions when convolved.

## Correct path forward

Given (⋆⋆⋆) is false as stated, three options:

**Option A: Prove (⋆⋆) directly at H_c level.**

Skip the intermediate (⋆⋆⋆) and prove (⋆⋆) via a global argument on
$H_c(a, b, j) = P_j(a) Q_j(b) S_j(a, b, c)$. Candidate strategies:

1. **Shift-and-conquer.** Write $H_c(a, b, j)$ as a symmetric function evaluated
   at "shifted variables" $a, b$ with $j$ playing the role of a discrete
   deformation parameter. The Sahi-Okounkov interpolation Macdonald polynomials
   are exactly this kind of object; there may be a direct application.

2. **Recognize $S_j$ as a shifted-Schur polynomial.** The identity
   $S_j = \sum_\mu \kappa_\mu s^*_\mu$ with $\mathcal{S}_j$ being partitions of $2j$
   built by $j$ vertical 2-strips suggests $S_j = h_j^*[y_1 + y_2 + y_3]$ or
   $s_{(1^j)}^*$ evaluated at a plethystic argument. Verify via O-O tables.

3. **Convolution identity.** Prove that the top-$j$-degree part of
   $C_{u,v}(j)$ has the specific form $\binom{j}{u+v} \cdot F_{u,v}(c)$
   (i.e., a plain binomial coefficient), and that $F_{u,v}(c)$ satisfies
   a linear relation over $(u, v)$-tuples with fixed sum that matches the
   elementary-symmetric structure of $(a+3)_{c-1-j}$. Then convolution
   annihilation is a shifted-Chu-Vandermonde argument.

**Option B: Use (T-a) + (T-b) split.**

The T-verification writeup notes that (T) equals (T-a) ∧ (T-b), where each
is a 1D degree bound. Empirically both hold. A univariate finite-difference
argument may be much simpler than the 2D version. Recommended for a fresh attempt.

**Option C: Direct proof of (I) via interpolation on the Sahi-Okounkov grid.**

Skip (T) entirely and prove the interpolation-ansatz identity (I) directly.
This requires an explicit Newton interpolation of $Q_{2R}$ on a chosen grid.
Requires more work but might yield a stronger structural theorem.

## Bottom line

- **(⋆⋆⋆) as stated in the T-verification writeup is FALSE at the S_j level.**
  Empirical $j$-degree of $C_{u,v}(j) := [a^{j-u} b^{j-v}] S_j$ is $2(u+v)$,
  not $\leq u + v$.
- **Rick's H_c-level (⋆⋆) still holds** (verified for $R = 2, 3, 4, 5$).
  The naive S_j → H_c reduction fails because the required cancellation
  happens *inside* the $P_j \cdot Q_j \cdot S_j$ convolution, not at $S_j$ alone.
- **Recommendation:** revise the proof strategy. The cleanest path is
  probably **Option B (T-a + T-b split via 1D finite differences)**.
  The reduction attempted in the T-verification writeup needs to be dropped
  or replaced by a genuinely stronger convolution-cancellation argument
  (Option A.3).

**Assessment.** This is a real gap in Rick's proof program. The empirical (⋆⋆) at
H_c-level is robust, but the combinatorial reduction to $S_j$ needs to be redone.
Given the observed pattern $j\text{-deg}([a^i b^k] H_c) = 2 \min(p, q)$ (only EVEN
values, and only the smaller-displacement coordinate matters), the cancellation
must exploit the $(a \leftrightarrow b)$-symmetry of $ds_j/V$. This suggests the
right proof is via SYMMETRY of $S_j$ rather than layer-by-layer degree counting.

**This is a matter for Rick's direct attention** — the substantive question is
"why does the H_c convolution have MUCH better $j$-degree bounds than the naive
product bound?" and the answer likely involves a clean symmetric-function identity
we haven't identified yet.

## Files

- Verification script v2: `/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify-v2.py`
- Log v2: `/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify-v2.txt`
- Verification script v1 (kappa enumeration): `/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify.py`
- Log v1: `/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify.txt`
- T-verification writeup with original (⋆⋆⋆): `/home/agent/projects/proofs/2026-08-19-day112-T-verification.md`
