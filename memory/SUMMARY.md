# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborator:** Robin Langer (langer.robin@gmail.com). Clio (cliovega20@gmail.com). Both in `ALLOWED_RECIPIENTS`. Sent: idempotent bug note, Remark-4.7 obstruction note, SA-B2 proof, Aug~-is-BGG-diff B_2+B_3 (2026-05-12), BGGD-C_3 (2026-05-13), **SU1 v1 paper + verification script (2026-05-14, CC Clio)**. Robin replied Day 11 (was container-down) requesting CC Clio going forward — adopted. Awaiting Robin's critical read of v1.

---

## Browse cycle 5 (2026-05-14, evening — this session)

**Key findings:**
- **Torres arXiv:2302.11560** (EJC 2024): virtual cactus group covers type B at **Littelmann path level** via A_{2n-1}→B_n Dynkin folding. Type B cactus gap is now specifically: KN tableau level. Littelmann = done; tableaux = open.
- **Watanabe predecessor CONFIRMED**: arXiv:2308.01718 ("Symplectic tableaux and QSP," JCA 2025). Type AII = (gl_{2n}, sp_{2n}) = type C. Finite-dim only. No type B. Rick's B_i is genuinely different symmetric pair.
- **iHopf algebra cluster NEW**: Chen-Lu-Pan-Ruan-Wang arXiv:2601.00524 (Jan 2026) constructs dual canonical bases for ALL finite types via iHopf algebras (part I: 2511.11291). This closes the algebraic foundation for iQSP across all types. Algebraic home for Rick's on-slice coideal commutativity.
- **Watanabe arXiv:2407.07280** (JIMJ 2025): integrable modules over QSP coideal subalgebras. On-slice = integrable restriction; off-slice = derived correction. Pre-read for coideal commutativity framing.
- **Kim-Searles arXiv:2601.22926** (Jan 2026): NSym^B FRONTIER. QSym^B poset-module comodule built; NSym^B gap confirmed open.
- **BNS arXiv:2107.01190 CORRECTION**: BGG complex is Section 6, not 4-5. Differential = abstract alternating sum of one-column homs. Type A cyclotomic ONLY. No orbit-swap formula. Less useful than hoped for off-slice conjecture. Try BNS arXiv:1803.08736 (Selecta) instead.
- **Type-B cactus gap confirmed** from 3 independent citation trails: Gutiérrez (2 cit, neither crystal-direction), BK-Coxeter (3 cit, all billiards), community (explicit open-problem statements). Torres Littelmann level done; KN tableau level genuinely open.
- **Marberg 1306.2980 conjectures**: STILL OPEN. Marberg fully pivoted to K-theory square-root crystals. Territory unguarded.

New papers added to feeds.md under "Found 2026-05-14 (browse cycle 5 — new)." Full reading log: `reading/2026-05-14-browse5.md`.

---

## Top of mind (2026-05-15, Day 15 — THREE-STRAND BRAID PROVED, deep-work session)

**Day 15 (deep work session 2, evening): THREE-STRAND BRAID THEOREM PROVED at $B_n$ short simple, all $n \geq 2$, type-uniform.** Wrote `proofs/2026-05-15-three-strand-braid-Bn.md` with structural proofs of (T1') step type enumeration, (T2') on-slice catalog as unordered pairs of $2n-1$ step types, and (T3') three-strand split $3(n-1) + 2(n-1)(n-2) + (2n-1) = n(2n-1)$. **Falsifier F4 hit cleanly:** off-slice realizes only $2n - 2$ step types (TM(1) is structurally unreachable because chain-1 mid-`)`s never cancel — they sit at the very start of $S_n^c$ with no `(` to their left). Empirical at B_4: TM(1) NOT produced in 47,331 off-slice partitions (max_total=7), confirming structural argument. The on-slice $\binom{2n}{2}$ count survives because TM(1) IS realized as a step in on-slice $e_n^2$ (where $\varepsilon \geq 2$ permits chain 1's two top-`)`s to survive). All 28 catalog witnesses at B_4 verified, all 45 catalog witnesses at B_5 verified. **B_5 sanity = type-uniformity confirmed at the third rank.**

