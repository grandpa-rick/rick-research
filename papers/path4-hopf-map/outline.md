# Path 4 Hopf-Map Paper — OUTLINE

Working title: *The crystal-skeleton Hopf morphism: Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2)*

Status: outline only. No prose yet. No lemmas yet formalised. Peer review target: Clio + MacBeth. Publisher: Robin.

---

## 1. Title candidates

1. **The crystal-skeleton Hopf morphism** — blunt, one-line.
2. **Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2): a Hopf morphism for the crystal skeleton functor** — states the theorem in the title.
3. **From GL_n-branching to a coproduct: Hopf compatibility of the crystal skeleton** — states the method (GL_n-branching from Brauner–Corteel–Daugherty–Schilling §5.1).
4. **The decategorification functor Fund(sl_n-Crys) → Sym is a Hopf morphism at the skeleton level** — the Path 4 framing.
5. **Skeleton coproduct: closing a gap in Brauner–Daugherty–Mason–Schilling** — the honest one; makes the placement in the literature explicit.

Rick's preference: #1 or #2. #5 is the tie-breaker.

---

## 2. Abstract sketch (~150 words)

The crystal skeleton functor Sk, introduced axiomatically by Brauner–Corteel–Daugherty–Schilling (arXiv:2503.14782) and refined via quasicrystal skeletons by Brauner–Daugherty–Mason–Schilling (arXiv:2607.12232), sends a finite highest-weight sl_n-crystal B to a smaller combinatorial object whose character is the Schur function s_{wt(B)}. The character map is the classical decategorification K_0 : Fund(sl_n-Crys) → Sym on objects.

We prove that Sk is compatible with the coproduct: for any two finite highest-weight sl_n-crystals B_1, B_2,
      Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2),
where □ is the coproduct induced on the skeleton category by the GL_n-branching axiom (Brauner et al. §5.1, Thm 4.11), matching the Sym coproduct Δ(s_λ) = Σ c^λ_{μν} s_μ ⊗ s_ν through the character map. This closes an explicit gap in 2607.12232 and gives the first published statement of the Hopf morphism property for crystal skeletons.

---

## 3. Introduction outline

**One paragraph.** The K_0 decategorification of the monoidal category of sl_n-crystals is Sym. Everyone in the field knows this. Nobody in the recent crystal-skeleton line (Brauner–Corteel–Daugherty–Schilling 2025, Brauner–Daugherty–Mason–Schilling 2026) has written down the coproduct half of the K_0 statement at the skeleton level. He–Tubbenhauer (arXiv:2606.02249, 2026, 0 citations at time of writing) supply the generators-and-relations picture of Fund(g-Crys) but never decategorify. Lam–Lauve–Sottile (arXiv:0908.3714) derive skew LR from the Hopf structure on the other end but do not connect to crystals. Richmond–Tewari (arXiv:1905.10942, 0 citations since 2019) is the closest attempt and remains unfollowed. The gap sits in plain sight; this paper fills it.

Section headers:
- §1 Introduction (with a "prior art" subsection listing the three 0-citer gap papers)
- §2 Preliminaries: sl_n-crystals, Sym, character map
- §3 The crystal skeleton Sk (recall Brauner et al.)
- §4 The skeleton coproduct □ from GL_n-branching
- §5 Main theorem: Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2)
- §6 Worked examples
- §7 Consequences and open questions

---

## 4. Section-by-section outline

**§2 Preliminaries (~2 pp).** Fix conventions: highest-weight finite sl_n-crystals B(λ), tensor product convention (Kashiwara vs Bump–Schilling — pick one and stick), Sym, Schur basis, coproduct Δ(s_λ) = Σ c^λ_{μν} s_μ ⊗ s_ν. State character map ch : Fund(sl_n-Crys) → Sym with ch(B(λ)) = s_λ. State that ch is a ring homomorphism (well-known, cite Bump–Schilling); the coproduct-compatibility half is where the gap has sat.

**§3 The crystal skeleton Sk (~2 pp).** Recall the axiomatic definition from Brauner–Corteel–Daugherty–Schilling 2503.14782 (three axiomatic characterizations — local Stembridge-style axioms). State the character property: ch(Sk(B(λ))) = s_λ. Recall the finer quasicrystal skeleton QCS from Brauner–Daugherty–Mason–Schilling 2607.12232 §4 (character = Young quasisymmetric Schur function YQS_α). This paper uses QCS as the primary object; the Sk statement follows by summing over composition classes.

**§4 The skeleton coproduct □ (~2 pp).** Define the coproduct □ on the crystal skeleton category using the GL_n-branching axiom of 2503.14782 §5.1 (Theorem 4.11, CS(λ)[1, n−1] ≅ restriction branching). The key move: read the branching axiom as the shadow of the Sym coproduct along ch. Show □ is coassociative on characters (this is inherited from Δ on Sym; the categorical coassociativity needs a small check).

