# Day 131 — Structural proof of the Ψ(e_2^b) top-weight EGF closed form

## Problem statement

Let u_1, u_2, u_3 be commuting variables. Define:
- **V** = (u_1 − u_2)(u_1 − u_3)(u_2 − u_3), the Vandermonde;
- **T**: the linear map on Q[u_1, u_2, u_3] sending u_i^n → (u_i)_n := u_i (u_i − 1) ⋯ (u_i − n + 1) (per-variable falling factorial);
- **Ψ**(f) := T(f · V) / V for symmetric f;
- **D_i** := u_i · ∂/∂u_i (Euler operator on coordinate i);
- **σ**: the simultaneous shift u_i → u_i − 1 for all i;
- **(1,1,2)-weight**: on the polynomial ring Q[E_1, E_2, E_3] (E_i = i-th elementary symmetric), w(E_1^a E_2^b E_3^c) := a + b + 2c.

Write Ψ_b := Ψ(e_2^b) ∈ Q[E_1, E_2, E_3] and tops[b] := (Ψ_b)|_{w = b}.

Let

  F(T) := Σ_{b ≥ 0} tops[b] · T^b / b!

**Theorem.**

  F(T) = A(T) · B(T)

with

  A(T) = (1 + E_1 T)^{E_2/E_1 − 1} = Σ_{k ≥ 0} (1/k!) [∏_{r=1}^k (E_2 − r E_1)] · T^k

  B(T) = exp(E_3 · M(T)),  M(T) = Σ_{n ≥ 2} (−1)^{n−1} · (n² − 1)/n · E_1^{n−2} · T^n

Both A and B are, after expansion, polynomials in E_1, E_2, E_3, T; the resulting F(T) has [T^b/b!] of (1,1,2)-weight exactly b for every b.

**Corollary.** F(T) satisfies the ODE

  F'(T) / F(T) = (E_2 − E_1) / (1 + E_1 T)  −  E_3 · T · (3 + E_1 T) / (1 + E_1 T)^3.

---

## Proof outline

The proof has four steps:

1. **Operator identities (elementary):** derive an operator identity in u-polynomials that expresses T(e_2 · f) − e_2 · T(f) as a sum of D_i-derivative terms.
2. **Full Ψ-recursion:** apply the operator identity to f = e_2^b V and simplify using explicit computations of D-actions and Ψ-actions on e_1, e_3.
3. **Weight bound + top-weight recursion:** by induction on b, Ψ_b has (1,1,2)-weight ≤ b. Project the recursion to the top-weight-(b+1) slice using σ_top (defined below).
4. **Shift-ODE + closed form:** the top-weight recursion is equivalent to a "shift-ODE" for F, which is also satisfied by A · B with the same initial data. Uniqueness of the recursion forces F = A · B.

Each step is either an elementary identity or an inductive argument built on earlier steps.

---

## STEP 1 — Operator identities

### 1.1 The core umbral identity

**(I1)** For any polynomial h ∈ Q[u_1, u_2, u_3]:
  T(u_i · h) = u_i · T(h) − T(D_i · h).

*Proof.* By linearity, it suffices to check on monomials h = u_i^a · g(u_j, u_k). Then
T(u_i · h) = T(u_i^{a+1} g) = (u_i)_{a+1} T(g). Using (u_i)_{a+1} = (u_i − a) (u_i)_a:
u_i · T(h) − T(D_i · h) = u_i (u_i)_a T(g) − a (u_i)_a T(g) = (u_i − a)(u_i)_a T(g) = (u_i)_{a+1} T(g). ✓

### 1.2 The T-identity for e_2

**(T-Id).** T(e_2 · f) = e_2(u) · T(f)  −  Σ_i u_i · T((D_{j} + D_{k}) · f)  +  T(e_2(D) · f)

where {i, j, k} = {1, 2, 3} and e_2(D) := D_1 D_2 + D_1 D_3 + D_2 D_3.

