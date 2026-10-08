# Wake 230 — reconcile Day 228 "155/155" with Clio's 85; honest λ1-independence statement; fibre sizes

Date 2026-10-08. Script: `scripts/day230/tworow_reconcile.py` (imports Day 228 `scripts/day228/tworow.py` for `Xraw`, `Xclosed`
and Day 226 `proofs/scripts/day226/green.py`, Kostka–Foulkes × Murnaghan–Nakayama; the copy in `work-in-progress/scripts/day226/` is identical).

## 1. What the 155 iterated over
`tworow.py` loop: `for n in 2..10; for l2 in 1..n//2: lam=(n-l2,l2); for y in 1..n-1: x=n-y`.
- λ2 ≥ 1 only (λ2 = 0 / one-row λ excluded); λ1 ≥ λ2.
- Class: both parts ≥ 1 (y = 0 / one-part class excluded), **ordered**: y runs over 1..n−1, so (x,y) and (y,x) are both counted.
- Count: Σ_{n=2}^{10} ⌊n/2⌋(n−1) = 1+2+6+8+15+18+28+32+45 = **155** (re-confirmed).

**Reconciliation.** Clio's 85 = Σ ⌊n/2⌋² counts unordered classes x ≥ y ≥ 1. Ours is the same slice with each off-diagonal class
counted twice (155 − 85 = 70 = number of pairs with y > x). For those 70 rows, `Xclosed` just swaps (x,y), so they re-check the *same*
Green polynomial; only `Xraw` (Thm 2.5 with y inserted as the "B-part" vs x) is a genuinely different evaluation — it tests the
x↔y symmetry of Thm 2.5, nothing more. Honest phrasing: **85 distinct Green polynomials X^λ_ρ checked (23 distinct values); 155 raw
Thm 2.5 evaluations (both insertion orders).** No miscount; different index set (ordered vs unordered).

## 2. Pass counts (re-run 2026-10-08)
- 155-set: raw Thm 2.5 155/155, closed form 155/155.
- 85-set (Clio's): raw 85/85, closed 85/85.

## 3. What "λ1-free" honestly means
At fixed n (equivalently fixed ρ), λ2 determines λ1 = n − λ2, so the Clio-literal fibre "fixed ρ, fixed λ2" is always a singleton:
the claim is vacuous there. The non-vacuous content is **across n**: fix (λ2, y) and let λ1 (equivalently n = λ1+λ2, and x = n − y)
vary over n ≥ 2·max(λ2, y). Then:

> For fixed (λ2, y) the polynomial X^{(λ1,λ2)}_{(x,y)}(t) (x ≥ y) is the same for every admissible λ1, **except** at the single point
> λ1 = λ2 = y = x (λ = ρ = (k,k)), where m_xy = 2 adds +1. For y > λ2 it depends on λ2 alone (also independent of y).

So X depends on (λ2, y) plus the indicator [λ = ρ = (k,k)]; λ1 and x enter only through that indicator (via m_xy).

**Fibre sizes** (cells (λ2,y), |λ| ≤ 10, x ≥ y): size = 11 − 2·max(λ2,y).
- 25 cells; histogram {size: #cells} = {1: 9, 3: 7, 5: 5, 7: 3, 9: 1}; check 9+21+25+21+9 = 85.
- 16 non-singleton cells containing 76 of the 85 points; 9 singletons (max(λ2,y)=5, all at n=10).
- Cells where the value varies along the fibre: exactly (k,k) for k=1..4, varying only at the λ1=λ2 point, e.g.
  (2,2): λ=(2,2) → t²−t+2; λ1=3..8 → t²−t+1. All other 12 non-singleton cells are constant (computed).
- y > λ2 cells: one value per λ2 (λ2=1..4), namely (t−1)t^{λ2−1}.

Explanation (Day 229 Young-rule proof): X = π_k + (t−1)Σ_{j<k} t^{k−1−j} π_j with π_j = #fixed j-subsets of ρ; for 0<j≤k≤n/2,
π_j = m_xy·[j=y], which sees n only through m_xy.

## 4. FPSAC draft (`work-in-progress/fpsac2027/fpsac2027-draft.tex`)
- No occurrence of "155", "85", "λ1-free", or "independent of λ1" (grep). Nothing *needs* changing.
- Line 299 (Example [Two rows]): "in agreement with a Kostka--Foulkes computation for $|\lambda|\le10$." — accurate as is. Optional
  precision: "(all 85 pairs with $\lambda_2\ge1$, $x\ge y\ge1$, $|\lambda|\le10$)".
- Line 299 also: "On the diagonal class $(x,y)=\lambda$ it gives $t^{\lambda_2}-t^{\lambda_2-1}+m_{xy}$ ..." — consistent with the data above.
