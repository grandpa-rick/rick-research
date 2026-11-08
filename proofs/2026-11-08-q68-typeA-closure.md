# Q68 in type A: closure note. The twin decision procedure is complete, and the census n ≤ 16 is a theorem modulo one computed KL value (PROVE 284, 2026-11-08)

Scripts and outputs: `proofs/prove284/` (`link.py`, `out_link.txt`, `rerun.sh`, `out_rerun.txt`).
Earlier records: P279 `2026-11-06-q68-kl-cone-twins.md`, P280 `2026-11-06-q68c-s14-twin.md`,
P281 `2026-11-07-q68-s15-separator.md`, P282 `2026-11-07-q68-ii-kills.md`, W/P283 `2026-11-08-q68-lemmaI-false-s16-closed.md`.
Registry: `proofs/registry/seedQ2-kl-cone.json`.

This note is the stable write-up asked for by PROVE 284. **It opens no Q69 on this arc.**

## 0. Answer in one screen

**The completeness claim is TRUE. It is Theorem W (§4), proved for every finite Coxeter group.** The proof needs only (F1) and μ ≥ 0, not Lemma S.
- It is the P280 Step 2 argument, which P281 §3 stated generally. Here it is written down once, in its own right.
- "Parity" is **not** an independent conjunct. In a connected simply-laced W it is *implied* by the witness inequality (Corollary W2). The census uses it only as a cheap prefilter: a parity kill *is* a witness failure, with μ(*x, z) = 0 by even gap.
- Honest remark: Theorem W is close to a tautology (P281 gap 3 already said so). The content of a TWIN verdict lies in the μ-values, not in the witness set.

**Lemma S is what turns each μ-certificate into a proof.** Proposition C (§6) lists exactly what each certificate type proves.

**New in this session:**
1. **Proposition Q, cell independence.** It is now **proved** from Knuth's theorem plus Lemma S. It was previously "recall-only (Haiman dual equivalence)" or "computed (`dualconn.py`)". So every census verdict, made in one cell Q₀, holds in **every** left cell of the shape.
2. **Proposition M.** The two computed μ-values that the census actually uses, μ(in0b) and μ(in1b), are both equal to μ(in0) by *proved* relations. One is a single right star; the other is w₀-conjugation followed by two right stars (`link.py`). So:

> **Theorem (type-A census, n ≤ 16).** The dominated twins of S_n, n ≤ 16, are exactly the TWIN pairs (P_x, P_z) of the certificate files, in every left cell of the shape.
> - n ≤ 13: 0.
> - n = 14: 4.
> - n = 15: 26 (of 48 candidates).
> - n = 16: 114 (of 410).
>
> The theorem holds **modulo**:
> - (a) the recall-only KL/RSK basics of §2;
> - (b) the exhaustive enumeration code (C3 dominance check; `listn.py`);
> - (c) the mechanical certificate replays;
> - (d) **exactly one computed KL value**, μ(x₀, z₀) = 1 for the S_16 pair `in0`. It was computed by two independent implementations, and only the TWIN verdicts of pairs 353 and 364 use it.

Grade: Theorem W **proved**; Prop Q **proved** (modulo the textbook facts named); Prop M **proved**; census **computed (certificate-complete)**. See §7 for why I don't call the census "proved".

## 1. Setting and definitions

- W is a finite Coxeter group with simple reflections S, length l, and Bruhat order ≤. L(w) = {s : sw < w} and R(w) = {s : ws < w}.
- P_{y,w} are the KL polynomials. For y < w, μ(y,w) is the coefficient of q^{(l(w)−l(y)−1)/2} in P_{y,w}.
- **Symmetric μ̃(a,b)**: μ(a,b) if a < b, μ(b,a) if b < a, and 0 otherwise. Below, "μ(y,x)" always means μ̃.
- Left preorder (KL79): y ≤_L w is the transitive closure of the relation "μ̃(y,w) ≠ 0 and L(y) ⊄ L(w)". Left cells are its equivalence classes.
- **Cell module** (GW 2604.18894 Ex 4.7, convention C), at v = 1, with basis e_x, x ∈ Γ:
  - (1+s)e_x = 0 if s ∈ L(x);
  - otherwise (1+s)e_x = 2e_x + Σ_{y∈Γ, s∈L(y)} μ̃(x,y) e_y.
