# PROVE 257 — Conjecture 8 (`conj:T`) of the LG/OG draft: PROVED

Date: 2026-10-25. Registry: `proofs/registry/q488-converse.json`, node `q488-oc-half-step-T-ribbons`.
Draft: Prop 6.16 (prop:T), WIP 45cf937. Scripts: `proofs/scratch/prove257/` = WIP `scripts/prove257/` (`verify.py` = all identities below; `ctrl.py` = negative control).

## Problem

Strict partitions κ, ordered by inclusion of shifted diagrams D(κ) (⇔ κ_r ≥ ν_r for all r). For ν ⊆ κ put
θ = D(κ)∖D(ν). A_o(κ,ν) = [θ antichain, no diagonal box], A_e(κ,ν) = [θ antichain]. A_oA_e is the matrix
of (★) (Lemma `lem:layers`(a)), unitriangular. T := its unique unitriangular square root. Claim:

(a) s_{x+1/2} = T s_x for all x ∈ ℂ, where s_x(κ) = (−1)^{|κ|}H_κ(−x).

(b) T(κ,ν) = ∏_{components D of θ} w(D), with w = 1 (single off-diagonal box), 0 (off-diagonal, ≥2 boxes),
0 (≥2 diagonal boxes), 0 (one diagonal box, contains a 2×2 square), ε(−1/2)^{|D|} (ribbon with one diagonal
box; ε = +1 iff the left neighbour of the NE end box of D lies in D).

## Notation

Parts κ_1 > κ_2 > … > κ_ℓ > 0, κ_r := 0 for r > ℓ = ℓ(κ). κ' := (κ_2, κ_3, …). Convention for ν = ∅:
ν_1 := 0, ν' := ∅. For ν ≠ κ, r_0(κ,ν) := min{r : ν_r ≠ κ_r}.
Matrices are indexed by strict partitions and are lower triangular for inclusion (M(κ,ν) = 0 unless ν ⊆ κ);
all products are finite sums over intervals, and restricting to the down-set {parts ≤ m} is multiplicative,
so everything below holds verbatim for the draft's finite matrices.

* ζ(κ,ν) = [ν ⊆ κ]; ζ_o(κ,ν) = [ν ⊆ κ, ℓ(ν) = ℓ(κ)].
* S = diag((−1)^{|κ|}).
* X(κ,ν) = δ_{κν} − [ν≠κ][ℓ(ν)=ℓ(κ)−1] 2^{−κ_{r_0}} [ν_s ≤ κ_{s+1} for all s ≥ r_0].
* P(κ,ν) = δ_{κν} + [ν≠κ] 2^{−κ_{r_0}} [ν_s ≤ κ_{s+1} for all s ≥ r_0].

(In P the bracket forces ν ⊆ κ, r_0 ≤ ℓ(κ) and ℓ(ν) < ℓ(κ). In words: keep the first r_0−1 parts, delete
the part κ_{r_0} at cost 2^{−κ_{r_0}}, and shrink the tail; X shrinks the tail keeping its length.)

## Step 0 — Möbius identifications

Finite order ideals of the shifted plane are the D(κ) (Lemma `lem:ideals`), so (strict partitions, ⊆) is the
lattice of finite order ideals J of a poset. In a distributive lattice μ(ν,κ) = (−1)^{|θ|}[θ antichain]
([EC1, Ex. 3.9.6]: [ν,κ] is Boolean iff κ∖ν is an antichain). Hence
**ζ^{-1} = S A_e S.** The set Λ_ℓ of strict partitions of length ℓ is convex for ⊆ (ν ⊆ ρ ⊆ κ with
ℓ(ν)=ℓ(κ) forces ℓ(ρ)=ℓ(κ)), so the Möbius function of Λ_ℓ is the restriction of μ; an antichain θ with
ℓ(ν)=ℓ(κ) has no diagonal box and conversely (diagonal boxes of θ are (i,i), ℓ(ν) ≤ i < ℓ(κ)). Hence
**ζ_o^{-1} = S A_o S.** So A_oA_e = S ζ_o^{-1} ζ^{-1} S.
(Checked numerically: verify.py, m ≤ 8.)

## Step 1 — First-row recursions

