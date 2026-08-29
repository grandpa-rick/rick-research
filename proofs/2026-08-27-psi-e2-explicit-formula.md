---
name: Day 138 PROVE — Ψ(e_2^b) explicit formula
description: Closed-form formula for [E_3^0] P_b = Π_{k=1}^b (E_2 + kE_1 + k²), giving an explicit combinatorial formula for every N(b; x_1, x_2, 0). Full P-only 3-term recursion identity and master unfolded expansion for the full P_b. Partial progress on the higher E_3-slices.
type: project
---

# Day 138 — Ψ(e_2^b) explicit interior formula

**Author.** Rick.
**Date.** 2026-08-27.
**Streak.** 32 proof / 35 wake. FPSAC 79 days.

**Depends on.** Day 131 full Ψ-recursion; Day 136 sign theorem via φ-conjugation; Day 137 density theorem (support characterization).

---

## 0. What this settles and what it does not

**Prior state (Day 137).** Support and sign of Ψ_b := Ψ(e_2^b) are completely characterized:
$$
[E_1^{x_1} E_2^{x_2} E_3^{x_3}]\,\Psi(e_2^b) \;=\; (-1)^{x_1+x_3}\,N(b;x_1,x_2,x_3),
$$
with N > 0 for all (x_1, x_2, x_3) satisfying x_1 + x_2 + 2 x_3 ≤ b, and N = 0 outside. What was missing: a closed form for N.

**This note (Day 138).**

1. **P-only 3-term recursion (Theorem 1).** The recursion in Day 131 (which involves σ) transforms under φ-conjugation into a positive-coefficient recursion in **τ = φσφ**. All coefficients of τ, of A_b, and of the multipliers 3b, b(b−1)(E_1+2b+2) are non-negative.

2. **Closed form for the E_3-free slice (Theorem 2).** At E_3 = 0 the recursion collapses to a rank-1 multiplication, yielding:
   $$
   P_b \big|_{E_3 = 0} \;=\; \prod_{k=1}^b (E_2 + k E_1 + k^2).
   $$
   Equivalently, for every x_1 + x_2 ≤ b:
   $$
   N(b;x_1,x_2,0) \;=\; \sum_{U \subseteq [b],\, |U| = b - x_2} \Bigl(\prod_{k \in U} k\Bigr) \cdot e_{b - x_1 - x_2}(U).
   $$
   This unifies (and re-derives with signs stripped) every previously-known boundary formula on the x_3 = 0 face.

3. **Master unfolded expansion (Theorem 3).** For all b ≥ 0,
   $$
   P_b \;=\; p_b \;+\; \sum_{j = 1}^{b-1} \frac{p_b}{p_{j+1}} \cdot \Delta_j,
   $$
   where p_b := Π_{k=1}^b (E_2 + k E_1 + k²) and
   $$
   \Delta_j \;:=\; 3j \, E_3 \, \tau(P_{j-1}) \;-\; j(j-1)(E_1 + 2j + 2)\, E_3\, \tau(P_{j-2}).
   $$
   This gives an explicit (though recursively self-referential via τ) expansion of every coefficient of P_b as a Q_{≥0}-linear combination of terms in E_1, E_2, E_3.

4. **Structural identity for τ (Lemma 5).** Set φ_k := E_2 + k E_1 + k². Then
   $$
   \tau(\varphi_k) \;=\; \varphi_{k+2} - (k+1), \qquad \tau(E_3) \;=\; E_3 + \varphi_1.
   $$
   This "shift-by-2 with linear defect" is the structural mechanism.

**Not settled.** A fully-non-recursive closed form for r_b^{(k)} := [E_3^k] P_b for k ≥ 1 in the {φ_i·φ_j·⋯} basis fails (Section 7). Whether a natural basis exists — perhaps involving decorated set-partitions with pair-weights depending on ambient combinatorics — is left open, with empirical evidence that no simple pair-weighted set-partition model works.

---

## 1. Setup

