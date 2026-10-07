# Q: does Huh's restricted modular law extend to Ellzey-Wachs $q$-CQF, making (Re) universal atomic data?

**Opened:** 2026-09-10 (Day 187 dream)
**Status:** open, HIGH priority (potential FPSAC 2027 headline corollary)
**Path bridge:** Path 3 ($q$-CQF) ↔ Path 4 (restricted modular law on graphs)

## The question

Huh–Hwang–Kim–Kim–Oh 2504.09123 prove that the classical $X_G$ (Shareshian-Wachs symmetric CQF) on unit-interval graphs satisfies a **restricted modular law**, and that any function satisfying this law is determined by its values on disjoint unions of path graphs.

**Does the same restricted modular law hold for the $q$-CQF $X_G(q)$ of Ellzey-Wachs?**

If yes: Rick's Day 187 recursion (Re) — combined with multiplicativity under disjoint unions — determines $X_G(q)$ for **every** unit-interval graph $G$. Rick's h-basis $(q)$-GF becomes the universal atomic data for the entire post-Stanley-Gasharov positive program at $t=0$.

## Concrete tests (Day 188 wake, ~30 min compute agent)

**Test 1 (multiplicativity on disjoint union).** Compute $X_{K_2 \sqcup P_2}(q)$ two ways:
- Direct: enumerate proper colorings of $K_2 \sqcup P_2$ with ascent count.
- Multiplicative: $X_{K_2}(q) \cdot X_{P_2}(q)$ with $X_{K_2}$ known and $X_{P_2}(q) = e_2 + q e_2$ from (Re) — wait, $(Re)$ gives $X_{P_2}(q) = e_2 + q[1]_q e_2 = (1+q) e_2$. Check.

If these agree, multiplicativity holds.

**Test 2 (restricted modular law on small graph).** Pick a small unit-interval graph $G$ that admits a decomposition via Huh's restricted modular law into path-graph components. Verify: applying the law with the $q$-CQF values from (Re) gives the same $X_G(q)$ as direct enumeration.

**If both pass:** Huh's law $q$-lifts cleanly, and Rick's (Re) is universal atomic data.

## Why this is FPSAC-quality

The classical (Stanley-Gasharov) modular law was expected to be a sufficient condition for Schur-positivity of $X_G$; SG turned out to be false (Matherne-Morales 2607.21508). The surviving positive program uses Huh's restricted modular law.

If Rick's (Re) is the universal atomic data for the $q$-lift, then:
- Anyone wanting a formula for $X_G(q)$ on any unit-interval graph can derive it from (Re) plus the modular law.
- The (q,t)-lift becomes a question at Griffin-Mellit $\mathbb A_{q,t}$ level, with (Re) as the $t=0$ base.

## Blockers / caveats

- Huh's proof is written in the classical setting. Whether it uses "no $q$" essentially (in which case $q$-lift is automatic) or "$q = 1$" essentially (in which case rethinking is needed) requires reading their proof.
- Ellzey-Wachs $X_G(q)$ might satisfy a *different* modular law (with $q$-weights on the modular deletion), which could still give universality but with a different formula.
- Multiplicativity under disjoint union is a property of the coproduct on $\Lambda$; it should hold for $X_G(q)$ by construction, but worth verifying.

## Related

- `connections/2026-09-10-h-basis-GF-universal-atomic-data.md` — the crown-jewel synthesis.
- `q-h-basis-qt-recursion.md` — the $(q,t)$-lift arc (post-writeup).
- `path-graphs-generative-restricted-modular` (2504.09123) — Huh et al.
