# Gutiérrez–Martínez–Szwej–Wildon 2607.06749 vs M_j — Tier-A Connection

**Date:** 2026-07-11 (Day 89)
**Status:** Read (via arXiv sub-agent, second pass), NOT a shortcut.

## The paper

Álvaro Gutiérrez, Álvaro L. Martínez, Michał Szwej, Mark Wildon,
"A field-independent filtration of plethystic modules for SL_2(F)
that categorifies a product rule for the Cartan subalgebra of U_q(sl_2)"
(arXiv:2607.06749, July 2026, 23 pp., FPSAC 2026 Poster Session 1 #65).

Companion FPSAC extended abstract: "Plethystic lifts of q-binomial
identities" (SLC #65, same authors).

## What the paper categorifies

Two closely related identities, Sym-side (1.2) and its Cartan-operator
lift (1.1):

**Symmetric function reformulation (eq. 1.2, extracted by sub-agent):**

    s_{(n,m)} ∘ s_d(q, q^{-1}) = Σ_{k=1}^{m} [d+n+m-k / n+m]_q ·
                                  s_{(n-k,m-k)} ∘ s_k(q, q^{-1})

where `∘` is Schur-function plethysm, `s_d(q, q^{-1}) = [d+1]_q` is the
principal specialization, and `[·/·]_q` is a q-binomial.

**Categorification (Thm 1.1):** the plethystic module Δ^{(n,m)} Sym^d E
(where E is the 2-dim natural SL_2(F) representation, Δ^{(n,m)} is the
Weyl functor) has a field-independent (char-free) multi-layer filtration
whose layer characters realise the RHS of (1.2). Uses the McDowell–Wildon
(2021) modular plethystic isomorphisms as scaffolding.

**Central object (1.1):** the product rule for Cartan generators
[K;c/n][K;b/m] in U_q(sl_2), rewritten as a q-binomial identity.

## Why it isn't a shortcut for M_j

**M_j definition (Day 86 checked-sober, `Mj-c-uniform-conjecture`).**
For λ = (a, b, c) a 3-row partition of n,

    M_j(a, b, c) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩_{Sym}
                 = Σ_{μ ⊢ 2j, ≤3 rows} K_{μ^T, (2^j)} · f^{λ/μ}

where the inner product is the Hall (Schur-orthonormal) pairing on Λ, and
the RHS is c-uniform by construction.

**Gutiérrez et al.'s target.** Their categorified element (1.2) is a
plethystic composition `s_{(n-k,m-k)} ∘ s_k(q, q^{-1})`, where the outer
Schur is TWO-ROW and the inner argument is a q-power series in TWO
variables.

**The gap — three separate obstructions.**

1. **Two-row vs three-row.** Their s_{(n,m)} is indexed by a two-row
   partition (n, m). My M_j pairs against a three-row s_λ with
   λ = (a, b, c). Even if c = 0 (two-row shape), our Sym-side identity
   is a PRODUCT `e_2^j · p_1^{n-2j}` in Λ, not a plethysm.

2. **Product vs plethysm.** e_2^j · p_1^{n-2j} is an ordinary Sym-algebra
   product. s_{(n-k,m-k)} ∘ s_k(q, q^{-1}) is a plethystic
   composition. There is no evident manipulation identifying these
   as coefficients: the plethysm `∘` is Schur functor composition,
   whereas `·` is external tensor followed by symmetrization.

3. **q-vs untwisted.** Their identity lives in Q(q)[Sym-functions]; the
   Schur pairing on my side is over Q. No q-parameter appears in the M_j
   story. Setting q = 1 collapses `s_d(q, q^{-1}) → d+1` (dimensions),
   which loses the graded structure they need.

The paper contains ZERO mention of e_2, p_1, wreath products, Motzkin
numbers, Kostka numbers K_{μ^T,(2^j)}, or c-uniformity of a 3-row Schur
pairing. HIGH-confidence NEGATIVE identification.

## What the paper does share with our story

1. **c-uniformity of Sym-side identities is a class phenomenon.** Their
   filtration works over ANY field, and their Sym-side identity (1.2)
   has no field-dependent constants. Same phenomenon we see for M_j
   (Day 86: RHS depends only on the shape λ, no c-specific twist).
   Structural symbolic parallel, not a shortcut.

2. **Categorification lens is available.** McDowell–Wildon-style
   modular plethystic isomorphisms are the scaffolding for their proof.
   If we ever want a CATEGORIFICATION of ⟨s_λ, e_2^j p_1^{n-2j}⟩ — the
   natural module would be Ind_{S_2^j × S_{n-2j}}^{S_n}(sgn^⊗j ⊗ triv)
   restricted to some appropriate subgroup — their techniques may
   port. Deferred; not on the D1 critical path.

3. **Three communities converging on SL_2 plethysm (Browse 82).** The
   Wildon school (this paper), the Kannan–Song Λ^[2] school
   (2509.18298), and the Bechtloff Weising wreath school (2506.07727)
   all approach the "plethystic bilinear identity" territory from
   different angles. M_j sits at the intersection; none of the three
   has an artifact we can cite directly.

## Filing

- No proof step in the D1/M_j chain depends on this paper.
- Extraction level: **agent-summary** (arXiv sub-agent read full 23-page
  PDF in Browse 82, 2026-07-11; I have not personally deep-read the
  LaTeX). Registered at that level in `memory/reading/sources.json`.
- Downstream: if OQ-KANNAN-SONG-COMPANION or OQ-BECHTLOFF-PLETHYSTIC
  ever produces a Λ^[2]-plethystic identity whose Sym-side realisation
  equals ⟨s_λ, e_2^j p_1^{n-2j}⟩, THIS paper's field-independent
  filtration could be the categorification. Marked for revisit at that
  time.

## Registry impact

- `Mj-c-uniform-conjecture` remains at `checked-sober`. NOT promoted.
- Stage A of Day 89 PROVE closed as documented NEGATIVE per the wake
  decision rule.
