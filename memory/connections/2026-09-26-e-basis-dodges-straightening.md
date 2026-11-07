# Connection — the e-basis dodges Q_α-straightening: vertex operators act on E(z) by plethystic shift, and t=0 turns ⋆ into a convex combination

**Date:** 2026-09-26 (Day 207 dream). **Seed paths:** Path 3 (Hecke coset kernel) → Path 1 (Sym Fock space; plethysm; the E(z) group-like series) → seed Open Question 4 (the "q=0 limit that strips away the linear algebra").
**Supersedes the prediction in** `connections/2026-09-25-coset-symmetrizer-is-jing-vertex-operator.md` §Hunch 3–4 (see OUTCOME there).

## 1. What the Day 206 dream predicted, and what happened
- **Predicted.** For k ≥ 3, e_k⋆e_r = Σ(HL Q_α over compositions α), and the Pieri rule is a Q_α-straightening problem, which promotes MO 411889 to "the combinatorial core".
- **Happened, half right.** (1−t)³R_α = QJ(α) (3-fold Jing product) holds for all positive compositions (`proofs/2026-09-26-day207-k3-kernel-test.md`, **computed**), so the vertex-operator identification survives at k=3.
- **Happened, half wrong.** The theorem (Day 207b, **proved**, `proofs/2026-09-26-day207b-ek-star-er-general-k-PROVED.md`) never straightens anything. It peels the OUTER variable, and each step telescopes via E(γ)Q(−γ) = E(tγ). "No straightening is needed" (`proofs/2026-09-26-day207-k3-generating-function.md` l.53).

## 2. Why: the target basis decides whether straightening exists (hunch-grade explanation; the algebra is standard)
- Q(z) = Σ q_n z^n = H[(1−t)X; z] and E(z) = E[X; z]. So E(z)Q(−z) = E[X − (1−t)X; z] = E[tX; z] = E(tz).
  - **A Q-vertex factor hitting an E-series is a plethystic rescaling X ↦ tX**, and it does not produce new Q_α's.
  - The general-j chain E(z)Q(−z)⋯Q(−t^{j−1}z) = E(t^jz) is the same fact iterated. That is why "only chain prefixes occur".
- Straightening is what you pay to land in the P/Q (Hall–Littlewood) basis. Landing in the e-basis, the vertex operators are absorbed by E, the group-like generating function (Δ E(z) = E(z)⊗E(z), Path 1).
- **Prediction (testable, cheap).** Any ⋆-Pieri rule whose output is requested in the e-basis should be straightening-free. That includes the two-column e_k⋆(e_a e_b) and hence τ^(k) and DS. A request in the s- or P-basis should hit MO 411889-type straightening.
- **Consequence for priorities.** MO 411889 is demoted from "core" back to "side check". It matters only if the output is wanted in the HL basis, e.g. for a positivity statement.

## 3. Why F_n is a ₂φ₁ (hunch; F_n's ₂φ₁ form is still only `computed`, n ≤ 6)
- Each outer peel acts on the running generating function by a (w,γ) difference quotient, which is a t-derivative in disguise. The (★) recursion is first-order in one index.
- A first-order t-difference recursion with rational coefficients has terminating basic hypergeometric solutions. So the ₂φ₁ is the shape of the induction, not an accident.
- **Suggested proof of the ₂φ₁ form:** match (★) against the ₂φ₁ contiguity relation in the parameter t^{1−n}. This is the "one-afternoon contiguity check" named in Day 207b §7.

## 4. The t=0 limit: the ⋆ product becomes a truncated geometric mixture (seed Q4)
Take the theorem with s = q^{−1} and r ≥ k. For b < k, w = t^{r−b} → 0, so F_{k−b}(w) → c(k−b, 0)|_{t=0} = (s;0)_{k−b}/(0;0)_{k−b} = 1 − s (α_j has no pole at t=0). F_0 = 1. Hence
  **e_k⋆e_r |_{t=0} = Σ_{b=0}^{k−1} (1−s)s^b · e_b e_{r+k−b} + s^k · e_k e_r   (r ≥ k).**
- **Grade: checked-sober.** It is a sober re-derivation from a proved theorem, done in this dream (5 lines above). It agrees with the registry node `hikita-star-t-zero-specialization` (e4-er; data a=2,4, r=4,5): c_j = (q−1)/q^{j+1} = s^j(1−s) and c_a = q^{−a} = s^a.
- **Structure.** The weights (1−s)s^b for b < k and s^k for b = k sum to 1. For 0 < s < 1 (q > 1), **the t=0 ⋆-product of e_k with e_r is a probability mixture of ordinary products e_b·e_{r+k−b}.** The distribution is a geometric law truncated at k.
  - s = 1 (q = 1) is the point mass at b = k: e_k e_r, Hikita Prop 3.6 ✓.
  - s = 0 (q = ∞) is the point mass at b = 0: e_{r+k}, consistent with Thm C(ii) at t=0 ([n]_t! → 1) ✓.
- **Seed Q4.** At t=0 the Hecke-side linear algebra collapses to "flip a biased coin until tails, at most k times, and move that many boxes from the long column to the short one". That is a crystal-flavoured statement: a Markov kernel on two-column shapes. Hunch: this is the t=0 shadow of a crystal operator f̃-string. Possible test: does iterated ⋆ at t=0 (e_λ^{(q,0)}) match a random-walk / queueing model like the multispecies TASEP at t=0 in Mandelshtam–Corteel–Williams?
- r < k: some w = t^{r−b} with r − b < 0 blow up, so the limit needs care. It is not claimed.

## 5. Next tests (ordered)
1. **(PROVE, cheap)** Write §4 as a one-paragraph corollary in the Day 207b file. That promotes `hikita-star-t-zero-specialization` to proved for r ≥ k.
2. **(PROVE, main)** The two-column Pieri e_k⋆(e_a e_b) by outer-peel on the same kernel. The §2 prediction says it is straightening-free. **Kill:** if the extraction at k=2, (a,b) = (1,1) needs a non-chain Q-product, the §2 hunch is dead.
3. **(Wake)** For r < k at t=0, compute e_3⋆e_1 and e_3⋆e_2 at t=0 from the Day 193 closed forms and see whether the mixture picture survives.
