---
name: Q — is the block valuation law (t=0 case) classical? Gate before the FPSAC s=1 section
description: Day 220 dream. The t=0 case of Thm C unfolds to "(1−q)-valuation of (W(q)^{-1})_{μλ} = ℓ(λ)−κ(λ,μ)", W = HL P→m matrix. That's an old matrix; search for prior art before any abstract sentence.
type: question
---
- **Statement to search (unfolded, see crown §3):** P_λ(x;q) = Σ W_{λμ}(q) m_μ, W(1) = Id. Claim:
  v_{(1−q)}((W^{-1})_{μλ}) = ℓ(λ) − κ(λ,μ), leading coeff (−1)^{ℓ−κ}N(λ,μ). Equivalently [h_μ]Q′_λ(x;q).
  Hand check ((1,1),(2)): m_2 = P_2 − (1−q)P_{11} ✓.
- **Where to look:** Macdonald III.2–III.5 (P in m: (5.11′) tableau formula; the inverse is not in the book as far as
  I remember: check Examples); Wheeler–Zinn-Justin "Hall polynomials, inverse Kostka polynomials and puzzles"
  (arXiv ID to verify; Clio has their HL papers on her shelf, email 2026-10-03 00:16); Kirillov "Ubiquity of Kostka
  polynomials" math/9912094; search by formula, not name ([feedback] search by operator formula).
- **Generic t (our ⋆, s and t both live) is much less likely to be classical**: the order-filtration proof of Thm A
  and the merge-history formula with W_k(J) (Thm W) are Hikita-specific. Novelty risk concentrates at t=0.
- **Decision rule:** if the t=0 statement is found, cite it and present Thm C at general t as its deformation
  (Thm A lower bound + t=0 specialisation). If not found, claim both, with Clio's "I did not find it" standard.

## Day 221 wake verdict — LIKELY-FOLKLORE at t=0 (~75%)
DLT (SLC 32, 1994) eq (11) + Jacobi–Trudi raising form give Q′_λ = ∏(1−R_ij)/(1−qR_ij) h_λ; the coefficient
is a (1−x)/(1−qx)-Kostant partition function and the no-cancellation argument is ten lines. No paper states the law.
Computed n≤8. W (P→m) itself obeys the same law n≤5 (unexplained, likely via Macdonald III (5.11′)).
Consequence: FPSAC frames t=0 as an exercise; novelty = generic t + merge weights (Thm W) + leading coefficients.
File: reading/2026-10-04-wake221-inverse-HL-novelty.md. STATUS: gate resolved (folklore-risk accepted).

## Day 221 dream note
The t=0 DLT minimal flows for μ=(n) ARE the increasing trees of Theorems G/F, with flow = subtree mass. So the
folklore t=0 law and the proved generic-t lead formula share one combinatorial skeleton. Present G as the
t-deformation of the DLT flow count. Follow-up for general μ: `q-general-mu-lead-flow-forests.md`.
