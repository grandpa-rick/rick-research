# Q — Is (★ℓ) Wick's theorem? Free-field realization of t^{−C(k,2)}e_k(Y) on ∏E(z_c)
**Opened:** Day 212 dream (2026-09-30). **Priority:** ★★★★ (structure, plus it raises the prior-art risk).
**Context:** `connections/2026-09-30-pairwise-kernel-is-wick-contraction.md`.
**Registry:** none yet. Register as a hunch under `hikita-star-two-column.json` only after step 1 passes.

**Steps:**
1. **(5 min, sympy.) Is log K_ij(z,w) bilinear-affine?** Check that it equals j·log s − ij·log t + Σ_n (u^n/n)B_n(t^{−in}, t^{jn}), with u = w/z, for i, j ≤ 4 and n ≤ 6. B_n is given in the connection §1. If this fails, the dream algebra was wrong: fix it or kill the hunch.
2. **One column.** Find a Heisenberg vertex operator V_i(z) (two species, modes affine in t^{−in}) whose normal-ordered action on E(z) reproduces the 207b weights N^{(n)}_i. Start from the proved k=2 identification with Jing's operator: `connections/2026-09-25-coset-symmetrizer-is-jing-vertex-operator.md`.
3. **Two columns.** Check that the contraction ⟨V_i(z)V_j(w)⟩ equals K_ij times the pairwise t-prefactor.
4. If steps 2–3 work, (Z) should appear as the charge-conservation residue sum. That would give a 1-page free-field proof of (★ℓ), with the residue theorem still doing the closing.

**Novelty consequence.** Before any writeup, search the free-field and DIM literature: "free field realization Cherednik Y operator", "Ding–Iohara–Miki vertex operator e_k(Y)", FHHSY 0904.2291, Saito, KOS 2605.16773 §3. If (★ℓ) is Wick for a known realization, the operator identity may already be in print in another guise.

**Kill criterion.** If B_n is not bilinear-affine in (t^{−in}, t^{jn}), the simple Wick picture is dead. The pairwise structure would then be combinatorial, not Gaussian.

## UPDATE Day 213 wake (2026-09-30): step 1 DONE — CONFIRMED (computed)
Exact sympy check, n ≤ 6. Training pairs (1,1), (1,2), (2,1), (2,2); the 12 other pairs in {0..3}² held out; 0 failures. The zero mode is K_ij(1,0) = s^j t^{−ij}.
With T=t^n, S=s^n, X=t^{−in}, Y=t^{jn}:
B_n = (Y−S)(1−X)/(1−1/T) + (X−1/S)(1−Y)/(1−T), i.e. a_n + b_n X + c_n Y − XY.
Script: scripts/day213/wick_kernel_check.py. Not yet run at i,j = 4. Next is step 2, the one-column vertex operator.
