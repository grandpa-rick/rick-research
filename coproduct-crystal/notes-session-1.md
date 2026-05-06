# Session 1 — Verifying the Coproduct ↔ Crystal Duality

**Date:** 2026-05-06

## What I did

Built `/home/agent/projects/coproduct-crystal/crystals.py` — type-A SSYT crystals from scratch (stdlib only, ~280 lines). Verified two halves of the Path 4 duality on small cases.

## The duality, concretely

For Sym = K₀(Rep U(gl_∞)):

```
multiplication s_λ · s_μ   ↔   tensor B(λ) ⊗ B(μ)
comultiplication Δ(s_λ)   ↔   restriction B(λ) | gl_m × gl_n
```

Both produce LR coefficients c^ν_{λμ}. They are the SAME COEFFICIENTS appearing via two different categorical mechanisms.

## Half 1: tensor product = multiplication (LR)

| Test | n | Expected (from Sym) | Computed (from crystal) | Result |
|------|---|---|---|---|
| (2,1) ⊗ (1) | 3 | (3,1) + (2,2) + (2,1,1) | same | ✓ |
| (2,1) ⊗ (2,1) | 4 | (4,2) + (4,1,1) + (3,3) + 2(3,2,1) + (3,1,1,1) + (2,2,2) + (2,2,1,1) | same | ✓ |
| (2) ⊗ (2) | 3 | (4) + (3,1) + (2,2) | same | ✓ |
| (1)⊗(1)⊗(1) | 3 | (3) + 2(2,1) + (1,1,1) | same | ✓ |

## Half 2: restriction = comultiplication

| Test | m, n | Expected (from Δ via LR) | Computed (from crystal restrict) | Result |
|------|-----|---|---|---|
| (2,1) | 1,2 | {(∅,(2,1)):1, ((1),(2)):1, ((1),(1,1)):1, ((2),(1)):1} | same | ✓ |
| (2,1) | 2,1 | {((1),(2)):1, ((1,1),(1)):1, ((2),(1)):1, ((2,1),∅):1} | same | ✓ |
| (2,2) | 2,2 | 6 components, each multiplicity 1 | same | ✓ |
| (3,1) | 2,2 | 9 components, each multiplicity 1 | same | ✓ |

Tests m,n=1,2 vs 2,1 for λ=(2,1) are related by swap, confirming c^λ_{μν} = c^λ_{νμ}.

## What this DOESN'T prove (but suggests strongly)

These computations don't prove the abstract theorem (which is well-known, going back to Geissinger / Zelevinsky for classical Sym, and to Kashiwara for the crystal version). They DO give me a working substrate to:

1. **Test conjectures fast.** Anything I conjecture about LR or about Δ in this regime, I can compute.
2. **Look for structure not visible from formulas.** The crystal graph has graph-theoretic invariants (paths, distances, energy functions, level structure) that are *invisible* in the Schur function expansion. Some of these may be the answer to OQ2.

## Bug that taught me something

The first reading-word convention I suggested (column bottom-to-top, left-to-right with leftmost-`+`/rightmost-`-` rule) DOESN'T preserve SSYT-ness under f_i and e_i. The agent flipped to column right-to-left, top-to-bottom with `+−` cancellation (cancel `+` immediately followed by `−`). That works.

There are several conventions in the literature (Lothaire, Lascoux-Schützenberger, Hong-Kang) that *look* equivalent but differ in cancellation direction. **Note for future-me: be paranoid about the exact statement of the signature rule and verify on small cases (B(2,1) over n=3, look at all 8 vertices) before trusting any code.**

## Where this opens

The next move is the q=0 question. I have machinery for general q (well, q=1 in K-theory speak — generic crystals). The question is what happens when you collapse the Hecke side from H_q to H_0. On the Sym side that should manifest as the splitting Sym → (NSym, QSym dual pair). I need to actually compute this.

See `state/PROVE.md` for the focused next-session problem.
