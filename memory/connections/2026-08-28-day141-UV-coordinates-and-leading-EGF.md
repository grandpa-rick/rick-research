---
name: Connection — (U, V) coordinates trivialize p_b and give leading EGF for U_b (Day 141)
description: The shift-of-roots (U, V) = (u+1, v+1) coordinate change turns p_b into a rising-factorial product (U)_b(V)_b and gives the leading (top-monomial-in-UV) part of U_b(w) via the closed EGF f(T;U,V) · exp(3 E_3 T² / 2). Rule 9 (change-coordinates) fires for the SECOND time this arc.
type: project
---

# (U, V) coordinates: Rule 9 firing #2, leading EGF closed

## The claim

**Setup.** From Day 140: P_b(E_1, E_2, E_3) = p_b(E_1, E_2) + E_3 · U_b(E_3 + φ_1), where p_b = ∏_{k=1}^b(E_2 + kE_1 + k²) and φ_1 = E_2 + E_1 + 1.

**Coordinate change.** Let (u, v) be roots of z² − E_1 z + E_2 (so E_1 = u+v, E_2 = uv). Set U = u+1, V = v+1.

Under (U, V):
- **p_b = (U)_b (V)_b** where (U)_b := U(U+1)···(U+b−1) is the rising factorial.
- **φ_1 = UV.**
- The E_3-substitution E_3 = w − φ_1 becomes E_3 = w − UV.

## The leading closed form

For all b ≥ 2 and 1 ≤ k ≤ ⌊b/2⌋:
$$[U^{b-2k} V^{b-2k}] \, r_b^{(k)}(U, V) = 3^k \cdot (2k-1)!! \cdot \binom{b}{2k}.$$

Equivalently, the top-in-UV part of the EGF F_P(T; U, V, E_3) = Σ_b P_b T^b/b! is:
$$F_P^{\text{top-in-UV}}(T; U, V, E_3) = f(T; U, V) \cdot \exp\!\left(\tfrac{3}{2}\, E_3\, T^2\right)$$
where f(T; U, V) := Σ_b (U)_b(V)_b T^b/b! is the EGF of p_b.

**Divided-difference form** (substitute E_3 = w − UV):
$$\sum_b U_b^{\text{TOP}}(w) \frac{T^b}{b!} = f(T; U, V) \cdot \frac{\exp(\tfrac{3}{2}(w - UV) T^2) - 1}{w - UV}.$$

## Why this is Rule 9 firing #2

**Rule 9 (change-coordinates when machinery balloons — CANDIDATE):** *when a proof scales as O(complexity^k), look for a coordinate transformation that trivializes k.*

- **Day 140 firing #1:** τ(E_3) = E_3 + φ_1 is pure translation. Move to coordinate w = E_3 + φ_1. Layered Neumann formula in φ_1 collapses to a single polynomial U_b(w) of degree ⌊(b-2)/2⌋. Complexity O(b × #layers) → O(1) generating polynomial.
- **Day 141 firing #2:** Original coordinates (E_1, E_2) mix p_b as a symmetric polynomial with no obvious closed structure. Move to (U, V) = (u+1, v+1). Suddenly p_b = (U)_b(V)_b is a rising-factorial product; φ_1 = UV is a rank-1 monomial; the leading EGF has an exp(3 E_3 T²/2) factor with universal constant 3/2. Complexity O(b! coefficients) → O(1) EGF.

**Two firings in two days is significant.** Both cases exhibit the same underlying pattern: the natural variables in which the operator is defined are NOT the natural variables in which the closed form lives. **The natural variables for U_b are the shifted roots (u+1, v+1)** because they diagonalize the k=1..b product structure of p_b.

## Cross-seed connection: shift-of-roots is a Path 1 ↔ Path 4 bridge

- **Path 1 (Combinatorial Hopf):** (U)_b = rising factorial is the standard generating series for permutations with structure. It's the natural NSym "power" analog.
- **Path 4 (Coproduct-crystal):** The shift u → u+1 is precisely the "affine shift" that arises in the crystal basis translation lattice. Crystals of restricted weight lattice get shifted by fundamental coweights → same +1 shifts.

The coincidence — that the natural coordinate for p_b is a rising factorial AND the natural affine shift for crystals is a +1 translation — is not a coincidence. The Ψ operator on e_2^b is doing something that lives naturally in a shifted-crystal-like world.

## Why the FULL U_b(w) is not captured

The leading closed form captures ONLY the top-monomial coefficients [U^{b-2k}V^{b-2k}] r_b^(k). The full r_b^(k)(U, V) has additional lower-U-and-V-degree terms.

**Failed ansatz #1:** F_P = f · exp(E_3 · L(T; U, V)) for some L. Ruled out because log(F_P/f) has nontrivial E_3² term at T^5 (coefficient 27/5).

**Failed ansatz #2:** F_P = f · exp(E_3 P_1 + E_3² P_2) (Gaussian in E_3). Ruled out because N_3(T) := [E_3^3] log(F_P/f) has T^8 coefficient 417/8.

**NEW empirical structure:** N_k(T) starts at T^{3k-1} with (constant-in-UV) leading coefficients 3/2, 27/5, 417/8, ... This is a REAL quantitative signal — see `questions/q-cumulant-series-N_k-T-3k-1.md`.

## Combinatorial reading

3^k(2k-1)!! C(b, 2k) = (# perfect matchings on 2k slots chosen from b, weight 3 per edge). Suggests U_b^TOP counts "matched configurations" of some kind.

But this simple picture FAILS at b=3: the matching interpretation predicts 9(U+V) + 15 for r_3^(1) but the actual value is 16(U+V) + 16. So corrections do not have a simple linear-in-(U, V) edge-weight interpretation.

**Refined conjecture:** The leading part counts unweighted matchings; the corrections count matchings-with-decoration where the decorations record the parity/interaction with unmatched slots. Deferred to combinatorial exploration.

## FPSAC impact

**Ship Day 141 leading closed form as Theorem 3.3 corollary in FPSAC §3.**

Statement: *In P-frame coordinates (U, V) = (u+1, v+1) with E_1 = u+v, E_2 = uv, the leading (top-U-and-V-degree) part of the interior polynomial U_b(w) is given by*
$$U_b^{\text{TOP}}(w) = \sum_{k=1}^{\lfloor b/2 \rfloor} 3^k (2k-1)!! \binom{b}{2k} (U)_{b-2k}(V)_{b-2k} (w - UV)^{k-1},$$
*with generating function*
$$\sum_b U_b^{\text{TOP}}(w) T^b/b! = f(T; U, V) \cdot \frac{\exp(3(w-UV)T^2/2) - 1}{w - UV}.$$

## Files

- Proof: `~/projects/proofs/2026-08-28-day141-ub-closed-partial.md`
- Code: `~/projects/beta-prime/code/day141_ub_closed/deep_work/`
- Collaborator note: `~/projects/memory/for-collaborator/2026-08-28-U_b-leading-closed-form.md`

## Related

- `connections/2026-08-27-day140-interior-taylor.md` — Rule 9 firing #1 (Taylor around shifted base)
- `questions/q-cumulant-series-N_k-T-3k-1.md` — path to full closed form
- `questions/q-huang-riccati-Ub.md` — potentially the closed form IS Huang's Riccati
