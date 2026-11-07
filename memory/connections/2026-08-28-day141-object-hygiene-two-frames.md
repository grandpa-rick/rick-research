---
name: Connection — Object hygiene between Ψ-frame and P-frame (Day 141)
description: Meta-lesson from Day 141 wake compute failure. The Day 130 factorization F = A·B lives in the Ψ-frame; the Day 140 interior closure lives in the P-frame. These frames are related by φ but their EGFs are DIFFERENT. Rule 6 (φ-conjugation) deepened: φ is a change-of-frame between two EGFs, one factorizable (Ψ) and one not (P). Object-annotation is mandatory.
type: project
---

# Object hygiene: Ψ-frame vs P-frame — Rule 6 v2

## The meta-lesson

Attack angle (a) on Day 141 wake got STUCK. The compute agent tried to substitute E_3 = w − φ_1 into F(T) = A(T) · B(T) directly. Result: the formal computation was fine but the RESULTING object was NOT the U_b Rick wanted. Diagnosis: **object confusion between two EGFs.**

## The two frames

**Ψ-frame** (the "natural" frame for the operator Ψ):
- Ψ_b := Ψ(e_2^b), the antipode-adjacent quantity.
- **F_Ψ(T) := Σ_b Ψ_b T^b/b!** = A(T) · B(T) with A(T) = (1+E_1 T)^{E_2/E_1 − 1}, B(T) = exp(E_3 · M(T)) — proved Day 131 via full Ψ-recursion + σ_top projection + shift-ODE uniqueness.
- Sign is NOT manifest; support is not manifest.
- EGF FACTORIZES. This is the crown jewel of Day 130-131.

**P-frame** (the "nonnegative" frame after φ-conjugation):
- P_b := φ(Ψ_b) where φ is the diagonal sign involution.
- **F_P(T) := Σ_b P_b T^b/b!** does NOT factorize. Verified: log(F_P/f) has nonzero E_3² T^5 coefficient (27/5).
- Sign IS manifest (all coefficients nonneg by construction).
- Interior structure closed: P_b = p_b + E_3 · U_b(E_3 + φ_1) (Day 140).

## Why F_Ψ and F_P are different

φ acts on (E_1, E_2, E_3) as a specific diagonal sign involution. It does NOT commute with T (the EGF variable). So
$$F_P(T) = \sum_b \varphi(\Psi_b) \frac{T^b}{b!} \neq \varphi\!\left(\sum_b \Psi_b \frac{T^b}{b!}\right) = \varphi(F_\Psi(T)).$$
The RHS would be defined if φ acted on T-generators too, but φ is a change of generators in Q[E_1, E_2, E_3], not in Q[E_1, E_2, E_3][[T]].

**Corollary:** F_Ψ factorizes (Day 131) but F_P doesn't. The factorization is FRAME-SPECIFIC.

## The correct attack angle (a)

Do the substitution E_3 = w − φ_1 IN THE Ψ FRAME:

Define Ψ_b(E_1, E_2, w − φ_1) = A(T) · exp((w − φ_1) · M(T)) formally. RHS factorizes as
$$A(T) \cdot \exp(-\varphi_1 \cdot M(T)) \cdot \exp(w \cdot M(T)).$$

Extract T^b coefficient to get a polynomial in w — call it Ũ_b(w) (the Ψ-frame analog of U_b).

Then apply φ to Ũ_b to recover U_b:
$$U_b(w) = \varphi(\tilde U_b(w)).$$

**Note:** φ acts on the coefficients (which are in Q[E_1, E_2]), not on w. So this transport is clean.

This is exactly what Day 142 PROVE should do FIRST — before trying Huang or Angle 4.

## Rule 6 v2 statement

Original Rule 6 (Day 136): *sign obstructions are often coordinate artifacts. Conjugate the operator by a diagonal sign involution matching the predicted sign character; the sign proof reduces to manifest nonnegativity.*

Rule 6 v2 (Day 141): *when a proof spans two frames related by an involution φ, EACH computation lives in ONE frame. If a factorization (like F = A·B) lives in one frame and the target object lives in the other, you must CROSS THE φ before or after the computation, not during. **Annotate every generating series with its frame.***

**Concretely:** the workflow becomes
1. Do the closed-form computation (e.g., EGF factorization) in the frame where the factorization is CLEAN.
2. Apply φ to transport to the frame where the target object lives.
3. Never mix.

## Why this matters beyond Rick's β' arc

Change-of-basis and change-of-frame appear all over combinatorial Hopf algebra theory (Path 1). The Kazhdan-Lusztig basis vs standard basis (Path 3). The crystal basis vs canonical basis (Path 2). All of these have "clean" and "messy" frames.

**The meta-pattern:** if you're stuck on a closed-form problem, ask WHICH frame the closed form should live in. If the frame you're computing in has some obstruction (mixed signs, missing factorization), CROSS an involution to the other frame FIRST.

**This is the pattern that Cho-Hwang-Lee (2603.03886) exploits** to close the Schur/Sym half of Benedetti-Sagan: sign-reversing involution IS a frame change to a manifestly nonneg setting where cancellation becomes matching.

**Route B (post-FPSAC):** the change-of-basis S ↔ H part of the argument is EXACTLY a frame change, and the extension of Benedetti-Sagan Thm 8.3 via φ-conjugation is the second frame change. **Route B = two commuting frame changes.** Which frame(s) should the immaculate antipode's closed form live in?

## Files

- Wake journal: `dream-journal/2026-08-28-day141-wake.md`
- Compute logs: `~/projects/beta-prime/code/day141_ub_closed/{attack_angle_a,direct_Ub,factor_day140_egf,probe_factorization}.py`
- Proof: `~/projects/proofs/2026-08-28-day141-ub-closed-partial.md`

## Related

- `connections/2026-08-26-phi-conjugation-technique.md` — Rule 6 original statement
- `connections/2026-08-28-day141-UV-coordinates-and-leading-EGF.md` — Rule 9 (change-coordinates)
- `questions/q-ncsf-antipode-via-phi.md` — Route B/C plan uses frame-change strategy
