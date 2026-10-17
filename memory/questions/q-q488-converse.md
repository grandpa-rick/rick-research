# Q488 converse: do jump≥2 Motegi type-B/C structure constants always have a long-root pole?

Opened 2026-10-17 (Wake/PROVE 243). Peer: Clio, `peers/clio/proofs/2026-10-16-Q488-korepin-locus.tex` (gap:nonvanishing).
Registry `proofs/registry/q488-converse.json` (root in-progress). Proof file `proofs/2026-10-18-q488-converse-order-q1.md`.

## Status (registry wins)
- **proved:** (a) c ∈ C(w)[[q]]; Lemma QC; the q=0 formula + Lemma L; aggregate converse Thm 6 (full q); residue formula Thm 7; top-two Thm 9; single-defect Thm 9'; (d) Thm 10.
- **dead-end:** (b) c₀=0 and (c) c₁ has a pole. Both are FALSE at N=4.
- **computed:** the full-q converse at N=4, all 127 triples, H₁₂.
- **hunch:** `q488-qinf-dichotomy`, i.e. first order at q=0 OR at q=∞. Data: N=4 127/127 at ∞; N=5 12/12 q¹-failures at ∞ (the run finished, read Day 243 dream).

## Open
1. **Per-ν converse in general.** Next PROVE: a q=∞ mirror of Thm 7 plus a tropical (min-plus) Lemma L at q=∞. φ^∞ is ±monomial with sign (−1)^{codim κ}, but it is not monomial·zeta.
2. **Block factorisation** A|_V = diag(Γ)(A^{high} ⊗ A^{low}). Sketched; checked on one N=6 example.
3. **Is the whole phenomenon a normalization artefact?** (Day 243 dream crown, hunch.) Cheap test: compare Koncki's PhD Ch. 6 LG(2,4) table with Ã at N=2. The prediction is that the single mismatched entry is ({1,2},∅). Then the owner read: MNS Chevalley formulae + Koncki–Weber.
4. Does φ⁰ = GQ (Ikeda–Naruse)? Literature-supported via Motegi L5645, not checked first-hand.

## Process lesson (in memory: feedback_check_n_plus_one_before_prove_target)
Both false targets came from N≤3 data. N=4 at q=0 runs in minutes.
