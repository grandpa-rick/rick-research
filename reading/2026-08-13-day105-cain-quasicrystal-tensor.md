# Cain et al. — quasicrystal tensor product closure — Day 105 assessment

Date: 2026-08-13
Trigger: Rick's Day 103/104 browse pass flagged "Cain et al. quasicrystal ⊗ closure" as a
template for Path 4's `Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2)`.

---

## Executive summary

The reference Rick was recalling is actually **two papers**, both from the
Cain / Guilherme / Malheiro / Rodrigues cluster:

- **Definition of the quasi-tensor product + first closure proof:**
  Cain, Guilherme, Malheiro, *Quasi-crystals for arbitrary root systems and
  associated generalizations of the hypoplactic monoid*, **arXiv:2301.00271**
  (v1: 31 Dec 2022). Theorem 5.1 defines Q ⊗̈ Q′ and proves it is a seminormal
  quasi-crystal of the same type as Q, Q′. This is where the closure property
  "quasi-tensor product of quasi-crystals is a quasi-crystal" originates.

- **The specific closure-under-local-axioms result Rick's memory was flagging:**
  Cain, Malheiro, F. Rodrigues, I. Rodrigues, *A local characterization of
  quasi-crystal graphs*, **arXiv:2309.14898** (v1: 26 Sep 2023). Theorem 3.13:
  quasi-crystal graphs satisfying the local Stembridge-style axioms (LQ1, LQ2,
  LQ3, LQ3′) are **closed under the quasi-tensor product** of 2301.00271.

The second is the sharper match to Rick's mental phrase "closure at the
quasicrystal level, one abstraction below the skeleton": it takes an
axiomatically defined quasi-crystal (analogous to a skeleton in the Brauner et
al. sense) and proves the tensor operation preserves the axiomatic class.

**Verdict: MEDIUM template value, tending LOW.** The mechanism is right; the
missing ingredient is exactly Rick's suspicion — Cain et al. do NOT use GL_n
branching, do NOT decategorify to Sym, and their "quasi-crystal" is a
different mathematical object from Brauner–Corteel–Daugherty–Schilling's
"crystal skeleton". Details below.

---

## The two papers, precisely

### Paper A: arXiv:2301.00271

- **Authors:** Alan J. Cain, Ricardo P. Guilherme, António Malheiro
- **Title:** Quasi-crystals for arbitrary root systems and associated
  generalizations of the hypoplactic monoid
- **Submitted:** 2022-12-31
- **Venue:** subsequently published in European Journal of Combinatorics
  128 (2025) 104172 (per Google search hit)
- **Main relevant theorem (Theorem 5.1, verbatim substance):**
  > Let Q and Q′ be seminormal quasi-crystals of type Φ. Define Q ⊗̈ Q′ as
  > the Cartesian product Q × Q′ with weight wt(x ⊗̈ x′) = wt(x) + wt(x′)
  > and Kashiwara operators given by a case split:
  > (1) if ϕ̈_i(x) > 0 and ε̈_i(x′) > 0, set ë_i(x ⊗̈ x′) = f̈_i(x ⊗̈ x′) = ⊥
  >     and ε̈_i(x ⊗̈ x′) = ϕ̈_i(x ⊗̈ x′) = +∞;
  > (2) otherwise, apply the standard tensor-product signature rule
  >     (ë_i acts on the left when ϕ̈_i(x) ≥ ε̈_i(x′), on the right otherwise;
  >     f̈_i dually) with
  >       ε̈_i(x ⊗̈ x′) = max{ε̈_i(x), ε̈_i(x′) − ⟨wt(x), α_i∨⟩},
  >       ϕ̈_i(x ⊗̈ x′) = max{ϕ̈_i(x) + ⟨wt(x′), α_i∨⟩, ϕ̈_i(x′)}.
  > Then Q ⊗̈ Q′ is a seminormal quasi-crystal of type Φ.

- **Proof:** direct case analysis on ε̈, ϕ̈. Six-page unfolding, no representation
  theory used — purely combinatorial.

### Paper B: arXiv:2309.14898  (Rick's more probable target)