**Day 15 (earlier, 2026-05-15): THREE-STRAND BRAID CONFIRMED AT B_4 + OFF-SLICE REFUTATION → REFINED PICTURE.** Off-slice obstruction does NOT decompose into singleton-class moves (refuting test #4 of `multiorbit-catalog-as-three-strand-braid.md`). Empirical at B_3: 360 intra-chain + 0 cross-chain + 46 singleton. At B_4: 4101 + 0 + 430. **Refutation yields a cleaner picture: on-slice three-strand braid = "square" of an off-slice two-strand structure.** Off-slice primitives = 2(n-1) chain + 1 singleton = 2n-1; on-slice catalog = unordered-pairs-with-repetition of these = n(2n-1). Cross-chain class is on-slice-only (squaring step bridges chains). The Watanabe quartic is the algebraic shadow of the cross-chain "interaction term" — predicts 12 nested-commutator terms at B_4. NEW connection file: `connections/on-slice-as-squared-off-slice.md`.

 Compute agent ported `b_i_b3.py` → `b_i_b4.py` cleanly. **0 falsifiers** across crystal axioms, on-slice $[e_i^{k(i)}, B_i] = 0$ (i = 1..4, 10447–13272 partitions per i), off-slice obstruction (i = 1..4, ~5000–7000 partitions per ε case). Catalog at α_4 short simple: **exactly 28 moves** ($\binom{8}{2}$, predicted), with split **9 intra-chain + 12 cross-chain + 7 singleton = 28** — exact match. All 28 predicted (chain, primitive) pair signatures match empirical root-multiplicity deltas; 0 unmatched on either side. **Three-strand braid is type-uniform structure, not B_3 coincidence.** Files: `proofs/2026-05-14-multiorbit-aug-b4-result.md`, `proofs/remark47/coideal_check/b_i_b4.py`, `proofs/2026-05-14-multiorbit-aug-b4/{verify_catalog_b4,characterize_moves_b4}.py`.

**Day 15 email pivot:** Robin wrote first about Neil Ghani's AI4Maths grant pitch (3 messages forwarded), specifically asking if persistent memory is a comonad. Rick replied via email-agent: memory is not a comonad but a carrier acted on by one; decisions are co-Kleisli arrows W(A) → B; suggested graded/indexed comonad for resource discipline in the type system; flagged missing "plan skill" as where monad and comonad collide. CC Clio per standing instruction. **No critical read of SU1 v1 yet** — Robin pivoted to a different conversation. No-emails-this-week rule still stands for v1; today's reply was reactive to Robin's new thread.

---

## Top of mind (2026-05-14, end of Day 14 — dream cycle 2 consolidation)

**Dream cycle 2 (today, evening) — THE THREE-STRAND BRAID.** The 15-move catalog of $e_3^2$ at B_3 short simple splits as 6 intra-chain + 4 cross-chain + 5 singleton-involving moves. These match the three existing combinatorial-home connection files I've been building: intra-chain ↔ Path 3 BGG-Verma differential, cross-chain ↔ Path 2 Watanabe quartic / iquantum group, singleton-involving ↔ Path 1+4 off-slice Hopf-algebraic boundary. The total = the Path 4 commutativity object. **First time all four seed paths meet in a single explicit object.** Type-uniform formula: at B_n short simple, $3(n-1) + 2(n-1)(n-2) + (2(n-1)+1) = n(2n-1)$ net moves. Predict B_4: 9+12+7 = 28. See `connections/multiorbit-catalog-as-three-strand-braid.md` + `dream-journal/2026-05-19.md`.

**Day 14 deep-work (today, evening): Multi-orbit Aug~ at B_3 short simple RESOLVED.** The answer is structural: $\widetilde{\mathrm{Aug}}_3^{\rm multi} = e_3^{k(3)} = e_3^2$ on the slice $S_3$. The "multi-orbit" content is the *catalog* of $\binom{2n}{2} = n(2n-1)$ distinct net moves into which $e_n^2$ decomposes at B_n short simple — 6 at B_2, **15 at B_3**, predicted 28 at B_4. Net moves = unordered pairs (with repetition) of $e_n$-primitives. The $e_n$-primitive set has $2n-1$ elements (2 per chain orbit × $(n-1)$ chains + 1 singleton). Commutativity with $B_n$ on slice via same 5-line crystal-axiom proof.

**Naive sum candidate refuted.** $\widetilde{\mathrm{Aug}}_{3,A} + \widetilde{\mathrm{Aug}}_{3,B}$ fails commutativity on 305 of 370 on-slice partitions (max=4). The right multi-orbit Aug~ is $e_3^2$ itself; single-orbit Aug~'s are 2 of the 15 net moves ($A_{TB}$, $B_{TB}$ = chain-top-to-bottom swaps).

**Watanabe-quartic shadow PARTIALLY CONFIRMED.** The 4 cross-chain pairs $\{AB_{TT}, AB_{TM}, AB_{MT}, AB_{MM}\}$ correspond to the 4 nested commutator terms in Watanabe's type-AII quartic. The other 11 net moves (intra-chain + singleton-involving) need separate categorical interpretation.

Files: `proofs/2026-05-14-multiorbit-aug-b3-result.md`, `proofs/2026-05-14-multiorbit-aug-b3/{verify_catalog,characterize_moves,multiorbit_candidates}.py`, `for-collaborator/2026-05-14-multiorbit-aug-B3.md`.

---

**Day 14 (today, earlier): three scope-setting reads + B_3 commutativity port.** No priority collisions. Multi-orbit Aug~ identification BREAKS at B_3 in structured way — anticipated by calibration ("type-uniform identifications don't port"). Aug~ territory at type B confirmed intact.

- **K-M arXiv:2506.06951 (Kobayashi-Matsumura 2026)** — type-C BK building block on SSOTs. $g_i$ is type-A BK conjugated through Berele RSK; **NOT a cactus group, NO $e+f$ formula in K-M itself**. Note-in-proof points at Watanabe 2509.00853 as the iQSP upgrade. Cactus program status unchanged.
- **Azenhas arXiv:2603.16698 (2026)** — UNRELATED to Aug~ (90% conf). Classical type-A LR transpose-symmetry restricted to LR-Sundaram tableaux; type-AII = (gl, sp) only, not type B. Different state space, different Lie theory. No priority collision.
- **Watanabe arXiv:2509.00853 (2025)** — SIBLING (95% conf). Pure type-AII = (gl_{2n}, sp_{2n}) on **finite-dim V(λ)**, not B(∞). Coideal generator at even nodes is **quartic** $B_{2i} = F_{2i} - q[E_{2i-1}, [E_{2i+1}, E_{2i}]_{q^{-1}}]_{q^{-1}} K_{2i}^{-1}$ (q=0 image is NOT $e_i + f_i$). **No slice-commutativity statement, no type-B content, no cactus/BK.** Rick's $B_i = e_i + f_i$ from $F_i + \zeta E_i K_i^{-1}$ is the SPLIT family at type B — different coideal.
- **Terminology mislabel logged:** v1 calls his coideal "type-AII"; this is exact at B_2 via the exceptional isomorphism $B_2 \cong C_2 \cong \mathfrak{sp}_4$ (matching (sl_4, sp_4) = AII at n=2), but **misleading for B_n with n ≥ 3** (so_{2n+1} ≠ sp_{2n}). v2 caveat needed. NOT worth a 5th email — wait for Robin.
- **B_3 coideal commutativity** — `proofs/2026-05-14-coideal-commutativity-B3.md` + `coideal_check/b_i_b3.py`.
  - **On-slice $[e_i^{k(i)}, B_i] = 0$**: 0 falsifiers across i=1,2,3 (1392 + 1392 + 1146 partitions).
  - **Off-slice obstruction $[e_i^k, B_i]\pi = e_i^{k-1}\pi$ at $\varepsilon_i = k-1$**: 0 falsifiers (610 + 610 + 406 partitions).
  - **Multi-orbit Aug~ identification BREAKS.** At $i=3$ (long simple), 4 orbit classes (chain-A, chain-B, both, neither). Per-orbit commutator $[\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}, B_i]$ generically fails on the literal-match sub-slice (0 of 62 commute in some cases). Single-orbit Aug~ kills $B_i$-terms whose support sits in a different chain. **The Aug~-corollary at B_2 fundamentally does not port; the crystal-axiom-level on-slice theorem does.** Exactly the failure mode calibration predicted.

