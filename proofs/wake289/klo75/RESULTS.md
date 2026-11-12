# KLO 2310.20571 Conj 7.5 — computational check (Wake 289 agent, 2026-11-11)

All results are **computed**, not proved. The arithmetic is mod p. Hypothesis cases were run at two primes (32003 and 30011), which agree; the other cases used p=32003 only.

## Model (matches the paper's definitions exactly)
- **Same module as the paper.** By Thm 5.5, M_P depends only on sh(τ_P). For every basic skew shape λ/μ we therefore use P = poset(τ_0^{λ/μ}). Distinguished labelings are in bijection with RSP_n (Lemma 3.6 / eq. (3.3)), so the skew-shape sweep covers all of RSP_n up to isomorphism.
- **Basis.** Σ_L(P) = read_{τ_0}(SYT(λ/μ)) (Lemma 3.2). τ_0 labels the boxes right-to-left, starting with the top row.
- **Action, eq. (2.3).**
  - π_i γ = γ if i ∈ Des_L(γ).
  - Otherwise π_i γ = s_iγ (swap the values i and i+1) if s_iγ lies in the basis, and 0 if it does not.
- **Composition order.** λ/μ = C_1 ⋆ … ⋆ C_k, with C_1 the top-right component.
- **Ribbon.** A component is a ribbon if it contains no 2×2 square.
- **Categories.**
  - **dr** (contains a disconnected ribbon): some C_j and C_{j+1} are both ribbons.
  - **hyp**: disconnected and not dr. These are exactly the cases covered by the conjecture.
- **Checks on the model.**
  - The H_n(0) relations were checked exactly for every module.
  - The character Σ F_{comp(Des_L γ)^c} was checked.
  - Example 7.4 is reproduced exactly: basis [21435, 42531]_L, dim 10, End = ⟨id, 21435↦42531⟩.

## Cross-check against the induction model (`indmodel.py`, `crosscheck.py`)
- **Construction.** An independent iterated induction X_{C_1} ⊠ … ⊠ X_{C_k}, using explicit Ind on coset representatives.
- **Coverage.** All 318 disconnected shapes with n ≤ 6.
  - Dimension and full F-character agree in 318/318 cases.
  - Explicit isomorphism (a random element of Hom is invertible) holds in every case with d ≤ 40.
- **Order matters.** The reversed product C_k ⊠ … ⊠ C_1 is often *not* isomorphic. This is consistent with Prop A.2(1), whose top-right factor comes first.
- **End algorithm check (`endcheck.py`).** The cyclic-generator method agrees with the brute-force commutant in dim End and in the number of eigenvalues: 232/232 shapes, n ≤ 6, d ≤ 45.

## End / indecomposability method (`klo.py: end_algebra, local_test`)
- **Reduction to v = f(σ).** M is cyclic on σ = read_{τ_0}(T_{λ/μ}), which is the minimum of the interval. So f ∈ End is determined by v = f(σ).
- **Necessary conditions on v.**
  - v is supported on {γ : Des(σ) ⊆ Des(γ)}.
  - π_i v = 0 for every i that exits the interval at σ.
- **Building and verifying f_v.**
  - f_v is built by BFS along the weak order.
  - Linear combinations are solved by testing commutators against random vectors.
  - **Every** End basis element is then verified to commute exactly with all π_i.
- **Locality test.** Take the left-regular matrix of a random X ∈ End (k×k, in v-coordinates). Count the distinct roots of its characteristic polynomial over the algebraic closure, using deg(cp / gcd(cp, cp′)).
  - 1 distinct root ⇔ End is local ⇔ M is indecomposable, up to the probability of an unlucky random choice.
  - In general the count equals the number of indecomposable summands, with multiplicity.
- **Top.** dim Hom(M, F_α) for every α, computed exactly as a union-find (graph) problem.

## Counts (`out_sweep_2_7.jsonl`, `out_sweep_8_8.jsonl`, one JSON record per shape)
| n | hyp | hyp indec | hyp dec | conn (all indec) | dr tested (all dec) / skipped by dim cap |
|---|---|---|---|---|---|
| 2 | 0 | – | – | 2 | 1 / 0 |
| 3 | 0 | – | – | 4 | 5 / 0 |
| 4 | 0 | – | – | 9 | 19 / 0 |
| 5 | 2 | 2 | 0 | 20 | 65 / 0 |
| 6 | 13 | 13 | 0 | 46 | 212 / 1 (d>400) |
| 7 | 60 | 60 | 0 | 105 | 380 / 305 (d>400) |
| 8 | 229 | 229 | 0 | 242 | 54 / 2134 (d>120) |

- **Conj 7.5 holds for every shape with |λ/μ| ≤ 8, at both primes. NO COUNTEREXAMPLE.**
- Largest hypothesis module: d = 1176 at n = 8. dim End over hyp cases ranges from 2 to 50.
- **No hypothesis case is a brick (dim End ≥ 2 always).** Connected shapes are often bricks.
- Run times: n ≤ 7 takes 4 min, n = 8 takes 24 min. n = 9 (788 hyp cases, d up to 6552) was not run.

## Observations (computed, 1468 records with n ≤ 8)
- **Summand count.** The number of indecomposable summands equals ∏ over maximal runs of r consecutive ribbon components of 2^{r−1}. This holds in all cases: conn, hyp and the tested dr.
  - This is the natural strong form of the conjecture. In the Prop 7.3(2) splitting, each piece X^(1) ⊠ P_γ ⊠ X^(2) is indecomposable, where the run of ribbons is replaced by a single projective.
- **Top structure.** top(M) is always multiplicity-free and equals ⊕_{β∈[α_proj]} F_β, with 2^{k−1} summands for k components. This is consistent with Lemma 5.4.
  - So hypothesis modules with k components have a 2^{k−1}-dimensional top that is glued; for k = 2 that is two top functionals.
  - The cases with k = 3 at n ≤ 8 (1 + 8 + 42 shapes) all have patterns of the form R,N,R or N,R,N. All have a 4-dim top and are still indecomposable.

## Files
`klo.py` (model, End, top), `indmodel.py` (induction model), `crosscheck.py`, `endcheck.py`, `sweep.py` (args: nlo nhi drcap), `count.py`.

**Note:** `brute.py, endo.py, shapes.py, run.py, summarize.py, out_n*.jsonl` are NOT from this agent. They appeared 00:34–01:02 while this one was running, apparently from a parallel agent writing to the same directory. They are untouched and unverified here. The files listed above under "Files", plus `t1.py` (the Example 7.4 check), belong to this RESULTS.md.
