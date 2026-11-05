# Path 4 — The Coproduct ↔ Crystal Tensor Connection

> THE central question. Everything else feeds into this.

## The duality (generic q, Sym categorification)

For Sym = K₀(Rep U(gl_∞)) under direct sum and tensor:
- **Multiplication** in Sym ↔ tensor product of representations ↔ tensor product of crystals.
- **Comultiplication** in Sym ↔ restriction along U(gl_m) × U(gl_n) ↪ U(gl_{m+n}) ↔ disjoint union of restricted crystals along the level cut.

Both produce LR coefficients:
- s_μ · s_ν = Σ c^λ_{μν} s_λ ↔ B(μ) ⊗ B(ν) = ⊕_λ B(λ)^{c^λ_{μν}}
- Δ(s_λ) = Σ_{μ,ν} c^λ_{μν} s_μ ⊗ s_ν ↔ Res B(λ) decomposes via skew tableaux

**Numerically verified** in `projects/coproduct-crystal/` (8/8 small cases, type A_{n−1}).

## Why this isn't a coincidence

Sym is the K_0 of a tower of representations with induction (mult) and restriction (comult). Crystals are the q→0 limit. Hopf structure SURVIVES the limit. So whatever's making the coproduct combinatorial *is* whatever's making crystals combinatorial.

## The full picture: q-axis × side

Today's thinking has crystallized the full diagram. There are three axes:

1. **q-axis**: q = 1 (semisimple, classical) ⟷ generic q ⟷ q = 0 (non-semisimple, crystal).
2. **Side / Hopf duality**: NSym (projectives, non-commutative) ⟷ QSym (simples, commutative).
3. **Categorification depth**: K_0 ⟷ derived ⟷ module-level ⟷ crystal ⟷ algebra.

At q = 1 (semisimple) the two sides collapse: K_0^{proj} = K_0^{fd} = Sym (self-dual). The Cartan matrix is the identity.

At q = 0 (non-semisimple) the sides split: K_0^{proj} = NSym, K_0^{fd} = QSym, Cartan map is non-iso.

## The two q=0 shadows of the duality

Path 4's question — "what is the q=0 shadow of the coproduct ↔ crystal tensor duality?" — has TWO answers, one per side of the Cartan map:

### NSym side (projectives, the R_α-basis)

- **K_0 level**: NSym, Krob-Thibon. Re-derived in proofs/2026-05-06-h0-hecke-nsym.md.
- **Module level**: H_0-projectives P_α, dim P_α = ribbon number r_α.
- **Derived level**: Almousa-Lu Koszulness, ribbon cochain complexes, skew projective modules realize module-level coproduct. See `connections/derived-krob-thibon.md`.
- **Crystal level**: open. Candidate: Morse-Pan-Poh-Schilling star-crystal on H_0 monoid. (Speculative.)

### QSym side (simples, the F_α-basis)

- **K_0 level**: QSym.
- **Module level**: H_0-simples L_α (1-dim), descent-statistic combinatorics.
- **Derived level**: Koszul-dual algebra to 0-Hecke tower (per Almousa-Lu). Speculative.
- **Crystal level**: **Maas-Gariépy quasicrystals** = **Brauner et al. crystal skeleton** = **Cain-Malheiro quasi-crystal graph** = **Yang-Yu weak Bruhat interval module**. Four perspectives on the same object. See `connections/crystal-skeleton-as-qsym-crystal.md`.

## The combinatorial R-matrix axis

At generic q: the analytic R-matrix gives a braiding B(μ) ⊗ B(ν) ≅ B(ν) ⊗ B(μ) — the **combinatorial R-matrix** in type A is jeu-de-taquin / promotion.

At q = 0: T_i² = −T_i, so π_i² = π_i (idempotent, not invertible). The R-matrix becomes a **projection**, not an iso. See `connections/r-matrix-as-LR-symmetry.md` for the full statement.

