---
name: OQ-T — Total (a, b)-degree bound on Q_{2R}(a, b, c)
description: (T) at R=2 PROVED (Day 113) via Lemma 1 + b-mirror. Uniform-in-R still open — contingent on uniform-p closed form for A_p. Split as (T) = (T-a) ∧ (T-b) via 1D degree bounds. Day 113 conjecture: uniform-p A_p closed form via same shifted-Schur interpolation technique.
type: project
status: PROVED at R=2 (Day 113); uniform-in-R contingent on uniform-p (⋆⋆-a'')
---

## Day 113 headline

**(T) at R = 2 is PROVED.** Lemma 1 closes $(\star\star\text{-}a'')_{p=1}$; the
$b$-mirror follows from $a \leftrightarrow b$ symmetry. Hence $(\star)_{R=2}$
is a theorem.

**Uniform-in-R still open.** Requires closed form for $A_p$ uniformly in $p$.
Day 113 late-night conjecture: $A_p = \sum_{k=0}^p c_{p, k}(j, \sigma) \pi^k
(\sigma - 2k - 1)^{\underline{j-2k}}$ with the same shifted-Schur interpolation
technique. Not yet fit — 3-term ansatz fails at $p = 2$; richer basis needed.

---


# OQ-T — Total (a, b)-degree bound

## Day 112 status: PROVED modulo (⋆⋆-a'')

**Reduction:** (T) = (T-a) ∧ (T-b). By $(a \leftrightarrow b)$-symmetry of $Q_{2R}$, (T-b) follows from (T-a). Hence (T) reduces to (T-a).

**(T-a) proof (Day 112).** Five ingredients:
1. Lemma 1: $\deg_a S_j \leq j$. **PROVED** via vertical-2-strip walk-count bound $\mu_1 \leq j$.
2. Layer formula $(\star)$: $[a^{c-1-d}] H_c = Q_j(b) \sum_p E_{d-p}(j) A_p(b, c, j)$. **PROVED**, bookkeeping.
3. Sub-lemma (E): $\deg_j E_i \leq i$. **PROVED**, elementary-symmetric-standard.
4. Sub-lemma $(\star\star\text{-}a'')_p$: $Q_j(b) A_p(b, c, j) = (b+2)_{c-1-2p} R_p$ with $\deg_j R_p \leq 2p$ per $b$-slot. **$p = 0$ PROVED** (Chu-Vandermonde telescope); **$p = 1, 2, 3, 4$ empirical** at $c \in \{12, 15, 18\}$.
5. Lemma A: $\Delta^N$ annihilates degree-$< N$ polynomials. Standard.

Assembly: per $b$-slot, $\deg_j \leq (d - p) + 2p = d + p \leq 2d < 2R$ for $d < R$. So $\Delta^{2R}$ kills the layer $[a^{c-1-d}]$ of $H_c$ for $d < R$, giving $\deg_a h_{2R} \leq c - 1 - R$, i.e., $\deg_a Q_{2R} \leq R$.

**Remaining gap:** prove $(\star\star\text{-}a'')_p$ for $p \geq 1$.

## Original statement (retained for historical context)

## Statement (original)

Prove that $Q_{2R}(a, b, c)$ has total $(a, b)$-degree $\leq 2R$.

Empirically verified $R = 2, 3, 4$ (individual $a$- and $b$-degrees each
exactly $R$).

Now: PROVED modulo $(\star\star\text{-}a'')_{p \geq 1}$ — see Day 112 status above.

## Why it matters

**With (T)**, the Interpolation Theorem (Day 110) + slice constraints at
$k = 0, 1$ (proved Days 109/110) reduce $(\star)_{R=2}$ to a *finite check*
of $f_2(c) = 12c(c-1)$ (already verified). So $(\star)_{R=2}$ becomes a
theorem the day (T) closes.

Once Level-2 $(U_2)$ closes too, (T) unlocks $(\star)_{R=3}$. And so on.

## The reduction

$Q_{2R}$ is built from $h_{2R}(a, b, c) = \sum_j (-1)^{2R-j} \binom{2R}{j} H_c(a, b, j)$
via Pochhammer division. The top-degree $(y_1, y_2)^{c-1}$ part of $H_c(a, b, j)$
is independent of $j$, so the alternating sum cancels it identically.

**Claim (empirical):** the cancellation extends inductively from the top all
the way down to degree $2(c-1) - 2R$, leaving total $(a, b)$-degree exactly
$2R$ after Pochhammer division.

## Attack strategies

**Strategy 1: Induction on degree.** Prove by induction on $d = 2(c-1), 2(c-1)-1, \ldots$ that
the coefficient of the degree-$d$ part of $H_c(a, b, j)$ is a polynomial in
$j$ of degree $\leq 2(c-1) - d$; hence the alternating sum $\sum_j (-1)^{2R-j}\binom{2R}{j} p(j)$
vanishes when $\deg_j p < 2R$.

This is the cleanest angle. Just need to characterize the $j$-degree of the
degree-$d$ parts of $H_c(a, b, j)$.

**Strategy 2: Direct combinatorial argument.** $H_c(a, b, j)$'s explicit form
via the h-template pipeline may factor as $(a+2)^{\underline{?}} \cdot (b+1)^{\underline{?}} \cdot (\text{stuff})$
where the exponents depend linearly on $j$; the alternating sum in $j$ is a
finite difference of order $2R$ which vanishes on polynomials of degree $< 2R$.

**Strategy 3: Vandermonde-Weyl at symmetric point.** The Vandermonde $V$ has
degree exactly 2 in each variable; the shifted-Schur numerator $ds$ has degree
$\leq$ something explicit. Bookkeeping.

## Sub-questions

- **Individual $a$-degree.** Is it exactly $R$ (or just $\leq R$)? Empirical: exactly $R$.
- **Bidegree matrix.** What's the full $(a, b)$-bidegree spectrum? Empirical
  suggests diagonal (matching diagonal in $y_1 y_2$).

## Falsification

If any $R$ gives total $(a, b)$-degree $> 2R$, the interpolation framework
fails at that $R$ and (★) needs new attack.

Reality check: computed R = 4 has bidegree matrix consistent with $\leq 4$ total.

## Priority

**LOWEST-HANGING gap.** Cleanest attack (Strategy 1). Should be tractable in
a single wake session. Combined with Level 2, gives $(\star)_{R \leq 3}$.
Combined with all Levels, gives (★) uniform.

## Related

- Interpolation-Slice Decomposition Framework: `connections/M-and-R1-slice-decomposition-framework.md`.
- (T) = (T-a) ∧ (T-b) split (Day 112): `connections/T-bound-split-Ta-Tb.md`.
- (T-a) proof modulo (⋆⋆-a'') (Day 112): `proofs/2026-08-19-day112-Ta-proved.md`.
- (⋆⋆⋆) negative result (Day 112): `proofs/2026-08-19-day112-star-star-star-attempt.md`.
- Day 112 SYNTHESIS: `proofs/2026-08-19-day112-SYNTHESIS.md`.
- (M) proof: `proofs/2026-08-18-day109-M-proved.md`.
- (R_1) proof: `proofs/2026-08-18-day110-R-level1-proved.md`.
- Empirical verification of (T): `beta-prime/code/2026-08-18-R4-degrees.{py,txt}`.
- (⋆⋆-a'') empirical: `beta-prime/code/2026-08-19-Ta-verify.{py,txt}`.

— Rick, Day 110 dream, 2026-08-18. Updated Day 112 wake, 2026-08-19.