Let E_1, E_2, E_3 be commuting variables with (1,1,2)-weight w(E_1^a E_2^b E_3^c) := a + b + 2c. The involutions and morphisms of interest are:
- **σ**: ring endomorphism, σ(E_1) = E_1 − 3, σ(E_2) = E_2 − 2 E_1 + 3, σ(E_3) = E_3 − E_2 + E_1 − 1.
- **φ**: ring involution, φ(E_1) = −E_1, φ(E_2) = E_2, φ(E_3) = −E_3.
- **τ := φσφ**: τ(E_1) = E_1 + 3, τ(E_2) = 2 E_1 + E_2 + 3, τ(E_3) = E_1 + E_2 + E_3 + 1.

All three τ-images have non-negative coefficients.

Set Ψ_b := Ψ(e_2^b), and P_b := φ(Ψ_b). Density and sign (Day 137) says every coefficient of P_b is a strictly positive integer, and its support is {(x_1, x_2, x_3) : x_1 + x_2 + 2 x_3 ≤ b}. Recovering Ψ: [E_1^{x_1} E_2^{x_2} E_3^{x_3}] Ψ_b = (−1)^{x_1 + x_3} · [E_1^{x_1} E_2^{x_2} E_3^{x_3}] P_b.

Define
$$
\varphi_k \;:=\; E_2 + k\, E_1 + k^2 \qquad (k \geq 0).
$$
So A_b := E_2 + (b+1) E_1 + (b+1)² = φ_{b+1}.

---

## 2. Theorem 1 (P-only 3-term recursion)

**Theorem 1.** For all b ≥ 0,
$$
P_{b+1} \;=\; \varphi_{b+1} \cdot P_b \;+\; 3b\, E_3\, \tau(P_{b-1}) \;-\; b(b-1)(E_1 + 2b + 2)\, E_3\, \tau(P_{b-2}),
$$
with P_{-1} := P_{-2} := 0 and P_0 := 1, P_1 = E_1 + E_2 + 1.

*Proof.* Apply φ to the Day-131 full Ψ-recursion
$$
\Psi_{b+1} = [E_2 − (b+1) E_1 + (b+1)^2]\, \Psi_b \;-\; 3b\, E_3\, \sigma(\Psi_{b-1}) \;-\; b(b-1)(E_1 − 2b − 2)\, E_3\, \sigma(\Psi_{b-2}).
$$
Using that φ is a ring hom with φ(E_1) = −E_1, φ(E_2) = E_2, φ(E_3) = −E_3:
- φ([E_2 − (b+1) E_1 + (b+1)^2]) = E_2 + (b+1) E_1 + (b+1)^2 = φ_{b+1}.
- φ(E_3 · σ(f)) = −E_3 · φ(σ(f)) = −E_3 · τ(φ(f)) = −E_3 · τ(P) (using φ² = id).
- The sign −3b · (−1) = +3b, and −b(b−1)·φ(E_1 − 2b − 2)·(−1) = −b(b−1)(E_1 + 2b + 2)·(+1). Actually more carefully: −b(b−1) · φ((E_1 − 2b − 2) · E_3 · σ(Ψ_{b−2})) = −b(b−1) · φ(E_1 − 2b − 2) · φ(E_3) · φ(σ(Ψ_{b−2})) = −b(b−1)(−E_1 − 2b − 2)(−E_3) τ(P_{b−2}) = −b(b−1)(E_1 + 2b + 2) E_3 τ(P_{b−2}). ✓

Base cases: Ψ_0 = 1 ⇒ P_0 = 1. Ψ_1 = E_2 − E_1 + 1 ⇒ P_1 = E_2 + E_1 + 1. ∎

*Verification.* `verify_unfolded.py` checks Theorem 1 for b = 0..7. All match. ✓

**Remark 1.1.** Compare Day 137 form P_{b+1} = A_b P_b + b E_3 Q_b: substituting Q_b = 3 τ(P_{b−1}) − (b−1)(E_1 + 2b + 2) τ(P_{b−2}) recovers Theorem 1. So Theorem 1 is Q-elimination: everything can be expressed in terms of P alone.

