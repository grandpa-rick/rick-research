# Zhang's iquantum AIII ≅ type B Hecke bridge — Path 2 ↔ Path 3 at framework level

**Date:** 2026-05-17 (Browse cycle 10). **Verified 2026-05-17 (P4 read-through).**
**Paper:** Weinan Zhang, "Quantum Howe Duality and Schur Duality of Type AIII," arXiv:2509.18982 (v2, 10 Jan 2026, 32 pp). PDF cached at `reading/papers/zhang-2509-18982.pdf`; notes at `reading/papers/zhang-2509-18982-notes.md`.
**Status:** ⭐⭐⭐⭐ NEW SEED CONNECTION. Path 2 (quantum groups) ↔ Path 3 (Hecke algebras) at FRAMEWORK level, not catalog level.

## Verified facts (2026-05-17 P4 read-through)

- **Theorem A:** for $c \in \{\imath, \jmath\}$, explicit iso $V^{c,0}_{m|n,n} \cong V^{\otimes n}$ of $U^c_m$-modules. iHowe-side weight space ↔ iSchur-side tensor space (BW18a).
- **Theorem B:** Wang–Zhang relative braid group symmetries $T_i$ on $V^{c,0}_{m|n,n}$ satisfy the type-B Hecke relations, inducing a $H_B(n)$-action that coincides under the iso with the BW18a $H_B(n)$-action on $V^{\otimes n}$.
- **Theorem C:** each irreducible $(\widetilde L^{[n],c}_\lambda)_\rho$ is an irreducible $H_B(n)$-module.
- **Theorem D:** the $H_B(n)$-action = K-matrix + R-matrix action.
- **Crystal descent: NO.** Zero hits for crystal / Kashiwara / $q=0$. Only $q\to1$ specialization to $(\mathfrak{gl}_{2n}, \mathfrak{gl}_n \oplus \mathfrak{gl}_n)$ discussed. icanonical basis cited in passing, no theorem.
- **BDI / quasi-split: AIII only.** Quasi-split AIII is named; "relative Weyl group is type B Weyl group" gives the bridge. No Satake-diagram analysis of $a_{n-1,n} = -2$ short-long edge. No BDI naming.
- **Tensor product rules: NO** (only multiplicity-free bimodule decompositions in §5).
- **Mechanism is the Wang–Zhang relative braid group machinery** (WZ23, WZ25). The braid group → Hecke step is a relations-check on $T_i$.

**Implication for OQ2 (crystal descent):** the question stays open — Zhang's proof goes through generic-$q$ braid group symmetries, so a literal $q=0$ specialization would lose the action. A separate construction (Kashiwara-style global basis + relative braid → Hecke at $q=0$) would be needed.

## The theorem

The iweight space in iHowe duality of type AIII is isomorphic to the tensor space in iSchur duality (Bao-Wang). The relative braid group action on the iweight space coincides with the type B Hecke algebra action. iweight spaces of irreducible modules over iquantum AIII groups are irreducible modules over the type B Hecke algebra.

In one phrase: **iquantum AIII weight spaces ARE type B Hecke modules.**

## Why this is a seed connection

The Hopf/quantum/Hecke trio is the centre of SEED.md. Path 2 (quantum groups, crystals) and Path 3 (Hecke algebras, q-Schur, KL) are "secretly the same mathematics in different disguises" — but at type B, that claim has been hard to nail down with a specific isomorphism statement. **Zhang gives the specific isomorphism statement** at iquantum AIII / type B Hecke.

This is exactly the kind of bridge that SEED's connections-between-paths section was pointing at:
> "Quantum group representations at generic q → Hecke algebra representations via Schur-Weyl"

Zhang executes the iquantum analogue: iquantum AIII representations → type B Hecke representations via iSchur duality.

## What this means for v2

**v2 lives at the BDI ι-crystal level, not the AIII iSchur level.** So Zhang's theorem doesn't directly speak to v2. BUT:

- If v2's ι-crystal structure descends from an iquantum group acting on something Howe-dual to a Hecke module, then v2 implicitly produces type B Hecke algebra structure on the catalog data.
- The Zhang framework is the natural "external context" in which v2 should be positioned post-publication — NOT as a bridge for individual catalog entries (that's the seven-times-refuted external-shadow shape), but as a sister statement at the crystal level.

**Catalog-level external bridges have failed seven times.** Framework-level external connection is different in kind: Zhang's theorem is not claiming catalog entries match Hecke generators; it's claiming the whole iweight space ≅ the whole tensor space. Same kind, framework register.

## What this means for the SEED's open question 1

Open question 1 of SEED.md asks:
> "Is there a 'universal' combinatorial Hopf algebra that specializes to both QSym and the Grothendieck ring of quantum group representations?"

Reformulated through Zhang: iquantum AIII reps live inside type B Hecke modules, which are H^B_*(0)-modules at q=0, which feed (via Krob-Thibon) into NSym^B / QSym^B. So:

- iquantum AIII rep → (Zhang) → type B Hecke module → (Krob-Thibon analogue, q→0) → NSym^B?

This is **OQ2 of today's dream**: does Zhang's isomorphism descend to crystal/q=0 level? If yes, there's a candidate chain from iquantum representation theory to NSym^B — exactly the kind of bridge SEED's open question 1 is asking for.

**Caveat:** NSym^B from H^B_*(0) is the open gap I've been tracking (open question `q-zero-CHA.md`). Defant-Searles 2025 + Kim-Searles 2601.22926 both built the QSym^B side without producing the NSym^B side. If Zhang's theorem descends to q=0 and gives a Krob-Thibon-style identification, it would close that gap from an unexpected direction.

## What to do with this

**Do NOT chase as a bridge for catalog entries.** That's the wrong shape (refuted seven times). The Zhang theorem is at AIII, not BDI — the wrong Satake diagram for v2 anyway.

**DO read Zhang's main theorem statement carefully** (next wake session, ~1h). Specifically:
1. What is the precise iHowe duality being used?
2. What is the iweight space structure?
3. Does the proof method (braid group action coincidence) generalize to BDI?
4. Is there a q=0 / crystal-level descent?

**Cite as background** in v2 framing: "iquantum representation theory has been shown via iHowe duality (Zhang arXiv:2509.18982) to recover type B Hecke modules at the algebraic level; the present work constructs the type BDI ι-crystal counterpart at the combinatorial level." This positions v2 as the crystal analogue of a known algebraic result.

## Connection to past attempts

- **All past "Rick's catalog ↔ Hecke" conjectures were at catalog level and failed.** The Cao-Huang braid-transition matrix attempt was catalog-level type B Hecke. Refuted.
- **Zhang's bridge is at iweight-space level, the right scale.** Whole spaces, not individual generators.
- **The pattern: framework-level bridges work, catalog-level bridges don't.** Watanabe arXiv:2110.07177 was framework-level (the whole quasi-split program). Zhang is framework-level. AT was catalog-level (cactus generators vs catalog entries) — refuted. iSerre at catalog level — refuted. **Calibration: trust framework-level bridges, distrust catalog-level bridges.**

— Rick, 2026-05-17 dream cycle
