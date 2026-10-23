# (Z), the vanishing half of the odd-zero law, for every κ: hyperplane-section induction (PROVE 252)

Rick, 2026-10-23 (PROVE 252; the file name is the date PROVE.md asked for). Conventions are those of
`proofs/2026-10-23-odd-zero-law.md`: X_κ ⊂ LG(m,2m) has dimension |κ|, and H_κ(j) := χ(X_κ, O(j)), which is a polynomial
in j (Snapper). Scripts are in `work-in-progress/scripts/wake252/caseB/` (files `prove252_*.py`).

## 0. Verdict

| item | statement | grade |
|---|---|---|
| **Lemma S** (reflection) | D(κ^∨) = R(Δ_m ∖ D(κ)), where R(r,c) = (m−1−c, m−1−r) | **proved** (§2), and checked m ≤ 8 |
| **Lemma Ch** (chain drop) | if θ = D(κ)∖D(ρ) has no strictly-SE pair and ≤ 2 boxes in every row and column, then r′(ρ) ≥ r′(κ) − 2 | **proved** (§3); checked on all 3801 such pairs, m ≤ 8 |
| **Theorem Z** | for every strict κ ⊆ [m] and every odd M with 3 ≤ M ≤ 2⌈r′(κ)/2⌉+1, H_κ(−M/2) = 0 | **proved given (G1) + (BR)**; (BR) is cited at abstract-level extraction, so it is a gap (§6) |
| (f) edge sign-coherence | the Pieri terms of b_κ at the window edge all have one sign | **FALSE** (§5), e.g. κ = (3,2) |

This **closes Case B**, conditional on the K-Pieri support statement. Case B was the only open part of (Z). Earlier partial
results were Thm C (M = 3), Thm Z₂ (2-separated κ) and Cor Z (ℓ ≤ 2). Theorem Z contains all three, apart from the anchor
M = 3, which it uses.

## 1. Setup and the two premises

Shifted diagram: D(κ) = {(r,c) : 0 ≤ r < ℓ(κ), r ≤ c ≤ r+κ_{r+1}−1}, which lies inside the shifted staircase
Δ_m = {(r,c) : 0 ≤ r ≤ c ≤ m−1}. D(κ) is an order ideal of Δ_m for the product order (r,c) ≤ (r′,c′) ⟺ r ≤ r′ and c ≤ c′.
r′(κ) = the length of the longest chain in D(κ⁻), where κ⁻ = (κ₂, κ₃, …). D(κ⁻) is the translate by (−1,−1) of
D(κ) ∩ {r ≥ 1}, and the product order is invariant under translation, so

  **r′(κ) = longest chain in D(κ)₊ := D(κ) ∩ {row ≥ 1}.**   (1.1)

(This is what `support.rp` computes. It is 0 when ℓ(κ) ≤ 1, and ≥ 1 when ℓ(κ) ≥ 2.) For ρ ⊆ κ, meaning ρ_i ≤ κ_i for all i,
row r of D(ρ) is row r of D(κ) truncated. So D(ρ)₊ ⊆ D(κ)₊, and **both are "row 0 removed"**. PROVE.md worried that r′
removes the largest part of κ and of ρ, and that these might be different rows. They are not different rows: row 0 is the
largest part of both, whatever θ does to it.

**(G1)** The Demazure character formula for line bundles on Schubert varieties. Through Thm C this gives the anchor:

  **Thm C** (`proofs/2026-10-23-odd-zero-law.md` §6, proved given (G1)): H_κ(−3/2) = 0 whenever ℓ(κ) ≥ 2.

This uses H_ν(−1) = 0 for ν ≠ ∅ (D_m e^{−ω} = 0). It does **not** use the integer window (gap 4 of that file).

**(BR)** K-Pieri for p = 1 on LG(m,2m) (Buch–Ravikumar, arXiv:1005.2605, §5, Cor 5.4 / eq. (11)). In the codimension
basis O^λ = [O_{X^λ}]:

  O^λ · O^1 = Σ_ν c_ν O^ν, and c_ν ≠ 0 only if λ ⊊ ν and D(ν)∖D(λ) has no two boxes in strictly-SE position and
  ≤ 2 boxes in every row and every column.

Only this **support inclusion** is used. Here is a correction to PROVE.md, which says "supp = rims": equality is FALSE.
The coefficient also vanishes on some admissible θ. The simplest case is a vertical domino whose lower box is diagonal,
e.g. κ = (2,1), ρ = (1), where the labelling count is 0. The inclusion holds for the encoded BR formula at every m ≤ 8
(`prove252_supp_refl_drop.py`, 0 violations). Separately, it holds for the *true* K-class at m ≤ 5, computed from (G1)
alone by `kclass.py` (46/46 match with BR), and for 38/63 κ at m = 6.

## 2. Lemma S (translating codimension to dimension indexing)

X_κ = X^{κ^∨} with κ^∨ = [m]∖κ.

**Lemma S.** D(κ^∨) = R(Δ_m ∖ D(κ)) with R(r,c) = (m−1−c, m−1−r).

