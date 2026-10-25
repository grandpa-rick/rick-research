# Q488 converse: do jump≥2 Motegi type-B/C structure constants always have a pole on a short-root (e_a+e_b) divisor H_ab?

Opened 2026-10-17 (Wake/PROVE 243). Peer: Clio, `peers/clio/proofs/2026-10-16-Q488-korepin-locus.tex` (gap:nonvanishing).
Registry `proofs/registry/q488-converse.json` (root in-progress). Proof files `proofs/2026-10-18-q488-converse-order-q1.md` and `proofs/2026-10-17-koncki-LG24-motegi-correction.md`.

## Reframe (Day 244 PROVE, computed at N=2)
- The poles are **Motegi's normalisation defect, not geometry**.
  - Koncki's twisted mC basis of LG(2,4) (thesis §6.2.1) has Laurent structure constants. That is automatic for any R(T)[y]-basis of honest classes.
  - Motegi's Ã has the (st−1) pole.
  - Dictionary: y=−q, w₁=1/s, w₂=1/t, λ∈(0,½].
- **Prop K (N=2, proved):** 15/16 is the maximum agreement for any honest table. The odd entry is (24)|e13 = Ã_{12,∅}, and the ratio there is g.
- So Q488 becomes a question about the **change-of-basis matrix C: Ã → honest**.
  - At N=2, C has one off-diagonal entry, q(1−q)/(1−1/(w₁w₂)), on the point class.
  - Clio's poles of c^ν_{λμ} are the honest Laurent constants conjugated by C.
  - Expected: Thm 6's support condition (∃M''⊆[N]∖ab with M''≥λ,μ) is the support pattern of C.

## Day 245 resolution of the H_ab half (registry wins)
- **Theorem Ψ (proved, all N):** Clio's vertex gauge Â = Ã·Ψ, Ψ(M)=∏_{m∈M}ψ(w_m), ψ(v)=(1−qv²)/(1−q), is an honest GKM class on LG(N,2N). Registry `q488-theorem-psi-honest-gkm`; file `proofs/2026-10-18-theorem-psi-honest-gkm.md`.
- **Corollaries (proved, all N):** the structure constants of Â are regular on every C_N root divisor, and Â→(any honest basis) is root-free. Registry `q488-psi-corollary-no-root-poles`.
- **So Q488's H_ab-poles are a normalisation artefact.** Ã spans the g-twisted lattice, products land in the g² lattice, and Ψ is a 0-cochain (NOT a global class), with ρ = g = δ(1/ψ).
- The old item 1(ii) ("GKM-only correction C at N=3") is ANSWERED: the correction is the vertex gauge Ψ. It is not a basis-change matrix.

## Day 246 resolution of the converse on H-divisors (registry wins)
- **(D∞) PROVED, all N** (`q488-qinf-D-infinity`). **Clio's converse PROVED on the H-divisors, all N, generic q**
  (`q488-converse-all-N`): c^ν_{λμ} has a pole on H_ab ⟺ E(λ,μ,ν;ab) := {M'' ⊆ [N]∖ab : M''∪ab ≤ ν, M'' ≥ λ,μ} ≠ ∅.
  Both are modulo ONE cited theorem, Motegi 2610.15344 all-cardinality biorthogonality (L4365–4411).
  File `proofs/2026-10-18-q488-d-infinity.md`.
- New proved nodes: `q488-phi-inf-closed-form`, `q488-phi-inf-dual-biorthogonality`, `q488-weighted-theorem-W`.
  `q488-qinf-residue-formula` and `q488-qinf-dichotomy` were upgraded to proved.
- Correction: Thm 6 is an aggregate over ν. The per-ν condition is E ≠ ∅.
- Dream 246 (hunch): `connections/2026-10-18-q0-qinf-are-w0-bar-duals-and-only-one-end-is-clean.md`.

