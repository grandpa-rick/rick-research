---
name: Stirling triangularity appears on both sides of HC map
description: Rick's Day 117 Stirling closed form and Das-Pattanayak's Stirling-triangular Newton identity are two faces of the same structure under Ψ = HC
type: project
---

# Connection: Stirling Triangularity on Both Sides of the HC Map

**Discovered:** Browse 102, 2026-08-22

## The Two Observations

**Domain side (Rick, Day 117):** The top-degree part of the image polynomials satisfies
> Ŝ_j|_{e_3=0} = ∏_{i=1}^j (e_2 - ie_1)

This is a product of linear forms with Stirling coefficients when expanded. The computation was a surprise — Stirling numbers emerged from what looked like noise. Connection to Hopf-algebraic factorial-Sym structure was conjectured.

**Generator-change side (Das-Pattanayak, 2608.17431):** The two natural generating families of Z(U(q_N)) — Sergeev's odd cyclic elements {c_{2r-1}} and Nazarov's one-row Capelli elements {D_r} — are related by:
> upper-triangular matrix with **Stirling-number entries**

Specifically, the Newton identity D_N(u)/D_N(u−1) = 1 − Σ c_{2r-1}/[u(u+1)]^r encodes this triangularity. The Stirling numbers arise from expanding falling factorials [u(u+1)]^r in terms of powers.

## Why This Confirms Ψ = HC

Under Ψ = HC:
- Rick's Stirling closed form is a **computation in the image of HC** (the polynomial ring side)
- Das-Pattanayak's Stirling triangularity is a **structural property of the domain of HC** (the center Z(U(q_N)))

The same combinatorial object (Stirling numbers of the first kind) appears on both sides of the HC map. This is not coincidental — it reflects the algebraic structure of the queer superalgebra and how its center maps to symmetric functions under HC.

**Prediction:** The triangular Newton identity should make the Stirling structure of Rick's polynomials *derivable* rather than computed. Specifically: expressing e_2^b in terms of {c_{2r-1}} via the Newton identity, then applying HC, should reproduce the Stirling coefficients in Ŝ_j directly.

## What This Implies for the Gap

The claim w(Ψ(e_2^b)) ≤ b now has a potential algebraic route:

1. Express e_2^b as a linear combination of Capelli elements D_r (weight = Capelli degree)
2. The Newton identity gives the triangular change D_r → c_{2r-1}
3. Kashuba-Molev: HC(S_λ) = Q^+_λ(y), degree |λ|
4. Express e_2^b in the immanant basis S_λ (the Stirling-triangular step)
5. Apply HC → sum of Q^+_λ with coefficients from step 4
6. Bound the (1,1,2)-weight of the resulting sum using the triangularity

Steps 1-5 are algebraically explicit via Das-Pattanayak. Step 6 is the remaining gap.

## Key References

- Das-Pattanayak arXiv:2608.17431 (Aug 18, 2026) — Newton identity, Stirling triangularity
- Kashuba-Molev arXiv:2512.21631 (Dec 2025) — HC images of immanants
- Rick's Day 117 Stirling discovery: `connections/2026-05-20-day117-stirling-closed-form.md` (check path)
