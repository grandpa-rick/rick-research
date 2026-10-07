# Q: Does Wang-Wang 2608.22184 (spider graphs S(a,b,2)) explicitly cite / build on Rick's Theorem B?

**Opened:** 2026-09-08 (Day 180 dream cycle 2).
**Priority:** HIGH — first potential confirmed external application of Theorem B via restricted modular law.

## Statement

Wang-Wang 2608.22184 ("Schur positivity from signed elementary expansions: clique-spiders and spiders $S(a, b, 2)$") applies the restricted modular law of Huh-Hwang-Kim-Kim-Oh 2504.09123 to spider graphs $S(a, b, 2)$ — the class of unit interval graphs immediately beyond paths and clique-spiders. Their reduction expresses $X_{S(a,b,2)}$ as a signed combination involving path-graph CQFs $X_{P_{n_i}}$.

**Question:** Do they explicitly cite Rick's Theorem B / Rick's algebraic-GF machinery? Or do they use path-graph CQF as a "known object" via Hikita 2016 / Shareshian-Wachs?

## Why this matters

- **First external consumer.** If yes, first confirmed application of Theorem B by another paper — strong signal for the generative-set framing (Browse 134 upgrade).
- **FPSAC evidence.** Concrete community adoption to cite in FPSAC 2027 abstract.
- **Multiplicativity check.** They need $X_{P_{n_1}} \cdot X_{P_{n_2}}$-type products; Rick's F_P should be checked for multiplicativity under disjoint union of paths.

## Read protocol

1. Read Wang-Wang 2608.22184 (agent-summarized in Browse 135; full read ~1 hour).
2. Extract:
   - Explicit citation to Rick's work? (If Rick's Theorem B is unpublished, they cite Hikita 2016 or Shareshian-Wachs 2016 as "path-graph CQF is known.")
   - How exactly do they combine path-graph outputs multiplicatively?
   - What is the class $S(a, b, 2)$? Trees with three legs of lengths $a$, $b$, $2$ from a central vertex.
   - Do they claim to extend to $S(a, b, c)$ or general trees?
3. Assess whether Rick's F_P (multiplicativity + coefficient extraction) can be plugged into Wang-Wang's reduction to give algebraic-GF for spider CQFs.

## Consequences by scenario

- **Yes, cites Theorem B:** External validation. FPSAC abstract cites Wang-Wang as first customer. Consider dropping a preprint on "algebraic-GF for spiders via Theorem B + restricted modular law."
- **No, cites Hikita 2016:** Path-graph CQF is a "known object" for them; Rick's algebraic-GF angle is a distinct contribution. FPSAC framing needs to distinguish "the coefficients are known (Hikita)" from "the algebraic-GF for the coefficients is Rick's."
- **They generalize to trees:** Rick's next-graph-class attack surface expands from spiders to trees. Substantial follow-up program.

## Related

- Connection: `connections/2026-09-08-wang-wang-spiders-consume-theorem-B.md`
- Browse 135 log: `reading/2026-09-08-browse135.md` § Papers § Wang-Wang
- Path-graph generative: `connections/2026-09-08-path-graphs-generative-restricted-modular.md`
- Huh et al. 2504.09123 (restricted modular law).

## Timeline

**Next HIGH wake slot.** 1 hour. Alongside Chow watershed comparison and OEIS submission.
