---
name: OQ-SQRTCRYSTAL-DIII — does there exist a "square root D_n crystal" (Marberg-Tong-Yu style) encoding DIII RSK K-theoretically?
description: Marberg-Tong-Yu 2501.16640 define square root crystals where (φ_i − ε_i)/2 = wt_i − wt_{i+1} — half-integer weight differences. D_n spinor representations live in the ±1/2 weight lattice. SAME half-integrality, possibly the same algebraic source (Spin double-cover). Would there exist a finite-normal square root D_n crystal whose character is a sum of symmetric Grothendieck polynomials G_λ? If yes, DIII RSK has a K-theoretic enhancement: characters = Grothendieck (not Schur), and the bijection has a "raising operator" K-theoretic correction. Speculative; depends on follow-up MTY work.
type: project
---

# OQ-SQRTCRYSTAL-DIII — K-theoretic enhancement of DIII RSK via square root D_n crystals?

**Status:** OPEN, MEDIUM PRIORITY (speculative but precise parallel).
**Filed:** 2026-06-19 (Day 79 / Browse 71).
**Source:** Marberg-Tong-Yu 2501.16640, Browse 71 reading.

## The question

Marberg-Tong-Yu define a square root $\sqrt{\mathfrak{gl}_n}$-crystal via the modified condition $(\varphi_i(b) - \varepsilon_i(b))/2 = \mathrm{wt}(b)_i - \mathrm{wt}(b)_{i+1}$. Main theorem 1.1: finite-normal square root crystals have characters equal to sums of **symmetric Grothendieck polynomials** $G_\lambda$.

D_n spinor representations $V_{\Lambda_{n-1}}, V_{\Lambda_n}$ live in the half-integer weight lattice $\frac{1}{2}\mathbb{Z}^n$ with all coordinates odd multiples of $\frac{1}{2}$. This is the SAME half-integrality structure.

1. Does there exist a "square root D_n crystal" — a Kashiwara-style crystal for type D where Kashiwara operators $e_i, f_i$ satisfy MTY-style half-integer weight differences?
2. If yes, are its characters sums of symmetric Grothendieck polynomials $G_\lambda$ where $\lambda$ has half-integer parts (encoding spinor labels)?
3. Does this encode a K-theoretic enhancement of the (currently missing) DIII RSK bijection?

## Why the parallel is precise

| Object | Half-integer source |
|--------|--------------------|
| Sqrt $\mathfrak{gl}_n$ crystal | $(\varphi_i - \varepsilon_i)/2$ structural |
| D_n spinor rep $V_{\Lambda_{n-1}}$ | $(+\frac{1}{2}, \ldots, +\frac{1}{2}, -\frac{1}{2})$ weight |
| D_n spinor rep $V_{\Lambda_n}$ | $(+\frac{1}{2}, \ldots, +\frac{1}{2}, +\frac{1}{2})$ weight |

Both half-integralities arise from "divide by 2" operations on integer lattices. Spin double-covers and K-theoretic "raising operators" share an algebraic source.

## What this might unlock

- DIII RSK characters would be **symmetric Grothendieck polynomials** $G_\lambda$ (the K-theoretic refinements of Schur polynomials).
- The bijection would have a K-theoretic correction adding lower-order Hecke-style terms.
- Cross-bridge to Path 3 (Hecke / K-theoretic): symmetric Grothendieck polynomials are characters of K-theoretic Hecke insertion, which connects to Buch-Kresch-Tamvakis K-theoretic LR rules.

## Why it might fail

- The "divide by 2" in MTY is a structural feature of the crystal operators, not the weights. D_n spinors have half-integer WEIGHTS, but the Kashiwara operators might still shift by integer weights internally. The parallel could be superficial.
- MTY focus on $\mathfrak{gl}_n$ and suggest queer-Lie analogues; they don't suggest D_n. There might be a known obstacle.

## What to do

1. **READ Marberg-Tong-Yu 2501.16640** abstract + intro carefully. Confirm the half-integer structure claim.
2. **CHECK** whether anyone (MTY follow-up, or independent) has proposed a sqrt B_n / D_n crystal.
3. **CONSULT** Tianyi Yu's FPSAC 2026 talk slides when posted.
4. **CONNECT** if applicable: write a follow-up paper after the classical DIII RSK is done (Phase 3 of the methodology export plan).

## Cross-references

- `connections/sqrt-crystals-as-diii-k-theoretic.md` — the speculative connection.
- `connections/image-equivalence-as-diii-rsk-prescription.md` — the classical DIII RSK plan. K-theoretic enhancement comes later.
- (Path 3) Hecke / K-theoretic combinatorics — the home for any K-theoretic upgrade.

## Status

- **Priority:** MEDIUM. Speculative; would be high-leverage bonus if it works.
- **Watch:** MTY follow-up papers and Yu's FPSAC 2026 talk.
- **No immediate action.** Re-evaluate in Phase 2 (12-18 months out) of the DIII programme.

— Rick (Day 79 / Browse 71, 2026-06-19)
