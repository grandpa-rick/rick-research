# Q52 — Parabolic vanishing in LS12 (3.6): PROVED (all Coxeter groups, all dominant λ)

PROVE 265, 2026-10-30 (file dated 10-31 per PROVE.md). Registry node `q488-Q52-parabolic-vanishing`.

## Problem

LS12 = Lenart–Shimozono, arXiv 1203.3237, §3.1 (read first-hand this session, /tmp/rem421/ls12.txt l.422–490).
For W a Coxeter group, J ⊆ S, τ ∈ W/W_J and w ∈ W with wW_J ≥ τ, Prop 3.1(2) [Deo]:
dn(w,τ) := Bruhat-max of {v ∈ W : v ≤ w, vW_J = τ}. For an LS path p of shape λ (λ dominant, W_λ = W_J)
with directions σ_1 ≥ … ≥ σ_k and ι(p)=σ_1 ≤ wW_λ: w_0' = w, w_i' = dn(w_{i-1}', σ_i), dn(w,p) := w_k'.
D^λ_{w,z} := {p : ι(p) ≤ wW_λ, dn(w,p) = z}  (3.2).

**Claim (Q52).** In type C_m, λ = ω_m, P the maximal parabolic: if z ∈ W^P and w ∉ W^P then D_{w,z} = ∅.
(Here z = z_κ = w_0 w_κ w_{0,P}; these are all of W^P.)

## Solution

Notation: D_R(x) = {s ∈ S : ℓ(xs) < ℓ(x)}. W^J = minimal-length representatives of W/W_J.

**Fact 0.** x ∈ W^J ⇔ D_R(x) ∩ J = ∅.
(⇒) if s ∈ J and xs < x, then xs ∈ xW_J is shorter. (⇐) if x ∉ W^J write x = x^J x_J with
ℓ(x) = ℓ(x^J) + ℓ(x_J), x_J ∈ W_J ∖ {e} [Björner–Brenti GTM 231, Prop 2.4.4]; x_J is a product of letters from J, so by the
deletion property it has a reduced word (in W) using only letters from J; let s ∈ J be its last letter, so
ℓ(x_J s) < ℓ(x_J). Then ℓ(xs) ≤ ℓ(x^J) + ℓ(x_J s) < ℓ(x).

**Lemma 1 (lifting, right version).** If v ≤ w, s ∈ D_R(w), s ∉ D_R(v), then vs ≤ w.
*Proof (subword property, BB Thm 2.2.2).* Fix a reduced word w = s_1⋯s_r s (possible since ws < w), so
s_1⋯s_r is a reduced word for ws. v ≤ w, so some reduced word for v is a subword of s_1⋯s_r s.
– If that subword uses the final s: v = v'' s with v'' a subword product of s_1⋯s_r, so vs = v'' ≤ ws < w.
– If not: v is a reduced subword of s_1⋯s_r; appending the final s gives a subword of s_1⋯s_r s of length
ℓ(v)+1 with product vs, and ℓ(vs) = ℓ(v)+1 since s ∉ D_R(v); so it is a reduced subword and vs ≤ w. ∎
(This is the right-handed form of the lifting property / Deodhar's Property Z, BB Prop 2.2.7.)

**Lemma 2 (down-lifts keep parabolic descents).** Let τ ≤ wW_J and v = dn(w,τ). Then D_R(w) ∩ J ⊆ D_R(v).
*Proof.* Let s ∈ D_R(w) ∩ J and suppose s ∉ D_R(v), i.e. vs > v. Then v ≠ w, and v ≤ w, so Lemma 1 gives
vs ≤ w. As s ∈ W_J, vsW_J = vW_J = τ. So vs lies in the set {u ≤ w : uW_J = τ}, whose Bruhat-maximum is v.
Hence vs ≤ v, contradicting vs > v. ∎

**Corollary 3.** For every LS path p with ι(p) ≤ wW_λ: D_R(w) ∩ J ⊆ D_R(dn(w,p)).
*Proof.* Induction along w = w_0' ≥ w_1' ≥ … ≥ w_k' (each step is Lemma 2 with τ = σ_i; LS12 guarantees
each step is defined, σ_i ≤ σ_{i-1} = w_{i-1}'W_J). ∎

**Theorem (Q52, general form).** For any symmetrizable Kac–Moody W, any dominant λ, J = {i : s_iλ = λ}:
if w ∉ W^J and z ∈ W^J then D^λ_{w,z} = ∅. Consequently, for z ∈ W^J,
[L^{-λ}][O_z] = Σ_{w ∈ W^J, w ≥ z} Σ_{p ∈ D_{w,z}} (−1)^{ℓ(w)−ℓ(z)} e^{−p(1)} [O_w]   (LS12 (3.6)).
*Proof.* w ∉ W^J ⇒ (Fact 0) some s ∈ D_R(w) ∩ J ⇒ (Cor 3) s ∈ D_R(dn(w,p)) ⇒ (Fact 0) dn(w,p) ∉ W^J,
for every p; so no p has dn(w,p) = z. ∎ Q52 is the case C_m, λ = ω_m, J = S∖{s_m}.

Nothing about ω_m, LS paths, or z_κ is used: only that dn is a Bruhat-MAX within a W_J-coset.

## Consequence for the long draft (Rem 4.22 `rem:LSbij`)

π: G/B → G/P, π^* ring map preserving L, injective (π_*π^* = id). Then
π^*[O_{X_κ} ⊗ L^{-1}]_T = [L^{-ω_m}][O_{z_κ}] = (3.6) = Σ_{ρ} (Σ_{p ∈ D_{z_ρ,z_κ}} (−1)^{|θ|} e^{−p(1)}) [O_{z_ρ}]
(Theorem: only w ∈ W^P = {z_ρ} survive) = Σ_ρ A_{κρ} [O_{z_ρ}] (Rem 4.22 bijection with V-maps, Q48)
= π^*(Σ_ρ A_{κρ} [O_{X_ρ}]_T), and injectivity of π^* gives Thm 4.20's formula.
No spanning statement and no basis statement is used. **(KT) leaves Rem 4.22 entirely**; it is now used
only in Thm 4.20's own proof (and its uniqueness clause).

## Verification

`proofs/prove265/q52.py` (imports the Wake 265 referee implementation `proofs/wake265/check.py`,
written from LS12's printed statement):

| m | LS paths ω_m | Lemma 2 tests (w,τ) | Lemma 2 failures | #(w∉W^P, p) with dn∈W^P | #(w∉W^P, p) with dn∉W^P |
|---|---|---|---|---|---|
| 2 | 5 | 20 | 0 | 0 | 12 |
| 3 | 14 | 210 | 0 | 0 | 280 |
| 4 | 42 | 3024 | 0 | 0 | 6624 |

So the vanishing holds set by set, not by signed cancellation (do-first #1). The last column is the
non-vacuity check: every off-W^P (w,p) does go somewhere off W^P.

Negative control `q52_ctrl_min.py`: replace Bruhat-max by Bruhat-min in dn. Lemma 2 fails 175/210 (m=3)
and 2898/3024 (m=4), and every off-W^P pair lands in W^P (280 and 6624). So the max is what carries the
proof, as Lemma 2 says.

## Gaps

None. External inputs: BB05 Thm 2.2.2 (subword property) and Prop 2.4.4 (parabolic factorization), both
standard textbook facts; LS12 §3.1 definitions read first-hand.

## Honest grade of the question

The question was **nearly empty**: a three-line lifting-property argument, true for any z ∈ W^J and any
dominant λ. The do-first #2 instinct ("maybe it's forced in one line") was right. Its value is in what
it removes: (KT) is no longer needed in Rem 4.22.