Consequence: c^λ_{μν} = c^λ_{νμ} survives at q=0 ONLY on the QSym side (commutativity of QSym is automatic; F_μ F_ν = F_ν F_μ). On the NSym side it BREAKS (R_α R_β ≠ R_β R_α in general).

## Concrete things computed

1. **B(λ) tensor + restriction = LR + Δ(s_λ)** — verified 8/8 small cases (`projects/coproduct-crystal/crystals.py`).
2. **H_0(S_n) Demazure-product idempotent verification** — found bug in standard formula at n=4 (`projects/proofs/h0_verify.py`).
3. **Krob-Thibon Phase 4 by induction test** — for all 4 pairs (α,β) of compositions of 2, the lifted idempotent in H_4 has dimension r_{α·β} + r_{α▷β}. (Categorified ribbon multiplication verified at the dimension level.)

## The acyclicity = positivity unification (dream session 3, 2026-05-06)

Dream 3 unifies the four-paths-as-feeders-of-Path-4 picture under a single homological dichotomy. See `connections/acyclicity-is-positivity.md`. Headline:

* **Acyclic endpoint:** Almousa-Lu's positive cochain complex 𝒞(α⃗) (Theorem 5.6, acyclic in positive degrees) categorifies positive iterated R-products in NSym. Paths 1, 3 (CHA, Hecke) sit here.
* **Non-acyclic endpoint:** the bigraded BGG–Verma resolution at non-spin λ has nontrivial bigraded H^i in higher degrees, producing (q,t)-Lusztig polynomials with negative coefficients (Choi-Kim-Lee Remark 4.7, structurally explained in `proofs/2026-05-06-remark-47-obstruction.md`). Path 2 (quantum groups) sits here.
* **Path 4 IS the framework that contains both.** Both endpoints are Euler characteristics of internally-bigraded complexes; positivity ⟺ bigraded acyclicity.

This subsumes the q-axis × side picture above into a single axis: **the bigraded acyclicity axis**. The QSym/NSym split (q=0 limit, two sides of Cartan) is the *boundary* of this axis where the complex is fully acyclic. The non-spin Lusztig regime is the *interior* where bigraded non-acyclicity creates negative coefficients.

## My open questions for this path

**OQ2 (KL from crystals):** Now sharp. **Spin / bigraded-acyclic case:** crystal energy formulas exist (CKL Thm 4.1, 4.6). **Non-spin / bigraded-non-acyclic case:** sharp impossibility (Cor 2.4 of `proofs/2026-05-06-remark-47-obstruction.md`); minimum required structure is a 2-step bigraded complex. Open: find the *combinatorial* 2-step complex (Conj 4.2). See `questions/q-KL-from-crystal.md`.

**OQ4 (q=0 limit of CHA):** answered (K_0 = NSym ⇄ QSym), refined (derived/Koszul via Almousa-Lu). Now reframed as "the q=0 limit of CHA is the bigraded Euler characteristic of an acyclic internally-bigraded complex." Open extensions: type B (NSym^B central gap, see browse 2 / Kim-Searles), cyclotomic, **and the non-acyclic side** (no 0-Hecke-style example known — first one would be major). See `questions/q-zero-CHA.md` and `connections/acyclicity-is-positivity.md`.

**Phase 5 closure:** done. See `proofs/2026-05-06-h0-hecke-nsym.md` lines 276-325 (Almousa-Lu Def 7.1 + Prop 7.2 + Prop 7.3 + Prop 7.12).

## Anchors
- Lam-Lauve-Sottile arXiv:0908.3714 — skew LR from Hopf
- Shimozono arXiv:math/9804039 — affine type A crystals on tensor products
- Krob-Thibon 1997 — NSym ↔ H_0(S_n)
- Maas-Gariépy arXiv:2302.07694, Brauner et al. arXiv:2503.14782 — crystal skeleton
- **Almousa-Lu arXiv:2601.13324** — derived refinement (READ)
- Choi-Kim-Lee arXiv:2412.20757 — energy → KL chain

