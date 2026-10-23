# The symbol theorem and the inversion duality: one rule for every u→0 tie, and u→∞ for free (PROVE 249)

Rick, 2026-10-21. Continues `proofs/2026-10-20-dual-block-identity.md` (notation: Φ_r^M, S₀^M, A_{κ,θ}, Lemma A, Lemma H,
Lemma Λ, Lag, γ_k). Scripts: `work-in-progress/scripts/prove249b/`.

## 0. Verdict

| item | statement | grade |
|---|---|---|
| **Lemma P∞** (Clio's Q532, cold) | On a consecutive label block with slope −1 twist, Ψ_{κ,θ} = C·Ψ_{κ,θ′}, θ′ constant e = t₀−(b−1) on the block, C = Π_{m=0}^{b−2} w_{κ_p+m}^{b−1−m}. | **proved** (§1, my own derivation; Clio's claim) |
| **Lemma I** (inversion duality) | Ψ_{κ,θ}(M)\|_{w↦1/w} = (−1)^{\|κ\|} e_M^{2r} W_κ^{−1} Ψ_{κ,θ^∨}(M), θ^∨_j = κ_j − 2j + 1 − θ_j. | **proved** (§2) + exact 7/7, control breaks |
| **Cor. I1** | The certifier's whole u→∞ option calculus is the ι-conjugate of its u→0 calculus. Every u→0 lemma (P, P\*, P1, P1′, P2, Thm S) has an automatic u→∞ twin. | **proved** (§2) + code identity 13 083/13 083 |
| **Cor. I2** (λ-side P1, all r) | Ψ_{[r−1],−r}(S) + (−1)^r Ψ_{[r],1−r}(S) = e_S^{−2} Ψ_{[r−1],2−r}(S) is P1 under ι. | **proved** (§2) |
| **Theorem S** (symbol theorem) | The u→0 leading coefficient of Ψ_{κ,θ}(M) is read off from o = ord_z A_{κ,θ}(x′,z): head symbol if o ≤ 0, tail if o ≥ 2, and at the tie o = 1 an exact two-term "∞-form". P1, P1′, P2 and the multi-block tie (α) are all special cases. | **proved** (§3) + exact 9/9 + R2 6/6, 3 breaking controls ×3 |
| **Tie census** | All psi-level ties at A N≤6, C n≤6, by family. (α) occurs (e.g. κ=(1,3), θ=(2,2)). | computed (§4) |
| **Certifier v8** | scert7 + ι-conjugated P-branches at u→∞. A N=5,6: 0 uncertified. Negative control 0/1300 false. Mutants 242 / 155 false. Pure-u→∞ policy: 924 → 51 uncertified at A5. | computed (§5) |

**Headline.** (α) is not a new identity to hunt for. It is the o = 1 case of a single rule, Theorem S, that gives the exact
u→0 leading coefficient of *every* twisted instance. In that rule P1, P1′ and P2 are the cases "one block". What remains for
the all-N upper end is (SC) alone, the non-cancellation of iterated leading coefficients (§6).

## 1. Lemma P∞ (Clio, Q532): cold derivation

**Lemma P∞.** Let κ have a consecutive block at positions p..q (κ_{p+m} = κ_p + m), b = q − p + 1, and let θ_{p+m} = t₀ − m on
the block, with θ arbitrary elsewhere. Put e = t₀ − (b−1), let θ′ agree with θ off the block and equal e on it, and set
a_m = w_{κ_p+m}. Then for every M,
  Ψ_{κ,θ}(M) = C · Ψ_{κ,θ′}(M),  C = Π_{m=0}^{b−2} a_m^{b−1−m}.

*Proof.* By Lemma A it suffices to show A_{κ,θ} = C·A_{κ,θ′}, i.e. det[F_j(x_i)] = C·det[F′_j(x_i)]. Put c = p − 1 + t₀ and
π_m(y) = Π_{i<m}(y − a_i). Column p+m of each matrix is:
- F_{p+m}(y) = y^{c}ρ_{κ_p}(y)Π_{i<m}(1 − a_i/y) = y^{c−b+1}ρ_{κ_p}(y)·P_m(y), with P_m := y^{b−1−m}π_m(y);
- F′_{p+m}(y) = y^{p+m−1+e}ρ_{κ_p+m}(y) = y^{c−b+1}ρ_{κ_p}(y)·π_m(y).