- **Dominated twin.** A pair (x, z) with x ≠ z ∈ Γ, L(z) ⊆ L(x), and

  (TW) μ̃(y,z) ≥ μ̃(y,x) for every y ∈ Γ with L(y) ⊄ L(x).

  Lemma A: a twin makes cone({e_w : w ≠ z} ∪ {e_z − e_x}) a strictly larger pointed invariant cone, so C_KL(Γ) is not maximal.
- **Interior.** For W simply laced, int A = {s ∈ A : every neighbour of s lies in A}. In type A the end nodes count as interior when they lie in A.
- **Candidate pair** (type A). A pair (x, z) in one left cell with L(x) = A and ∅ ≠ L(z) ⊆ int A. By C2 every twin is a candidate pair.
- **Type-A dictionary.** w is in one-line notation, and s_i·w swaps the *values* i and i+1.
  - L(w) = Des P(w) and R(w) = Des Q(w), where (P, Q) = RSK(w).
  - Left cells are {w : Q(w) = Q}, written Γ_Q.
  - λ ⊢ n; f^λ = #SYT(λ); in Γ_Q, w ↔ P(w) is a bijection with SYT(λ).
- **Witness sets of x** (any W):
  - W_i(x) = {sx : s ∈ S, sx ∈ Γ, L(sx) ⊄ L(x)};
  - W_ii(x) = {y ∈ Γ : L(y) ⊋ L(x), y < x}.

## 2. Inputs used without proof (textbook / recall-only)

KL:
- (K1) KL79 (2.2.c) recursion and (2.3.g): P_{y,w} = P_{sy,w} for s ∈ L(w).
- (K2) μ ≥ 0 in Weyl groups (KL79/KL80 via intersection cohomology; Elias–Williamson 2014 for every Coxeter group).
- (K3) P_{y,w} = P_{y⁻¹,w⁻¹}, and y ≤ w ⟺ y⁻¹ ≤ w⁻¹.
- (K4) A diagram automorphism of (W,S) (in S_n: w ↦ w₀ww₀) preserves l, ≤ and every P_{y,w}.
- (K5) If y < w with l(w) − l(y) = 1, then P_{y,w} = 1. If l(w) − l(y) is even, or y and w are incomparable, then μ̃ = 0.

RSK:
- (R1) RSK is a bijection S_n → ⊔_λ SYT(λ)².
- (R2) L(w) = Des P(w). By Schützenberger symmetry RSK(w⁻¹) = (Q,P), so R(w) = Des Q(w).
- (R3) Left cells of S_n = {Q fixed} (KL79 §5, with the Knuth-class description). This is the convention all the census code uses.
- (R4) **Knuth's theorem.** P(w) = P(w′) ⟺ w and w′ are joined by elementary Knuth moves. These are yxz ↔ yzx and xzy ↔ zxy on three adjacent positions, with x < y < z.

All of these were validated in S_5/S_6 against full KL or brute force, in earlier sessions (`prove280/test_star.py`, `prove282/rskfacts.py`).

## 3. Proved lemmas (restated with proofs)

**(F1)** Let y < w, s ∈ L(w) \ L(y) and μ(y,w) ≠ 0. Then y = sw.

*Proof.* By (K1), P_{y,w} = P_{sy,w}. If sy ≠ w, then sy < w and the degree of P_{sy,w} is ≤ (l(w)−l(y)−2)/2, so μ(y,w) = 0. ∎

**(F2)** If μ̃(y,w) ≠ 0, L(y) ⊄ L(w) and L(w) ⊄ L(y), then y ~_L w.

*Proof.* Immediate from the definition of ≤_L applied in both directions. ∎

**Lemma A** (P279). If (TW) holds, the cone K = cone({e_w}_{w≠z} ∪ {e_z − e_x}) is simplicial, {1+s}-invariant, and contains C_KL strictly.

*Proof.* Put v = e_z − e_x. The set is a basis, and e_z = v + e_x gives K ⊇ C_KL. Strictness holds because v ∉ C_KL. Check (1+s)v in three cases:
- s ∈ L(z) ⊆ L(x): (1+s)v = 0.
- s ∈ L(x) \ L(z): (1+s)v = (1+s)e_z ∈ C_KL.
- s ∉ L(x): (1+s)v = 2v + Σ_{s∈L(y)} (μ̃(z,y) − μ̃(x,y)) e_y. Every such y has L(y) ⊄ L(x) and y ∉ {x, z}, so each coefficient is ≥ 0 by (TW). ∎

