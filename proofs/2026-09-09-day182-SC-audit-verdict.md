# Day 182 — SC Audit Verdict

**Date:** 2026-09-09.
**Audited proof:** `proofs/2026-09-09-day181-SC-attempt.md` (Day 181
sub-agent attempt at sub-claim (SC), Fact 8's last conditional dependency).

## VERDICT — **HOLDS.**

The Day 181 sub-agent's proof of (SC) is correct. All three ingredients
(u_i u_j-lemma §3.1, splitting §3.2, key vanishing §3.3) and both
reductions (§3.4 for m'' ∈ ℚ[E₁,E₂] and §3.5 for E₃-factors) survive
independent re-derivation from scratch.

**The Day 181 wake pre-audit ρ-convention worry was a misreading**:
the sub-agent's §3.3 uses ρ(A) = ρ(B) = 1 (Rick's Day 179 convention),
not ρ(A) = 2 as feared. Under ρ(A) = ρ(B) = 1 the ρ-count
$\rho(A^a B^b p_{l+b+2d}^{\text{[top]}}) = a + b + (l + b + 2d) =
2r - a + l$ (using $a+b+d=r$) is strictly DECREASING in $a$, so the
maximum $\rho = 2r + l$ is achieved uniquely at $a = 0$, and at $a = 0$
the binomial $\sum_b\binom{r}{b}(-1)^b = 0$ collapse applies. The
sub-agent's argument is therefore correct in Rick's convention.

## Audit protocol — per-step results

### Step 1: Read cold — done

Read the proof file top to bottom. Load-bearing step identified:
**§3.3 (key vanishing $M_l(f)^{\text{[top]}} = 0$)**. Everything else
follows from §3.3 by elementary linearity/binomial arguments.

### Step 2: §3.1 (u_i u_j-lemma) — PASS

Independent re-derivation via manual Newton reduction (not sympy.symmetrize).
Verified:
- $p_r \bmod E_{\ge 4}$ has top-ρ piece $E_1^r$ at ρ = r, for r = 1..6.
- Pair-monomial identity $M = p_a p_b - p_{a+b}$ (or $p_a^2 - p_{2a}$) has
  top-ρ slice $= 0$ at ρ = $a+b$, for $(a,b)$ with $a, b \in \{1,\ldots,4\}$
  (10/10 pass).
- Full lemma statement on random symmetric $f = u_i u_j \cdot g$ at
  $n = 4, 5$: 10/10 trials pass.

Script: `scratch/day182/audit_step2_uiuj.py`.

### Step 3: §3.3 (KEY VANISHING) — PASS

**Convention resolution.** The Day 181 wake pre-audit worried that the
sub-agent might have claimed ρ(A) = 2. Actual reading: the sub-agent's
formula
$\rho(A^a B^b p_{l+b+2d}^{\text{[top]}}) = a + b + (l+b+2d)$
decomposes as ρ(A^a) + ρ(B^b) + ρ(p^{[top]}), giving ρ(A) = ρ(B) = 1.
This matches Rick's Day 179 convention exactly. Sub-agent even says
explicitly (§3.2): *"Naive top-ρ = $2r+\rho(m'')+1$ (routine count using
ρ(A) = ρ(B) = 1)."* No convention discrepancy. Pre-audit worry
withdrawn.

**Why a=0 is special under ρ(A)=1.** Under $a+b+d=r$:
$\rho \le a + 2b + 2d + l = a + 2(r-a) + l = 2r - a + l$,
strictly decreasing in $a$. Maximum $2r+l$ at $a=0$ only.
(Pre-audit's alternative worry that the count would be constant
in $a$ under ρ(A)=2 was also wrong: under ρ(A)=2, the count is
$2a + b + (l+b+2d) = 2(a+b+d) + l = 2r + l$, constant in $a$ —
which would kill the sub-agent's mechanism. But that's not the
convention the sub-agent uses. Both convention worries fail.)

**Independent numerical verification.** Fresh script computing $M_l(f)$
via manual Newton reduction mod $E_{\ge 4}$ (no sympy.symmetrize):
- Multinomial expansion of $(A - Bu + u^2)^r$ for $r = 1..4$: 24/24 coefficients match.
- ρ-count of $A^a B^b p_m^{[\text{top}]}$: 6/6 test cases match $a+b+m$.
- $M_l(f)^{[\text{top}, 2r+l]} = 0$ at $(r, l) \in \{1..5\} \times \{0..3\}$: 20/20 pass.

Script: `scratch/day182/audit_step3_key_vanishing.py`.

**Verdict on §3.3:** the load-bearing step is fully rigorous. The
$(1-1)^r = 0$ collapse is the whole story.

### Step 4: §3.2 (splitting) and §3.4–3.5 (reductions) — PASS

**§3.2 splitting** $X_{ij}^r = \alpha_r(u_i, u_j) + u_iu_j\beta_r(u_i, u_j)$
with $\alpha_r = f(u_i) + f(u_j) - A^r$:
verified symbolically for $r = 1, 2, 3$ that $X_{ij}^r - \alpha_r$
vanishes at $u_i = 0$ and $u_j = 0$, hence divisible by $u_iu_j$ (Bezout).

**§3.4 reduction to m'' = E_2^b.** At $n = 5$: (SC) bound $\rho(T^{X,r}(E_2^b)) \le 2r+b$
verified 6/6 for $(b, r) \in \{0, 1, 2\} \times \{1, 2\}$. In every case
the observed max ρ equals the (SC) bound exactly — bound is tight.

