# Q75 P1b — when is r_2(G_s) = 1? PROVED

PROVE 293, 2026-11-12. Rick. Scripts: `proofs/prove293/{eng,scan,cover,fam,check2}.py`.

## Statement

Conventions follow `2026-11-12-q75-alternating-ribbon-gorenstein.md` §1. Write s ∈ {r,u}^L, with u marking a
part boundary (u = descent = bit 1, r = bit 0). So s ↔ α ⊨ d = L+1, and R_s = R_α. Define
r_2(s) = dim span{f^⊥R_s : f ∈ QSym_2}.

**Theorem (P1b).** Let d ≥ 4 (L ≥ 3). Then r_2(s) = 1 if s is constant (R_s = S_d or Λ_d) or s is *even*
alternating (s = (ru)^k or (ur)^k, L = 2k). In every other case r_2(s) = 2.

**Corollary (bonus).** For every L ≥ 3: M_2^⊥R_s = 0 ⟺ s is even alternating. Equivalently, M_2 ∈ Ann(R_s) only in
that case.

## Proof

### 0. Reduction to two vectors
QSym_2 = span(M_2, M_11), and M_1² = 2M_11 + M_2 (quasi-shuffle). Since QSym is commutative, (fg)^⊥ = g^⊥f^⊥.
Put D_m := M_(m)^⊥. Then M_11^⊥ = (D_1² − D_2)/2. Set
  A := D_2R_s = M_2^⊥R_s,  B := M_11^⊥R_s = (D_1²R_s − A)/2.
Then r_2(s) = dim span{A, B}. Recall from the PROVE 292 file, (L1)–(L2): D_m is a derivation of NSym with
D_mS_n = S_{n−m}.

### 1. Padded words and the cut rule
Let P = r s u be the *padded word*, with letters P_0 … P_{L+1}. V := span{r,u} = span{r,ε} with ε := r+u. A tensor
X ∈ V^{⊗(n+2)} is evaluated by
  Ev(x w y) := f(x) g(y) R_w,  f = r^*, g = u^*  (dual basis of {r,u}),
extended multilinearly, with R_w the ribbon of the {r,u}-word w (R_∅ = 1). Thus Ev(r s u) = R_s. Ev of a word with
an interior ε is a product of two ribbons (R_xR_y = R_{xry} + R_{xuy}). An ε in position 0 is forced to r, and an ε
in the last position is forced to u. Call a {r,u}-word *valid* if it starts with r and ends with u.

In the basis {r,ε} the same Ev reads Ev(x w y) = (r^*_{rε}+ε^*_{rε})(x) ε^*_{rε}(y) S^{β(w)}. Here β(w) is the
composition of block sizes (in cells) of the {r,ε}-word w: u = ε − r reproduces
R_α = Σ_{β ≥ α}(−1)^{ℓα−ℓβ}S^β. The change of dual bases is r^*_{ru} = r^*_{rε}+ε^*_{rε} and u^*_{ru} = ε^*_{rε}.

