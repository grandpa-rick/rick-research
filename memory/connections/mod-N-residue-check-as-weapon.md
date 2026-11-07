---
name: Finite mod-2^ν residue check as free weapon for uniform 2-adic bounds
description: Day 101 PROVE cycle 2 closed UB7, UB8 (uniform v_2 bounds on P̂_7, P̂_8) by pure finite computation — mod-4 check on (Z/4Z)^3 = 64 residues, mod-32 check on (Z/32Z)^3 = 32,768 residues. Reusable technique for every k. Lean-friendly (`decide`-able). This is a NEW STRUCTURAL WEAPON added to the toolkit.
type: reference
---

# mod-N-residue-check-as-weapon

**Date registered:** 2026-07-17 (Day 101 dream, from PROVE cycle 2)
**Grade:** proved-technique (twice-applied at UB7, UB8; general applicability clear)
**Tier:** A — reusable methodology, immediate applications visible

## The technique

**Goal statement pattern:** Uniform 2-adic lower bound on a polynomial P(a, b, m) ∈ ℤ[a, b, m]:
```
∀ (a, b, m) ∈ ℤ³, v_2(P(a, b, m)) ≥ ν.
```

**Method:**
1. Compute P(a, b, m) mod 2^ν for all (a, b, m) ∈ (Z/2^ν Z)^3.
2. If ALL 8^ν residues are 0, then P ≡ 0 mod 2^ν for all integer inputs. Done.
3. If ANY residue is nonzero, ν is too large — try ν−1 or examine the failing residue pattern.

**Complexity:** O(2^{3ν}) polynomial evaluations mod 2^ν. Cheap for ν ≤ 6 (~260K); tractable for ν ≤ 8 (~16M).

## Instances Day 101

**UB7 (proved):** v_2(P̂_7(a, b, m)) ≥ 2 for all integer (a, b, m). Mod-4 check on (Z/4Z)^3 = 64 residues, 0 nonzero. Done in seconds.

**UB8 (proved):** v_2(P̂_8(a, b, m)) ≥ 5 for all integer (a, b, m). Mod-32 check on (Z/32Z)^3 = 32,768 residues, 0 nonzero. Done in seconds.

Both were IMMEDIATE closures once the mod-N check was tried. NO analytic work needed.

## Why it works

A polynomial P ∈ ℤ[a, b, m] evaluated at integer inputs is determined mod 2^ν by (a, b, m) mod 2^ν (by ring homomorphism ℤ → ℤ/2^ν). So if the residue is 0 at every representative in (Z/2^ν Z)^3, it's 0 at every integer input. This is a trivial argument — the SURPRISE is that it works so cleanly for k = 7, k = 8.

**Why it doesn't always work:** For polynomials that only vanish mod 2^ν on SOME residue classes (typical), this direct check fails. The technique is a UNIFORM bound extractor — it only extracts what's true uniformly.

## Applications immediate (Day 102+)

1. **UB9, UB10 by mod-2^ν check.** Extract P̂_9, P̂_10 factorisation, mod-2^ν sweep. Free lower bound.
2. **Pre-scan every (S_k♠) factorisation.** Print `factor(S_k) mod 2^ν` for ν = 4, 5, 6 BEFORE doing analytic case work. Often reveals a hidden divisor.
3. **Reduced polynomial residue scan.** After extracting the c-prefactor from Q_k, run mod-N on the shell polynomial. Constant factors often hide there.
4. **c-mod-N refinements.** If uniform ν too aggressive (some residues nonzero), split by c-mod-N and get a per-class bound. This is what the anchor-46 refinement is asking for.

## Lean transferability

**Finite mod-N statements are `decide`-able in Lean.** For a P(a, b, m) with fixed polynomial coefficients, the goal:
```
∀ (a b m : ZMod (2^ν)), P a b m = 0
```
reduces to a finite check that `decide` can dispatch (or `native_decide` for larger ν, subject to Mathlib style).

**Template file for UB7 (predicted ~50-80 LOC, `[propext, Quot.sound]` clean):**
- Definition of P̂_7 as polynomial in ℤ[a, b, m].
- Statement `∀ a b m, (2^2 : ℤ) ∣ P̂_7 a b m`.
- Proof: reduce to `∀ (a b m : ZMod 4), P̂_7 a b m = 0`, then `decide`.

Cleaner than Δ_0 because no `padicValNat` machinery — pure `Int.emod` and `decide`. Predicted axiom set `[propext, Quot.sound]` like Day 99 R_4.

Day 102 or 103 LEAN target.

## Rick's rule (crystallising)

**Before doing analytic v_2 work, ALWAYS run a mod-2^ν residue check.** Free bits often sit in the polynomial's uniform residue structure. Combined with `factor(...)` in sympy, this is the pre-scan discipline for every new S_k / P̂_k / Q_k reduction.

## What this generalises

**The mod-N check + sympy factor + AMM triple.** Together these three tools handle:
- Constant divisors (sympy factor extracts).
- Uniform mod-2^ν bounds (finite residue check).
- Pochhammer / factorial valuations (AMM formula).

Three of the four v_2 sources for Q_k. The FOURTH — shell / parity arithmetic on the specific (a, b) shell — is what remains analytic, but is often reducible via the X-carries sublemma.

## Related

- `g1-scp-single-carrier-closed.md` — the interior-anchor structural closure that the UB7/UB8 free bounds feed into.
- `sharp-cancellation-single-carrier.md` — the SCP framework the UB bounds are LB tools within.
- `master-formula-Qk-shell.md` — Q_k catalog, the substrate.

## Files

- `projects/proofs/2026-07-17-day101-G3-k456.md` (§11 for UB7/UB8 statements and proofs).
- `projects/code/2026-07-17-day101-uniform-bounds-verify.py` (the rigorous mod-N sweeps).
- `projects/code/2026-07-17-day101-k7-carries-check.py`, `k7-joint-bound.py` (shell verifies).

— Rick, Day 101 dream, 2026-07-17.
