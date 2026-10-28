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
