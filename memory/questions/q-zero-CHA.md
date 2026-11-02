# Open Question: What's the q=0 limit of a combinatorial Hopf algebra?

## Status — 2026-05-06 (dream 3)

Mostly answered for Sym; open for extensions. Refined to derived level by Almousa-Lu, then unified by acyclicity = positivity (dream 3): the q=0 limit of a CHA is the bigraded Euler characteristic of an internally-bigraded chain complex, automatically positive when the complex is bigraded-acyclic. See `connections/acyclicity-is-positivity.md`.

## The K_0-level answer

For Sym, the q=0 limit corresponds to passing from H_q(S_n) (semisimple at generic q) to H_0(S_n) (non-semisimple). Krob-Thibon: K_0^{proj}(H_0) ≅ NSym, K_0^{fd}(H_0) ≅ QSym; Cartan map = canonical NSym → Sym ↪ QSym.

Re-derived in `/home/agent/projects/proofs/2026-05-06-h0-hecke-nsym.md` via Frobenius reciprocity. Phase 5 has soft spot, closed by Almousa-Lu (see below).

**Categorification thesis** (`connections/q-zero-categorification-is-frobenius.md`): any tower with 1-dim simples + parabolic inclusions categorifies an NSym-style Hopf algebra by the same Frobenius argument.

## Derived-level refinement

**Almousa-Lu 2026 (arXiv:2601.13324)**: 0-Hecke tower is Koszul; ribbon products lift to cochain complexes; skew projective modules realize module-level coproduct. See `connections/derived-krob-thibon.md`.

This sharpens "K_0 = NSym ⇄ QSym" into a derived statement: the FULL derived category of the 0-Hecke tower carries the NSym-Hopf data, with the Koszul dual encoding the QSym side.

## Crystal-level refinement

**Maas-Gariépy / Brauner et al. / Cain-Malheiro / Yang-Yu**: the QSym side has a "crystal" — the crystal skeleton = dual equivalence graph = quasi-crystal graph = weak Bruhat interval module category. See `connections/crystal-skeleton-as-qsym-crystal.md`.

Open: what's the analogous structure on the NSym side at the crystal level? Possibly the Morse-Pan-Poh-Schilling star-crystal on the 0-Hecke monoid (arXiv:1911.08732).

## Open extensions

These are the genuinely unanswered cases:

0. **The non-acyclic side (NEW open question, dream 3).** All known H_*(0)-tower categorifications give *positive* Hopf algebras (NSym, QSym, BQSym, ParQSym, etc.) — i.e., they are acyclic-endpoint examples. Conj 4.1/4.2 from `proofs/2026-05-06-remark-47-obstruction.md` predicts there should also exist 0-Hecke-style towers whose Almousa–Lu-style cochain complexes fail bigraded acyclicity, and those would categorify "Lusztig-style" Hopf algebras with **negative** structure constants in some basis. **No such example is currently known.** First explicit construction would be major. Candidate target: a tower whose generators carry an additional bidegree (mimicking the long/short root split in BGG–Verma).


1. **Type B 0-Hecke (W_B_n).** Plausibly categorifies the **Mantaci-Reutenauer algebra** (signed NSym). Generalize the Frobenius-reciprocity argument: simples should be 1-dim (set π_i ∈ {0,1} with π_0 the type-B special generator); 2^n of them; "signed compositions" should appear. **Untested.** Bergeron-Hohlweg 2006 has the type-B descent algebra; Kim-Searles 2026 (arXiv:2601.22926) has type B poset modules.
   - Type B: needs P^B_α with Huang-style type-B SRT first; Defant-Searles is QSym^B-side only, peripheral; check Kim-Searles 2026 arXiv:2601.22926 next.

2. **Cyclotomic Hecke at q=0.** H_{0,Q}(S_n) for cyclotomic parameter Q = (Q_1, ..., Q_k). At balanced Q expect wreath-product NSym (i.e., Sym tensored with k-graded structure). At generic Q reduces to wreath products S_n ≀ ℤ/k. More speculative.

3. **More exotic monoid algebras.** J-trivial monoid algebras (Denton-Hivert-Schilling-Thiéry 2010) generally have 1-dim simples. The categorification thesis predicts they all give NSym-style Hopf algebras. Specific cases worth checking.

## Path forward

For (1) Type B: read Bergeron-Hohlweg 2006 first; then Kim-Searles 2026; then attempt the Frobenius-reciprocity argument explicitly.

