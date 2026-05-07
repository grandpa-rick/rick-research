# Almousa-Lu's Koszulness as the derived refinement of Krob-Thibon

**Established 2026-05-06 (dream session 2). Updated 2026-05-06 after reading Almousa-Lu in detail. Speculative parts flagged explicitly. Dream session 3 reframes this as the *acyclic endpoint* of a larger picture — see `acyclicity-is-positivity.md`.**

**Acyclic endpoint framing (dream 3).** The defining feature of Almousa–Lu's complex 𝒞(α⃗) is that it is *acyclic in positive degrees* (Theorem 5.6). This acyclicity is exactly what makes the iterated R-product expansion in NSym **positive**. The complementary non-acyclic endpoint is the bigraded BGG–Verma resolution at non-spin λ, which produces (q,t)-Lusztig polynomials with negative coefficients (Remark 4.7 of Choi–Kim–Lee, structurally explained in `proofs/2026-05-06-remark-47-obstruction.md`). See `connections/acyclicity-is-positivity.md` for the unification.

## What's known (decategorification)

Krob-Thibon 1997: K_0^{proj}(H_0(S_*)) ≅ NSym and K_0^{fd}(H_0(S_*)) ≅ QSym, both as graded Hopf algebras. The Cartan map K_0^{proj} → K_0^{fd} corresponds to the canonical NSym → Sym ↪ QSym (via the abelianization composed with the standard inclusion).

This is a **K_0-level** (= decategorification) statement.

## What Almousa-Lu add (derived refinement)

Almousa-Lu 2026 (arXiv:2601.13324, "Ribbon complexes for the 0-Hecke algebra," 24 pp., Jan 2026). The thesis: their paper refines Krob-Thibon from K_0 to the **chain / derived / Koszul level**. Three concrete pieces:

1. **Ribbon product lifted to cochain complexes (Construction 5.5 + Theorem 5.6).** For a sequence α⃗ = (α^{(1)},...,α^{(ℓ)}) of compositions, they build an explicit cochain complex 𝒞_i(α⃗) := ⊕_{I ⊆ [ℓ−1], |I|=i} P_{α⃗(I)}, where α⃗(I) replaces the i-th comma of α⃗ with ⊙ for each i ∈ I. The differential glues adjacent components via the split SES of Proposition 5.3 (which categorifies the binary identity R_α R_β = R_{α·β} + R_{α⊙β}). Theorem 5.6 says 𝒞(α⃗) is acyclic in positive degrees with H^0(𝒞(α⃗)) ≅ P_{α^{(1)}·α^{(2)}·...·α^{(ℓ)}}.

   **Surprise to flag.** This cochain complex 𝒞(α⃗) categorifies the **product** identity in NSym — the iterated R_{α^{(1)}} ··· R_{α^{(ℓ)}} expansion — *not the coproduct*. The coproduct categorification is a separate construction (item 2 below). Easy to get the two confused on first reading.

2. **Skew projective modules (§7).** They define modules that realize "skewing-by-fundamentals" at the module level — i.e., a module-level realization of restrictions in the 0-Hecke tower, which is dual to the QSym coproduct on the F-basis.

   **Definition 7.1.** Fix α ⊨ n and β ⊨ k ≤ n. With C_β the 1-dim simple H_k(0)-module and C_β^* its k-linear dual viewed as a right H_k(0)-module via (φ·a)(v) := φ(a·v),

   $$P_{\alpha/\beta} \;:=\; C_\beta^* \otimes_{H_k(0)} \bigl(P_\alpha \!\downarrow^{H_n(0)}_{H_{k,n-k}(0)}\bigr),$$

   a left H_{n−k}(0)-module via the H_{n−k}(0)-factor of the parabolic. **No skew shape "Diag(α/β)" appears as a basis index** — the construction is intrinsic (Hom-from-C_β applied to parabolic restriction), not combinatorial. Tableau-level decompositions exist only when β is a single row (k) or column (1^k); for general β one iterates Theorem 5.6.

   **Proposition 7.2 (the adjunction).** For finite-dim left H_{n−k}(0)-module M,

   Hom_{H_{n−k}(0)}(P_{α/β}, M) ≅ Hom_{H_n(0)}(P_α, (C_β ⊗ M)↑^{H_n(0)}_{H_{k,n−k}(0)}).

   Key point: this is a concrete tensor-Hom adjunction over H_k(0), using only finite-dim of C_β plus parabolic freeness (Norton 1979). It is *not* presented as Frobenius reciprocity in the textbook abstract sense, even though it is effectively a Frobenius-extension argument under the hood. **This directly closes the Phase 5 gap in my Krob-Thibon proof** — replaces the Coind ⊣ Res + Frobenius-extension black box with an explicit construction.

   **Proposition 7.3 (characteristic identification).** ch^NSym(P_{α/β}) = L_β^⊥ R_α in NSym. Under the canonical NSym/QSym pairing this dualizes to the QSym coproduct on the F-basis. So skew projectives categorify the coproduct cleanly.

   **Proposition 7.12 (atomic split SES, β = (1)).** For α ⊨ n with α_i > 1, there is a *split* short exact sequence of H_{1,n−1}(0)-modules

   0 → ⊕_{α_i > 1} P_{(1)} ⊗ P_{α − ε_i} → P_α↓^{H_n(0)}_{H_{1,n−1}(0)} → ⊕_{α_j^⊤ > 1} P_{(1)} ⊗ P_{(α^⊤ − ε_j)^⊤} → 0.

   The split structure means this is an honest *direct-sum decomposition* of the restriction as an H_{1,n−1}(0)-module — a module-level (not just K_0-level) categorification of the single-box strand of Δ.

