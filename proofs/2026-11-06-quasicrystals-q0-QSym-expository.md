# PROVE 277: Quasi-crystals are the q=0 avatar of QSym (expository write-up of the Q62/Q65/Q66 arc)

Date: 2026-11-06 slot (written 2026-11-05). **The claim is the PDF:** `expository/2026-11-06-quasicrystals-q0-QSym.tex` (.pdf, 9 pp, 0 errors /
0 overfull / 0 undefined refs). WIP copy: `notes/2026-11-06-quasicrystals-q0-QSym.{tex,pdf}`. This .md is the map, not the proof.
Example checks: `proofs/prove277/examples.py`, independent re-implementation from the printed statements.

## Problem statement
Write the finished quasi-crystal arc (PROVE 275 Theorems A/B/P/C, PROVE 276 Q65/Q66) as one self-contained note in which no idea is used before it is proved.

## Dependency order of the note (what restating changed)
1. Words, i-brackets, seminormal crystals. Tensor product in **word order** (x⊗y ↔ xy, the reverse of Kashiwara/CGM; bridge CMRR 2309.14898 p.10).
2. **Lemma 2.4 (concatenation = tensor product)**, proved via brackets: #brackets(uv) = #br(u) + #br(v) + min(ε̃u, φ̃v).
3. Word quasi-crystal (CMRR 2309.14887 Def 2.13), quasification Q (CMRR 2309.14898 Def 4.5), defect δ_i = wt_{i+1} − ε̃_i.
   Lemma 3.5: δ is constant on strings, ≥ 0 for polynomial weights, counts brackets on words, and **Q(word crystal) = word quasi-crystal**.
4. **Defect identity** δ(x⊗y) = δx + δy + min(ε̃x, φ̃y) ⇒ **Theorem 4.3 (Q66)** Q_{B⊗B'} = Q_B ⊗̈ Q_{B'} for polynomial seminormal B, B'.
   Sharpness: det⁻¹⊗det; B(0,−1)⊗B(2,1).
5. **Theorem A is now a COROLLARY** of Q66 + Lemma 2.4 (B = [n]^m, B' = [n]^k). The direct PROVE 275 proof is kept as a second proof.
   Owner: Cain–Guilherme–Malheiro 2301.00271 Thm 5.1 / Prop 5.9 / Def 6.9, with word reversal.
6. Gessel's bijection C_σ ≅ P_D(n), Theorem B (components = std classes, unique ë-source of weight α padded, character F_α).
7. Prop P (tensor ↦ product), Lemma (F-basis of QSym_n), **Theorem 6.5 (Q65)**: K_0(𝒬_n) ≅ QSym_n as rings, commutativity for free,
   stability n → n+1.
8. Theorem C (Levi branching via ψ(w) = (w|≤a, w|>a − a)) ⇒ Res_a ↦ Δ, multiplicative.
9. Corollary 8.1: Sym_n ↪ QSym_n as the K_0 shadow of Q, and s_λ = Σ_T F_{Des T}. Black boxes: B(λ) ⊂ words, Gessel's formula.
10. Punchline (Crown S): tensor ↦ product (positions), branching ↦ coproduct (values). Q is the locus with no cross-cut bracket.
    Seed Q1/Q4. The σ↔σ⁻¹ / FQSym remark is graded **hunch**.
11. Owners. Open questions: intrinsic axioms, antipode/ζ, cross-cut ↔ self-duality. Plus one closed as empty: the opposite kill rule = the opposite monoidal structure.

## Subsumptions found while restating
- **Theorem A ⇐ Q66.** The quasi-tensor rule on words is the special case B = [n]^m, B' = [n]^k of monoidality, once "word crystal of uv =
  tensor product of the word crystals" (textbook signature rule, now proved in-note as Lemma 2.4) is on the page. So the kill clause *is* the cross-cut bracket term. Registry node
  `Q62a-via-Q66` (attempt, proved).
- Theorem B's "ë preserves std" and the b-coordinate action merge into one step (Theorem B proof part (1)).
- Former Crown S "other kill rules" question: it is empty. The opposite clause is ⊗̈ on swapped factors (the opposite monoidal structure), with the same K_0.

## Verification (`proofs/prove277/examples.py`, re-implemented from the printed statements)
Theorem A rule vs definition: 1272 cases (n ≤ 4, |u|+|v| ≤ 3), 0 failures. Swapped-kill control fails (6, n=2). Defect identity on words
(n=3, |u|=|v|=3), 0 failures. Components = std classes (n=3, N=4). C_21 chain 21 →2 31 →1 32. 211/212 dead, std 312/213.
F1F2 = F3 + F12 + F21. Shuffle set {123, 213, 312}. ΔF21 cuts. det⁻¹⊗det: ∞, ∞ vs 0. B(0,−1)⊗B(2,1): alive 1-string ε̈ = 0, 1, 2, while every element of Q_B⊗̈Q_B' is dead.
Theorem B unique source weight = α padded (N ≤ 4, n ≤ 4, all σ), 0 failures. Theorem C ψ bijection + iDes formulas: 464 slices, 0 failures.

## Gaps
None new. Black boxes used only in §8 and in remarks: (1) the tensor product of seminormal crystals is seminormal (only for general B, B' in Q66; for words it is Lemma 2.4);
(2) B(λ) embeds in a word crystal, with ch = s_λ; (3) Gessel s_λ = Σ F_{Des T} (only for the explicit form of Cor 8.1(c)).
𝒬_n is defined via words, so an intrinsic axiomatisation is open (Q1 in the note).