**Lemma C1** (star kill, P279; pairing step = Stembridge RT 12 (2008) Prop 4.4/4.2). Let (x, z) be a twin, s ∈ L(x), t ∉ L(x), m(s,t) = 3. Then s ∉ L(z).

*Proof.* Let *x be the element of {sx, tx} of type {t}. Then μ̃(x, *x) = 1, and F2 gives *x ∈ Γ. (TW) at *x gives μ̃(*x, z) ≥ 1.
Suppose s ∈ L(z). Then z has type {s}, since t ∉ L(z) ⊆ L(x), and *x has type {t}. By (F1) in either Bruhat direction, z ∈ {s·*x, t·*x}. The type-{s} one is x, so z = x, a contradiction. ∎

**Corollary C2.** If W is simply laced and (x, z) is a twin, then ∅ ≠ L(z) ⊆ int L(x).

**Lemma P** (P281). If W is connected and simply laced and (x, z) is a twin, then l(x) ≡ l(z) (mod 2).
*Proof.* This is Corollary W2 below.

**Lemma S** (KL79 Thm 4.2 for m = 3; proof in P280 Step 1). For s, t with m(s,t) = 3 and y, w ∈ D_L(s,t), μ̃(y,w) = μ̃(*y,*w).
The right version, for y, w ∈ D_R(s,t) with right star w ↦ w*, follows from (K3).

*Proof outline* (full computation in P280). Write elements of D_L as su, tsu, tu, stu, with u minimal in its ⟨s,t⟩-coset.
- *Same coset:* the six pairs are checked directly.
- *Different types:* (F1) forces w = *y, both before and after the star.
- *Same form:* (K1) at w = su′, tw > w. The second and third terms of the recursion both contribute μ(stsu, su′), with opposite signs.
- *Mixed form* (the gap-changing case): (K1) at stu′ = s·tu′. The first term has too low a degree, the second gives μ(tsu, tu′), and the third is killed by (F1). ∎

**Layer Lemma** (folklore: Billey–Braden math/0202252 Thm 6, Polo RT 3 L. 2.6; proof in P282 §3). Let u ∈ ^K W be minimal in W_K u, and v, v′ ∈ W_K. Then P_{v′u, vu} = P_{v′, v}.

*Proof outline.* Induct on l(v). The inputs are (K1), length additivity, and the fact that w ↦ w^K is Bruhat order-preserving (BB Prop 2.5.1). Every term of the recursion stays in the layer W_K u. ∎

**Theorem B** (P279, all finite W, non-simply-laced half). If m(s,t) ≥ 4, then (w_J, stw_J), with J = S \ {t}, is a twin. Stated here for completeness; it is not used in type A.

## 4. Theorem W: completeness of the witness set (NEW write-up; proved)

**Theorem W.** Let W be a finite Coxeter group, Γ a left cell, and x ≠ z ∈ Γ with L(z) ⊆ L(x) =: A.
- (a) If y ∈ Γ, L(y) ⊄ A and μ̃(y,x) ≠ 0, then y ∈ W_i(x) ∪ W_ii(x).
- (b) μ̃(y,x) = 1 for every y ∈ W_i(x).
- (c) (x, z) is a dominated twin ⟺ μ̃(y,z) ≥ μ̃(y,x) for all y ∈ W_i(x) ∪ W_ii(x).
- (d) For y ∈ W_i(x) this inequality reads μ̃(y,z) ≥ 1.

*Proof.*
(a) Since μ̃(y,x) ≠ 0, y and x are comparable, and y ≠ x because L(y) ⊄ A.
- *y > x.* Pick r ∈ L(y) \ A. Then r ∈ L(y) \ L(x), and (F1) gives x = ry, so y = rx ∈ W_i(x).
- *y < x and A ⊄ L(y).* Pick r ∈ A \ L(y). Then r ∈ L(x) \ L(y), and (F1) gives y = rx ∈ W_i(x).
- *y < x and A ⊆ L(y).* Since L(y) ⊄ A, we get L(y) ⊋ A, so y ∈ W_ii(x).

(b) sx and x are comparable with length difference 1, so μ̃ = 1 by (K5).

