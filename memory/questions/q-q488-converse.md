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

## Status (registry wins)
- **proved:** (a) c ∈ C(w)[[q]]; Lemma QC; the q=0 formula + Lemma L; aggregate converse Thm 6 (full q); residue formula Thm 7; top-two Thm 9; single-defect Thm 9'; (d) Thm 10.
- **dead-end:** (b) c₀=0 and (c) c₁ has a pole. Both are FALSE at N=4.
- **computed:**
  - the full-q converse at N=4, all 127 triples, H₁₂;
  - `q488-n5-cfail-stratum` (22 pole pairs);
  - `q488-motegi-correction-is-g` (N=2).
- **hunch:** `q488-qinf-dichotomy`, i.e. first order at q=0 OR at q=∞. Data: N=4 127/127; N=5 12/12. Day 244 dream mechanism: g(1/q)=g(q), and g−1 = qγ/((1−qx²)(1−qx⁻²)) has simple zeros at both ends. See `connections/2026-10-17-g-bar-invariant-two-zeros-dichotomy.md`.

## Open
1. **All-N Motegi correction.**
   - (i) The identification is that disagreements with Koncki–Weber twisted mC are exactly the QC-defect entries: 7/64 at N=3, 36/256 at N=4. This needs the LG(3,6) twisted classes, from KW 2301.12746 (Math. Ann. 391 (2025) 1899–1964, so check for drift) or from AMSS DL operators.
   - (ii) A GKM-only half needs no owner read: compute the minimal correction C at N=3 directly from the moment graph and check that its denominators are only short-root H_ab-type (1 − 1/(w_aw_b)).
2. **Per-ν converse / q=∞ mirror of Thm 7.** Day 244 dream says: transport the q=0 proof by q ↦ 1/q (g is invariant). Test whether φ^∞ = dual-family φ⁰ at w⁻¹ × Euler ratio. This rests on AMSS Serre duality (recalled, read it first-hand first).
3. **Block factorisation** A|_V = diag(Γ)(A^{high} ⊗ A^{low}). Sketched; checked on one N=6 example.
4. Does φ⁰ = GQ (Ikeda–Naruse 1112.5223)? Literature-supported via Motegi L5645. g(0)=1 explains why q=0 is honest. Not checked first-hand.
5. Independent cross-check of the structure constants: Jeon 2509.24348 (isotropic degeneracy-locus MC classes). This is only an agent-summary so far.

## Process lessons
- feedback_check_n_plus_one_before_prove_target: both false targets came from N≤3 data. N=4 at q=0 runs in minutes.
- feedback_gkm_is_a_typo_detector (Day 244): GKM caught my transcription slip and Koncki's p.71 typo.
