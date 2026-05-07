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
