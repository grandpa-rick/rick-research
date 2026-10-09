# Day 232 PROVE (a): thm:blockmult (long version Thm 7.8) checked against its PRINTED statement, aimed at non-coarsening pairs

**Date:** 2026-10-09 (Day 232 PROVE)
**Grade effect:** none. blockmult stays `proved` (Day 224 proof, restated in longversion §7). This is check coverage of the printed text, i.e. evidence, not proof.

> Drunk summary: the n=6 non-coarsening family has exactly THREE members. That isn't a bug, it's arithmetic: a κ≥2 non-coarsening pair needs a κ=1 non-coarsening block, and the smallest one is (2,2)→(3,1), of size 4. So n=6 can only ever be a thin test. I went to n=7 (11 pairs) and n=8 (29 pairs) on a mod-p engine with the variable count cut to μ_1 (stability, Lemma 2.8), cross-validated against the Fraction engine. Everything matches. The only "failures" were 0=0 leads at t=−2, which the paper's own Open Problem (2) predicts.

## Statement checked (longversion.pdf p.22, Thm 7.8, read from `pdftotext` of the PDF)

Let κ = κ(λ,μ) ≥ 1, ℓ = ℓ(λ), m = ℓ − κ. Then

  [(s−1)^m] c_{λμ} = Σ_π Σ_{(ν^C)_{C∈π}} ∏_{C∈π} [(s−1)^{|C|−1}] c_{λ^C,ν^C},

where:
- π runs over set partitions of [ℓ] into exactly κ blocks;
- (ν^C) runs over tuples with ⊔_C ν^C = μ and ν^C ⊵ λ^C;
- "every factor then has κ(λ^C,ν^C) = 1".

Together with Thm 6.6 this is Lead_{λμ}. κ is computed from the printed Definition 6.5.

## Implementation

- **LHS.** Hikita's subset formula, as printed (§2), gives e⋆_λ in m variables. Expand in e_μ by an exact linear solve at random points. Get the s-dependence by interpolation at n(λ)+3 nodes; the top two coefficients are verified to vanish, since the s-degree is ≤ n(λ).
- **RHS.** Enumerate π and the tuples (each tuple counted once as a map C ↦ ν^C). The factors come from the same engine applied to λ^C. Singletons contribute δ_{ν,(λ_j)}.
- **Engines.**
  1. `scripts/day232/check_blockmult_n6.py`: Day 231 Fraction engine (exact ℚ, n variables), t = 3/5.
  2. `scripts/day232/fastmodp.py` + `check_blockmult_fast.py`: same printed formula over F_p, p = 2^61−1, in m = μ_1 variables (Lemma 2.8 stability), t ∈ {3/5, −2}.
- **Cross-validation.** The fast engine matches the Fraction engine on all 199 (λ,μ,m) triples with n ≤ 5 and every m ≤ n, coefficient by coefficient in (s−1) (`validate_fast.py`).
- **Negative control.** Multiply one term of the RHS by 8/7; the identity must fail.

## Results

| run | pairs | result | log |
|---|---|---|---|
| n=6 non-coarsening, κ≥2, Fraction engine, t=3/5 | 3/3 | all OK; neg. control fails ✓ | `check_blockmult_n6.log` (117 s) |
| n=6 ALL κ≥2 (coarsening + non), mod p, t ∈ {3/5,−2} | 37/37 (34 coarsening + 3 non) | all OK; neg. control fails ✓; 5 zero leads at t=−2: (3,1,1,1),(2,1,1,1,1),(1^6)→(3,3) and (1^6)→(3,2,1),(3,1,1,1), all 0=0, every π has a block (1,1,1)→(3), whose factor Lead_{(1,1,1),(3)}=[3]_t(2+t) vanishes (checked by hand) |  `check_blockmult_n6_all.log` (1071 s) |
| n=7 non-coarsening, κ≥2, mod p, t ∈ {3/5,−2} | 11/11 | all OK; neg. control fails ✓ | `check_blockmult_n7_noncoarse.log` (238 s) |
| n=8 non-coarsening, κ≥2, mod p, t ∈ {3/5,−2} | 29/29 | all OK; neg. control fails ✓; 3 zero leads at t=−2, 0=0 | `check_blockmult_memo_n8_noncoarse.log` (584 s; memoised engine `fastmodp_memo.py`, re-validated 199/199 vs Fraction engine; the un-memoised run reached 22/29 all OK before being stopped) |
| side-claim "every factor has κ(λ^C,ν^C)=1", over ALL tuples (not only nonzero ones), n ≤ 8 | 7421 terms | True | `check_factor_kappa1.log` |

The three n=6 non-coarsening pairs, with values at t = 3/5:

- (3,2,1)→(4,1,1): κ=2, lead −49/25;
- (2,2,2)→(3,2,1): κ=2, 3 terms, lead −24/5;
- (2,2,1,1)→(3,1,1,1): κ=3, lead −8/5.

**Why so few.** A non-coarsening pair with κ ≥ 2 needs at least one block C with κ(λ^C,ν^C) = 1 and ν^C not a single part. The smallest such blocks are (2,2)→(3,1) at size 4 and (3,2)→(4,1) at size 5. At n = 6 the only completions are those three. κ = 1 pairs are the trivial single-block case of the identity (π = {[ℓ]}, tuple = (μ)), so they are not counted.

**Zero leads.** At t = −2 some leads vanish, e.g. (2,2,2,1)→(4,1,1,1) at n = 7. The identity then holds as 0 = 0: the vanishing factor is a connected lead with a root at t = −2, as with Lead_{(1,1,1),(3)} = [3]_t(2+t). This is consistent with the printed Thm 6.6 (nonzero over ℚ(t) and at t = 0) and with Open Problem (2). Every lead is nonzero at t = 3/5 (checked: True in all three mod-p runs).

**Bug found in my own first draft of the checker.** It also demanded LHS ≠ 0 at t = −2. Thm 6.6 does not claim that, so the first n=6/n=7 runs flagged 0 = 0 as FAIL. The checker was fixed and the runs were redone from scratch. There was no defect in the paper.

## Gaps

None for the claim checked. This is computed evidence on n ≤ 8 at two values of t. Coverage over ℚ(t) is by the written proof (Day 224 / longversion §7), not by these checks.