(c) ⇒ holds because W_i ∪ W_ii ⊆ {y ∈ Γ : L(y) ⊄ A}.
For ⇐, take y ∈ Γ with L(y) ⊄ A. If y ∈ W_i ∪ W_ii, the inequality is the hypothesis. Otherwise (a) gives μ̃(y,x) = 0 ≤ μ̃(y,z), by (K2).

(d) follows from (b). ∎

Remarks.
- W_ii(x) ∩ {y > x} = ∅ is built in. Elements with L(y) ⊋ A lying above x with μ̃ ≠ 0 are star images (by (F1)), so they sit in W_i. This matches P283's correction: inst 0 is both the (i), s = 10, element and the (ii)-element of pair 352.
- Nothing about cells, RSK or Lemma S enters. The census verifier's y-set is W_i together with {y ∈ Γ : Des P_y ⊋ A, μ̃(y,x) = 1 certified}. That set contains every y on which (TW) has content. If some μ̃(y,x) with Des P_y ⊋ A is undecided, the verifier refuses TWIN (`unk` flag). It still allows NO, since a single kill suffices.
- **μ̃(y,x) ≥ 2 is not excluded a priori** for y ∈ W_ii. In the census every needed μ̃(y,x) ∈ W_ii was certified to be exactly 1 (or exactly 0), so no case with μ ≥ 2 arose.

**Corollary W2 (parity is implied, not assumed).** Let W be connected and simply laced, and (x, z) a twin. Then:
- W_i(x) ≠ ∅;
- l(z) ≡ l(x) (mod 2).

*Proof.* L(x) ≠ ∅ by C2. Also L(x) ≠ S, because w₀ is alone in its cell and the cell has ≥ 2 elements. By connectivity there are adjacent s ∈ L(x), t ∉ L(x). Then *x (with respect to {s,t}) lies in Γ by F2, and t ∈ L(*x) \ L(x), so *x ∈ W_i(x).
By (d), μ̃(*x, z) ≥ 1. By (K5), l(*x) − l(z) is odd, and l(*x) = l(x) ± 1. ∎

So the PROVE 284 hunch "twin ⟺ parity AND witness inequality" is a true statement, but the parity conjunct is redundant. **The decision procedure is: C2 filter → witness inequality.** Parity is the cheapest instance of the second step.

## 5. Proposition Q: cell independence (NEW proof; previously recall-only/computed)

**Lemma K.** In S_n, the right star ρ_j with respect to {s_j, s_{j+1}} is defined on w iff exactly one of w(j) > w(j+1) and w(j+1) > w(j+2) holds. When it is defined, ρ_j(w) is the elementary Knuth move on positions j, j+1, j+2. Every elementary Knuth move arises this way.

*Proof.* Right multiplication by s_j swaps positions j and j+1, and R(w) ∩ {s_j, s_{j+1}} is read off the three letters.
- Type {s_j} with pattern yxz (x < y < z): w s_j = xyz has type ∅, and w s_{j+1} = yzx has type {s_{j+1}}. So ρ_j: yxz ↦ yzx.
- Type {s_j} with pattern zxy: w s_j = xzy has type {s_{j+1}}, and w s_{j+1} = zyx has type {s_j, s_{j+1}}. So ρ_j: zxy ↦ xzy.
- The type-{s_{j+1}} patterns yzx and xzy map back.

These two moves are exactly the Knuth relations. ∎

**Proposition Q.** Let λ ⊢ n and Q, Q′ ∈ SYT(λ). There is a bijection φ: Γ_Q → Γ_{Q′} with:
- P(φw) = P(w);
- L(φw) = L(w);
- μ̃(φw, φw′) = μ̃(w, w′) for all w, w′ ∈ Γ_Q.

Consequently, for T, T′ ∈ SYT(λ): ((T,Q), (T′,Q)) is a dominated twin ⟺ ((T,Q′), (T′,Q′)) is one.

*Proof.*
1. *A chain of Knuth moves.* Fix P₀ ∈ SYT(λ). By (R4) and Lemma K there are j₁, …, j_k with ρ_{j_k}⋯ρ_{j₁}(P₀,Q) = (P₀,Q′). Since R(w) = Des Q(w) is constant on a left cell, ρ_j is defined either on all of Γ_{Q(w)} or on none of it.
2. *One step.* Let ρ = ρ_j be defined on Γ = Γ_Q.
   - ρ is injective, being an involution on D_R.
   - It preserves P (R4, Lemma K), hence L (R2).
   - It preserves μ̃ on Γ × Γ, by Lemma S (right version).
