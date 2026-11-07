# Coideal Subalgebra as Aug~ Categorical Home

> **Conjecture (Rick, 2026-05-13, post Watanabe browse):** Aug~ on (w, π) commutes with the type-AII coideal subalgebra action on B(∞). If true, this is (a) the categorical home for Aug~ and (b) a concrete bridge to the Gutiérrez gap — the missing type-B BK involution at the KN-tableau level.

## The Watanabe input

Watanabe arXiv:2509.00853 (2025) lifts Berele row-insertion (type-C Schensted) to an isomorphism of representations over a quantum symmetric pair coideal subalgebra of type AII. Key consequence: **any type-B BK involution that hopes to lift to a quantum-categorical statement must respect a coideal subalgebra action.** The coideal subalgebra is the natural categorical framework for type-B involutions.

## The Aug~ side

Aug~ is the BGG-Verma differential on Kostant partitions (proved 2026-05-13 SU1, doubly-laced uniform). Kostant partitions ARE the PBW basis of U(𝔫⁻). U(𝔫⁻) at q=0 is B(∞). The type-AII coideal subalgebra acts on B(∞) — explicitly known.

## The bridge claim

If Aug~ commutes with the type-AII coideal generator on B(∞), then:

1. **Categorical home.** Aug~ is not just a combinatorial involution — it's the q=0 shadow of a coideal-module morphism. The non-locality of Aug~ (84% greedy failure for B_3) is then the coideal non-commutativity.

2. **Gutiérrez gap fill candidate.** Gutiérrez arXiv:2311.10659 named an explicit gap: no analogue of Bender-Knuth involutions at the KN-tableau level for type B. **Salisbury-Tingley arXiv:1708.04311 gives the bridge: explicit bijection between PBW Kostant partitions and KN tableaux for B(∞).** If Aug~ on Kostant partitions commutes with the type-AII coideal, then projecting via Salisbury-Tingley gives a candidate BK^B involution at KN-tableau level — exactly what Gutiérrez said was missing.

## What needs to be checked

1. **Read Salisbury-Tingley arXiv:1708.04311 carefully.** Understand the PBW Kostant partition ↔ KN tableau bijection explicitly. This is the bridge map. **Pre-requisite for everything below.**

2. **Concrete test in B_2.** Pick small KN tableaux of shape λ ∈ {(1), (2)}, encode as (w, π) pairs via Kostant + Salisbury-Tingley. Apply the type-AII coideal generator explicitly. Check whether Aug~ commutes.

3. **If commutes:** publish a follow-up paper "type-B Bender-Knuth involution via the BGG differential and the Salisbury-Tingley bridge" — fills Gutiérrez's named gap.

4. **If doesn't commute:** record the obstruction; the coideal action might respect a *modified* Aug~ (e.g., a signed version), or Aug~ might not be the right object for the Gutiérrez gap.

## Why this is the right next move post-SU1 v1

- **SU1 v1 is closed.** Doubly-laced uniformity at the BGG-differential level is theorem.
- **The next visible target** is the Gutiérrez gap (the named missing KN-tableau type-B BK).
- **Watanabe gives the precise structural condition** (coideal-respecting) that any type-B BK candidate must satisfy.
- **Salisbury-Tingley gives the bridge** to translate Aug~ from Kostant partitions to KN tableaux.
- The three pieces — Aug~, coideal action, Salisbury-Tingley — make a concrete computational test possible at B_2 scale.

## Adjacent / related

- **Barkley-Defant-Hodges-Kravitz-Lee arXiv:2401.17360 (2024) BK billiards.** Defines BK involutions for ALL Coxeter groups as toggle maps, restricting to involutions on convex subsets of W. The "convex subset" framing is the *Coxeter-theoretic* shadow of the "coideal-respecting subset" picture. Same question, different community. Worth checking whether spin-dominant subsets in W(B_n) are convex in the BK-billiards sense.

- **Bao-Wang 1310.0103** is the iQSP foundation paper; the type-B KL world operates through canonical-basis / coideal lens. SU1's BGG-Verma lens is complementary. **The two approaches meet at the positivity question:** type-B KL positivity = coefficients of BGG differential in Kostant basis are non-negative.

- **Lu-Yang-Zhang arXiv:2407.13127 (2024).** PBW bases for ι quantum groups. Rick uses Kostant partition = PBW basis; this paper may give the iQSP-language version. The comparison could reveal whether the REDUCED structure of SU1 appears in iQSP PBW theory.

## Status (2026-05-14 update)

**Salisbury-Tingley extraction returned by agent (2026-05-14).** Actual citation is Criswell–Salisbury–Tingley, arXiv:1708.04311, finite types B_n and C_n. Key findings:

1. **Explicit row-by-row crystal isomorphism Ψ: 𝒯(∞) → Kp(∞)**, fixed reduced word w_0 = (s_1 ⋯ s_n s_{n−1} ⋯ s_1)(s_2 ⋯ s_n s_{n−1} ⋯ s_2)⋯ s_{n−1} s_n. Constructive: each box / (k, k̄) pair in row R_j produces a positive root β_{j,k} or γ_{j,k} in Ψ(R_j).
2. **Doubling rule (n, n̄) ↦ 2β_{j,n} in type B** is the doubly-laced fingerprint.
3. **Agent's verdict: Aug~ ↔ Kashiwara crystal operators e_i / f_i on KN tableaux via Ψ.** NOT RSK / jeu-de-taquin — honest Kashiwara action.
4. **Agent's stronger claim (needs verification): Rick's REDUCED quotient = Kashiwara's bracket-cancellation step S_i → S_i^c.** Same operation viewed from opposite sides. **MUST hand-check before trusting** — this is the load-bearing claim of the bridge.

Extraction note: `reading/2026-05-14-salisbury-tingley-extraction.md`.

## Next concrete test (B_2 hand-check)

Use stack notation (CST §4). Pick a small B_2 Kostant partition π with a non-trivial s_i action. Verify two things explicitly:

1. **REDUCED = bracket-cancellation.** Encode π as a tableau T = Ψ⁻¹(π). Read off the i-signature string S_i. Apply Kashiwara bracket-cancellation to get S_i^c. Compare to Rick's REDUCED-multiset normalization on π. They should match step-for-step.

2. **Coideal commutativity.** Pick the type-AII coideal generator B_i. Compute B_i · T = (something), then apply Ψ. Compute f_{α_i} · π = Aug~(π) (one step), then apply B_i on the tableau side. Commute? If yes, type-B BK candidate found.

**Estimate:** 1-2 hours each. Do (1) first — it's the bridge correctness check. If (1) clean, (2) becomes the natural follow-up.

## Status

**Bridge identified. REDUCED ↔ bracket-cancellation claim needs hand-verification (load-bearing).** If verified: P1 promoted to P0.

Date: 2026-05-13 (born from browse 2). 2026-05-14 (CST extraction + verdict).
