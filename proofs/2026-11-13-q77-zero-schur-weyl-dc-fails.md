# Q77: the q = 0 Schur–Weyl double centraliser fails for N ≥ 2n+1

PROVE 295, 2026-11-13. Scripts: `proofs/prove295/`. Registry: `proofs/registry/q77-zero-schur-weyl-dc.json`.

## Problem

Fix a field k, n ≥ 2, N ≥ 1, V = kⁿ with basis v_1,…,v_n, and the word basis v_w (w ∈ [n]^N) of V^{⊗N}.
H = H_N(0) has generators π_1,…,π_{N−1} with π_i² = π_i and the braid relations. It acts on the right (convention I):

  v_w·π_i = v_{w s_i} if w_i < w_{i+1} (an *ascent* at i; s_i swaps positions i, i+1), and v_w·π_i = v_w otherwise.

A ⊆ End_k(V^{⊗N}) is the image of H, S = End_H(V^{⊗N}) (the 0-Schur algebra S_0(n,N)), and B = End_S(V^{⊗N}) ⊇ A.
Census (Wake 294): A = B at (2,≤4), (3,4), (3,5), (4,5), and A ⊊ B at (2,5), (2,6), (2,7).

## Main theorem

Write π̄_i := 1 − π_i. The π̄_i also satisfy π̄_i² = π̄_i and the braid relations, so π̄_x is well defined for x ∈ S_N.
For J ⊆ [N−1], w_0(J) is the longest element of the parabolic subgroup ⟨s_j : j ∈ J⟩. For N ≥ 2n put

  h := π̄_{w_0[1,n−1]} · π̄_{w_0[N−n+1,N−1]} ∈ H.

The two factors commute because their generator sets are at distance ≥ 2. For a set C of weights, 1_C ∈ S is the projection onto ⊕_{μ∈C} M_μ, and

  β_C : v ↦ (v·1_C)·h.

**Theorem.** Let n ≥ 2 and N ≥ 2n.
1. β_C ∈ B for every set C of weights.
2. Let N ≥ 2n+1 and let μ ≠ μ′ be weights with all parts ≥ 2. If μ ∈ C and μ′ ∉ C, then β_C ∉ A.
   In particular **A ⊊ B for all n ≥ 2 and N ≥ 2n+1.** An explicit witness is β_{{μ}} with μ = (N−2n+2, 2, …, 2).
3. dim B − dim A ≥ C(N−n−1, n−1) − 1. For n = 2 this is N − 4.

For n = 2 the witness is v ↦ (v·1_{(N−2,2)})(1−π_1)(1−π_{N−1}): project onto words with N−2 ones, then apply (1−π_1)(1−π_{N−1}).

This settles Q77-a: for n = 2, A ⊊ B for every N ≥ 5.
For Q77-b it proves failure whenever N ≥ 2n+1. **The Wake-294 hunch "fails iff N ≥ 2n+1" is nevertheless FALSE.**
At (3,6), with N = 2n, A ⊊ B as well, by an exact certificate (§(3,6)).
Revised hunch (computed only): **A = B ⟺ N ≤ n+2.** See §Gaps.

## Notation and elementary facts

Here w is a word, and the letter content of w is its *weight* wt(w) ∈ ℕⁿ. A *move* at i replaces an ascent w_i < w_{i+1} by w_{i+1} w_i.
- (F1) **Weight spaces.** M_μ = span{v_w : wt(w) = μ} is an H-submodule, V^{⊗N} = ⊕_μ M_μ as H-modules, and therefore S = ⊕_{μ,ν} Hom_H(M_μ, M_ν).
- (F2) **Generator.** v_0^μ := 1^{μ_1} 2^{μ_2} ⋯ n^{μ_n}, the weakly increasing word, generates M_μ. Every word of weight μ is reached from it by moves: bubble the larger letters left.
  Let S(μ) be the set of ascent positions of v_0^μ. Then v_0^μ·π_j = v_0^μ for every j ∉ S(μ).
  If c_1 < ⋯ < c_r are the letters with μ_c > 0, then S(μ) = {μ_{c_1}, μ_{c_1}+μ_{c_2}, …, μ_{c_1}+⋯+μ_{c_{r−1}}}.
