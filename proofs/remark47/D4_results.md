# D_4 verification of the BGG-Verma type-B/D program

**Status:** D_4 single-graded KL polynomial is **positive for all integer AND all spin pairs** (562 integer at λ_1 ≤ 3, 3912 spin at λ_1 ≤ 9/2). The B_n integer-vs-spin dichotomy does **not** transfer to D_4 in the obvious way, because D_n is simply-laced and so has no canonical (q,t)-bigrading from root length.

**Script:** `/home/agent/projects/proofs/remark47/bgg_decomposition_D4.py`
**Run log:** `/home/agent/projects/proofs/remark47/D4_run_log.txt`
**Date:** 2026-05-12

---

## 1. Conventions

* **Root system D_4 in R^4**, simple roots α_1 = e_1−e_2, α_2 = e_2−e_3, α_3 = e_3−e_4, α_4 = e_3+e_4.
* **Positive roots** (12 total, all of equal length): {e_i ± e_j : 1 ≤ i < j ≤ 4}. We split them into
  * "S" (minus-roots) = e_i − e_j (6 roots),
  * "L" (plus-roots) = e_i + e_j (6 roots).

  This split is W(A_3)-equivariant (just permutations) but NOT W(D_4)-equivariant: the sign-flip-pair elements in W(D_4) exchange S and L roots. This is the central caveat: the (q,t)-bigrading we use is **not canonical** in D_n.
* **ρ = (3, 2, 1, 0)** (verified as ½·Σ_{α>0} α).
* **Weyl group W(D_4):** signed permutations with even number of sign flips, |W| = 192. Length distribution exactly matches the Poincaré polynomial [2]_q[4]_q[4]_q[6]_q:
  ```
  ℓ:  0  1  2  3   4   5   6   7   8   9  10  11  12
  #:  1  4  9 16  23  28  30  28  23  16   9   4   1   (sum 192)
  ```
* **Dot action:** w·λ = w(λ+ρ) − ρ.
* **(q,t)-Kostant:** K_{q,t}(β) = #(decompositions of β into pos roots) weighted by q^(#L) t^(#S).
  Verified against brute-force enumeration on (1,1,0,0), (2,0,0,0), (1,1,1,1), (1,1,1,−1).
* **BGG identity:** KL_{λ,μ}(q,t) = Σ_w (−1)^{ℓ(w)} K_{q,t}(w·λ − μ).
* **Single-graded χ_q:** collapse (q,t) → q (every root contributes q^1). This is the canonical D_n KL polynomial.

## 2. Sampling

| Category | Total enumerated | Nonzero contribution to χ |
|---|---|---|
| Integer, λ_1 ≤ 3, λ ≥ μ ≥ 0 componentwise within dominant box | 1811 | **562** |
| Spin (all half-integer), λ_1 ≤ 9/2, dominant | 13284 | **3912** |

