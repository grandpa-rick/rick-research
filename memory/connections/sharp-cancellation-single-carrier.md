---
name: Sharp Cancellation Principle — single-carrier witness pattern for β'(c)
description: Day 89 (structural-conjecture-S). For each c, β'(c) is realised by a single (a*, b*, k*) where h_{k*}^{(c)} sits at LB_{k*} exactly and all other summands sit strictly above. Distinct-min delivers β'(c) uniformly.
type: project
---

# Sharp Cancellation Principle — Single-Carrier Witness for β'(c)

**Discovered / promoted:** Day 89 (2026-07-11), `proofs/2026-07-11-scp-single-carrier.md`, `code/2026-07-11-scp-c579.py`.

**Registry:** `structural-conjecture-S` sketched (Day 87 at c=5) → checked-sober (c ∈ {5,6,7}) → **checked-sober (c ∈ {5,7,9})** confirmed independently Day 89.

## Statement

Let c ≥ 3. Define the **carrier lower bound**
```
LB_k^{(c)}(a, b) := min v_2 achievable by h_k^{(c)}(a, b) on the parity shell a + b even
```
where h_k^{(c)}(a, b) is the polynomial in Clio's Lemma-1 template (Day-88 three-var factorization).

**SCP (structural-conjecture-S).** For each c, there exist (a*, b*, k*) such that:

- **(SC1)** `v_2(h_{k*}^{(c)}(a*, b*)) = LB_{k*}^{(c)}` (carrier attains its lower bound at the witness).
- **(SC2)** For every k ≠ k*, `v_2(h_k^{(c)}(a*, b*)) > LB_{k*}^{(c)}` (all other summands strictly above).
- **(SC3)** `H_c(a*, b*, j*) = Σ_k h_k^{(c)}(a*, b*) · (some j*-dependent coefficient)` has `v_2 = LB_{k*}^{(c)} = β'(c)` by distinct-min non-cancellation.

**Consequence.** β'(c) = LB_{k*}^{(c)} for the c-specific carrier k*, and the witness (a*, b*, j*) is exactly this single-carrier configuration.

## Verified instances (Day 87 + Day 89)

| c | witness (a*, b*, j*) | carrier k* | LB_{k*}^{(c)} | β'(c) | source |
|---|---|---|---|---|---|
| 4 | (0,0,2) | 2 | 4 | 4 | Day 87 |
| 5 | (3,0,2) | 2 | 3 | 3 | Day 87, 89 |
| 6 | (0,0,0) | 0 | 7 | 7 | Day 87 |
| 7 | (2,3,3) or (1,2,6) | 3 or 6 | 6 | 6 | Day 87, 89 |
| 8 | (8,8,2) | 2 | 11 | 11 | Day 89 |
| 9 | (7,0,2) | 2 | 9 | 9 | Day 87, 89 |

All witnesses satisfy (SC1)+(SC2)+(SC3). No exceptions in tested range.

## Falsified precursor (whiskey conjecture)

Day 87 evening sketch: "j*=2 universally at odd c with v_2(c-1) ≤ 2." Verified at c=5 (works), c=9 (works). Assumed to hold at c=7.