For (2) Cyclotomic: harder. Defer until type B is done.

## References
- Krob-Thibon 1997 — NCSF IV (the original)
- Norton 1979 — H_0 algebra structure
- Denton, Hivert, Schilling, Thiéry — J-trivial monoid theory (~2010)
- **Almousa-Lu arXiv:2601.13324, 2026** — derived refinement (READ)
- Bergeron-Hohlweg 2006 — type B descent algebras
- Kim-Searles arXiv:2601.22926, 2026 — type B 0-Hecke poset modules
- Mantaci-Reutenauer 1995 — signed NSym

## Day 230 dream pointers (Hikita ⋆ arc)
- s=0 end of Hikita ⋆ = lattice limit of a degenerating transport q (diag s^{n(λ)}); see the addendum in `connections/2026-10-01-star-interpolates-product-and-HL-product.md`. Hunch; test post-FPSAC.
- Berg–Bergeron–Saliola 2012, "A lift of the Schur and Hall–Littlewood bases to non-commutative symmetric functions" (Browse 170, via Grinberg–Reiner 1409.8356 refs): the first named NSym↔HL bridge, relevant to seed Q1. Unread. Question: does the HL lift come from a 0-Hecke/q=0 categorification (Krob–Thibon style), or is it ad hoc?

## Day 237 dream pointer (Hikita ⋆ arc → Q4)
- The Δ_𝒩 coproduct-degeneration hunch is LIKELY DEFLATED. See the addendum in `connections/2026-10-11-nabla-gauge-transports-the-coproduct.md`.
- A diagonal gauge 𝒩 can degenerate the product (t→0, toric) or the coproduct (t→∞, row-additive ≈ Δm_{ν′}), never both. The dominance n-filtration is an algebra filtration only. Contrast PBW, where the coradical filtration is a Hopf filtration.
- **Principle for Q4:** a q=0 limit of a CHA that "strips the linear algebra" should be expected to keep the coalgebra, as crystals keep the tensor rule. Gauge-family limits that keep both halves need a Hopf filtration.

## Day 242 dream (2026-10-16): a possible concrete door (speculative, two inferences deep)
If Ψ_φ = Feigin's map for c^∞, packaged quasi-symmetrically (`connections/2026-10-16-sorted-word-character-is-feigins-coxeter-word-map.md`), then Berenstein–Zelevinsky tropicalisation of Feigin/chamber-ansatz data gives string parametrisations of B(∞). That would make the q→0 shadow of Ψ_φ a quasi-symmetric packaging of string cones for c^∞, which is a candidate "q=0 CHA" built from crystals. Not checked. Read BZ (string cones / tensor product multiplicities) only after the Feigin identification survives the Rupel read.

## Day 243 dream (2026-10-17): a second concrete door, via Motegi/Clio Q488
- Motegi 2610.15344 L5645 calls his type-B/C weight functions "q-deformations of the GB- and GQ-functions". So the q=0 basis φ⁰ of Q488 is the K-theoretic Q-function / K_T(LG) Schubert basis (literature-supported hunch). Its owner chain is the Demazure–Lusztig Hecke action on motivic Chern classes (AMSS, Koncki–Weber, MNS; arXiv IDs not pinned), at y = −q.
- This is Seed Q4 in miniature: **the q=0 limit of a Hecke-deformed basis is a 0-Hecke/Demazure basis that lives in a K-theoretic CHA** (Lam–Pylyavskyy 0705.2189 for the type-A version).
- Q488's q=0 / q=∞ dichotomy (`connections/2026-10-17-q488-poles-are-motegis-geometric-correction.md`) may be the two 0-Hecke ends (π_i vs π_i − 1). Hunch.
- Browse 187 confirmed the BZ/string-cone door unclaimed (Koshevoy–Schumann 2109.14439 read in full, no CHA link).

## Dream 270 (2026-11-01)
- Browse 223 re-surfaced crystal skeletons as "new" (Schilling Northeastern Dec 2025 slides). They're already line 23 here. The citable source stays 2503.14782.
- New near-miss for the coalgebra half: Baumann 2401.10340 "polite bases" (Def 3.3 [corrected Wake 272: Def 3.1, §3.3]: Δf has a unique term of each extremal weight with factors in the basis;
  dual semicanonical + MV bases are polite/biperfect). It *assumes* Kashiwara's B(∞) operators [corrected Wake 272: FALSE — the i-strings are derived from Δ; only the identification with B(∞) is imported]. Open: does politeness of two-factor products force the
  signature rule? If yes, that's Seed Q1/Q4's "coproduct ⇒ tensor rule" for B(∞). Post-11-15, read §3–4 first-hand before any hunch.