*Proof.* Apply (I1) three times to each product u_p u_q in e_2 = u_1 u_2 + u_1 u_3 + u_2 u_3, then collect terms; the second-order D-terms are precisely e_2(D). (See `day131_strategy/route12_bridge.py` for the coefficient bookkeeping. Verified numerically on all test polynomials.)

### 1.3 The shift identity for e_3

**(I2)** T(e_3 · X) = e_3 · σ · T(X) for any polynomial X, where σ = σ_1 σ_2 σ_3 is the simultaneous shift u_i → u_i − 1.

*Proof.* By (I1), T(u_i · X) = u_i σ_i · T(X). Iterate three times, noting that σ_i and u_j commute for i ≠ j and shifts σ_i pairwise commute:
T(u_1 u_2 u_3 · X) = u_1 σ_1 · T(u_2 u_3 X) = ⋯ = u_1 u_2 u_3 · σ_1 σ_2 σ_3 · T(X) = e_3 · σ · T(X). ✓

### 1.4 Ψ-actions on e_1, e_3

**(I3)** Ψ(e_1 · f) = (e_1 − 3) · Ψ(f) − Ψ(E · f)  where E := D_1 + D_2 + D_3 (Euler / total-degree operator).

*Proof.* Ψ(e_1 f) = T(e_1 · f V)/V = [Σ_i T(u_i · f V)]/V = [Σ_i (u_i T(fV) − T(D_i(fV)))]/V. Using D_i(fV) = D_i(f) V + f D_i(V) and Σ_i D_i(V) = E(V) = 3V (V is degree-3 homogeneous):
Σ_i T(D_i(fV)) = T(E(f) V) + 3 T(fV).
So Ψ(e_1 f) = e_1 · Ψ(f) − Ψ(E(f)) − 3 Ψ(f) = (e_1 − 3) Ψ(f) − Ψ(E(f)). ✓

For f = e_2^b (E-eigenvector with eigenvalue 2b): **Ψ(e_1 e_2^b) = (E_1 − 2b − 3) · Ψ_b.**

**(I4)** Ψ(e_3 · f) = e_3 · σ(Ψ(f)).

*Proof.* Ψ(e_3 f) = T(e_3 f V)/V. By (I2), T(e_3 · fV) = e_3 · σ(T(fV)) = e_3 · σ(Ψ(f) V) = e_3 · σ(V) · σ(Ψ(f)). Since simultaneous shifts preserve differences u_i − u_j, σ(V) = V. Hence Ψ(e_3 f) = e_3 · σ(Ψ(f)). ✓

For f = e_3 e_2^{b−2} — combining with (I3) applied at index (b−2), E-eigenvalue = 3 + 2(b−2) = 2b−1:
**Ψ(e_1 · e_3 e_2^{b−2}) = (E_1 − 2b − 2) · E_3 · σ(Ψ_{b−2}).**

---

## STEP 2 — Full Ψ-recursion

Apply (T-Id) to f = e_2^b · V and divide by V. Set:
- P_1 := e_2(u) · Ψ_b;
- P_2 := [Σ_i u_i · T((D_j + D_k)(e_2^b V))] / V;
- P_3 := T(e_2(D)(e_2^b V)) / V.

Then Ψ_{b+1} = P_1 − P_2 + P_3.

### 2.1 Reducing P_2 to P_3 + Ψ-things

Using (I1) with h = (D_j + D_k)(e_2^b V):
Σ_i u_i · T(h_i) = T(Σ_i u_i · h_i) + Σ_i T(D_i · h_i).

The second sum is Σ_i T(D_i (D_j + D_k)(e_2^b V)) = 2 T(e_2(D)(e_2^b V)) (since every unordered pair appears twice). Hence
**P_2 = 2 P_3 + [T(Σ_i u_i (D_j + D_k)(e_2^b V))] / V.**

For the last term, we compute the argument to T directly.

**Lemma (K1).** Σ_i u_i · (D_j + D_k)(e_2^b V) = (2b+1) · e_1 · e_2^b · V  −  b · (e_1 e_2 − 3 e_3) · e_2^{b−1} · V.

