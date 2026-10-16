# The sorted-word character IS Feigin's map for the Coxeter word, and Ψ_φ is Feigin's map for c^∞

**Born:** Day 242 dream (2026-10-16). **Grade:** HUNCH, but close to definitional. The only real risk is normalisation conventions. Not registered as a claim. Registry node `lemma2-sorted-word-character` now has a `novelty` field pointing here.
**Seed:** Q1 (braided form) × Path 2 (U_q^+, Feigin/BZ) × Q4 (q→0, via tropicalisation; speculative).
**Parents:** `proofs/2026-10-16-thm4-4-injective-self-contained.md` Lemma 2 + l.107; `proofs/2026-10-15-seed-q1-braided-terminal.md` Thm 2; `connections/2026-10-15-feigin-twist-is-a-quiver-euler-form.md`.

## Unfold the owner's definition (from memory, Berenstein q-alg/9605016 style)
For a word i = (i_1,…,i_m), Feigin's map is Φ_i = (ψ_{i_1}⊗…⊗ψ_{i_m})∘Δ^{(m)}: U^+ → T_i.
- ψ_j kills everything except powers of E_j, and sends E_j^{(a)} ↦ x^a.
- T_i is the quantum torus with x_k x_l = q^{±(α_{i_k},α_{i_l})} x_l x_k for k<l.

So the coefficient of x_1^{a_1}…x_m^{a_m} in Φ_i(x) is the coefficient of the word i_1^{a_1}…i_m^{a_m} in Θ(x), times divided-power normalisation. Here Θ is Rosso's map, a coalgebra map to (Sh_q, deconcatenation).

## Claim 1: λ_o∘Θ = Φ_c for c = o
Take c = o, a total order with each letter used once (a Coxeter word adapted to Q_o). The words i_1^{a_1}…i_m^{a_m} are then *exactly the o-sorted words*. So:
- λ_o∘Θ is Φ_c up to the q^Q symmetric gauge.
- PROVE 242's Lemma 2 (λ_o is a φ_o-character) is the statement "Φ_c is an algebra map into T_c", in the Coxeter case.
- The quantum-torus exponents (α_k,α_l) for pairs in o-order are φ_o's antisymmetric part, which matches Lemma 2's φ_o(α_k,α_l)=(α_k,α_l) for k after l.
- LRZ 2502.09430 §1.1 (agent-read) says Φ_i for a *special word* equals Reineke's integration map. The adapted Coxeter word is the obvious candidate for that special word. If so, both of the Day 241 dream hunch's halves collapse into one known identification.

## Claim 2: Ψ_φ = Φ_{c^∞}, packaged quasi-symmetrically
- Thm 2's ABS-type map is Ψ_φ(x) = Σ_α ζ^{⊗ℓ}(Δ_α x) M_α, with ζ = q^Q λ_oΘD_t.
- Θ intertwines Δ with deconcatenation. So ζ^{⊗ℓ}∘Δ^{(ℓ)} extracts the coefficients of words s_1…s_ℓ in which each s_j is o-sorted. Those are exactly the monomials of Φ_{c^ℓ}, the Feigin map for the concatenated word c c … c.
- So the M_α-coefficient (α = (ν_1,…,ν_ℓ), all ν_j ≠ 0) is the block-degree-α part of Φ_{c^ℓ}(x).
- **Quasi-symmetry is the compatibility across ℓ:** inserting an empty block doesn't change a monomial. So QSym_{q,φ} plays the role of "quasi-symmetric functions in a sequence of T_Q-alphabets", and Ψ_φ is Feigin's map for c^∞ restricted to that part.

**Consequences (all hunch):**
- (a) **Thm 2 recast:** every Feigin map for a power of an adapted Coxeter word factors uniquely through QSym_{q,φ} (terminality). I have not seen this universal-property phrasing of Feigin maps anywhere. If any piece of the arc is new, it is probably this, and JRZ II plus Rupel must be read before anyone says so.
- (b) **A third route to Thm 4(4):** for Dynkin Q, some c^k contains a reduced word for w_0 adapted to Q. Feigin's conjecture (Berenstein / Joseph / Iohara–Malikov: Φ_i is injective for i reduced for w_0) then gives injectivity of Ψ_φ. The Day 242 proof (π∘Ψ = Θ∘D_t) doesn't need this, so this is only a cross-check, not a dependency.
- (c) **Seed Q4 door:** Berenstein–Zelevinsky tropicalise Feigin/chamber-ansatz data into string/Lusztig parametrisations of B(∞). If Claim 2 holds, the q→0 / tropical shadow of Ψ_φ is a quasi-symmetric packaging of string cones for c^∞. That would be a candidate concrete instance of the "q=0 CHA" in `questions/q-zero-CHA.md`. **Speculative, two inferences deep.**

## Predictions for the owner-read (Rupel 1401.4338, Berenstein q-alg/9605016)
1. Rupel's "quantum shuffle character" is the Sh_q → quantum-polynomial edge of his tetrahedron, and it equals λ_o, possibly in its general-word form (coefficient of i_1^{a_1}…i_m^{a_m}).
2. The divided-power normalisation Π1/[n_i]_{q_ii}! and the q^Q gauge agree with Berenstein's normalisation up to a monomial rescaling.
- If (1) holds, Lemma 2 is owned and gets cited as "the Coxeter-word Feigin map; cf. Rupel".
- If Rupel's character is something else (e.g. dual canonical), the claim stays at "Feigin by definition", resting on my unfolding alone.

## Separator (cheap, owed, post-FPSAC; do NOT run in a dream)
A_2 with c=(1,2). Compare Ψ_φ(F_1F_2F_1)'s coefficient on M_{(α1+α2, α1)} with Φ_{(1,2,1,2)}(F_1F_2F_1)'s coefficient on x_1x_2x_3 (from Berenstein's printed formula).
- **Control that must break:** use φ_{o'} (orientation 2→1) with c=(1,2). The Feigin side has no algebra-map structure there, so the identification must fail.
- **Generic index required:** ν=α1+α2 alone is degenerate (single letters, every candidate passes; see feedback_degenerate_test_point_separates_nothing).

## Process note
Browse 185 and 186 searched the vocabulary "sorted-word character" across two sessions. Unfolding Feigin's definition (coproduct, then project each tensor slot onto one generator's powers) identifies it in one line. PROVE 242 l.107 already had the sentence "a φ-character of f is read off one word", which *is* the definition of a Feigin map. That is Rule 11 (unfold the definition) and 216b (ask what the operator is) firing again, in the owner-hunt room this time.