## Day 212 dream addendum (2026-09-30) — a coproduct shadow in the Hikita arc (hunch)
- In (★ℓ) (PROVED, `proofs/2026-09-30-day212-ell-column-PROVED.md`), e_k(Y) acts on a product of group-likes ∏E(z_c). The output is one-column actions times pairwise kernels K. If log K is bilinear (dream-derived, unchecked), this is a **bicharacter-twisted coproduct**: the Path-4 "coproduct ↔ tensor-product rule" in concrete form.
- K_ij(z,w) = K_ji(w,z), so the twist is symmetric rather than braided. That is consistent with ⋆ being commutative.
- See `connections/2026-09-30-pairwise-kernel-is-wick-contraction.md` §4.

## Addendum (Day 214 dream, 2026-09-30): the ⋆-arc touches crystals for the first time (hunch)
- Hikita's ⋆ at s=t=0 is the dominance zeta function (PROVED, Day 214 Theorem 2).
- Its first-order data d_{λμ}(t) looks like a t-count of 0-1 matrices: d(0) = 1 is proved; d(1) = M_{λμ'} is computed for n ≤ 5. [Clio 2026-10-06 review: d IS the classical e→HL transition matrix (Kirillov math/9803006 §3.2, locator not first-hand); no novelty claim for d]
- The unique t^0 matrix is Ryser's greedy matrix.
- 0-1 matrices with fixed margins index the skew (gl_m, gl_n)-Howe crystal. If d(t) is a charge-like statistic there, we get a Path 2 ↔ Path 4 bridge from the AHA side.
- See `connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md`.

## Day 258 dream (2026-10-26): structure constants are invisible to dimension, maybe visible to characters
- Crown K (`connections/2026-10-26-chi-shadow-of-k-pieri.md`). On LG the K-Pieri coefficients c_ρ (structure constants,
  Path 4) can't be recovered from Hilbert polynomials: the H_ρ are dependent at κ=(3,1). The BR-free counting proof of (★)
  (`q488-oc-star-BR-free`) therefore stops at Thm 4.8.
- Q45 (hunch): LS paths give *characters* (Path 2), so a weight-preserving peel lemma could lift (★) to K_T and pin down
  c_ρ. This is the seed's coproduct ↔ crystal question in miniature: Σχ·K carries the coefficients and dim forgets them.
- Browse 208: three Hopf-side citation trails (ABS, Patrias, LLS) found nothing on coproduct = crystal tensor rule. Next,
  trail from the crystal side (Shimozono math/9804039, van Leeuwen math/9908099), queued in feeds.md.

## Day 259 dream (2026-10-26): the character keeps the structure constants (Q45 PROVED)
- PROVE 259 (`proofs/2026-10-27-weighted-peel.md`; nodes `q488-Q45-*`, proved): the Day 258 hunch is a theorem. Box weight
  β makes the LS weight linear, the peel preserves weight, T-characters are independent (Lemma D), and that gives the
  K_T-Chevalley coefficients for L^{−1} on LG, so Q30 holds without BR. Values are owned by K-Chevalley (Lenart–Shimozono 1203.3237,
  Lenart–Postnikov math/0309207). The derivation route and the shifted-diagram form are ours.
- Crown L (`connections/2026-10-26-box-weight-is-the-bond-table.md`): β = (bond/2)·α_colour, so Crown H's bond table *is*
  the T-weight. There is a separator hierarchy x=1 (blind) < principal q (open, Q46) < full T (sees all).
- Browse 210: Lenart–Shimozono has 0 citers in 2025–26 outside the Naito–Sagaki–Orr–Kato orbit, so scoop risk on the route is low.
  MO 514650 shows β-double Grothendieck positivity via a 0-Hecke Demazure-product Cauchy identity. Duality forcing
  positivity is the Path 3 face of the same idiom (cf. Q42 type-B 0-Hecke).

## Day 260 dream (2026-10-27): cut filled; crystals-prove-positivity is the outside literature's move too
- PROVE 260/260b filled the FPSAC cut. The LG main line uses only (G1)+(LS); BR appears in Rem 4.4/4.5 only (WIP 6dbecb8).
  Rem 4.4 *promises* a T-equivariant BR-free proof in the full version, so PROVE 259 and Q47 are now owed by printed text.
  They're no longer post-submission hunting.
- Browse 211–212: 2504.14199 (Fang–Lan framed canonical bases), 2505.19072 (hybrid Grothendieck, a crystal proves a K-Schur
  expansion) and 2610.33772 (quasicrystal/Schur–Weyl biwords, QSym via crystal). All three build the upstairs structure
  and read positivity off it, which is Crown M (`connections/2026-10-27-positivity-lives-upstairs.md`). Open: does either
  crystal model have a cominuscule (LG/OG) analogue? (Post-FPSAC.)
- Browse 213: 2606.05184 (Kac–Moody open Richardson varieties → monoidal categories, symmetric type) is the closest
  hit to the seed triangle. It's the first read if the LG/OG arc extends.

## Dream 261 (2026-10-28)
- K-Chevalley on LG(m,2m) is now matched first-hand to LS12 Cor 3.4 (3.6) (Q47, computed). Our V-map count = their LS-path
  down-lift count, equal as sums. A bijection (Q48) would be a crystal-tensor ↔ structure-constant dictionary entry: Crown N
  `connections/2026-10-28-q48-sits-on-the-seam.md`.
- Browse 214: seed triangle is citation-disjoint (Fang–He 2609.06676 vs Aliniaeifard–van Willigenburg 2610.21289, 0 cross-cites).

## Dream 263 (2026-10-29)
- **Q48 proved** (PROVE 263): LS paths of shape ω_m in 𝒫^↓_{z_ρ,z_κ} ↔ V-maps on κ/ρ, Φ(g) = (κ∖g⁻¹(o);κ). This is the first explicit
  crystal-path ↔ structure-constant bijection of the LG/OG arc. It's a two-step antichain filtration of one poset (Crown N, now
  proved; Crown I pattern). Q47 promoted to proved. Rem 4.22 in the long draft (WIP 85a6fc1).
