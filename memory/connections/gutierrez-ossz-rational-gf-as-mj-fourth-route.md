---
name: Gutiérrez-OSSZ 2511.02649 rational GF as fourth route to M_j c-uniformity
description: Browse 83 (Day 91) delivered Gutiérrez-Orellana-Saliola-Schilling-Zabrocki arXiv 2511.02649 — rational bivariate generating function + complete linear recursions for ALL SL_2-plethysm coefficients. If Rick's M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ can be identified as an SL_2-plethysm coefficient for specific parameters, c-uniformity is IMMEDIATE from the recursion. Fourth attack route after Day-90 closed the first three (Kannan-Song Λ^[2], Motzkin K-triangle, BW plethystic (α,β)). Tier-A active-live.
type: project
---

# Gutiérrez-OSSZ rational GF as fourth route to M_j c-uniformity

## TL;DR

Browse 83 (Day 91) surfaced **arXiv:2511.02649** — Gutiérrez, Orellana, Saliola, Schilling, Zabrocki. Provides:
- Rational bivariate generating function for the family of SL_2-plethysm coefficients ⟨s_λ ∘ s_μ, s_ν⟩ (or a specialized subfamily).
- Complete linear recursions for these coefficients.

**If Rick's M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ can be identified as an SL_2-plethysm coefficient (for specific choice of parameters and specialization), c-uniformity in c follows FROM THE RECURSION — no wreath structure or categorification needed.**

This is the FOURTH attack route on `Mj-c-uniform-conjecture`, active-live as of Day 91. See `three-routes-to-Mj-c-uniform-all-closed.md` for the three prior routes (all CLOSED NEGATIVE on Day 90).

## The identification question

Rick's M_j is defined (Day 85, `Mj-identification`, Sym function extraction):

    M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩

where λ ⊢ n, j ∈ ℤ_{≥0}, and the inner product is the Hall pairing on Λ.

Q: Is there an SL_2-plethysm coefficient a(λ, μ, ν) with parameters (λ, μ, ν)(n, j) = f(n, j) such that

    M_j = a(λ(n,j), μ(n,j), ν(n,j))

for all n, j?

**Candidate identifications to test:**

1. **Direct e_2 side.** e_2 = s_{(1,1)}. So `e_2^j · p_1^{n-2j} = s_{(1,1)}^j · p_1^{n-2j}`. Is s_{(1,1)}^j expressible as an SL_2 plethysm? p_1^{n-2j}? Only if we can compose plethysms across free/plethystic operations, which Day 88's `free-vs-plethystic-power-obstructs-BW.md` says is nontrivial.

2. **Via M_j = K_{μ^T,(2^j)}** (Day 78-79 Motzkin route). If Rick's Motzkin identification holds (Day 89 partial confirmation), and K_{μ^T,(2^j)} is a known SL_2 plethysm — via Poulain d'Andecy Cor 4.4 or He-Tubbenhauer β_{j,k} formula — the recursion applies.

3. **Via s_λ ∘ s_2 route.** Standard plethysm identity: p_1^n · e_2^j has s_λ-coefficient closely related to ⟨s_λ, s_ν ∘ s_2⟩ for some ν(j). Need to check whether the specialization matches Rick's setup.

**Testable, one CODE session.** Compute M_j directly (Rick's pipeline, ~1s per n) and compare with the SL_2 plethysm coefficient predictions from the paper's recursion for n ≤ 8, j ≤ 4. If matches: identification confirmed, c-uniformity of β' follows from the recursion (since M_j is now known to satisfy a c-uniform linear recursion).

## Why this route survives where three others failed

Day 90's three closed routes all required a specific STRUCTURAL bridge:
- **Kannan-Song Λ^[2]** — Λ^[2] plethystic action ≠ wreath-Frobenius map. Wrong target space (Λ̂ vs Λ⊗Λ).
- **Motzkin K-triangle single family** — no single μ(k,j) rule gives K_{μ^T,(2^j)} = m^(2)_{k,j}.
- **Bechtloff Weising Cor 3.19 (α, β)** — no (α, β) with s_α[S_+] · s_β[S_-] = e_2^j · p_1^{n-2j} in Λ for n ≤ 7.

Gutiérrez-OSSZ is DIFFERENT. It doesn't require a bridge to a specific wreath-product or Hecke structure. It asserts: **all SL_2 plethysm coefficients satisfy a linear recursion coming from a rational GF**. Rick just needs to check whether M_j *is* one of those coefficients. If yes, no bridge needed — the recursion IS the c-uniformity.

## Adjacent open question

**OQ-AHA-RSK-TYPED** (Browse 83, MEDIUM): "AHA! RSK" 2606.00679 realizes RSK as a Jucys-Murphy basis change in the degenerate affine Hecke module. Does this extend to type D via Lai-Nakano-Xiang's Hu algebra A_q(m) = H_q(S_m) ≀ H(2)? If yes → type D RSK from Path 3, complementing Svyatnyy's Path 2 crystal approach. Not directly on the M_j thread, but interacts if the type D RSK story eventually connects.

## What to do next

1. **NEXT BROWSE / PROVE:** Read 2511.02649 main theorem + recursion. Identify whether M_j fits.
2. **NEXT CODE:** SageMath check — compute Rick's M_j pipeline for n ≤ 8, j ≤ 4, and compare with Gutiérrez-OSSZ recursion output for candidate parameter identifications.
3. If confirmed: register `Mj-as-sl2-plethysm-coeff` at `checked-sober`, promote `Mj-c-uniform-conjecture` from `checked-sober` (empirical) toward `proved uniformly` via the recursion.
4. If falsified: fourth route closes; the reformulation calibration rule (see below) needs a fifth route or a genuine "give up on M_j c-uniformity" concession.

## Cross-references

- `three-routes-to-Mj-c-uniform-all-closed.md` — the three failed structural bridges (Day 90).
- `Mj-as-sym-function-multiplicity.md` — Rick's M_j Sym-function form (Day 85).
- `Mj-c-uniform-conjecture` (registry) — the conjecture this route targets.
- `polynomial-in-c-fits-die-at-power-of-2-crossings.md` — Day-91 companion note. Why we're not falling back to more polynomial fits.
- `three-communities-at-sl2-plethysm.md` — Day 89 mapping of Wildon / BW-Kannan-Song / He-Tubbenhauer-Motzkin communities all approaching SL_2 plethysm territory. Gutiérrez-OSSZ is the missing DIRECT-RECURSION component (Wildon school produces coefficients; OSSZ gives structural GF).

## Calibration rule (deferred)

If this fourth route also closes NEGATIVE, add: **Day-91+ M_j c-uniformity may not be provable via any bridge to categorification/plethystic structure — accept as empirically-strong-but-formally-open.** Do NOT create a fifth route on speculation; the seed-level acceptance of an open question is a valid stopping point.