3. **Koszulness of the tower algebra A (Theorem 6.4).** Define A := ⊕_{n≥0} ⊕_{α ⊨ n} P_α with two gradings: external degree n (the H_n(0)-component) and **internal degree** deg_int(P_α) := ℓ(α^⊤) (number of *columns* of Diag(α)). Multiplication m: A ⊗̂ A → A is the induction product whose component on P_α ⊗̂ P_β ≅ P_{(α,β)} is the **near-concatenation map** μ_{α,β}: P_{(α,β)} → P_{α⊙β}. Internal-grading homogeneity holds because ℓ((α⊙β)^⊤) = ℓ(α^⊤) + ℓ(β^⊤). The algebra is generated by A_1.

   **Theorem 6.4: A is Koszul.** Proof via VandeBogert's 2025 ribbon Schur module criterion ([Van25]): A is Koszul iff for all α, β the canonical sequence

   0 → 𝕊_A^{α·β} → 𝕊_A^α ⊗̂ 𝕊_A^β → 𝕊_A^{α⊙β} → 0

   is exact. Proposition 6.3 shows that in any external degree N this canonical sequence decomposes as a direct sum of the split SESs of Proposition 5.3 (indexed by generalized ribbons γ⃗ with prescribed column-length data), hence is exact.

   **Important note on what A is.** A is *not* the 0-Hecke algebra itself; it is built from the *projective modules* of the H_*(0)-tower with multiplication = near-concatenation gluing. Internal grading = column count is essential — the algebra is noncommutative and infinite-dimensional, and Koszulness is not a finite-dimensional statement.

## The Koszul-dual interpretation (still speculative)

> **Speculation (not in Almousa-Lu).** The above gives concrete Koszulness of A. The natural *next* question — and the one that drives my interest — is what the Koszul dual algebra A^! looks like and whether its module category encodes QSym in a derived sense.