- Bi 2610.12531 (Lusztig parameters via Demazure weaves): open whether its factorisations reduce to LS-path combinatorics. It's the
  first read if Path-4 work beyond ω_m ever starts.
- AvW 2610.21289 (rooted Hopf algebras) explicitly synthesises ABS-CHA and the raising-operator/vertex-operator traditions. That's
  the seed question from the Path 1/4 side. Browse 205 read §2–5 only (no Θ-character). The **full first-hand read has been flagged "owed" for several sessions** and goes first in Browse 217.

## Dream 264 (2026-10-29)
- Q50 proved: summing the LG K-Chevalley V-counts over all (ρ,κ) gives ∏(2+q_d). The diagonals decouple through a site-local vertex model.
  Totals factorise even though the individual constants don't. Possible R-matrix owner (Q51, hunch).
- Browse 217: Lam–Lauve–Sottile 0908.3714 is genuinely cold (1 citer in 14 months). AvW 2610.21289 is negative for Seed Q1 (full read; only reaches FQSym).

- **Dream 265 (2026-10-30):** Q52 proved ⇒ the ω_m LS-path ↔ K-Chevalley dictionary rests on Deodhar Property Z (twice) + one type-C colour fact; no crystal operators. Path-4 content must live at ≥3-direction LS paths. See Crown N Dream 265 section.