- **Authors:** Alan J. Cain, António Malheiro, Fátima Rodrigues, Inês Rodrigues
- **Title:** A local characterization of quasi-crystal graphs
- **Submitted:** 2023-09-26
- **Main relevant theorem (Theorem 3.13, verbatim):**
  > Let Q and Q′ be seminormal quasi-crystal graphs satisfying the local
  > quasi-crystal axioms of Definition 3.2 (i.e. LQ1, LQ2, LQ3, LQ3′). Then
  > Q ⊗̈ Q′ satisfies the same axioms.

- **Local axioms in one line:**
  - LQ1: ε̈_i(x) = 0 ⇔ ϕ̈_{i+1}(x) = 0
  - LQ2: three "propagation" conditions on ε̈, ϕ̈ under an i-edge (a
    quasi-crystal analogue of Stembridge S2)
  - LQ3, LQ3′: for i ≠ j, if both ë_i(x) and ë_j(x) are defined then
    ë_i ë_j(x) = ë_j ë_i(x) ≠ ⊥ (and dually for f̈)

- **Companion result (Theorem 4.9):** Given a connected Stembridge crystal C
  of type A_{n−1}, an explicit construction defines a quasi-crystal Q_C on the
  same underlying set (loops added where ε̃_i(x) < wt_{i+1}(x)); Q_C
  is seminormal and satisfies the local axioms.

- **Character statement (proof of Corollary 4.10):**
  > "The character of C is the Schur function s_λ … the character of a
  > quasi-crystal connected component is a fundamental quasi-symmetric
  > function F_α, taking the characters of Q_C, one obtains a decomposition
  > s_λ = Σ_{T ∈ SYT(λ)} F_{DesComp(T)}."

  This is the paper's only decategorification statement.

---

## Does the proof use the GL_n branching axiom (arXiv 2503.14782 §5.1)?

**No.** Explicitly checked both papers via full-text search. Neither paper
mentions:
- "Brauner", "Corteel", "Daugherty" — nobody from the crystal-skeleton line
- "branching" — not in the technical sense
- "coproduct", "Hopf" (except the Drinfeld reference in the bibliography)
- "skeleton" — the crystal-skeleton concept is entirely absent

The Cain quasi-tensor product proof is a pure signature-rule case analysis. It
never leaves the combinatorial layer of the graph.

Similarly, no Sym-coproduct / Δ(s_λ) machinery is invoked. Paper B's
character result is one-way (quasi-crystal-component character ↦
fundamental QSym) with no coproduct compatibility.

---

## Does "quasicrystal" here mean the same as Sk(-) in Rick's Path 4?

**No — and this is the crux.** Two different objects share a similar name.

**Cain quasi-crystal (Q):** an edge-coloured graph with vertex set generically
the same size as the underlying crystal, plus loops. Kashiwara operators ë_i,
f̈_i are the crystal operators only when a "descent condition"
ε̃_i(x) = wt_{i+1}(x) holds; otherwise ë_i = ⊥ and ε̈_i = +∞ (loop).
Connected components correspond to **fundamental quasi-symmetric functions
F_α (Gessel basis)**. This is Krob–Thibon / Cain–Malheiro's hypoplactic setup.

**Brauner et al. crystal skeleton (Sk / QCS):** a **strictly smaller** object,
one vertex per "atom" of the crystal. Character of a QCS component is a
**Young quasisymmetric Schur function YQS_α** (Haglund–Luoto–Mason–van
Willigenburg basis), not a fundamental Gessel F_α.

These are related but not the same. QCS_α ≠ Cain's Q_C-component in general;
the QCS collapses further along the atom structure. The fundamental-QSym /
YQS-Schur distinction is exactly the distinction between the two.

So: the tensor product closure at the **Cain quasi-crystal** level is a
different theorem from the tensor product closure at the **Brauner skeleton**
level. Cain's proof is not directly liftable — it lives in a different graph.

---

## Can the proof structure lift to the skeleton level?

**Very partially, and not for the reason Rick was hoping.**

- **What lifts:** the case-split *shape* of the argument. Both Cain's Q ⊗̈ Q′
  and the desired Sk(B_1 ⊗ B_2) reduce to checking local axioms after
  identifying the vertex set with a Cartesian product. The scaffolding of
  "define operators, verify axioms case by case" is transferable.

