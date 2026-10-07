---
name: Type-B cactus structure at the crystal level (and the adjacent Gutiérrez gap)
description: Aug~ is not the type-B cactus (Δℓ-refuted 2026-05-08); Aug~ IS the BGG-Verma differential, doubly-laced uniform (PROVED 2026-05-13). Cactus at Littelmann-path level CLOSED by Torres 2302.11560 (browse 5); the genuine open gap is the KN tableau level. Aug~ targets exactly this gap via Salisbury-Tingley descent + iQSP coideal commutativity (proved on-slice at B_2 + B_3 2026-05-14).
type: project
---

# Q: Type-B cactus structure at the crystal level

## Status (2026-05-16, end of Day 17)

**SU1 v1 PROVED** the BGG-differential identification at REDUCED-multiset level. **On-slice coideal commutativity PROVED at B_2 + B_3 + B_4** (5-line crystal-axiom proof, type-uniform). **Multi-orbit Aug~ RESOLVED** at B_n short simple as $e_n^2$ with $n(2n-1)$-move catalog, **three-strand braid structure PROVED type-uniform** at $B_n$, all $n \geq 2$ (`proofs/2026-05-15-three-strand-braid-Bn.md`). **Categorical-home question for on-slice commutativity CLOSED 2026-05-15** by trichotomy: crystal-level commutativity is trivial; the deep content is the combinatorial three-strand braid realisation; algebra-level $(\mathrm{ALG})$ is standalone with no naive $q=0$ bridge.

**Rep-theory mirror search CLOSED 2026-05-16** after four refutations. v2 is purely combinatorial: three-strand braid theorem + three-class decomposition + iSerre cross-chain match at $n \in \{3,4,5\}$. See `connections/aug-tilde-purely-combinatorial-after-four-refutations.md`.

**The gap is now precise:** type-B cactus at **KN tableau level**. Aug~ targets exactly this via Salisbury-Tingley PBW↔KN descent.

**The territory map (browse 8, 2026-05-16):**

Three independent approaches now exist, none closes the full gap:

- **Approach A: Torres-Azenhas virtualization.** Azenhas-Gonzalez-Huang-Torres arXiv:2409.12666 (2024) — works DIRECTLY on type B KN-tableaux. Gives the FIRST purely combinatorial definition of orthogonal evacuation (= one cactus generator, length-$n$ subdiagram commutor) via virtualization + De Concini-Lecouvey splitting. Full cactus action NOT constructed.

- **Approach B: Svyatnyy spinor Howe duality.** arXiv:2504.14344 (GT patterns) + arXiv:2605.00514 (short SSYT). TYPE D objects via $O_N$ Howe duality with $D_n$ spinor crystal. Gets cactus action on the spinor side. KN-tableau isomorphism not written.

- **Approach C (Rick): BDI coideal.** $B_i = F_i + \zeta E_i K_i^{-1}$ on $K_p(\infty)$. Three-strand BRAID relation on the depth-$k$ slice. Catalog of $n(2n-1)$ moves with three categorical homes (intra-chain / cross-chain / singleton).