## Status (registry wins)
- **(Day 246 additions, proved, all N mod Motegi):** D∞, converse-all-N, φ^∞ closed form, dual (D), Theorem W,
  ∞-Thm 7, dichotomy. The list below predates Day 246; the dichotomy "hunch" entry is now superseded.
- **proved:**
  - (a) c ∈ C(w)[[q]];
  - Lemma QC;
  - the q=0 formula + Lemma L;
  - aggregate converse Thm 6 (full q);
  - residue Thm 7;
  - Thms 9 and 9′;
  - (d) Thm 10;
  - **Theorem Ψ + corollaries (Day 245)**.
- **dead-end:** (b) and (c). Both are FALSE at N=4.
- **computed:**
  - N=4 full-q 127/127;
  - `q488-n5-cfail-stratum`;
  - `q488-motegi-correction-is-g` (N=2);
  - `q488-psi-renorm-honest-n3-n4`, now subsumed by Theorem Ψ.
- **peer-claimed:** Clio's ρ-boundary, coboundary, QC recheck at N=4, and Koncki no-go nodes.
- **hunch:** `q488-qinf-dichotomy` (first order at q=0 OR at q=∞). Mechanisms:
  - Day 244: g−1 vanishes at both ends.
  - Day 245 dream: Ψ is a monomial gauge at both ends (1 and ∏w²), and bar(ψ)=v²ψ(1/v). See `connections/2026-10-18-psi-is-a-c2-levi-gauge-monomial-at-both-ends.md`.

## Open
1. **(Q)-divisor half of Clio's Thm B** (her 0/115 at N=3, computed). Ask Clio for an argument. No GKM edge controls the (Q)-factors.
2. **What IS Â geometrically?** Â ≠ Koncki at N=2: Â→Koncki is lower-triangular with denominators (s²−q)(t²−q) = Ψ-divisors (dictionary checked by hand, Day 245 dream).
   - Prediction N=3: Â→KW twisted mC has denominators ⊆ {1−qw_i²} only.
   - Revived (not refuted by the Day 244 kill, which was about Ã): Â = twisted mC at another slope or chamber?
3. ~~Owner of ψ~~ ANSWERED Wake 246 (sketched): ψ is the j=k diagonal factor that E^B (Def 2.13) has and E^C (Def 2.8) omits. It is not a K-matrix factor. Node `q488-psi-is-motegi-EC-diagonal-completion`.
4. ~~Per-ν converse / q=∞ mirror~~ ANSWERED Day 246 (D∞, above). The transport route was a tautology (`q488-mirror-transport-formal`, sketched); the working route was Motegi biorthogonality.
4a. **Weight window: mostly ANSWERED Day 247 (PROVE 247 + 247b).**
   - W⁺: c ≤ −1 clean (proved).
   - Z^A_2 = ∅, Z^A_3 = {2}, Z^A_4 = [0,4] (proved). [0, 2N−4] ⊆ Z^A_N (proved).
   - Z^A_5 = [0,6], Z^A_6 = [0,8] (computed, certifier).
   - Upper end proved for λ, μ ∈ G (U_G).
   - **Still open: the upper end for all N.**
     - Route 1: closed form for the u→0 dual block sums (certifier gap 1).
     - Route 2 (dream hunch): sign-coherence of R/Weyl-denominator beyond the Δ wall. See `connections/2026-10-19-zero-window-is-a-cn-wall-crossing-strip.md`.
   - Also open: the C-cancellation nodes (7 at n=5, 208 at n=6) and the 325 N=7 A-triples with ν^c a length-3 block.
   - **Update 2026-10-20.** Route 2 KILLED (Wake 248, `proofs/2026-10-20-sign-coherence-probe.md`). Route 1 done (PROVE 248, `proofs/2026-10-20-dual-block-identity.md`):
     Lemma A, P/P\*, P1/P1′/P2 proved; C/B n≤6 and A N≤7 all certified ⇒ **Z^A_7 = [0,10]** (computed). The C-nodes and the 325 are CLOSED.
     All N now reduces to **(SC)** (some peel policy gives σ=±1) plus the multi-block tie identity **(α)** (file §6).
     Day 248 dream hunch: (α) is a K-Chevalley instance for GQ, and (SC) is GKM triangularity (`connections/2026-10-20-twisted-psi-is-ikeda-naruse-GQ-at-fixed-points.md`, kill tests K0–K2).
   Original question text:  Is Theorem W sharp? Is c=−1 clean? Is the zero window even c ∈ [0, 2N−4]? See the predictions in the Day 246 dream connection. A q=0 mirror theorem (wt0 nonzero for c ≥ 2?) would explain the window {0,2,4} ↔ {−4,−2,0}.
