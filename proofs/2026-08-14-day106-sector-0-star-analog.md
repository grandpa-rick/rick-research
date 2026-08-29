# Day 106 PROVE — Sector-0 analog of the Reduction (★) for R ≡ 0 mod 4

**Date:** 2026-08-14
**Author:** Rick's prove-agent (Day 106 deep-work)
**Goal:** Re-derive the three-line algebra of Day 104 (★) in the sector
c ≡ R mod 16 with R ≡ 0 mod 4 (i.e. R ∈ {4, 8, 12, 16, ...}), and reconcile
the K_R discrepancy that surfaced from H5 (Day 105).

**Headline.** The Day 104 (★) formula
```
    ε_R = C_R − 4R + 2 + s_2(R−1) + s_2(R) + s_2(R+1) + K_R           (★_2)
```
is valid only for R ≡ 2 mod 4. In the sector R ≡ 0 mod 4, the correct analog is
```
    ε_R = C_R − 4R + s_2(R−1) + s_2(R) + s_2(R+1) + s_2(R/4)           (★_0)
```
i.e. the constant "+2" and the residual K_R merge into a single elementary
term s_2(R/4).

Combined with H5 (`C_R = 4R − 3 s_2(R)`) and H3 (`ε_R = ⌈log_2(R+2)⌉`), this
reconciles the discrepancy: the corrected K_R^{(0)} := s_2(R/4) − 2 gives
K_4 = K_8 = **−1** (matching Day 104's back-solve) rather than the Day 105
table entries K_4 = 1, K_8 = 0 (which came from mis-applying (★_2) in the
wrong sector).

---

## 1. Root cause of the sector split

Day 104's (★) equates `v_2(h_{2R}^{(c)}(R−2,R))` (via Pochhammer collapse +
Legendre + Claim B) with `β(c) − D(c) − (v_2(c−R) − ε_R)` under Claim A. The
base-UB deficit D(c) is sector-dependent:

- Sector-2 (c ≡ 2 mod 4, Day 98): `D_02(c) = 1 + s_2(m − 1)`, m = (c−2)/4.
- Sector-0 (c ≡ 0 mod 4, Day 97): `D_04(c) = s_2(c/4) − 1`.

In sector-0, m = (c−2)/4 is a **half-integer** (c ≡ 0 mod 4 ⇒ c−2 ≡ 2 mod 4),
so Day 104's Lemma 2 identity `s_2(c−1) − s_2(m−1) = s_2(R−1) − K_R + s_2(t)`
is meaningless: s_2(m−1) is not defined. The correct step uses D_04 and its
native integer parameter n := c/4 — with `s_2(n)` in place of `s_2(m−1)`
(no −1 shift, because D_04 involves s_2(c/4), not s_2(c/4 − 1)).

---

## 2. The sector-0 setup

Fix R ∈ {4, 8, 12} (i.e. R ≡ 0 mod 4, 4 ≤ R ≤ 15). Set
```
    c = R + 16t,   t ≥ 1  (so c > 2R for t large enough; c ≡ R mod 16).
```
Then c is divisible by 4 (both R and 16t are), so we're in the c ≡ 0 mod 4
sector; and c/4 = R/4 + 4t is a positive integer.

**Elementary s_2-decompositions.** Because R − 1 < 16, R < 16, R + 1 ≤ 16, and
R/4 < 4, the binary supports of these small numbers do not overlap with the
binary support of 16t (respectively 4t for R/4), so:
```
    s_2(c − R) = s_2(16t) = s_2(t)                                    (D1)
    s_2(c − 1) = s_2(R − 1 + 16t) = s_2(R − 1) + s_2(t)               (D2)
    s_2(c/4)   = s_2(R/4  + 4t)   = s_2(R/4)  + s_2(t)                (D3)
    v_2(c − R) = 4 + v_2(t)                                            (D4)
```
(D2) holds for R ≤ 16 since R − 1 ≤ 15 < 16 has no bit overlap with 16t.
Similarly R/4 < 4 for R ≤ 12 gives (D3); for R = 16 the identity R/4 = 4 does
overlap 4t but R = 16 doesn't fall in our target range because c ≡ 16 mod 16
means c ≡ 0 mod 16 which is a different residue class (handle separately).

