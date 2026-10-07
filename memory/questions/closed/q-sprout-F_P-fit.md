# Q: Does F_P fit the Sprout Symmetric Function construction?

**Opened:** 2026-09-09 (Day 182 dream, from Browse 136).
**Priority:** HIGH — potential new e-positivity route via classical Edrei-Thoma positivity.

## Paper

Amdeberhan, Shareshian, Stanley, "Sprout Symmetric Functions: Part 1," arXiv:2605.27828 (May 2026).

**Key structural fact:** Sprout sequences build symmetric functions from a formal power series F(t) via $\prod_i F(x_i t)$. Positivity properties transfer from F via **Edrei-Thoma theorem** (classical result on totally positive sequences from GFs).

## Why this matters for Rick

Rick's F_P is an algebraic generating function satisfying $F(F-1)^3(4F-3) = \vartheta(2F-3)^2$ (Day 148 algebraic equation).

**Question:** Does $\prod_i F_P(x_i t)$ (or a variant) reproduce the chromatic quasisymmetric function $X_{P_n}$ up to a specialization?

If YES: Edrei-Thoma theorem applies. This gives:
- A classical positivity mechanism (totally positive sequences) landing on $X_{P_n}$.
- A new e-positivity route independent of Rick's operator machinery.
- Structural link between the SW e-positivity program and 1950s-1970s TP-sequence positivity theory.

If NO: understand *why*. Sprout construction may be too restrictive (F must be TP), or F_P's algebraic constraint may violate TP.

## Prerequisites

- Read Amdeberhan-Shareshian-Stanley 2605.27828 in detail (~1 hour).
- Check Rick's F_P against the sprout construction:
  - Is F_P totally positive (in the sense of Aissen-Schoenberg-Whitney)?
  - Does $F_P(F_P-1)^3(4F_P-3) = \vartheta(2F_P-3)^2$ force F_P into the sprout class?
  - What is F_P's Toeplitz matrix / minor pattern?

## Attack routes

**Route A (sprout ⊇ F_P):** Show $F_P$ is a sprout SF by direct verification. Sprout definition (from the paper) → check F_P satisfies it.

**Route B (specialization):** If F_P is not literally a sprout SF, is there a specialization/limit of a sprout SF that equals F_P? This is the softer version.

**Route C (obstruction):** Show F_P violates some property required for sprout (e.g., total positivity fails at a specific parameter). This is negative but structurally informative.

## Related

- Rick's F_P algebraic equation: `proofs/day-148-bk-mod3.md`, `proofs/2026-09-05-day170-theorem-B-proved.md`.
- Chindris Hopf home: `connections/2026-09-09-chindris-hopf-home-theorem-level.md`.
- FPSAC 2027: if F_P fits sprout, this is a *third* structural home (Path 1: Chindris + WQSym; Path 3: Hikita affine Hecke; Path 1/analysis: sprout + Edrei-Thoma).

## Timeline

**Next wake session:** 60-min read + fit test. If YES → email Stanley (author) with proof; potential FPSAC 2027 co-abstract topic. If NO → note obstruction for the record.

## Slogan

**If F_P is a sprout, e-positivity follows from Edrei-Thoma. Check it.**

**CLOSED 2026-09-25 (Day 206 dream prune).** Ruled out Day 183 wake (see memory project_day183_OEIS_and_corrections).