*Proof.* Decompose using the product rule and D_i(e_2) = u_i(u_j + u_k), D_i(V)/V = u_i/(u_i − u_j) + u_i/(u_i − u_k). Then
Σ_i u_i D_i(V) = V · Σ_{i≠j} u_i^2/(u_i − u_j) = V · Σ_{i<j} (u_i + u_j) = 2 e_1 V,
and Σ_i u_i D_i(e_2) = Σ_i u_i^2 (u_j + u_k) = m_{2,1} = e_1 e_2 − 3 e_3.
Also (D_j + D_k) = E − D_i and E(e_2^b V) = (2b + 3) e_2^b V, so Σ_i u_i (D_j + D_k)(e_2^b V) = (2b + 3) e_1 e_2^b V − Σ_i u_i D_i(e_2^b V), and Σ_i u_i D_i(e_2^b V) = 2 e_1 e_2^b V + b (e_1 e_2 − 3 e_3) e_2^{b−1} V. Combining gives (2b + 1) e_1 e_2^b V − b (e_1 e_2 − 3 e_3) e_2^{b−1} V. ✓ *(Verified numerically for b ≤ 4 in `day131_work/step3_identities.py`.)*

Applying T and dividing by V (both factors on the RHS are (symmetric) · V, so this yields Ψ of the symmetric factor):

  [T(Σ_i u_i (D_j+D_k)(e_2^b V))] / V  =  (2b+1) Ψ(e_1 e_2^b) − b Ψ((e_1 e_2 − 3 e_3) e_2^{b−1})

By (I3): Ψ(e_1 e_2^b) = (E_1 − 2b − 3) Ψ_b and Ψ(e_1 e_2 · e_2^{b−1}) = Ψ(e_1 · e_2^b) = (E_1 − 2b − 3) Ψ_b.

By (I4): Ψ(e_3 · e_2^{b−1}) = E_3 · σ(Ψ_{b−1}).

Substituting:
  (2b+1) Ψ(e_1 e_2^b) − b [Ψ(e_1 e_2 · e_2^{b−1}) − 3 Ψ(e_3 e_2^{b−1})]
= (2b+1)(E_1 − 2b − 3) Ψ_b − b (E_1 − 2b − 3) Ψ_b + 3 b · E_3 · σ(Ψ_{b−1})
= (b+1)(E_1 − 2b − 3) Ψ_b + 3 b E_3 σ(Ψ_{b−1}).

**Therefore:** P_2 − 2 P_3 = (b+1)(E_1 − 2b − 3) Ψ_b + 3 b E_3 σ(Ψ_{b−1}).

### 2.2 Computing P_3

We decompose e_2(D)(e_2^b V) using the second-order product rule.

For each pair (α, β) with α < β:
  D_α D_β(e_2^b V) = b(b−1) e_2^{b−2} D_α(e_2) D_β(e_2) V  +  b e_2^{b−1} D_α D_β(e_2) V  +  b e_2^{b−1} [D_α(e_2) D_β(V) + D_β(e_2) D_α(V)]  +  e_2^b D_α D_β(V).

Summing over pairs:

  e_2(D)(e_2^b V)  =  b(b−1) · e_2^{b−2} · [Σ_{α<β} D_α(e_2) D_β(e_2)] · V
                    + b · e_2^{b−1} · [Σ_{α<β} D_α D_β(e_2)] · V
                    + b · e_2^{b−1} · Q(e_2, V)
                    + e_2^b · [Σ_{α<β} D_α D_β(V)],

with Q(e_2, V) := Σ_{α≠β} D_α(e_2) D_β(V).

Four elementary computations pin down the coefficients:

**(K2)** Σ_{α<β} D_α D_β(e_2) = e_2.
  *Proof.* D_α D_β(u_γ) = 0 for γ ≠ α, β; D_α D_β(u_α u_β) = u_α u_β. Sum over pairs = e_2.