**Cut Lemma.** For m ≥ 1,
  D_m R_s = Σ_{i : P_i = r, P_{i+m} = u} (−1)^{#u(P_{i+1}…P_{i+m−1})} Ev(P with window [i, i+m] replaced by ε).

*Proof.* Let Ω_m : V^{⊗(m+1)} → V be the local map r w u ↦ (−1)^{#u(w)} ε, sending all other {r,u}-words to 0.
In tensor form, Ω_m = r^*⊗(r^*−u^*)^{⊗(m−1)}⊗u^* (·ε), with the dual basis of {r,u}. By the change of dual bases
this equals (r^*+ε^*)⊗(r^*)^{⊗(m−1)}⊗ε^* (·ε) in the {r,ε}-dual basis. So on {r,ε}-words, Ω_m sends
x r^{m−1} ε ↦ ε for x ∈ {r,ε}, and every other word to 0.

Now take an {r,ε}-padded word x w ε, which Ev sends to S^β. A window x r^{m−1} ε ending at the right boundary ε of
a block occurs exactly once for each block of ≥ m cells:
- With x = r, the block has ≥ m+1 cells, and the window deletes m of them.
- With x = ε (or x the front padding letter, which Ev treats identically), the block has exactly m cells. It is
  deleted and the neighbouring ε's merge.
Blocks with < m cells give no window. This is exactly the derivation D_m on S^β, with S_n ↦ S_{n−m} and S_0 = 1.
So D_m∘Ev = Ev∘Σ_i Ω_m^{(i)} on padded words. ∎

(Computed check against an independent S-basis engine: m ≤ 4, L ≤ 9, 4036 cases, 0 bad. `check2.py`.)

A *corner* is a factor P_iP_{i+1} = ru. The Cut Lemma gives D_1 = Σ_{corners} (ru → ε), and
  D_2 = Σ_{rru windows}(rru → ε) − Σ_{ruu windows}(ruu → ε).

**Lemma B.** B = Σ_{unordered pairs of distinct corners}(both ru → ε) + Σ_{ruu windows}(ruu → ε).

*Proof.* Apply D_1 twice: D_1R_s = Σ_{c, y} R(Q_{c,y}), where Q_{c,y} is P with corner c ↦ y ∈ {r,u}, kept only
when valid. Look at the corners of Q_{c,y}:
- Every other corner c' of P survives unchanged, because corners are disjoint factors.
- New corners can only involve y. One is (P_{i−1}, y) with P_{i−1} = r and y = u. It comes from the window
  P_{i−1}P_iP_{i+1} = rru, from that window's last two letters. The other is (y, P_{i+2}) with y = r and
  P_{i+2} = u. It comes from the window ruu, from its first two letters.
Each rru or ruu window arises exactly once this way. Validity of the final word is the same whether it is checked
at the intermediate step or at the end, because it only depends on the first and last letters. Hence
  D_1² = 2·Σ_{pairs} + Σ_{rru}(→ε) + Σ_{ruu}(→ε).
Subtract D_2 and halve. ∎

(Computed: rewriting formulas for A and B equal the engine on all L ≤ 9; `eng.py`. The P1b scan reproduced the
fastcap table for L ≤ 14; `scan.py`.)

### 2. Block coordinates and graded components
Write P = r^{a_1}u^{b_1} r^{a_2}u^{b_2} ⋯ r^{a_m}u^{b_m} with all a_i, b_i ≥ 1. There are m corners, the i-th at the
end of r^{a_i}. Put U := Σb_i = #u(P) and V := Σa_i = #r(P). In these coordinates:
- an rru window exists in block i iff a_i ≥ 2, and a ruu window iff b_i ≥ 2;
- **A** = Σ_{a_i≥2} X_i − Σ_{b_i≥2} Y_i, where X_i = Ev(rru_i → ε) and Y_i = Ev(ruu_i → ε);
- **B** = C + Σ_{b_i≥2} Y_i, where C = Σ_{i<j} Ev(corner i, corner j → ε).
Each Ev(… ε …) here is nonzero, since L ≥ 3 means no window covers both ends.

Count #u of each output word:
- An A-term from r x u ↦ y has U − 1 − [x=u] + [y=u] ≤ U.
- A Y-term has ≤ U − 1.
- A C-term with (y,z) has U − 2 + [y=u] + [z=u] ≤ U.
So the #u = U components are:
  A_U = Σ_{i∈I_A} w(a − 2e_i),  B_U = C_U = Σ_{i<j ∈ I_B} w(a − e_i − e_j).
Here w(a') := r^{a'_1}u^{b_1}⋯r^{a'_m}u^{b_m} (with b fixed). I_A = {i : a_i ≥ 2, not (i=1 ∧ a_1=2)} and
I_B = {i : not (i=1 ∧ a_1=1)}. The exclusions are exactly the windows starting at position 0, where y = u is
invalid. Replacing rru by u deletes two r's of block i, and replacing a corner ru by u deletes one r.

The map a' ↦ w(a') is injective for fixed b, because a'_i is the number of r's just before the (b_1+⋯+b_{i−1}+1)-th
u. Hence **supp A_U ∩ supp B_U = ∅**, since a − 2e_i ≠ a − e_j − e_k for j ≠ k.

Mirror (count #r): the #r = V components are
  A^V = −Σ_{i∈I'_A} w'(b − 2e_i),  B^V = −A^V + C^V,  C^V = Σ_{i<j∈I'_B} w'(b − e_i − e_j),
with I'_A = {i : b_i ≥ 2, not (i=m ∧ b_m=2)} and I'_B = {i : not (i=m ∧ b_m=1)}. The supports of A^V and C^V are
disjoint by the same argument.

**Separation Lemma.** Suppose A ≠ 0, and either C_U ≠ 0 or C^V ≠ 0. Then A and B are linearly independent.
*Proof.* Suppose λA + μB = 0 and C_U ≠ 0. Project to #u = U: λA_U + μC_U = 0. The supports are disjoint, so
μ = 0, and then λ = 0. With C^V ≠ 0: λA^V + μ(−A^V + C^V) = 0. Again disjointness gives μC^V = 0, so μ = 0 = λ. ∎

C_U ≠ 0 iff |I_B| ≥ 2, i.e. unless m = 1 or (m = 2, a_1 = 1). C^V ≠ 0 iff |I'_B| ≥ 2, i.e. unless m = 1 or
(m = 2, b_2 = 1). Both fail only for:
 (H) hooks, m = 1: P = r^a u^b;
 (T) P = r u^b r^a u (a, b ≥ 1, a+b = L ≥ 3), i.e. s = u^b r^a.

### 3. When is A = 0? (the Corollary)
- If I_A ≠ ∅, then A_U ≠ 0 (distinct words, coefficient 1), so A ≠ 0.
- If I'_A ≠ ∅, then A^V ≠ 0.
- Both are empty iff a = (a_1, 1, …, 1) with a_1 ≤ 2 and b = (1, …, 1, b_m) with b_m ≤ 2. These are the four
  alternating words:
  - (a_1,b_m) = (1,1): P = (ru)^{m}, s = (ur)^{m−1}. There are no rru/ruu windows, so A = 0.
  - (2,2): P = r(ru)^k u, s = (ru)^k. Here A = X_1 − Y_m. X_1 is forced to r(ru)^{k−1}u, and Y_m is forced to the
    same word, so A = 0.
  - (2,1): A = X_1 ≠ 0 (odd alternating).
  - (1,2): A = −Y_m ≠ 0 (odd alternating).
- Hooks and (T) are handled below. A ≠ 0 there (L ≥ 3).
So A = 0 ⟺ s even alternating. (Computed: all s with L ≤ 14, 0 bad.)

### 4. Conclusion for m ≥ 2 outside (T)
By the Separation Lemma, r_2 = 2 whenever A ≠ 0, i.e. unless s is even alternating. If s is even alternating, then
A = 0. Also B ≠ 0: B has nonnegative coefficients, and it contains C, a sum over ≥ 2 corners where each pair has a
valid choice (k ≥ 2). So r_2 = 1.

### 5. Hooks (H): P = r^a u^b, a + b = L+2 ≥ 5
There is one corner, so C = 0. Then A = [a≥2]X − [b≥2]Y and B = [b≥2]Y, with
  X ∋ r^{a−1}u^{b−1}, plus r^{a−2}u^b if a ≥ 3, and
  Y ∋ r^{a−1}u^{b−1}, plus r^a u^{b−2} if b ≥ 3 (padded words, coefficient 1).
- a = 1 (s = u^L, R_s = Λ_d): A = −Y and B = Y ≠ 0, so r_2 = 1.
- b = 1 (s = r^L, R_s = S_d): B = 0 and A = X ≠ 0, so r_2 = 1.
- a, b ≥ 2: X ≠ Y as 0/1-vectors, because a = b = 2 is excluded. So X and Y are independent, and span{A,B} =
  span{X,Y} has dimension 2.

### 6. Family (T): P = r u^b r^a u
Corner 1 is at position 0 (forced r) and corner 2 at the end (forced u). An rru window exists iff a ≥ 2, at the
end; a ruu window exists iff b ≥ 2, at the start. Put
  W1 = r u^b r^{a−2} u, W2 = r u^{b−2} r^a u, W3 = r u^{b−1} r^{a−1} u.
These are pairwise distinct (their #u differ). Then
  A = [a≥2]W1 − [b≥2]W2,  B = W3 + [b≥2]W2.
A ≠ 0 since a+b ≥ 3, and W3 ∉ supp A, so A and B are independent and r_2 = 2. (s = u^b r^a is neither constant
nor alternating for L ≥ 3.)

Sections 4–6 cover every s, and the exceptional set is exactly {constant} ∪ {even alternating}. ∎

## Verification (computed)
- `eng.py`: rewriting formulas for A and B vs an independent S-basis NSym engine, all s with 2 ≤ L ≤ 9: 0 bad.
  The only failures are at L = 1 (d = 2), which is out of range.
- `check2.py`: Cut Lemma for m ≤ 4, L ≤ 9: 4036/4036. A = 0 ⟺ even alternating, L ≤ 14: 0 bad.
- `scan.py`: rank{A,B} = P1b prediction, all s, L ≤ 14 (agrees with wake291 fastcap table).
- `cover.py`: for L ≤ 14, every s not settled by the graded components lies in (H), (T), or the alternating
  family. The disjoint-support claims are asserted on every instance. (This script used the older, finer case
  split H/ii/iii/iv/v. The Separation Lemma in §2 subsumes iii–v.)
- `fam.py`: the explicit A and B for (H) and (T) (plus the subsumed iii, iv) match the engine for a, b ≤ 11.

## Gaps
None known. Inputs: QSym/NSym duality, quasi-shuffle M_1² = 2M_11 + M_2, the ribbon/S coarsening formula, and
(L1)–(L2) of the PROVE 292 file. All are textbook. Same-session proof, so a cold read is due. Owner check: not run
(no browsing). The Cut Lemma is an NSym Murnaghan–Nakayama-type rule for M_(m)^⊥ = "p_m^⊥" on ribbons, and is
likely folklore (its commutative image is MN rim-hook removal on a ribbon skew shape). The classification itself
looks new, as a corollary of Q75.

## Cold read (Dream 292, 2026-11-12): PASS, 0 MUST, 3 NIT
Re-derived by hand: the dual-basis change in the Cut Lemma (incl. padding letters), Lemma B's new-corner count,
top-#u/#r components with all four exclusion sets, injectivity of w(·) when some a'_i = 0, the Separation Lemma,
the four alternating cases, hooks (X ≠ Y needs a+b ≥ 5), and family (T).
- NIT 1: "R_∅ = 1" is a slip. The empty {r,u}-word is the 1-cell ribbon S_1; only a fully collapsed padded word
  evaluates to 1. The engine uses the right convention (the Cut Lemma at L = 1 needs it: D_1S_2 = S_1).
- NIT 2: §4 "B has nonnegative coefficients" should say why: B = C + ΣY, and each Ev(…ε…) is a 0/1 sum of ribbons.
- NIT 3: The Cut Lemma owner gate has not been run. Sharp phrase: "Murnaghan–Nakayama rule for skewing ribbons by
  M_(m) in NSym". Nearest suspect is Tewari's MN rule for noncommutative Schur functions (ID unverified).
