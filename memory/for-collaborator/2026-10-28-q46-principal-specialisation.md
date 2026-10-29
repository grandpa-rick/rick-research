# Q46 (PROVE 262): one q is not enough. Principal specialisation does not separate Demazure characters

**For Clio and Robin. Not urgent, and the FPSAC cut is unaffected.** Proof: `proofs/2026-10-29-q46-principal.md`.

- **Theorem (q-Lemma D, sharp).** Let a ∈ Z^m be a regular grading (x_i ↦ q^{a_i}). Then rank_{Q(q)}{π_a ch_ρ : ρ ⊆ κ} = number of
  distinct values (w_ρω_m, a) over ρ ⊆ κ. The proof expands D_w in Q(x)#W, uses Vandermonde for the upper bound, and a triangular argument with a minimal-size representative per value for the lower bound.
- **π_q (a = ρ_C):** (w_ρω, ρ_C) = m(m+1)/2 − 2|ρ|, so **rank = |κ|+1**. The family is independent iff κ = (k) or (2,1).
  The first failure is **κ = (3,1)**: (3) and (2,1) collide. So under π_q the recursion does not pin down π_q(c_{κρ}).
- **Same rank as x=1**, and the π_q kernel specialises at q=1 to the x=1 (Crown K) kernel. Explicitly, at (3,1):
  ch_{21} − (q²−q+1)/(q²+1)·ch_3 − q/((q+1)(q²+1))·ch_2 − q²/((q+1)(q²+1))·ch_1  →  ch_{21} − ½ch_3 − ¼ch_2 − ¼ch_1.
- Moral: uniqueness needs a grading that separates (3) from (2,1). The bad locus is the hyperplanes Σ_{ρ∖σ} b_k = Σ_{σ∖ρ} b_k,
  and most of these are not root hyperplanes. Now in the long draft as Rem 4.19 (`rem:onegrading`, WIP a0da3a9), right after Lemma D.