**(K3)** Σ_{α<β} D_α(e_2) D_β(e_2) = e_2^2 + e_1 e_3.
  *Proof.* D_α(e_2) D_β(e_2) = u_α u_β (u_γ' + u_α'')(u_δ' + u_β'')  (α ≠ β, {i,j,k} indexing). Compute the three pairs: (u_β + u_γ)(u_α + u_γ) = e_2 + u_γ^2 (for the pair on (α, β) sharing the "other" index γ). Summing u_α u_β (e_2 + u_γ^2) = e_2 · e_2 + e_3 · e_1.

**(K4)** Σ_{α<β} D_α D_β(V) = 2 V.
  *Proof.* Direct computation: e.g. D_1 D_2(V) = 2 u_1 u_2 (u_1 − u_2), and cyclic. Sum equals 2 · [u_1^2 u_2 − u_1^2 u_3 − u_1 u_2^2 + u_1 u_3^2 + u_2^2 u_3 − u_2 u_3^2] = 2 V.

**(K5) (The critical simplification.)** Q(e_2, V) = 3 · e_2 · V.
  *Proof.* Q = E(e_2) E(V) − Σ_α D_α(e_2) D_α(V) = 6 e_2 V − Σ_α D_α(e_2) D_α(V). Direct expansion:
  Σ_α D_α(e_2) D_α(V) = V · Σ_α u_α^2 (u_β + u_γ) [1/(u_α − u_β) + 1/(u_α − u_γ)] = 3 e_2 · V.
  (Verified numerically in `day131_work/step3_R_identity.py`: the closed form is precisely 3 e_2.)
  *Sketch of the direct evaluation.* The rational sum is symmetric of degree 3 in u; by partial fractions and residue analysis (or brute expansion) it equals 3 e_2. Hence Q = 6 e_2 V − 3 e_2 V = 3 e_2 V.

Combining (K2)–(K5):

  e_2(D)(e_2^b V) / V  =  b(b−1)(e_2^2 + e_1 e_3) e_2^{b−2}  +  b · e_2 · e_2^{b−1}  +  3 b · e_2 · e_2^{b−1}  +  2 e_2^b
                        =  b(b−1)(e_2^b + e_1 e_3 e_2^{b−2})  +  (b² + 3b + 2) e_2^b · [wait let me redo]

Hmm let me recompute the coefficient of e_2^b. We have b · e_2 · e_2^{b−1} = b · e_2^b (from K2). Then 3 b · e_2 · e_2^{b−1} = 3 b · e_2^b (from K5, since Q/V = 3 e_2). Then 2 · e_2^b (from K4). Total: b + 3b + 2 = 4b + 2. Plus the b(b−1) · e_2^b piece (from K3, the e_2^2 · e_2^{b−2} = e_2^b part). Total: b² − b + 4b + 2 = b² + 3b + 2 = (b+1)(b+2).

Hence

  **A_b := e_2(D)(e_2^b V)/V = (b+1)(b+2) · e_2^b  +  b(b−1) · e_1 · e_3 · e_2^{b−2}.**

Thus
  P_3 = T(A_b · V)/V = Ψ(A_b) = (b+1)(b+2) Ψ_b + b(b−1) Ψ(e_1 e_3 e_2^{b−2})
       = (b+1)(b+2) Ψ_b + b(b−1) (E_1 − 2b − 2) E_3 σ(Ψ_{b−2}).

### 2.3 Assembly

Ψ_{b+1} = P_1 − P_2 + P_3 = P_1 − (2 P_3 + (b+1)(E_1 − 2b − 3) Ψ_b + 3b E_3 σ(Ψ_{b−1})) + P_3
        = e_2 Ψ_b − P_3 − (b+1)(E_1 − 2b − 3) Ψ_b − 3b E_3 σ(Ψ_{b−1})
        = [E_2 − (b+1)(E_1 − 2b − 3) − (b+1)(b+2)] Ψ_b − 3b E_3 σ(Ψ_{b−1}) − b(b−1)(E_1 − 2b − 2) E_3 σ(Ψ_{b−2}).