**§3.5 E_3-extension.** At $n = 5$: (SC) bound verified 8/8 for
$m'' \in \{E_3, E_3^2, E_1 E_3, E_2 E_3\}$ and $r \in \{1, 2\}$. Again
bound is tight (observed max ρ = (SC) bound).

Argument review:
- The $E_3$-induction identity $T^{X,r}(E_3^c \mu) = \sum_k \binom{c}{k}
  E_3^{c-k} T^{X,r+k}(\mu)$ is a direct consequence of $E_3|_{ij} =
  E_3 + X_{ij}$ (Day 179 §1). No circularity: each $T^{X,r+k}(\mu)$
  with $r \ge 1, k \ge 0$ hence $r+k \ge 1$ and $\mu \in \mathbb Q[E_1,E_2]$
  is covered by §3.4.
- $E_1$-linearity $T^{X,r}(E_1 m''') = (E_1 + 2)T^{X,r}(m''')$
  and its ρ-consequence (top piece = $E_1 \cdot \pi_\rho T^{X,r}(m''')$)
  is elementary. Argument identical to Day 179 (R1).

Script: `scratch/day182/audit_step4_split_reduce.py`.

## Registry actions

**Promote (SC).** Move `day181-sub-claim-SC` in
`registry/conjecture-P.json` from `trust: computed` to
`trust: checked-sober`. Add `recheck` field:
```
"recheck": "Day 182 audit 2026-09-09: independent re-derivation
scratch/day182/audit_step{2,3,4}_*.py. §3.3 mechanism verified with
Rick's ρ convention (ρ(A) = ρ(B) = 1); pre-audit worry about ρ(A) = 2
was a misreading of the sub-agent's formula. All 4 audit steps clean.
Boundary: checked-sober, not proved — Clio should review before
promotion to publishable."
```

**Promote Lemma 1 (arity-0 identity, day178-lemma1-arity-0-identity).**
Was checked-sober on ℚ[E₁,E₂]-slice (Day 179 §3 rigorous) +
computed on E₃-slice (contingent on SC). Now: **checked-sober on full
ℚ[E₁,E₂,E₃]-slice**. Trust cap remains checked-sober (not proved)
until Clio audits (SC).

**Promote Lemma 2 (day178-lemma2-higher-arity-vanishing).** Was already
`proved` unconditionally (Day 180 MVL). No change.

**Promote Fact 8.** Was `proved on E₃-free slice` + `checked-sober++ on
ℚ[E₁,E₂,E₃]-slice`. Now: **checked-sober on full ℚ[E₁,E₂,E₃]-slice**
(unified language; drop the "++" hedge since (SC) is now checked-sober
in the strict sense). Cap: pending Clio review.

**DO NOT unilaterally promote (SC), Lemma 1, or Fact 8 to `proved`**
per Day 182 protocol. `checked-sober` is Rick's boundary; `proved`
requires (a) written proof file (already have), (b) Clio's independent
audit or a second sober re-derivation on a fresh day.

## What comes next

1. **Send to Clio.** Reply PDF summarizing (SC) + audit for her review.
   Include the ρ-convention clarification since Clio has been sharp on
   convention discrepancies (Q99, Q105 both hinged on similar concerns).
2. **Consider Clio-review-then-promote pipeline for arc close.** If
   Clio's audit closes clean, Fact 8 → `proved` on full ℚ[E₁,E₂,E₃]
   slice. Then Day 175 closed form promotes to `proved` on full slice;
   Day 172 (A) settles as `proved`; Day 174 recursion settles.
3. **Rule 11 scorecard:** 9-1 (audit step also purely elementary; every
   substantive move was Newton mod $E_{\ge 4}$ + binomial). Arc-2
   remains extremely consistent.

## Notes on the sub-agent proof file

The proof file is unusually well-organized:
- §5 correctly identifies §3.3 as the load-bearing step.
- §7 correctly names the files.
- §8 self-grades at `checked-sober` (below what the sub-agent claims to
  have) and defers to Rick — this is exactly the right etiquette per
  session rules.
- §9 postmortem is honest about which move got furthest.

One nit: the proof file says the (SC) bound is "$\le 2r + \rho(m'')$" and
"drops from naive $2r + \rho(m'')+1$." The numerics (§4, my §4) confirm
the bound is TIGHT — observed max ρ equals bound in every case tested.
So (SC) is a sharp equality "up to strict inequality on average" claim;
the "drops by 1" is the effective content. Worth noting for future
Fact 8 uses that this bound is TIGHT, not slack.

## Files (audit day)

- `scratch/day182/audit_step2_uiuj.py` — §3.1 independent verification.
- `scratch/day182/audit_step3_key_vanishing.py` — §3.3 mechanism + ρ-count + numerics.
- `scratch/day182/audit_step4_split_reduce.py` — §3.2/3.4/3.5 verification.
- `proofs/2026-09-09-day181-SC-attempt.md` — audited proof file.
- This file — verdict.

## Pre-registered predictions — postmortem

Day 182 pre-registered no explicit predictions (audit-only session, no
new results). Implicit prior: "60% audit clean, 30% gap found and named,
10% proof incorrect." Outcome: **audit clean.**

The pre-audit's specific worry (ρ(A) = 2) turned out to be a misreading —
lesson: when a session's pre-audit spots a specific gap, verify the
sub-agent's LITERAL claim before working out downstream implications.
The pre-audit derived a wrong implication from a claim the sub-agent
did not make.
