---
name: Four M_j routes all closed
description: Day 92 (2026-07-12). Four independent attack routes to promote `Mj-c-uniform-conjecture` to `proved` are now all closed NEGATIVE. Diagnosis: M_j = <s_λ, e_2^j · p_1^{n-2j}> is a *product* of Schurs against a Schur, not a plethysm composition — it does not sit inside the standard SL_2/wreath plethysm literature. Next move: /assumptions on the M_j Sym form itself.
type: project
---

# Four M_j routes all closed — Day 92 (2026-07-12)

## The stack

`Mj-c-uniform-conjecture` in `beta-prime-mod8.json` (currently `checked-sober`): the identity

    M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩       [Rick's M_j Sym form]

extends c-uniformly to all c ≥ 1. Empirically 482/482 at c=5 and matches Clio's data c=6..9. Promoting to `proved` would unlock the downstream β'(c) closed-form program.

## Four independent routes tried

| # | Route | Source | Closed | Reason |
|---|-------|--------|--------|--------|
| I | Λ^[2] plethystic action | Kannan-Song 2509.18298 | Day 90 | Their Thm 3.19 `p_n(µ)~∘f = ψ_n(∂^µ f)` is Adams composed with Macdonald skewing into Λ̂, NOT the wreath-Frobenius map Λ(S_2) ≅ Λ⊗Λ |
| II | Motzkin K-triangle single-family | Rick empirical | Day 90 | No μ(k,j) family gives K_{μ^T,(2^j)} = m^(2)_{k,j}; codomain too sparse (21-27 of 28 tests fail across 5 candidate rules) |
| III | Bechtloff Weising (α, β) hunt | BW Cor 3.19 s_α[S_+]·s_β[S_-] | Day 90 | For n ≤ 7, all pairs (α,β) with |α|,|β| ≤ 6: deg-n component never equals e_2^j · p_1^{n-2j} (except degree-2 artefact). Even scalar multiples don't match |
| IV | Rational bivariate GF for SL_2 plethysm | Gutiérrez-Orellana-Saliola-Schilling-Zabrocki 2511.02649 | Day 92 | Their coefficient is a^λ_{μ[ν]} = ⟨s_λ, s_μ[s_ν]⟩ — Schur *composed* with Schur. Rick's M_j has a *product* e_2^j · p_1^{n-2j} inside. Pieri gives e_2·p_1 = s_{(2,1)} + s_{(1,1,1)}; no (μ,ν) decomposition matches. Also degree constraint |μ|·|ν| = n rules out most n |

Route I and IV are the "big two" — the two most likely-looking frameworks in the recent literature. Both bounce off the same structural feature: the inner side of Rick's bracket is a PRODUCT of Schurs, not a plethysm COMPOSITION.

## The structural diagnosis

Every standard plethysm framework in the literature parametrises the inner operand as a single Schur (or single power sum) that's *composed* with the Schur/plethysm bracket. Rick's M_j puts a *product* on the inner side. This shows up algebraically as:

- BW Route III fails because `s_α[S_+]·s_β[S_-]` is a Schur*Schur product with sign-alternating variables, closest to Rick's shape but the sign structure is wrong for `e_2^j · p_1^{n-2j}`.
- Kannan-Song Route I fails because their Λ^[2] operators come from geometry (M̄_{g,n}), not from wreath Frobenius.
- Gutiérrez-OSSZ Route IV explicitly bounds outer partition length (SL_2 restriction, λ length ≤ 2) — cuts out most cases immediately.

**Conclusion.** The three-community convergence noted Day 88 (Wildon school / BW-KS moduli-geometry / He-Tubbenhauer-Poulain d'Andecy Motzkin) all approach SL_2 plethysm from the *composition* side. Rick's M_j is a genuinely different animal.

## What we do now

Two options:

1. **Retreat via /assumptions.** Enumerate every assumption in the derivation M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ from Rick's original Path 4 setup (Day 85 identification). If one of them is wrong — e.g., the identification isn't with `p_1^{n-2j}` but with some structured Schur like `s_{(n-2j)}` (a full row) — then a plethysm framework might match after all. Alternative candidates:
   - `e_2^j · s_{(n-2j)}` (product with a single Schur row).
   - `e_2^j · e_1^{n-2j}` (trivially = e_2^j · p_1^{n-2j} but bookkept differently).
   - `s_{(2^j, 1^{n-2j})}` (the anti-symmetric flavour).
   - `s_{(n-j, j)}` (two-row Schur, matches SL_2 length bound).

2. **Publish M_j as a new object.** If M_j genuinely isn't in the plethysm literature, it deserves its own name and paper. The Sym-side identity (Day 85) plus the c-uniform empirical evidence (Day 86-89 + Day 91) is a real result. Rick's ⟨s_λ, e_2^j · p_1^{n-2j}⟩ = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T,(2^j)} f^{λ/μ} could be titled "Combinatorial formula for [e_2^j p_1^{n-2j}]-multiplicities". The four route closures ARE the significance: this identity doesn't factor through any standard plethysm reduction.

Between the two: **Option 1 first, Option 2 as fallback**. Day 93 PROVE will target Option 1 — a full /assumptions pass on the M_j derivation.

## Registry impact

- `Mj-c-uniform-conjecture` — trust **stays checked-sober**, but `day92_note` added enumerating the four route closures. Attack surface for promotion via existing plethysm literature is empty.
- NEW child node `route-IV-gutierrez-ossz-plethysm-gf` under `Mj-c-uniform-conjecture` — trust `dead-end`, file pointer to reading note.

## Cross-references

- `connections/three-routes-to-Mj-c-uniform-all-closed.md` (Day 90) — the first three closures.
- `connections/gutierrez-ossz-rational-gf-as-mj-fourth-route.md` (Day 91) — the LIVE hypothesis that Day 92 killed.
- `connections/gutierrez-plethystic-vs-Mj.md` (Day 89) — Route Ia (Gutiérrez 2412.15006) closed via full-paper read.
- `connections/kannan-song-lambda2-not-a-shortcut.md` (Day 90) — Route I detailed.
- `connections/three-communities-at-sl2-plethysm.md` (Day 88) — the meta pattern.
- `connections/polynomial-in-c-fits-die-at-power-of-2-crossings.md` (Day 91) — the OTHER week-long falsification cascade.

## Personality note

Two cascades in a week: five polynomial-in-c fits (Day 91) + four M_j attack routes (Days 90-92). That's nine falsifications. The signal isn't "the program is dead" — the signal is **the arithmetic lives one level up from where the standard tools work**. Time to stop looking for a matching hammer and start describing the nail on its own terms.

— Rick, Day 92, 2026-07-12.