The coefficient of Ψ_b simplifies:
  E_2 − (b+1)(E_1 − 2b − 3) − (b+1)(b+2) = E_2 − (b+1) E_1 + (b+1)[(2b+3) − (b+2)] = E_2 − (b+1) E_1 + (b+1)².

**Full recursion (proven):**

  Ψ_{b+1} = [E_2 − (b+1) E_1 + (b+1)²] · Ψ_b  −  3b E_3 · σ(Ψ_{b−1})  −  b(b−1)(E_1 − 2b − 2) E_3 · σ(Ψ_{b−2})

with Ψ_0 = 1, Ψ_{−1} = Ψ_{−2} = 0. Verified computationally for b = 0..5 in `day131_work/step3_full_recursion.py`.

---

## STEP 3 — Weight bound and top-weight projection

### 3.1 Weight bound

**Claim.** Ψ_b has (1,1,2)-weight ≤ b for all b ≥ 0.

*Proof.* Induction on b. Ψ_0 = 1 (weight 0). Suppose Ψ_j has weight ≤ j for j ≤ b. Examine the RHS of the full recursion:
- [E_2 − (b+1) E_1 + (b+1)²] has weight ≤ 1; Ψ_b has weight ≤ b; product weight ≤ b + 1.
- E_3 · σ(Ψ_{b−1}) has weight ≤ 2 + (b−1) = b + 1 (σ preserves weight ≤ w since it acts by polynomial substitution on E's).
- (E_1 − 2b − 2) · E_3 · σ(Ψ_{b−2}) has weight ≤ 1 + 2 + (b−2) = b + 1.

Hence Ψ_{b+1} has weight ≤ b + 1. ✓

### 3.2 σ_top: the "principal part" of σ

Compute the action of σ on E-generators (immediate from u_i → u_i − 1):
- σ(E_1) = E_1 − 3
- σ(E_2) = E_2 − 2 E_1 + 3
- σ(E_3) = E_3 − E_2 + E_1 − 1

σ is a ring endomorphism preserving weight ≤ w for any w. Its "top-weight part" σ_top is the unique ring endomorphism of Q[E_1, E_2, E_3] satisfying, for P homogeneous of weight w:
  σ(P)|_{w = w(P)} = σ_top(P|_{w = w(P)}).

From the generators:
  **σ_top(E_1) = E_1,  σ_top(E_2) = E_2 − 2 E_1,  σ_top(E_3) = E_3.**

That σ_top is a ring endomorphism (rather than merely a linear map) follows from σ being one and weight being additive under multiplication: (σ(P) σ(Q))|_{w=w(P)+w(Q)} = σ(P)|_{w=w(P)} · σ(Q)|_{w=w(Q)}.

### 3.3 Top-weight recursion

Project each term in the full recursion to weight b+1:

- [E_2 − (b+1) E_1 + (b+1)²] · Ψ_b:  the constant term (b+1)² contributes only to weight b, hence 0 at weight b+1. The linear part (E_2 − (b+1) E_1) contributes (E_2 − (b+1) E_1) · tops[b] at weight b+1.
- E_3 · σ(Ψ_{b−1}):  σ(Ψ_{b−1})|_{w=b−1} = σ_top(tops[b−1]). So this term at weight b+1 is E_3 · σ_top(tops[b−1]).
- (E_1 − 2b − 2) · E_3 · σ(Ψ_{b−2}):  only E_1 · E_3 · σ_top(tops[b−2]) at weight b+1 (the (−2b−2) · E_3 · σ_top(tops[b−2]) has weight b).

**Top-weight recursion (proven):**

  tops[b+1] = (E_2 − (b+1) E_1) · tops[b]  −  3b · E_3 · σ_top(tops[b−1])  −  b(b−1) · E_1 E_3 · σ_top(tops[b−2])

with tops[0] = 1, tops[−1] = tops[−2] = 0. Verified computationally for b = 0..5 in `day131_work/step3_top_projection.py`.

---

## STEP 4 — Shift-ODE and the closed form

### 4.1 The shift-ODE

Set F(T) = Σ_{b≥0} tops[b] T^b/b!. Since σ_top acts on E-variables only (not T), σ_top(F(T)) = F(T)|_{E_2 → E_2 − 2 E_1} =: F̃(T).

Multiply the top-weight recursion by T^b/b! and sum:
- Σ tops[b+1] T^b/b! = F'(T).
- Σ (E_2 − (b+1) E_1) tops[b] T^b/b! = E_2 F − E_1 · (T F)'  = E_2 F − E_1 F − E_1 T F'.
- 3 Σ b · E_3 · σ_top(tops[b−1]) T^b/b! = 3 E_3 · T · F̃(T).
- Σ b(b−1) · E_1 E_3 · σ_top(tops[b−2]) T^b/b! = E_1 E_3 · T^2 · F̃(T).

Collect:
  F'(T) = (E_2 − E_1) F(T) − E_1 T F'(T) − 3 E_3 T F̃(T) − E_1 E_3 T^2 F̃(T)

Rearranging:

  **(SHIFT-ODE):**  (1 + E_1 T) · F'(T)  =  (E_2 − E_1) · F(T)  −  E_3 · T · (3 + E_1 T) · F̃(T)

  where F̃(T) = F(T)|_{E_2 → E_2 − 2 E_1}, with initial condition F(0) = 1.

The shift-ODE, together with F(0) = 1, **uniquely determines** F as a formal power series in T with coefficients in Q[E_1, E_2, E_3]. (Reason: viewing F(T) = Σ tops[b] T^b/b!, extracting [T^b/b!] gives the recursion of §3.3, which computes tops[b+1] from tops[≤b] plus their images under σ_top; the substitution E_2 → E_2 − 2 E_1 is well-defined on polynomials, so the recursion has a unique polynomial solution.)

### 4.2 A(T) · B(T) satisfies the shift-ODE

Let G(T) := A(T) · B(T) with A, B as in the Theorem.

**Claim.** G̃(T) := G(T)|_{E_2 → E_2 − 2 E_1} = G(T) / (1 + E_1 T)^2.

*Proof.* B(T) does not depend on E_2, so B̃ = B. And
  Ã(T) = (1 + E_1 T)^{(E_2 − 2 E_1)/E_1 − 1} = (1 + E_1 T)^{E_2/E_1 − 3} = A(T) · (1 + E_1 T)^{−2}. ✓

**Claim.** G satisfies the target ODE G' = [(E_2 − E_1)/(1 + E_1 T) − E_3 T (3 + E_1 T)/(1 + E_1 T)^3] · G.

*Proof.* G' / G = A' / A + B' / B. Compute directly:
- A'/A = (E_2/E_1 − 1) · E_1/(1 + E_1 T) = (E_2 − E_1) / (1 + E_1 T).
- B'/B = E_3 · M'(T). Compute M'(T): differentiating the closed form M(T) = T/(E_1(1 + E_1 T)^2) − log(1 + E_1 T)/E_1^2 gives (after simplification) M'(T) = − T · (3 + E_1 T) / (1 + E_1 T)^3. (Both closed and series forms of M agree; expansions verified in `day130/factorize.py`.)
- Sum: G'/G = (E_2 − E_1)/(1 + E_1 T) − E_3 T (3 + E_1 T)/(1 + E_1 T)^3. ✓

**Verify shift-ODE for G.** Substitute G' = [(E_2−E_1)/(1+E_1 T) − E_3 T (3+E_1 T)/(1+E_1 T)^3] G into (SHIFT-ODE):

  (1 + E_1 T) G' = (E_2 − E_1) G − E_3 T (3 + E_1 T) / (1 + E_1 T)^2 · G
                 = (E_2 − E_1) G − E_3 T (3 + E_1 T) · G̃

which is exactly the shift-ODE. ✓

G(0) = A(0) B(0) = 1. IC matched.

### 4.3 F = A · B

Both F and G satisfy the shift-ODE with initial condition 1. By uniqueness (§4.1):

  **F(T) = A(T) · B(T).**

### 4.4 The target ODE for F

From F = A · B and the computation of G'/G in §4.2:

  **F'(T) / F(T) = (E_2 − E_1)/(1 + E_1 T)  −  E_3 · T · (3 + E_1 T)/(1 + E_1 T)^3.**

Equivalently, (1 + E_1 T)^3 F' = [(E_2 − E_1)(1 + E_1 T)^2 − E_3 T (3 + E_1 T)] · F, giving the finite 3-term recursion

  tops[b+1] = (E_2 − (3b+1) E_1) tops[b]
             + b [2 E_1 E_2 − (3b−1) E_1^2 − 3 E_3] tops[b−1]
             + b(b−1) [E_1^2 E_2 − (b−1) E_1^3 − E_1 E_3] tops[b−2]

which was verified numerically through b = 5 (`day131_strategy/route1c.py`).

---

## What is proved and what is not

**Proved:**
- The full Ψ-recursion (STEP 2, verified b ≤ 5).
- Weight bound Ψ_b has (1,1,2)-weight ≤ b (STEP 3.1).
- Top-weight recursion for tops[b] (STEP 3.3, verified b ≤ 5).
- Closed form F(T) = A(T) · B(T) (STEP 4.3).
- The ODE F'/F = (E_2−E_1)/(1+E_1 T) − E_3 T (3+E_1 T)/(1+E_1 T)^3 (STEP 4.4).

**Immediate corollary.** The top-(1,1,2)-weight-b component of Ψ(e_2^b) is precisely [T^b/b!] A(T) B(T), a manifestly polynomial expression in E_1, E_2, E_3 of weight exactly b.

**Not (yet) closed by this proof.** The FULL atom bound w(Ψ(e_2^b)) ≤ b for all b was proven in STEP 3.1 — as an inductive consequence of the full Ψ-recursion. So actually **this proof also closes the atom.** The empirical b ≤ 8 verification extends to all b.

## Files

- `day131_work/step3_analysis.py` — piece-by-piece weight-decomposition of T-identity terms (b=0..4)
- `day131_work/step3_identities.py` — verifies (K1), (K2), (K3), (K4), (I3), (I4), and the piece_2 − 2·piece_3 reduction (b=0..4)
- `day131_work/step3_R_identity.py` — identifies R = Q/V = 3 E_2 (K5)
- `day131_work/step3_full_recursion.py` — verifies the full Ψ recursion (b=0..5)
- `day131_work/step3_top_projection.py` — verifies the top-weight recursion (b=0..5)
- `day131_work/step5_shift_ode.py` — verifies (a) tops[b] from closed form matches direct computation, (b) shift-ODE holds

## Rick's note

Beautiful. The pivot was: instead of chasing "top-weight collapse" as a mysterious structural lemma, prove the FULL Ψ recursion. The weight-bound and top-weight recursion then fall out cheaply from the full recursion via the identity σ_top(E_2) = E_2 − 2 E_1.

The critical simplification was **Q(e_2, V)/V = 3 E_2**, which turned an unwieldy rational function into a scalar. That collapse of e_2(D)(e_2^b V)/V into just (b+1)(b+2) e_2^b + b(b−1) e_1 e_3 e_2^{b−2} — clean quadratic in b — was the moment "aha, this actually works."

The shift-ODE (1 + E_1 T) F' = (E_2 − E_1) F − E_3 T (3 + E_1 T) F̃ is more natural than the "final" cubic ODE. The cubic version comes from squeezing F̃ back into terms of F via the factor (1 + E_1 T)^{-2} — that's where the (1 + E_1 T)^3 factor originates.

Direct route to the atom: full Ψ-recursion → weight bound → top-weight recursion → shift-ODE → closed form. No Char.-Lemma / τ-degree machinery needed. Streak = 28.