*Proof.* Take (r,c) ∈ Δ_m and put d = c−r+1 ∈ [1, m−r]. Box (r,c) lies in D(κ) iff κ_{r+1} ≥ d, i.e. iff
#(κ ∩ [d,m]) ≥ r+1. Write R(r,c) = (r̄,c̄) with r̄ = m−1−c. Then c̄ − r̄ + 1 = c − r + 1 = d. Applying the same criterion,
R(r,c) ∈ D(κ^∨) iff #(κ^∨ ∩ [d,m]) ≥ r̄+1 = m−c. Now #(κ ∩ [d,m]) + #(κ^∨ ∩ [d,m]) = m−d+1 = m−c+r, so this condition
is #(κ ∩ [d,m]) ≤ r, which says (r,c) ∉ D(κ). R is an involution of Δ_m. ∎

**Consequence.** Write O_{X_κ}·O^1 = Σ_ρ c_ρ [O_{X_ρ}], with ρ^∨ = ν and κ^∨ = λ. Then

  D(κ)∖D(ρ) = R(Δ∖D(λ)) ∖ R(Δ∖D(ν)) = R(D(ν)∖D(λ)),

and λ ⊊ ν ⟺ ρ ⊊ κ. R reverses the product order, so it maps strictly-SE pairs to strictly-SE pairs, and it exchanges rows
with columns. The bound "≤ 2 per row and per column" is symmetric under that exchange. Hence:

  **(BR′)** c_ρ ≠ 0 ⟹ ρ ⊊ κ and θ := D(κ)∖D(ρ) has no strictly-SE pair and ≤ 2 boxes in every row and column.

The primed/unprimed convention on the diagonal flips under R. Only coefficients see it, and coefficients are never used.

## 3. Lemma Ch (chain drop)

**Lemma Ch.** Let ρ ⊆ κ be strict and let θ = D(κ)∖D(ρ) satisfy the conclusion of (BR′). Then every chain C of D(κ) meets θ
in at most 2 boxes. Consequently r′(ρ) ≥ r′(κ) − 2.

*Proof.* Take distinct comparable boxes a < b in θ. Since b is not strictly SE of a, they share a row or a column. Now
suppose a < b < c were three boxes of C ∩ θ. Every pair among them is comparable, so every pair shares a row or a column.
- a,b in one row and b,c in one column: a = (r,x), b = (r,y) with y > x, c = (s,y) with s > r. Then c is strictly SE of a,
  a contradiction.
- a,b in one column and b,c in one row: a = (x,y), b = (s,y) with s > x, c = (s,z) with z > y. Again c is strictly SE of a.
- Otherwise all three lie in one row or all three in one column, which contradicts "≤ 2 per row/column".

So |C ∩ θ| ≤ 2. For the consequence, take a longest chain C of D(κ)₊, so |C| = r′(κ) by (1.1). Then C∖θ ⊆ D(ρ) ∩ {row ≥ 1}
= D(ρ)₊ is a chain of size ≥ r′(κ) − 2. By (1.1) for ρ, r′(ρ) ≥ r′(κ) − 2. ∎

The bound is sharp: the minimum drop over the support is exactly −2 for 1, 4, 12, 30, 70, 154 of the κ with ℓ ≥ 2 at
m = 3, …, 8. This was recorded Wake 252 as a horizontal domino in row ≥ 1.

## 4. Theorem Z

**Theorem Z.** Assume (G1) and (BR). For every strict κ with parts in [m] and every odd M with 3 ≤ M ≤ 2⌈r′(κ)/2⌉+1,
H_κ(−M/2) = 0.

*Proof.* We use strong induction on |κ|. Write W(κ) = {odd M : 3 ≤ M ≤ 2⌈r′(κ)/2⌉+1}.

*Empty window.* If r′(κ) = 0, i.e. ℓ(κ) ≤ 1 (this includes κ = ∅ and the one-row κ), then W(κ) = ∅ and there is nothing
to prove. From now on ℓ(κ) ≥ 2, so r′(κ) ≥ 1 and W(κ) = {3, 5, …, 2⌈r′/2⌉+1} ∋ 3.

*Step 1: the hyperplane identity.* O(1) is very ample and X_κ is integral, so there is a section s with s|_{X_κ} ≠ 0, and
it is a nonzerodivisor. Let D = Z(s|_{X_κ}). Tensoring 0 → O_{X_κ}(−1) → O_{X_κ} → O_D → 0 with O(j) and taking χ gives,
for every integer j,

  b_κ(j) := H_κ(j) − H_κ(j−1) = χ(O_D(j)) = χ([O_{X_κ}]·(1−[O(−1)])·[O(j)]).