3. *The image is one left cell.* For w, w′ ∈ Γ we have w ≤_L w′ ≤_L w. Every element on a chain realising w ≤_L w′ lies between w and w′ ~_L w, so the chain stays inside Γ ⊆ D_R. ρ maps each link (μ̃ ≠ 0, L ⊄ L) to a link, so ρw ≤_L ρw′, and symmetrically. Hence ρ(Γ) ⊆ Γ_{Q″} with Q″ = Q(ρ w) for any w ∈ Γ.
4. *Equality.* The P-values on ρ(Γ) are all of SYT(λ), so Q″ has shape λ and |ρ(Γ)| = f^λ = |Γ_{Q″}|. Thus ρ(Γ) = Γ_{Q″}.
5. *Compose.* Apply step 2–4 along the chain from step 1. The cell containing ρ_{j_m}⋯ρ_{j₁}(P₀,Q) is the next domain, and the last one is Γ_{Q′}.
6. *Twins transport.* (TW), together with L(z) ⊆ L(x) and x ≠ z, is expressed in L and μ̃ over y ∈ Γ, so φ carries it across. Since P(φx) = P(x) and φx ∈ Γ_{Q′}, we get φx = (T, Q′). ∎

Remarks.
- Q(ρ_j w) depends only on Q(w). This is Haiman's elementary dual equivalence, and it falls out of step 3 without being cited.
- Lemma P's parity is Q-independent too: each right star changes both lengths by ±1.
- `prove281/dualconn.py` (computed connectivity) and `randQ.py` (53/53 re-decisions in random cells) are now *controls* of Prop Q, not premises.

## 6. Certificates: what each one proves (Proposition C)

The census certificates (`certifyn.py` → `verifyn_u.py` / `verifyn_ext.py`, `verify_red.py`) are explicit finite objects, and each is replayed by code with no shared logic. Here is what each type proves.

1. **Star path + endpoint.** A sequence of simultaneous left stars (both entries in D_L at every step) and right stars (both in D_R) takes (a, b) to (a′, b′). By Lemma S and its right version, μ̃(a,b) = μ̃(a′,b′). The verifier asserts membership at every step. The endpoint then gives:
   - μ̃ = 1 if the elements are comparable with gap 1 (K5);
   - μ̃ = 0 if the gap is even, the elements are Bruhat-incomparable (K5), or some r ∈ L(hi) \ L(lo) has r·hi ≠ lo (F1).

   Bruhat is checked by the rank-matrix criterion.
2. **Layer certificate** (5 pairs of shape (5,5,3,3)). A star path reaches a pair with letter 16 (or 1) at the same position. The Layer Lemma gives P_{y,z} = P_{y∖v, z∖v}. A further star path in S_15 ends at an incomparable pair, so μ = 0.
3. **Ext certificate** (2 pairs of shape (6,4,3,3)). A right-star path reaches the literal dyer2 input pair, and μ is read from the dyer2 output after the lengths and the μ-index are checked.
4. **Verdict rule.** TWIN ⟺ every y in W_i ∪ {certified μ̃(y,x) = 1 elements of Des ⊋ A} has certified μ̃(y,z) = 1, and no μ̃(y,x) with Des P_y ⊋ A is undecided. NO ⟺ some such y has certified μ̃(y,z) = 0.

By Theorem W, both rules are exactly (TW). Note that μ̃(y,z) = 1 ≥ μ̃(y,x) = 1 needs exactness of μ̃(y,x), and type 1 certificates give exact values.

**Proposition M (the census needs ONE computed μ).** Put:
- x₀ = [5,4,3,1,9,8,7,2,15,14,11,6,13,10,12,16], z₀ = [14,8,4,1,15,9,5,2,16,10,6,3,11,7,12,13] (`prove283/in0.txt`; l = 33, 52);
- (x₀ᵇ, z₀ᵇ) = `in0b.txt` (l = 34, 53);
- (x₁ᵇ, z₁ᵇ) = `in1b.txt` (l = 35, 54);
- c(w) = w₀ww₀.

Then:
- (x₀ᵇ, z₀ᵇ) = ρ₃(x₀, z₀), with both entries in D_R(s₃,s₄);
- (x₁ᵇ, z₁ᵇ) = ρ₁₃ρ₁₁(c x₀, c z₀).

