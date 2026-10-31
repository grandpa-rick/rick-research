# Q54 — Antichain pairs in LG(m,2m) are Pell, refined by |S| ↔ runs of 2s

PROVE 267, written 2026-10-31. Status: **PROVED**. Bounded jewel. The draft stays frozen and nothing from here goes into it.

## Statement

The shapes are the subsets λ ⊆ {1..m}, i.e. the strict partitions λ_1 > λ_2 > … > λ_ℓ ≥ 1 with λ_1 ≤ m. The shifted diagram is
D(λ) = {(i,j) : 1 ≤ i ≤ ℓ, i ≤ j ≤ i+λ_i−1}. Cells carry the product order (i,j) ≤ (k,l) ⇔ i≤k, j≤l.
A pair (ρ,λ) with D(ρ) ⊆ D(λ) is an *antichain pair* if S = D(λ)∖D(ρ) is an antichain (S = ∅ is allowed). Define A_m(t) = Σ t^{|S|} over the antichain pairs.

**Theorem (Q54).** A_m(t) = Σ_{w∈W_m} t^{r_2(w)}. Here W_m ⊆ {0,1,2}^m is the set of words with no adjacent 12 or 21, and r_2(w) is the number of maximal runs of 2s in w. More precisely,

  A_m(t) = Σ_{x∈{0,1}^m} (1+t)^{r_1(x)} = Σ_{r≥0} C(m+1,2r) (1+t)^r,

and in particular A_m(1) = ((1+√2)^{m+1} + (1−√2)^{m+1})/2 = 3, 7, 17, 41, 99, 239, 577, 1393, … (Pell recurrence a_m = 2a_{m−1}+a_{m−2}), and A_m(0) = 2^m.

The whole proof is one observation: **an antichain skew is a set of corners, and the corners of a shifted shape are the runs of consecutive parts.**

## Proof

Let T_m = {(i,j) : 1 ≤ i ≤ j ≤ m} be the shifted staircase, with the product order.

**Lemma 0. The shifted diagrams D(λ), λ ⊆ {1..m}, are exactly the order ideals of T_m.**
*D(λ) is an ideal.* We have D(λ) ⊆ T_m because i+λ_i−1 ≤ m, which holds since λ_i ≤ m−i+1 by strictness. Take (k,l) ∈ D(λ) and (i,j) ∈ T_m with i≤k and j≤l. Then
j ≤ l ≤ k+λ_k−1 ≤ i+λ_i−1, using λ_k ≤ λ_i−(k−i). Also j ≥ i, so (i,j) ∈ D(λ).
*Every ideal I is a D(λ).* Row i of I is down-closed in j and contains (i,i) whenever it is nonempty, since (i,i) ≤ (i,j). So it is an interval [i, i+r_i−1].
If row i is nonempty then (i−1,i) ≤ (i,i) lies in I, so row i−1 is nonempty. If (i, i+r_i−1) ∈ I then (i−1, i+r_i−1) ∈ I, so r_{i−1} ≥ r_i+1. Hence (r_i) is a
strict partition, its parts are ≤ m because the cells lie in T_m, and I = D(r). ∎

**Lemma 1. If D(ρ) ⊆ D(λ), then S = D(λ)∖D(ρ) is an antichain iff S ⊆ max D(λ), where max D(λ) is the set of maximal elements of D(λ). Conversely, every subset S ⊆ max D(λ) arises from exactly one ρ.**
(⇒) Take s ∈ S and t ∈ D(λ) with s < t. The ideal D(ρ) (Lemma 0) does not contain s, so it does not contain t. Then t ∈ S and s < t, which contradicts the antichain property.
So s is maximal.
(⇐) A subset of max D(λ) is an antichain. Given S ⊆ max D(λ), the set D(λ)∖S is still down-closed: if t ∈ D(λ)∖S and s ≤ t with s ∈ T_m, then
s ∈ D(λ), and s ∉ S, because s ∈ S would force s = t by maximality. By Lemma 0 it equals D(ρ) for a unique ρ. ∎

So A_m(t) = Σ_λ Σ_{S ⊆ max D(λ)} t^{|S|} = Σ_λ (1+t)^{c(λ)}, where c(λ) = |max D(λ)|.

