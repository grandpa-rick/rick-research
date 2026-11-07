---
name: Free-vs-plethystic power obstructs BW — the Sym-algebra reason
description: Day 88 second-cycle seed lens. M_j uses e_2^j (free power in Sym); BW uses s_β[e_2] (plethystic power). The obstruction is the standard Sym identity f^n = Σ_λ f^λ · s_λ[f]. Puts BW-vs-Mj gap in Path-1 territory.
type: project
---

# Free-vs-Plethystic Power — The Sym-Algebra Reason BW Isn't a Shortcut

**Filed:** 2026-07-10 (Day 88 dream cycle 2)
**Companion to:** `BW-reciprocity-vs-Mj.md` (which identified the gap at the subgroup-lattice level; this file identifies it at the Sym-algebra level).
**Tier:** S (seed-level, Path 1 + Path 3).

## The identity

For any f ∈ Sym and any n ≥ 0,
    f^n = Σ_{β ⊢ n} f^β · s_β[f]                                  (†)
where f^β = χ^β(1) = dim S^β is the ordinary irrep dimension of S_n on partition β, and s_β[f] is the plethysm.

This is a standard Sym identity — the RHS is the decomposition of the free power f^n of a single Sym-function element into plethysms weighted by S_n-character dimensions. Special case f = h_1: h_1^n = Σ_β f^β · s_β, which is the regular-rep decomposition of R(S_n).

## Why this is exactly the BW-vs-M_j obstruction

**M_j uses the FREE power e_2^j.** By definition,
    M_j(a,b,c) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩          (n = a+b+c, λ = (a,b,c))
The e_2^j is the ordinary j-fold Sym product. In representation terms:
    Frob^{-1}(e_2^j · p_1^{n-2j}) = Ind^{S_n}_{S_2^j × S_1^{n-2j}}(sgn^{⊗j} ⊠ triv)
where S_2^j is a **direct product** Young subgroup (no wreath).

**BW gives the PLETHYSTIC pieces.** BW Theorem 3.18 (and its cyclic Cor 3.19) computes branching multiplicities of GL_{nm} irreps restricted to wreath (Z/2)^n ⋊ S_n = B_n. Translated to Sym: BW's RHS involves Sym-function pairings of the form ⟨s_λ, s_β[f] · (rest)⟩ with s_β[f] plethystic — precisely the terms on the RHS of (†).

**Applying (†) to Rick's M_j:**
    e_2^j = Σ_{β ⊢ j} f^β · s_β[e_2]
so
    M_j(a,b,c) = Σ_{β ⊢ j} f^β · ⟨s_λ, s_β[e_2] · p_1^{n-2j}⟩ = Σ_{β ⊢ j} f^β · N_β(λ)      (‡)
where N_β(λ) is a **BW-computable** wreath-branching multiplicity: it's the ⟨s_λ, s_β[e_2] · h_1^{n-2j}⟩ pairing, which is exactly the Sym-side of BW's Cor 3.19 with η = sgn, m = 2, G = Z/2, and top-wreath label β.

So BW does NOT compute M_j directly. It computes each N_β. To reconstruct M_j you must then execute the **aggregation Σ_β f^β · N_β** — which requires computing N_β at every β ⊢ j and summing weighted by irrep dimensions. For j = 6, β runs over 11 partitions; for j = 12, 77 partitions; growth is P(j). Aggregation isn't intractable, but it's not a shortcut either.

## Seed-lens implications

**Path 1 (combinatorial Hopf algebras).** The identity (†) is a fundamental Path-1 structural fact — it says that in Sym viewed as a Hopf algebra, the **plethystic structure and the free-product structure are related but distinct**. Free power f^n lives in the polynomial subring Q[f, f^2, ...] ⊆ Sym; plethystic powers s_β[f] live in a strictly finer decomposition (dim Q[f]_n = 1 < dim Sym_n typically). The relation between them is (†), and (†) is a *linear* relation with combinatorially-natural coefficients f^β.

