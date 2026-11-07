---
name: The crown-jewel atom is closed — w(Ψ(e_2^b)) ≤ b PROVED for ALL b (Day 131)
description: The central open gap of Rick's β' arc since Day 125 — the 1-parameter atom w(Ψ(e_2^b)) ≤ b — is CLOSED as an immediate corollary of the Day 131 EGF closed form F(T) = A(T)·B(T). The closure passes through operator formula Ψ(f) = T(fV)/V (Day 125), T-shift operator identity via falling-factorial umbral (Day 130), full Ψ-recursion Ψ_{b+1} = [E_2−(b+1)E_1+(b+1)²]Ψ_b − 3b·E_3·σ(Ψ_{b−1}) − b(b−1)(E_1−2b−2)·E_3·σ(Ψ_{b−2}) proved via K1-K5 elementary computations + I3/I4 Ψ-actions, top-weight projection via σ_top (E_2→E_2−2E_1), and shift-ODE uniqueness. Route α (τ-degree preservation, Day 127 machinery) permanently HISTORICAL. The full 3-parameter Day 124 monomial claim (w(Ψ(e_1^{a_1}e_2^{a_2}e_3^{a_3})) ≤ a_1+a_2+2a_3) is now a THEOREM via Day 125 factorization theorem + Day 131 atom closure.
type: project
---

# Crown Jewel Closed — w(Ψ(e_2^b)) ≤ b PROVED for ALL b

**Date closed:** Day 131 (2026-08-23).
**Central open gap since:** Day 125 (2026-08-22).
**Machinery:** operator formula + T-shift identity + full Ψ-recursion + σ_top projection + shift-ODE.

## The claim

Ψ: Sym_3 → Sym_3 sending s_μ → s*_μ (Molev-Olshanski shifted Schur, in u-basis). Claim: for every b ≥ 0,

  **w(Ψ(e_2^b)) ≤ b**

where w is the (1,1,2)-weight (E_1 → 1, E_2 → 1, E_3 → 2). This is the 1-parameter atom to which Day 125's factorization theorem reduces the full 3-parameter monomial preservation claim.

## The closure

The closure was NOT via the anticipated Route α (τ-degree preservation under Char. Lemma substitution, Day 127 machinery). Instead, it went via the operator formula.

**Key steps:**

1. **Day 125 Lemma 0 (operator formula):** Ψ(f) = T(fV)/V where T(u^β) = ∏ [u_i]_{β_i}, V = Vandermonde. One-line proof via S_3-antisymmetry of T(fV).

2. **Day 130 T-shift identity:** T(e_2·f) = e_2(u)·T(f) − Σ u_i·T((D_j+D_k)f) + T(e_2(D_1,D_2,D_3)·f), where D_i = u_i ∂/∂u_i, {i,j,k} = {1,2,3}. Proved from falling-factorial umbral identity u_i(u_i)_n = (u_i)_{n+1} + n(u_i)_n. Each RHS group separately S_3-symmetric.

3. **Day 131 K5 (the load-bearing lemma):** Q(e_2, V)/V = 3·E_2, a scalar. The apparently-messy cross-derivative term Σu_i·e_1_hat_i(D)·V/V (where e_1_hat_i = derivative operators on remaining vars) collapses to a scalar via direct antisymmetrization + Vandermonde identity.

4. **Day 131 full Ψ-recursion (proved for ALL b, no weight assumption):**
   
   Ψ_{b+1} = [E_2 − (b+1)E_1 + (b+1)²] Ψ_b − 3b·E_3·σ(Ψ_{b−1}) − b(b−1)(E_1−2b−2)·E_3·σ(Ψ_{b−2})
   
   where σ is the simultaneous shift u_i → u_i − 1 acting on Sym_3 as ring endomorphism E_1 → E_1, E_2 → E_2 − 2·E_1, E_3 → E_3 (top-weight action = σ_top).

5. **Weight bound corollary (inductive):** Each RHS term has weight ≤ b+1: E_2·Ψ_b has weight 1 + b = b+1; E_1·Ψ_b has weight 1 + b; E_3·σ(Ψ_{b−1}) has weight 2 + (b−1) = b+1; E_1·E_3·σ(Ψ_{b−2}) has weight 1+2+(b−2) = b+1. Base cases: Ψ_0 = 1 (weight 0), Ψ_1 = Ψ(e_2) = e_2 (weight 1). Induction closes.

6. **Top-weight recursion via σ_top:** Projecting to top-(1,1,2)-weight-(b+1) gives tops[b+1] = (E_2 − (b+1)E_1)·tops[b] − 3b·E_3·σ_top(tops[b−1]) − b(b−1)·E_1·E_3·σ_top(tops[b−2]).

7. **Shift-ODE uniqueness:** F(T) := Σ tops[b] T^b/b! satisfies F'(T)/F(T) = (E_2 − E_1)/(1+E_1·T) − E_3·T·(3+E_1·T)/(1+E_1·T)^3 with F(0) = 1. Unique solution: F(T) = (1+E_1·T)^{E_2/E_1 − 1} · exp(E_3·M(T)) with M(T) = T/(E_1·(1+E_1·T)^2) − log(1+E_1·T)/E_1^2.

## What this replaces

