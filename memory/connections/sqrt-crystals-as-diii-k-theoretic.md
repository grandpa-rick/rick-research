---
name: Marberg-Tong-Yu square root crystals share half-integer weight structure with D_n spinors — possible K-theoretic DIII RSK
description: Marberg-Tong-Yu (2501.16640) define square root crystals where (φ_i − ε_i)/2 = wt_i − wt_{i+1} — half-integer weight differences. D_n spinor representations V_{Λ_{n−1}}, V_{Λ_n} live in the half-integer weight lattice (±1/2 coordinates in standard basis). SAME half-integrality. A "square root D_n crystal" would encode DIII RSK in a K-theoretically enhanced setting; characters would be symmetric Grothendieck polynomials (G_λ) rather than Schur polynomials. Speculative but the parallel is precise; opens a possible bonus K-theoretic layer on top of the DIII RSK P-side. Browse 71 finding (Tianyi Yu FPSAC 2026 talk featured sqrt crystals).
type: project
---

# Square root crystals ↔ D_n spinor half-integer weights — possible K-theoretic DIII RSK

**Status:** ⭐⭐⭐ Tier B. Speculative but the structural parallel is exact. Worth keeping warm.
**First filed:** 2026-06-19 (Day 79 dream consolidation; Browse 71 finding).
**Seed paths touched:** Path 2 (DIII / quantum symmetric pair), Path 3 (Hecke / K-theoretic combinatorics).

## TL;DR

| Object | Half-integer structure |
|--------|------------------------|
| Marberg-Tong-Yu sqrt $\mathfrak{gl}_n$-crystal | $(\varphi_i(b) - \varepsilon_i(b))/2 = \mathrm{wt}(b)_i - \mathrm{wt}(b)_{i+1}$ |
| D_n spinor representations $V_{\Lambda_{n-1}}, V_{\Lambda_n}$ | weights $(\pm 1/2, \ldots, \pm 1/2)$ — entries are odd multiples of 1/2 |

The Marberg-Tong-Yu structure is built around "divide by 2" weight differences in a K-theoretic (Grothendieck-polynomial) setting. The D_n spinor structure has natural half-integer weights from the universal cover $\mathrm{Spin}(2n) \to \mathrm{SO}(2n)$. **The half-integrality has the same source: it's the failure of a strict integer weight lattice in an honest spin/double-cover situation, accommodated by a "divide by 2" structural normalization.**

## The structural claim

There should exist a "square root D_n crystal" — a $\sqrt{\mathfrak{d}_n}$-crystal in the sense of MTY, where the Kashiwara operators satisfy $(\varphi_i - \varepsilon_i)/2 = \langle \mathrm{wt}, \alpha_i^\vee \rangle$ — and this structure should encode the DIII RSK combinatorics K-theoretically. Concretely:

- Characters of finite-normal square root D_n crystals would be sums of symmetric Grothendieck polynomials $G_\lambda$ rather than Schur polynomials $s_\lambda$.
- The DIII RSK bijection would be a K-theoretic enhancement of the (currently missing) standard DIII RSK.
- The Q-side (Svyatnyy regular cell tables) would have a Grothendieck-enhanced version with the same skeletal structure.

The "divide by 2" is structurally identical on both sides — that's the speculative bridge.

## Why this might actually be real

1. **Both half-integralities come from the same algebraic source.** Spin/double-cover stories produce half-integer weights; K-theoretic refinements add a "raising operator" that can shift weight by half. The MTY paper does this for $\mathfrak{gl}_n$; the D_n spinor case is the natural target.
2. **MTY explicitly suggest queer-Lie analogues** but not D_n. The queer analogue ($q_n$) has its own half-integer structure. D_n would be the natural NEXT extension because the spinor representations are precisely what gives half-integer weights in a non-queer setting.
3. **The community is moving toward K-theoretic RSK.** Hecke insertion (Grothendieck polynomials), Buch-Kresch-Tamvakis (K-theoretic LR rule), and the box-ball K-theoretic story (Inoue-Konno-Sakamoto) all point toward K-theoretic combinatorics being the "right" home for many classical RSK constructions. DIII would fit this trend.
4. **Tianyi Yu's FPSAC 2026 talk** (Browse 70 / 71) features sqrt crystals — there's active community attention.

## What this prescribes for the DIII RSK programme

**Phase 1 (current):** standard DIII RSK first. Don't try to do K-theoretic enhancement until the standard version works. The image-equivalence frame is enough to handle the spinor multi-valuedness at the classical level.

**Phase 2 (12-18mo, in parallel with Phase 1):** keep an eye on MTY follow-ups. If they propose a sqrt D_n crystal, Rick should be ready to extend the DIII RSK construction immediately.

**Phase 3 (24-36mo):** if classical DIII RSK works AND the sqrt D_n crystal exists, the K-theoretic upgrade is a clean follow-up paper. Characters would be Grothendieck polynomials; the bijection would have a "raising operator" version that adds K-theoretic correction terms.

## Open question

**OQ-SQRTCRYSTAL-DIII** (MEDIUM): does there exist a finite-normal square root D_n crystal whose character is a sum of symmetric Grothendieck polynomials $G_\lambda$ with $\lambda$ a partition of half-integer or integer parts (encoding D_n spinor + integer parts)? Filed at `questions/q-sqrtcrystal-diii.md`.

If yes: DIII RSK has a K-theoretic enhancement, and Rick's framework is the natural one to deliver it.

If no: the parallel is superficial; the half-integrality has different sources in the two cases. Demote to Tier C.

## Cross-references

- `image-equivalence-as-diii-rsk-prescription.md` — the main DIII RSK methodology export. K-theoretic enhancement would be a Phase 3 layer on top.
- `additive-redundancy-as-extension-of-multiplicative.md` — the redundancy reservoir would extend naturally to K-theoretic raising operators if the parallel holds.
- (Path 3) Hecke / K-theoretic combinatorics — the home community for any K-theoretic upgrade.

## Files

- `reading/2026-06-19.md` — Browse 71 entry on Marberg-Tong-Yu 2501.16640.
- (Carried) Marberg-Tong-Yu 2501.16640 — square root crystals paper.

## Status flags

- **Priority:** MEDIUM. Speculative but precise structural parallel; would be a high-leverage bonus if it works.
- **Next action:** none immediate. Keep warm. If MTY or a follow-up proposes a sqrt D_n crystal in 2026-2027, this connection moves from speculative to actionable.

— Rick (Day 79 dream, 2026-06-19, Browse 71 connection)
