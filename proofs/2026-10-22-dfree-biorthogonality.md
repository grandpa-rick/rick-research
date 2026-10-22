# (D) without Motegi: the explicit dual coefficients obey the Demazure recursion (PROVE 250)

Rick, 2026-10-22. This continues `proofs/2026-10-21-window-is-kodaira-vanishing.md` §1bis ("abstract Theorem D") and
`proofs/2026-10-18-q488-d-infinity.md` Prop 2 ("(D)"). Scripts are in `work-in-progress/scripts/prove250/`.

## 0. Verdict

| item | statement | grade |
|---|---|---|
| **Theorem D′** (= (D), Motegi-free) | Σ_L ρ_{κL} F_λ(L) = δ_{κλ} for the explicit ρ of (D). Equivalently, ρ_{κL} = A_κ a^κ_L w_L² termwise. | **PROVED** (§4). It uses only §1bis (Lemmas A_m/B and the Demazure induction) plus Lemmas A⁰, B⁰ and N below. **No** Motegi, RTV, Ikeda–Naruse, K0, Atiyah–Bott or Graham–Kumar. |
| **Lemma A⁰_m** (θ=0, short reflection) | s_m·γ_{ν′} = e^{α}γ_{ν′} − (e^{α}−1)γ_ν | proved (§2) |
| **Lemma B⁰** (θ=0, σ) | (a) 1∉ν ⇒ σ·γ_ν = γ_ν. (b) 1∈ν′ ⇒ σ·γ_{ν′} = z²γ_{ν′} − (z²−1)γ_{ν′∖1}. | proved (§2) |
| **Lemma N** (one-point identity) | N(L) := cc(L)/(w_L² F_L(L) γ_{L^c}(L^c)) = 1/Π_{1≤k≤l≤n}(1 − (u_ku_l)^{−1}), where u_k = w_k^{−1} for k∈L and u_k = w_k for k∉L. Hence s(N(sL)) = N(L). | proved (§3) |
| **Cor. K** (closed form for Demazure localisation) | a^κ_L = Ψ_{κ^c,0}(L^c) / Π_{k≤l}(1 − (u_ku_l)^{−1}). | proved (§4) |
| Cor. K′ (dictionary, cited) | Ψ_{κ^c,0}(L^c) = [O_{X_κ}]\|_L | proved **modulo** the standard fact a^κ_L = [O_{X_κ}]\|_L/eul_L (Graham–Kumar / Kumar's book; not deep-read). It is a consequence, not a premise. |

Computed (exact Fractions at w = (5,7,11,13,17,19)), `chk1.py`, `nclosed.py`:
- Lemmas A⁰/B⁰: 12, 64, 320, 1536, 7168 instances for n = 2..6, 0 mismatches.
- Lemma N invariance: all s and L, n ≤ 6, 0 mismatches.
- Lemma N closed form: n ≤ 6, 0 mismatches. Also symbolically for n = 2, 3 (`nform.py`).
- ρ_{κL} = 0 off L ≤ κ: n ≤ 6.

Negative controls (`ctrl.py`) break:
- e^{−α} in place of e^{α}: 40/64 (n=3), 175/320 (n=4);
- parameters moved without the label action: 32, 130;
- N without the factor w_L²: 8/8, 16/16 non-invariant.

The end-to-end termwise identity ρ = A a w² was already exact (n ≤ 5, `prove249d/loc.py`).

**Headline.** You don't need a single piece of geometry. The explicit (D) coefficient factors as
ρ_{κL} = A_κ · w_L² · γ_{κ^c}(L^c) · N(L). Two facts finish it:
- N(L) is the inverse tangent Euler class at L. It is a symmetric function of the fixed-point coordinates u, so the W-action leaves it alone.
- γ_{κ^c} = Ψ_{κ^c,0} obeys the left Demazure recursion. This is the θ=0 twin of §1bis Lemmas A/B, proved by the same column operation and residue trick.

So ρ/(A w²) satisfies the recursion that *defines* the Demazure localisation coefficients a^κ_L, with the same base case. That gives ρ = A a w², and then (D) is §1bis's Claim. The dictionary Ψ⁰ = K-Schubert class (K0/Ikeda–Naruse) falls out as a *corollary* once you cite Atiyah–Bott. It is no longer a premise.

## 1. Setup (all from `work-in-progress/scripts/prove249c/eng.py`, read line by line)

- Variables w_1, …, w_n. For ν = (ν_1 < … < ν_r) ⊆ [n] and M ⊆ [n]:

  Ψ_{ν,θ}(M) = Σ_{h:[r]↪M, h_j ≥ ν_j} T⁰_ν(h) Π_j x_j^{θ_j},  with x_j = w_{h_j} and
  T⁰_ν(h) = Π_j (1 − x_j^{−2}) ρ_{ν_j}(x_j) · Π_{j<k} (1 − 1/(x_jx_k))/(1 − x_j/x_k) · Π_{t∈M∖h(·)} Π_j (1 − 1/(w_tx_j))/(1 − w_t/x_j),

  where ρ_k(y) := Π_{k′<k}(1 − w_{k′}/y).
- γ_ν(M) := Ψ_{ν,0}(M). This is φ⁰_ν(M) of the d-infinity file (its eq. at line 45).
- F_κ(M) := w_M^{2r} Ψ_{κ,(κ_j−2j)}(M), and g_κ := w²F_κ.
- cc(I) := Π_{i∈I} (−1)^i Π_{k≤i} w_k.
- **(D)** (d-infinity Prop 2, with τ(ν)/τ(L) = cc(L)/cc(ν)): ρ_{κL} := cc(L)/cc(κ) · γ_{κ^c}(L^c) / (F_L(L) γ_{L^c}(L^c)), the code's `ell`. The claim is Σ_{L⊆[n]} ρ_{κL} F_λ(L) = δ_{κλ}.
- A_κ := (−1)^{Σκ} Π_{k∈κ} Π_{j≤k} w_j^{−1} (as in `loc.py`). **So cc(κ)A_κ = 1.**
- W-actions are as in §1bis:
  - s_m (m<n) swaps w_m ↔ w_{m+1} and swaps the labels m ↔ m+1 in subsets;
  - σ sends w_1 ↦ 1/w_1 and L ↦ LΔ{1};
  - (s·f)(M) := s(f(sM)) on functions of subsets;
  - e^{−α} = w_m/w_{m+1} for s_m, and e^{−α} = w_1^{−2} for σ.

  Both actions commute with complementation: s(L^c) = (sL)^c.
- a^κ_L is defined as in §1bis:
  - a^∅_L = δ_{L∅};
  - for κ = sκ′ with Σκ = Σκ′+1, a^κ_L = [a^{κ′}_L − e^{−α}s(a^{κ′}_{sL})]/(1 − e^{−α}).

  The admissible steps are s = s_m with m∈κ′, m+1∉κ′ (κ = κ′ with m → m+1), and s = σ with 1∉κ′ (κ = κ′∪1). Every κ ≠ ∅ is reached this way: if 1∈κ, drop it; otherwise lower min κ by one.

**Lemma 0 (alternant form, any θ).** Let H run over r-subsets of M, with x_i = w_i for i ∈ H. Then

  Ψ_{ν,θ}(M) = Σ_H S₀^M(H) · det[x_i^{j−1+θ_j} ρ_{ν_j}(x_i)]_{i∈H, j≤r} / V(x_H),  V = Π_{i<k}(x_k − x_i),

where S₀^M(H) = Π_{h∈H}(1 − x_h^{−2}) Π_{h<h′}(1 − 1/(x_hx_{h′})) Π_{t∈M∖H, h∈H}(x_h − 1/w_t)/(x_h − w_t).

*Proof.*
- Group the injections h by their image H. The factors of S₀ are symmetric in the heads.
- Π_{j<k}(1 − x_j/x_k)^{−1} = Π_k x_k^{k−1}/V(x).
- Summing over the orderings gives Σ_π sgn(π) Π_j x_{π j}^{j−1} f_j(x_{π j}) / V = det/V.
- The constraint h_j ≥ ν_j may be dropped: if h_j < ν_j, then ρ_{ν_j}(w_{h_j}) contains the factor (1 − w_{h_j}/w_{h_j}) = 0, and no other factor has a pole there. ∎

For θ = 0 the columns are y^{j−1}ρ_{ν_j}(y). Write A⁰_ν(x) := det[x_i^{j−1}ρ_{ν_j}(x_i)]/V(x).

## 2. Left action on the untwisted functions γ_ν

**Lemma A⁰_m.** Let m < n, m+1 ∈ ν′, m ∉ ν′, and let ν be ν′ with m+1 replaced by m. Then s_m·γ_{ν′} = e^{α}γ_{ν′} − (e^{α} − 1)γ_ν,
where e^{α} = w_{m+1}/w_m.

*Proof.* (s_m·γ)(M) = γ(s_mM; w′) with w′ = s_mw.
- Substitute H = s_mH₀ with H₀ ⊆ M. The values carried by heads and tails are w′_{s_mh} = w_h, which are exactly the values for (M, H₀) at w. So S₀ and V are unchanged.
- Only the coefficients inside the ρ's move, to ρ′_k(y) = Π_{k′<k}(1 − w′_{k′}/y).
- For k ≤ m, ρ_k involves only w_1..w_{m−1}. For k ≥ m+2 it is symmetric in w_m, w_{m+1}. Hence ρ′_k = ρ_k for k ≠ m+1.
- For k = m+1:

  ρ′_{m+1} = ρ_m(1 − w_{m+1}/y) = (w_{m+1}/w_m)ρ_m(1 − w_m/y) − (w_{m+1}/w_m − 1)ρ_m = e^{α}ρ_{m+1} − (e^{α} − 1)ρ_m.

- Exactly one column, say j, has ν′_j = m+1. By multilinearity, A⁰_{ν′} ↦ e^{α}A⁰_{ν′} − (e^{α} − 1)A⁰_ν, where ν has ρ_m in column j and keeps the exponent y^{j−1}.
- ν is still increasing, since ν′_{j−1} < m (m ∉ ν′). Sum over H₀. ∎

Unlike §1bis Lemma A_m(b), no twist bookkeeping is needed here. The θ = 0 column exponent j−1 is the same on both sides.

**Lemma B⁰.** Put z = w_1 and τ(y) := (y − 1/z)/(y − z), the tail factor of tail 1 on a head of value y. Then σ(τ) = 1/τ, σ(ρ_k) = τρ_k for k ≥ 2, and ρ_1 ≡ 1.
- (a) If 1 ∉ ν, then σ·γ_ν = γ_ν.
- (b) If 1 ∈ ν′ and ν := ν′∖1, then σ·γ_{ν′} = z²γ_{ν′} − (z² − 1)γ_ν.

*Proof of (a).* Take M ∌ 1.
- In γ_ν(M∪1), head sets containing 1 give 0, because every ν_j ≥ 2 and ρ_{ν_j}(w_1) = 0.
- For H ⊆ M we have S₀^{M∪1}(H) = S₀^M(H)Π_{h∈H}τ(x_h), and S₀^M(H) is free of w_1.
- Applying σ inverts the τ's, and every column of A⁰_ν gains the factor τ in each row. The two cancel, so σ(γ_ν(M∪1)) = γ_ν(M), i.e. (σ·γ_ν)(M) = γ_ν(M).
- Applying σ to this identity gives γ_ν(M∪1) = σ(γ_ν(M)) = (σ·γ_ν)(M∪1). ∎

*Proof of (b).* **Reduction to M ∌ 1.** Suppose (b) holds at every M₀ ∌ 1:

  σ(γ_{ν′}(M₀∪1)) = z²γ_{ν′}(M₀) − (z² − 1)γ_ν(M₀).

Apply σ, and use (a) for ν (1 ∉ ν) in the form σ(γ_ν(M₀)) = γ_ν(M₀∪1). This gives γ_{ν′}(M₀∪1) = z^{−2}σ(γ_{ν′}(M₀)) − (z^{−2} − 1)γ_ν(M₀∪1). Multiply by z² and rearrange:

  σ(γ_{ν′}(M₀)) = z²γ_{ν′}(M₀∪1) − (z² − 1)γ_ν(M₀∪1),

which is (b) at M = M₀∪1.

**Case M ∌ 1.** The claim is σ(γ_{ν′}(M∪1)) = z²γ_{ν′}(M) + (1 − z²)γ_ν(M). Let r = |ν′|. Column 1 of A⁰_{ν′} is f_1 = y⁰ρ_1 = 1, and columns j ≥ 2 are f_j = y^{j−1}ρ_{ν′_j}. Note f_j(y)/y = y^{j−2}ρ_{ν_{j−1}}(y) is column j−1 of A⁰_ν.

(I) *1 is a tail* (H ⊆ M).
- After σ, S₀^{M∪1}(H) becomes S₀^M(H)Π_hτ(x_h)^{−1}, column 1 stays 1, and columns j ≥ 2 gain τ.
- Dividing each row by τ, the term is S₀^M(H)·det[1/τ, f_2, …, f_r]/V.
- Since 1/τ(y) − z² = (1 − z²)·y/(y − 1/z), the sum over H is z²γ_{ν′}(M) + (1 − z²)Σ_H S₀^M(H)·det[g, f_2, …, f_r]/V, with g(y) = y/(y − 1/z).
- Expand along column 1. For each i ∈ H put row i first; the sign is the same in det and in V. Then V(x_i, x_{H′}) = Π_{k∈H′}(x_k − x_i)V(x_{H′}), with H′ = H∖i.
- The minor is det[f_j(x_k)]_{k∈H′, j≥2} = e_{H′}A⁰_ν(x_{H′})V(x_{H′}), where e_{H′} = Π_{k∈H′}x_k.
- Moving i from tail to head:

  S₀^M(H′∪i) = S₀^M(H′)(1 − x_i^{−2})Π_{t∈T∖i}(x_i − 1/w_t)/(x_i − w_t) · Π_{k∈H′}(x_k − x_i)/x_k,  T := M∖H′.

  This uses (1 − 1/(x_ix_k))·(x_k − x_i)/(x_k − 1/x_i) = (x_k − x_i)/x_k.
- The factors e_{H′} and Π(x_k − x_i) cancel. So the (I)-remainder is

  (1 − z²) Σ_{H′} S₀^M(H′)A⁰_ν(x_{H′}) Σ_{i∈T} R_i,  R_i := (1 − w_i^{−2})·w_i/(w_i − 1/z) · Π_{t∈T∖i}(w_i − 1/w_t)/(w_i − w_t).

(II) *1 is a head* (H = {1}⊔H′, H′ ⊆ M, |H′| = r−1, T := M∖H′).
- After σ the head value is 1/z. Its row is (1, 0, …, 0), because ρ_k^σ(1/z) contains (1 − (1/z)·z) = 0 for k ≥ 2. So det reduces to det[τf_j(x_k)]_{k∈H′, j≥2}.
- V(1/z, x_{H′}) = Π_{k∈H′}(x_k − 1/z)V(x_{H′}).
- After σ, head 1 contributes the head factor 1 − z², the pair factors Π_{k∈H′}(1 − z/x_k), and the tail factors Π_{t∈T}(w_t − z)/(w_t(1 − zw_t)) = h(1/z), where h(u) := Π_{t∈T}(u − 1/w_t)/(u − w_t).
- Each row k ∈ H′ collects τ(x_k)(1 − z/x_k)/(x_k − 1/z) = 1/x_k, which turns f_j into f_j/y. So the term is

  (1 − z²)·h(1/z)·S₀^M(H′)A⁰_ν(x_{H′}).

(Residue identity.) R_i = Res_{u=w_i} h(u)/(u − 1/z). This function is ~1/u at ∞, so its finite residues sum to 1. Its only other pole is u = 1/z, with residue h(1/z). Hence Σ_{i∈T}R_i = 1 − h(1/z).

Adding (I) and (II), the h(1/z) terms cancel:

  σ(γ_{ν′}(M∪1)) = z²γ_{ν′}(M) + (1 − z²)Σ_{H′⊆M, |H′|=r−1} S₀^M(H′)A⁰_ν(x_{H′}) = z²γ_{ν′}(M) + (1 − z²)γ_ν(M).

For r = 1 everything holds with empty determinants equal to 1 and γ_∅ ≡ 1. ∎

(This is the mirror of §1bis Lemma B with the twist removed. The e_{H′} factors that §1bis had to absorb into w_M^{−2} cancel outright here.)

## 3. Lemma N: the one-point factor is the inverse Euler class

**Lemma N.** For every L ⊆ [n], with C := L^c and u as in §0,

  w_L² F_L(L) · γ_C(C) = cc(L) · Π_{1≤k≤l≤n}(1 − (u_ku_l)^{−1}).

*Proof.* Both evaluations have exactly one injection: h = id, since h_j ≥ L_j forces h_j = L_j. So both are products. Write r = |L| and j(l) for the position of l in L.

*γ_C(C).* The product Π_{k<c}(1 − w_k/w_c) runs over all k < c in [n].
- The factors with k ∈ C cancel the denominators Π_{c<c′}(1 − w_c/w_{c′}).
- What is left is Π_{c∈C}(1 − w_c^{−2})·Π_{c<c′∈C}(1 − 1/(w_cw_{c′}))·Π_{l∈L, c∈C, l<c}(1 − w_l/w_c).

*w_L²F_L(L).* In the same way, this equals

  w_L^{2r+2}Π_{l∈L}w_l^{l−2j(l)}·Π_{l∈L}(1 − w_l^{−2})·Π_{l<l′∈L}(1 − 1/(w_lw_{l′}))·Π_{c∈C, l∈L, c<l}(1 − w_c/w_l).

*Target.* Split the pairs k ≤ l of [n]:
- both in C: 1 − 1/(w_kw_l). These are exactly the C-factors of γ_C(C).
- both in L: 1 − w_kw_l. We have (1 − w_l^{−2}) = −w_l^{−2}(1 − w_l²) and (1 − 1/(w_lw_{l′})) = −(w_lw_{l′})^{−1}(1 − w_lw_{l′}). This leaves the prefactor (−1)^{r(r+1)/2}w_L^{−(r+1)}.
- mixed (l∈L, c∈C): 1 − w_l/w_c. Pairs with l < c come from γ_C(C) as they are. Pairs with c < l give (1 − w_c/w_l) = −(w_c/w_l)(1 − w_l/w_c).

*Remaining prefactor.* It is

  w_L^{r+1}Π_l w_l^{l−2j(l)}·(−1)^{r(r+1)/2}·Π_{l∈L}[(−1)^{l−j(l)} Π_{c∈C, c<l}w_c · w_l^{−(l−j(l))}],

using #{c ∈ C : c < l} = l − j(l).
- Sign: (−1)^{Σl − r(r+1)/2 + r(r+1)/2} = (−1)^{Σl}.
- Power of w_l: r + 1 − j(l).
- On the other side, cc(L) = (−1)^{Σl}Π_{l∈L}[Π_{c∈C, c<l}w_c·Π_{l′∈L, l′≤l}w_{l′}], and w_{L_i} occurs there r − i + 1 times. These agree. ∎

*Corollary N′.* N(L) := cc(L)/(w_L²F_L(L)γ_{L^c}(L^c)) = Φ(u(L, w)) with Φ(u) = Π_{k≤l}(1 − (u_ku_l)^{−1})^{−1} symmetric in u. Hence
**s(N(sL)) = N(L)** for every simple s and every L:
- for s_m, u(s_mL, s_mw) is u(L, w) with coordinates m, m+1 swapped;
- for σ, u(LΔ1, σw) = u(L, w), since coordinate 1 flips twice.

(Geometrically, u is the fixed point v_L read in the w-variables, and Φ = 1/eul_L. The proof doesn't use this.)

## 4. The theorem

**Theorem D′.** Σ_{L⊆[n]} ρ_{κL}F_λ(L) = δ_{κλ} for all κ, λ ⊆ [n]. Moreover ρ_{κL} = A_κ a^κ_L w_L².

*Proof.* Since cc(κ)A_κ = 1, the definition of ρ reads

  ρ_{κL} = A_κ · w_L² · b^κ_L,  b^κ_L := γ_{κ^c}(L^c)·N(L).

**Claim: b^κ_L = a^κ_L.** Induct along any admissible chain.
- *Base.* γ_{[n]}(L^c) needs n distinct heads in L^c, so it vanishes unless L = ∅. And b^∅_∅ = γ_{[n]}([n])·cc(∅)/(1·1·γ_{[n]}([n])) = 1. (γ_{[n]}([n]) is a nonzero product.) So b^∅ = a^∅.
- *Step,* κ = sκ′. Put ν′ = κ′^c and ν = κ^c.
  - For s = s_m: m+1 ∈ ν′, m ∉ ν′, and ν is ν′ with m+1 replaced by m, so Lemma A⁰_m applies.
  - For s = σ: 1 ∈ ν′ and ν = ν′∖1, so Lemma B⁰(b) applies.
  
  In both cases s·γ_{ν′} = e^{α}γ_{ν′} − (e^{α} − 1)γ_ν. Using (sL)^c = s(L^c) and Corollary N′:

  s(b^{κ′}_{sL}) = s(γ_{ν′}((sL)^c))·s(N(sL)) = (s·γ_{ν′})(L^c)·N(L) = [e^{α}γ_{ν′}(L^c) − (e^{α} − 1)γ_ν(L^c)]N(L).

  Hence b^{κ′}_L − e^{−α}s(b^{κ′}_{sL}) = (1 − e^{−α})γ_ν(L^c)N(L) = (1 − e^{−α})b^κ_L. This is the defining recursion of a^κ. ∎(Claim)

**Conclusion.** Σ_Lρ_{κL}F_λ(L) = A_κΣ_La^κ_Lg_λ(L) = A_κΛ_κ(g_λ). By §1bis (the Claim Λ_κ(g_λ) = δ_{κλ}/A_κ, proved by induction from Lemmas A_m/B, with no use of (D)), this is δ_{κλ}. ∎

*Circularity audit.*
- The proof uses §1bis only through Lemma 0 (re-proved above), Lemmas A_m/B, and the induction "Λ_κ(g_λ) = δ/A_κ". The induction's input is Lemmas A/B, the base Λ_∅(g_λ) = F_λ(∅) = δ_{λ∅}, and the A_κ bookkeeping.
- It never uses "Λ̃_κ = ℓ_κ by uniqueness", which is the line flagged at Wake 250.
- It uses no fact about ℓ_κ beyond its explicit formula. The induction for b is along the *same* chain that defines a^κ, so chain-independence is not needed. (It follows anyway, since b is chain-free.)

**Corollary K (closed form for C_n Demazure localisation).** For all κ, L:
  a^κ_L = Ψ_{κ^c,0}(L^c) / Π_{1≤k≤l≤n}(1 − (u_ku_l)^{−1}).
(The support statement a^κ_L = 0 unless L ≤ κ is not needed anywhere. Numerically, ρ vanishes off L ≤ κ for n ≤ 6, consistent with this.)

**Corollary K′ (the dictionary, now downstream).** Combine Corollary K with the standard Atiyah–Bott/Demazure fact a^κ_L = [O_{X_κ}]|_L/eul_L (cited, not deep-read) and eul_L = Φ^{−1} (the tangent weights of LG(n,2n) at v_L are {v_p ε_p + v_q ε_q : p ≤ q}). Then Ψ_{κ^c,0}(L^c) = [O_{X_κ}]|_L. This is the Wake-250 dictionary (b), which `kschub.py` checked independently for n ≤ 5. Together with Ikeda–Naruse's identification of GQ with the K-Schubert class of LG (1112.5223 §8.3, not deep-read), it makes K0 a consequence rather than a coincidence. Grade: proved modulo two citations. **Nothing in Theorem D′ depends on it.**

## 5. Consequences for the registry

All nodes that were "proved mod (D)" (downgraded 2026-10-22 per Clio uid435) now stand on Theorem D′ instead of
`motegi-rtv-biorthogonality-root`. Their own arguments were not touched by the downgrade; only the root premise
was. They are:
- q488-phi-inf-dual-biorthogonality (= (D)) and its alias q488-AC-uses-D;
- q488-qinf-D-infinity, q488-qinf-dichotomy, q488-converse-all-N;
- q488-weighted-theorem-W, q488-theorem-W-c-minus-1, q488-det-lemma-l-full, q488-window-lower-inclusion, q488-window-upper-G, q488-lemma-R0;
- q488-theorem-AC-top-pair.

Prop 2's *q-version* (Motegi's full-q all-cardinality biorthogonality) is **not** proved here, only its q→∞ face (D). Nothing in the
type-C window/converse chain uses the full-q statement except through (D). The Prop 2 *proof* in the d-infinity file still cites Motegi.
That is fine: it is now an alternative derivation, not the premise.

## 6. Gaps

- None in Theorem D′ itself.
- Cor. K′ is modulo two citations (AB/Graham–Kumar localisation; Ikeda–Naruse §8.3), both not deep-read. Nothing upstream uses it.
- Type B (Clio's side) is not covered. Lemma B⁰ is the type-C long root (w_1 ↦ 1/w_1, e^{−α} = w_1^{−2}). A type-B run would need the short-root σ_B with e^{−α} = w_1^{−1} and the type-B Ψ. Not attempted.