Braid (Rick) ≠ cactus (Torres / Svyatnyy) — different combinatorial register. The bridge question (Rick's braid restricted to length-$n$ subinterval ↔ Azenhas-Torres orthogonal evacuation) is the critical pre-v2 consistency check: `connections/azenhas-torres-orthogonal-evacuation-bridge.md`.

**Watanabe arXiv:2107.00170 (AI-crystal)** remains the immediate precedent: parity-controlled $\widetilde B_i$ + commutation for $|i-j|>1$ + NO BRAID. Rick's BDI braid is the FIRST braid relation on an iquantum-tableau-crystal model. (See `connections/watanabe-AI-crystal-precedent.md`.)

**Chen-Lu-Wang arXiv:2601.00524** = algebraic precursor: ibraid invariance of dual canonical bases for all finite types including type B at the ALGEBRA level. Rick's result is the crystal-level counterpart for type BDI.

## Where type-B cactus stands across levels

- **W-level / KL-basis: CLOSED.** Gossow-Yacobi 2023 App B + Bonnafé 2016. Δℓ = ±2 within left cells; Schützenberger-evac at the S_n example.
- **Crystal-level for arbitrary B(λ): OPEN.** Long-form: A (Henriques-Kamnitzer 2006) → C (Halacheva 2022, virtualization) → D (Brown-Elek-Halacheva Dec 2024) → **B (open at tableau level)**.
- **Type-B at Littelmann path level: CLOSED (Torres EJC 2024, arXiv:2302.11560).** Virtual cactus on type-B Littelmann paths via A_{2n-1} → B_n Dynkin folding + Pan-Scrimshaw virtualization. Caught browse 5 2026-05-14.
- **Type-B at GT-pattern level: PARTIALLY DONE.** Svyatnyy arXiv:2504.14344 (2025) — cactus on so_N GT patterns; needs verification of so_{2n+1} coverage.
- **Type-B at KN tableau level: THE ACTUAL GAP.** No explicit BK^B on KN tableaux. Aug~ targets here.
- **Categorical cactus on crystals: SIMPLY-LACED ONLY** (HLLY 2021, arXiv:2101.05931 — type B *explicitly excluded*). Correction caught 2026-05-13 browse 1.
- **Abstract via J-ring: ALL Coxeter types** (Rouquier-White 2024, arXiv:2408.16922) — but only *conjectures* recovery of crystal-level Losev-Bonnafé actions, doesn't prove.

## Adjacent gaps Aug~ may fill

### (i) Gutiérrez gap: missing type-B Bender-Knuth at KN-tableau level

Gutiérrez arXiv:2311.10659 (2023) explicitly names this gap: no analogue of Bender-Knuth involutions between KN-tableaux and Sundaram tableaux in type B. Aug~ on (w, π) pairs is the natural candidate.

**Bridge identified (2026-05-13 browse 2):** Salisbury-Tingley arXiv:1708.04311 gives an **explicit bijection between PBW Kostant partitions and KN tableaux for B(∞).** This is the bridge map that translates Aug~ from Kostant partitions to KN tableaux. Pre-requisite for any computational test.

### (ii) Coideal-categorical home

Watanabe arXiv:2509.00853 (2025): any type-B BK involution must respect a type-AII coideal subalgebra action on B(∞). **Concrete commutativity test possible at B_2 scale.** See `connections/coideal-subalgebra-as-aug-tilde-home.md`.

### (iii) Barkley-Defant Coxeter-toggle framework

Barkley-Defant-Hodges-Kravitz-Lee arXiv:2401.17360 (2024). BK involutions for ALL Coxeter groups as toggle maps; non-invertible in general, but invertible on convex subsets of W. **Question:** are spin-dominant subsets of W(B_n) convex in the BK-billiards sense? If yes, the type-B KN-tableau BK involution follows by restriction.

## Other adjacent / type-related

- **Virtual cactus framework.** Ilin-Kamnitzer-Li-Przytycki-Rybnikov arXiv:2308.06880 (virtual cactus + cactus flower curves) — current consensus framework for going beyond type A. Type B via D-folding. Aug~ might be the intrinsic, non-virtual realisation.
- **iQSP / Bao-Wang stack.** Type-B KL world operates through canonical-basis / coideal lens. SU1's BGG-Verma lens is complementary. Meeting point: type-B KL positivity ↔ non-negativity of BGG-differential coefficients in Kostant basis.

## Concrete next steps (revised 2026-05-15 end of Day 16)

1. ✅ **Read Salisbury-Tingley arXiv:1708.04311.** DONE Day 12. Explicit Ψ: 𝒯(∞) → Kp(∞), row-by-row, doubling rule (n, n̄) ↦ 2β_{j,n} at type B.
2. ✅ **Coideal commutativity test.** PROVED Day 13 at B_2; ported Day 14 to B_3, Day 15 to B_4 (0 falsifiers across all simples).
3. ✅ **Multi-orbit Aug~ at B_3.** DONE Day 14 deep work: $\widetilde{\mathrm{Aug}}_3^{\rm multi} = e_3^2$, 15-move catalog.
4. ✅ **B_4 multi-orbit confirmation** (28 moves = 9 + 12 + 7). DONE 2026-05-15.
5. ✅ **Three-strand braid theorem PROVED type-uniform** at $B_n$, $n \geq 2$. DONE 2026-05-15. T1' + T2' + T3'; F4 hit cleanly via convex-first-chain TM(1) structural unreachability.
6. ✅ **Categorical-home question CLOSED.** DONE 2026-05-15: trichotomy of trivial-crystal / deep-realisation / standalone-algebra.
7. ✅ **Read Cao-Huang arXiv:2604.19490** (Day 17). REFUTED as Aug~ rep-theory mirror at both parameter-set and braid-transition layer.
8. ⛔ **"Han 2024 Young wall ι-quantum"** — PHANTOM (Day 17). Cross-author-thread conflation. Replaced by:
8'. ✅ **Read Watanabe arXiv:2107.00170 AI-crystal** (Day 17). NO BRAID. Confirms Rick's BDI braid is first. See `connections/watanabe-AI-crystal-precedent.md`.
9. ✅ **"Watanabe quartic"** (Day 17). Mis-attribution; real source is Letzter / Bao-Wang iSerre. Under iSerre reading, count $2(n-1)(n-2)$ matches cross-chain class at $n \in \{3,4,5\}$. See `connections/watanabe-quartic-as-cross-chain-CONFIRMED.md`.
10. **READ NEXT — arXiv:2409.12666 (Azenhas-Gonzalez-Huang-Torres, "Keys and Evacuation via Virtualization").** Critical pre-v2 read. Extract orthogonal evacuation formula on type B KN-tableaux. Run consistency check vs Rick's three-strand braid restricted to length-$n$ subinterval. See `connections/azenhas-torres-orthogonal-evacuation-bridge.md`.
11. **Watanabe $k=1$ collapse test.** Does Rick's $\widetilde{\mathrm{Aug}}$ at $k=1$ at $B_n$ short simple reduce to Watanabe's AI commutation $\widetilde B_i \widetilde B_j = \widetilde B_j \widetilde B_i$ for $|i-j|>1$? First concrete bridge between AI and BDI at depth 1.
12. **Check arXiv:2502.20958 (Lyndon bases of split iquantum groups).** Is type BDI covered at the algebraic level?
13. **Check arXiv:2110.07177 (Watanabe, "Crystal bases ... certain quasi-split types").** Is BDI covered?
14. **Convex-subset check.** Spin-dominant subsets in W(B_n) convex in Barkley-Defant sense? Lower priority.

## Status summary (2026-05-15)

- **Type-B cactus at KN tableau level: OPEN.** Aug~ is *not* the W-level realisation (different Δℓ signature) but is the leading candidate for the KN-tableau-level realisation.
- **Aug~ → type-B BK at KN level via Salisbury-Tingley: BRIDGE BUILT, descent map explicit.**
- **Aug~ → coideal-respecting BK on-slice: PROVED type-uniform via three-strand braid theorem.** Crystal-axiom level. Off-slice obstruction characterised exactly.
- **Categorical home for on-slice commutativity: TRIVIALLY KASHIWARA.** No iQSP/iHopf/QSP-BGG machinery needed for the commutativity itself; the deep content is the combinatorial three-strand braid realisation.
- **Aug~ → type-B cactus via Torres virtual cactus: COMPARISON TESTABLE.** Aug~-on-Kp(∞) vs Torres-on-Littelmann-paths, both should give the same answer on the open-crystal slice.
- **Cao-Huang sp_4 = B_2 (2604.19490) provides independent rep-theory-side cross-check** for v2.

See: `aug-tilde-as-bgg-differential.md`, `coideal-subalgebra-as-aug-tilde-home.md`, `coideal-commutativity-on-slice-B2-PROVED.md`, `multiorbit-aug-as-e-k-decomposition.md`, `multiorbit-catalog-as-three-strand-braid.md`, `on-slice-as-squared-off-slice.md`, `algebraic-home-and-crystal-home-are-independent.md`, `categorical-home-dissolution-as-method.md`, `aug-tilde-as-type-B-cactus.md` (refuted, kept for lessons).