Hence μ(in0b) = μ(in1b) = μ(x₀, z₀), by Lemma S (right) and (K4).

*Proof.* Explicit (`prove284/link.py`, BFS over simultaneous right stars, endpoint compared literally; `out_link.txt`).
By hand, the first move is the Knuth move on positions 3–5: 3,1,9 ↦ 3,9,1 in x₀ and 4,1,15 ↦ 4,15,1 in z₀. Both are yxz ↦ yzx. ∎

**μ(x₀, z₀) = 1 is COMPUTED**, by two independent implementations:
- `prove283/dyer2.c` (Dyer path formula, coset mode);
- `prove283/verify_indep/` (from-scratch Deodhar parabolic KL on W^J, J = R(z₀), with a 22,208-element W^J interval).

They give the same P_{x₀,z₀} = 1+12q+62q²+181q³+328q⁴+381q⁵+279q⁶+119q⁷+26q⁸+q⁹. dyer2 run directly on in0b and in1b agrees. Neither code was validated beyond S_6 against an external reference. Prop M upgrades the earlier caveat "inst 1 has no independent replay" to "inst 1 is *proved* equal to inst 0, which has two independent computations".

## 7. The census, n ≤ 16

**n ≤ 13: no candidate pairs, hence no twins** (Thm C3; exhaustive Kostka-dominance check `dominance_star.py`, cross-checked by SYT enumeration for n ≤ 11).

**n = 14** (P280, re-certified P281): 4 candidate pairs, **4 TWIN**.

| λ | pairs | TWIN |
|---|---|---|
| (4,4,3,3), (5,3,3,3), (4,4,4,2), (4,4,4,1,1) | 1 each | 1 each |

**n = 15** (P281): 48 candidate pairs, **26 TWIN / 22 NO**. The NO verdicts are 20 parity and 2 Prop-U (W_ii) kills.

| λ | pairs | TWIN | NO |
|---|---|---|---|
| (6,3,3,3) | 4 | 4 | 0 |
| (5,4,4,2) | 3 | 1 | 2 |
| (5,4,4,1,1) | 3 | 1 | 2 |
| (5,4,3,3) | 12 | 4 | 8 |
| (5,3,3,3,1) | 3 | 1 | 2 |
| (4,4,4,3) | 4 | 4 | 0 |
| (4,4,4,2,1) | 12 | 6 | 6 |
| (4,4,4,1,1,1) | 4 | 4 | 0 |
| (4,4,3,3,1) | 3 | 1 | 2 |

**n = 16** (Wake 282, P282, P283): 410 candidate pairs, **114 TWIN / 296 NO / 0 undecided**. The NO verdicts break down as:
- 186 parity;
- 19 with a (ii)-kill;
- 86 (i)-only kills;
- 5 layer certificates.

| λ | pairs | TWIN | NO | note |
|---|---|---|---|---|
| (7,3,3,3) | 10 | 10 | 0 | |
| (6,4,4,2) | 6 | 1 | 5 | |
| (6,4,4,1,1) | 6 | 1 | 5 | |
| (6,4,3,3) | 54 | 11 | 43 | 2 TWIN rest on μ(x₀,z₀) (Prop M) |
| (6,3,3,3,1) | 12 | 4 | 8 | |
| (5,5,4,2) | 3 | 0 | 3 | |
| (5,5,4,1,1) | 3 | 0 | 3 | |
| (5,5,3,3) | 18 | 4 | 14 | 5 NO by layer certificates |
| (5,4,4,3) | 43 | 9 | 34 | |
| (5,4,4,2,1) | 48 | 6 | 42 | |
| (5,4,4,1,1,1) | 12 | 4 | 8 | |
| (5,4,3,3,1) | 48 | 6 | 42 | |
| (5,3,3,3,2) | 3 | 0 | 3 | |
| (5,3,3,3,1,1) | 6 | 1 | 5 | |
| (4,4,4,4) | 4 | 4 | 0 | |
| (4,4,4,3,1) | 43 | 15 | 28 | |
| (4,4,4,2,2) | 18 | 9 | 9 | |
| (4,4,4,2,1,1) | 54 | 18 | 36 | |
| (4,4,4,1,1,1,1) | 10 | 10 | 0 | |
| (4,4,3,3,2) | 3 | 0 | 3 | |
| (4,4,3,3,1,1) | 6 | 1 | 5 | |