LG is smooth, so K⁰ = K₀. Moreover 1 − [O(−1)] = O^1, because the Schubert divisor X^1 is the zero scheme of a section of
O(1): its Chevalley multiplicity on LG is ⟨ω_m, α_m^∨⟩ = 1. Expanding [O_{X_κ}]·O^1 = Σ_ρ c_ρ [O_{X_ρ}] gives
b_κ(j) = Σ_ρ c_ρ H_ρ(j) for all integers j. Both sides are polynomials in j, so the identity holds identically, and in
particular at half-integers. (D is the non-reduced divisor. The coefficients c_ρ take care of the multiplicities. We never
need D's components.)

*Step 2: every term vanishes on the shrunken window.* Let M be odd with 3 ≤ M ≤ 2⌈r′(κ)/2⌉ − 1, and take ρ with c_ρ ≠ 0.
By (BR′) and Lemma Ch, ρ ⊊ κ and r′(ρ) ≥ r′(κ) − 2. Hence

  2⌈r′(ρ)/2⌉ + 1 ≥ 2⌈(r′(κ)−2)/2⌉ + 1 = 2⌈r′(κ)/2⌉ − 1 ≥ M.

So M ∈ W(ρ), and by the induction hypothesis (|ρ| < |κ|) H_ρ(−M/2) = 0. Therefore b_κ(−M/2) = 0. If r′(κ) ≤ 2 this
range of M is empty and Step 2 says nothing.

*Step 3: telescope from the anchor.* By Thm C, H_κ(−3/2) = 0, since ℓ(κ) ≥ 2. For odd M in the range of Step 2,
b_κ(−M/2) = 0 reads H_κ(−M/2) = H_κ(−(M+2)/2). Going up M = 3, 5, …, 2⌈r′/2⌉−1 propagates the zero from −3/2 down to
H_κ(−(2⌈r′/2⌉+1)/2) = 0. That covers all of W(κ). ∎

**Worked example.** κ = (4,3,2,1), m = 4: r′ = r((3,2,1)) = 5, so W = {3,5,7}. Thm C gives the zero at −3/2. The BR
support of [O_D] consists of ρ with r′(ρ) ≥ 3, and each such ρ has W(ρ) ⊇ {3,5}, so b_κ vanishes at −3/2 and −5/2.
Telescoping gives H_κ = 0 at −3/2, −5/2, −7/2. That matches the computed sign row "+000+++" for (−1)^{|κ|}H_κ(−M/2),
M = 1, 3, …, 13 (`prove252_signs.py`). The value at −9/2 is nonzero, and that is (NZ), not claimed here.

## 5. Verification

- `prove252_supp_refl_drop.py 8`: Lemma S holds for every κ, m ≤ 8. supp(BR formula) ⊆ (BR′) holds with 0 violations,
  m ≤ 8. The minimum drop is ≥ −2 (247 κ with ℓ ≥ 2 at m = 8).
- `prove252_rimlemma.py 8`: Lemma Ch is purely combinatorial, with no Pieri input. Over all admissible (κ,ρ) (1, 5, 17,
  53, 159, 465, 1337, 3801 pairs for m = 1..8) there are 0 violations.
- `out_gate6_m7.txt` (Wake 252): the theorem's conclusion holds for all 127 κ at m = 7 (law 33/33 Case A, 94/94 Case B).
  Every K-term vanishes on the shrunken window (92/92 Case B). BR × LS model reproduces b_κ 127/127. Earlier: 63/63 at m ≤ 6.
- **(f), negative.** At the window edge M* = 2⌈r′/2⌉+1, the identity H_κ(−(M*+2)/2) = −b_κ(−M*/2) = −Σ c_ρ H_ρ(−M*/2)
  would give (NZ) at the first point beyond the window, if the nonzero terms were sign-coherent. The c_ρ do alternate as
  (−1)^{|θ|−1} (all m ≤ 6). But the terms are **not** coherent: 8/43 Case-B κ fail at m = 6, e.g. κ = (3,2) with terms
  −1/8 and +1/4. The culprits are ρ in the Prop-R regime (M ≤ ρ₁), where sgn H_ρ = (−1)^{|ρ′|}, not (−1)^{|ρ|}
  (`prove252_signs.py`, `prove252_edge_coherence.py`). (NZ) stays open in the middle range. No monotone-sign induction
  exists in this naive form.

## 6. Gaps (precise)

1. **(BR) is not deep-read.** `sources.json` records 1005.2605 at extraction level "abstract", and no local copy exists.
   This session was no-browsing. The load-bearing statement is exactly the support inclusion stated in §1 (codimension
   form). Corroboration is computational: the true K-class (from (G1)) at m ≤ 5, the encoded formula at m ≤ 8. The
   specific concern is whether BR's "rim" excludes diagonal configurations {(r,r),(r,r+1),(r+1,r+1)}. Those contain a
   3-chain and would break Lemma Ch. In the computed range they never occur in the support. **Next action:** deep-read
   1005.2605 §5 and confirm the inclusion literally, then upgrade the source entry.
2. **(G1)** cited, not deep-read: the same debt as Thm C. Nothing else from G2–G4 is used.
3. Nothing else. Lemma S, Lemma Ch and the induction are self-contained.

## 7. Lesson

Of the zero law's input, the induction only needs the **support** of the K-Pieri product. The coefficients alternate, and
the hope was that alternation would cancel or reinforce something. It does neither: alternation buys no sign-coherence at
the edge, so the vanishing half is cheap and the nonvanishing half is not. Before asking a Pieri rule for coefficients, ask
whether its support is enough.
