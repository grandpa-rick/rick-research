# Connection (Day 224 dream): the lead is exp(connected), it is symmetric under the contragredient, and the class-4 wall is a coproduct

**Seed paths:** Path 1 (exponential formula / primitives / Hall pairing is a Hopf pairing) × Path 2 (dual representation of GL_N twisted by det^N) × Path 4 (coproduct = splitting the alphabet).
**Inputs (all in `proofs/2026-10-06-day224-Gprime-second-order.md`, proved per its §9):** Thm 2.1 Box Complement, Cor 2.2 Column Lemma, Cor 2.3, Thm 6.1 block multiplicativity, §8 class table, escalation `for-collaborator/2026-10-05-day224-escalation-class4.md`.
**Status:** §1 and §2 are readings of proved statements; they add no new claims. §3 is an UNTESTED attack plan for class 4.

## 1. Thm 6.1 + Thm G + primitive pairing = the moment–cumulant (exponential) formula
- Thm 6.1: [(s−1)^{ℓ−κ}]c_{λμ} = Σ_{π ⊢ [ℓ], |π|=κ} Σ_{(ν^C)} ∏_C ConnLead(λ_C, ν^C).
  This is "moments = Σ over set partitions of products of cumulants", read at the leading (s−1)-order.
- Day 223 crown (`connections/2026-10-05-lead-is-a-primitive-pairing.md`) says the κ=1, μ=(n) connected piece is pairing with the primitive p_n, i.e. a Hopf logarithm.
  Day 222 crown (`connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md`) says its value is a cumulant of e_k ↦ t^{C(k,2)}.
- **Together:** the whole lead structure is a *character on the Hopf monoid of set partitions* (Aguiar–Mahajan Π). That character is exp of its connected part. The
  ⋆-specific content lives ONLY in the connected leads. Thm 6.1 is the formal half, Mayer-type with low novelty; say so in FPSAC.
- Consequence for G′: the general-μ problem is exactly "compute the infinitesimal character on connected (κ=1) pairs". Day 224 closed that for μ=(n) (Thm G),
  (n−1,1) (Thm 4.2), λ∋1 (Thm 5.2), and their orbits (§2). The rest is class 4.

## 2. Box Complement is the contragredient; the class table is an orbit table
- In N variables, x ↦ 1/x on Λ_N[e_N^{±1}] is the dual-representation involution of R(GL_N): V_λ* ⊗ det^N = V_{N^ℓ−λ}.
  Thm 2.1 says ⋆ commutes with this involution up to the unit s^{N·C(ℓ,2)−(ℓ−1)|λ|}. Cor 2.2 (Column Lemma) is ⊗det.
  So **⋆ structure constants are invariant (up to s-units) under the infinite dihedral group D_∞ = ⟨⊗det, dual⊗det^N⟩ acting on ℓ-row boxes.**
  Seed reading: the antipode of the representation Hopf algebra (dual rep) survives the ⋆ deformation, with grading defect only.
- Leads are units-free, so **Lead is a D_∞-orbit invariant** (Cor 2.3). The §8 classes are orbit data:
  - class 1 = orbits containing a coarsening (Thm G);
  - class 2 = orbits containing (n−1,1);
  - class 3 = orbits containing a λ with a part 1;
  - **class 4 = orbits containing none of these.** Smallest: (3,3,3)→(7,2). 16 pairs n≤12 (`classify.py`).
- Cheap sanity check this predicts and the PROVE already saw: mirror consistency 10/10 (n≤10).
- Novelty: likely the (N)-shadow of Macdonald VI complementation P_ν(x^{−1})e_N^ℓ = P_{ν^c}. The direct (N)-free proof is ours-as-checked. Check Hikita 2503.23597 / DFK 1505.01657 for an inversion symmetry of E_k before claiming it.

## 3. UNTESTED attack on class 4: the 2-point functional is the 1-point functional on Δ
The escalation's missing datum is f ↦ ⟨T_af, p_xp_y⟩ (Hall pairing), with a ≥ 2. Day 223's lesson was "p is primitive", so use it again:
- The Hall pairing is a Hopf pairing: ⟨G, p_xp_y⟩ = ⟨ΔG, p_x⊗p_y⟩.
- ⟨H, p_x⟩ = (−1)^{x−1}[e_x]H (Day 223 §1).
- So **⟨G, p_xp_y⟩ = (−1)^{x+y}·(lin_e ⊗ lin_e) of the bidegree-(x,y) piece of G(X+Y).** The 2-point functional is the
  1-point functional (Day 223 Thm 1.5, a principal specialization) applied to each tensor leg of the coproduct.
- For G = T_af: the symmetrizer over X⊔Y splits as A = A_X ⊔ A_Y. c_A = c_{A_X}·c_{A_Y}·(cross factor ∏(x_i − t y_j)/(x_i − y_j) over A_X × (Y∖A_Y), and symmetrically).
  The cross factor is the "interaction". **Prediction to test first:** at a = 1 this must reproduce the known (1−t)[x][y]f(1) (`twopoint.log`).
  If the cross factor collapses under lin_e⊗lin_e (each variable has degree ≤ 1, so only its linear Taylor piece survives), the result is a
  "two-string principal specialization". That is exactly the form the escalation note asked for.
- Fallback, if the cross factor does not collapse: the HL Murnaghan–Nakayama rule (Macdonald III.7, Morris 1963), read first-hand.
- Kill: the a = 2 value fails to match the engine on (3,3,3)→(7,2). Its lead is 2t¹³+3t¹²+3t¹¹+6t¹⁰+6t⁹+6t⁸+9t⁷+6t⁶+3t⁵+9t⁴+6t³+3t+4.

## Why this matters for the seed
Path 4's core question asks why the coproduct is simultaneously restriction and the tensor rule. Here the coproduct is ALSO the tool that turns
a 2-cycle character (Green polynomial / MN data, Path 3) into two 1-cycle characters (q-dimensions, Path 2). If §3 works, it is the same
mechanism as "branching = coproduct", applied to the parabolic HL symmetrizer.
