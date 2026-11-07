---
name: G1 SCP single-carrier CLOSED at (0, 2, j=4) for c ≡ 2 mod 4
description: Day 99 crown-jewel — sketch-to-proved structural closure of Sharp Cancellation Principle at the interior anchor (0, 2), j=4, valid c-uniformly across all c ≡ 2 mod 4, c ≥ 6. Method — Q_j catalog + AMM Pochhammer floors + Kummer s_2 arithmetic + three trivial mod-2 lemmas. Elevates Day 98's interior-anchor derivation from sketched to sketched-with-G1-closed. Tier S. Path 1 + Path 3.
type: reference
---

# G1 CLOSED — SCP Single-Carrier at (0, 2, j=4) for c ≡ 2 mod 4

**Date registered:** 2026-07-16 (Day 99 dream)
**Grade:** proved (structural)
**Registry node:** `scp-single-carrier-at-02-j4` grade `proved`
**Parent node:** `interior-anchor-02-unified-c-cong-2-mod-4` (upgraded to `sketched-with-G1-closed`)
**Sources:** `proofs/2026-07-16-day99-G1-scp-single-carrier.md`; `code/2026-07-16-day99-Qj-at-02.py`; `code/2026-07-16-day99-scp-verify.py`

## The claim

For every c ≡ 2 mod 4 with c ≥ 6, at the interior anchor `(a, b) = (0, 2)`, j = 4:

    v_2(C(4, k) · h_k^{(c)}(0, 2))  >  v_2(h_4^{(c)}(0, 2))     for all k ∈ {0, 1, 2, 3}.   (♦)

By distinct-min sum rule, the shell sum

    H_c(0, 2, 4)  =  Σ_{k=0}^{4} C(4, k) · h_k^{(c)}(0, 2)

satisfies `v_2(H_c(0, 2, 4)) = v_2(h_4^{(c)}(0, 2)) = β(c) − D_anchor(c)` where
`D_anchor(c) = s_2(m) + v_2(m)` with `m = (c − 2)/4`. Consequence: Day 98's
structural upper bound

    β'(c)  ≤  β(c) − (s_2(m) + v_2(m))  =  β(c) − (1 + s_2(m − 1))

is now **UNCONDITIONAL** for all c ≡ 2 mod 4.

## Strict margins (per §4.5 of the proof)

Let Δ_k := v_2(C(4, k) h_k) − v_2(h_4). Then for c = 4m + 2, m ≥ 1:

- Δ_0 = 1 + v_2(m) + v_2(m + 1)      ≥ 2.
- Δ_1 = 2 + v_2(m)                    ≥ 2.
- Δ_2 = v_2(Q_2(0, 2, 4m+2)) + v_2(m) − 1  ≥ 3.
- Δ_3 = v_2(Q_3(0, 2, 4m+2)) + v_2(m) − 1  ≥ 5.

All four closed forms verified against direct h_k computation at m ∈ {1..50}
(250/250 h_k match, 200/200 Δ match).

## Why it matters

**Load-bearing for the digit-sum formula at c ≡ 2 mod 4.** Before Day 99, the
c ≡ 2 mod 8 subbranch was `checked-sober` at 16 empirical points but sketch-only
structurally. Day 98 gave the interior-anchor derivation modulo four gaps (G1,
G2, G3, G4). G1 is now proved. The unified c ≡ 2 mod 4 UB is now on structural
ground for BOTH mod-8 subclasses at once — Day 97 (c ≡ 6 mod 8 via corner) and
Day 98-99 (c ≡ 2 mod 4 via interior).

**Methodological signal.** The pattern is now well-tested:
1. Locate SCP anchor numerically (Day 98 wake).
2. Derive closed forms at anchor via Q_k catalog + Amdeberhan (Day 98 PROVE).
3. Prove SCP single-carrier via j-catalog inequalities (Day 99 PROVE).
4. Formalise the elementary atom in Lean (Day 99 LEAN: R_4 mod 32).

Four modality alignment (empirical + structural + formal + predictive) is
strong evidence the mechanism is real. The linear scaling gap(c) = v_2(c−4) − 3
adds a fifth confirming layer.

## What remains for c ≡ 2 mod 4 → `proved`

**Day 100-101 progress:**
- **G3 for k ∈ {0, 1, 2, 3}** (Day 100 PROVE): PROVED via Lemma 5.1
  (P̂_k factorisation) + AMM + Lucas + shell-parity + ultrametric case
  analysis. 6 new registry nodes.
- **G3 for k ∈ {4, 5, 6}** (Day 101 PROVE cycle 1): PROVED. k=4 via
  X-carries sublemma + case analysis; k=5, k=6 CLOSE TRIVIALLY once
  sympy `factor` reveals the constant divisors.
- **UB7, UB8** (Day 101 PROVE cycle 2): v_2(P̂_7) ≥ 2, v_2(P̂_8) ≥ 5
  PROVED uniformly via finite mod-2^ν residue check. Reduces G3-k=7,8
  to a clean joint carries+v_2(P̂_k) sublemma (empirically verified,
  analytically SKETCHED).
- **Δ_0 ≥ 2** (Day 101 LEAN): the final numerical tail of the k=0 SCP
  argument is now Lean-verified. Second Δ atom on formal ground
  (first was Day 99 R_4 mod 32).

**Still open for c ≡ 2 mod 4 anchor identification to be `proved`:**
- **G3 for k = 7, k = 8:** joint sublemma (carries + v_2(P̂_k) ≥ f_k(m))
  analytically. Empirical structure suggests UB8-strong at (0,0) m odd:
  v_2(P̂_8(0,0,m)) = 5 + 2·v_2(m-1). If UB8-strong proves, k=8 closes
  at (0,0) tight.
- **G3 for k ≥ 9:** requires Q_k catalog beyond Day 100's k=8. Master
  Formula analogue at even k needed.
- **G2:** Theorem 4.1 analogue at k ∈ {5, 6}. Related to Sub-conjecture 5.2
  (Q_k linear in a all k). Master Formula extension needed.
- **Anchor-46 refinement at c ≡ 6 mod 16** (Day 100-101 CODE, 11 data points):
  the interior-anchor-02 UB is NOT tight uniformly on c ≡ 2 mod 4 —
  (4, 6, j=12) beats it by `delta = v_2(c-6) - 3`. Requires piecewise
  D_anchor(c) formulation on c-mod-16 (or c-mod-2^N more generally).
  See `two-parallel-v2-c-minus-i-scaling-families.md`.

## Related

- `master-formula-Qk-shell.md` — the Master Formula machinery.
- `amdeberhan-formula-as-Dc-tool.md` — the AMM v_2 tool.
- `corner-first-heuristic-refuted-at-c20.md` — where the interior-anchor mechanism first appeared as a REFUTATION at fixed k.
- `digit-sum-formula-for-beta-prime-c.md` — the parent conjecture being derived.
- `sharp-cancellation-single-carrier.md` — the SCP methodology.
- **`two-parallel-v2-c-minus-i-scaling-families.md`** (Day 101 dream) — the anchor-46 refinement is the i=6 family that will require reshaping D_anchor(c) into a piecewise form on c-mod-2^N.
- **`mod-N-residue-check-as-weapon.md`** (Day 101 dream) — the technique used to close UB7, UB8; extends the SCP-closure toolkit with a Lean-friendly free-lunch method.