**Lemma 2 (corners = runs).** max D(λ) = {(i, i+λ_i−1) : λ_i−1 ∉ λ}, with the convention 0 ∉ λ. Hence c(λ) = r_1(x(λ)), the number of maximal runs of
1s in the indicator word x(λ) ∈ {0,1}^m with x_k = [k ∈ λ].
*Proof.* A maximal cell must end its row, because (i,j+1) ∈ D(λ) would lie above it. So the candidates are e_i = (i, i+λ_i−1). If some t = (k,l) ∈ D(λ) satisfies t > e_i, then k > i. When l > j := i+λ_i−1 this is impossible, since then (i,j+1) ≤ t lies in T_m and hence in D(λ), contradicting the end of row i. So l = j, and then (i+1, j) ≤ t lies in T_m and hence in D(λ).
So e_i is non-maximal iff (i+1, i+λ_i−1) ∈ D(λ). That requires row i+1 to exist with i+λ_{i+1} ≥ i+λ_i−1, which by strictness means λ_{i+1} = λ_i−1,
i.e. λ_i−1 ∈ λ. If λ_i = 1 the cell (i+1,i) is not in T_m, and indeed 0 ∉ λ. So the corners are the parts k with k−1 ∉ λ, which are exactly the bottoms of the maximal runs of consecutive parts. ∎

**Bijection.** Let Φ(λ,S) be x(λ) with every maximal 1-run whose corner lies in S recoloured from 1 to 2. Each corner belongs to exactly one run, the one with bottom part k and corner in the row of part k. The words of W_m are exactly the words in {0,1,2}^m whose maximal nonzero blocks are monochromatic, because a non-monochromatic block contains an adjacent 12 or 21. Such a word is determined by its support x ∈ {0,1}^m together with the set of blocks coloured 2. So Φ is a bijection from {(λ, S ⊆ max D(λ))} to W_m with r_2(Φ(λ,S)) = |S|. Combined with Lemma 1, this gives the Theorem. ∎

**Closed form.** There are C(m+1,2r) binary words of length m with r runs of 1s: pad with a 0 at each end, and the 2r run boundaries are a choice among the m+1
gaps. So A_m(t) = Σ_r C(m+1,2r)(1+t)^r. At t=1 this is Σ_r C(m+1,2r) 2^r = ½[(1+√2)^{m+1}+(1−√2)^{m+1}], the Pell–Lucas half-companion numbers. At t=0 it is
Σ_r C(m+1,2r) = 2^m.
Check at m=6: Σ_r C(7,2r) C(r,s) = 64, 112, 56, 7 for s = 0..3, which matches Wake 267's data.

## Verification

`proofs/prove267/q54_bijection_check.py` (output in `q54_bijection_check.out`) checks, for m = 1..8:
Lemma 1 in both directions, Lemma 2 (both the corner set and the count), that Φ lands in W_m with r_2 = |S|, and that Φ is injective with image all of W_m.
All True: 3, 7, 17, 41, 99, 239, 577, 1393. This agrees with the brute-force separator `q54_separator.py`, which was implemented independently.

## Remarks

- The "one local exclusion rule" in W_m is simply that a run gets one colour. The Pell growth comes from 2^{#runs}, not from any vertex-model R-matrix. So
  Q54 gives **no** evidence for the Q51 R-matrix hunch. The transfer matrix is trivial: it is the run-counting matrix [[1,1],[1+t,1]] on states {0, nonzero}.
- The content is Lemma 1 (antichain skew ⇔ subset of corners), which holds for any order ideal in any poset, plus Lemma 2 (shifted corners = bottoms of runs of consecutive parts). This is the same mechanism as Q48 Lemma A: antichain pairs are "remove any set of corners", i.e. dn(z_ρ, z_λW_J) = z_λ exactly when ρ is λ with some corners removed.
- Ownership: Σ_λ(1+t)^{c(λ)} over the strict partitions in a box is folklore-grade. Nothing here is a claim of novelty. It is a jewel for the proofs/ shelf only.

## Gaps

None.