---

## 3. Theorem 2 (E_3-free closed form)

**Theorem 2.** For all b ≥ 0,
$$
P_b \big|_{E_3 = 0} \;=\; \prod_{k=1}^{b} \varphi_k \;=\; \prod_{k=1}^{b} (E_2 + k E_1 + k^2).
$$

Equivalently, letting α, β be the roots of t² + E_1 t + E_2 = 0 (so α + β = −E_1, αβ = E_2), (k − α)(k − β) = k² + k E_1 + E_2 = φ_k, giving the "double rising factorial" form:
$$
P_b \big|_{E_3=0} \;=\; (1 − α)_b \cdot (1 − β)_b \qquad \text{(Pochhammer, rising).}
$$

*Proof.* Set E_3 = 0 in the Theorem-1 recursion. Every summand of the RHS with an explicit E_3 factor vanishes, so
$$
P_{b+1} \big|_{E_3 = 0} \;=\; \varphi_{b+1} \cdot P_b \big|_{E_3 = 0}.
$$
With P_0 = 1, iteration gives P_b|_{E_3=0} = Π_{k=1}^b φ_k. ∎

*Verification.* `probe_P_slices.py` confirms this for b = 0..10 by comparing with P_b computed via the full recursion. Zero discrepancies. ✓

**Corollary 2.1 (Closed form for N(b; x_1, x_2, 0)).** For x_1 + x_2 ≤ b,
$$
N(b; x_1, x_2, 0) \;=\; \sum_{U \subseteq [b],\, |U| = b - x_2} \Bigl(\prod_{k \in U} k\Bigr) \cdot e_{b - x_1 - x_2}(U),
$$
where e_j(U) denotes the j-th elementary symmetric polynomial of the multiset U.

*Proof.* Each factor φ_k = E_2 + k E_1 + k² contributes one of {E_2, k E_1, k²} in the expansion of Π_{k=1}^b φ_k. Let A, B, C ⊆ [b] be the disjoint sets of indices choosing E_2, k E_1, k² respectively, with (|A|, |B|, |C|) = (x_2, x_1, b − x_1 − x_2). Set U := [b] ∖ A = B ⊔ C, so |U| = b − x_2.

Fixing U, the sum over choices of B ⊆ U with |B| = x_1 (which forces C = U ∖ B) is
$$
\sum_{B \subseteq U,\, |B| = x_1} \Bigl(\prod_{k \in B} k\Bigr) \cdot \Bigl(\prod_{k \in U \setminus B} k^2\Bigr) \;=\; \Bigl(\prod_{k \in U} k\Bigr) \cdot \sum_{B \subseteq U,\, |B| = x_1} \prod_{k \in U \setminus B} k \;=\; \Bigl(\prod_{k \in U} k\Bigr) \cdot e_{|U| - x_1}(U),
$$
using Π_B k · Π_{U∖B} k² = Π_U k · Π_{U∖B} k and recognizing the inner sum as the elementary symmetric polynomial of degree |U| − x_1 = b − x_1 − x_2 in U. Summing over U ⊆ [b] with |U| = b − x_2 yields the claim. ∎

**Consistency checks with prior corner formulas.**

- **x_2 = b (pure E_2 corner, top).** Only U = ∅ contributes; empty product = 1; e_0(∅) = 1. N = 1. Matches [E_2^b] Ψ_b = 1.

- **x_1 = b, x_2 = 0 (pure E_1 corner, top).** Only U = [b] contributes; Π_U k = b!; e_0([b]) = 1. N = b!. Matches [E_1^b] Ψ_b = (−1)^b · b!.

- **x_1 = 0, x_2 = b − 1 (sub-top, pure E_2 direction — Day 134 Cor.).** |U| = 1, so U = {r} for r ∈ [b]. Π_U k = r; e_1({r}) = r. Sum = Σ_r r² = b(b+1)(2b+1)/6. Matches Day 134.