---

## 3. Left-hand side of the reduction

By Day 88 Pochhammer collapse (Day 104 Lemma 1):
```
    h_{2R}^{(c)}(R−2, R) = (c−R−1)! (c−R)! / (R! (R+1)!) · Q_{2R}(R−2, R, c).
```
Legendre + `s_2(n−1) = s_2(n) + v_2(n) − 1` (Day 104 §2), and Claim B
(`v_2(Q_{2R}(R−2, R, c)) = C_R` constant on c ≡ R mod 16), give
```
    v_2(h_{2R}^{(c)}(R−2, R)) = 2(c−R) − 2 s_2(c−R) − v_2(c−R) − (2R+1)
                                + s_2(R) + s_2(R+1) + C_R.               (♦)
```
This identity is **sector-independent** — its derivation uses only Legendre
2-adics and Claim B, both of which apply for any c ≡ R mod 16 regardless of
R mod 4.

Substituting (D1), (D4):
```
    v_2(h_{2R}^{(c)}(R−2, R)) = 32t − 2 s_2(t) − 4 − v_2(t) − 2R − 1
                                + s_2(R) + s_2(R+1) + C_R
                              = 32t − 2 s_2(t) − v_2(t) − 2R − 5
                                + s_2(R) + s_2(R+1) + C_R.               (♦_0)
```

---

## 4. Right-hand side (sector-0 target)

The target formula (piecewise conjecture, sector-0 version) is
```
    v_2(H_c(R−2, R, 2R)) = β(c) − D_04(c) − (v_2(c−R) − ε_R),           (§_0)
```
using **D_04 instead of D_02**. With β(c) = 2(c−1) − s_2(c−1) and the
substitutions (D2), (D3):
```
    β(c) − D_04(c) = 2c − 2 − s_2(c−1) − (s_2(c/4) − 1)
                   = 2c − 1 − s_2(c−1) − s_2(c/4)
                   = 2c − 1 − s_2(R−1) − s_2(R/4) − 2 s_2(t).
```
Then RHS of (§_0):
```
    β(c) − D_04(c) − v_2(c−R) + ε_R
        = 2(R + 16t) − 1 − s_2(R−1) − s_2(R/4) − 2 s_2(t) − (4 + v_2(t)) + ε_R
        = 32t + 2R − 5 − s_2(R−1) − s_2(R/4) − 2 s_2(t) − v_2(t) + ε_R. (§_0′)
```

---

## 5. Setting (♦_0) = (§_0′) and solving for ε_R

Equate:
```
    32t − 2 s_2(t) − v_2(t) − 2R − 5 + s_2(R) + s_2(R+1) + C_R
      = 32t + 2R − 5 − s_2(R−1) − s_2(R/4) − 2 s_2(t) − v_2(t) + ε_R.
```
Cancel `32t`, `− 2 s_2(t)`, `− v_2(t)`, `− 5`:
```
    − 2R + s_2(R) + s_2(R+1) + C_R = 2R − s_2(R−1) − s_2(R/4) + ε_R.
```
Solve for ε_R:
```
    ε_R = C_R − 4R + s_2(R−1) + s_2(R) + s_2(R+1) + s_2(R/4).           (★_0)
```

This is the sector-0 analog of Day 104's (★). **The comparison with (★_2):**
```
    (★_2)   ε_R = C_R − 4R + 2 + s_2(R−1) + s_2(R) + s_2(R+1) + K_R
    (★_0)   ε_R = C_R − 4R + 0 + s_2(R−1) + s_2(R) + s_2(R+1) + s_2(R/4)
```
The "+2" in (★_2) has vanished, and the residual `K_R` (which was
`s_2(m−1) − s_2(t)` in sector-2) is replaced by the closed-form `s_2(R/4)`.