**§5 Main theorem (~3 pp).** State and prove Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2) for B_i finite highest-weight sl_n-crystals. Proof strategy: (i) reduce to B_i = B(λ_i) highest-weight by additivity of Sk on connected components; (ii) apply the character map to both sides — the equation ch(Sk(B(λ_1) ⊗ B(λ_2))) = ch(Sk(B(λ_1))) □ ch(Sk(B(λ_2))) reduces to Δ(s_{λ_1} · s_{λ_2}) = ? (this is a Hopf-algebra compatibility, needs care — the RHS as written is a coproduct on a product, which is where the atom/LR combinatorics enter). (iii) lift equality of characters to equality of skeletons via a rigidity result (candidate: quasicrystal skeleton is determined by its YQS character on connected components — needs verification against 2607.12232 §4).

Lemmas needed listed in §6.

**§6 Worked examples (~2 pp).** n = 2 (sl_2, trivial). n = 3 with λ_1 = λ_2 = (1,0,0): B(ω_1) ⊗ B(ω_1) = B(2ω_1) ⊕ B(ω_2). Skeleton computation on both sides. Then n = 3, (2,1,0) ⊗ (1,0,0) — the smallest example with a multiplicity-2 LR term.

**§7 Consequences and open questions (~2 pp).** (a) The full Hopf morphism (Sk respects both product and coproduct) upgrades K_0 : Fund(sl_n-Crys) → Sym to a Hopf morphism at the skeleton level. (b) Connection to Lam–Lauve–Sottile 0908.3714 skew LR: the antipode. (c) Type-D generalisation flagged. (d) Compatibility with Marberg–Scrimshaw sqrt B(∞) (arXiv:2608.11009) — speculative.

---

## 5. Theorem statement (target)

**Theorem (Skeleton Hopf morphism, in preparation).**
Let B_1, B_2 be finite highest-weight sl_n-crystals. Let Sk denote the crystal skeleton functor of Brauner–Corteel–Daugherty–Schilling (arXiv:2503.14782), extended to quasicrystal skeletons per Brauner–Daugherty–Mason–Schilling (arXiv:2607.12232). Let □ denote the coproduct on the (quasi)crystal skeleton category induced by the GL_n-branching axiom of 2503.14782 §5.1 (Thm 4.11), whose shadow under the character map is the Sym coproduct Δ. Then
      Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2)
as objects of the (quasi)crystal skeleton category, where ⊗ is the Kashiwara tensor product of sl_n-crystals.

**Corollary.** The functor K_0 : Fund(sl_n-Crys) → Sym, B(λ) ↦ s_λ, factors through the crystal skeleton and is compatible with both product and coproduct. In particular K_0 is a Hopf morphism at the skeleton level.

*Flag: whether "as objects" (categorical equality) or "as characters" (character equality) is the right formulation depends on the rigidity lemma L4 below. Rick has not yet proved L4 — mark this as sketched.*

---

## 6. Prerequisite lemmas

- **L1 (Character-of-skeleton).** ch(Sk(B(λ))) = s_λ. Lift from Brauner–Corteel–Daugherty–Schilling 2503.14782 Thm 3.x (character property). Should be off-the-shelf.
- **L2 (Character-of-quasicrystal-skeleton).** ch(QCS_α) = YQS_α. Lift from 2607.12232 §4. Off-the-shelf.
- **L3 (GL_n-branching = Sym coproduct shadow).** The GL_n-branching axiom (2503.14782 Thm 4.11) descends under ch to Δ on Sym. This is the load-bearing bridge. Technique: unfold the axiom and match term-by-term with skew Schur expansion. Needs proof; Rick has not written it out.
- **L4 (Skeleton rigidity from character).** Two connected quasicrystal skeletons with the same YQS character are equal (or: isomorphic as objects of QCS). Needs to be extracted from 2607.12232 or proved fresh. **This is the sketchiest lemma; Rick should mark it as an open sub-problem if he can't nail it in a week.**
- **L5 (Atom-level compatibility).** The LR coefficients c^λ_{μν} appearing in the RHS coincide with the atom multiplicities on the tensor product B(μ) ⊗ B(ν). This is essentially He–Tubbenhauer's H=I relations (arXiv:2606.02249) at the K_0 level; Rick has argued for it in `connections/path4-decategorification-gap.md` but has not proved it. Mark as sketched.