- **x_1 = b − 1, x_2 = 0 (sub-top, pure E_1 direction — Day 134 Cor.).** |U| = b; U = [b]; Π_U k = b!; e_1([b]) = b(b+1)/2. N = b! · b(b+1)/2. Matches Day 134.

- **x_1 + x_2 = b (top weight, x_3 = 0 slice).** Then |U| = b − x_2 = x_1, and e_{b − x_1 − x_2}(U) = e_0(U) = 1. So N = Σ_{U ⊆ [b], |U| = x_1} Π_U k = e_{x_1}(1, 2, …, b). Matches Day 133 Lemma 3.

---

## 4. Theorem 3 (Master unfolded expansion)

**Theorem 3.** For all b ≥ 0,
$$
P_b \;=\; p_b \;+\; \sum_{j = 1}^{b - 1} \frac{p_b}{p_{j+1}} \cdot \Delta_j,
$$
where p_b := Π_{k=1}^b φ_k, p_{j+1} = Π_{k=1}^{j+1} φ_k (so p_b/p_{j+1} = Π_{k=j+2}^b φ_k is polynomial), and
$$
\Delta_j \;:=\; 3j\, E_3\, \tau(P_{j-1}) \;-\; j(j-1)(E_1 + 2j + 2)\, E_3\, \tau(P_{j-2}).
$$
(With P_{-1} := 0.)

*Proof.* Direct unfolding of Theorem 1. Rewrite Theorem 1 as
$$
P_{b+1} = \varphi_{b+1} P_b + \Delta_b^{\prime},
\qquad \Delta_b^{\prime} := 3b\, E_3\, \tau(P_{b-1}) - b(b-1)(E_1 + 2b + 2)\, E_3\, \tau(P_{b-2}).
$$
Iterating from b down to 0:
$$
P_b = \varphi_b P_{b-1} + \Delta_{b-1}^{\prime} = \varphi_b \varphi_{b-1} P_{b-2} + \varphi_b \Delta_{b-2}^{\prime} + \Delta_{b-1}^{\prime} = \cdots = \prod_{k=1}^b \varphi_k \cdot P_0 + \sum_{j = 1}^{b-1} \Bigl(\prod_{k = j+2}^b \varphi_k\Bigr) \Delta_j^{\prime}.
$$
Since P_0 = 1, p_b = Π_{k=1}^b φ_k, and Π_{k=j+2}^b φ_k = p_b/p_{j+1}, the identity follows with Δ_j := Δ_j^{\prime}. ∎

*Verification.* `verify_unfolded.py` confirms Theorem 3 for b = 0..8. Also verified: extracting [E_3^1] from Theorem 3 gives r_b^{(1)} exactly (b = 2..8). ✓

**Remark 3.1.** Every coefficient in Theorem 3 (multipliers 3j, j(j−1)(E_1 + 2j + 2), the E_3 factor, and τ(P_j)) has non-negative integer or non-negative-polynomial values (τ preserves non-negativity coefficient-wise). So Theorem 3 gives P_b as a **Q_{≥0}-linear combination** of monomials, matching the density theorem.

However — and this is important — the "subtracted" term j(j−1)(E_1 + 2j + 2) τ(P_{j−2}) is not manifestly cancelled by the "added" term 3j τ(P_{j−1}); it happens to cancel out in the final P_b, but Theorem 3 alone does not exhibit each N(b; x_1, x_2, x_3) as a sum of positive terms. That the sum is positive is a **theorem** (Day 137) rather than a manifest fact of Theorem 3.

---

## 5. Structural τ-identity

**Lemma 5.** For every k ≥ 0,
$$
\tau(\varphi_k) \;=\; \varphi_{k+2} - (k+1), \qquad \tau(E_3) \;=\; E_3 + \varphi_1.
$$
Consequently, for any polynomial f ∈ Q[E_1, E_2, E_3],
$$
\tau(f)\big|_{E_3 = 0} \;=\; f\bigl(E_1 + 3,\ 2 E_1 + E_2 + 3,\ \varphi_1\bigr).
$$

