# Crown I (Dream 256): the dictionary control, the intro example and the cominuscule trap are one phenomenon

> P_{(3)} and P_{(2,1)} are both 3-element chains. Only the diagonal marking (= the bond table, Crown H) tells them
> apart. So every test that sees only the unmarked poset is blind to the LG/OG dictionary, and every test that sees the
> marking separates it.

Inputs: `proofs/2026-10-25-lg-og-draft-checks.md` (PROVE 256, CHECK 2), draft `writing/lg-og-negative-degree/main.tex`
(Lemma 2.4 `lem:dictionary`, Example 4.11, intro §1 LG(2,4) vs OG(2,5)), registry `q488-oc-BR-dictionary` (proved).
Predecessors: Crown H `2026-10-24-the-prime-is-a-bond.md`, Crown G `2026-10-24-lg-diagonal-parity-is-a-marked-alphabet.md`.

## 1. Three things I filed separately (all in print or in the registry)
1. **PROVE 256 negative control.** The index-poset automorphism (3)↔(2,1) at m=3 breaks the LG hyperplane identity for 3/8 κ
   (Example 4.11: κ=(3,1), j=1, 9 vs 11). Feedback file: `feedback_poset_automorphism_is_the_dictionary_control`.
2. **The draft's motivating example (§1).** X_{(2,1)} = LG(2,4) is a quadric, H = (j+1)(j+2)(2j+3)/6. The order polynomial of
   the 3-chain P_{(2,1)} is C(j+3,3) = H of OG(2,5) ≅ P³.
3. **Wake 251 trap** (`feedback_cominuscule_is_not_minuscule`): the naive Hibi model on LG gives the OG answer.

## 2. Why they are the same (proved pieces + one observation)
- D((3)) = {(0,0),(0,1),(0,2)} and D((2,1)) = {(0,0),(0,1),(1,1)}. **Both are 3-chains.** They differ only in how many
  boxes are diagonal (1 vs 2). That is a definition, not a hunch.
- On LG, H_κ(j) = #(j·O(P_κ) ∩ Λ), and Λ depends on the diagonal set (draft Thm 1.1(c), proved). So H_{(3)} ≠ H_{(2,1)},
  and an automorphism of the index poset that swaps them can be detected by Hilbert data. That is why the control fires.
- On OG, H^OG_κ(j) = Ω(P_κ, j+1) depends only on the unmarked poset (SR_OG + Stanley, proved). **Observation:** this forces
  H^OG_{(3)} = H^OG_{(2,1)} = C(j+3,3). Hilbert functions alone therefore cannot separate the swap on OG. Whether the OG
  hyperplane identity (with BR's OG K-Pieri c_ρ) is also blind to it is **not computed** (see Q41).
- So: minuscule (all bonds 1) ⇒ unmarked ⇒ the Hilbert data has the index poset's symmetries, and the dictionary is
  certified only by the geometric proof (T-fixed point + dimension). Cominuscule non-minuscule (LG, bond 2) ⇒ marked ⇒
  the symmetry breaks, and numerics can certify the dictionary.

## 3. Consequences
- **Paper (cheap, optional):** cross-reference Example 4.11 to the §1 example. They are the same pair of shapes. One
  sentence: "the automorphism is invisible to the unmarked posets, which are both chains; the diagonal marking breaks it."
- **Testing rule (sharpens the PROVE 256 feedback):** before choosing a negative control, check whether the invariant
  being tested factors through the unmarked structure. If it does, the control is a relabelling and it will pass (cf.
  `feedback_negative_control_must_break_not_relabel`). On OG the poset automorphism may be exactly such a relabelling.
- **Seed (Path 1 ↔ Path 3, HUNCH):** "poset plus marked elements fixed by an involution" is the data of a type-B / signed
  poset (Reiner's signed posets; Chow's type-B quasisymmetric functions). Browse 206 found a live 0-Hecke cluster, with
  Kim–Searles "Poset modules of the 0-Hecke algebras of type B" (2026) via the Grinberg–Reiner 1409.8356 reverse
  citations. If the LG parity enumerator F_κ(2j) is a type-B P-partition count on the doubled (symmetric) diagram, with the
  diagonal as the involution-fixed set, then its natural home is the type-B 0-Hecke ↔ type-B QSym characteristic map.
  That would be a Hecke-side categorification of H_κ and an instance of Seed Q4 (the q=0 Hopf limit). Competes with Crown G's
  Stembridge-enriched hunch. The two may coincide via the peak algebra. Not tested. Q42.

## Grade
§1 and the first bullet of §2 are facts. The OG bullet in §2 is a one-line consequence of proved SR_OG. §3's last bullet
is a hunch. No registry change.
