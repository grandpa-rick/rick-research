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
10. **Is Ψ_{κ,θ} twisted GQ = GQ·[O(θ)]?** (Day 248 dream). If yes, import IN 1112.5223 vanishing + K-Chevalley (Mihalcea–Naruse–Su; Buch–Ravikumar) for (α)/(SC). Kill test K0 = recompute from the printed (2.17).

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