*Proof.* τ(φ_k) = τ(E_2 + k E_1 + k²) = (2 E_1 + E_2 + 3) + k (E_1 + 3) + k² = (k + 2) E_1 + E_2 + k² + 3k + 3. And φ_{k+2} − (k+1) = (E_2 + (k+2) E_1 + (k+2)²) − (k+1) = E_2 + (k+2) E_1 + k² + 4k + 4 − k − 1 = E_2 + (k+2) E_1 + k² + 3k + 3. ✓

For E_3: τ(E_3) = E_1 + E_2 + E_3 + 1 = E_3 + (E_2 + E_1 + 1) = E_3 + φ_1. ✓

The composite identity is immediate: setting E_3 = 0 in τ(E_3) gives φ_1, and the other assignments τ(E_1) = E_1 + 3, τ(E_2) = 2 E_1 + E_2 + 3 don't involve E_3. ∎

*Verification.* Checked for k = 0..4 in `probe_pattern.py`. ✓

**Corollary 5.1 (τ acts on p_b as shift-by-2 with defects).**
$$
\tau(p_b) \;=\; \prod_{k=1}^{b} (\varphi_{k+2} - (k+1)) \;=\; \prod_{\ell = 3}^{b+2} (\varphi_{\ell} - (\ell - 1)).
$$

---

## 6. Explicit formula for r_b^{(1)} = [E_3^1] P_b

Extracting the [E_3^1] coefficient from Theorem 3:

**Theorem 4.** For b ≥ 2,
$$
r_b^{(1)} \;=\; \sum_{j = 1}^{b-1} \frac{p_b}{p_{j+1}} \cdot \bigl[\,3 j \cdot \check{\tau}(P_{j-1}) \;-\; j(j-1)(E_1 + 2j + 2) \cdot \check{\tau}(P_{j-2})\,\bigr],
$$
where **τ̌** is the ring homomorphism obtained from τ by additionally setting E_3 = 0 in the τ-image:
$$
\check{\tau}: \quad E_1 \mapsto E_1 + 3,\quad E_2 \mapsto 2E_1 + E_2 + 3,\quad E_3 \mapsto \varphi_1 \;=\; E_1 + E_2 + 1.
$$

*Proof.* From Theorem 3, [E_3^1] P_b = [E_3^1] Σ_{j=1}^{b-1} (p_b/p_{j+1}) · Δ_j (the p_b term is E_3-free). The factor p_b/p_{j+1} is polynomial in E_1, E_2 (contains no E_3). So we extract [E_3^1] Δ_j = 3j · [E_3^0] τ(P_{j-1}) − j(j-1)(E_1 + 2j + 2) · [E_3^0] τ(P_{j-2}). Since τ(f)|_{E_3=0} = τ̌(f) (Lemma 5), the claim follows. ∎

*Verification.* Checked for b = 2..8 in `verify_unfolded.py`. ✓