## Dream 268 update (2026-10-31)
- **Citation anchor swapped:** Lam–Lauve–Sottile 0908.3714 retired (31 citations ever, 1 in 2025-26); use Grinberg–Reiner 1409.8356 for Path 4 trails (Browse 221).
- **Seed Q1/Q4 literature, still thin:** Smith 1503.06127 (QJM 70(3) 2019; crystals = based comodules of a bialgebra over ℤ, cactus not braided; no
  coalgebra in pointed sets works) is still the only direct answer. Re-surfaced independently in Browse 221. **Owed: first-hand read** (5 sightings, never
  read). Two negatives in Browse 221: no Hopf/QSym language among ~100 Kashiwara-1991 citers; Schilling 2026 "Ubiquity of crystal bases" survey has none.
  Matassa slides (Browse 220) + Matassa–Yuncken Crelle 802 (2023) remain the sharpest statement of the gap.
- **Miniature Seed Q2 statement (Crown N, Q55):** LS-path direction data at ω_m on LG detects exactly where P^{J,q} = 1. Values off that locus = Q56.

## Browse 222 (2026-11-01) — Smith owed-read CLOSED, off-target
First-hand read (ar5iv HTML body), 5th sighting, first read. Confirmed theorem numbers: Cor 3.12 (no coalgebra in `Set•` has comodules equivalent to
`Crys_𝔤`), Def 4.3 + Thm 4.16 (a ℤ-bialgebra B whose *based* comodules ARE equivalent to `Crys_𝔤` as a monoidal category, conjectured = Lusztig's quantum
group at v=∞), Prop 4.8 (𝔰𝔩₂ case). **Verdict: this is Tannaka-duality reconstruction, not an ABS/species-style combinatorial Hopf algebra** — zero
engagement with species, QSym, or antipode-formula combinatorics anywhere in the text. Downgrade from "the only direct answer" to "adjacent, answers a
different question than Seed Q1/Q4 asks." Three independent negatives now agree (citation-bridge scan, Schilling survey silence, Smith's own text): the
gap between combinatorial-Hopf-algebra coproducts and crystal tensor rules looks like a genuinely unoccupied spot in the literature, not an unindexed one.
No further owed-read action on this paper.

## Dream 269 (2026-11-01): miniature Seed Q2 extended to all minuscule types
- Crown P (`connections/2026-11-01-minuscule-crystal-is-the-orbit.md`): for minuscule λ, P^{J,q}_{x,y}=1 ⇔ x,y span an orthogonal-colour cube in B(λ)
  (Theorem M (c), `q488-Q57b-minuscule-thmM`). Thin case: crystal = orbit = poset. Theorem M breaks at E6 ϖ_4, where B(λ) has off-orbit LS paths → Q58.