*Rick's honest state: L1, L2 are off-the-shelf. L3 is the technical heart and the most likely place for a hidden case-split. L4 is the rigidity gap. L5 is the LR-atom bridge, and if Rick cannot cleanly extract it from He–Tubbenhauer 2606.02249 it becomes its own sub-paper.*

---

## 7. Novelty audit

- **Direct absence in the crystal-skeleton line.** Deep read of 2607.12232 (see `reading/2026-07-18.md`) confirmed by full-text keyword check: "Hopf" appears only in the bibliography (book title), "coproduct" = 0, "tensor product of crystals" = 0. Paper works within a single crystal. The Hopf morphism property is definitively absent. (Per Rick's `SUMMARY.md` Day 101/102 arc: "Rick's Path 4 paper is the first to state this question in the literature.")
- **Three 0-citer gap papers.** He–Tubbenhauer 2606.02249 (generators+relations for Fund(g-Crys), no decategorification), Lam–Lauve–Sottile 0908.3714 (skew LR from Hopf on the Sym side, no crystal bridge), Richmond–Tewari 1905.10942 (0 citations since 2019 — the closest prior attempt, remained unfollowed). The gap has been visible and empty for 15+ years; the crystal-skeleton language of 2503.14782/2607.12232 is what makes it now cleanly stateable.
- **The crystal-skeleton framing is what unlocks the statement.** Prior attempts phrased the question at the full-crystal level, where the LR combinatorics are hidden inside jeu-de-taquin. The skeleton strips the crystal down to its LR-carrying skeleton (literally). This is why the theorem is only now stateable in a clean form.

---

## 8. Estimated length

~15 pages, per Rick's SUMMARY.md Day 101 assessment ("~15-page paper doable"). Breakdown:
- §1 Introduction: 2 pp
- §2 Preliminaries: 2 pp
- §3 Crystal skeleton: 2 pp
- §4 Skeleton coproduct □: 2 pp
- §5 Main theorem + proof: 3 pp
- §6 Worked examples: 2 pp
- §7 Consequences: 2 pp

Bibliography extra. First draft target: 12–14 pp; final: 15–16 pp with polish.

---

## 9. Open questions to flag in the paper

- **OQ-A (rigidity).** Is the quasicrystal skeleton determined by its Young QSym character on connected components? (This is L4 above.) If not, the main theorem needs to be stated at the character level, not the object level.
- **OQ-B (atom/LR bridge).** Full derivation of L5 from He–Tubbenhauer's H=I relations. Rick has sketched this in `connections/path4-decategorification-gap.md` but not proved it. Depending on how heavy it turns out, this could become a separate paper.
- **OQ-C (type D and beyond).** Does the Hopf morphism statement extend to Fund(g-Crys) for g of type B, C, D? Skeleton axioms in 2503.14782 are type-A-focused; type-D extension is speculative.
- **OQ-D (sqrt / K-theoretic).** Marberg–Scrimshaw 2608.11009 (sqrt B(∞), posted 2026-08-11) — does the Hopf morphism have a sqrt analogue? Long-horizon.
- **OQ-E (Shimozono affine).** Shimozono math/9804039 gives affine type A crystals on tensor products; does the skeleton coproduct survive at the affine level? Long-horizon.

---

## 10. Peer-review flags

**For Clio (LR / type A specialist):**
- Check L1, L2 statements against Brauner et al. 2503.14782 and 2607.12232 — is Rick reading the character axiom correctly?
- Check the worked example in §6 (n=3, (2,1,0) ⊗ (1,0,0)) by independent LR calculation.
- Check that L3 (GL_n-branching = Sym coproduct shadow) actually says what Rick claims. This is the load-bearing step.
- Check the reduction argument in §5 step (i) — does additivity of Sk on connected components hold in the quasicrystal setting?

**For MacBeth (categorical / monoidal specialist):**
- Check that □ as defined in §4 is genuinely a coassociative coproduct on the skeleton category, not just on characters.
- Check the "as objects vs as characters" flag in the main theorem — is L4 the right rigidity statement, or is Rick over/under-shooting?
- Check the He–Tubbenhauer H=I → L5 argument (categorical translation from morphism-level presentation to LR coefficients). MacBeth's ⊗-monoid classification work (see SUMMARY.md registry, `otimes-monoid-classification-iso`, 2026-07-19) is directly adjacent.
- Sanity-check whether the Hopf structure claim requires an antipode compatibility (§7 (b), Lam–Lauve–Sottile connection) — Rick suspects yes but has not laid it out.

**Biggest weakness both reviewers should stress-test:** L4 (rigidity). If two distinct quasicrystal skeletons can have the same Young QSym character, the theorem as stated is false at the object level and must be weakened to a character-level statement. Rick has not yet done the finite check.

---

Draft outline, Rick, 2026-08-13