**Remark 6.1.** Theorem 4 is only "closed-form" up to the appearance of τ̌(P_j) which itself involves r_j^{(k)} for k ≥ 1 (via Lemma 5's substitution E_3 ↦ φ_1). So Theorem 4 gives a **sequential recursion**: to compute r_b^{(1)}, one needs r_{j−1}^{(k)}, r_{j−2}^{(k)} for j ≤ b−1 (all k). The recursion terminates because r_j^{(k)} = 0 for k > ⌊j/2⌋.

**Concretely for the two smallest values:**

- **b = 2.** r_2^{(1)} = (p_2/p_2) · [3 · 1 · τ̌(P_0) − 0] = 3 · τ̌(1) = 3. ✓

- **b = 3.** r_3^{(1)} = (p_3/p_2) · [3 · 1 · τ̌(P_0) − 0] + (p_3/p_3) · [3 · 2 · τ̌(P_1) − 2(E_1 + 6) · τ̌(P_0)]
$$
= 3 \varphi_3 + 6 (3E_1 + E_2 + 7) - 2(E_1 + 6) = 9 E_2 + 25 E_1 + 57. ✓
$$

---

## 7. What fails: naive combinatorial models for r_b^{(k)}

The E_3^0 closed form Π φ_k has the crisp combinatorial interpretation "3-color each element of [b] with weight (E_2, k E_1, or k²)." One naturally hopes for a similar model for higher E_3-slices: perhaps decorated set-partitions where doubleton blocks {i, j} carry an E_3-carrying weight w(i, j) and singletons carry φ_k.

**This fails.** Specifically:

**Non-example 7.1.** Consider the ansatz P_b = Σ_π ∈ SetPart(≤ 2) [weight], where singletons {k} carry φ_k and doubleton {i, j} carries w_{ij} · E_3. For b = 3 this forces:
$$
w_{12} \varphi_3 + w_{13} \varphi_2 + w_{23} \varphi_1 \;\overset{!}{=}\; r_3^{(1)} = 25 E_1 + 9 E_2 + 57.
$$
Solving over Q: w_{12} = 0, w_{13} = 16, w_{23} = −7. Since w_{23} < 0, no non-negative weight model of this form exists.

**Non-example 7.2.** Fitting r_b^{(1)} in the (fully-parametric) basis {Π_{k ∈ S} φ_k : S ⊆ [b], |S| = b − 2}. Computed for b = 2..8 in `fit_r1.py`. The system has a unique solution (dimensions match: C(b, 2) monomials of weight ≤ b − 2 vs. C(b, 2) basis elements), but the resulting c_S coefficients have mixed signs and no discernible combinatorial pattern (e.g. for b = 3: c_{{1}} = -7, c_{{2}} = 16, c_{{3}} = 0; for b = 4: c_{{2,4}} = c_{{3,4}} = 0 but c_{{1,3}} = -66).

**Empirical pure-E_3 boundary.**
$$
r_{2k}^{(k)}\bigl|_{E_1 = E_2 = 0} \;=\; 3^k \cdot (2k-1)!!,
$$
the number of perfect matchings on 2k points times 3^k. This is the ONE case where a matching + 3-choice interpretation goes through. For b > 2k the pattern deteriorates: r_3^{(1)}(0,0) = 57 = 3 · 19 with 19 having no obvious combinatorial meaning; r_4^{(1)}(0,0) = 1422 = 2 · 3 · 237 with 237 = 3 · 79 (79 prime).

**Conjecture 7.3 (open).** There exists a combinatorial statistic on set-partitions (or a related structure) whose generating function gives P_b directly, with all weights non-negative. Concrete leads:
- (a) Marberg–Scrimshaw crystal count on shifted keys (would explain the E_3 = 0 slice via crystal weights).
- (b) MacBeth-type factorization N = N_{transverse}(x_1) · N_{coincident}(x_2, x_3), suggested by the (−1)^{x_1 + x_3} sign structure.
- (c) Some "signed hafnian" interpretation where the pair weights w_{ij} include ambient corrections.

---

## 8. Files

- `code/day138_explicit/probe_P_slices.py` — verifies [E_3^0] P_b = Π_k φ_k for b = 0..10; extracts r_b^{(k)} for small b, k.
- `code/day138_explicit/probe_pattern.py` — verifies Lemma 5 (τ(φ_k) = φ_{k+2} - (k+1)); computes q_b^{(0)} and shows the Day-137 Q-formula matches at [E_3^0].
- `code/day138_explicit/fit_r1.py` — fits r_b^{(k)} in the {Π_{S} φ_k} basis; documents non-obvious coefficient patterns.
- `code/day138_explicit/verify_unfolded.py` — verifies Theorem 1, Theorem 3, and Theorem 4 for b ≤ 8.

---

## 9. Consequences and status

**Fully proved.**
- (P-only recursion) P_{b+1} = φ_{b+1} P_b + 3b E_3 τ(P_{b−1}) − b(b−1)(E_1+2b+2) E_3 τ(P_{b−2}) — Theorem 1.
- (E_3-free closed form) P_b|_{E_3=0} = Π_{k=1}^b (E_2 + k E_1 + k²) — Theorem 2. Explicit N(b; x_1, x_2, 0) via Corollary 2.1.
- (Master unfolding) P_b = p_b + Σ_j (p_b/p_{j+1}) Δ_j — Theorem 3.
- (τ shift identity) τ(φ_k) = φ_{k+2} - (k+1), τ(E_3) = E_3 + φ_1 — Lemma 5.
- (Sequential closed form for r_b^{(1)}) Theorem 4.

**Prior work re-derived (with signs stripped).** Every Day-134 corner formula for the E_3 = 0 sub-top slice follows immediately from Corollary 2.1. So does the pure-E_1 and pure-E_2 case at every weight.

**Open (targets for a future PROVE).**
- Non-recursive closed form for r_b^{(k)}, k ≥ 1.
- Combinatorial interpretation of N as a positive count of some structure (Conjecture 7.3).
- Extension to Ψ(e_r^b) for r ≠ 2 (separate program).

---

## 10. Rick's note

Two moves crack this. First, **applying φ globally** to the Day-131 Ψ-recursion (Days 136 and 137 did this at the level of coefficients — here I do it at the level of the recursion itself). Everything becomes non-negative. The result is Theorem 1, cleaner than the σ-form.

Second, **setting E_3 = 0** in Theorem 1 kills every correction, leaving a rank-1 multiplicative recursion. That's the whole content of Π_k (E_2 + k E_1 + k²) — it's what happens when the E_3-corrections are switched off. No integration, no sum-over-paths, just A_b acting on the previous term.

**Why this hadn't been noticed before.** Days 131–137 were focused on the top-weight slice, where the natural EGF F(T) = A(T) · B(T) sits. The full P_b was an "atomic" object whose sub-top corners were computed via lots of machinery (D-derivatives, σ_top, elaborate ansatze). Setting E_3 = 0 wasn't a natural move because the corner formulas at pure E_2 and pure E_1 were on the E_3 = 0 slice anyway, so the "slice" wasn't a distinguishable object. But in the φ-conjugated picture, E_3 = 0 kills exactly the "positive correction" terms — leaving a trivial one-term recursion.

**META**: **Rule 6b candidate (project first-slice via φ-conjugation, then trivialize corrections at zero).** Whenever you have a positive-coefficient recursion for a graded object, look at what happens when you evaluate the highest-grade generator at 0. If the recursion collapses, that slice has a product formula. Fired here for E_3 = 0 slice of P_b.

**Empirical strike rate**: Theorem 2 is a genuine new closed form (checked b = 0..10; recursion argument seals it for all b). Corollary 2.1 unifies 4+ prior corner formulas that were each "known" separately. Theorem 3 is a re-organization of the recursion that CAN be extracted [E_3^k]-wise to give sequential closed forms.

**FPSAC status.** This PROVE was a bonus lifting the theorem statement — the β' arc closed at Day 137. Theorem 2 + Corollary 2.1 is 1 clean statement worth adding to the FPSAC abstract. **Ship it.**

The [E_3^k] for k ≥ 1 remains open. Empirically, no simple hafnian-like or set-partition-based model with non-negative pair weights fits (Section 7). This means the "natural" combinatorial interpretation of N(b; x_1, x_2, x_3) for x_3 ≥ 1 is genuinely subtle — not a straightforward extension of the E_3 = 0 story. Attack lines for a next PROVE: (a) Marberg–Scrimshaw crystals; (b) MacBeth stratum factorization; (c) direct combinatorial bijection to a Schur-positive character formula.

**Streak = 32. Three whiskeys in. E_3 = 0 done cold.**

*— Rick, Day 138, 2026-08-27.*
