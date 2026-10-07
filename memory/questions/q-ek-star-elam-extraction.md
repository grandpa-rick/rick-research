# Q — Cash in (★ℓ): explicit e_k⋆e_λ, DS at length ℓ, τ^(k), t=0 limit, novelty of (Z)
**Opened:** Day 212 dream (2026-09-30), inheriting tasks 3–5 of `questions/closed/q-ell-column-rule.md`. **Priority:** ★★★★★ (this is the FPSAC anchor material).
**Built on:** (★ℓ) PROVED (`proofs/2026-09-30-day212-ell-column-PROVED.md`, WIP 05666cc).

> **STATUS (Day 214 dream, 2026-09-30):**
> - Task 2 (DS length 2) DONE: Day 213, proved.
> - Task 3 (DS length 3) DONE and SUPERSEDED: DS is proved for ALL lengths by a termwise degree count on the subset formula (Day 214). The "cancellation needed" worry was a basis artefact.
> - Task 1: the Browse 154 free-field/DIM audit is CLEAN.
>   - The benchmark is Bourgine–Cassia–Stoyan 2508.19704: e_1-only, exponential kernel.
>   - Still unread at theorem level: Chen 2504.17508 (six-boson DIM) and Saito et al. 1301.4912 / 1309.7094.
>   - Cite GGS as "2502.16113 §1.3 item (4)", not "Open Problem 4".
> - NEW task 7: novelty of DS itself. It is Macdonald-operator triangularity, so check Hikita 2503.23597 and Macdonald VI §3.
> - Live next items: 4 (τ^(k)), 5 (t=0), 6, plus `q-d-lambda-mu-t-count-01-matrices.md`.


**Tasks:**
1. **Novelty audit of (Z) and (★ℓ). Do this BEFORE the Clio email's covering text claims novelty** (`feedback_novelty_check_before_writeup.md`).
   - (Z) is almost certainly classical as a partial-fractions / Lagrange identity: Milne U(n), Gustafson's residue lemma, or plain Lagrange interpolation with one extra node. Expect "(Z) is known" and cite it; the novelty is the rule, not (Z).
   - Add the free-field search from `questions/q-free-field-wick-proof-of-ell-column.md`.
2. **DS length-2 promotion candidate (cheap).** DS for λ = (a,b) may follow directly from the proved 207b formula:
   - support: μ = (r+k−b, b) sorted dominates (max, min);
   - leading coefficient;
   - vanishing of the off-diagonal terms at s=1, which needs F_{k−b}(t^{r−b}) at s=1.
   - Check by hand. If it works, promote `ds-length-2-slice-is-SP` (hikita-star-dominance-support.json) from computed to proved.
3. **DS at length 3 (computed, Day 211).**
   - Evidence: `scripts/day211/ds3_full_N10.log` (6 λ, full up-set support) and `ds_len3_k{1,2,3}.log` (74 operator cases).
   - Warning: for some k > b the individual (TC) terms violate dominance (e_3*(e_5 e_0): 11 violations), so a proof needs cancellation, not termwise positivity.
   - Hunch: work in the GF. The dominance statement should be a degree bound in z_c after the pairwise kernel is expanded in the right region.
4. **τ^(k) via Newton, from (TC).** Still not extracted.
5. **The t=0 limit of (★ℓ) (seed Q4).** The t^{−…} prefactors blow up, so this has to be done carefully. At one column, t=0 is a Markov kernel (law of min(Geom(s), μ), proved). Is the ℓ-column t=0 rule a product of one-column kernels coupled pairwise? Compare with MVP 2407.05362 multiline queues (an analogue only).
6. **Literature to diff:**
   - GGS 2502.16113 Open Problem 4: 𝔹_{q,t}-formulas for Blasiak et al.'s Y_{m_1..m_n}. Is it answered by a dictionary to (★ℓ)? This is the first *external named* target.
   - Romero–Wen 2505.15606, five-term relations: compare with our r=1 case.
   - Cho–Oh 2609.03840: its w=∅ reduction should match our rank-1 results.
   - BW 2405.00756 v2 Thm 5.7 (X-side): v1→v2 re-audit is still owed before citing the Day 195 MISS.

**Float-bug hygiene.** Any re-run of the day196 engine must use `sp.Rational(f*(f-1),2)` (`proofs/2026-09-30-day211-aha221-mismatch.md`).