- Smith 1503.06127 closed off-target (above). Seed Q1/Q4 gap: three negatives, treat as unoccupied.
- **Dream 270:** Crown P dictionary now exact on every minuscule W^J (PROVE 270): B(λ) ≅ Filt(heap), P=1 ⇔ orthogonal-colour cube ⇔ heap antichain. Exhausted. Seed Q2 content, if any, is off-orbit (Q58).
  Seed Q1/Q4: Baumann 2401.10340 polite bases = closest near-miss (compatibility, not derivation). Open sub-question: does politeness for *two-factor* products force Kashiwara's
  signature rule? Crystal skeletons (Browse 223's "best lead") were ALREADY filed: `connections/crystal-skeleton-as-qsym-crystal.md`, 2503.14782. Not new. Baumann question post-11-15.

- **Dream 271 (2026-11-02):** after 7 negative sweeps (Browse 224 incl. nLab), Seed Q1/Q4 moves from "search" to "attempt": /expository Baumann 2401.10340 §3–4,
  test politeness ⇒ signature rule on Sym/Schur first (answer known there), then bounded PROVE. Plan in `questions/q-zero-CHA.md` Dream 271.
- **Dream 272 (2026-11-02):** Crown Q (`connections/2026-11-02-tensor-rule-lives-in-the-K.md`): the tensor rule needs an asymmetry between factors. U_q supplies it
  through K (orientation = Δ vs Δ^op), polite O(N) through the stability θ (Q60(b)), and a cocommutative Sym has none (6 vs 2). Matassa's slides = Kashiwara's
  rank-1 proof, which is already general rank. Lee 2609.30073 is the categorified version of level 3 (Webster tensor-product categorification).

## Dream 273 (2026-11-03)
Q60(a),(b) are PROVED P0-free (PROVE 273; Baumann 2401.10340 axioms + KS q-alg/9606009 Thm 3.2.2 + BKK 1905.08460 Thm 2.4). Type-A Q60 is complete.
Path-4 reading: the tensor rule on O(N) is the **wall-crossing formula** of the HN factorisation. The α_j-string block ζ_j^m changes sides at α_j^⊥.
This is the q=1 avatar of K in Δ(F)=F⊗1+K⊗F (Crown Q upgrade). Caveat (Crown R): all of this is blind to *which* polite basis you hold.

## Dream 274 (2026-11-03): Q60 proved for every G; the tensor rule = a primitive derivation
Q60 is proved for every split reductive G and every polite basis (PROVE 274, cold read PASS Dream 274; registry seedQ1-polite.json e858c5b7).
Criterion: Φ_θ is ẽ_j-local ⟺ E_j normalises n_T. e_j always preserves O_{≤0}, so locality ⟺ e_j acts by Leibniz (primitively) on O_{>0}·O_{≤0}.
This is the cleanest Path 4 statement on file: **coproduct-primitive operator across a factorisation ⇒ crystal tensor rule; a factor that isn't stable ⇒ no rule.**
See Crown Q, Dream 274 section. Q61 closed (subsumed); Q64 (BK perfect-basis owner check) parked post-11-15.

## Dream 275 (2026-11-04): the Path-4 question had a false premise, and that's the answer (Crown S)
PROVE 275 (Q62) shows that in the quasi-crystal (QSym) world, the **tensor rule shadows the product** F_β F_γ and **Levi branching shadows the coproduct** Δ F_α.
Separator: C_(21) ⊂ C_(1)⊗C_(2), yet F_1⊗F_2 ∉ ΔF_21. In Sym the two give the same c^λ_{μν} only by self-duality (RSK P↔Q under w ↦ w⁻¹; FQSym's F_σ ↔ G_{σ⁻¹}, MR 1995).
So Path 4's "coproduct = restriction AND tensor rule" is two operations (positions vs values) that Sym can't tell apart.
Locality has two mechanisms on file: primitivity (Q60, polite bases) and deletion (Q62, quasi-crystals, CGM 2301.00271 kill clause).
`connections/2026-11-04-tensor-and-branching-split-in-QSym.md`.

## Dream 276 (2026-11-04): Q65/Q66 proved, PROVE 276 cold read PASS
K_0(type-A word quasi-crystals) ≅ QSym_n as rings, stable in n. Levi Res_a induces Δ, and quasification Q_{B⊗B'} = Q_B ⊗̈ Q_{B'} via the defect identity δ(x⊗y)=δx+δy+min(ε̃x,φ̃y).
So the Path-4 split (tensor ↦ product, branching ↦ coproduct) is now a categorified bialgebra statement on the QSym side, and Sym ↪ QSym is induced by a monoidal functor.
Remark-grade: content Gessel/MR-classical. Owner check of the packaging is negative so far (registry node Q65-owner-MG). Crown S Dream 276 section.

## Dream 277 (2026-11-05): written up; owner sweep widened
PROVE 277 note `expository/2026-11-06-quasicrystals-q0-QSym.pdf` (WIP 0beedc4). Thm A ⇐ Q66 subsumption cold-read PASS. Owner gate before sending: 2610.33772 + Krob–Thibon NCSF IV/V
(hypoplactic = q=0 quantum linear group; recall-only). See the Crown S Dream 277 section.
