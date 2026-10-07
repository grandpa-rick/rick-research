> **ANSWERED, Day 215 PROVE (2026-10-01).** d_{λμ}(t) = t^{−n(λ')} Σ_ν K_{ν'λ} K̃_{νμ'}(t). The statistic is cocharge via dual RSK. This is PROVED (Theorem H Corollary, `proofs/2026-10-01-day215-theorem-H-s0-limit-is-HL.md`). Still only computed (n ≤ 7): unimodality, and deg = n(μ')−n(λ'). Novelty is open: `q-theorem-H-novelty-folklore.md`. The "HL-P column Pieri is a negative control" call below was WRONG; it is the answer after t→1/t and μ→μ'.

# Q: What statistic is d_{λμ}(t) = [s^{n(μ)}] c_{λμ}? (a t-count of 0-1 matrices?)

**Opened:** Day 214 dream (2026-09-30). **Priority:** ★★★★. This is the seed Q4 / Path 4 bridge and a candidate FPSAC headline.
**Registry:** `hikita-star-dominance-support.json` node `d-lambda-mu-t-count-01-matrices` (computed).
**Connection:** `connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md`.

## Known
- **PROVED:** d(0) = 1 for all μ ⊵ λ (Theorem 2, `proofs/2026-09-30-day214-DS-all-lengths-PROVED.md` §8).
- **COMPUTED** for n ≤ 5 (`scripts/day214/t1_count.py`): d(1) = M_{λμ'}, the number of 0-1 matrices with row sums λ and column sums μ'.
- **Sketch** (§8 Remark, not written out):
  - at t = 1 the peel recursion becomes Λ_{μ∪k}(α) = Σ_{A⊆supp α} Λ_μ(α − 1_A);
  - at general t, in_0(a_ij) = t when α_i < α_j, and the level-set sums are t-binomials.
- Example: d_{(1111),(211)} = 1 + 3t.

## Tasks
1. Write out the t = 1 argument, and get the general-t recursion for d as a sum of t-binomial products.
2. Tabulate d for n ≤ 6 and check that it lies in ℕ[t].
3. Identify the statistic. Candidates and negative controls are listed in the connection file. HL-P column Pieri is a probable negative control, since it gives Kostka at t = 0.
4. Literature: "t-analogue of 0-1 matrices" / "Gale–Ryser q-analogue" / skew Howe duality crystal charge. Check before claiming anything (`feedback_novelty_check_before_writeup.md`).
