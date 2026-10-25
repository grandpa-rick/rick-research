# PROVE 257 — Conjecture 8 of the LG/OG draft is now a proposition

**For:** Clio (and Robin). **Date:** 2026-10-25.
**Draft:** https://github.com/grandpa-rick/work-in-progress/blob/main/papers/lg-og-negative-degree/main.pdf (WIP 45cf937)
**Proof record:** `proofs/2026-10-25-conjT-half-step-operator.md`; scripts `work-in-progress/scripts/prove257/`.

## What changed in the draft
- Conjecture 8 (the half-step operator T) is now **Proposition 6.16** in a new subsection §6.5, which runs about 2 pages.
  §8 no longer lists it. The outline mentions it. The rest of the paper does not depend on it.
- The statement is the corrected Wake-257 text, unchanged, except that it now says "unitriangular" instead of "unipotent"
  and includes a uniqueness line.

## The proof in five lines
1. A_e = S ζ^{-1} S and A_o = S ζ_o^{-1} S. These are signed Möbius functions; the proof is the alternating sum over subsets of max θ.
   Here ζ_o is the containment matrix restricted to equal lengths.
2. Define X(κ,ν) = δ − 2^{−κ_{r₀}}[ℓ(ν)=ℓ(κ)−1][ν_s ≤ κ_{s+1} ∀s ≥ r₀]. Here r₀ is the first part where ν and κ differ:
   delete the part κ_{r₀} and shrink the tail. Define P by the same formula with + and no length condition.
3. First-row recursions give Xζ = ζ_oP, and then XP = I, both by induction on ℓ(κ).
4. Hence T = S ζ_o^{-1} X S squares to A_oA_e, so it is the unique unitriangular root. The column P(·,∅) = 2^{−κ₁} gives
   T s₀ = s_{1/2}, which is (a).
5. (b): T = A_o·(SXS). Expanding gives an inclusion–exclusion over removable maximal boxes. For a non-ribbon, a toggle
   involution at the lowest row that overlaps the row above in two columns kills the sum. For a ribbon only ∅ and {NE end}
   survive, which gives ε(−½)^{|D|}.

## Checks
For parts ≤ 8 (256 partitions), the computer confirms Lemma 6.17, Lemma 6.18(c)(d), T² = A_oA_e, the printed rule (b) and
T s₀ = s_{1/2}. For parts ≤ 6 it also checks T against the binomial series. A negative control (perturbed X weight) fails every check.

## Requested
A line-read of §6.5 when convenient. It is lower priority than Prop 4.6, and nothing else in the paper uses it.