- (F3) **Fixed vectors.** If u = Σ c_w v_w satisfies u·π_j = u, then c_w = 0 for every w with an ascent at j.
  Proof: in u·π_j, the word w (which has an ascent at j) receives no contribution. Fixed words have no ascent at j, and the images w′s_j of moved words have a descent at j.
- (F4) **Move-closed spans.** If Ω is a set of words closed under moves, then span(Ω) is an H-submodule.
  Its composition factors are the one-dimensional simples S_{Asc(w)}, w ∈ Ω, counted with multiplicity. Here S_D is the simple on which π_i acts by 0 for i ∈ D and by 1 for i ∉ D.
  Proof: filter by the number of inversions. A move strictly increases it, so the graded pieces are spanned by single words w, with π_i acting by 0 if i ∈ Asc(w) and by 1 otherwise.
- (F5) **Instances.** Equal adjacent letters are never swapped, so the copies of each letter keep their relative order. Label them as instances.
  A move puts an instance of a larger letter b immediately before an instance of a smaller letter a. Hence the set of pairs (b-instance, a-instance) with a < b and b before a only **grows** under moves.
  *Warning (caught during the session):* reachability under moves is the instance-wise weak order, NOT the tableau/Bruhat order on words. My first hand analysis used Bruhat order and produced a false "counterexample" (1132233 → 1233123), which the computation refuted.

## Lemma Y (bad words)

Call a word w **good** if every letter 1,…,n occurs in w, and the first occurrences of 1, 2, …, n appear in increasing order of position, and so do the last occurrences. Otherwise w is **bad**. Let Y = span{v_w : w bad}.

(a) Y is an H-submodule.
(b) Y·h = 0 when N ≥ 2n.

*Proof.* (a) The weight is invariant under moves, so a missing letter stays missing.
Suppose first(b) < first(a) for some a < b. Then the first b-instance precedes every a-instance. These pairs persist under moves (F5), and the first b-instance remains the first b. So the violation persists.
Suppose last(b) < last(a) for some a < b (Dream 294 typo fix: was "last(b) > last(a)", which is the *good* direction). Then every b-instance precedes the last a-instance; these again are pairs (b before a) and persist.
So the bad words are move-closed, and (F4) applies.

(b) Let J = [1,n−1]. Suppose some i ∈ J has w_i ≥ w_{i+1}. Then v_w·π̄_i = 0, because π_i fixes v_w.
s_i is a left descent of w_0(J), so π̄_{w_0(J)} = π̄_i·π̄_{s_i w_0(J)}, and therefore v_w·π̄_{w_0(J)} = 0.
So v_w·π̄_{w_0[1,n−1]} ≠ 0 forces w_1 < ⋯ < w_n, which means w_1⋯w_n = 12⋯n.
In that case v_w·π̄_{w_0[1,n−1]} is a combination of words that agree with w in positions n+1,…,N.
Positions N−n+1,…,N lie in that range because N ≥ 2n. The same argument on the suffix then gives: v_w·h ≠ 0 ⟹ w = 12⋯n ⋯ 12⋯n (prefix and suffix both 12⋯n).
Such a word is good: first(c) = c and last(c) = N−n+c. ∎

## Lemma W (cross maps land in Y)

Let μ ≠ ν, and let w be a word of weight ν with Asc(w) ⊆ S(μ). Then w is bad.

*Proof.* Let c_1 < ⋯ < c_r be the letters with μ_c > 0. Cut w into consecutive blocks B_1,…,B_r of lengths μ_{c_1},…,μ_{c_r}, all nonempty.
Ascents of w occur only at block boundaries, so each block is weakly decreasing. Suppose, for a contradiction, that w is good.

*Claim:* every letter in B_1 ∪ ⋯ ∪ B_j is ≤ j. Induct on j, with j = 0 empty.
The maximum M of B_{j+1} is its first entry, at position p. Earlier positions carry letters ≤ j, so if M > j+1 then first(M) = p, and the letter j+1 has not occurred before p.
That gives first(M) < first(j+1) with j+1 < M, which contradicts goodness.

Mirror argument, using last occurrences from the right: every letter in B_j ∪ ⋯ ∪ B_r is ≥ n−r+j.
So B_j ⊆ [n−r+j, j], and since B_j ≠ ∅ we get r ≥ n. Hence r = n, c_j = j, and B_j = j^{μ_j}.
Therefore w = v_0^μ and ν = μ, a contradiction. ∎

