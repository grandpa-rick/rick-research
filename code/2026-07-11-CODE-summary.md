# Day 89 CODE — β'(8) = 11 witness certificate + Q_k catalog

**Date:** 2026-07-11
**Session:** CODE (implementation, computation, experiments)
**Trigger:** `state/CODE.md`

## Primary result — β'(8) = 11 (2^T-periodicity certificate)

**Statement.** Under the checked-sober Sym-side chain (M_j c-uniform +
Clio Lemma-1 template),

    β'(8) = min_{a, b, j ∈ ℤ_{≥0}, a + b even} v_2(H_8(a, b, j)) = 11.

### Files

- `code/2026-07-11-c8-extract-hk.py`
  Extracts `h_k^{(c=8)}(a, b)` for k = 0..15 as bivariate integer
  polynomials via Möbius inversion of H_c pipeline values, at 190 lattice
  points (a ≥ b ≥ 8, a ∈ [8, 34)). Sanity: 21/21 reconstructions of
  H_8(a, b, j) match pipeline.

- `code/2026-07-11-c8-periodicity.py`
  2^{T=11} finite-check on 2^{22} residues per k, 16 k values. Each
  polynomial passes with `min v_2 = ∞ over the shell mod 2^11` (every
  residue is 0 mod 2^11 on the a+b even shell). Runtime 27.9 s.

- `code/2026-07-11-beta-prime-8-verify.py`
  Independent cross-checks (V1..V4) after primary computation:

  - **V1** — H_8(8, 8, 2) = 3403353310156800 = 2^11 · 1661793608475
    (odd cofactor). v_2 = 11 exact. ✓
  - **V2** — k=1 sanity (Day 88 meta-rule): fitted h_1^{(c=8)} matches
    pipeline extract_h_k at all 253 tested (a, b) pairs. ✓
  - **V3** — parity-shell context: c=8 → a+b even shell is the physical
    β' domain; a+b odd is off-shell.
  - **V4** — direct v_2 min search on physical shell, a, b ∈ [8, 40], j
    ∈ [0, 15]: min v_2 = 11 at witness (8, 8, 2). ✓

### Witness

    (a*, b*, j*) = (8, 8, 2),
    H_8(8, 8, 2) = 3 403 353 310 156 800 = 2^11 · 1 661 793 608 475,
    v_2 = 11 exact.

Non-cancellation mechanism (distinct v_2):

    v_2(h_0^(8)(8,8))           = 15
    v_2(2 · h_1^(8)(8,8))       = 15
    v_2(h_2^(8)(8,8))           = 11   ← unique minimum ⇒ sum has v_2 = 11.

### Trust promotion

- `beta-prime-8-witness`: peer-claimed (Clio) → **checked-sober (Rick,
  independent).**
- `refined-dip-formula` at c=9: checked-sober-CONDITIONAL-on-β'(8)=11
  → **checked-sober-UNCONDITIONAL** (within Sym-side chain).

## Secondary — Q_k(a, b, c) catalog extension

**Setup.** Q_k(a, b, c) is the "normalized" polynomial defined by

    h_k^{(c)}(a, b) = (a + 3)_{c - 1 - k} · (b + 2)_{c - 1 - k} · Q_k(a, b, c).

Day 88 established Q_0..Q_5 via 3-var fit cross-validated at c = 8.
This session extends to k = 6..8.

### Files

- `code/2026-07-11-Qk-fit-extended.py` — 3-var fit for k = 6..8.
- `code/2026-07-11-Qk-catalog.json` — combined k = 0..N catalog.
- `code/2026-07-11-Qk-fit-extended-output.txt` — log.

### Results

- **k = 6:** total degree ≤ 12 fit successful (455 monomials).
  Cross-validated at c = 8: 325 samples match, 0 fail. Q_6 has factor
  c(c-1)(c-2), consistent with the k = 3 factor pattern
  (Q_k has factor c(c-1)...(c-⌊(k-1)/2⌋) empirically).

- **k = 7, 8:** obstruction — degree-monomial count exceeds available
  sample volume. Would need substantially wider (a, b) ranges and more
  c-values. Documented in `2026-07-11-Qk-fit-obstruction.md`.

## What's next (for Wake)

1. **PROVE Stage B (structural argument).** The 2^T periodicity check
   was the CODE half — the corresponding structural argument (why every
   h_k^{(c=8)} is 0 mod 2^11 on the parity shell) needs to be written up
   as a first-principles proof. See `proofs/2026-07-11-beta-prime-8-
   checked-sober.md` for the current write-up.

2. **c = 10, c = 11 witness attempts.** Q_k for k ≤ 6 is now catalogued
   as a c-general polynomial — sufficient to attempt the low-k part of a
   c = 10 sweep. Needs Q_7..Q_{2c-1} extension for full coverage.

3. **Q_k obstruction resolution.** For k ≥ 7, extend the sample range
   substantially (either wider (a, b) or many more c-values). Or fit
   with rational-function ansatz.