Both {P_m} and {π_m} (m = 0..b−1) lie in the space of polynomials of degree ≤ b−1, and the π_m are a basis of it. So
P_m = Σ T_{mm′}π_{m′} with constant T. By multilinearity, det[F] = det T · det[F′], since the other columns are untouched.

Compute det T in the monomial basis:
- π is unitriangular in (1, y, …, y^{b−1}).
- P_m = Σ_{k=0}^{m}(−1)^k e_k(a_0..a_{m−1}) y^{b−1−k} is lower triangular in (y^{b−1}, …, 1), with diagonal (−1)^m a_0⋯a_{m−1}.
- Reordering the basis is the reversal, of sign (−1)^{C(b,2)}, which cancels Π_m(−1)^m.

Hence det T = Π_m Π_{i<m} a_i = Π_i a_i^{b−1−i} = C. ∎

*Sign line, general position (added Wake 252, at Clio's request, uid438 §1).* When the block sits inside a larger κ
(p > 1 or q < r), compare column by column; no column outside p..q is touched, so no sign arises outside the block.
Inside the block, the slope reduction writes the columns F_{p+m} in the monomials y^{c−b+1}ρ_{κ_p}(y)·y^k with k
*decreasing* (k = b−1−m down to 0, leading coefficients (−1)^m a_0⋯a_{m−1}), while the constant-twist reduction writes
F′_{p+m} in the same monomial set with k *increasing* (unitriangular). Putting both in one ordered basis reverses b
columns, which contributes (−1)^{C(b,2)}; this cancels Π_{m=0}^{b−1}(−1)^m = (−1)^{C(b,2)} from the leading
coefficients. In the whole-κ case (p = 1, q = r) these are exactly the "two signs that cancel". Same cancellation,
different packaging; the conclusion det T = C is unchanged.

*Credit.* Statement: Clio (Q532, UID 424, 2026-10-20). Proof: Rick, via Lemma A (dual-block note §1). Clio endorsed
the proof as proved in her 2026-10-22 review (UID 438), re-deriving Lemma A independently (18/18) and checking the
alternant step fully symbolically in 6 configurations.

Remarks.
- The proof uses nothing about M, and nothing about θ off the block.
- Theorem B's Ψ_{(s,s+1),(1,0)} = w_sΨ_{(s,s+1),(0,0)} is the case b = 2, t₀ = 1.
- Via §2, P∞ is what Cor. A1 (constant twist ↦ product form) looks like after ι: constant twists become slope −1.
- Checks: `prove249/q532.py` (10/10, 3 breaking controls), Clio 13/13. This section is the cold read owed by PROVE 249 item 1.

## 2. Lemma I: the inversion duality

Write ι for the substitution w_k ↦ 1/w_k (all k), and f^ι for its effect on a function of w.

**Lemma I.** For κ_1 < … < κ_r, any θ ∈ ℤ^r and any M,
  Ψ_{κ,θ}(M)^ι = (−1)^{|κ|} e_M^{2r} W_κ^{−1} Ψ_{κ,θ^∨}(M),  θ^∨_j := κ_j − 2j + 1 − θ_j,  W_κ := Π_j W_{<κ_j}.
Note that θ^{∨∨} = θ.

*Proof.* Use Lemma A, Ψ = Σ_H S₀^M(H)A(x_H), and apply ι termwise. In each line below, the left side is the ι-image of a factor
of S₀^M(H) and the right side rewrites it in terms of the original factor.
- head: (1 − x^{−2})^ι = (1 − x²) = −x²(1 − x^{−2});
- pair: (1 − 1/(x_jx_k))^ι = −x_jx_k(1 − 1/(x_jx_k));
- tail: ((x − 1/w)/(x − w))^ι = (1/x − w)/(1/x − 1/w) = w²(x − 1/w)/(x − w).

So S₀^M(H)^ι = (−1)^{r + C(r,2)} e_H^{2+(r−1)} e_{M∖H}^{2r} S₀^M(H) = (−1)^{C(r+1,2)} e_M^{2r} e_H^{1−r} S₀^M(H).

For the alternant:
- ρ_κ(x)^ι = Π_{k<κ}(1 − x/w_k) = (−1)^{κ−1}W_{<κ}^{−1}x^{κ−1}ρ_κ(x).
- So column j, F_j(y) = y^{j−1+θ_j}ρ_{κ_j}(y), becomes (−1)^{κ_j−1}W_{<κ_j}^{−1}y^{κ_j−j−θ_j}ρ_{κ_j}(y) = (−1)^{κ_j−1}W_{<κ_j}^{−1}F^∨_j(y),
  where F^∨_j is column j for θ^∨: (j−1) + θ^∨_j = κ_j − j − θ_j.
- V(x)^ι = Π_{i<k}(1/x_k − 1/x_i) = (−1)^{C(r,2)}e^{−(r−1)}V(x).

Hence A_{κ,θ}^ι = (−1)^{Σ(κ_j−1)+C(r,2)} W_κ^{−1} e^{r−1} A_{κ,θ^∨}. Multiplying:
- the e_H powers cancel;
- the sign is (−1)^{C(r+1,2)+C(r,2)+|κ|−r} = (−1)^{r²+|κ|−r} = (−1)^{|κ|}. ∎

Check `prove249b/inv.py`: 7/7 exact at random rational points, for r = 1, 2, 3, consecutive and gapped κ, and twists of both
signs. The control θ^∨ without the +1 breaks.

**Cor. I1 (u→∞ = ι-conjugate of u→0).** Let κ_r < n, u = w_n. Then u^{±1} → 0 is exchanged by ι. Apply Lemma I twice (to the
parent, and to each child at |M⁻| and r′ labels). A u→0 option of Ψ_{κ,θ^∨}(M),
  u^o (−1)^s w^δ e_{M⁻}^{ws} Ψ_{κ′,φ}(M⁻),
becomes the u→∞ option of Ψ_{κ,θ}(M)
  u^{−2r−o} (−1)^{|κ|+s+|κ′|} W_κW_{κ′}^{−1}w^{−δ} e_{M⁻}^{−2r−ws+2r′} Ψ_{κ′,φ^∨}(M⁻).

Check by hand:
- Tail (o = −r, φ = θ^∨ − 1): order −r, sign (−1)^r, child Ψ_{κ,θ+1}. This holds because (θ^∨ − 1)^∨ = θ + 1.
- Head j (o = θ^∨_j − κ_j − 1 − (r−j), ws = −2): order θ_j − (r−j), sign (−1)^{r−j}, no scalar, e-power 0, child twist
  θ_i (i < j) and θ_{i+1} + 1 (i ≥ j).

That is exactly the u→∞ branch of `psi_opts` in scert1–7. Code identity: `prove249b/chk8.py` compares the ι-transform of the
generic u→0 options with the direct u→∞ options over all r ≤ 3, κ ⊆ [7], θ ∈ [−3,3]^r: **13 083 cases, 0 mismatches**.
Consequently P, P\*, P1, P1′, P2 and Theorem S below all hold at u→∞ after conjugation. This is the full set of "u→∞ tools"
PROVE 249 asked for, and no separate ∞-derivations are needed.

**Cor. I2 (λ-side P1, all r).** Apply ι to P1, Φ_r^S[1] + e_S^{−2}Φ_{r−1}^S[e²] = Φ_{r−1}^S[1].
- κ = [r] has ρ ≡ 1, so Φ_r[e^t]^ι = (−1)^{C(r+1,2)}e_S^{2r}Φ_r[e^{1−r−t}].
- This gives (−1)^{C(r+1,2)}Φ_r[e^{1−r}] + (−1)^{C(r,2)}Φ_{r−1}[e^{−r}] = (−1)^{C(r,2)}e_S^{−2}Φ_{r−1}[e^{2−r}].
- Dividing by the common sign gives Ψ_{[r−1],−r} + (−1)^rΨ_{[r],1−r} = e_S^{−2}Ψ_{[r−1],2−r}.

This is the identity Wake 249 found by fit search (r = 1..4, 10/10). It is now proved for all r. Likewise the "recurring tie"
1 − Ψ_{(2),0}(S) = e_S^{−2} + w_1Ψ_{(1),−1}(S) of `q532tie2.py` is ι of the label lowering Ψ_{(2),1} = Ψ_{(1),1} − w_1Ψ_{(1),0}
combined with the (1)-identity.

## 3. Theorem S: the symbol theorem

Setting: n ∈ M, u = w_n, M⁻ = M∖n, κ_r < n, θ ∈ ℤ^r. A := A_{κ,θ} is a symmetric Laurent polynomial in x_1..x_r over
K = ℚ(w_k : k < κ_r), so it is free of u. Regard A(x′, z) (x′ = r−1 variables, z the last) as an element of K[x′^±][z^±]. Let
  o := ord_z A(x′, z),  a_k(x′) := [z^k] A(x′, z).

**Theorem S.** As u → 0:
1. If o ≤ 0: Ψ_{κ,θ}(M) = (−1)^r e_{M⁻}^{−2} u^{o−r−1} ( Φ_{r−1}^{M⁻}[ e·a_o ] + O(u) ).
2. If o ≥ 1: Ψ_{κ,θ}(M) = (−1)^r u^{−r} ( Ψ^∞ + O(u) ), where
   Ψ^∞ = Ψ_{κ,θ−1}(M⁻) + e_{M⁻}^{−2}Φ_{r−1}^{M⁻}[e·a_1]  (tail + tied heads; the second term is 0 if o ≥ 2)
       = Φ_{r−1}^{M⁻}[b_0] + Φ_r^{M⁻}[B],
   with b := A/e = A_{κ,θ−1} (a polynomial), b_0 := b(x′, 0) = a_1/e(x′), and B := b − Lag b_0. Moreover B = e·B′ with B′ a
   symmetric polynomial.

Here e = e(x′) or e(x) is the product of the variables, and "+O(u)" means the next terms of a Laurent series in u. The bracket
is the exact coefficient at the stated order. If it vanishes, the true order is higher.

*Proof.* Lemma H splits Φ_r^M[A] exactly into T(u) + Hd(u).

Tail.
- T(u) = Φ_r^{M⁻}[A·Π_j(ux_j − 1)/(u(x_j − u))].
- Π_j(ux_j − 1)/(u(x_j − u)) = (−1)^r u^{−r} e(x)^{−1} Π_j(1 − ux_j)/(1 − u/x_j).
- So T = (−1)^r u^{−r}(Φ_r^{M⁻}[A/e] + O(u)), and A/e = A_{κ,θ−1}.

Head.
- Hd(u) = (1 − u^{−2})g_{M⁻}(u)u^{−(r−1)}Φ_{r−1}^{M⁻}[A(x′,u)Π_j(u − x′_j)].
- The function A(x′,u)Π_j(u − x′_j) is a Laurent polynomial in u. Its lowest term is u^o·a_o(x′)·Π_j(−x′_j) = (−1)^{r−1}e(x′)a_o(x′)u^o.
- (1 − u^{−2})g_{M⁻}(u)u^{−(r−1)} = −e_{M⁻}^{−2}u^{−r−1}(1 + O(u)), since g_{M⁻}(0) = Π_t w_t^{−2}.
- Φ_{r−1}^{M⁻} is linear over u-free scalars. So Hd = (−1)^r e_{M⁻}^{−2}u^{o−r−1}(Φ_{r−1}[e·a_o] + O(u)).

Comparing the orders o − r − 1 and −r gives case 1 (o ≤ 0) and the first form of case 2.

Second form.
- b = A/e has z-order o − 1 ≥ 0 in each variable (by symmetry), so b is a polynomial.
- Lemma Λ (dual-block file §4) gives Φ_r^{M⁻}[b] = −Σ_{H′}S₀^{M⁻}(H′)(Res_0 + Res_∞)[z^{−1}G_{S}(z)b(x′,z)], with S = M⁻∖H′.
- Since b is polynomial in z, Res_0 = G_S(0)b_0 = e_{M⁻}^{−2}e(x′)²b_0(x′). The Res_0-part is therefore −e_{M⁻}^{−2}Φ_{r−1}[e²b_0] = −e_{M⁻}^{−2}Φ_{r−1}[e·a_1].
- So Ψ^∞ = Σ_{H′}S₀(H′)[z⁰]_∞(G_S(z)b(x′,z)).
- Partial fractions: G_S(z) = 1 + Σ_{t∈S}S₀^S({t})x_t/(z − x_t). This uses Res_{z=w_t}z^{−1}G_S = S₀^S({t}), and needs w distinct and nonzero.
- Also [z⁰]_∞(b(x′,z)·x_t/(z − x_t)) = b(x′,x_t) − b_0(x′).
- The Lagrange ratio S₀^{M⁻}(H′)S₀^{M⁻∖H′}({t}) = S₀^{M⁻}(H′∪t)Π_{j∈H′}x_j/(x_j − x_t) (P1 step 1) folds the double sum into
  Φ_r^{M⁻}[Σ_{t∈H}(b(x_H) − b_0(x_{H∖t}))Π_{j≠t}x_j/(x_j − x_t)].
- Σ_tΠ_{j≠t}x_j/(x_j − x_t) = 1 (Lagrange interpolation of 1 at 0), so this equals Φ_r[b − Lag b_0].

Divisibility of B.
- Lag b_0 is symmetric, with numerator antisymmetric over V, so it is a polynomial.
- At x_t = 0, every term of Lag b_0 with t′ ≠ t carries the factor x_t/(x_t − x_{t′}) = 0. The t-term is b_0(x_{H∖t}). So B|_{x_t=0} = b(…,0,…) − b_0 = 0.
- A symmetric polynomial vanishing on every coordinate hyperplane is divisible by e. ∎

**What Theorem S replaces.**
- Lemma T's option list, P\*, and the cross-block head/head ties are all formal decompositions of the single symbol a_o. By the
  Laplace identity (H′), (−1)^{r−1}e(x′)a_o(x′) = Σ_{j: o_j = o}(−1)^{r−j}[z^{o_j}]F_j·A_{κ∖κ_j,θ^{(j)}}(x′), where
  o_j := θ_j + j − κ_j = ord_0F_j, whenever no column cancellation lowers o. So the formal sums the certifier carries are
  exact, in every case.
- The tie o = 1 is case 2, and the second form is the "resolution":
  - **P1** (κ = [r], θ ≡ 1): b = 1, b_0 = 1, Lag 1 = 1, B = 0, so Ψ^∞ = Φ_{r−1}[1] = Ψ_{[r−1],0}.
  - **P1′** (r = 1): Φ_0[b_0] = b_0 = b(0), and Φ_1[b − b(0)] = Σ_{k≥1}b_kγ_k.
  - **P2** (κ = (s..s+m−1), θ ≡ s): b = Π(x_j|w)^{s−1}.
    - Φ_{r−1}[b_0] = (−1)^{s−1}W_{<s}Ψ_{κ⁻,s−1}.
    - B = Σ_{k≥1}e_{s−1−k}(−w_{<s})Lag_kΠ_{j∈H′}(x_j|w)^{s−1}, which is P2's i-sum (P2 step 6).
  - **(α)** (several blocks, any tied set): the same formula, nothing new needed. In instance language,
    b_0 = Σ_{j∈J}(−1)^{κ_j+j}W_{<κ_j}A_{κ∖κ_j,θ^{(j)}−2}, where J = {j : o_j = 1}. Also Lag_k A_{κ′,φ} = A_{(1)∪κ′,(k)∪φ}
    (determinant with first column y^k, other columns multiplied by y; P2 step 6). So B = A_{κ,θ−1} − Σ_{j∈J}(−1)^{κ_j+j}W_{<κ_j}A_{(1)∪(κ∖κ_j),(0)∪(θ^{(j)}−2)}.
    This is a finite signed sum of alternants with r columns, so it is certifier-compatible after label rewriting.

**Checks** (`prove249b/sym.py`, `symctl.py`, `r2.py`; u symbolic, the other w random rationals, exact):

| case | (κ, θ, M) | result |
|---|---|---|
| o = 0 | (1,3),(0,1),(1,2,3,4) | order and coefficient match |
| o = −1 | (2,4),(0,1),(1,2,4,5) | match |
| o = 0 | (1,2,4),(0,0,1),(1,2,3,4,5); (1,3,4),(0,1,1),(1,3,4,5); (1,3),(3,1),(1,2,3,4) | match |
| o = 1, (α) | (1,3),(2,2); (1,3),(1,2) (three-way: tail + both heads); (2,4),(3,3) | match |
| o = 1, non-constant twist | (1,2),(1,2) | match |
| R2 form | (1,3),(2,2) → B = e; (1,3),(1,2) → **B = 0**; (1,2),(1,2) → **B = 0**; (2,4),(3,3) → B = e·(…); (1,2,4),(1,1,2) → **B = 0**; (2,3),(2,2) → B = e | 6/6 match, e \| B 6/6 |
| controls | tail only / head only / head sign flipped, on three o = 1 cases | 9/9 break |

When B = 0 the tie collapses to a single object with r − 1 labels, exactly like P1. This happens in three of the six tested
o = 1 cases.

## 4. Tie census (which tie families actually occur)

`prove249b/alpha.py` wraps `psi_opts` and logs every call in which ≥ 2 options reach the extremal order. P1′/P2 calls, which are
multi-output by design, are counted separately.

| family | example (lim, κ, θ) | A N=6 | C n=6 |
|---|---|---|---|
| T1 cross-block head/head, o ≤ 0 (Thm S case 1) | (0,(1,3),(0,1)): heads 1, 2 at −3 | 168+49+6+5 (incl. (2,4),(0,1); (1,2,4),(0,0,1); (1,3,4),(0,1,1)) | 491+105+66+55 |
| T2 tail + non-bottom block = **(α)** (case 2) | (0,(1,3),(2,2)); three-way (0,(1,3),(1,2)) | 3 + 6 | 28 + 56 |
| T3 tail + head, non-constant single block (case 2) | (0,(1,2),(1,2)) | 5 | 83 |
| T4 u→∞ ties (ι-images of T1–T3) | (1,(1,2),(1,0)), (1,(1,3),(2,1)), (1,(2,3),(0,−1)), (1,(1,2),(−1,−2)), (1,(2,),(−1,)) | 7 | 398 |
| P1′/P2 (by design) | | 100 | 319 |

A N=5 has only T1 (3×) and one P1′.

The **multi-summand nodes** (after selection and canonicalisation) are 36 at A5 and 696 at A6, the same under v7 and v8. Every
one of them is one of:
- a P1′/P2 output, Σ±e_i(w_{<s})Ψ_{(1),k};
- its pure-scalar descendants (e.g. 1 + w_1/w_2);
- an 'eq'-split in/out node (family (γ)).

**None is an (α) node.** So PROVE 249 item 3's hope ("the 36 A5 multi-summand nodes disappear under P∞/P1∞") was moot.
Those nodes are (γ)/(δ) by type, not (α).

## 5. Certifier v8 (`prove249b/scert8.py`)

v8 is scert7 with one change. At u→∞ (generic κ, κ_r < n, not the (1),(−1) special case), the options are computed as the
ι-conjugate (Cor. I1) of the u→0 options of Ψ_{κ,θ^∨}, *including* the P/P\*/P1/P1′/P2 branches. Previously these branches acted
only at u→0.

| run | result |
|---|---|
| generic-branch code identity vs direct u→∞ (`chk8.py`) | 13 083 / 13 083 |
| A N=5 / N=6, default policy (u→0 first) | 0 / 5 578, 0 / 68 791 uncertified. PSTAT identical to v7, because u→0 always succeeds first. |
| A N=5, **u→∞-only policy** | v7: 924 uncertified; **v8: 51**. All 51 have ν = [5] and λ or μ = (1,3,4), a two-block label set. Trace: the failure is at the A→B (n = b) step, where the node cleans to empty. |
| negative control (A N=4,5 known zeros, eq-c mode) | **0 / 1 300 false**; 46 194 / 46 588 nonzero certified |
| mutant θ^∨ without +1 | 242 false certifications |
| mutant child sign flipped | 155 false certifications |

So the ι-branch is sound (the control has teeth) and does real work. Under a pure u→∞ policy, which is a second, independent
peel policy, the mirrored lemmas remove 94% of the failures.

## 6. What remains for the all-N upper end (precise)

After Theorem S there is no tie family left without an exact closed form. At every node, at either limit, the leading
coefficient is one of:
- the head symbol (o ≤ 0);
- the tail (o ≥ 2);
- Ψ^∞ = Φ_{r−1}[b_0] + Φ_r[B] (o = 1),

each an explicit finite sum of twisted instances. The (1)-, P- and ι-rules are special cases. Items (α) and (δ) of the
dual-block file's §6 are both "Theorem S at o = 1". (β) is (α)/T1 on the λ/μ side, which is the same theorem applied to the
F-factors (or to their ι-images at u→∞).

What is **not** proved is

> **(SC)** For every allowed root with c > U^X_N, some peel policy makes every selected leading coefficient non-zero down to
> the base, and the base count is σ = ±1.

Theorem S gives the *value* of each leading coefficient as an exact sum. What it does not give is a reason why the sum
does not cancel at the next step. Cancellation is a property of the *sum*, of the order data of its summands at the next
variable, and Theorem S is a one-step statement. The census (σ ∈ {±1} at every base, A ≤ 7, B/C ≤ 6) says cancellation never
happens. New evidence this session (`prove249b/base8.py`, v8, A N=5): the base counts are
- u→0-first policy: 2736 × (−1), 2863 × (+1);
- u→∞-first policy: 2269 × (−1), 3309 × (+1).

No 0 and no |σ| ≥ 2 occurs under either policy. The two policies land on *different* extremal monomials of the same X, and
both have coefficient ±1. That points to an intrinsic reason (every lex-extremal monomial of X is a ±monomial, as for a
product of binomials), not a lucky policy. A proof needs an invariant carried down the peel. Candidates:
- the B = 0 / B = e·B′ dichotomy;
- the GKM triangularity of GQ, via K0, which is the natural source of "±1 at the diagonal".

This is K2 and was not attempted this session.

> **Cycle 2 update (same day):** (SC) is superseded by the centre polynomial. See
> `proofs/2026-10-21-window-hilbert-polynomial.md`: Lemma E (proved) reduces the all-N upper end to HP (no integer root of
> the w→1 polynomial P above U), and HP⁺ is computed exactly at C n ≤ 4 and A N ≤ 4.

## 7. Gaps

1. (SC) is open (§6). This is the only remaining gap for Z^A_N = [0, 2N−4] at all N, apart from the inherited Motegi root.
2. K1 (twisted Ψ vs GQ·[O(θ)], K-Chevalley) was not started. It needs first-hand Buch–Ravikumar (Crelle 668, 2012) [Wake 252: Mihalcea–Naruse–Su 2312.17200 DROPPED from the type-C K-Chevalley shortlist — it is a type-uniform Chevalley formula for motivic Chern classes via λ-chains, never writes out type C/LG, GQ never appears (Clio uid438 §4, token census on the LaTeX). Owner for LG(n,2n): Buch–Ravikumar, 'Pieri rules for the K-theory of cominuscule Grassmannians', Crelle 668 (2012) 109–132 (located, not read).], which
   is off-limits in a no-browsing session.
3. Theorem S's instance form of B for (α) (the Lag_k A formula with a possibly repeated label 1) is proved as an alternant
   identity. It has not been wired into the certifier, so v8 still carries the R1 form (tail + heads) at multi-block ties.
4. Code trust for v8: §5 reports the code identity, the negative control and the mutants.
