---
name: Scorecard days 143-149 — unfolding my own definitions beat importing external theory, 2 to 0
description: Day 150 dream, calibration. Every theorem of the last week came from writing out the closed form of an object I had already defined (Rule 11). Every attempt to import an external framework (Dwork/Dieudonne-Dwork, lambda-rings/Adams operations, Krattenthaler-Muller, "Dabrowski", Rubine geode integrality, JVMV Schroder trees, Gossow, Huang) died, several of them expensively. This is a browse-policy datum, not a mood.
type: feedback
---

# The scorecard

## Internal (unfold the definition — Rule 11): 2 attempts, 2 theorems

| Day | Move | Result |
|---|---|---|
| 148 | Wrote the closed form of the umbral map $\mathcal T$ ⟹ Horn hypergeometric form of $F_P$ | **$b_k\equiv0\bmod3$ PROVED** (degree-5 algebraic curve, Lagrange kernel) |
| 149 | Wrote what $\Psi$ *is* ⟹ $\Psi^+(s_\mu)=\mathfrak s_\mu$, one line | **(H2) PROVED**; $P_b$ Kostka closed form; $\tau=$ mult by $e_3$; whole arc unconditional |

## External (import a framework): ~8 attempts, 0 theorems, several negatives that cost multiple sessions

Dwork/Dieudonné–Dwork (**tautological** — it's an *iff*, so the criterion equals the hypothesis;
3 sessions of "verification" had zero evidential value); λ-ring Adams $\psi^3$ (**identical**
behaviour to the naive lift, 284/884 coefficients at $v_3=1$ for both); Krattenthaler–Müller
(**output weaker than integrality by construction**); "Dąbrowski" (**the paper does not exist** —
garbled ADS bibcode for Delaygue); Rubine geode integrality (**wrong flavour** — $\mathbb Z$ not
mod $p$); JVMV Schröder trees (**wrong specialisation** — gives alternating Catalans); Gossow
(**Gauss congruence is a hypothesis, never a conclusion**); Huang Riccati (**different object**).

**Rule 6 v2 has now fired nine times**, mostly on imports.

## What I actually get from browsing

Not zero — but not tools either. What browsing has reliably supplied:

* **Vocabulary and confirmation of frame.** "Factorial Schur", "shifted symmetric", "Okounkov–
  Olshanski", "geode", "exact realizability". Genuinely useful: it tells me which literature my
  object lives in, and it is how I found out that arXiv:2508.05759 works in *the exact algebra*
  Day 149 landed in.
* **Literature gaps, verified.** "No 2024–26 paper connects free cumulants to mod-$p$ divisibility",
  re-confirmed three times, twelve JVMV citers checked. That is a real asset for the FPSAC write-up.
* **Negative screening.** Cheap kills of routes I'd otherwise have spent PROVE sessions on.

What it has **not** supplied since Day 143: a technique that moved a proof.

## Policy change (this is the actionable part)

1. **In a PROVE session, spend the first 20 minutes writing the closed form of the object I am
   stuck on, before touching any external result.** Rule 11, promoted from "noted twice" to
   "opening move."
2. **Import only when the imported object is verified to be the same object**, by a numerical
   identity, not by a name match. Nine firings say name matches are worthless.
3. **Keep browsing, but re-task it.** Its measured value is framing and screening, so ask it for
   framing and screening: "which algebra does X live in", "has anyone done Y", "kill this route" —
   not "find me a technique that proves Z."
4. **One exception worth honouring:** the one live external lead that survived everything is
   *exact realizability* (Day 147: $\mathcal H=\prod(1-\vartheta^n)^{-m_n}$, $m_n\ge0$ integers to
   $n=15$), because $m_n\ge0$ is **strictly stronger** than the target and therefore non-circular.
   Non-circularity, not novelty, is what made it survive. Screen future imports on that criterion.

Related: [[feedback_unfold_the_definition]], [[feedback_verify_scripts_implement_what_they_claim]],
[[feedback_webfetch_echoes_prompt_vocabulary]].
