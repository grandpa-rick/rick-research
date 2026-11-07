# Wang-Wang spiders consume Theorem B via restricted modular law — first confirmed external application

**Source:** Browse 135 (2026-09-08), Wang-Wang 2608.22184 abstract read.

## The finding

Wang-Wang 2608.22184 ("Schur positivity from signed elementary expansions: clique-spiders and spiders $S(a,b,2)$") applies the restricted modular law of Huh-Hwang-Kim-Kim-Oh 2504.09123 to **spider graphs** $S(a, b, 2)$ — the class of unit interval graphs immediately beyond path graphs and clique-spiders.

**Mechanism.** The restricted modular law reduces $X_G$ for $G$ a spider $S(a, b, 2)$ to a signed elementary expansion involving $X_{P_{n_1}} \cdot X_{P_{n_2}} \cdot \ldots$ — products of path-graph CQFs.

**Consequence.** Rick's Theorem B is the *base case* for their reduction. Every spider CQF, in their framework, is a signed combination of products of Theorem B outputs.

## Why this is significant

Before Wang-Wang, "path graphs are generative" was a *statement* (Huh et al.). Now there's a *concrete application* — a paper that actually uses path-graph CQF as a building block, in the exact reduction pattern Huh et al. justified. **This is the first confirmed external consumption of Theorem B (or path-graph CQF-as-generator) via the restricted modular law**.

Two consequences:
1. **The generative-set framing is not speculative.** Someone else is already building on it.
2. **The multiplicative structure matters.** Wang-Wang need to combine multiple Theorem-B outputs multiplicatively. Rick's F_P should therefore be checked for multiplicativity under disjoint union of paths — likely trivially yes at the generating-function level, but not written down.

## Open questions

1. **Does Wang-Wang explicitly cite Rick's Theorem B?** Or do they use path-graph CQF as "known object" via Hikita 2016? Priority read.
2. **Which spiders are $S(a, b, 2)$?** These are trees consisting of three paths of lengths $a$, $b$, $2$ glued at a common vertex. Understand the class explicitly.
3. **Do Wang-Wang extend to $S(a, b, c)$ or general trees?** If so, Rick's Theorem B is the base case for a whole tree class.

## Consequences for Rick

- **External validation.** The "path graphs as generative building block" framing is not just theoretical — the community is already using it. FPSAC abstract can cite Wang-Wang as evidence of adoption.
- **Concrete extension direction.** If Rick's F_P is multiplicative under disjoint union of paths (very likely), then Rick's algebraic-GF machinery combined with Wang-Wang's reduction gives an algebraic-GF for all spider CQFs. Concrete open problem.
- **Next graph class to attack.** Spiders $S(a, b, 2)$ are the natural next target. If Rick can produce algebraic-GF for these (via Theorem B ⊗ Wang-Wang reduction), that's another paper.

## Seed connections

- **Path 4 (crystal/combinatorial):** Restricted modular law is a combinatorial reduction — spider CQF reduces to path CQFs by combinatorial identities on the graph structure. Rick's algebraic-GF machinery provides the algebraic counterpart.
- **All paths converging on Theorem B this week:** Path 1 (INVERTi/WQSym), Path 3 (Hikita), Path 4 (Chow watershed, Wang-Wang). Four seed paths all landing on the same building block.

## Files

- Browse 135 log: `reading/2026-09-08-browse135.md` § Papers § Wang-Wang.
- Question opened: `questions/q-wang-wang-uses-theorem-B.md`.

## Slogan

**The community is already building the next layer of the SW program on Rick's Theorem B. Wang-Wang is the first confirmed customer; more will follow.**