Replay today (`prove284/out_rerun.txt`, `rerun.sh`): every certificate file for n = 14, 15, 16 was replayed with `verifyn_ext.py`, and the (5,5,3,3) layer certificates with `verify_red.py`. The counts are in §7a.

**Why "computed (certificate-complete)" and not "proved".** Each verdict is a finite, explicit, replayed derivation from the §2 inputs, Lemma S, the Layer Lemma, Theorem W and Prop Q. It is a computer-assisted theorem of the usual kind, with one exception: the single number μ(x₀, z₀), which no human can check and which rests on two codes validated only to S_6. I grade the census *computed*, with the dependency list above as its exact content. If μ(x₀,z₀) were 0, the census would read 112/298, and pairs 353 and 364 would flip to NO. Nothing else would change.

### 7a. Replay counts

Replayed 2026-11-08 (`prove284/out_rerun.txt`, 0 errors):

| n | source | replay result |
|---|---|---|
| 14 | `wake282/certs14_*.json` | 4 TWIN OK |
| 15 | `prove281/certs15_*.json` (9 shapes) | 26 TWIN, 22 NO, all OK |
| 16 | `wake282/certs16_*.json` (21 shapes) | 112 TWIN, 291 NO, 7 UNDECIDED, all OK |
| 16 | `prove282/verify_red.py rest16.json` | the 5 (5,5,3,3) UNDECIDED → incomparable endpoint (μ = 0) ⇒ NO |
| 16 | `prove283/certs16_6433_ext.json` | 352 NO, 353 TWIN, 364 TWIN, 365 NO, all OK |

Net for n = 16: 112 + 2 = **114 TWIN**, 291 + 5 = **296 NO**. This matches §7.

## 8. What died on this arc (counterexamples)

| hunch | killed by | grade of refutation |
|---|---|---|
| Q68(c) simply-laced "no twins" | T14: (4,4,3,3) twin in S_14 | proved (certificate) |
| (★)-violator ⟺ twin, (λ,A) level | S_15: 22 non-twin candidates (20 parity, 2 Prop U) | proved (certificate) |
| shape level "violation ⟺ twin" | S_16: (5,3,3,3,2), (4,4,3,3,2), (5,5,4,2), (5,5,4,1,1) carry violations, have no twin | proved (certificate) |
| sieve R1 "twin ⟺ parity OK and W_ii = ∅" | S_16: 86 false positives killed by W_i | proved (certificate) |
| "(ii) always kills" (Q68-ii-kills) | S_16 pairs 352/365 (and 353/364): μ̃(y,z) = 1 at the (ii)-element | computed (μ(x₀,z₀)) |
| Lemma I (x-free: μ(x,z) = 0 for candidate pairs) | open26 insts 0, 1, 11, 13, 14: μ = 1 | computed (inst 13: two implementations; inst 0: two; 1 = 0 by Prop M; 11, 14 Dyer only, 12 = mirror of 11) |
| Lemma I′ (non-tight) | insts 0, 1 | computed |
| Crown U "Lemma I = Stembridge arc rule" | Lemma I false | — |

Inst 13 by itself kills Lemma I independently of the census and of μ(x₀,z₀):
x = [7,3,2,11,10,6,5,1,15,9,8,4,16,14,13,12], z = [10,6,2,14,11,7,3,1,15,12,8,4,16,13,9,5], P_{x,z} = 1+8q+24q²+35q³+26q⁴+9q⁵+q⁶.

## 9. Gaps (precise)

1. **μ(x₀, z₀) = 1 is computed, not proved.** This is the only non-certificate input to the census. It affects 2 of the 410 n = 16 verdicts, and the refutations of ii-kills and Lemma I′.
2. The §2 inputs are recall-only: the KL79 recursion, positivity, inverse and automorphism invariance, RSK, Knuth's theorem, and left cells = {Q fixed}. All are textbook, and all were validated small.
3. The enumeration codes (`dominance_star.py`, `listn.py`) are trusted as exhaustive. They have independent cross-checks at small n (SYT enumeration n ≤ 11; P280 list reproduced by listn at n = 14).
4. Not addressed, and by decision not opened: n ≥ 17; any structural criterion for twins beyond Theorem W; the non-type-A picture beyond Thm B.
