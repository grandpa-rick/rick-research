# The QC defect g is bar-invariant (q ↦ 1/q). g−1 has simple zeros at q=0 and at q=∞, and the q=0/q=∞ dichotomy is their shadow

Day 244 dream, 2026-10-17. **Grade: HUNCH.** The algebra below is exact and was checked by hand tonight; the link to the dichotomy is not proved.
Registry: `q488-qinf-dichotomy` (hunch, unchanged), `q488-lemma-qc` (proved), `q488-motegi-correction-is-g` (computed).

## The two lines of algebra
Write g = (1−q)²/((1−qx²)(1−qx⁻²)), with x = w_a, which is the Lemma QC twist on H_ab (`proofs/2026-10-18-q488-converse-order-q1.md` §3).
- **Bar invariance:** (q−x²)(q−x⁻²) = (1−qx²)(1−qx⁻²), so **g(1/q) = g(q)** exactly.
- **Two zeros of the defect:** g − 1 = q·γ / ((1−qx²)(1−qx⁻²)), where γ = (x−x⁻¹)².
  - At q=0, g−1 = γq + O(q²). This is Day 243 Cor 4, ∂_q g(0) = γ.
  - At q=∞, g−1 = γq⁻¹ + O(q⁻²). This is the mirror, and it is new tonight.
- γ = −(1−x²)(1−x⁻²) is (minus) the product of the two long-root GKM weights. That is the same shape as the Day 244 global correction, Koncki − Motegi = q(1−q)(1−w₁⁻²)(1−w₂⁻²).

## Why it matters for Q488
- Thm 6 (aggregate converse, proved) has the residue ∝ (g²−g)·φφ = g(g−1)·φφ.
  - So every long-root residue carries the factor g−1. That factor is exactly first order at both ends, and it is the same γ at both ends.
  - This would explain why the data shows first-order residues at q=0 *or* at q=∞: N=4 gives 127/127 at ∞, and N=5 gives 12/12 q¹-failures first order at ∞.
  - The "or" must come from the Ã-side factor, i.e. whether φφ survives at that end. It cannot come from g.
- **Strategy shift for the q=∞ mirror of Thm 7** (the open item in `questions/q-q488-converse.md`):
  - Don't do a tropical min-plus analysis from scratch. Transport the q=0 proof by q ↦ 1/q.
  - g is invariant under that map, so the only asymmetry is Ã's normalisation.
  - With y = −q, the map q ↦ 1/q is y ↦ 1/y. On motivic Chern classes that is (recalled, NOT checked first-hand) AMSS 1902.10101's Serre-duality / dual-MC statement: it exchanges mC_y and a dual family at y⁻¹, up to a factor (−y)^{dim} and w ↦ w⁻¹.
  - Prediction: φ^∞_I(M) = (−1)^{codim} · monomial · (φ⁰ of the dual/opposite family)(w⁻¹).
  - The non-row×column exponents of φ^∞ (Day 243 `phiinf.py`: 6, 6, 4, 4) would then be the dual Euler-class ratio, not a tropical mystery.
- **Cheap test (PROVE fallback):**
  - At N=3, compare φ^∞ (`work-in-progress/scripts/day243/q488c/phiinf.py`) with the w ↦ w⁻¹ image of φ⁰ times the ratio of repelling to attracting Euler classes.
  - Negative control: the same comparison without the inversion w ↦ w⁻¹. It must fail (the control has to break, not relabel).
  - Owner gate: read AMSS's duality theorem first-hand before using it.

## Seed connection
- **Path 3.** q ↦ q⁻¹ is the Kazhdan–Lusztig bar involution of the Hecke algebra. Motegi's parameter is the Demazure–Lusztig parameter y = −q, so the defect that separates his basis from the honest geometric one is a **bar-invariant** element.
  - Q488's two regimes are then the two 0-Hecke ends (π_i at q=0 vs π_i − 1 at q=∞; O vs ideal sheaves). The Day 243 dream proposed exactly this, and tonight supplies the mechanism.
- **Seed Q4.** g(0) = 1 is *why* the q=0 Motegi basis is honest (GQ, Ikeda–Naruse 1112.5223) while every q ≠ 0 basis is not. The q=0 limit is the unique finite point where the normalisation defect dies.
  - g(∞) = 1 gives the second such point. So "the q=0 limit of a Hecke-deformed basis is a K-theoretic CHA basis" (Lam–Pylyavskyy 0705.2189) should have a q=∞ twin, the dual (ideal-sheaf) K-basis.

## Killed in-dream (same-session recheck)
- I briefly floated that Motegi's Ã is the twisted mC at a *different slope on long roots*: α = 2⌈λ⌉−⌈2λ⌉ is the long/short ceiling discrepancy, which would make g a wall-crossing factor.
- **Dead by Prop K** (`proofs/2026-10-17-koncki-LG24-motegi-correction.md` §2): no honest K-class matches Motegi's ∅-column at more than 3 of 4 points, and every slope's twisted mC is honest. So g is not a wall-crossing between honest twists.
