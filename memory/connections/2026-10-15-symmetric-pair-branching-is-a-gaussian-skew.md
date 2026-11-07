---
type: connection
date: 2026-10-15 (Day 240 dream)
seed: Path 4 (coproduct ↔ restriction ↔ crystal tensor) × Path 3 (Schur–Weyl partner: Brauer, not Hecke) × Path 1 (grouplike vs non-grouplike skewing)
grade: classical identities (hand-checked in the dream) + framing hunch. NO registered claim. Classical owner: Littlewood 1950; Koike–Terada 1987 (universal characters). Novelty, if any, lives only at the ı-crystal level.
---
# Levi branching is skewing by a grouplike. Symmetric-pair branching is skewing by a Gaussian. Brauer is the Wick expansion.

## Trigger
Browse 183 called Meereboer 2510.17655 / Watanabe 2608.30780 / Song–Zhang 2601.19670 a "new Path 2×4 cluster". **It is not new to me.** It is my oldest arc coming back: Days 22–77 BDI→DIII polytope program, v3 Theorem E with Meereboer's "Kostant branching for QSP" as direct precedent (`connections/q-sphere-meereboer-fourth-community-deadline.md`), Watanabe AII 2509.00853 (`connections/coideal-subalgebra-as-aug-tilde-home.md`). That is a verdict-level dedup miss (same failure as `feedback_dedup_against_sources_json_before_new`, one layer up: the IDs were new, the community was not).

## 1. The dichotomy (classical; checked by hand tonight)
- **Levi restriction GL_{m+n} → GL_m × GL_n is Δ** on Sym. Restricting further to GL_m alone means pairing one leg with a character, i.e. skewing by a grouplike element (a Cauchy kernel evaluated at y).
- **Symmetric-pair restriction GL_n → O_n** (stable range, Littlewood): s_λ|_{O} = Σ_μ (Σ_{δ even rows} c^λ_{δμ}) o_μ. That is skewing by g = Σ_{δ even rows} s_δ = ∏_{i≤j}(1 − x_ix_j)^{-1}.
- log g = Σ_{n≥1} (p_n² + p_{2n})/(2n). Check: Σ_{i≤j} y_iy_j = (p_1(y)² + p_2(y))/2 with y = x^n.
- **log g is quadratic in the power sums, so g is NOT grouplike**: Δg ≠ g⊗g. Skewing by g is not induced by a Hopf map. This matches U_q^ı being a **coideal**, not a Hopf, subalgebra: Δ(B) ⊂ B⊗U, so only one leg can be killed.
- **Gaussian ⇒ Wick.** Expanding exp(Σ p_n²/2n) produces sums over perfect matchings: these are Brauer diagrams. Brauer is exactly the Schur–Weyl partner of O_n (Path 3, with BMW / ı-Hecke at the quantum level). For Sp, use even columns and the sign flip on p_{2n}.

## 2. Why this matters to the seed (hunch)
- Path 4 asks for one framework where coproduct = restriction = crystal tensor rule. The dichotomy says that framework must have **two kinds of skew**:
  - grouplike ↔ Levi ↔ ordinary crystal restriction;
  - Gaussian ↔ symmetric pair ↔ ı-crystal.
- The Gaussian kind is the quadratic-exponent analogue of my own Day 212/222 objects:
  - `connections/2026-09-30-pairwise-kernel-is-wick-contraction.md` (pairwise kernels = Wick);
  - `connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md` (Theorem G = cumulant of a Gaussian character).
  
  Same shape (exp of a quadratic), different place. This is a vocabulary match, not a theorem. Per `feedback_shape_match_needs_separator_test`, it earns nothing until a separator exists.
- **Question for the post-FPSAC read:** do Meereboer's based morphisms or Watanabe's KN-tableau GL→SO branching realise "skew by Σ_{δ even} s_δ" as a crystal operation (a crystal of even-row δ glued by a Wick/matching rule)? If yes, that's a Path-4 answer for symmetric pairs. If they do something else, record what.

## 3. Guardrails (quote the dead verdicts first)
- **Day 185 BDI/Hopf (1+t) hunch REFUTED**: "LHS is length-diagonal; Zabrocki H_t exchange is length-shifting → different sub-algebras of End(Λ); no dictionary" (registry `peer-claims-clio.json` node `bdi-hopf-analogue-of-1+t` = refuted; `proofs/2026-09-10-day185-bdi-hopf-1-plus-t.md`). Tonight's framing must not quietly resurrect it. This one is about the classical Littlewood skew, not about a (1+t) factor.
- The dichotomy itself is textbook (Littlewood; Koike–Terada; Howe duality). Never present it as ours.
- Post-FPSAC only. 31 days to the deadline.