Spin pairs are tagged by (λ_type, μ_type) where type = "spin1" if λ_4 > 0 and "spin2" if λ_4 < 0. The two spin lattices correspond to the two half-spin representations of D_4; they are W(D_4)-distinct (Weyl elements preserve parity-of-#-negative-coordinates) but lie in the same coset of the root lattice (so KL_{λ,μ} can be nonzero across spin1/spin2).

## 3. Confusion matrices

### 3.1 Integer pairs, λ_1 ≤ 3 (562 nonzero)

**Bigraded (q,t)** — using the artificial (L, S) split:

| acyclic_qt ↓ \ positive_qt → | True | False |
|---|---|---|
| **True**  | **429** | 0 |
| **False** | 0 | **133** |

Off-diagonal cells (True, False) and (False, True) are empty — this is the tautological sanity check that the BGG bookkeeping is implemented correctly. 133/562 pairs are bigraded-non-acyclic-and-negative.

**Single-graded χ_q** — the canonical D_4 KL polynomial:

| | count |
|---|---|
| χ_q has all nonneg coefficients | **562** |
| χ_q has any negative coefficient | **0** |

**All 562 nonzero integer pairs have nonneg single-graded χ_q.** Consistent with Elias-Williamson positivity of KL polynomials at simply-laced D_4.

### 3.2 Spin pairs, λ_1 ≤ 9/2 (3912 nonzero)

**Bigraded (q,t):**

| acyclic_qt ↓ \ positive_qt → | True | False |
|---|---|---|
| **True**  | **3031** | 0 |
| **False** | 0 | **881** |

Again off-diagonal is empty. 881/3912 spin pairs are bigraded-non-acyclic-and-negative.

**Single-graded χ_q:**

| | count |
|---|---|
| χ_q has all nonneg coefficients | **3912** |
| χ_q has any negative coefficient | **0** |

**All 3912 nonzero spin pairs have nonneg single-graded χ_q.**

### 3.3 Spin breakdown by (λ_type, μ_type)

| (λ_type, μ_type) | nonzero | acyclic_qt + pos_qt | nonac_qt + neg_qt | pos_q | neg_q |
|---|---|---|---|---|---|
| (spin1, spin1) | 1137 | 1084 | 53 | 1137 | 0 |
| (spin1, spin2) | 819  | 701  | 118 | 819  | 0 |
| (spin2, spin1) | 819  | 594  | 225 | 819  | 0 |
| (spin2, spin2) | 1137 | 652  | 485 | 1137 | 0 |

**There IS a spin1-vs-spin2 asymmetry** at the level of the bigraded χ_{q,t}: spin2 (λ_4 < 0) pairs produce more bigraded-non-acyclic results than spin1, especially on the (spin2, spin2) diagonal. The asymmetry is **an artifact of the bigrading choice**: the L/S split treats e_i+e_4 and e_i−e_4 differently, and the spin2 lattice (with λ_4 < 0) interacts asymmetrically with this split.

In the canonical single-graded χ_q, the asymmetry vanishes: all four cells are 100% positive.

## 4. Examples

### 4.1 Integer pairs — bigraded χ_{q,t} negative but χ_q positive

Five representative pairs where bigrading sees an "obstruction" that the single grading does not:

| λ | μ | χ_{q,t} | χ_q |
|---|---|---|---|
| (1,1,0,0) | (0,0,0,0) | −t² − t⁴ + q + qt + 2qt² + qt³ + qt⁴ | q + 2q³ + q⁵ |
| (1,1,1,−1) | (0,0,0,0) | −t³ − t⁴ − t⁵ + qt + qt² + 2qt³ + qt⁴ + qt⁵ | q² + q⁴ + q⁶ |
| (2,0,0,0) | (0,0,0,0) | −t³ − t⁴ − t⁵ + qt + qt² + 2qt³ + qt⁴ + qt⁵ | q² + q⁴ + q⁶ |
| (2,1,0,0) | (1,0,0,0) | −t² − t³ − t⁴ + q + 2qt + 3qt² + 2qt³ + qt⁴ | q + q² + 2q³ + q⁴ + q⁵ |
| (2,1,1,−1) | (1,0,0,0) | −t² − 2t³ − 2t⁴ − t⁵ + 2qt + 3qt² + 4qt³ + 2qt⁴ + qt⁵ | q² + q³ + 2q⁴ + q⁵ + q⁶ |

Pattern: the bigraded negative coefficients are confined to a "pure-t" stripe (no q), and the same coefficient mass shows up positively in the "qt^k" stripes; collapsing q+t → q makes them cancel into a palindromic positive polynomial.

### 4.2 Spin pairs — bigraded χ_{q,t} negative but χ_q positive

| λ | μ | χ_{q,t} | χ_q |
|---|---|---|---|
| (3/2,3/2,1/2,−1/2) | (1/2,1/2,1/2,−1/2) | −t²−t³−t⁴ + q+2qt+3qt²+2qt³+qt⁴ | q + q² + 2q³ + q⁴ + q⁵ |
| (3/2,3/2,3/2,−3/2) | (1/2,1/2,1/2,−1/2) | −t³−t⁴−t⁵ + qt+qt²+2qt³+qt⁴+qt⁵ | q² + q⁴ + q⁶ |
| (5/2,1/2,1/2,−1/2) | (1/2,1/2,1/2,−1/2) | −t²−2t³−2t⁴−t⁵ + 2qt+3qt²+4qt³+2qt⁴+qt⁵ | q² + q³ + 2q⁴ + q⁵ + q⁶ |

Note: in B_3 (where the bigrading IS canonical) ALL spin pairs were bigraded-acyclic-and-positive. The fact that ~22% of D_4 spin pairs are bigraded-negative reflects the non-W-invariance of our chosen (L, S) split.

### 4.3 Spin pairs — both χ_{q,t} and χ_q positive (acyclic-and-positive bigraded)

| λ | μ | χ_{q,t} | χ_q |
|---|---|---|---|
| (1/2,1/2,1/2,1/2) (spin1) | (1/2,1/2,1/2,1/2) (spin1) | 1 | 1 |
| (3/2,1/2,1/2,1/2) (spin1) | (1/2,1/2,1/2,−1/2) (spin2) | q + qt + qt² | q + q² + q³ |
| (3/2,1/2,1/2,−1/2) (spin2) | (1/2,1/2,1/2,1/2) (spin1) | t + t² + t³ | q + q² + q³ |

The pair (spin1)↔(spin2) examples illustrate that χ_{q,t} for spin1→spin2 is purely "q-stripe" and spin2→spin1 is purely "t-stripe", related by the outer-automorphism that exchanges the two half-spin reps.

## 5. Interpretation: the load-bearing question

**The B_n integer/spin dichotomy does NOT obviously survive at D_4.** Two reasons:

1. **In simply-laced D_n there is no canonical (q,t)-bigrading.** The B_n bigrading came from the two root lengths (long/short); D_n has only one. Any (q,t)-bigrading we impose by splitting the 12 D_4 positive roots into two classes is necessarily non-canonical, and the natural candidate (L = e_i+e_j, S = e_i−e_j) is non-invariant under sign-flip Weyl elements.

2. **In the canonical single-graded picture, both integer and spin pairs at D_4 are 100% positive.** This is consistent with the Kazhdan-Lusztig positivity theorem (Elias-Williamson) for simply-laced types, and means there is **no integer/spin dichotomy at the single-graded level** at D_4 — both behave the same way.

What might still be true: if we work with a *folded* root system, e.g., view D_4 as the fixed locus of B_4 under a diagram automorphism, then perhaps the B_4 (q,t)-bigrading restricts to a nontrivial bigrading on the D_4 weight lattice. We did not pursue this.

## 6. Summary of findings

* **Implementation sanity check passes:** off-diagonal cells (acyclic-and-negative, non-acyclic-and-positive) are empty in both integer and spin categories (tautological by χ = mult_even − mult_odd bookkeeping).
* **Single-graded D_4 KL positivity confirmed empirically:** 562/562 integer + 3912/3912 spin = 4474/4474 pairs are χ_q-positive.
* **Spin1/spin2 asymmetry observed only in the bigrading**, not in the canonical single grading. The asymmetry is an artifact of our chosen non-canonical (L, S) split.
* **The B_n type-uniformity hypothesis does not have an obvious D_n analog**: simply-laced means no canonical bigrading, so the "spin saves positivity at the bigraded level" phenomenon of B_n does not directly transfer.

## 7. Computational notes

* W(D_4) of size 192 enumerated by signed permutations with even number of sign flips. Each Weyl element's length verified by inversion count; distribution matches [2][4][4][6] Poincaré exactly.
* (q,t)-Kostant via memoized recursion over POS_ROOTS_ORDERED, grouped by leading-nonzero-coord to enable strong pruning. Verified against brute-force on 4 cases; full integer + spin run completes in well under a minute.
* No surprises in runtime; the script ran end-to-end in a few seconds for ~15,000 (λ, μ) pairs.

## 8. Files

* `/home/agent/projects/proofs/remark47/bgg_decomposition_D4.py` — D_4 script.
* `/home/agent/projects/proofs/remark47/D4_run_log.txt` — full run output.
* `/home/agent/projects/proofs/remark47/D4_results.md` — this file.
* `/home/agent/projects/proofs/remark47/bgg_decomposition_B3.py` — B_3 template that this builds on.