For our M_j family: **c-uniformity is a free-power property** (e_2^j is a monomial in Sym; its Sym-side coefficients in the Schur basis are c-uniform polynomials via Kostka-inversion arguments). The plethystic pieces s_β[e_2] individually are also c-uniform (that's BW), but the aggregation (‡) is a nontrivial weighted sum. Both perspectives see c-uniformity — but for **different structural reasons**.

**Path 3 (Hecke / Schur-Weyl).** The direct product S_2^j × S_1^{n-2j} vs the wreath (S_2 ≀ S_j) × S_{n-2j} distinction is *not* superficial. Under Schur-Weyl duality, the direct product acts on V^{⊗n} through the flag ∏ Sym^2 ⊗ h_1^{n-2j} inside GL, whereas the wreath acts through Sym^j(∧^2) ⊗ h_1^{n-2j}. The "outer plethysm layer" is precisely what h_j[∧^2 V] adds beyond (∧^2 V)^{⊗j}. In Iwahori-Hecke language: the wreath is Weyl(B_j) = S_2 ≀ S_j sitting inside S_{2j}, and Hecke H_q(B_j) has a copy inside H_q(S_{2j}). Rick's M_j lives at the Young level; BW's identities live at the Weyl-B_j (Hecke type B) level.

**Path 2 (quantum groups) — speculative but load-bearing.** The plethysm s_β[e_2] is the Frob character of the wreath-labeled irrep of S_2 ≀ S_j; at q = 1 it decomposes to Weyl-B_j irreps. At q generic, this becomes an H_q(B_j)-module. So (†) has a q-deformation:
    ("e_2^j at level q") = Σ_β dim_q(β-irrep of H_q(B_j)) · s_β[e_2]_q
which — if it exists as a genuine identity in q-Sym / H_q(B_j) representation theory — would refine the c-uniformity phenomenon to a q-analog. **Open question**: is (†) the q=1 shadow of a Hecke-B_j identity? If yes, β' is secretly quantum-group data.

**Path 4 (crystals) — the diagonal thread.** Rick's Sym-side identification M_j = Σ_μ K_{μ^T,(2^j)} · f^{λ/μ} (Day 85-86) puts M_j squarely in the "Kostka × skew-tableau count" family — Path 4's home. The Kostka K_{μ^T,(2^j)} counts SSYT of shape μ^T with content (2^j) = column shape; via RSK this is the number of columns in μ^T of length 2^j... hmm actually more precisely it counts fillings of μ^T with j 1s, j 2s, ..., etc., that are SSYT. When μ is arbitrary and content is (2^j), this is a specific Kostka number that has a **crystal interpretation** via Kashiwara operators on words of content (2^j). The Path-4 story: **M_j is a Sym pairing computable via crystal statistics on rectangles**.

## What this suggests concretely

1. **Attack (A) shouldn't have been "BW gives M_j directly."** It should have been "BW gives N_β; can we compute Σ_β f^β · N_β in closed form?" With BW's Sym-side formula for N_β, this becomes a **plethysm summation** — a well-studied topic in Path-1 literature (e.g. Loehr-Warrington 2006, Assaf 2015).

2. **The h_k^{(c)}(a,b) factorization has a plethystic re-interpretation.** Each h_k^{(c)} = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a,b,c) can be re-expressed via (‡) as a sum over β ⊢ (c-1-k) of plethystic pieces. This might give an *independent* derivation route that doesn't go through Clio's Lemma-1 template. Would clarify what Q_k really is (Sym-function object, not just "the polynomial that makes the identity work").

3. **The Γ-ratio rescue (Day 88 methodology file) has a Path-1 shadow.** Analytic continuation past a Pochhammer boundary is DUAL to plethystic expansion past its "free" range. In (†), if β has more parts than makes combinatorial sense, s_β[f] is well-defined algebraically but has no obvious S_n-rep meaning — same phenomenon as Γ(x) at negative integers being formally defined via residues. The two extensions are algebraically parallel.

## Reg impact

**No registry node touched by this file** (it's a lens, not a computation). But:
- If plethysm-summation of N_β turns out to give M_j closed-form: `Mj-c-uniform-conjecture` might promote to `proved` by a BW-adjacent route.
- If the h_k^{(c)} factorization has a plethystic re-derivation: `hk-c-uniform-three-var-conjecture` gets an independent second proof — insurance against a subtle bug in Clio's template.

## Cross-references

- `BW-reciprocity-vs-Mj.md` — subgroup-lattice view.
- `Mj-as-sym-function-multiplicity.md` — the Sym-side identification (Path 1 + 3 + 4, Tier S).
- `gamma-ratio-rescue-notation-lies.md` — the notation-lies pattern; §"seed-lens implications" here notes plethystic parallel.
- `2T-periodicity-as-sym-2adic-bridge.md` — c-uniformity as Sym property.
- Registry: `beta-prime-mod8.json` node `Mj-c-uniform-conjecture` (approach text could benefit from adding "plethysm summation via BW" as alternative attack route).
- Cite for (†): standard in Sym literature; Macdonald Ch I §7 (plethysm), or Grinberg-Reiner arXiv:1409.8356 §11.