4b. **Insurance: Theorem W A2/A3 cold re-read PASSED Day 247.** The Motegi RTV step is still unchecked (gap 1). Original:  Do a cold re-read of Theorem W cases A2/A3 (the induction's asymptotic steps). Re-derive Motegi biorthogonality, or at least check the RTV U↦U^⊥ step, to remove the one citation (gap 1).
5. Block factorisation (sketched, one N=6 example).
6. φ⁰ = GQ (Ikeda–Naruse 1112.5223): literature-supported via Motegi L5645, not checked first-hand.
7. Cross-checks: Jeon 2509.24348 (agent-summary) and Micheli 2507.15841 (degenerate LG GKM, agent-summary, Browse 189).
8. Owner of the colength argument in Cor 1 (standard triangular-GKM-basis lattice count, e.g. Knutson–Tao / Guillemin–Zara style; locator NOT checked). Credit it as standard, never as new.

9. **Owner of Lemma Δ** (dual of the F-basis at κ=[n] = C_n Weyl numerator).
   - NOT in Motegi (Wake 248: Thm 4.18 gives the inverse entries, the det evaluation is ours).
   - Chain from Browse 193/194: GILL 2607.03966 → Mimachi (Duke 107 (2001) 265–281, pre-arXiv) → Sahi **q-alg/9710032** (not math/). Unread first-hand. curl + local extraction, since WebFetch garbles it.
   - Day 248 dream candidate (cheaper): Borel–Weil–Bott / Weyl character on Sp_{2n}, since κ=[n] ↔ the zero-part staircase in GQ indexing. See the 10-20 crown.
10. **Is Ψ_{κ,θ} twisted GQ = GQ·[O(θ)]?** (Day 248 dream). If yes, import IN 1112.5223 vanishing + K-Chevalley (Buch–Ravikumar, Crelle 668 (2012) 109–132) [Wake 252: Mihalcea–Naruse–Su 2312.17200 DROPPED from the type-C K-Chevalley shortlist — it is a type-uniform Chevalley formula for motivic Chern classes via λ-chains, never writes out type C/LG, GQ never appears (Clio uid438 §4, token census on the LaTeX). Owner for LG(n,2n): Buch–Ravikumar, 'Pieri rules for the K-theory of cominuscule Grassmannians', Crelle 668 (2012) 109–132 (located, not read).] for (α)/(SC). Kill test K0 = recompute from the printed (2.17).

11. **PROVE 249 cycle 2 (2026-10-21): (SC) SUPERSEDED.** All-N upper end ⇐ **HP**: the centre polynomial P (the lowest
    ε-coefficient of X(c)/X₀ on w = 1+aε; Lemma E, proved) has no integer root > U. HP⁺ (P(U+1+t) one-signed) is exact at
    C n ≤ 4 and A N ≤ 4. File `proofs/2026-10-21-window-hilbert-polynomial.md`. The open question is now the
    Kodaira-strip dictionary (K1′): is P the Hilbert polynomial of a twisted Richardson-type sheaf on LG(n,2n), with
    HP = vanishing? The naive dictionary fails at κ = {3}.

## Process lessons
- feedback_check_n_plus_one_before_prove_target: both false targets came from N≤3 data. N=4 at q=0 runs in minutes.
- feedback_gkm_is_a_typo_detector (Day 244): GKM caught my transcription slip and Koncki's p.71 typo.

## Day 249 dream update (2026-10-21; registry wins)
- **Upper end, all N.** (SC) is superseded by HP on the centre polynomial (Lemma E proved). For λ=μ=∅ at even c the case is
  Theorem E (computed: it is proved mod cited G1–G4). Type A is reduced to type C at d=0 (Theorem AC proved given D; Cor AC′
  computed, mod Gap 6). What remains:
  - (11a) **odd c / (OC) / HP⁰⁺.** The crystal route is in `connections/2026-10-21-hp0plus-is-interior-ehrhart-of-demazure-atoms.md`.
    Next: the LP test for a binom(s+a,b) decomposition at n=3,4.
  - (11b) **the triple-intersection Theorem E for general (λ,μ).** It needs Cor D2 pinned.
  - (11c) **the exceptional type-A instances** (d ≥ 1, non-constant). Computed: they are type-C polynomials shifted by
    s ∈ {0,1,2}. Mechanism unknown.
- **(12) Cor D2 pin: is F_λ ∝ L_ω⊗ξ^λ?** This is the ideal-sheaf basis. `ideal.py` failed with the naive orientation and
  twist. The 2×3×2 sweep is in `connections/2026-10-21-motegi-biorthogonality-is-k-theoretic-poincare-duality.md`. If it
  passes, K0 becomes a corollary of Theorem D and K1 is answered.
- **(13) Owner read: Mihalcea–Naruse–Su left Demazure–Lusztig operators** (pin the ID). Are Lemmas A_m/B their left
  operators at fixed points? One read, then footnote.
- **(14) Theorem AC = localisation to an LG(N−2) fixed component?** Compare normal weights with vG(v) at N=4.
- Superseded: item 10's K1 (K-Chevalley route to (α)). (α) is closed by Theorem S, and K1's remaining θ-twist question
  is now (12).

## Day 250 dream additions (2026-10-22)
15. **Owner of (D)'s meaning.** Pin the classical structure-sheaf ↔ boundary-ideal duality: Brion math/0410240 (believed), and
    Graham–Kumar positivity in K_T (ID?). Footnote `proofs/2026-10-22-dfree-biorthogonality.md`.
16. **(OC) = canonical strip for Schubert X_κ ⊂ LG.**
    - Deep-read Manivel 0904.2470 (top cell) and Golyshev 0903.2076.
    - Test: are the rational roots of P^κ at m=3,4 a sub-multiset of the top-cell short-root half-integers −(i+j)/2?
    - Literature: has anyone done the strip for Schubert varieties?
17. **Crown 2 risk.** Read Li–St. Dizier 2608.00377's mechanism, then run HP⁰⁺ at the next size before promoting it.
18. **Marberg door.** Do GQ coproduct coefficients alternate in sign via i^* along LG(a)×LG(b)→LG(a+b) (Brion / AGM)? Read
    Conj 4.35/4.36 first.
19. **Type B (D).** Same three lemmas on OG(n,2n+1)? Only if a reader asks.

## Wake 251 update (2026-10-22; registry wins)
- **15 answered (pinned):** Brion math/0410240 Thm 3.4.1; Graham–Kumar 0801.2776 Prop 2.1 (Buch math/0004137 §8).
- **16:** sub-multiset test FAILS (κ=(2,4),(1,3,5); κ=(3) root −3/4) — route dead. Strip −(r+1)/2 ≤ Re j < −1/2 computed m≤7;
  no Schubert-variety strip in literature. H_κ = LS parity order-quasi-polynomial (computed m≤5). **Live target: the odd-zero
  law** (H_κ(−M/2)=0 at odd M exactly for M=3..2⌈r′/2⌉+1; computed m≤6) ⇒ (OC). Prove it from the shifted/parity poset.
- **18 closed:** Marberg 2512.19045 Cor 1.4 proved Conj 4.35/4.36.

## Day 251 dream additions (2026-10-22; registry wins)
- **Resolved/superseded:**
  - 16 ((OC) via the strip) is superseded by PROVE 251 Thm B (computed, mod G1–G4).
  - 18 (Marberg door) is dead: 2512.19045 Cor 1.4.
  - 17 (Crown 2 / HP⁰⁺) is parked.
20. **Case B via the hyperplane section.**
    - ∂X_κ = X_κ ∩ H, so H_κ(j) − H_κ(j−1) = χ(O_{∂X_κ}(j)).
    - Anchor at Thm C (M=3 zero, proved). The run of odd zeros M=3..2⌈r′/2⌉+1 then follows iff χ(O_{∂X_κ}(−M/2)) = 0 for
      M = 3..2⌈r′/2⌉−1.
    - Prop H should extend to ∂X_κ: the Demazure character formula holds for unions of Schubert varieties (Frobenius split).
    - **Test:** compute χ(∂X_κ, ·) at half-integers by inclusion–exclusion, m≤5. Check whether the deep terms (codim ≥2,
      where r′ drops more) cancel or break it.
    - If they cancel, Case B and Case A are one induction on |κ|.
21. **Exact staircase = top cell.** δ_m = (m,…,1) gives X = LG, and H is the Weyl product, so the zeros can be read off.
    Confirm that the proof file's "Case B, e.g. the staircase" means near-staircase, and add a one-line remark that δ_m is
    Weyl.
22. **Pfaffian for Thm R** from the Sergeev/Clifford side (Crown D §3), rather than guessed. The subset-sum form
    Σ_S(−1)^{|S|}Π ε_r·Ĵ_S is already Pfaffian-shaped per S.
23. **Crown D tests** (`connections/2026-10-22-half-integer-twist-is-spin-twist.md` §4): LG(half) ↔ OG(integer) exchange;
    Thm A as a spin-crystal Demazure count; Kashiwara–Vergne owner check.
24. **§7 gap 4.** The integer window H_ν(−b)=0 for 1≤b≤⌊(r+1)/2⌋ is used in the application of Prop R to (Z) but has no
    LS-free geometric proof. Kawamata–Viehweg/Kodaira on X_κ (Day 249 "window = Kodaira strip") is the natural source. Grade
    the dependency honestly in the PDF.

## Day 252 dream additions (2026-10-23; registry wins)
- **Resolved:**
  - 20 (Case B) is closed by PROVE 252 Theorem Z, `q488-oc-Z-by-induction`, computed / conditional-proved given G1 + BR support.
  - 23 (Crown D) is dead (Wake 252 test 1).
  - 21 is moot: Theorem Z covers the staircase.
  - 22 (Pfaffian) is parked, since (Z) no longer needs residues.
25. **Deep-read Buch–Ravikumar 1005.2605 §5 (Cor 5.4 / eq. (11), p=1).**
    - Confirm the support inclusion literally, and that "rim" excludes the diagonal 3-box shape {(r,r),(r,r+1),(r+1,r+1)}.
    - This is the ONLY gap between Theorem Z and "proved given G1".
    - Browse 201's citation agent was pulling exactly this when the session ended under it (background agent). Run it
      FOREGROUND.
    - Clio was asked the same thing in `for-collaborator/2026-10-23-prove252-Z-closed.md`.
26. **Gap 4 (Q24) by the same induction.**
    - Anchor H_ν(−1) = 0, use Lemma Ch on the full diagram, telescope to ⌊(r+1)/2⌋.
    - See `connections/2026-10-23-zero-window-rate-is-k-pieri-height.md` §4(a).
    - Paper-only: check the definition of r and the ℓ ≤ 1 base. If it holds, gap 4 leaves the PDF's gap list.
27. **Height hypothesis, OG test.** Does the K-Pieri support for O^1 on OG have height 1, so that the window is the full
    chain? Cheap compute, m ≤ 5.
28. **(NZ) middle range** is still open. Edge sign-coherence is dead (`q488-oc-NZ-edge-sign-coherence`).
    - Candidate: (NZ) = "the first point past the window is the strict-reciprocity count". In type A, Ω(P,−(ℓ+1)) = ±(number
      of strict maps to [ℓ+1]) ≠ 0.
    - So look for an LG strict-map count (height-2 "strict" maps) at the first point beyond ⌈r′/2⌉. It would be a positive
      formula, which sign-coherence of Pieri terms never could be.

## Wake 253 (2026-10-23)
- **25 RESOLVED:** BR read first-hand; rim = no two boxes strictly SE, which excludes the diagonal 3-box shape. Z-by-induction is proved given G1.
- **27 RESOLVED (computed):** OG p=1 support = rook strips (height 1); zero window = full chain, 63/63 at m=6.
- **26 → PROVE 253** (Z_int, plus the OG twin Z_OG).
- **28 data:** NZ holds for all κ at m≤7. Fitted sign rule is a hunch; no count found. Integer side: strict-map formula with even
  diagonal values, 127/127.
- **29 NEW:** OG sporadic half-integer zeros (10 κ at m=6, e.g. 32 at −5/2, 51 at −3/2). Is this an accident or structure?

## PROVE 253 + Day 253 dream (2026-10-23; registry wins)
- **Resolved:** 24/26 (gap 4) by Theorem I (`q488-oc-Zint-by-induction`, proved given G0/G1/BR). 27 is a theorem on the
  window side (`q488-oc-ZOG-by-induction`). 28: the integer half is done (NZ_int, Theorem I), the half-integer range
  M ≤ κ₁+1 is done (`q488-oc-NZ-propR-range`), and the even-μ₁ base is done (Lemma E). **Only the odd-μ₁ base
  4f(μ′,b₀−1) ≥ s_{b₀+1}(μ) plus strictness remain** (`q488-oc-NZ-beyond-reduction`).
30. **KLG = strict fillings?** For every (κ,θ) in the LG p=1 support, is |c_ρ| (BR Cor 5.4 h-sum, `strip.py` `brpieri.C`)
    equal to F(θ) = #{strict maps θ→{even<odd}, diagonal boxes even}? Brute-force at m ≤ 7, about 10 min. If yes,
    `q488-oc-integer-strict-reciprocity` is proved given G0/G1/BR by iterating (★) from s₁ = [κ=∅], and its LS dependency is
    gone. See `connections/2026-10-23-kpieri-is-inclusion-exclusion-on-corners.md` §3. OG analogue (|c| = 1 on every nonempty
    corner set) is a citation of BR Lemma vanishB; check orientation via Lemma S, then register the OG strict-count identity
    (§2) as a node.
31. **(NZ) as a sign-reversing involution.** If 30 holds, 2^{κ₁}(−1)^{|κ|}H_κ(−a−½) = Σ_{ν⊆κ}(−1)^{|ν|}2^{κ₁−ν₁}N_a(κ/ν) with
    N_a = strict fillings of κ/ν by [2a] with diagonal even. Find the toggle (candidate: a first-row box moves between ν and
    κ/ν). Target: the odd-μ₁ base. Check first that Prop R is the "everything but the first row cancels" case. Even if 30
    fails, the formula holds with N_a = iterated |c| weights.
32. **Owner search: LG Hilbert function as a peak-algebra character.** OG/type A: H(−j) = antipode-twisted ABS character
    (classical: ABS math/0310016, Grinberg–Reiner 1409.8356 §5.2). LG "diagonal even" looks like Stembridge enriched
    P-partitions / the peak algebra. Search Stembridge 1997 (Enriched P-partitions), Billera–Hsiao–van Willigenburg (peak
    QSym), and any "Hilbert function of Lagrangian Schubert variety" + "P-partition". Browse item, not PROVE.
33. **m=5 Demazure check without interpolation.** `check.py 5` was killed after 50 min, and `mono.py 5` was killed too
    (`scripts/prove253/mono5.out` holds only the kill line). Evaluate χ(X_κ,O(−j)) = (D_w e^{−jω})(1) DIRECTLY at negative
    weights (the same trick as Lemma 1's anchor). That avoids the degree-15 exact-Fraction interpolation. Low priority:
    Theorem I is proved and m ≤ 4 + m ≤ 7 model checks agree.

## PROVE 254 + Day 254 dream (2026-10-24; registry wins)
- **Resolved:** 30 YES and PROVED (`q488-oc-Q30-KLG-strict-fillings`, given BR Cor 5.4 + Thm 5.5; §3.3 hand-written,
  unrefereed). 31 PROVED as Theorem HZ (`q488-oc-HZ-half-integer-law`, §9). The involution is the Lemma 9.2 bottom-row toggle
  plus the Lemma 9.4 shift, so the odd-μ₁ base is moot. 28 is fully closed. The `NZ-computed-m7` hunch sign rule is proved
  by HZ.
- **Open, in priority order:**
  - 35. **Write-up gate:** the (OC)/odd-zero sub-arc is done modulo (G0, G1, BR) and Clio's referee of §3.3 + §9.3.
    Owner search before /write (Q32 below), then decide arXiv note vs FPSAC (Robin's call, deadline 2026-11-15).
  - 32 (sharpened, Crown G §1). Dictionary: odd value ↔ primed letter, diagonal even ↔ unprimed diagonal. Search
    Stembridge "Enriched P-partitions" (TAMS 349, 1997) reciprocity; De Concini symplectic standard tableaux / doset
    ASL (Hilbert function of LG Schubert varieties); Proctor d-complete posets (P_κ shifted = d-complete); Ikeda–Naruse
    1112.5223 K-hook / excited Young diagrams. Question for each: does it state H_κ(−j) (or F_κ reciprocity) for LG Schubert?
  - 34 (new, Crown G §3). Is T = (I+C)^{1/2} (ribbons through one diagonal box, ±2^{−|D|}) the shifted Murnaghan–Nakayama
    rule for Q-functions in disguise? 30-min compute: MN coefficients for Q_λ·p_k restricted to double strips vs `tprime.py`.
  - 36 (new). LS-parity model and OG Ω-model are corollaries of SR_LG/SR_OG + Ehrhart–Macdonald/Stanley reciprocity (Crown G
    §2). Write this as a corollary in the PROVE 254 file, then promote `q488-oc-ls-parity-model`.
  - 29 (OG sporadic half-integer zeros) and 33 (m=5 Demazure without interpolation) remain. **33 was ignored again:**
    PROVE 254 launched an m=5 interpolation run that died with the session (no output file exists). Checks stand at m ≤ 4.
  - (OC) for triple intersections: unchanged since Day 251, and no one has looked.

## Wake 255 (2026-10-24)
- **32 RESOLVED (gate passed):** SR_LG not stated anywhere checked; SR_OG is a classical composite (credit). Risk paper
  2609.03195 (CCFL, interior LS paths) is read first in PROVE 255. Report: `reading/2026-10-24-q32-owner-search.md`.
- **34 REFUTED (computed N≤4):** T ≠ shifted MN (WIP f3918f0, scripts/wake255/).
- **36 DONE:** Corollary M written (§5.1, c321c27); `q488-oc-ls-parity-model` proved.
- 37 (new, = PROVE 255). Is there a BR-free proof of SR_LG, going LS paths ⇒ model (M) ⇒ Ehrhart–Macdonald? The core
  is a bijection between LS paths of shape jω_m with bond-2 half steps and weak even-diagonal maps into {0..2j}.

## PROVE 255 + Browse 205 + Day 255 dream (2026-10-24; registry wins)
- **37 ANSWERED (computed):** §11 gives a BR-free proof (Lemma 11.1 bonds, 11.2 parity, Prop 11.3 bijection).
  `q488-oc-ls-bijection` is proved. `q488-oc-SR_LG-via-LS-paths` is computed and becomes proved once the (LS) locator is
  read. **[2026-10-25: now PROVED — Q39 answered, see below.]** Numerics 164/164 (m≤5), OG 72/72, controls fail.
- **Open, in priority order:**
  - 35. **WRITE-UP GATE, now with two SR_LG proofs.** There is ONE remaining gate, 39. The folklore risk (De Concini
    1979, Dehy 1998 §4.2.2) goes in a footnote and does not get a session. Then /write "Negative-degree Hilbert functions
    of Lagrangian and orthogonal Schubert varieties". Robin decides the venue (FPSAC 2026-11-15, 22 days out).
  - 39 (new). **[ANSWERED 2026-10-25 — see section below.]** **(LS) locator, one wake deep-read, ≤45 min.** Find the theorem that the LS paths of shape λ with initial
    direction ≤ w give char of the Demazure module V_w(λ). Candidates: Littelmann, "Paths and root operators in
    representation theory", Ann. Math. 142 (1995) [Demazure statement, §5?]; Littelmann, Invent. Math. 116 (1994), the LR
    rule paper; Kashiwara 1993 Duke (Demazure crystals); Lakshmibai–Littelmann–Magyar 1998/2002 SMT. Pick whichever is
    reachable, cite its exact number, then promote `q488-oc-SR_LG-via-LS-paths`.
  - 38 (new, Crown H §2; optional, not a gate). The odd quadric Q^{2m−1} = B_m/P_1 has a chain Bruhat poset with one
    bond-2 step (ε_m → −ε_m, ⟨ε_m, 2ε_m⟩=2). Does its Schubert H(−j) obey strict reciprocity in the CCFL lecture-hall
    lattice? If yes, the paper gets a one-paragraph remark: "cominuscule ⇒ Ehrhart in the bond lattice". Its only
    non-minuscule instances are LG and the odd quadric. 20-min compute, AFTER the draft exists.
  - 40 (new, hunch). Is Q̃ = 2^ℓ P̃ (Pragacz, LG vs OG cohomology) the degree-0 shadow of the bond-2 lattice? Paper-remark
    material only, and only if a check is cheap.
  - 34 REFUTED (Wake 255). 36 DONE (Cor M). 32 PASSED.
  - Still parked: 29 (OG sporadic half-integer zeros), 33 (m=5 Demazure without interpolation), (OC) for triple
    intersections, Aliniaeifard–Li 2506.12868 (only if the paper wants a Θ-character remark), 2609.16765 triage (feeds.md
    QUEUED).

## 2026-10-25 (Q39 locator read; registry wins)
- **39 ANSWERED.** (LS) = Littelmann, *A Littlewood–Richardson rule for symmetrizable Kac–Moody algebras*, Invent. Math. 116
  (1994) 329–346, §5.2 (section number SECONDARY, quoted in Chirivì–Fang–Littelmann 2207.08904; Invent. text paywalled, not
  reached). Statement read FIRST-HAND in Littelmann, Proc. ICM Zürich 1994 vol. 1, §8, p. 305: Λ_{a1}∘⋯∘Λ_{ar}(e^λ) = Σ e^{π(1)}
  over LS paths of shape λ with τ_1 ≤ τ. It is the Demazure-OPERATOR identity; h^0 = #paths also needs the geometric Demazure
  character formula, which sits in (G1′). Also Mathieu, Bourbaki 798 Thm 10 (read). Report:
  `reading/2026-10-25-q39-ls-locator.md`.
- `q488-oc-SR_LG-via-LS-paths` promoted computed → **proved** 2026-10-25 (given (G1′), (LS)); §11 (LS) citation fixed
  (rick-research c272fed).
- New risk from the read: Dehy, J. Algebra 205 (1998) 505–524 (Demazure dims as Ehrhart-type polynomials, per Mathieu §4).
  Unread first-hand; possible overlap with the Ehrhart frame only. Priority up for the write-up footnote.
- Q35 (write-up gate) no longer has an open gate from 39.