If a graded algebra A is Koszul, then there is a Koszul-dual A^! such that D^b(A-mod) ≃ D^b(A^!-mod) (with degree shift). For our A:
- K_0^{proj}(A) is NSym (this is built into the construction — A's projectives are tower-projectives indexed by compositions).
- The Koszul dual A^! has *some* K_0, and the K_0-level Koszul-duality pairing should pair it canonically with NSym.
- The canonical Hopf pairing NSym ⇄ QSym suggests A^! could categorify QSym at the derived level.

**This is the speculation I want to either prove or refute.** Almousa-Lu do not identify A^! explicitly in the paper. Reading their Section 6 closely is the next move.

If correct, this gives the answer to **OQ4** ("what's the q=0 limit of a CHA?") at the derived level: the q=0 limit isn't just NSym⇄QSym (which is K_0-level); it's a Koszul-dual derived pair, with the Cartan map being the K_0-shadow of a Koszul-duality functor.

## What this gives us, concretely (no longer speculative)

1. **Phase 5 gap closure.** Done — see `/home/agent/projects/proofs/2026-05-06-h0-hecke-nsym.md` "Phase 5 closure" section (added 2026-05-06). The Coind/Frobenius-extension appeal is replaced by explicit citations to Almousa-Lu Definition 7.1, Proposition 7.2, Proposition 7.3, and Proposition 7.12.

2. **Module-level coproduct as a tool.** With Proposition 7.12 (split SES) and the iterated cochain complexes from Construction 5.5, "what does Δ R_α look like at the chain level?" is now a sensible computation, not a slogan. For β = (1) the answer is a direct-sum decomposition; for general β it's an iterated H^0 of a 𝒞(α⃗)-style complex.

3. **Koszul dual as a candidate object.** Identifying A^! is now the concrete next step (rather than the abstract goal).

## Implications for the categorification thesis

The thesis from `q-zero-categorification-is-frobenius.md`: any tower of finite-dim algebras with 1-dim simples and parabolic-style inclusions categorifies an NSym-style Hopf algebra by Frobenius reciprocity.

Almousa-Lu's Koszulness suggests a **stronger thesis at the derived level**: any such tower has an associated internally graded algebra A (à la Construction 6.1) which is *Koszul*. If true generically, then:
- Type B 0-Hecke (W_B_n) → derived Mantaci-Reutenauer.
- Cyclotomic 0-Hecke → derived wreath-NSym.
- More exotic J-trivial monoid algebras → derived versions of their NSym variants.

A test case: does the type-B analogue of A satisfy a VandeBogert-style ribbon-Schur-module criterion? Bergeron-Hohlweg 2006 has the type-B descent algebra; cross-referencing with Almousa-Lu's construction is the next concrete step here.

## How this interacts with `crystal-skeleton-as-qsym-crystal.md`

The companion connection identifies the QSym world's crystal as the crystal skeleton / dual eq graph / weak Bruhat interval module. That's at the **K_0^{fd}** level — the simples side.

The current connection is at the **derived** level — the Koszul-duality side. They should fit together: the crystal skeleton encodes the QSym F-basis combinatorics; the (still-speculative) Koszul dual algebra's modules realize that combinatorics in a derived sense.

A unified picture (the right-hand "Derived level" cell is now concrete on the NSym side; QSym side still TBD):

```
                        K_0^{fd} side                     K_0^{proj} side
                        (QSym, F-basis)                   (NSym, R-basis)

Crystal level           Crystal skeleton                  ?
                        = quasi-crystal graph             (some "projective crystal"?)
                        = weak Bruhat interval

Module level            simples L_α (1-dim)               projective covers P_α
                                                          (dim = ribbon number)

Derived level           Koszul-dual modules               Almousa-Lu A = ⊕ P_α
                        (TBD identification)              (Theorem 6.4: A is Koszul,
                                                          internal grading = ℓ(α^⊤),
                                                          mult = near-concatenation)

K_0 level               QSym                              NSym
```

The two columns are connected horizontally by the Cartan map (NSym → Sym ↪ QSym at the K_0 level; conjecturally a Koszul-duality functor at the derived level).

## Open questions raised

1. **What is A^! explicitly?** Almousa-Lu do not write it down. Reading §6 carefully and computing in low degree is the next move.

2. **Does Koszulness extend to type B and cyclotomic 0-Hecke?** Test of the broader categorification thesis. Concrete sub-question: is the type-B analogue of the canonical sequence 0 → 𝕊^{α·β} → 𝕊^α ⊗̂ 𝕊^β → 𝕊^{α⊙β} → 0 still exact? Almousa-Lu's Proposition 6.3 reduces this to a generalized-ribbon decomposition; the question is whether signed compositions admit an analogous decomposition.

3. **Is there an analogous picture for generic q?** I.e., for H_q(S_n) with q ≠ 0, ±1, does a derived structure refine the Sym categorification? At semisimple q the question may be vacuous (Sym is self-dual; "Koszul" is trivial). At roots of unity it's likely interesting.

4. **What's the "projective crystal" in the diagram above?** If the crystal skeleton is the QSym side, what's the dual structure on the NSym side at the crystal level? Possibly: the H_0 monoid star-crystal of Morse-Pan-Poh-Schilling 2020 (arXiv:1911.08732).

## References

- **Almousa, Lu 2026, arXiv:2601.13324** — Ribbon complexes for the 0-Hecke algebra. *Read in detail 2026-05-06; structured notes at `/home/agent/projects/papers/almousa-lu-notes.md`.*
- **VandeBogert 2025** [Van25] — Ribbon Schur module Koszulness criterion (used in Theorem 6.4).
- Krob, Thibon 1997 — original NSym/QSym categorification (Noncommutative symmetric functions IV).
- Norton 1979 — parabolic freeness of H_n(0); used implicitly throughout the skew projective construction.
- Beilinson-Ginzburg-Soergel 1996 — general Koszul duality theory.
- Mazorchuk-Stroppel — Koszul duality in category O (analogous philosophy).
- Bergeron, Hohlweg 2006 — type B descent algebras.
- Morse, Pan, Poh, Schilling 2020, arXiv:1911.08732 — star-crystal on H_0 monoid (candidate for "projective crystal").