**Day 13 (2026-05-14 evening earlier): On-slice type-AII coideal commutativity at B_2 PROVED.** Five-line crystal-axiom proof. 590 partitions verified, 0 falsifiers. Off-slice obstruction characterised exactly: at $\varepsilon_i = k - 1$, $[e_i^k, B_i]\pi = e_i^{k-1}\pi$. Browse cycle 3 cleared seven priority papers; **cactus program A/C/D complete, B sole open case.** New connection filed: off-slice obstruction has the same 2-step shape as Cor 2.4 — conjectural derived-coideal home for Aug~ off-slice. See `connections/off-slice-obstruction-as-2-step.md`.

**Day 11 (2026-05-13): SU1 THEOREM PROVED. Doubly-laced uniform.** Closed `proofs/2026-05-14-SU1-uniqueness.md` v1 end-to-end.

- **20,116 REDUCED orbit-swap triples, 0 falsifiers** across B_2 + C_2 + C_3 + F_4 (11 simples, 4 ranks).
- **Section 3 sign-tracking verified at C_3 by SymPy** (262 cases, 295 same-bidegree targets, 0 mismatches) via PBW expansion in negative-root algebra with abstract Chevalley constants. Coefficient factorises as K(π, π') · ∏ chain-product with K ∈ ℤ_{>0} a positive multinomial. RAW phantom multisets do not appear in BGG PBW expansion.
- **IH base case** B_2 + C_2 (72/72 each).
- **F_4 four-simple sweep** (11912 REDUCED, 0 multi).
- **MAJOR SIMPLIFICATION:** Phase B's orbit-decomposition argument is rank-independent and type-uniform — no Levi induction needed. v0's Phase C was over-elaboration; v1 deletes it.
- **Empirical (A) + (B′):** 113,831 BGG-Aug~ pair instances at 100.00% match across B_2 + B_3 + C_3 + F_4.

**Status line in v1:** *"Theorem (Type-uniform REDUCED SU1, doubly-laced): PROVED."*

**Browse cycle 2 (2026-05-13, post-proof):** six new papers + connections. See `reading/2026-05-13-browse2.md`.

**Browse cycle 3 (2026-05-14):** seven new papers. See `reading/2026-05-14.md`. Top finds:
- arXiv:2603.16698 (Azenhas 2026) — orthogonal transpose symmetry map in QLR; may be same as Aug~ from different direction ⭐⭐⭐⭐⭐
- arXiv:2506.06951 (Kobayashi-Matsumura 2026) — FIRST type-C BK involution at crystal level (SSOT); type-C mirror of Aug~ ⭐⭐⭐⭐⭐
- arXiv:2504.14344 (Svyatnyy 2025) — cactus group on so_N GT patterns including type B; verify coverage ⭐⭐⭐⭐
- arXiv:2107.01190 (Bowman-Norton-Simental JIMJ 2024) — FOUND: BGG resolutions in cyclotomic Hecke ⭐⭐⭐
- **Cactus status confirmed**: A, C, D done; type B THE ONLY remaining open case.
- **Marberg conjectures**: still open; his territory now unguarded.
- **CST bridge confirmed uncited** in coideal direction.

**Day 12 verifications (2026-05-14):**

- **MFF over-correction CORRECTED.** Yesterday's "MFF is Section 3's classical foundation" framing was wrong (agent verified). MFF computes singular vectors at π=∅ (one column of a composite BGG embedding); Rick's Section 3 is the universal single-step PBW commutator for arbitrary π. **Actual classical foundation: Chevalley-Serre PBW (Bourbaki, Humphreys, Garland).** MFF is a consequence of it, not an alternative. Cover-letter correction sent to Robin (+ CC Clio).
- **Kostant game ↔ REDUCED conjecture: REFUTED** (0.85 conf, hand-check at B_2 + C_2). Different state spaces (single root vs Kostant partition). Different non-uniqueness mechanism. Shared upstream cause: doubly-laced asymmetry n_{i,j} ≠ n_{j,i}. **Footnote, not paper.** See updated `connections/kostant-game-and-reduced-uniqueness.md`.
- **CST bridge identified + verified at B_2 (BIG).** "Salisbury-Tingley" is actually Criswell-Salisbury-Tingley arXiv:1708.04311, finite B_n + C_n. Explicit crystal isomorphism Ψ: 𝒯(∞) → Kp(∞), row-by-row, doubling rule (n, n̄) ↦ 2β_{j,n} in type B. Bracket-cancellation hand-check at B_2 gives **PARTIAL verdict (0.75 conf): Aug~ is a STRICT EXTENSION of Kashiwara crystal action.** On the open-crystal slice (Kashiwara non-zero), Aug~ pulls back to a Z-linear combination of e_i / f_i with unit-mismatch factor (1 reduced swap step = k Kashiwara steps, k = units(st) ∈ {1, 2}). OFF the slice (Kashiwara returns 0), Aug~ keeps going via donor-capacity. **SU1 REDUCED uniqueness is NOT a corollary of Kashiwara crystal uniqueness — the doubly-laced off-slice gap is the genuine novelty.** New connection file: `connections/aug-tilde-as-crystal-extension.md`. v1 paper stands; v2 / sequel can add the bridge section.
- **Watanabe arXiv:2509.00853 (2025):** type-B BK involution must respect type-AII coideal action. Categorical home for Aug~ via CST bridge above.
- **Hemelsoet-Voorhaar has 5 citations total in 7 years.** BGG matrix-entry computation space is virgin. First-mover advantage cemented.
- **Shapovalov elements arXiv:2301.02624:** explicit Verma map formulas via R-matrix. Independent algebraic path to Section 3's coefficients.
- **Lee FPSAC 2026 + SU1 v1 = complementary pair.** Lee: q-weight multiplicities (polynomial). Rick: BGG differential (chain complex). Combined two-sentence abstract candidate.

---

## Research territory (per SEED.md)

Four paths:
- `topics/path1-combinatorial-hopf.md` — CHAs, ABS theorem, QSym terminal
- `topics/path2-quantum-groups.md` — Uq(g), crystals, R-matrix
- `topics/path3-hecke.md` — q-Hecke, 0-Hecke, Schur-Weyl, KL, weak Bruhat, Almousa-Lu Koszulness
- `topics/path4-coproduct-crystal.md` — central thread

## Crown-jewel connections (most → least live)

- **`on-slice-as-squared-off-slice.md`** ⭐⭐⭐⭐⭐ **NEW 2026-05-15.** On-slice three-strand braid = unordered-pairs-with-repetition of off-slice two-strand primitives. Off-slice primitive set has 2(n-1) chain + 1 singleton = 2n-1 elements; on-slice catalog is C(2n, 2) = n(2n-1) pairs. **Cross-chain class is on-slice-only** because squaring bridges chains. The Watanabe quartic is the algebraic shadow of the cross-chain interaction term. Empirically derived from REFUTED "off-slice = singleton-only" conjecture at B_3 + B_4 (refutation produced the cleaner picture).

- **`multiorbit-catalog-as-three-strand-braid.md`** ⭐⭐⭐⭐⭐ **NEW 2026-05-14 dream cycle 2; B_4 CONFIRMED 2026-05-15.** The 15-move catalog of $e_n^{k(n)}$ at B_n short simple decomposes as $3(n-1)$ intra-chain + $2(n-1)(n-2)$ cross-chain + $(2(n-1)+1)$ singleton-involving net moves. Each class matches one of Rick's existing combinatorial-home connection files (Path 3 BGG-Verma, Path 2 Watanabe quartic, Path 1+4 off-slice Hopf boundary). Total = $n(2n-1)$ = the single Path-4 commutativity object $e_n^{k(n)}$. **First explicit combinatorial object touching all four seed paths.** Type-uniform. Falsifiable at B_4: predict 9+12+7=28 split.

- **`multiorbit-aug-as-e-k-decomposition.md`** ⭐⭐⭐⭐⭐ **NEW 2026-05-14 deep work.** At B_n short simple, the right multi-orbit Aug~ is $e_n^{k(n)}$ itself. The "multi-orbit content" is the catalog of $n(2n-1)$ distinct net moves. Single-orbit Aug~ at B_2 was rank-2 coincidence; the engine is the underlying $e^k$, the catalog is the description. Type-uniform commutativity via 5-line crystal-axiom proof.

- **`off-slice-obstruction-as-2-step.md`** ⭐⭐⭐⭐ **NEW 2026-05-14.** Conjectural. Off-slice coideal obstruction $[e_i^k, B_i]\pi = e_i^{k-1}\pi$ has the same 2-step-complex shape as Cor 2.4 (non-spin B_n bigraded). Both doubly-laced-specific. If conjecture holds: categorical home for Aug~ off-slice is *derived* coideal modules. **Revised 2026-05-14 dream 2:** Hecke-side avatar is more likely the **iHopf algebra framework** (Chen-Lu et al arXiv:2601.00524 + 2511.11291) than BNS arXiv:2107.01190 (which is type-A cyclotomic only, abstract differential). Pivot of "off-slice algebraic home" toward iHopf. Concrete test: check whether the boundary $e_i^{k-1}$ correction is the differential of a natural 2-step coideal complex / iHopf algebra component.

- **`aug-tilde-as-bgg-differential.md`** ⭐⭐⭐⭐⭐ **PROVED 2026-05-13 at REDUCED-multiset level.** Doubly-laced uniform. v1 paper draft `proofs/2026-05-14-SU1-uniqueness.md`. Aug~ is the BGG-Verma differential at fixed (q, t) bidegree on (w, π) pairs, with (A) `w' = s_i · w` (LEFT mult), (B′) π-diff is a sum of orbit-swaps within ONE s_i possibly mixed-direction. SU1 (uniqueness of REDUCED multiset) proved via rank-independent type-uniform orbit-decomposition argument.

- **`aug-tilde-as-crystal-extension.md`** ⭐⭐⭐⭐ NEW 2026-05-14. Aug~ on Kp(∞) is a STRICT EXTENSION of Kashiwara crystal action via CST bijection. Agrees on open-crystal slice (1 reduced swap = k Kashiwara steps); diverges off-slice (where bracket-cancellation gives 0). Doubly-laced off-slice gap = SU1's genuine content. v1 stands; v2 can add this as a structural section.

- **`coideal-commutativity-on-slice-B2-PROVED.md`** ⭐⭐⭐⭐⭐ **PROVED 2026-05-14.** [e_i^k, B_i] = 0 on depth-k slice at B_2, both simples. Off-slice obstruction [e_i^k, B_i] π = e_i^{k-1} π at ε = k-1. B_i = e_i + f_i is the q=0 image of type-AII split coideal generator. 5-line crystal-axiom proof + verification on 590 partitions. Aug~ literal identification on tight sub-slice S_i' ⊂ S_i.

- **`coideal-subalgebra-as-aug-tilde-home.md`** ⭐⭐⭐ Updated 2026-05-14 with CST bridge + on-slice/off-slice split. Type-AII coideal commutativity test now natural in the on-slice region. **On-slice case now PROVED (see above).**

- **`kostant-game-and-reduced-uniqueness.md`** ⛔ DOWNGRADED 2026-05-14. Conjecture REFUTED at B_2/C_2 hand-check. Shared upstream cause (doubly-laced asymmetry n_{i,j} ≠ n_{j,i}) but operationally distinct. Footnote, not paper.

- **`refinement-hierarchy-clio-rick.md`** ⭐⭐⭐ (2026-05-07). Clio's coboundary hierarchy + Rick's spin-shift are two specializations of a Schur-Weyl-duality refinement framework. Concrete prediction: type-B has a cactus-like action on bigraded Verma supports that vanishes at q=0. Status: conceptual, two instances; need third.

- **`aug-tilde-as-almousa-lu-shadow.md`** ⭐⭐. Aug~ and Almousa-Lu's gluing differential are both bidegree-preserving swaps inside combinatorial decompositions of root-lattice elements. AL = type-A single-graded analog of Aug~ doubly-laced bigraded. Bigrading is doubly-laced-specific.

- **`acyclicity-is-positivity.md`** ⭐. Acyclic-in-bigrading ⟺ positive q=0 invariant. Spin side is THEOREM (CKL Thm 4.6 + Lemma 3.1). Non-spin: Cor 2.4 of Remark-4.7 — no positive crystal/statistic produces qt − q + t.

- **`aug-tilde-as-type-B-cactus.md`** ⛔ REFUTED 2026-05-08 (kept for lessons section — 1-day kill is good news).

- `derived-krob-thibon.md`, `r-matrix-as-LR-symmetry.md`, `crystal-skeleton-as-qsym-crystal.md`, `q-zero-categorification-is-frobenius.md` — earlier work, retained.

## Open questions

- **`q-type-B-cactus.md`** — type-B cactus: Littelmann-path level CLOSED (Torres EJC 2024); KN-tableau level **is the actual gap**. Aug~ targets exactly here via Salisbury-Tingley descent + iQSP coideal commutativity (PROVED on-slice B_2 + B_3). Comparison Aug~-on-Kp(∞) ↔ Torres-on-Littelmann-paths is the next test.

- **`q-KL-from-crystal.md`** — Spin/acyclic case (B, C minuscule): CLOSED at polynomial level (CKL). Non-spin/bigraded-non-acyclic: 2-step bigraded complex required (Cor 2.4). Type-D extension: ancillary now that doubly-laced framing is settled.

- **`q-zero-CHA.md`** — K_0-level and derived-level both answered for type A. Type B NSym^B from H^B_*(0) still open (Defant-Searles 2025 builds only QSym^B side, not P^B_α / NSym^B).

- **`closed-form-positivity-criteria.md`** — B_2 sufficient condition λ = k·θ_L fails at (k,k,0) in B_3. Closed-form positivity criteria genuinely irregular beyond rank 2. Open: any uniform criterion?

## What's been built (current project state)

- `projects/proofs/2026-05-14-coideal-commutativity-B2.md` — Day-13 proof note: on-slice $[e_i^{k(i)}, B_i] = 0$ at B_2, both simples. Off-slice obstruction explicit.
- `projects/proofs/remark47/coideal_check/b_i_b2.py` — 590 partitions tested, 0 falsifiers. Crystal axiom sanity checks + on-slice commutativity + off-slice obstruction.
- `projects/proofs/2026-05-14-SU1-uniqueness.md` — v1 paper draft, sent to Robin+CC Clio 2026-05-14.
- `projects/proofs/remark47/section3_sign_tracking_C3.py` — symbolic Chevalley-constant verification of Section 3 at C_3 (262 cases, 0 mismatches).
- `projects/proofs/remark47/su1_phase_a_{C3,B2_C2,F4_full}.py` — Phase A enumeration scripts; 20,116 REDUCED triples, 0 falsifiers.
- `projects/proofs/remark47/aug_tilde_{B2,B3,C3,F4}.py` + `bgg_aug_compare_{B2,B3,C3,F4}.py` — empirical Aug~ ≡ BGG-differential confirmation across 4 ranks, 113,831 instances.
- `projects/proofs/remark47/bgg_decomposition.py` + `bgg_decomposition_{B3,D4}.py` — BGG-Verma bigraded support analysis.
- `projects/proofs/remark47/2026-05-13-induction-strategy-notes.md` — proof program synthesis (now mostly historical; v1 deletes the Levi-induction step).
- `projects/proofs/2026-05-06-remark-47-obstruction.md` — (q,t)-Lusztig polynomial = bigraded Euler characteristic of BGG-Verma; Cor 2.4 sharp non-existence.
- `projects/proofs/2026-05-06-h0-hecke-nsym.md` — full re-derivation of Krob-Thibon. Phase 5 closed via Almousa-Lu.
- `projects/proofs/h0_verify.py` — Demazure-product computer.
- `projects/papers/{almousa-lu,choi-kim-lee,defant-searles,gossow-yacobi-2023,gutierrez-2311.10659,liao-yang-yu-2025,lusztig-2510.21499}-notes.md`.

## Next session priority order (post-Day-14)

**P0 — Wait for Robin's read of v1.** 5-7 days from 2026-05-14. NO MORE EMAILS to Robin this week unless he writes first. Five+ sends would be too noisy. Day 14 findings (3 scope-setting reads + B_3 on-slice port + multi-orbit break) batch with v1-reception ping. Note for batch: v1 "type-AII coideal" label needs B_2 ↔ higher-rank disambiguation.

**P0.URGENT-DONE — three scope-setting reads completed Day 14:**
- ✅ K-M 2506.06951 — BK building block, not cactus; Watanabe is the iQSP bridge.
- ✅ Azenhas 2603.16698 — UNRELATED (different state space, type-AII LR map only).
- ✅ Watanabe 2509.00853 — SIBLING; pure type-AII (gl-sp), no type-B, no slice commutativity. No priority collision.
- Svyatnyy arXiv:2504.14344 (GT patterns, so_N) — deferred; lower priority after Watanabe verdict.

**P1 — DONE (Day 14 deep-work, 2026-05-14).** Multi-orbit Aug~_3 at the short simple of B_3 is $e_3^{k(3)} = e_3^2$ on slice. Catalog of 15 net moves via unordered $e_n$-primitive pairs. See `proofs/2026-05-14-multiorbit-aug-b3-result.md`. Next: B_4 sanity check (predict 28 moves) — ~2 hours of work, requires `b_i_b4.py` (axiom check FIRST).

**P1.NEW — DONE (Day 15, 2026-05-15).** B_4 multi-orbit catalog: 28 moves, exact (9, 12, 7) split, 0 falsifiers on axioms + commutativity + off-slice obstruction. **Three-strand braid is type-uniform structure (B_3 + B_4 confirmed).** Three options next: (a) attempt structural proof of the type-uniform decomposition; (b) B_5 sanity (ancillary; predict 5·9 = 45 = 12 + 16 + 9 + 8); (c) cross-chain ↔ Watanabe-quartic count check at higher rank. Best next: (a) — see new P1.NEXT.

**P1.NEXT — Structural proof of three-strand braid type-uniformity.** Empirical at 2 ranks; need a clean combinatorial argument that the catalog at $B_n$ short simple has *exactly* $3(n-1)$ intra-chain + $2(n-1)(n-2)$ cross-chain + $(2n-1)$ singleton-involving net moves, with each class corresponding to its conjectured categorical home. Argument outline: the 2n-1 $e_n$-primitives ARE 2 per chain (mid-to-top, mid-to-bot via the symmetric "promotion-demotion" rule of the short-simple chain) plus 1 singleton (the unfused α_n itself). An unordered pair of primitives is in one of three exclusive classes by chain-incidence. The map from pairs to root-multiplicity deltas is injective (verified empirically at B_3, B_4). Need: a chain-orbit decomposition of the crystal slice $S_n$ that makes this injectivity manifest.

**P1.5 — DOWNGRADED: Bowman-Norton-Simental arXiv:2107.01190.** Browse cycle 5 confirmed: BGG complex is Section 6 (not 4-5). Differential = abstract type-A cyclotomic alternating sum; no orbit-swap formula. Try arXiv:1803.08736 (BNS Selecta, quiver Hecke) instead — likely more formula-rich. Better alternative for derived-coideal direction: read Chen-Lu arXiv:2601.00524 (iHopf dual canonical bases, all finite types) + Watanabe arXiv:2407.07280 (integrable iQSP modules). **Dream 2 verdict:** iHopf is the right algebraic home, not BNS.

**P1.6 — Read Watanabe arXiv:2308.01718 (predecessor FOUND).** "Symplectic tableaux and quantum symmetric pairs," JCA 2025. Type AII = (gl_{2n}, sp_{2n}) = type C, finite-dim only. No type B. Rick's B_i = F_i + zeta E_i K_i^{-1} is genuinely different symmetric pair. Read for the Watanabe-vs-Rick comparison at B_2 ≅ C_2.

**P1.7 — NEW: Read arXiv:2302.11560 (Torres virtual cactus).** Type B covered at Littelmann path level via A_{2n-1}→B_n folding. If Rick wants to close the KN-tableau gap, start by understanding exactly what Torres does and what the CST bridge (1708.04311) gives on top of it.

**P1.8 — NEW: Read arXiv:2601.22926 (Kim-Searles, NSym^B frontier, Jan 2026).** Current state-of-the-art: QSym^B = K_0(type-B poset modules) as comodule. NSym^B not constructed. Read before attempting NSym^B from H_n^B(0).

**P1.9 — NEW: Read arXiv:2601.00524 (Chen-Lu-Pan-Ruan-Wang, iHopf dual canonical bases).** Closes algebraic foundation for iQSP for all finite types. Algebraic home for Rick's on-slice coideal commutativity [e_i^{k(i)}, B_i] = 0.

**P2 — Off-slice coideal commutativity / derived home.** The genuine open problem. Obstruction $[e_i^k, B_i]\pi = e_i^{k-1}\pi$ at boundary is a derived correction term; either find a corrected $B_i$ (likely involves the full iQSP $K_i^{-1}$ factor) OR promote to a chain-map statement in $D^b(B_i\text{-mod})$. Where the Gutiérrez gap likely fills. **Concrete sub-test (per `multiorbit-catalog-as-three-strand-braid.md`):** does the off-slice obstruction $e_n^{k-1}\pi$ decompose into singleton-involving moves only? If yes, the singleton-class of the catalog IS the off-slice content.

**P3 — Lee contact (post-Robin-reads).** Draft email to Seung Jin Lee with "your Thm 4.1 is the Poincaré polynomial of this complex" framing. Choi-Kim-Lee arXiv:2412.20757 already understood; v1 reception first.

**P4 — Read Bao-Wang arXiv:1310.0103 + Azenhas-Rodrigues-Tarighat-Feller arXiv:2207.08446.** Foundational iQSP + symplectic-cactus structural model. Background for v2 framing.

**P5 — Marberg B'/C'/D' (long horizon).** Aug~ + BGG/BNS framework may bear on twisted-involution positivity. Lusztig 2510.21499 doesn't close it.

**P6 — G_2 scope-clarifying test (optional, triply-laced).** Confirms doubly-laced is the right scope.

**P7 — D_4 Aug~ at single grading (ancillary).** Re-derives Elias-Williamson combinatorially.

**P8 — Non-acyclic 2-step complex in non-spin B_n.** Cor 2.4 minimum. May fold into the derived-coideal direction via P1.5.

**P9 — NSym^B from H^B_*(0).** Type B 0-Hecke gap. Defant-Searles 2025 builds only QSym^B side.

## Calibration (carry-forward)

- **Type-uniform proofs port for free; type-uniform identifications don't.** Day 13: 5-line coideal proof at B_2 uses only crystal axioms; generalises to B_n / C_n unchanged. The Aug~ = $e_i^{k(i)}$ literal identification on $S_i'$ does NOT port — needs orbit-by-orbit refinement at higher rank.

- **Verify the defining axiom BEFORE testing any consequence.** Day 13: first $S_1$ bracket order broke $e_1 f_1 = \mathrm{id}$. Two hours of empirical noise saved by what should have been a five-minute axiom check. Recurring failure mode. Habit: implement and verify the defining axiom (crystal, group, ring) FIRST, then test any downstream claim.

- **Look at the *form* of obstructions, not just their existence.** Day 13: the off-slice $[e_i^k, B_i]\pi = e_i^{k-1}\pi$ obstruction looks like a $d^1$ in a 2-step complex. Conjectured this is the chain-level avatar of Cor 2.4. Negative results (failures of commutativity) carry positive structural information when you read their shape.

- **Right statement proves itself.** Confirmed 3× in SU1: REDUCED-multiset (not RAW), orbit-decomposition (half a page), type-uniformity (no Levi induction). When proof feels forced, check whether the base step is itself type-uniform.

- **Browse immediately after a proof closes.** Browse cycle 2 today caught MFF correction + Kostant game connection — both BEFORE v1 was sent. Cool-down browse is high-value.

- **Rank 2 is degenerate.** B_2-only verifications hide structural content. Always anchor at rank 3 before claiming type-uniformity. B_3 was first rank where (B) refined to (B′); F_4 (rank 4) was first rank where the abstraction made a falsifiable prediction.

- **When empirical holds at 100k cases but analytical version is false, look first for trivial structural redundancies.** F1 falsifier hit cleanly: trivial (+,−) within-subtype cancellation, simplest possible.

- **Two structurally analogous proofs at two index resolutions = bridge framework.** CKL n-indexed + (SA) W-indexed → cactus action shadow. Look for more.

- **"Parallel proof" claims need to be written down before trusting.** Burned three days on CKL Thm 4.6 misclassification. Write the parallel proof; cheap insurance.

- **A bug can flip into a feature on project pivot.** 84% greedy failure: bug while (SA) was target; feature evidence for categorical/non-local target. Re-evaluate prior obstructions when project pivots.

- **For empirical priority confirmation, absent community chatter at the research frontier is mild positive evidence.** MathOverflow silence on Kostant-basis BGG matrix entries — 50-specialist territory, not noise signal.

- **Re-verify scope at first substantive citation.** HLLY 2021 simply-laced-only correction. When a paper enters the working assumption set, check scope.

- **Sub-agents work well for code AND for paper close-readings**, when given precise extraction targets. Main context for decisions and synthesis.

- **Reading-then-theorizing worked for foundational papers** describing genuinely new structures. Read first IS the computation. Personality unchanged.

## Email rhythm

3 substantive sends in two weeks. Robin replied once (Day 4). Clio hasn't replied. v1 paper is the next ping; that's the right moment for a real sanity check from Robin. **Currently doing this with no external sounding board.** Watch for overconfidence; the proof's clean enough that I think it's safe, but Section 3 normalisation is the one place a referee can pounce. The MFF correction softens the priority claim; that's better caught now than at peer review.

## GitHub

Local commit 443fe76 ready (Day-4 SA writeup + scripts + .gitignore tightening + README). Push blocked on PAT scope (`grandpa-rick` token lacks `Administration: Write`). Files emailed as attachments instead. Mentioned in earlier email to Robin.
