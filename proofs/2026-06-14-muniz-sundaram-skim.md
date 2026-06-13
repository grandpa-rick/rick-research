# Muniz arXiv:2505.21738 abstract + intro skim

**Date:** 2026-06-14 (Day 69 CODE Phase 3)
**Paper:** Bárbara Muniz, *Symplectic Branching through Crystals*,
arXiv:2505.21738 v1 (27 May 2025), updated 6 Jun 2025.
**PDF cache:** `/home/agent/papers/muniz_2505.21738.pdf`.

## Verdict

**CLOSE.** Not portable to BDI (GL(n) → O(p,q) restriction).
This is a strictly type-C (GL₂ₙ → Sp₂ₙ) paper. Per-rank crystal
construction with no orthogonal analogue or n-uniform statement.

Logs as **OQ-MUNIZ-PORT CLOSED.**

## Abstract (verbatim)

> We give an alternative proof of Naito-Sagaki's conjecture, which
> states that the restriction of gl₂ₙ(ℂ)-representations to sp₂ₙ(ℂ)
> can be described in terms of crystals. Using the tableau model for
> crystals, we construct an explicit and self-contained bijection
> between their highest weight elements and Sundaram's branching
> model.

## Key intro claims (pp. 1–3)

- Symplectic-only: GL₂ₙ(ℂ) ↓ Sp₂ₙ(ℂ). The multiplicity
  [V_{gl₂ₙ}(λ) : V_{sp₂ₙ}(μ)] = #{n-symplectic LR tableaux of shape λ\μ}.
- Main theorem: multiplicity = #{sp₂ₙ-HW SSYT of shape λ, weight μ}.
- Construction: sp₂ₙ-HW tableau splits as shape-μ part + skew λ\μ
  part filled by ordered barred-pairs {i, ī}.
- Bijection F = ι_sp⁻¹ ∘ ι_LR via two inductive pair-deletion maps.
- Prior art: Littlewood (stable n), Sundaram [Sun90] (general n),
  Kwon [Kwo18], Lecouvey-Lenart [LL20], Kumar-Tores [KT24] (hive
  bijection), Schumann-Torres [ST18] (Burge + symplectic RSK proof
  of Naito-Sagaki), Naito-Suzuki-Watanabe [NSW25] (coideal route).

## Answer to portability questions

### Q1: Is the construction n-uniform or per-rank?

**Per-rank.** The n-symplectic condition is intrinsically tied to
fixed rank n. The whole point of the paper over Littlewood's stable
result (n > ℓ(λ)) is enumerating which LR tableaux have fillings > n
— rank-dependent corrections. No n-uniform statement available.

### Q2: What's the analogue of GL→Sp for GL(n) → O(p,q)?

**None offered.** No mention of orthogonal groups, type B/D, BDI
real forms, or O(p,q) signature. The "alternative" in the title is
an alternative *proof* of Naito-Sagaki for Sp, not a different
model. The barred-pair ↔ ε₁+ε₂ trick is symplectic-specific (long
root, type C); orthogonal analogues (King/Sundaram-orthogonal,
Proctor) are not discussed.

### Q3: Partial sums / fences / one-row inequalities?

**No.** Combinatorics is column-strict LR with a barred-alphabet
n-symplectic condition. Constraints are column-local and pair-based
(not row-prefix partial sums). Reading is far-eastern Kashiwara
crystal reading (column top-to-bottom, right-to-left), not a
prefix/fence inequality on row sums.

This is fundamentally a different combinatorial structure from
Rick's BDI cone (which is partial-sum / fence based). No structural
bridge.

## Connection to Rick's program

- **No direct help for v4 §3 BDI ↔ AII bridging.** Muniz's bijection
  is a within-Sp result; Rick is doing GL ↔ Sp via the AII LR map.
- **Some methodological inspiration:** Muniz's
  "ι_sp⁻¹ ∘ ι_LR via inductive pair deletion" is structurally
  similar to Azenhas's iterated red⁻¹ in the quantum LR map. But
  the framework is sp-HW SSYT, not n-symplectic LR tableaux that
  Rick was studying via Sundaram.

## Reading time

10 minutes (abstract + intro pp. 1-3 + portability scan).

## Files

- This skim: `proofs/2026-06-14-muniz-sundaram-skim.md`.
- PDF cached: `papers/muniz_2505.21738.pdf`.

## Status flags

- **OQ-MUNIZ-PORT CLOSED** Day 69: GL→Sp only, per-rank, no
  partial-sum structure. No portability to BDI.
- **No update needed to v4 §3 references** — Muniz is parallel-only
  to NSW (within-Sp HW characterisation), doesn't add to Rick's
  GL ↔ Sp bridge.
