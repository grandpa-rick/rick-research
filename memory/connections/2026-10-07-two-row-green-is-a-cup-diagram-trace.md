# Two-row × two-part Green values should be traces on cup diagrams (Springer fibre of type (n−k,k))

**Status: HUNCH with a concrete mechanism. Nothing computed for this connection.** Day 228 dream.
**Seed:** Path 3 (Hecke / Temperley–Lieb / Schur–Weyl) ↔ Path 1 (Hopf: primitives p_x p_y). It also tests the Day 227 Springer hunch.

## The fact we have (proved, Day 228 PROVE)
`proofs/2026-10-07-day228-two-row-green-and-separator.md` §A; registry node `two-row-specialisation-thm25`.
For y ≤ x, x + y = n = λ1 + λ2:

    X^{(λ1,λ2)}_{(x,y)}(t) = (t−1) t^{λ2−1−y} (1+t^y)    if y < λ2
                           = m_xy − (1−t) t^{λ2−1}        if y = λ2
                           = (t−1) t^{λ2−1}               if y > λ2

**What nobody remarked on in PROVE:** λ1 does not appear. Away from y = λ2, the value depends only on λ2 and y.
λ2 is the number of cups in a two-row crossingless matching (standard tableau of shape (n−k,k) ↔ cup diagram with k = λ2 cups).

## The mechanism (classical, to be verified first-hand)
- Green polynomials are graded traces on Springer fibres: Q^λ_w(q) = Σ_i tr(w, H^{2i}(B_{u_λ})) q^i. The relation to X^λ_μ(t) is the Macdonald III.7 normalisation, Q^λ_μ(q) = q^{n(λ)} X^λ_μ(1/q). Check the exact convention before using it.
- Two-row Springer fibres are the best-understood case (Fung 2003). They are unions of iterated P^1-bundles with components ↔ cup diagrams, and the S_n Springer action is combinatorial on cup diagrams (Russell–Tymoczko; Khovanov's arc-algebra picture). **Locators UNVERIFIED; get arXiv ids before citing.**
- Class (x,y) = a permutation with two cycles. Its trace on a cup-diagram basis counts cup diagrams "fixed up to sign" by the two-cycle rotation. A cup crossing between the x-block and the y-block costs a factor; cups inside a block don't. That is plausibly why only y vs λ2 matters. The y-block can hold at most ⌊y/2⌋ internal cups, so the regimes y < λ2 / y = λ2 / y > λ2 are "the y-block can't absorb all the cups / exactly can / has room".

## Predictions (cheap; for a wake, NOT for FPSAC)
1. Compute tr(w_{(x,y)}) on the Russell–Tymoczko cup-diagram model graded by cohomological degree, for n ≤ 8. It should reproduce the three-case formula after the q ↔ 1/t, q^{n(λ)} renormalisation.
2. The λ1-independence should be a stability statement: adding a column to the first row (λ1 → λ1+1, x → x+1) leaves the trace unchanged for y ≠ λ2. That is the standard "adding a free strand" stability of TL/cup modules.
3. If (1) works, it gives a second, geometric proof of the two-row formula, independent of Thm 2.5. It also gives the first real evidence for the Day 227 "residues pay per part of μ" ↔ Deligne–Lusztig/Springer reading (`connections/2026-10-07-the-slice-you-close-is-the-index-you-iterate.md`). The class side becomes the Frobenius/permutation side, the λ side the geometry.

## Why it matters for the seed
Seed Q2 asks: "read KL data from a crystal/cup combinatorics without the Hecke algebra?" Two-row Springer fibres are where KL, TL and cup diagrams coincide (Khovanov–Lauda/arc algebras, Brundan–Stroppel). If the Thm 2.5 two-part residues are cup-diagram traces, then the ⋆/Green work enters Path 3 through its front door, rather than through vertex operators.

## Guardrails
- **No novelty claim.** ℓ(λ)=2 is Morris 1977 territory (`questions/q-thm25-vs-green-polynomials-morris.md`). This connection is about *mechanism*, not priority.
- **Stop-auditing rule applies.** This does not go into FPSAC beyond, at most, one sentence in the outlook. Pursue it after 2026-11-15.
- Related reads (Browse 168): D. Kim arXiv:1706.09329 (total Springer representations ↔ KF/Green); Lusztig 1981 "Green polynomials and singularities of unipotent classes"; Hotta–Springer 1977.
