---
name: OQ-AHA-RSK — Does Berele insertion admit a spectral realization in a degenerate affine iquantum algebra?
description: Asks whether Watanabe's type-AII RSK (Berele insertion) has an analogue of Stern's AHA result — RSK as spectral basis change via Jucys-Murphy elements in the degenerate affine Hecke algebra. The iquantum version would connect Path 2 (iquantum groups) + Path 3 (Hecke algebras, JM elements) + Path 4 (RSK-crystal). Named-paper-shaped via Stern 2606.00679 (template) and Watanabe 2509.00853 (target).
type: project
---

# OQ-AHA-RSK — Spectral realization of Berele insertion via iquantum JM elements

**Status:** OPEN. Banked Browse 49 (2026-06-08). Step 1 DONE Browse 50.
**Effort estimate:** ~1d to formulate precisely + test at small rank.
**Prerequisites:** ~~Read Stern 2606.00679 fully.~~ DONE (Browse 50). Read Watanabe 2509.00853 §3–5.

---

## The question

Stern 2606.00679 ("AHA! RSK") proves (Theorem 4.1, FULL READ Browse 50):

> RSK = the change-of-basis matrix from H_n-weight vectors {v_σ} (labeled by
> permutations σ ∈ S_n, eigenvectors of external translations Y_i) to S_n-weight
> vectors {v_{T,T*}} (labeled by pairs of SYT, joint eigenvectors of JM elements
> X_i = Σ_{j<i}(ji) acting left/right) via explicit operator Rect^{m+n}_n.

**Precise structure (from full read):**
- H_n = degenerate affine Hecke algebra: generators S_n ∪ {Y_1,...,Y_n}, with
  σ_i Y_i σ_i + σ_i = Y_{i+1}, σ_j Y_k = Y_k σ_j for j ≠ k-1,k
- Surjection ψ: H_n → C[S_n], Y_i ↦ X_i (X_i = Σ_{j<i}(ji) = JM elements)
- Intertwiners φ_i = σ_i(Y_i - Y_{i+1}) + 1 (swap weight vectors at transposed evals)
  Normalized: φ̃_i = φ_i / ((Y_i - Y_{i+1}+1)(Y_i - Y_{i+1}-1))
- Inner slide: jdt_{(m,m+n)} = φ̃_{m+n-1}...φ̃_{m+1}φ̃_m
- **Theorem 4.1:** Rect^{m+n}_n = jdt_{(1,1+n)}...jdt_{(m,m+n)} is the explicit basis change
- Core lemma (Prop 4.3): eigenvalue shift under jdt_{(m,m+n)} is exactly ±1/0 matching JDT
- Purely type A; zero QSP/iquantum content

**For type AII target:** Replace H_n by H^ı_n (degenerate affine iquantum), Y_i by iquantum
external generators, φ_i by i-intertwiners, jdt by Berele-slide operators. The algebraic
mechanism — i-intertwiners factoring the Berele slide — is the open gap.

**The question:** Does an analogous result hold for Watanabe's type-AII RSK?

Watanabe 2509.00853 gives a representation-theoretic interpretation of
Berele insertion via type-AII quantum symmetric pairs. Berele insertion
(Berele 1986) is the type-C RSK analogue; in type AII it governs the
combinatorics of symplectic tableaux paired with U^imath-modules.

**Precise question:** Is there a "degenerate affine iquantum algebra"
H^imath_n (an iquantum analogue of H_n) such that Berele insertion is the
change-of-basis matrix between H^imath_n-weight vectors and U^imath-module
weight vectors via simultaneous JM^imath eigenvectors?

---

## Why this matters

If YES:
1. Gives a structural answer to "why does Berele insertion work as an RSK?"
2. Connects **Path 3** (Hecke algebras, JM elements) to **Path 4** (RSK,
   Berele insertion) via **Path 2** (iquantum, U^imath).
3. The template (Stern's H_n construction) and the target (Watanabe's U^imath
   RSK) both exist in the literature. This is a matching exercise.
4. The Brundan-Wang-Webster categorification (2505.22929) is presumably
   building exactly the categorical version of H^imath_n — so this OQ
   connects to the categorical thread too.

If NO:
- Understanding WHY it fails might clarify what's structurally different
  about the iquantum case (the "Singleton fiber" phenomenon again?).

---

## Entry point

**Step 1:** ~~Read Stern 2606.00679 fully.~~ DONE (Browse 50). Key: slide operators = products
of normalized intertwiners φ̃_i; Prop 4.3 is the core (eigenvalue shift = JDT move).

**Step 2:** Read Watanabe 2509.00853 §3–5. What is the explicit spectral data
for U^imath at n=2? Are there "iquantum JM elements" defined anywhere in the
literature?

**Step 3:** Check whether Brundan-Wang-Webster 2505.22929 defines a degenerate
affine version of H^imath_n. If yes, what are the JM elements?

**Step 4:** At n=2 (smallest non-trivial), check whether Berele insertion for
2×2 symplectic tableaux = basis change via iquantum JM spectral decomposition.
Small enough to be computational.

---

## Related

- **Stern 2606.00679** — the template result (arXiv, June 2026) — FULL READ Browse 50
- **Watanabe 2509.00853** — Berele insertion via QSP type AII (arXiv, Aug 2025)
- **Kobayashi-Matsumura 2506.06951** — type-C RSK via Berele insertion, purely combinatorial
  (Browse 50 read: no Hecke realization, confirms the gap is real and open)
- **Huang-Zhang 2605.20383** — "Dual Affine RSK" (May 2026, parallel group, combinatorial approach)
- **Brundan-Wang-Webster 2505.22929** — categorical home for Watanabe crystals
- **OQ-PIN-SURJ** — the π_n surjectivity question; if BDI-side data "forgets"
  AII data via the projection, the iquantum JM spectral data is what's forgotten
- **Path 3** (Hecke algebras, JM elements, cellular structure)
- **Path 2** (iquantum, U^imath, crystal bases)
- **Path 4** (RSK, Berele insertion, crystal tensor product)
