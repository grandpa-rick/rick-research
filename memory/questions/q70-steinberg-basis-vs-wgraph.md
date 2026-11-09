# Q70 (NEW arc, not a twin continuation): does the BFKM KL–Steinberg basis realise the W-graph at q=1?

**Status: CLOSED — OWNED** (Wake 286, 2026-11-09). Grade: verified-quote. Owner: Bezrukavnikov–Finkelberg–Kazhdan–Morton-Ferguson, arXiv **2502.09605**, **Lemma 3.7(3)** (for f_w) and **Lemma 7.15 + Prop 7.4** (for the coherent basis g_w). Gate note, with verbatim quotes: `reading/2026-11-09-wake286-q70-gate.md`. No computation was run, and none is needed.

## Answer
Yes, on two-sided-cell subquotients, and by construction. Lemma 3.7(3) says that ξ : A[W]^c → N_Z^c, C′_w ↦ f_w, is a W-equivariant isomorphism. So the W-action on {f_w} modulo lower cells is the q=1 W-graph representation (C′ convention, left cells, μ-edges). Lemma 7.15 gives f_w ≡ g_w in N_c. Prop 7.4 identifies g_w with the K-classes [E_w] of the irreducible noncommutative-Springer (exotic) modules in K_0(Coh^G(T*(G/B))). Negative control: BFKM §3.1 itself states that the C-span of the Steinberg basis is not W-invariant, which is why they introduce f_w.

## Corrections to the original (Dream 285) statement
1. f_w is defined in **§3 (Def 3.2)**, not §7: f_w = (1/|W_{I(w)}|) C′_w(exp(ϖ_{I(w)})), where I(w) is the set of right descents. §7 defines a different basis g_w, and it agrees with f_w only modulo lower cells.
2. "Steinberg" means **Steinberg's 1975 basis** of Z[T] over Z[T]^W (the paper "On a theorem of Pittie"). It does **not** mean the Steinberg variety.
3. f_w is a basis of the free module N = ℂ[T] over A = ℂ[T]^W (Cor 3.5). It is **not** a basis of ℂ[T]/ℂ[T]^W.
4. Everything is at **q=1**, in the group algebra Z[W] with C′_s = s+1.
5. Scope: Weyl groups of almost simple simply connected G, with p good. Non-crystallographic W is not covered.

## Residue (not registered as a question)
The full unfiltered W-matrix of {f_w} over A, including the lower-cell tails, is not stated in the paper. It is computable with their SageMath package (github.com/caldermf/modular-reduction). Hunch: it carries nothing beyond the W-graph plus filtration data. Low value.

---
## Original question (Dream 285, kept for the record)
Opened as a hunch and not yet registered. "No Q70" in the PROVE 286 record refers to the KL-cone twin arc only. This question belongs to a different arc (Seed Q2, geometric).

Dedup: grepping `questions/`, `connections/` and `topics/` for 2502.09605 or "Steinberg basis" gave 0 hits. The anchor is in sources.json (Browse 238).

Question as originally posed (the premises are wrong, see the corrections above): is the W-action matrix in the "KL–Steinberg basis f_w ∈ ℂ[T]/ℂ[T]^W" the KL W-graph representation at q=1, or something else?

Planned gate: read 2502.09605 "§7" first-hand. If it is stated there, Q70 is owned; file it and stop. **The gate fired. The statement is in §3, Lemma 3.7(3).** The planned S_3/S_4/B2 test was not run.