**Where they differ algebraically.** In sector-2, D_02 contributes `+ s_2(m−1)`
to the s_2-tail; using the corollary of neighbours plus (c−1) = 16t + (R−1)
decomposition gives `s_2(m−1) = s_2(t) + K_R`. In sector-0, D_04 contributes
`+ s_2(c/4) − 1` to the s_2-tail; using c/4 = R/4 + 4t gives `s_2(c/4) =
s_2(t) + s_2(R/4)` **exactly** (no residual), and the "−1" merges cleanly
with the "−2" from D_02's `1 + s_2(m−1)`. Net effect: the sector-0 residual is
the constant `s_2(R/4)` (no t-dependence) and there is no additive "+2".

---

## 6. Verification: K_R for R ∈ {4, 8}

If we insist on writing the sector-0 identity in the (★_2)-style form (constant
"+2" plus residual K_R), then
```
    K_R^{(0)} := s_2(R/4) − 2.                                          (K_0)
```

- **R = 4:** K_4^{(0)} = s_2(1) − 2 = 1 − 2 = **−1**. ✓ Matches Day 104 back-solve.
- **R = 8:** K_8^{(0)} = s_2(2) − 2 = 1 − 2 = **−1**. ✓ Matches Day 104 back-solve.
- **R = 12:** K_12^{(0)} = s_2(3) − 2 = 2 − 2 = 0 (prediction; verify empirically).

The Day 105 K-closed table entries K_4 = 1, K_8 = 0 (from
`K = ⌈log_2(R+2)⌉ − 2 + 2 s_2(R) − s_2(R−1) − s_2(R+1)` applied via (★_2))
are **mis-applied**: that identity was derived under (★_2) and is only valid
in sector-2. Substituting H5 into (★_0) directly:
```
    ε_R = (4R − 3 s_2(R)) − 4R + s_2(R−1) + s_2(R) + s_2(R+1) + s_2(R/4)
        = s_2(R−1) − 2 s_2(R) + s_2(R+1) + s_2(R/4).                   (ε_0)
```

**Verification against H3 (`ε_R = ⌈log_2(R+2)⌉`):**

| R  | s_2(R−1) | s_2(R) | s_2(R+1) | s_2(R/4) | ε_R (ε_0)             | ⌈log_2(R+2)⌉ |
|----|----------|--------|----------|----------|------------------------|--------------|
| 4  | 2        | 1      | 2        | 1        | 2−2+2+1 = **3**       | 3 ✓           |
| 8  | 3        | 1      | 2        | 1        | 3−2+2+1 = **4**       | 4 ✓           |
| 12 | 3        | 2      | 3        | 2        | 3−4+3+2 = **4**       | 4 ✓           |
```
Prediction confirmed at R = 12 as well (contingent on H5 at R = 12, which is
open).

---

## 7. Summary

1. **Sector-0 (★_0):** `ε_R = C_R − 4R + s_2(R−1) + s_2(R) + s_2(R+1) + s_2(R/4)`.

2. **Where sector-0 diverges algebraically:** Lemma 2 of Day 104 substitutes
   `s_2(m−1)` with m = (c−2)/4. In sector-0, this m is not an integer;
   replacing with `s_2(c/4)` (from D_04) cleanly absorbs the residual K_R
   into the closed-form `s_2(R/4)` and kills the additive "+2".

3. **Verification numbers in the (★_2)-shape:** K_R^{(0)} := s_2(R/4) − 2, so
   K_4 = **−1** and K_8 = **−1** (matches Day 104's back-solve). Day 105's
   table entries K_4 = 1, K_8 = 0 came from mis-applying (★_2)'s K-closed
   identity in the wrong sector.

4. **No unified single-line K_R across sectors.** The two residuals — sector-0
   `s_2(R/4) − 2` and sector-2 K_R^{(2)} = ⌈log_2(R+2)⌉ − 2 + 2 s_2(R) −
   s_2(R−1) − s_2(R+1) — come from structurally different base-UB formulas
   (D_04 vs D_02) and don't merge into any `s_2(f(R))` for elementary f.

5. **Contingencies.** Same as Day 104: Claim A (empirical at R = 4, 8),
   Claim B (proved at R = 4 via Q_8, R = 8 via Vandermonde fit), and D_04(c)
   as base UB (Day 97, conditional on Master Formula M for m ≥ 3). R = 12
   Claim A/B unverified; H5 at R = 12 open.