**Route α (Day 127 machinery)**: τ-degree preservation under Char. Lemma substitution u_1=τ, u_2=y, u_3=c (with y+c=s, yc=τ). PROVED per-Schur for ℓ ≤ 3, empirical ℓ = 4 (53/53), 5 (19/19). Day 129 showed the max-d combinatorial part is universal in ℓ (6-line Stirling matrix argument). But full τ-degree preservation on sums with cancellations was OPEN at ℓ ≥ 4.

Day 131 makes the whole Route α line **PERMANENTLY HISTORICAL**. The atom is proved via operator formula + Ψ-recursion, not τ-degree. Cases A/B, Q_{m,n,p} diagonal contributions, three-way collision analysis — all shelved.

## What follows

**Immediate corollary (Day 125 factorization theorem + Day 131 atom):**

For every 3-parameter e-monomial:

  **w(Ψ(e_1^{a_1} · e_2^{a_2} · e_3^{a_3})) ≤ a_1 + a_2 + 2a_3**

This is the FULL Day 124 monomial claim, now a theorem for ALL (a_1, a_2, a_3). No empirical caveat.

**Extended (Day 133 density theorem):**

Not only is the weight bound tight, the top-weight slice has FULL SUPPORT: every (x_1, x_2, x_3) with x_1 + x_2 + 2x_3 = b has [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b] = (−1)^{b−x_2−x_3} · N(b; x_1, x_2, x_3) with N > 0 explicit. See `2026-08-25-day133-density-sign-mechanism.md`.

## Historical significance

**This closes the entire β' arc mathematically.** The Day 118 shifted-Pieri (**), Day 120 (C2), Day 121 (C1), Day 125 factorization theorem, and Day 131 atom together give: Rick's Layer-Shape Lemma at all d ⟹ β' polynomial coefficients have the desired structure ⟹ β'(c) 2-adic launch (Days 91-101) closes.

The atom was the last algebraic gap. What remains is EXPOSITION.

**Bonus.** The technique (operator formula + falling-factorial umbral identity + shift-ODE uniqueness) is transferable. Extensions:
- Ψ(e_r^b) for r ≠ 2 need analogs of K1-K5. The scalar collapse K5 (Q(e_r, V)/V clean) is the load-bearing lemma to check.
- Ψ(p_k^b) (power-sum monomials) may admit a similar generating series.
- The technique should work for OTHER shifted-Schur-type maps (skew shifted Schur, factorial versions), giving a template.

## Meta

The reduction chain (Day 125) sat with the τ-degree machinery dominating attention for 5 days. The Day 129 rule ("read the claim; check soft lower bound first") triggered a Day 130 re-read of Day 125's reduction, which found: **the atom is Char.-Lemma-independent, so try the operator formula directly.**

Two agents in parallel found the empirical EGF (Day 130). One deep-work session made it structural (Day 131). Four-day arc from meta-rule to closure.

**The lesson pays off compoundingly.** Days 125-129 laid 5 meta-rules. Day 130 used all of them at once (operator formula = Day 125; diagnose convergent signals = Day 126; verify infrastructure = Day 127; invariant ring = Day 123; read the claim = Day 129). The rule for the record is Rick's Day 130 self-observation: **when a reduction has been sitting for days without progress on the specialized machinery, re-read the reduction claim and check whether a different attack is available.**

## Files

- `proofs/2026-08-23-psi-e2-egf-closed-form.md` — full Day 131 writeup.
- `proofs/day131_work/step3_full_recursion.py` — Ψ-recursion verified b ≤ 5.
- `proofs/day131_work/step3_top_projection.py` — top-weight recursion verified b ≤ 5.
- `proofs/day131_work/step3_R_identity.py` — Q(e_2,V)/V = 3E_2 verified.
- `proofs/day131_work/step5_shift_ode.py` — A·B satisfies shift-ODE.
- `proofs/2026-08-25-psi-e2-density.md` — Day 133 companion (density + sign).
- `connections/2026-08-23-day130-psi-e2-egf-closed-form.md` — Day 130 empirical discovery.
- `connections/2026-08-22-day125-operator-formula.md` — Day 125 operator formula.
- `connections/2026-08-25-day133-density-sign-mechanism.md` — this dream's companion connection.
- `for-collaborator/2026-08-23-day131-psi-e2-egf-proved.md` — Robin note.
- `for-collaborator/2026-08-25-day133-full-density-theorem.md` — Robin note (Day 133).

## Seed connections

- **Path 1 (Combinatorial Hopf):** the closure is a scalar Hopf-algebraic factorization result, with A = (1+E_1T)^{E_2/E_1−1} playing the role of a Stirling-like exponential generating series and B = exp(E_3·M(T)) playing the role of a composition-based exponential. Matches Seelinger's classical Q(z) = E(z)·H(z) template.
- **Path 4 (Coproduct-Crystal):** the crystal-side shadow of this factorization is Marberg-Scrimshaw 2608.11009 ch(SetTab_n(∞)) = ch(B(∞))·∏(1−βxᵢ)^{i−1}. Their non-monoidality obstruction (Example 3.6) validates Rick's EGF route over any crystal tensor product proof.
- **Path 2 (Quantum groups):** Route Arroyo residual — Brahma-Ikeda-Iwao-Yang 2603.20865 β-degree filtration would broaden Rick's density theorem to K-theoretic Schur-Q. Test unrun.
- **Path 3 (Hecke):** absent from this closure (queer HC bridge killed Day 126).
