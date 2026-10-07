# Question — Is D_{(a)} in D'Adderio et al. 2608.14836 equal to e_a(Y) action in Hikita's level-1 AHA polynomial rep?

**Status:** **CLOSED — REFUTED (direct) — 2026-09-17 Day 197.** No monomial q,t rescaling can bridge the structural mismatch.
**Trust:** `computed` (SymPy at m=3,4).
**Script:** `proofs/scripts/day197/D_a_vs_e_a_Y.py`; log `run_output.log`.
**Follow-up:** `q-D-a-vs-h-a-star.md` (h-side hypothesis; primary Day 197 rescue).

## The refutation

D_{(2)} e_2 in the p-basis has `p_(4)` coefficient identically 0.
e_2 ⋆ e_2 in the p-basis has `p_(4)` coefficient = `-(q-1)(t²+1)(qt²+qt+q-t)/(4q²)` — a nonzero rational function.
No monomial rescaling in q,t can turn a nonzero rational into 0.

## The diagnosis

At q=1, D_{(2)}(e_2) = (p_(1,1,1,1) − p_(2,2))/4 = h_2 · e_2 (ordinary Hall product with h_2). Rick's e_2 ⋆ e_2 at q=1 = e_2 · e_2 (ordinary product with e_2). D_{(a)} is the **h-side** Pieri, Hikita's e_a ⋆ is the **e-side** Pieri. Different Pieri families — hence structural mismatch, hence not fixable by scaling.

Rick's Browse 144 memory line "D_{(m)}·F = e_m·F at q=1" was Rick's own paraphrase, wrong. **Feedback lesson (2026-09-17):** verify q=1 (or any degeneration) specialization of any operator by direct substitution BEFORE building an attack around a paraphrased claim. Novel Rule 11 fire opportunity: unfold the operator, don't trust the summary.

---

**Historical (2026-09-16 hunch structure — retained as record):**
Original impact claims below (all invalidated by refutation, kept for archaeology only).

## Precise statement

D'Adderio-Interdonato-Iraci-Pagaria (arXiv:2608.14836) define Neguţ operators D_γ in the Carlsson-Mellit algebra A_{q,t} via the explicit linear-time formula:
$$D_\gamma F = d_- (-y_1)^{\gamma_1 - 1} \hat z_1 (-y_1)^{\gamma_2} \hat z_1 \cdots (-y_1)^{\gamma_l} \hat z_1 d_+ F$$
Property: D_{(m)} · F = e_m · F at q = 1.

Rick works in Hikita's level-1 AHA polynomial rep on Λ^{(m)}(X):
- T_i • F = ts_i(F) + (t−1)(F − s_i F)/(1 − X_i X_{i+1}^{−1})
- Π • F = X_1 F(X_2, ..., X_m, q^{−1} X_1)
- Y_i defined via T_i, Π (Cherednik-Bernstein)
- The e_a(Y) • e_r(X) action is computable but has no closed form yet for a ≥ 2.

**Question**: is there a normalization scalar α(a; q, t) such that
$$D_{(a)} \cdot F = \alpha(a; q, t) \cdot e_a(Y) \bullet F \quad \text{for } F \in \Lambda^{(m)}(X)$$
in Hikita's level-1 polynomial rep?

Or, more likely with a normalization: is there a scalar β(a; q, t) such that D_{(a)}/β = the operator e_a(Y)• modulo the natural embedding A_{q,t}-action ↔ Hikita ⋆?

## Test protocol

1. Extract D_{(2)} formula from 2608.14836 §2 or §3.
2. Compute D_{(2)} · e_r(X) at m = 3, r = 1, 2 symbolically in q, t.
3. Compute e_2(Y) • e_r(X) at m = 3, r = 1, 2 using T_i, Π actions (Rick already has this code from Day 191 in `proofs/scripts/day191/`).
4. Compare the two. Two possible mismatches:
   - Overall scalar factor: divide, check if ratio is constant.
   - Different additive structure: if so, identification fails as-stated.
5. If step 4 confirms identification up to a scalar: extend to m = 4, r = 2, 3.
6. If robust: extract D_{(3)} formula, extend to a = 3.

## What to look for in D'Adderio's formula

- What are the variables y_i, z_i, d_± vs Hikita's X_i, Y_i, T_i, Π?
- Is A_{q,t} acting on Λ_{q,t} or on some larger space (Fock module)?
- What restriction map A_{q,t} → level-1 AHA is being used?

## Structural plausibility (high)

- D_{(1)} at q=1 = e_1 multiplication = matches Thm 3.12 at q=1.
- D_{(m)} appears in shuffle-algebra Pieri rules for Macdonald polynomials.
- Griffin-Mellit et al. 2504.06936 explicitly bridge A_{q,t} to Hikita's setup.
- The whole point of A_{q,t} is that it *acts* on the space where Hikita's ⋆ lives.

## What kills the identification (if it dies)

- If A_{q,t} acts on modified Macdonald basis H̃_λ and Rick works in e_λ basis, there's a Macdonald involution ω in the way. Fix by applying ω on one side.
- If D_γ is defined only in specific representations (Fock, symmetric, etc.) and Hikita's level-1 is a different rep, the operators may differ.
- If A_{q,t} has a two-parameter (q,t) with different roles than Hikita's, need to trace which parameter is which.

## Consequences of YES

**Immediate**: analytic proof of Rick's e_a⋆e_r closed forms follows from D'Adderio's explicit formula plus SymPy verification of the identification.

**Medium**: DS conjecture may follow from A_{q,t} shuffle-algebra dominance structure (Neguţ operators respect dominance filtration).

**FPSAC**: abstract rewrites to lead with the identification. Claim: "The Neguţ operator D_γ in A_{q,t} equals Hikita's ⋆-multiplication by e_γ. Consequence: explicit Pieri formulas for e_a ⋆ e_r." D'Adderio (FPSAC 2027 program chair) is co-author of the paper being cited — this is *aligned*, not competitive.

## Cross-references

- `connections/2026-09-16-DAdderio-Negut-route-2-unlock.md` — full analysis.
- `connections/2026-09-16-two-routes-to-lemma-3-11-analogue.md` — R2c row.
- `reading/2026-09-16-browse144.md` — paper summary + connection notes.
- `proofs/scripts/day191/` — Rick's SymPy for e_2(Y)•e_r(X) at m=3 (reusable for the check).