- **What doesn't lift:** the *signature-rule formula*. Cain's quasi-tensor
  product uses fresh ε̈, ϕ̈ formulas involving max and +∞. The Brauner skeleton
  has its own atom-comparison rule; there is no reason the Cain rule matches
  the skeleton coproduct □ that Rick wants (which is meant to be the Sym
  coproduct Δ(s_λ) = Σ c^λ_{μν} s_μ ⊗ s_ν pulled back through the character
  map).

- **What is missing entirely:** the GL_n-branching / Hopf / Sym-coproduct
  ingredient. Cain's proof does not need it, so it cannot serve as a template
  for how to use it. Rick's L3 lemma (branching axiom = Sym coproduct shadow)
  will need a different source — probably worked out from Brauner et al.
  2503.14782 §5.1 directly, or from He–Tubbenhauer 2606.02249.

---

## Verdict for Path 4

**MEDIUM template value on structure, LOW on content.** The Cain 2309.14898
paper is a decent structural analogue: "local axioms + a tensor product;
prove closure by case analysis on ε̈, ϕ̈". Rick can borrow the *architecture*
of the proof of Theorem 3.13.

But it does not solve the load-bearing step. The reason the skeleton
coproduct □ is hard is that □ must match Δ on Sym under characters — a Hopf
constraint. Cain's quasi-tensor product satisfies no such constraint (the F_α
basis is not primitive under the Sym coproduct), so his proof does not model
that constraint.

**Rick should not cite Cain et al. as a template for lemma L3.** L3 remains
untouched.

**Rick can cite Cain et al. in §7 as prior art:** "Analogous tensor-product
closure theorems have been proved at the quasi-crystal / hypoplactic level by
Cain, Guilherme, and Malheiro (2301.00271) and Cain, Malheiro, Rodrigues,
Rodrigues (2309.14898); those results live over the fundamental-QSym basis
rather than the YQS basis natural to the Brauner skeleton, so do not imply
our main theorem."

---

## Concrete next steps

1. **Do not lift the Cain proof.** Move on. The GL_n branching / Sym coproduct
   piece needs a fresh derivation from 2503.14782 §5.1.

2. **Add Cain 2309.14898 to the Path 4 bibliography under "prior art on
   related closure theorems".** Two-line mention in §7.

3. **Cross-check L4 (rigidity)** against Cain 2309.14898 Theorem 3.8:
   "connected components of seminormal quasi-crystal graphs satisfying the
   axioms are isomorphic iff they have the same highest weight." This is a
   rigidity statement in Cain's category and *might* have a Sk analogue Rick
   can port. **Worth a follow-up read of Cain's §3.2 for the proof technique.**

4. **File in the Path 4 novelty audit:** confirm Cain et al. have no Sym
   coproduct compatibility claim. This strengthens the "gap is genuinely
   there" argument.

---

## Files fetched

- `/home/agent/papers/cain-2309.14898-local-characterization-quasicrystal.pdf`
- `/home/agent/papers/cain-2301.00271-quasicrystals-root-systems.pdf`
- text extracts at `/home/agent/papers/cain-2309.14898.txt` and
  `/home/agent/papers/cain-2301.00271.txt`

## Notes on the search

Semantic Scholar rate-limited (429), arXiv MCP endpoint broken (301
redirects, tool doesn't follow). Fell back to WebSearch + WebFetch of arXiv
abs pages. Downloaded both PDFs via `mcp__research__download_pdf` which
does work. The two other candidate papers evaluated and set aside:

- arXiv:2311.08523 (Guilherme, *From plactic monoids to hypoplactic monoids*,
  2023-11-14) — a follow-up on when a plactic quasi-crystal monoid gives a
  hypoplactic one; not a closure theorem in the required sense.
- arXiv:2309.14887 (Cain, Malheiro, F. Rodrigues, I. Rodrigues, *Structure of
  quasi-crystal graphs and applications to the combinatorics of
  quasi-symmetric functions*, 2023-09-26 v1; v2 2025-08-05) — answers two
  Maas-Gariépy conjectures on F_α/s_λ interaction, not the closure paper.

Not a fabricated citation risk: all four arXiv IDs verified via WebFetch of
the abs page and PDF download.
