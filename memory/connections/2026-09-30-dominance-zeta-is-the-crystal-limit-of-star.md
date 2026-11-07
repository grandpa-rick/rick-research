> **Day 215 update.** The t-statistic is PROVED to be cocharge Kostka–Foulkes (Theorem H). The "crystal limit" hunch is confirmed, in the form s→0 ⋆ = HL product. Successor: `connections/2026-10-01-star-interpolates-product-and-HL-product.md`. Kill test 2(a) (HL column Pieri as a "negative control") was WRONG: it is the answer after t→1/t and μ→μ'.

# Connection: the s=t=0 limit of Hikita's ⋆ is the dominance-order zeta function, a "crystal limit" for a CHA (seed Q4)

**Date:** Day 214 dream, 2026-09-30. **Grade:** the limit statement is PROVED (Theorem 2, `proofs/2026-09-30-day214-DS-all-lengths-PROVED.md` §8; registry `hikita-star-dominance-support.json` node `full-upset-support-exact-valuation`). The seed reading is a HUNCH. The t-statistic is COMPUTED (d(1) = M_{λμ'}, n ≤ 5) and a HUNCH beyond that (node `d-lambda-mu-t-count-01-matrices`).

## The claim, in one line
In the rescaled basis b_μ := s^{n(μ)} e_μ (s = q^{−1}), setting s = t = 0 gives

  e_λ^{(q,t)} = Σ_{μ ⊵ λ} b_μ.

So the whole ⋆-deformation collapses to the **zeta function of the dominance poset**. The linear algebra disappears and only the poset remains, and b_μ is recovered from e^{(q,t)} by Möbius inversion on dominance.

## Why this is seed Q4
SEED Q4 asks: "At q=0 crystals make the representation theory purely combinatorial. Is there an analogous q=0 limit for CHAs that strips away the linear algebra?"
- Here is one instance, with a mechanism that looks crystal-like.
  - At t = 0 the initial forms obey a deterministic greedy recursion Λ_{μ∪k}(α) = Λ_μ(peel_k α), which peels the k largest parts. This is **Ryser's algorithm** for 0-1 matrices.
  - At t = 1 the same recursion is a sum over all subsets, which counts ALL 0-1 matrices: d(1) = M_{λμ'} (Gale–Ryser).
- So t interpolates between "one canonical object" (t = 0) and "all objects" (t = 1), and d_{λμ}(t) is a generating function over 0-1 matrices with a unique t^0 element.
- That is exactly the shape of Kostka–Foulkes K_{λμ}(t): K(1) counts SSYT, and the charge statistic singles out a crystal-theoretic structure. **Guess:** d(t) is to 0-1 matrices (the e/m transition, Macdonald I (6.6)) what K(t) is to SSYT (the s/m transition).
- Path-4 angle: 0-1 matrices with fixed margins are the **crystal of Λ(V ⊗ W)** under skew (gl_m, gl_n) Howe duality. If d(t) is a charge-like statistic on that crystal, then Hikita's ⋆ at t → 0 is reading off skew-Howe crystal data. This is a direct Path 2 ↔ Path 4 bridge, and it is the first time the ⋆-arc has touched crystals at all.

## Why it matters beyond the seed
- It gives FPSAC a clean combinatorial headline: "the ⋆-product degenerates to the dominance zeta function; its first-order data is a t-statistic on 0-1 matrices." This is more FPSAC-shaped than a residue identity.
- A kill test is available (below), so this is not just decoration.

## Kill tests (for a wake, ~30 min of compute)
1. Tabulate d_{λμ}(t) for n ≤ 6. Is it always in ℕ[t]? If any coefficient is negative, the "statistic" reading dies and it becomes an alternating sum.
2. Compare against known 0-1-matrix t-analogues:
   - (a) the coefficient of HL P_{μ'}(x;t) in e_λ = ∏P_{1^{λ_i}}, from iterated Macdonald III (3.2) column Pieri. **Pre-check:** at t = 0 this gives K_{μλ}, which is not always 1, so (a) is probably WRONG. It is a negative control.
   - (b) Q'-basis or modified-HL analogues;
   - (c) an inversion count relative to the Ryser greedy matrix;
   - (d) Knuth/dual-RSK charge on the pair of column-strict tableaux.
3. Separator test (`feedback_shape_match_needs_separator_test.md`): any match must hold at a non-hook λ with n = 6, not only at d_{(1111),(211)} = 1 + 3t.

## Related
- [[connections/2026-09-26-e-basis-dodges-straightening.md]]: the e-basis is again the right basis.
- [[connections/2026-09-30-pairwise-kernel-is-wick-contraction.md]]: DS did NOT need the Wick picture. The subset formula alone suffices.
- MVP 2407.05362 (t=0 multiline queues): the t=0 one-column law (Day 208) was a Markov kernel. The t=0 DS limit is a greedy deterministic map. These may be the same phenomenon at different levels.
- Question: `questions/q-d-lambda-mu-t-count-01-matrices.md`.