For κ ≠ ∅ and all ν:

  (RX) X(κ,ν) = [ν_1=κ_1] X(κ',ν') − 2^{−κ_1} ζ_o(κ',ν),
  (RP) P(κ,ν) = [ν_1=κ_1] P(κ',ν') + 2^{−κ_1} ζ(κ',ν),

and X(∅,ν) = P(∅,ν) = δ_{∅ν}.

*Proof.* If ν_1 = κ_1 (≥1): ν ≠ ∅; ν = κ ⇔ ν' = κ'; otherwise r_0(κ,ν) = 1 + r_0(κ',ν'), the parts and
conditions shift by one, ℓ drops by one on both sides; and ζ_o(κ',ν) = ζ(κ',ν) = 0 because ν_1 = κ_1 > κ'_1.
If ν_1 ≠ κ_1: ν ≠ κ, r_0 = 1, and the bracket [ν_s ≤ κ_{s+1} ∀ s ≥ 1] is [ν ⊆ κ']; with [ℓ(ν)=ℓ(κ')]
for X. ∎

## Step 2 — Pointwise lemma

For strict ρ and ν with ν_1 ≤ ρ_1: P(ρ, ν') = 2^{−ρ_1} [ν ⊆ ρ].

*Proof.* ρ = ∅ forces ν = ∅ = ν' and both sides are 1 (2^0). If ρ ≠ ∅ then ν'_1 = ν_2 < ν_1 ≤ ρ_1
(or ν'_1 = 0 < ρ_1), so ν' ≠ ρ and r_0(ρ,ν') = 1:
P(ρ,ν') = 2^{−ρ_1}[ν_{s+1} ≤ ρ_{s+1} ∀ s ≥ 1], which together with ν_1 ≤ ρ_1 is [ν ⊆ ρ]. ∎

## Step 3 — (I2): X ζ = ζ_o P

Induction on ℓ(κ). κ = ∅: both sides δ_{∅ν}. Let κ ≠ ∅, ℓ = ℓ(κ).

LHS. By (RX), (Xζ)(κ,ν) = Σ_{ρ'} X(κ',ρ') [ν ⊆ (κ_1,ρ')] − 2^{−κ_1} (ζ_oζ)(κ',ν). (ρ' runs over all strict
partitions; X(κ',ρ') ≠ 0 forces ρ'_1 ≤ κ_2 < κ_1 so (κ_1,ρ') is strict.) Since
[ν ⊆ (κ_1,ρ')] = [ν_1 ≤ κ_1][ν' ⊆ ρ'],

  (Xζ)(κ,ν) = [ν_1 ≤ κ_1] (Xζ)(κ',ν') − 2^{−κ_1}(ζ_oζ)(κ',ν).

RHS. ρ ∈ Λ_ℓ, ρ ⊆ κ ⇔ ρ = (a,ρ') with ρ' ⊆ κ', ℓ(ρ') = ℓ−1, ρ'_1 < a ≤ κ_1. By (RP) (ρ ≠ ∅):

  (ζ_oP)(κ,ν) = Σ_{ρ'} Σ_{a=ρ'_1+1}^{κ_1} ([ν_1=a] P(ρ',ν') + 2^{−a} ζ(ρ',ν))
             = Σ_{ρ'} [ρ'_1 < ν_1 ≤ κ_1] P(ρ',ν') + Σ_{ρ'} 2^{−ρ'_1} ζ(ρ',ν) − 2^{−κ_1}(ζ_oζ)(κ',ν),

ρ' over ζ_o-range of κ' (Σ_{a=b+1}^{c} 2^{−a} = 2^{−b} − 2^{−c}).

The 2^{−κ_1} terms agree. By induction (Xζ)(κ',ν') = (ζ_oP)(κ',ν') = Σ_{ρ'} P(ρ',ν'). So it remains:

  [ν_1 ≤ κ_1] Σ_{ρ'} [ρ'_1 ≥ ν_1] P(ρ',ν') = Σ_{ρ'} 2^{−ρ'_1}[ν ⊆ ρ'].

If ν_1 > κ_1, the right side is 0 (ν ⊆ ρ' ⊆ κ' needs ν_1 ≤ κ_2). If ν_1 ≤ κ_1 it holds termwise: for
ρ'_1 ≥ ν_1 by Step 2, and for ρ'_1 < ν_1 both terms are 0. ∎

## Step 4 — (I1): X P = I

Induction on ℓ(κ); κ=∅ trivial. By (RX) then (RP) at ρ = (κ_1,ρ'):
(XP)(κ,ν) = Σ_{ρ'} X(κ',ρ')([ν_1=κ_1]P(ρ',ν') + 2^{−κ_1}ζ(ρ',ν)) − 2^{−κ_1}(ζ_oP)(κ',ν)
          = [ν_1=κ_1](XP)(κ',ν') + 2^{−κ_1}[(Xζ)(κ',ν) − (ζ_oP)(κ',ν)]
          = [ν_1=κ_1] δ_{κ'ν'} + 0 = δ_{κν}
by induction and (I2) at κ'. ∎

## Step 5 — T = S ζ_o^{-1} X S

Put T̃ := ζ_o^{-1}X. By (I2), T̃ = P ζ^{-1}. Then T̃² = ζ_o^{-1}X P ζ^{-1} = ζ_o^{-1}ζ^{-1} by (I1).
So (S T̃ S)² = S ζ_o^{-1}ζ^{-1} S = A_oA_e (Step 0). S T̃ S is unitriangular (ζ_o, X are).
Unitriangular square roots are unique: if U² = V, then for ν ⊊ κ,
V(κ,ν) = 2U(κ,ν) + Σ_{ν⊊ρ⊊κ} U(κ,ρ)U(ρ,ν), which determines U(κ,ν) by induction on |κ|−|ν|.
Hence **T = S ζ_o^{-1} X S = A_o·(S X S)**, and **T̃ ζ = P**.

## Step 6 — Part (a)

s_1 = δ_∅ (Lemma `lem:anchor`, H_∅ ≡ 1) and s_1 = A_oA_e s_0 by (★), so
s_0 = (A_oA_e)^{-1}δ_∅ = S ζ ζ_o S δ_∅, i.e. s_0(κ) = (−1)^{|κ|}(ζζ_o)(κ,∅) = (−1)^{|κ|}
(the only ρ ⊆ κ of length 0 is ∅). Then
T s_0 = S T̃ S S 𝟙 = S (T̃ζ)(·,∅) = S P(·,∅) = ((−1)^{|κ|}2^{−κ_1})_κ = s_{1/2} (Theorem `thm:A`).
T commutes with T² = A_oA_e, so for integers j ≥ 0:
s_{j+1/2} = (A_oA_e)^j T s_0 = T (A_oA_e)^j s_0 = T s_j. Entrywise both sides of s_{x+1/2} = T s_x are
polynomials in x (T is finite on the down-set of κ) agreeing at all j ∈ ℤ_{≥0}, hence for all x. ∎

(Also: this gives s_0 internally; H_κ(0)=1 is not needed as an extra input.)

## Step 7 — Part (b)

T(κ,ν) = Σ_ρ A_o(κ,ρ)(−1)^{|ρ|−|ν|}X(ρ,ν). X changes length by 0 (only the diagonal δ) or exactly 1;
A_o preserves length. Write θ = D(κ)∖D(ν).

**ℓ(ν) = ℓ(κ).** T = A_o(κ,ν) = [θ antichain]. θ is convex in the plane poset (x ≤ z ≤ y, x,y ∈ θ ⇒ z ∈ θ),
so x < y in θ gives a path of adjacent boxes in θ; thus antichain ⇔ every component is a single box.
No diagonal boxes. Matches (b).

**ℓ(ν) ≤ ℓ(κ)−2.** T = 0. θ contains the diagonal boxes of rows ℓ(ν)+1..ℓ(κ) and the boxes (i,i+1)
between them (κ_r ≥ 2 for r < ℓ(κ)), so one component has ≥2 diagonal boxes: rule gives 0. Matches.

**ℓ(ν) = ℓ(κ) − 1.** Content coordinates: box (i,j) has content j−i ≥ 0; row r of θ (1-indexed) is the
content interval [ν_r, κ_r − 1]. A box of content c in row r sits directly above the box of content c−1 in
row r+1. Hence rows r, r+1 (both nonempty) are adjacent iff ν_r ≤ κ_{r+1}; a skew shape is connected iff its
nonempty rows are consecutive and successive ones adjacent; contents of a connected skew shape form an
interval (adjacent boxes differ by ±1), so for connected ρ/ν containing the diagonal box (content 0),
#contents = max content + 1.

*Lemma (Q_1 = rim weight).* For ℓ(ν) = ℓ(ρ)−1: X(ρ,ν) = −2^{−(1+maxcontent(ρ/ν))}[ρ/ν connected].
Proof: row ℓ(ρ) is nonempty (content 0..ρ_ℓ−1). The first nonempty row is r_0(ρ,ν); rows r ≥ r_0 being
nonempty and adjacent is ν_r ≤ ρ_{r+1} (which forces ν_r < ρ_r); so connected ⇔ the bracket in X. The max
content is ρ_{r_0} − 1 (top nonempty row, contents decrease down the rows). ∎

So, with A ranging over subsets of the off-diagonal maximal boxes of θ (the off-diagonal antichains removable
from D(κ) inside θ; maximal boxes of an up-set θ are maximal in D(κ)):

  T(κ,ν) = − Σ_A (−1)^{|θ|−|A|} 2^{−(1+maxcontent(θ∖A))} [θ∖A connected].

Let D_0 be the component of θ containing the unique diagonal box d, D_1..D_k the others (off-diagonal).
θ∖A connected forces A ⊇ D_1 ∪ … ∪ D_k; a component can be removed by maximal boxes only if all its boxes
are maximal, i.e. it is a single box (two adjacent boxes are comparable). So T = 0 if some D_i (i ≥ 1) has
≥2 boxes, and otherwise T = w(D_0) with

  w(D) := − Σ_{S ⊆ M(D), D∖S connected} (−1)^{|D|−|S|} 2^{−(1+maxcontent(D∖S))},

M(D) = off-diagonal maximal boxes of D (covers are adjacencies, so maximal in θ = maximal in D).

Rows of D: r_0..ℓ, content intervals [a_r, b_r] (a_r = ν_r, b_r = κ_r − 1), a, b strictly decreasing,
a_ℓ = 0, adjacency a_r ≤ b_{r+1} + 1. A maximal box is a row end; the end of row r is maximal iff r = ℓ or
b_{r+1} ≤ b_r − 2. D has a 2×2 square iff a_{r−1} ≤ b_r for some r ∈ (r_0, ℓ] (overlap ≥ 2 columns).

*Non-ribbon ⇒ w(D) = 0.* Let r* be the largest r ∈ (r_0,ℓ] with a_{r−1} ≤ b_r, x the end of row r*.
x is maximal: else b_{r*+1} = b_{r*} − 1 and a_{r*} < a_{r*−1} ≤ b_{r*} gives a_{r*} ≤ b_{r*+1},
contradicting the choice of r*. x ≠ d (content b_{r*} ≥ a_{r*−1} = ν_{r*−1} ≥ 1). S ↦ S △ {x} preserves
validity: row r* stays nonempty (a_{r*} ≤ b_{r*} − 1); the adjacency (r*−1, r*) holds both ways
(a_{r*−1} ≤ b_{r*}); row r*−1 has ≥ 2 boxes (a_{r*−1} ≤ b_{r*} < b_{r*−1}) so is never emptied; adjacency
(r*, r*+1) involves only a_{r*}. The max content is unchanged: row r*−1 is nonempty with end
≥ b_{r*−1} − 1 ≥ b_{r*}. The sign flips. So w(D) = 0.

*Ribbon (a_{r−1} = b_r + 1 for all r ∈ (r_0,ℓ]).* One box per content, |D| = b_{r_0} + 1. If S contains
the end of a row r > r_0 then the adjacency (r−1,r) fails unless rows r_0..r−1 are all emptied, which needs
row r_0 = {e} removable; but a single-box top row in a ribbon sits directly above the end of row r_0+1
(a_{r_0} = b_{r_0} = b_{r_0+1}+1), so e is not maximal. Hence S ⊆ {e} ∩ M(D). In a ribbon, e ∈ M(D) iff
row r_0 has ≥ 2 boxes (for r_0 < ℓ: b_{r_0+1} = a_{r_0} − 1 ≤ b_{r_0} − 2 ⇔ a_{r_0} < b_{r_0}; for r_0 = ℓ:
e ≠ d) iff the left neighbour of e lies in D, i.e. ε = +1. D∖{e} is a connected ribbon with max content
b_{r_0} − 1. So
  w(D) = −(−1)^{|D|}2^{−|D|} − [ε=+1](−1)^{|D|−1}2^{−(|D|−1)} = (−½)^{|D|}(−1 + 2[ε=+1]) = ε(−½)^{|D|}.
(D = {d}: ε = −1, w = ½.) ∎

## Verification

* `verify.py m`: X, P by the sequence formulas; (I1), (I2), Möbius identities (Step 0), (S T̃ S)² = A_oA_e,
  S T̃ S = printed rule (b), T s_0 = s_{1/2}: all True for m = 4,5,6,7,8 (m=8: 256 partitions). For m ≤ 6
  also S T̃ S = binomial-series T (the Wake-257 computation) exactly.
* Negative control `ctrl.py` (X weight ×3/2 for ℓ ≥ 2): every identity fails.
* Before the proof: Q_1 = ζ_o T̃ − I = −2^{−|rim θ|}[connected, length drop 1] found from data (qform.py,
  m ≤ 6, 0 failures); P = T̃ζ read off from data (pq.py).

## Gaps

None in the argument. External inputs: (★)/Lemma `lem:layers`(a), Lemma `lem:anchor`, Theorem `thm:A`
(only for (a)); EC1 Ex. 3.9.6 (Möbius function of a distributive lattice — textbook). Part (b) and
T² = A_oA_e use only Step 0 + combinatorics.

## What it means

T is not a Murnaghan–Nakayama operator; it is A_o·(I + SQ_1S): "remove an off-diagonal antichain, then
(with weight −(−1)^{|θ|}2^{−κ_{r_0}}) delete one part and shrink the tail". The half-step is the
length-changing piece; the integer step A_oA_e = Sζ_o^{-1}ζ^{-1}S is a product of two Möbius functions, and
T̃ζ = P, T̃ = ζ_o^{-1}X: the square root factors as (Möbius of Λ_ℓ)·X = P·(Möbius of Λ). X P = I is the
whole content.