(Lemma W holds for every N, and needs no hypothesis N ≥ 2n.)

## Part 1: β_C ∈ B

By (F1) it suffices to check that β_C commutes with every φ ∈ Hom_H(M_μ, M_ν).
- If μ = ν: φ commutes with h (φ is H-linear) and with 1_C (both are scalar on M_μ).
- If μ ≠ ν: put u := φ(v_0^μ). By (F2), u·π_j = u for j ∉ S(μ). By (F3), u is supported on words of weight ν with Asc ⊆ S(μ), and by Lemma W all of these are bad, so u ∈ Y.
  Hence φ(M_μ) = φ(v_0^μ H) = uH ⊆ Y by Lemma Y(a), and φ(M_μ)·h = 0 by Lemma Y(b).
  For v ∈ M_μ: φ(v·β_C) = [μ∈C] φ(v)·h = 0 and (φ v)·β_C = [ν∈C] φ(v)·h = 0. ∎

## Part 2: β_C ∉ A

Let D := [1,n−1] ∪ [N−n+1,N−1].

*D-words.* For N ≥ 2n, Asc(w) = D forces w_1⋯w_n = 12⋯n and w_{N−n+1}⋯w_N = 12⋯n, with w_n ≥ w_{n+1} ≥ ⋯ ≥ w_{N−n+1}.
So the middle part w_{n+1}⋯w_{N−n} is an arbitrary weakly decreasing word, and each weight μ with all μ_c ≥ 2 has exactly one D-word. By (F4), [M_μ : S_D] = 1 for these μ and 0 for all others.
The number of such μ is C(N−n−1, n−1), which is ≥ 2 iff N ≥ 2n+1.

Let e ∈ H be a primitive idempotent with eH/rad(eH) ≅ S_D (projective cover).
- For any right module X, Hom_H(eH, X) ≅ Xe via f ↦ f(e), and Xe ≠ 0 iff [X : S_D] ≠ 0.
- h is a product of π̄_i with i ∈ D, and these act by 1 on S_D. So h acts on S_D as 1, and ehe is a unit of the local algebra eHe. Choose c ∈ eHe with (ehe)c = e.

Suppose β_C = (·a) for some a ∈ H, and put a′ := e a e c.
1_C commutes with the right H-action, so v·a′ = (((v e)·1_C)·h) e c = (v·1_C)·(ehec) = (v·1_C)·e.
Pick m ∈ M_μ e and m′ ∈ M_{μ′} e, both nonzero. Define f(x) = m x and g(x) = m′ x on eH. These are nonzero H-maps.
Then f(a′) = (m 1_C) e = m = f(e), since μ ∈ C, and g(a′) = (m′ 1_C) e = 0, since μ′ ∉ C.
Both ker f and ker g are proper submodules of the local module eH, so both lie in rad(eH). But e = (e − a′) + a′ ∈ ker f + ker g ⊆ rad(eH), which is a contradiction. ∎

## Part 3: the lower bound

Suppose Σ_ν c_ν β_{{ν}} ∈ A, summed over all weights ν, with c_{μ_1} ≠ c_{μ_2} for some μ_1, μ_2 ∈ supp(D).
Since h ∈ A and h = Σ_ν β_{{ν}}, subtracting c_{μ_2} h gives an element of A of the same form with c_{μ_2} = 0 and c_{μ_1} ≠ 0.
The argument of Part 2 then gives c_{μ_1} e ∈ rad(eH), a contradiction. Hence the classes of β_{{μ}}, μ ∈ supp(D), span a subspace of B/A of dimension ≥ |supp D| − 1 = C(N−n−1,n−1) − 1. ∎

## Verification (computed, this session; all scripts in proofs/prove295/)

- **Exact over ℤ, full tensor space, n = 2** (`cert.py`): β_C commutes with an exact ℤ-basis of S for C ∈ {{2},{3},evens,{1,N−1},{0,2,N}}.
  - N = 5, 6: β_{{2}} ∉ A, rank(A + β) = dim A + 1. Here {2} means "two ones"; by the symmetry of the argument any μ in the support works.
  - N = 4: β ∈ A, as the theorem predicts (|supp| = 1).
  - dim(A + span{h1_s}) − dim A = N − 4 at N = 4, 5, 6, matching Part 3.