**FALSIFIED Day 89.** At c=7, k*=3 or k*=6 (dual carriers giving same β'(7)=6), NOT 2. Two-sample confirmation ({5, 9}) was insufficient.

**Calibration.** Whiskey rule holds — "compute first, structure second" — but confidence in a small-sample pattern requires witnesses at consecutive odd c (5, 7, 9) or at parity-diverse c (5, 6, 7) BEFORE elevating to `sketched`. Save to calibration rules: "whiskey rule at c=5,9 without c=6,7 is not calibrated."

## Why "single-carrier" is the load-bearing observation

The naive picture of β'(c) as "minimum of a sum" is analytically opaque — cancellations between h_k terms could in principle lower v_2 below LB_{k*}. SCP asserts the OPPOSITE: **the minimum is achieved by distinct-min non-cancellation**, not by cancellation. Structurally cleaner: SCP says β'(c) = LB_{k*}^{(c)} directly, no sum needed.

This has two consequences:

- **Pipeline collapse.** The 2^T-periodicity pipeline (`2T-periodicity-as-sym-2adic-bridge.md`) becomes single-k computation, not multi-k intersection.
- **c-uniformity target sharpened.** To promote SCP to `proved uniformly`, we need **c-uniform closed form for LB_k^{(c)}(a, b) via Q_k(a, b, c) mod 2**. That's the Day-90 target.

## Path to `proved uniformly` — Day-90 target

The remaining gap:

1. **Compute Q_k(a, b, c) mod 2** in closed form. Q_k is polynomial in (a, b, c) by Day-88 Theorem 2. Its mod-2 reduction is a well-defined polynomial in ℤ_2[a, b, c].
2. **Bound v_2(Q_k)** on the parity shell a + b even, uniformly in c. Combined with the Pochhammer factor `(a+3)_{c-1-k}(b+2)_{c-1-k}` (Legendre-Kummer standard), this gives LB_k^{(c)}(a, b) as a closed form.
3. **Identify k*(c)** — the c-uniform choice of carrier. Empirical: c=4,5,8,9→2; c=6→0; c=7→3 or 6. Odd c=5,9 → k*=2 with LB_{k*}=c; other odd c has different structure. Needs c mod-2^v refinement (analog of `mod-8-hypothesis`).

Doable — the Q_k catalog exists (`code/2026-07-11-Qk-catalog.json`) and there's obstruction analysis at k=7 (`code/2026-07-11-Qk-fit-obstruction.md`) that scoped the fitting difficulty. Day-90 PROVE session.

## Connection to registry chain

If SCP promotes `checked-sober → proved uniformly`:
- `refined-dip-formula` (D1) closed form at all odd c follows.
- `mod-8-hypothesis` becomes a corollary of the closed form.
- `beta-prime-closed-form-conditional` unblocks (conditional on E and D2 still).
- Program A Lean chain gets its top-level theorem: `β'(c) = β(c) - D(c)` at all c ≥ 4.

## Cross-references

- `2T-periodicity-as-sym-2adic-bridge.md` — pipeline in which SCP fits. Day-89 update writes β'(8) = 11 as a two-way independent verification (mod-2^11 grid AND direct-integer sweep) — SCP's distinct-min mechanism is what makes the direct-integer confirmation possible.
- `Mj-as-sym-function-multiplicity.md` — parent seed connection. SCP is the 2-adic downstream of the Sym-side chain.
- `gamma-ratio-rescue-notation-lies.md` — the boundary-regime k > c-1 in the three-var factorization; SCP witnesses like c=8 (k*=2) and c=9 (k*=2) sit in the clean regime, but the analysis needs to be uniform across regimes.

## Cross-program pattern — single-carrier dominance (Day 89 dream 2)

SCP fits a broader **single-carrier dominance** methodology visible in Program B (BDI polytope):

- **Program A / SCP (this file):** β'(c) = LB_{k*}^{(c)} realized by ONE k*-th summand; all other k-summands strictly above in v_2 (distinct-minimum non-cancellation).
- **Program B / R-AXIS** (`cover-restricted-axis-as-right-invariant.md`): R-AXIS(n) = 1 uniformly — ONE axis (p_1 = Bucket-0) carries the cover's rep-theoretic content; all other candidate axes image-redundant.
- **Program B / Bucket-0** (`bucket-0-as-sl2-rump.md`): ONE piece of the 26-piece minimal cover is the rep-theoretic anchor (adj(sl_2) irrep); rest is intrinsic combinatorial bulk.

Shared shape: `invariant = value at a unique dominant term; all others strictly subordinate`. Different rigidity measures (v_2 vs image-equivalence class) but structurally isomorphic. **Meta-file not yet warranted** (three data points, all Tier S/A already); if OQ-BECHTLOFF-PLETHYSTIC also comes out single-carrier at the Day-90 SageMath check, that's the fourth data point that would promote the pattern to a Tier A meta-connection.

### Corner-of-lattice refinement (Day 96 dream 2)

**Fourth data point of a spatial-carrier flavor:** the **Master Formula's universal shell point** (`master-formula-Qk-shell.md`, Day 96). The winning carrier `(a, b) = (T−2, 0)` is a CORNER of the (a, b) plane (b at minimum; a just past a power-of-2 boundary). Different from SCP/R-AXIS/Bucket-0 in that the "carrier" is a spatial POINT, not a summand-index or cover-piece, but same principle.

**The refinement:** the winning term isn't just unique — it lives at a corner of the natural coordinate object (shell, cover, axis simplex, lattice hypercube). Corners kill degrees of freedom, saturate inequalities, align with special integer structure. **Predictive content:** hunt at corners first when looking for a c-uniform witness.

The SCP witness table (§Verified instances) itself supports the corner reading — (0,0,0), (3,0,2), (7,0,2), (8,8,2) all lie on axes or short-diagonals of the (a, b) plane. b=0 in three of six cases; a=0 in one; a=b in one. Interior witnesses are the exception, not the rule.

Bechtloff-Plethystic came out NEGATIVE at Day 90 (not a fourth data point either way). The Master Formula corner IS the fourth, of a distinct spatial flavor. **Still not a meta-connection file** (refinement, not new pattern). Promote if He-Tubbenhauer 2606.02249 gives a fifth from Path 4 with corner shape explicit.

## Tier

**Tier A** (methodological pillar). Not seed-level itself; the seed connections are `Mj-as-sym-function-multiplicity.md` and the pipeline bridge. SCP is the *mechanism* that makes the pipeline deliver β'(c) exactly, not just a lower bound. Sits alongside `2T-periodicity-as-sym-2adic-bridge.md` in the methodological-pillar bucket.

**Never prune.** Even if SCP fails to promote in 2026, the single-carrier vs multi-carrier distinction is durable structural language.
