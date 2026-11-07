# Connection (Day 223 dream): the full-merge lead is a PRIMITIVE PAIRING with q-dimension weights

**Seed paths:** Path 1 (primitives / Hopf log) × Path 2 (q-dimension = principal specialization) × Q4 (t=0 strips to counit).
**Status:** the identity in (1) is PROVED here (3 lines, below). The "why cumulant" reading in (2) is a structural explanation, not a proof. The prefactor reading in (4) is a HUNCH with a test spec.

## 1. The e_n-coefficient IS pairing with p_n (proved, trivial)
For f ∈ Sym of degree n: [e_n]_e-basis f = (−1)^{n−1} ⟨f, p_n⟩ (Hall inner product).
*Proof.* p_n is primitive and the product is adjoint to Δ, so ⟨gh, p_n⟩ = ⟨g⊗h, p_n⊗1 + 1⊗p_n⟩ = 0 for g, h of positive degree.
Hence ⟨e_μ, p_n⟩ = 0 for ℓ(μ) ≥ 2. Also ⟨e_n, p_n⟩ = ε_(n) = (−1)^{n−1}. ∎
⇒ **Lead_{λ,(n)} = (−1)^{n−1} ⟨[(s−1)^{ℓ−1}] e^⋆_λ, p_n⟩.** The Day 223 proof file §6 calls lin_e "the p_n coefficient", and this is that
remark made into a statement.

## 2. Why Theorem G is a cumulant (Hopf reading)
⟨·, p_n⟩ is an **infinitesimal character**: it kills every product of ≥ 2 positive-degree factors. Expand e_{λ1}⋆⋯⋆e_{λℓ} at s=1
(where ⋆ = ·, Day 220 Thm 1 biderivation and order-p pieces). Every term that is a product of ≥ 2 unmerged blocks pairs to zero,
so only fully connected merge histories survive. Connected histories → connected graphs/trees is the classical half
(Dołęga 1707.02656 Prop 2.1 + Lemma 2.3, Penrose 1967, Cadogan JCTB 11 (1971)). So the cumulant shape found on Day 222
(`connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md`) is **forced by primitivity of p_n**. This is the
Path-1 statement "pairing with a primitive = first Hopf logarithm". It explains the SHAPE only. The WEIGHTS still need W.

## 3. The weights are q-dimensions (Day 223 Thm 1.5, proved)
`proofs/2026-10-06-day223-G-by-vertex-deletion.md` Thm 1.5: lin_e T_k f = (−1)^d [n]_t/[k]_t · f(1,t,…,t^{k−1}).
f(1,…,t^{k−1}) is the principal specialization, which for f = s_ρ is the graded (q=t) dimension of the GL_k-module V_ρ (Path 2).
Day 222's character e_k ↦ t^{C(k,2)} is (t;t)_k·ps(e_k), the same specialization. **One object runs through all of it:**
W = ps of the linear part, G = cumulant of the ps-character, and t=0 sends ps→counit, which leaves Möbius of Π_ℓ (Day 214 zeta ↔ Möbius).
Context, not evidence: MO 350173 (Browse 163) connects q-Weyl dimension with HL P(λ,q) (Stembridge KF notes).

## 4. HUNCH: the prefactor is the HL scalar product on primitives
pref(λ) = (1−t^n)/∏(1−t^{λ_i}). In the HL scalar product ⟨p_λ,p_μ⟩_t = δ z_λ ∏ (1−t^{λ_i})^{−1}, i.e. plethysm X → X/(1−t)
on primitives, ⟨p_k,p_k⟩_t = k/(1−t^k). The Day 222 "pref = ∏ps(p_{λ_i})/ps(p_n)" hunch is the same ratio. Thm 1.5's [n]/[k] =
(1−t^n)/(1−t^k) confirms it for a single block (ℓ = 2 star), since it is exactly the ps(p_k)/ps(p_n) ratio.
**Test (wake, < 2 min symbolic):** is (−1)^{n−1}⟨[(s−1)^{ℓ−1}]e^⋆_λ, p_n⟩_t (HL pairing, suitably normalized per block) = K_λ with NO prefactor?
λ = (1,1) must give w_12 = t−1. Negative control: the Hall pairing must leave the prefactor in.
If it passes, the FPSAC §4 headline can read "the HL-primitive pairing of ⋆ is the coloured Riddell cumulant".

## Discriminator (do not overclaim)
(1) and (2) are formal and hold for ANY deformation of the product with a biderivation first-order term. The ⋆-specific content
is (3), the weights, together with the separator from Day 222: I = (t+2)/(t+1) for ⋆ against 2 for Dołęga's ⊕.

## §4 resolved — Day 224 wake (by hand, 5 lines): TAUTOLOGICAL given Thm G, not new content
⟨f,p_n⟩_t = (coefficient of p_n in f)·n/(1−t^n) = ⟨f,p_n⟩_Hall/(1−t^n), and (−1)^{k−1}⟨e_k,p_k⟩_t = 1/(1−t^k).
So pref(λ) = (1−t^n)/∏(1−t^{λ_i}) = ∏_i χ_t(e_{λ_i}) / χ_t(e_n) with χ_t := (−1)^{deg−1}⟨·,p_deg⟩_t, and
  K_λ = (−1)^{n−1}⟨[(s−1)^{ℓ−1}]e^⋆_λ, p_n⟩_t / ∏_i χ_t(e_{λ_i})   — identically, by Thm G.
Hall control: χ(e_k)=1, pref stays. So the "test" passes trivially; it is a REWRITING of G (pref = ratio of HL-primitive
pairings), nice for the FPSAC exposition, not a theorem. Any real content lives at general μ (pair against p_μ) = Conj G′.