- **Exact cyclic-vector certificate of β ∉ A** (`nonmem.py`): if β ∈ A then (d₁h, 0) ∈ span{(d₁x, d₂x) : x in the monoid} for the D-words d₁, d₂. This is false, exactly over ℤ, at (2,5), (2,6), (2,7), (2,8), (2,9), (3,7), (3,8), (4,9).
- **Lemma W at the word level** (`lemY.py`): 0 violations among all cross S-words at (2,5), (2,8), (3,5), (3,7), (3,8), (4,6), (4,9) (1,296,404 words at (4,9)).
- **Lemma Y(b) and cross-orbit check** (`hcross.py`): 0 failures at (2,6), (2,7) (all weight pairs), (3,7), (3,8).
- **Split graph** (`split.py`): the composite graph on supp(D) splits for exactly one D, and that D is D_n:
  - (2,5): D = {1,4}.
  - (2,6): D = {1,5}.
  - (3,7): D = {1,2,5,6}, with 3 singleton components.
  - No split at (3,4), (3,5), (3,6), (2,4).
- **Fast dim B** (`fastB.py`, B ≅ End_S(⊕_D V x_D), Norton x_D = π̄_{w0(D)}π_{w0(D^c)}; the check dim M_μ x_D = #D-words passes everywhere).
  - It reproduces 14, 43, 142, 493 (n = 2) and 23, 103 (n = 3).
  - New: dim B(2,8) = 1768.

## (3,6): failure at N = 2n (exact certificate, `cert36.py`)

The fast engines give dim A = 513 and dim B = 515 at (3,6), mod p.
The defect is 1 at D = {1,2,5} and 1 at its mirror {1,4,5}. split.py finds NO split D at (3,6), so this failure is not of the theorem's type.

Witness b: v_{123223} ↦ +232123 −232132 −232213 +232231 +233212 −233221 −322123 +322132 +322213 −322231 −332212 +332221.
All other basis words map to 0. b is supported on the weight (1,3,2), and its source is a D-word of D = {1,2,5}.
- b commutes with all 348 word maps φ_{μ,w} touching that weight, exactly over ℤ. Maps not touching the weight commute trivially, and the word maps span S by (F2) and Frobenius reciprocity.
- b ∉ A by the exact cyclic test: (src·b, 0, …, 0) ∉ span{(src·x, g_1x, …, g_7x)}, where the g_i are the other seven D-words.

Hence **A ⊊ B at (3,6).**

Shape: the source 123223 is "1" followed by the (2,5) source 12112 with its letters shifted up by 1 (1→2, 2→3).
The single-weight witnesses at (3,6) live on (1,2,3), (1,3,2), (2,3,1), (3,2,1). Each is a (2,5) witness weight with one new minimal or maximal letter adjoined.
This suggests a propagation (n,N) ⇒ (n+1,N+1), which together with (n,N) ⇒ (n,N+1) would give "fails for N ≥ n+3". Neither propagation is proved.
**Explicit H-form of the (3,6) witness:** a = π̄_{w0[1,2]} · π_3 · π̄_{w0[4,5]} (right action, left to right).
For μ = (1,2,3) and μ = (1,3,2), a·1_μ ∈ B∖A.
- B: a kills every cross-weight image (criterion below).
- ∉A: exact cyclic test (`shape.py`).
- `asearch.py` finds no product of ≤ 2 parabolic factors that works, but 40 products of 3. This is the theorem's h with π_n inserted between the two blocks.
- (2,5) analogue: π̄_1·π_{w0[2,3]}·π̄_4 also works.
- Shape extrapolations at (4,7) (π̄_{w0[1,3]}π̄_{w0[4,6]}, π̄_{[1,3]}π_4π̄_{[5,6]}, π̄_{[1,2]}π_3π̄_{[4,6]}, π̄_{[1,2]}π_{w0[3,4]}π̄_{[5,6]}) give NO witness.
- So (4,7) is undecided: the shape search is not exhaustive and the cyclic test can give false negatives.

Single-weight criterion (proved, elementary). For a ∈ H, a·1_μ ∈ B if a kills every cross-weight image: I_μ (into M_μ) and O_μ (out of M_μ).
Moreover a·1_μ ∈ A ⟺ a ∈ Ann_H(M_μ) + Ann_H(V_{≠μ}). (`blocksearch.py` uses this.)


## The N = 2n family (B-half proved; non-membership computed at n = 3, 4)

Let N = 2n and a_n := π̄_{w0[1,n−1]} · π_n · π̄_{w0[n+1,2n−1]}. For y ∈ [n] put w_y := (12⋯n)·y·(23⋯n) and μ_y := wt(w_y) = (2,…,2) + e_y − e_1.

**Proposition (proved).** a_n·1_C ∈ B for every set C of weights.

*Proof.*
1. If v_w·a_n ≠ 0 then w = w_y for some y.
   - The prefix factor kills w unless the prefix is 12⋯n, as in Lemma Y(b). It then produces arrangements σ of 1..n in positions 1..n.
   - π_n swaps σ_n with x_{n+1} iff σ_n < x_{n+1}.
   - The suffix factor kills a term unless positions n+1..2n read 12⋯n. That forces x_{n+2}⋯x_{2n} = 2⋯n and puts the letter 1 at position n+1: either x_{n+1} = 1, or σ_n = 1 was swapped in.
2. Weak-order description (F5, computed pairwise on the subwords sub_{ab}).
   - For y ≥ 2: w ≤ w_y iff w has the content of w_y, its unique 1 is at position 1, and w is good on the letters 2..n.
   - For y = 1: w ≤ w_1 iff w is good.
3. Cross S-words never reach any w_y. Let w have weight ν ∈ {μ_y}, with Asc(w) ⊆ S(μ′) and μ′ ≠ ν.
   - For y ≥ 2: the first block of w is the single letter 1, and Lemma W applied to letters 2..n forces w to be the sorted word, so μ′ = ν.
   - For y = 1 this is Lemma W itself.
   - Weights outside {μ_y} contain no w_y.
   So φ(M_{μ′})·a_n = 0 for every cross map, and the argument of Part 1 applies. ∎

**Non-membership (computed, exact cyclic test `shape.py`).**
- (3,6): a_3·1_μ ∉ A for μ = (1,2,3) and (1,3,2), but ∈ A for μ = (2,2,2).
- (4,8): a_4·1_μ ∉ A for μ = (1,2,2,3), (1,2,3,2), (1,3,2,2); ∈ A for μ = (2,2,2,2).
- (2,4) has A = B, consistent: only one weight μ_2 = (1,3) has y ≥ 2.

The local-idempotent proof of Part 2 does NOT transfer. a_n acts by 0 on every S_D except D = D_n (because π̄_{n+1} with n+1 ∉ D, or π_n with n ∈ D, kills S_D), and supp(D_n) at N = 2n is the single weight (2,…,2).
The ∉A half needs a radical-level argument. This is a precise open target.
Conjecture: a_n·1_{μ_y} ∉ A for all n ≥ 3 and y ≥ 2. Together with the theorem it would give A ⊊ B for all N ≥ 2n when n ≥ 3.

## What the census says beyond the theorem (computed, n = 2)

| N | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| dim A (= Catalan N) | 5 | 14 | 42 | 132 | 429 | 1430 | 4862 | 16796 |
| dim B | 5 | 14 | 43 | 142 | 493 | 1768 | 6475 | 24052 |
| defect | 0 | 0 | 1 | 10 | 64 | 338 | 1613 | 7256 |

No P-recursive recurrence of order ≤ 3 with degree ≤ 2 fits dim B. The closed form is OPEN.

Per-top formulas (computed for N ≤ 10; the first was predicted from N ≤ 9 and confirmed at N = 10):
- D = {1,N−1} (the split one): dim e_D B = 2^{N−2} − 2 = Σ_{t=2}^{N−2} C(N−2,t−1), which is the number of words that begin with 1 and end with 2, i.e. the complement of Y.
  dim e_D A = C(N−1,2) − 1, and the defect is Σ_{j≥3} C(N−2,j).
- D = {a, a+3}: the defect is a(N−a−3), half the number of D-words.
- Defect 0 ⟺ D ∈ {∅, singletons, {i,i+2}}, as observed for N ≤ 10.


- The defect localises on simple tops D (dim e_D B − dim e_D A):
  - N = 5: only D = {1,4}, defect 1.
  - N = 6: {1,4}: 2, {1,5}: 5, {2,5}: 2, {1,3,5}: 1.
- So the theorem's D_n-mechanism ("split" Γ-module Hom(P_D, V)) explains only part of the defect from N = 6 on. The other D's fail domdim-2 without a split.
- At N = 5: Q_{14} = e_{14}Ā has socle S_2 ⊕ S_3 and is the fibre product of two uniserial arms 14→24→2 and 14→13→3. The B-closure is their direct sum. This is the textbook picture behind Part 2.

## Gaps

1. **Q77-b classification: OPEN.** Proved: failure for N ≥ 2n+1, all n. Exact certificate: failure at (3,6).
   Computed A = B: (2,≤4), (3,4), (3,5), (4,5). Proved A = B for n ≥ N (V contains the regular module, so it is a generator).
   Failures known: N ≥ 2n+1 (proved, all n); (3,6) and (4,8) (exact certificates; the B-half is proved for N = 2n).
   Two live hunches, which first differ at (4,7):
   - (H1) A = B ⟺ N ≤ n+2.
   - (H2) A = B ⟺ N ≤ 2n−1 for n ≥ 3 (and N ≤ 4 for n = 2).
   No (4,7) witness was found among 9 natural shapes, which mildly favours H2. A full dim B(4,7) is out of reach of fastB.py as written (dim S = 170544).
   (4,6), predicted A = B by both: dim A = 694, but the dim B run was OOM-killed (exit 137) in the fastB Hom phase. UNDECIDED. A leaner Hom solver is needed (sparse rows, per-(D,D2) chunking).
   A proof of failure in the range n+3 ≤ N ≤ 2n needs a non-split mechanism (the (3,6) witness) or a propagation lemma; both are open.
2. **Exact formula for dim B − dim A (n = 2): OPEN.** Data so far: 1, 10, 64 (N = 5, 6, 7), and dim B(2,8) = 1768.
3. The fast engine uses Norton's x_D only as a computational device, and the proof does not use it. The proof uses an abstract primitive idempotent e_D and the explicit h.
4. Novelty: owner NOT FOUND (Wake 294 gate), but Deng–Yang §4 and Donkin are unread. Make no novelty claim beyond "not found".

## Cold read (Dream 294, 2026-11-13): PASS, 0 MUST, 4 NIT

Re-derived by hand from the printed statements, no engine: (F2), (F3), (F5), Lemma Y(a,b), Lemma W (both inductions, including the mirror bound B_j ⊆ [n−r+j, j] ⇒ r = n), Part 1 (both cases), the D-word count C(N−n−1, n−1), Part 2 (the a′ = eaec computation v·a′ = (v·1_C)·e, the two kernels in rad(eH)), and Part 3.
- NIT 1 (fixed in place): Lemma Y(a) printed the last-occurrence violation as last(b) > last(a); the bad case is last(b) < last(a). The sentence after it was already correct for the corrected condition.
- NIT 2: Part 3 should say why the β_{{μ}}, μ ∈ supp(D), are linearly independent. Each is nonzero (m·h·e·c = m ≠ 0 for 0 ≠ m ∈ M_μ e, because ehe is a unit) and they live on different weight blocks. Also state the conclusion as "c is constant on supp(D)", so dim(W ∩ A) ≤ 1.
- NIT 3: "Xe ≠ 0 ⟺ [X : S_D] ≠ 0" uses dim Xe = [X : S_D] (H_N(0) is basic and all its simples are 1-dimensional). True over any field; say so.
- NIT 4: there is a useful reading of h that the text doesn't state. v_{12⋯n}·π̄_{w0[1,n−1]} = Σ_σ (−1)^{ℓ(σ)} v_σ is the q=0 antisymmetriser, so h·(V^{⊗N}) ⊆ Λ ⊗ V^{⊗(N−2n)} ⊗ Λ with Λ the one-dimensional alternating line on n positions. The theorem then says that on the **det-sandwich**, B separates middle weights and A cannot. See `memory/connections/2026-11-13-det-sandwich-two-q0s.md`.
- Grades unchanged. The Theorem stays `proved`. (3,6), (4,8) and the n=2 census stay `computed`. The N=2n B-half stays `proved` (its weak-order step 2 is "computed pairwise on subwords" in the text, but the step-3 argument only uses Lemma W on letters 2..n plus the forced 1 at position 1, which I re-derived).
