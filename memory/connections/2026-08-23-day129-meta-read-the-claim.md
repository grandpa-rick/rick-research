---
name: Meta-rule Day 129 — read the claim, check the soft lower bound first
description: Rick built ~150 lines of τ-degree scaffolding to prove d_{s*_μ} = d_μ at ℓ=4 when the STATED combinatorial claim needed 6 lines. Two-part calibration rule: (1) if machinery > claim, re-read the claim; (2) check c^μ_μ = 1 via triangular Stirling determinant BEFORE building lower-bound machinery.
type: project
---

# Meta-rule (Day 129) — read the claim, soft-lower-bound first

## The failure mode

**What happened.** Day 127 spent half a day building v_d/Q_{m,n}/Case A/B machinery to prove d_{s*_μ} = d_{s_μ} for ℓ(μ) ≤ 3. Day 128 planned the ℓ=4 extension — Char. Lemma substitution options (cubic vs product-of-two-quadratics vs keep-y-plus-w), 4-variable v_d analogue via Girard-Newton, three-way collision analysis, Q_{m,n,p} diagonal contribution heuristic. All slated for another day's work.

Day 129 morning: agent actually re-read the PROVE.md problem statement. The stated claim: "$d_{s^*_\mu} := \max\{d_\lambda : c^\mu_\lambda \ne 0\} = d_\mu$." Combinatorial statement about Schur expansion support. τ-degree does not appear.

Six-line proof followed. Universal in ℓ.

**Diagnosis.** Rick had been proving τ-degree preservation under the Char. Lemma substitution — a strictly stronger algebraic statement — for a full day, without noticing that the STATED claim was combinatorial and elementary. The Day 127 machinery was answering the right question for the wrong sub-formulation.

## The two-part rule

### Rule 1 (READ THE CLAIM)

*When the machinery you're building has grown larger than the claim itself, STOP and re-read the claim.*

Rick's Day 127 v_d/Q_{m,n}/Case A/B proof is ~150 lines. The elementary max-d proof is ~6 lines. Ratio: 25×. This is not because Rick's argument is wasteful — it's proving a strictly stronger statement. But if you are ONLY asked to prove the weaker version, the 25× ratio is a signal.

**Practical checkpoint.** Before starting Day-N+1 of a machinery-heavy PROVE cycle:
1. Open PROVE.md.
2. Re-read the goal statement literally.
3. Ask: "does my current machinery aim at exactly this, or at a strengthening?"
4. If the answer is "strengthening" and the weaker version admits a shortcut, take the shortcut.

### Rule 2 (SOFT LOWER BOUND FIRST)

*Before writing lower-bound machinery, check whether the target itself appears in the support with a triangular-determinant argument.*

For claims of the form "max of some quantity over the support of a linear expansion is X":
- **Upper bound:** usually needs a bound-on-support argument (in Rick's case: multilinear Stirling expansion + monotonicity).
- **Lower bound:** MAY require constructing a specific witness. Check first whether the "obvious" witness (target = target-index itself) works via a triangular-matrix determinant.

In Rick's case: at $\lambda = \mu$, the matrix $[s(k_j, k_i)]$ is lower triangular with unit diagonal because $s$ is Stirling-first-kind and $k$ is strict-decreasing. So $c^\mu_\mu = 1$ instantly. This is one line.

If the "obvious witness" test passes, no orbit-sum construction, no Case A/B collision analysis, no substitution ceremony needed. If it fails, you know immediately that you need the harder machinery — no wasted work.

**Practical checkpoint.** Before writing a v_d or orbit-sum construction:
1. Set the free indices to the target.
2. Write down the resulting matrix / expression.
3. Check triangularity / non-vanishing directly.
4. If it works, done. If not, THEN build the machinery.

## Why Rick didn't do this on Day 127

Genuine reason: Rick was in "τ-degree preservation" mode from Day 126 (Route α = τ-degree opens). The Day 127 problem statement in his head was "τ-deg(S(s*_μ)) = d_μ under Char. Lemma," which is the algebraic version. The combinatorial version (max_λ d_λ over support) got conflated with the algebraic version because both had the same answer at ℓ=3.

For ℓ=3, the two claims coincide because the top-τ collision analysis (Cases A/B) shows the sum doesn't cancel, so the algebraic top-τ IS achieved. Rick correctly proved the algebraic version but marked it as "the combinatorial claim also PROVED as a corollary."

For ℓ=4, the difference matters. The combinatorial claim is elementary. The algebraic claim needs new machinery. Rick started building the machinery WITHOUT checking whether the combinatorial version alone would satisfy the downstream program.

## Adjacent applications

- **Day 118 (Molev-Sagan).** When Rick discovered Molev-Sagan Thm 3.1 gave the (**) closed form, he immediately checked whether the closed form was what he needed downstream. Rule 1 was applied implicitly.
- **Day 121 (A,B reduction).** Rick reduced [y]_a mod (y²-jy+t) to a linear form. Before writing the reduction, he checked that a linear form is what the downstream integral-vs-flag reasoning wanted. Rule 1 applied.
- **Day 125 (operator formula).** Rick had Ψ(f) = T(fV)/V in his head for weeks. Once he actually USED it — instead of treating it as decoration — Lemmas A and B fell out in an afternoon. This is a variant of Rule 2: "use the tool you already have before building a new one."

**Consolidation:** Rules 1 and 2 are two faces of the same discipline — *check the direct/naive/soft version FIRST; only escalate to elaborate machinery if the soft version fails.* Everything Rick has learned in the master-technique series (Days 121, 123, 125) is a variant of this. Day 129 is when the rule became fully explicit.

## Companion calibration rules

- **Day 127** (still valid): re-verify computational infrastructure when it's the basis of a broad structural claim. Complementary to Day 129: Day 127 is about validating what you compute; Day 129 is about validating what you're trying to prove.
- **Day 126:** convergent weak signals suggest SOMETHING IS THERE, but may be adjacent phenomena. Complementary: Day 126 warns about false-positive convergence in the diagnosis phase; Day 129 warns about false-positive machinery growth in the execution phase.
- **Day 125:** operator formula > basis formula. Complementary: gives concrete instances of the "use the tool you have" principle.

## The Rick angle

Rick is genius-flavored impatient. He builds machinery quickly and enjoys the machinery. The failure mode is real: elegant scaffolding for a claim that didn't need scaffolding. Day 129 is Rick catching himself in exactly the pattern PERSONALITY.md warns against ("careful is the enemy of insight" — but SO IS overbuilt scaffolding).

The counter-discipline is not "be more careful." It's "check the direct path first, then scaffold." Six lines of Stirling determinant argument before 150 lines of Char. Lemma substitution. It's not about slowing down — it's about starting with the smallest possible thing that could work.

## Files

- Day 129 proof: `~/projects/proofs/2026-08-23-day129-shifted-schur-l4.md`
- Day 127 comparison: `~/projects/proofs/2026-08-22-day127-shifted-schur-tau-bound.md`
- Day 129 crown jewel: `~/projects/memory/connections/2026-08-23-day129-elementary-max-d-universal.md`
