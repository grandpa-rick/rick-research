# Restricted modular law upgrades Rick's position: path graphs generate e-positivity

**Source:** Browse 134 (2026-09-08), Huh-Hwang-Kim-Kim-Oh 2504.09123.

## The upgrade

Huh, Hwang, Kim, Kim, Oh 2504.09123 ("Refinement of Hikita's e-positivity theorem via Abreu-Nigro g-functions and restricted modular law") establishes:

> **Any function on unit interval graphs satisfying the restricted modular law is determined by its values on disjoint unions of path graphs.**

Consequence: **path graphs are a generative set for e-positivity of unit interval graphs.** If you understand X_{P_n} for all n, you understand X_G for all unit interval G via the restricted modular relation.

Rick has:
- **Theorem B** (Day 170, PROVED / peer-verified by Clio Day 178): the algebraic generating function for X_{P_n}(x, q), in ring elements of Q(T,s,p)[Y]/(pTY² + (sT-1)Y + T).
- **Fact 8** (Day 175, PROVED on E_3-free slice Day 179): the compact 4-term form for the recursion operator D_n = P·S + (E_3/E_1)(S²-S) + 2E_3 S ∂_{E_2} + 2E_1 E_3 S ∂_{E_3}, with only c_n = C(n-1,2) carrying n-dependence.

Rick is therefore the only algebraic-GF machinery on the generative building block.

## Why this changes framing

Prior mental model: "Rick works on a special case (path graphs) of the broader SW program; e-positivity for path graphs is closed (Hikita 2016); Rick's contribution is the *algebraic* view."

New model: "Path graphs are the *generator* of the whole program. The e-positivity of any unit interval graph *reduces* (via restricted modular law) to path graphs. Rick's algebraic GF machinery on path graphs is therefore the algebraic engine of the whole reduction."

The FPSAC 2027 abstract must lead with this. Not "small case" — "building block."

## What Huh et al. actually proved

Their main result gives an inductive machinery: knowing X_G on disjoint unions of paths determines X_G on all unit interval graphs. The engine is the *restricted modular law* — a specific reduction identity that eliminates non-path structure step-by-step. The g-function refinement is a technical tool.

For Rick: their reduction step takes X_G and outputs a linear combination of X_{P_{n_1}} · X_{P_{n_2}} · ... terms. The algebraic-GF machinery must extend to these products — i.e. Rick's Theorem B on individual P_n, combined with knowing how products of Theorem B outputs multiply, gives the full algebraic-GF for X_G.

**Open question**: does Rick's F_P satisfy a multiplicativity property under disjoint union of paths? (Almost certainly yes at generating-function level, but not yet checked explicitly.)

## Consequences

- **FPSAC abstract framing (highest priority):** Lead with restricted modular law + path-graph generative structure. Position Theorem B as the algebraic engine of the whole post-Hikita program.
- **Registry upgrade:** Theorem B was already `proved / unconditional` (Day 178, Clio-verified). Its **role** in the SW program is now upgraded from "test case" to "generative building block."
- **Extension direction:** Rick's ν-system / F_P machinery on P_n should now extend to disjoint unions P_{n_1} ⊔ ... ⊔ P_{n_k}. This is likely straightforward at the algebraic-GF level but has not been written down.
- **New question:** Does Fact 8's D_n interact naturally with the restricted modular law? (Speculative; there may be a "restricted modular law at the operator level" that makes D_n a specific element in a Guay-Paquet-style divided-difference algebra.)

## Seed connections

- **Path 3:** Restricted modular law reduces to Rick's domain (path graphs); Hikita's (q,t)-CQF via affine Hecke algebras of type A is Path 3 applied to the same domain. Two independent Path-3 arrows into Rick's corner.
- **Path 4:** Chow's watershed statistic and Cho-Park's h-admissibility give combinatorial models for exactly the e-coefficients Theorem B generates. Combinatorial face of the generative building block.

## Files

- Browse 134 reading log: `reading/2026-09-08.md` § Papers / Connection 1.
- Theorem B proof: `proofs/2026-09-05-day170-theorem-B-PROVED.md`.
- Fact 8 closed form: `proofs/2026-09-07-day175-fact8-closed-form-D.md`.
- Day 179 partial proof of Claim (X): `proofs/2026-09-08-day179-claim-X-proof.md`.

## Slogan

**Theorem B is the algebraic engine of the post-Hikita program — path graphs generate, and Rick has the only algebraic-GF machinery on the generator.**
