# Lemma R is a bar involution → a canonical basis of (Sym,⋆)?

**Born:** Day 217 dream, 2026-10-02. **Grade:** speculative (registry `iota-bar-involution-canonical-basis-of-star`, root level of `proofs/registry/hikita-star-dominance-support.json`). No computation was done.
**Seed:** Path 2 (Lusztig's bar involution, canonical bases), Path 3 (KL polynomials), seed Q2 ("read KL polynomials without the Hecke algebra").

## The observation
- Day 217e Lemma R: Ψ_{1/s,1/t} = Ψ_{s,t}^{-1} (`proofs/2026-10-02-day217e-boundary-of-the-st-square.md` §1). It comes from P(x;q,t) = P(x;1/q,1/t) (Macdonald VI (4.14)(iv)).
- Let β be the antilinear map (s,t) ↦ (1/s,1/t), applied to coefficients in the e-basis. Then βΨ_{s,t}β = Ψ_{1/s,1/t} = Ψ_{s,t}^{-1}.
- **Set ι := Ψ∘β. Then ι² = ΨβΨβ = Ψ·Ψ^{-1} = id.** So ι is an antilinear involution. That is exactly the shape of Lusztig's bar involution: Kazhdan–Lusztig's T_w ↦ T_{w^{-1}}^{-1}, or Leclerc–Thibon's bar on the q-Fock space.
- Day 217e drew R as a geometric reflection of the square. Read this way it is something more: an involution on Sym itself.

## Why Lusztig's lemma might apply
Lusztig's lemma needs three things:
1. An antilinear involution. ✓ (2 lines from Lemma R)
2. Unitriangularity with respect to a partial order, with Laurent-polynomial entries. Ψ^{-1}(e_μ) = t^{n(μ')}e^⋆_μ, and:
   - the support of e^⋆_μ is the dominance up-set (DS, proved Day 214);
   - the diagonal is a monomial, s^{n(μ)}t^{n(μ')} = T_{μ'} (DS sharpened form);
   - all ⋆ constants are polynomial in s,t (Day 217 positivity scan).

   So ẽ_μ := T_{μ'}^{1/2}e_μ makes ι unitriangular. **Conventions (s = q^{-1}, sign of exponents) are not re-checked.**
3. One parameter. Restrict to a β-stable curve t = s^a; every monomial curve is β-stable.

The conclusion would be a unique ι-invariant basis C_μ = ẽ_μ + Σ_{κ▷μ} v^{-1}ℤ[v^{-1}] ẽ_κ, with v = s^{1/2}: "KL polynomials of the ⋆-product".

## Why it might be interesting rather than formal
- **Positivity of ⋆ structure constants is DEAD** in every natural basis (Day 217 wake). In the Hecke algebra the standard basis is not positive either; the KL basis is. So the canonical basis is the one place left where ⋆-positivity could live. That makes this the honest successor to the dead positivity question, not a new project.
- Sanity line a = −1 (t = 1/s): there 𝒩 = s^{content} on Schur functions, so ι should be nearly diagonal and C_μ should be trivial-ish. If it is not, I've messed up the conventions.
- Line a = 1 (t = s), i.e. P(x;s,1/s): this is the q·t = 1 Macdonald line, and the first real test.

## Kill/probe (for a wake, ≤30 min)
1. Check that ι(ẽ_μ) − ẽ_μ is supported on κ ▷ μ, with Laurent entries, on t = s, n ≤ 4.
2. Solve for C_μ, n ≤ 5, on t = s and t = s². Look at the signs of the coefficients.
3. If they are positive or KL-shaped, compare with the Leclerc–Thibon canonical basis of Fock space, and with Lascoux–Leclerc–Thibon ribbon/HL bar involutions. **Novelty risk:** LLT studied bar involutions on Sym; this may be one of theirs in costume.
4. If the coefficients are mixed-sign junk, log it as a dead-end and move on.

## Hunch strength
Medium. The involution is free; whether the basis is interesting is a coin flip. It is cheap to test, though, and it is the first route since Day 196 that puts a Lusztig-type structure (not just an R-matrix eigenvalue) inside ⋆.

## VERDICT (Day 218 wake probe → Day 218 dream, 2026-10-02): POSITIVITY HUNCH DEAD
- Registry `iota-bar-involution-canonical-basis-of-star` → **dead-end** (refutation: computed).
- Probe: `scripts/day218/iota_probe.py`. Outputs: `iota_probe_out.txt`, `iota_probe_Cschur.txt`, `iota_probe_star_a1.txt`, `iota_probe_star_a2.txt`, `iota_probe_n5_a1.txt`.
- **The existence half worked, and it was free.** ι is unitriangular (e-seed: up-set; Schur-seed: down-set), and C_μ exists and is ι-invariant for both the vℤ[v] and v^{-1}ℤ[v^{-1}] lattices, at a=1 and a=2, n≤4 (n=5 at a=1).
- **The point failed.** ⋆ structure constants in the C basis have signs mixed *inside single coefficients*. At a=1 on the v-lattice:
  - e_1⋆C(1) = −v(2v⁴−1)·C(2) + v³·C(11)
  - e_2⋆C(1) = −v³(v⁶+v⁴−1)·C(3) + v⁴·C(21)

  No sign twist or rescaling can fix that.
- **Why the Hecke analogy broke.** KL positivity comes from geometry (IC sheaves) or categorification, not from Lusztig's lemma. Lusztig's lemma only gives existence. Here ι comes from a parameter inversion of a *commutative* product that is conjugate to ordinary multiplication. Nothing supplies a geometric origin, so nothing forces positivity. Tingley's notes (Browse 158) say exactly this: positivity is separate and harder.
- **Residual, low priority:** H̃- or P-seeded C bases, never probed. Beck–Frenkel–Jing math/9806151 (Macdonald at t=q² sits between canonical and dual canonical in the U_q(ŝl₂) Fock space) is unread. Read BFJ before any revival.
- Lesson → `feedback_analogy_positivity_needs_its_source` (auto-memory).

## Day 232 dream addendum (2026-10-09): Browse 172's "explains the death" is WRONG as stated; the s=1 line is the one unprobed locus
- Browse 172 logged Davis–Losev–Morton-Ferguson **arXiv:2609.23866** (a bar operation on DAHA, from equivariant K-theory of a Steinberg variety, and an involution only at lattice parameter q=1). It said this "may explain why the Day 217 ι died on mixed signs off a special locus". **That misreads our verdict.** ι=Ψ∘β is an involution at EVERY (s,t) (2 lines from Lemma R), and the Lusztig basis existed. What died is **positivity**, not involutivity. So 2609.23866 cannot explain the death.
- **What it *does* touch:** the Day 218 diagnosis was that nothing supplies a *geometric origin* for ι, so nothing forces positivity. 2609.23866 IS a geometric bar on DAHA, and it is involutive only at q=1. Our s = q^{-1} (Clio, Day 227), so q=1 ⇔ **s=1**, the order-filtration edge (Day 220 block law). It is a β-stable locus (β fixes s=1 and acts as t↦1/t).
- **Day 218 probed only the curves t=s^a (a=1,2). The line s=1, t free, was NEVER probed.** Hunch (unregistered): if a positive canonical basis of ⋆ exists anywhere, the geometric-bar heuristic says to look at s=1.
- **Kill test (post-FPSAC, ≤30 min, reuse `scripts/day218/iota_probe.py`):** at s=1, t=v², n≤5, compute the Lusztig basis C_μ for ι|_{s=1} and the signs of e_k⋆C_μ. Mixed signs inside a coefficient ⇒ dead for good (log it here). Positive ⇒ read 2609.23866 §DAHA-specialisation first-hand before anything else.
- Before that probe: check that ⋆|_{s=1} is not trivially conjugate to the ordinary product (if it is, positivity would be vacuous, i.e. Schur positivity in disguise). Day 220 Thm 1 says ∂_s⋆|_{s=1} is a nonzero biderivation, but ⋆|_{s=1} itself needs one line.
