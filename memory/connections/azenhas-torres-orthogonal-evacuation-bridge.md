---
name: Azenhas-Torres orthogonal evacuation is a candidate bridge for Rick's three-strand braid
description: arXiv:2409.12666 (Azenhas-Gonzalez-Huang-Torres 2024) gives the FIRST purely combinatorial definition of orthogonal evacuation on type B KN-tableaux. Rick's braid catalog, restricted to the length-n subinterval, may agree with their evacuation formula — providing a representation-theoretic origin (BDI coideal) for their virtualization-based combinatorial construction.
type: project
---

# Azenhas-Torres orthogonal evacuation ↔ Rick's three-strand braid (candidate bridge)

**Date created:** 2026-05-16 (dream 2 / Day 17 PM, browse cycle 8)
**Status:** ⭐⭐⭐⭐⭐ — keystone external connection, consistency check identified
**Source:** browse 8 citation trail via Torres 2302.11560

## What Azenhas-Torres have (arXiv:2409.12666)

"Keys and Evacuation via Virtualization" (Olga Azenhas, Joel Gonzalez, Yu Huang, Inês Pires Torres, 2024).

- **Setting:** crystals of any two finite Cartan types, related by virtualization (Fujita; PPSS = Pappe-Pfannerer-Schilling-Simone).
- **Main theorem:** virtualization commutes with left and right key maps, embedding Demazure crystals and atoms.
- **Key application:** Works DIRECTLY on **orthogonal Kashiwara-Nakashima tableaux** (type B). Proves that the virtualizations from type B into type C considered independently by Fujita and by PPSS coincide with the De Concini-Lecouvey splitting map.
- **Consequence (the punchline for Rick):** gives a **purely combinatorial definition of orthogonal evacuation** — the first explicit combinatorial description of the partial Schützenberger involution acting on type B KN-tableaux.

This is the closest extant combinatorial result to Rick's type B KN-tableau cactus program. One specific cactus generator (evacuation = length-$n$ subdiagram commutor) is defined combinatorially on the right objects. The full cactus group action is NOT constructed.

## What Rick has

Three-strand braid theorem at $B_n$ short simple (proved type-uniform 2026-05-15). Catalog of $n(2n-1)$ net moves of $\widetilde{\mathrm{Aug}}_n^{\mathrm{multi}} = e_n^{k(n)}$ on the depth-$k$ slice, splitting as:
- $3(n-1)$ intra-chain
- $2(n-1)(n-2)$ cross-chain
- $(2n-1)$ singleton-involving

The braid relations live on $K_p(\infty)$, the lower-half Kostant-partition crystal, derived from the BDI coideal generator $B_i = F_i + \zeta E_i K_i^{-1}$.

## The bridge claim

**Conjecture:** Rick's three-strand braid, when restricted to the length-$n$ subinterval $[1, n]$ of the braid group $B_n$, agrees with Azenhas-Torres's orthogonal evacuation formula on type B KN-tableaux.

If true, this gives:
- A **representation-theoretic origin** (BDI coideal) for Azenhas-Torres's combinatorial construction.
- A **consistency check** validating Rick's braid against the only independently-defined combinatorial structure on the same crystal.
- A bridge between the "virtualization" school (Fujita / PPSS / Torres / Azenhas) and the "iquantum coideal" school (Letzter / Bao-Wang / Watanabe / Chen-Lu-Wang / Rick).

The bridge is asymmetric — Rick gives MORE structure (the full braid relation, not just one generator). Azenhas-Torres's evacuation should be a *specialization* of Rick's braid, not the other way around.

## Why this might fail

1. **Different crystals.** Azenhas-Torres operate on type B KN-tableaux of shape $\lambda$ (finite crystal). Rick operates on $K_p(\infty)$ (infinite, lower-half). Need the right embedding / restriction to compare.

2. **Different operator types.** Their evacuation is an involution; Rick's braid is a length-3 relation. Comparing requires reading off which specific composite of $\widetilde B_i$'s corresponds to the length-$n$ subdiagram commutor.

3. **Virtualization vs coideal.** The De Concini-Lecouvey splitting map is type-B-into-type-C; Rick's coideal $B_i$ is intrinsic to type BDI. The relationship between these two perspectives is non-trivial.

## Falsifiable test

At $B_2$ short simple, $\lambda = \omega_1 + \omega_2$ (a small case with both row types):
- Compute Azenhas-Torres's orthogonal evacuation on every type B KN-tableau of shape $\lambda$.
- Compute Rick's $\widetilde B_1 \widetilde B_2 \widetilde B_1$ (length-2 subdiagram commutor) on the corresponding $K_p(\infty)$ elements, restricted to the slice $S_2 = \{$depth-2 elements$\}$.
- Check whether the two maps agree on weight-zero elements (where the comparison makes sense).

If they agree → strong positive connection, v2 has a clean "our braid lifts Azenhas-Torres's evacuation" paragraph.
If they disagree → the bridge claim is wrong; v2 simply cites Azenhas-Torres as adjacent work that doesn't compete (since braid ≠ cactus generator anyway).

Either outcome is publishable. Disagreement is fine — Rick's braid is a distinct structural object regardless.

## Seed connections

- **Path 2 (quantum groups):** the BDI coideal $B_i$ is the q=0 image of the type-BDI coideal generator in $U_q(\mathfrak{so}_{2n+1})$.
- **Path 3 (Hecke):** the virtualization B→C uses the Kashiwara involution; the BDI coideal naturally extends Hecke-style structure.
- **Path 4 (coproduct-crystal):** both Azenhas-Torres and Rick work on crystal-level objects. The bridge sits squarely in Path 4.

## Action

- **Next prove session P1.** Read arXiv:2409.12666 in full (~3-4h). Extract orthogonal evacuation formula. Run the $B_2$ consistency check (~1h compute).
- **Before v2 submission.** Include consistency check result (positive OR negative) as a structural cross-reference.
- **Email Azenhas / Torres** post-v2 if connection holds — this is exactly the audience for the result.

## Calibration

This is the **fifth instance** of "two independent constructions of similar-looking objects on the same domain". Past instances:
1. Rick's Aug~ + Almousa-Lu gluing (Path 1, type A) — held.
2. Rick's coideal commutativity + Stroppel-Wang BGG (refuted by category mismatch).
3. Rick's Aug~ + Cao-Huang Verma-KN bijection (refuted, four times now).
4. Rick's three-strand braid + Watanabe AI-crystal (held as precedent without competition).
5. Rick's three-strand braid + Azenhas-Torres orthogonal evacuation (open; testable).

Refined calibration (today): check the constructions produce the SAME KIND of object BEFORE expecting a bridge. Azenhas-Torres = involution on KN-tableaux; Rick = braid relation on $K_p(\infty)$. Length-$n$ subinterval restriction projects Rick's braid to a single involution → same kind. The kind-check passes. Now the question is whether they're the *same* involution.

If they are: bridge framework. If not: adjacent-but-distinct.

— created 2026-05-16 dream 2 (Day 17 PM)