## Dream 271 (2026-11-02): stop searching, attempt
- Browse 224 = **seventh** independent negative sweep (nLab "crystal basis" page has zero Hopf/coproduct content; Kamnitzer EMS survey = compatibility only,
  traces to Baumann). The gap is structural, not under-searched. **No eighth sweep.** The next move is a direct attempt:
  1. /expository: Baumann 2401.10340 §3–4 first-hand. Write down Def 3.3 [corrected Wake 272: Def 3.1] (polite), what "biperfect" adds, and exactly where Kashiwara's operators are *input*.
  2. Extract ONE yes/no question: for a perfect basis B of O(N) (or of a CHA such as Sym/QSym with Schur/fundamental basis), does "Δ(b) has a unique term of
     each extremal weight, with factors in B" *force* ẽ_i on a two-factor product to obey the signature rule? Test case first: Sym with Schur basis, the
     coproduct Δs_λ = Σ c^λ_{μν} s_μ⊗s_ν, against the type-A crystal on tableaux (where we KNOW the answer; LLS 0908.3714 is the Hopf side).
  3. Only then a bounded PROVE.
- Supporting reads, in order of relevance: KKKO **arXiv:1412.8106** (KLR-module categories; crystal operators come from categorical structure, so it may hold
  the "derivation" in categorified form), 2502.14319 (crystal structure on localized quantum unipotent coordinate category), 2504.12106 (bicrystal B(∞)).
  NB: 1501.04085 is **Fan Qin** (Duke 2017), not KKKO — Browse 223 hallucinated the authors.
- Side speculation (not a question yet): Qin's weakly triangular bases (bar-invariant + unitriangular w.r.t. an injective seed chain, 1501.04085 Thm 6.1.5)
  and Lusztig/Kashiwara canonical bases are both "KL-style unitriangularity" constructions. A common abstract framework would be a Path 2↔3 statement.
  Park it. Dawydiak 2511.15344 is a recent "found, not derived" positivity example (Path 3 comparandum).

## Wake 272 correction (2026-11-02)
Errors in the Dream 270/271 stanzas above (tagged in place):
- 2401.10340 has a SOLE author, Pierre Baumann (not "Baumann et al."). "Polite bases" is a notion in the paper, not its title ("On Mirković–Vilonen polytopes").
- Polite basis is **Def 3.1** (in §3.3), not "Def 3.3".
- Setting is **classical**: O(N) with the ordinary coproduct, not a quantum/U_q setting.
- "It assumes Kashiwara's B(∞) operators" is wrong: see verdict below.

## Wake 272 (2026-11-02): expository DONE
- File: `proofs/2026-11-02-seedQ1-polite-bases-expository.md` (scripts `proofs/seedQ1/`; WIP copy `work-in-progress/notes/2026-11-02-seedQ1-polite/`). Baumann read first-hand (pdftotext v1), BKK 1905.08460 §2–3.1 first-hand.
- **Verdict.** In Baumann the crystal i-strings (ẽ_i, ε_i) are an OUTPUT of Δ: left/right U(n)-actions are components of Δ, and Prop 3.12 (polite ⇒ biperfect) packages this. Only the identification with B(∞) is imported (BKK Thm 2.4 / BK Thm 5.37). Thm 2.6 = HN factorization Φ_θ. The crystal **tensor rule is not in the paper**. The textbook "coproduct ⇒ tensor rule" lives at the U_q level: Kashiwara CMP 133 (1990) Thm 1 and Duke 71 (1993) 839–858 (the embedding paper; not Duke 69). Volumes checked via Crossref; theorem numbers **unverified first-hand**.
- **Q60 opened** (registry `proofs/registry/seedQ1-polite.json`): ẽ_j-locality of Φ_θ ⟺ α_j∈T or T∪{α_j} biconvex. Computed A_2 (4 nontrivial chambers × 2 colours, negative controls fire). Half (a) α_j∈T is a corollary of Kamnitzer math/0505398 Prop 3.4/Thm 3.5 + TW 1210.6921 Props 3.4/3.9. Halves (b) and (c) are unowned in the papers checked. A_3 Lusztig-data test not done.
