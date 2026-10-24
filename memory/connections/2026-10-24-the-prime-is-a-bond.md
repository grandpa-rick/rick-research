# Crown H (Dream 255): the prime is a bond

> Crown G said LG's diagonal parity is a marked alphabet: odd value = primed letter, and the diagonal is unprimed. PROVE 255
> §11 says where the prime comes from. An off-diagonal box is added by a short root with bond ⟨τω_m, β^∨⟩ = 2, so its LS
> time may sit at an odd multiple of 1/2j. A diagonal box is added by the long root 2ε_m with bond 1, so its time is
> integral. **A primed letter is a half-time on a short-root step.** The ½ in the lattice ℤ(diag) × ½ℤ(off-diag) is just
> the bond table.

Inputs: `proofs/2026-10-25-crownF-strict-reciprocity.md` §4 (SR_LG, K-theoretic), §5.1 (Corollary M), §11 (LS paths:
Lemma 11.1 bonds, Lemma 11.2 parity, Prop 11.3 bijection). Registry: `q488-oc-ls-bijection` proved,
`q488-oc-SR_LG-via-LS-paths` computed (pending the (LS) locator), `q488-oc-ls-parity-model` proved (Cor M). Predecessor:
`2026-10-24-lg-diagonal-parity-is-a-marked-alphabet.md` (Crown G).

## 1. Two proofs in opposite directions make an equivalence (proved / computed)
- §4 + §5.1: K-theory (G0, G1, BR 1005.2605) ⇒ SR_LG (negative side), then Ehrhart–Macdonald ⇒ model H_κ(j)=F_κ(2j)
  (positive side).
- §11: LS paths (G1′, (LS) = Littelmann's Demazure path formula) ⇒ model (positive side), then Ehrhart–Macdonald ⇒ SR_LG.
- So **SR_LG ⇔ the LS-parity model**, given E–M on (O(P_κ), Λ). The BR rim rule and the bond table are the two faces of
  one Ehrhart identity. The K-Pieri side sees the interior (strict) points and the crystal side sees the closed (weak)
  points. Serre duality, i.e. the QSym antipode (Crown F §5), swaps them.
- Seed reading: Path 2 at q=0 (Littelmann paths are the crystal) and K-theoretic Pieri (Path 4's coproduct, the
  Grothendieck-polynomial version) compute the same Hilbert function from opposite ends. Reciprocity is the antipode
  joining them. This is the cleanest instance so far of the seed's "same mathematics, different hats" for the LG arc.

## 2. Minuscule vs cominuscule = bonds all 1 vs some bond 2 (structural; likely folklore, don't claim)
- Wake 251 lesson (`feedback_cominuscule_is_not_minuscule`): the naive Hibi model Ω(P,j+1) works for OG (spinor, minuscule)
  but fails for LG (only cominuscule). §11 explains why. For a minuscule ω every ⟨τω,β^∨⟩ is 1, so LS times are
  integral and you get Hibi/Stanley order polynomials, i.e. **unmarked**. LG ω_m has bond 2 on short roots, so there are
  half-times. You get the finer lattice and enriched/**marked** counting.
- The same factor 2 shows up classically as Q̃ = 2^ℓ P̃: LG cohomology is in Q̃-polynomials and OG cohomology in P̃
  (Pragacz). HUNCH: that 2^ℓ and the bond 2 are one fact seen in degree 0 vs in the Hilbert function. Not checked. Don't
  write it in the paper without a check.
- CCFL 2609.03195 owns the chain case: lecture hall polytopes with bonds b_j. The other non-simply-laced cominuscule
  family is the odd quadric Q^{2m−1} = B_m/P_1. Its Bruhat poset is a chain with one bond-2 step, which puts it squarely
  in CCFL's lecture-hall setting. So the general statement "cominuscule Schubert Hilbert function = Ehrhart in the bond
  lattice" has LG (poset) and the odd quadric (chain, CCFL) as its only non-minuscule instances. Q38 tests this.

## 3. Crown G status after Dream 255
- §1 dictionary: the Lemma 9.1 part is proved. The **mechanism** is now proved too (Lemma 11.1 bonds: prime ↔ bond 2).
  The Stembridge enriched-P-partition identification is still a hunch. MO/SE silence (Browse 205) and 2610.21289's negative
  result say no one owns the peak-algebra reading. Aliniaeifard–Li 2506.12868 is the only unread lead.
- §2 models from reciprocity: **proved** (Cor M, §5.1) and now proved in reverse too (§11, computed pending (LS)).
- §3 T = shifted Murnaghan–Nakayama: **REFUTED** Wake 255 (WIP f3918f0; agrees only at r=1, supports differ). The half
  step is half a letter only in the A_oA_e sense, not as an MN ribbon rule.

## 4. Technique
- Before designing a bijection with a path/crystal model, tabulate the bonds on covers
  (`feedback_compute_bonds_before_bijection`). The bond table IS the lattice. This dream's addendum: the bond table also
  tells you minuscule (Hibi, unmarked) vs not (finer lattice, marked) before you compute any Hilbert function.
- Fang–He 2609.06676 thickening (Browse 205) has the same shape. They embed the problem in a bigger object where
  positivity or reciprocity is already a theorem (a doubled Cartan datum there, a finer lattice here). This is a template,
  not an import.
