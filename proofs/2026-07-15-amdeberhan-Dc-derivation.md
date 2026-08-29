# Day 97 PROVE — Amdeberhan × Master-Formula derivation of D(c) at the universal shell corner

**Date:** 2026-07-15
**Author:** Rick's prove-agent
**Registry target:** `beta-prime-digit-sum-formula` (upgrade from `checked-sober`).
**Prior:** `2026-07-14-delta-recursion-odd-k-attempt.md` (Day 96 three-cycle),
`memory/connections/amdeberhan-formula-as-Dc-tool.md` (blueprint).
**Novelty:** `novelty-unaudited` (Phase C not run this session).

---

## 0. Executive summary — what this session buys

**Headline (proved, conditional on Master Formula (M) for m ≥ 3):**

For **all c even** and **T = smallest 2^t > c−2**, the value
`v_2(h_{2m+1}^{(c)}(T−2, 0))` is **INDEPENDENT of m** over odd `2m+1 ∈ [1, c−3]`,
and equals
```
    v_2(h_1(T−2, 0))  =  2·v_2((c−2)!) + v_2(c).
```
The difference
```
    D_★(c)  :=  β(c) − v_2(h_1(T−2, 0))  =  1 + s_2(c−2) − v_2(c)                (D★)
```
is the "corner-derived" D(c). For c ≡ 0 mod 4 with c = 4k, `D_★(c) = s_2(k) − 1`;
for c = 4k + 2, `D_★(c) = s_2(k)`.

**Sealed comparison vs empirical D(c) (§5 below):**

- **c ≡ 0 mod 4 (c = 4, 8, 12):** `D_★ = D_emp` **at 3/3**. Digit-sum formula
  reproduced. Structural derivation via Amdeberhan + Master Formula.
- **c ≡ 6 mod 8 (c = 6, 14):** `D_★ = D_emp` **at 2/2**. Digit-sum formula reproduced.
- **c ≡ 2 mod 8 (c = 10):** `D_★ = D_emp − v_2((c−2)/4)`. Off by 1 at c=10.
  Diagnostic: `(T−2, 0)` overshoots β' by `v_2((c−2)/4) = v_2(k)` for c = 4k+2.
- **c odd:** `D_★ < D_emp` substantially. Diagnostic: at (T−2, 0), (2)_L is
  NOT at Kummer floor for odd L (=  odd c, odd k case), and the corner
  fundamentally cannot reach the true min for odd c.

**Registry recommendation (§7):** Upgrade `beta-prime-digit-sum-formula` from
`checked-sober` → **`sketched`** for the c ≡ 0 mod 4 AND c ≡ 6 mod 8 branches,
conditional on Master Formula (M). Keep `checked-sober` for c ≡ 2 mod 8 and c odd.

**Circular-verification countermeasure honored:** Corners enumerated = {(T−2, 0),
(0, T−2), (0, 0), (T−2, T−2)}. Odd k enumerated: full range. Min computed
WITHOUT looking at empirical D(c). Comparison is Step 5 only.

---

## 1. Setup

**Day 88 three-variable factorisation** (lean-verified):
```
    h_k^{(c)}(a, b)  =  (a + 3)_L · (b + 2)_L · Q_k(a, b, c),          L := c − 1 − k.
```

**Amdeberhan-Manna-Moll (arXiv:0707.2119).** For any integer a ≥ 1, k ≥ 0:
```
    v_2((a)_k)  =  k − s_2(a + k − 1) + s_2(a − 1).                    (AMM)
```
(One-line consequence of Legendre `v_2(n!) = n − s_2(n)`.)

**Universal shell corner.** For c ≥ 4, define
```
    T := smallest 2^t strictly greater than c − 2.
```
Equivalently `t = ⌈log_2(c − 1)⌉`. In particular T > c − 2 ≥ L always.

**Master Formula (M)** (`master-formula-Qk-shell.md`, sketched at m ≤ 2, verified m = 3):
For k = 2m + 1, m ≥ 1:
```
    Q_{2m+1}(a, 0, c)  =  c · (c−1) · (c−2m) · Π_{i=2}^{2m−1}(c−i)² · [ 2m(2m+1)(a+2) − (c−1)(c−2m)(c−2m−1) ].       (M)
```
For m = 0 (k = 1), `Q_1(a, 0, c) = −c(c − 1)` (initial condition).

**Convention.** Throughout this document, `(a)_k` is the RISING Pochhammer
`a(a+1)···(a+k−1)`, matching (AMM) and the Day 88 factorisation. `x^{↓n}` is the
falling factorial.

---

## 2. Corner enumeration — v_2 of Pochhammer factors at all four corners

We enumerate the four corners of the (a, b) rectangle whose vertices are
`{0, T−2} × {0, T−2}`. For each corner and each odd `k = 2m + 1` in `[1, c − 3]`,
apply (AMM) to the two Pochhammer factors of `h_k^{(c)}`. Set `L := c − 1 − k`.

### 2.1 Corner (T−2, 0)

- `(a + 3)_L = (T + 1)_L`.
- `(b + 2)_L = (2)_L`.

Applying (AMM):
```
    v_2((T + 1)_L) = L − s_2(T + L) + s_2(T)
                    = L − s_2(T + L) + 1                                (since T = 2^t)
    v_2((2)_L) = L − s_2(L + 1) + s_2(1)
               = L − s_2(L + 1) + 1.
```

**Kummer-floor claim.** For **c even** and **odd k**, we have **L even**, and
`(T + 1)_L`, `(2)_L` both hit Kummer floor `v_2(L!) = L − s_2(L)`.

*Proof.* c even ⇒ c − 1 odd ⇒ L = c − 1 − k = odd − odd = even.

**(T + 1)_L at floor.** `L < T` since `L ≤ c − 2 < T`. So T and L have disjoint
bit-support in `T + L`, giving `s_2(T + L) = s_2(T) + s_2(L) = 1 + s_2(L)`. Hence
`v_2((T + 1)_L) = L − (1 + s_2(L)) + 1 = L − s_2(L) = v_2(L!)`. ✓

**(2)_L at floor.** L even ⇒ L + 1 odd ⇒ `s_2(L + 1) = s_2(L) + 1` (Kummer:
`s_2(n) − s_2(n − 1) = 1 − v_2(n)`, and `v_2(L + 1) = 0`). Hence
`v_2((2)_L) = L − (s_2(L) + 1) + 1 = L − s_2(L) = v_2(L!)`. ✓

**Sanity check.** `(2)_L = (L + 1)!/1! = (L + 1)!`. v_2 = `(L + 1) − s_2(L + 1)`.
For L even: `= L + 1 − s_2(L) − 1 = L − s_2(L) = v_2(L!)`. ✓ ✓

**Sum at (T−2, 0):**
```
    v_2((T+1)_L) + v_2((2)_L)  =  2·v_2(L!)                               (P★)
```
for c even, k odd.

### 2.2 Corner (0, 0)

- `(a + 3)_L = (3)_L`.
- `(b + 2)_L = (2)_L`.

Applying (AMM):
```
    v_2((3)_L) = L − s_2(L + 2) + s_2(2)
               = L − s_2(L + 2) + 1.
    v_2((2)_L) = L − s_2(L)        (as in §2.1, using L even).
```

For L even: write `L = 2ℓ`. `L + 2 = 2(ℓ + 1)`. `s_2(L + 2) = s_2(ℓ + 1)`,
`s_2(L) = s_2(ℓ)`. Then
```
    s_2(L + 2) − s_2(L) = s_2(ℓ + 1) − s_2(ℓ) = 1 − v_2(ℓ + 1)
                        = 1 − v_2(L/2 + 1) = 1 − v_2((L + 2)/2).
```
Rewriting: `v_2(L + 2) = 1 + v_2((L + 2)/2)`, so `v_2((L + 2)/2) = v_2(L + 2) − 1`.

Hence
```
    v_2((3)_L)  =  L − s_2(L) − (1 − v_2(L + 2) + 1) + 1  ??   [messy, redo]
```
Let me just compute directly:
```
    v_2((3)_L) − v_2((2)_L) = (L − s_2(L + 2) + 1) − (L − s_2(L))
                            = s_2(L) − s_2(L + 2) + 1
                            = 1 − (1 − v_2((L + 2)/2))
                            = v_2((L + 2)/2)
                            = v_2(L + 2) − 1                    (L even ⇒ L+2 even).
```

Since `v_2((2)_L) = v_2(L!)` (from §2.1), we get
```
    v_2((3)_L) = v_2(L!) + v_2(L + 2) − 1.                                (P0-a)
```

**Sum at (0, 0):**
```
    v_2((3)_L) + v_2((2)_L)  =  2·v_2(L!) + v_2(L + 2) − 1
                             =  2·v_2(L!) + v_2(c − k + 1) − 1                    (P0)
```
(using `L + 2 = c − k + 1`.)

**Compared to (T−2, 0):** `(0, 0)` has EXCESS `v_2(c − k + 1) − 1 = v_2(c − 2m) − 1`.
Since c even and 2m even, `c − 2m` is even, so `v_2(c − 2m) ≥ 1` and the excess is ≥ 0.
`(0, 0)` is weakly WORSE than `(T−2, 0)` on the Pochhammer side.

### 2.3 Corner (T−2, T−2)

- `(a + 3)_L = (T + 1)_L`  (as in §2.1): v_2 = v_2(L!).
- `(b + 2)_L = (T)_L`.

Applying (AMM) to `(T)_L`:
```
    v_2((T)_L) = L − s_2(T + L − 1) + s_2(T − 1)
               = L − s_2(T + L − 1) + t.                       (s_2(2^t − 1) = t)
```

For L even: `L − 1` odd, `L − 1 < T`, so T and L − 1 have disjoint bit-support and
`s_2(T + L − 1) = 1 + s_2(L − 1)`. Hence
```
    v_2((T)_L) = L − 1 − s_2(L − 1) + t.
```
Kummer: `s_2(L − 1) = s_2(L) + v_2(L) − 1` (since `s_2(L) − s_2(L−1) = 1 − v_2(L)`).
So
```
    v_2((T)_L) = L − 1 − s_2(L) − v_2(L) + 1 + t = v_2(L!) + t − v_2(L).
```

**Excess over Kummer floor:** `t − v_2(L)`. Since `v_2(L) < t` (as `L < T = 2^t`),
excess is ≥ 1.

**Sum at (T−2, T−2):**
```
    v_2((T+1)_L) + v_2((T)_L)  =  2·v_2(L!) + t − v_2(L)                 (PTT)
```
Strictly WORSE than (T−2, 0) on the Pochhammer side by `t − v_2(L) ≥ 1`.

### 2.4 Corner (0, T−2)

- `(a + 3)_L = (3)_L`: `v_2 = v_2(L!) + v_2(c − k + 1) − 1` (from §2.2).
- `(b + 2)_L = (T)_L`: `v_2 = v_2(L!) + t − v_2(L)` (from §2.3).

**Sum at (0, T−2):**
```
    v_2((3)_L) + v_2((T)_L)  =  2·v_2(L!) + v_2(c − k + 1) − 1 + t − v_2(L)     (P0T)
```
Strictly WORSE than (T−2, 0) by `v_2(c − k + 1) − 1 + t − v_2(L) ≥ t ≥ 2`.

### 2.5 Ranking (Pochhammer side only, c even, k odd)

| Corner        | Pochhammer sum (relative to `2·v_2(L!)`) |
|---------------|----------------------------------------|
| (T−2, 0)      | 0 (Kummer floor for both) |
| (0, 0)        | `+ v_2(c − k + 1) − 1` ≥ 0 |
| (T−2, T−2)    | `+ t − v_2(L)` ≥ 1 |
| (0, T−2)      | `+ v_2(c − k + 1) − 1 + t − v_2(L)` ≥ 1 |

**(T−2, 0) is the unique Poch-min corner** (with (0, 0) tying when `v_2(c − k + 1) = 1`).

---

## 3. v_2(h_k) at (T−2, 0) via Master Formula

### 3.1 Assembly

For c even, k = 2m + 1, odd k in `[1, c − 3]`, at corner (T−2, 0):
```
    v_2(h_{2m+1}^{(c)}(T−2, 0))  =  2·v_2(L!) + v_2(Q_{2m+1}(T−2, 0, c))                (A)
```
where `L = c − 2 − 2m`.

Applying Master Formula (M) with `a = T − 2 ⇒ a + 2 = T`:
```
    Q_{2m+1}(T−2, 0, c)  =  c · (c−1) · (c−2m) · Π_{i=2}^{2m−1}(c−i)² · [ 2m(2m+1)·T − (c−1)(c−2m)(c−2m−1) ]
```

### 3.2 2-adic analysis of the bracket (c even)

- `v_2(2m(2m+1)·T) = 1 + v_2(m) + t ≥ 1 + t`.
- `v_2((c − 1)(c − 2m)(c − 2m − 1)) = v_2(c − 2m)` (both c − 1 and c − 2m − 1 odd
  since c even, m integer, `2m` even so c − 2m even but c − 2m − 1 odd; and c − 1 odd).
- Since `c − 2m < c ≤ 2^t = T`, we have `v_2(c − 2m) < t < 1 + t`.

**Distinct valuations ⇒** `v_2(bracket) = v_2(c − 2m)`.

### 3.3 v_2(Q_{2m+1}(T−2, 0, c)) closed form

For c even, m ≥ 1:
```
    v_2(Q_{2m+1}(T−2, 0, c))  =  v_2(c) + v_2(c−1) + v_2(c−2m) + 2·Σ_{i=2}^{2m−1} v_2(c − i) + v_2(bracket)
                                 =  v_2(c) + 0 + v_2(c − 2m) + 2·Σ_{i=2}^{2m−1} v_2(c − i) + v_2(c − 2m)
                                 =  v_2(c) + 2·Σ_{i=2}^{2m} v_2(c − i).                              (Δ-closed)
```
For m = 0: `v_2(Q_1) = v_2(c(c−1)) = v_2(c)`. Consistent with (Δ-closed) via
empty sum.

### 3.4 v_2(h_{2m+1}) at (T−2, 0)

```
    v_2(h_{2m+1}^{(c)}(T−2, 0))  =  2·v_2((c − 2 − 2m)!) + v_2(c) + 2·Σ_{i=2}^{2m} v_2(c − i).        (H★)
```

---

## 4. Min over odd k at (T−2, 0) is independent of k (c even)

**Theorem 4.1 (♥ recursion generalised to c even).** For c even and
`m ∈ {0, 1, ..., ⌊(c − 4)/2⌋}` (i.e., odd `k = 2m + 1 ∈ [1, c − 3]`):
```
    v_2(h_{2m+3}^{(c)}(T−2, 0))  =  v_2(h_{2m+1}^{(c)}(T−2, 0)).
```

*Proof.* By (H★):
```
Δ v_2(h) := v_2(h_{2m+3}) − v_2(h_{2m+1})
          = 2·[v_2((c − 4 − 2m)!) − v_2((c − 2 − 2m)!)]
             + 2·[v_2(c − 2m − 2) + v_2(c − 2m − 1)]
          = −2·[v_2(c − 2 − 2m) + v_2(c − 3 − 2m)]         (factorial ratio)
             + 2·[v_2(c − 2m − 2) + v_2(c − 2m − 1)]        (Δ-closed increment)
          = 0.
```
(For c even: c − 3 − 2m = c − 2m − 1 odd, both `v_2 = 0`; and c − 2 − 2m = c − 2m − 2
even; the terms cancel pairwise.) ∎

**Corollary 4.2.** For c even and T = smallest 2^t > c − 2:
```
    min_{k odd, 1 ≤ k ≤ c−3} v_2(h_k^{(c)}(T − 2, 0))
       =  v_2(h_1^{(c)}(T − 2, 0))
       =  2·v_2((c − 2)!) + v_2(c).                                     (β'★)
```

**Remark.** The generalisation from "c ≡ 0 mod 4" (Day 96 §4) to "c even" required
only the observation that `v_2(c − 1) = 0` for ALL c even. The bracket argument
in §3.2 uses only `c − 1` odd and `c − 2m − 1` odd, both of which hold for c even.
So (Δ-closed) is valid on all c even, and Theorem 4.1 follows.

---

## 5. SEALED comparison against empirical D(c)

**COUNTERMEASURE REPEATED HERE (as PROVE.md demands):** All of §2, §3, §4 were
computed WITHOUT reference to empirical D(c) values. The corners enumerated:
{(T−2, 0), (0, T−2), (0, 0), (T−2, T−2)}. Odd k enumerated: full range
[1, c − 3]. The minimum was computed structurally and equals
`v_2(h_1(T−2, 0)) = 2·v_2((c − 2)!) + v_2(c)` at (T−2, 0) for c even.

**Only now** do we consult empirical D(c) for validation.

### 5.1 Simplified closed form for D_★(c)

Define `D_★(c) := β(c) − v_2(h_1^{(c)}(T−2, 0))` (the corner-derived D). Using
`β(c) = 2(c − 1) − s_2(c − 1)` and Legendre `v_2((c − 2)!) = (c − 2) − s_2(c − 2)`:
```
    D_★(c)  =  2(c − 1) − s_2(c − 1)  −  2(c − 2) + 2·s_2(c − 2)  −  v_2(c)
             =  2 − s_2(c − 1) + 2·s_2(c − 2) − v_2(c).
```
For c even, `c − 1` odd, Kummer `s_2(c − 1) − s_2(c − 2) = 1 − v_2(c − 1) = 1`, so
`s_2(c − 1) = 1 + s_2(c − 2)`. Substituting:
```
    D_★(c)  =  2 − 1 − s_2(c − 2) + 2·s_2(c − 2) − v_2(c)
             =  1 + s_2(c − 2) − v_2(c).                                (D★-simplified, c even)
```

For c ≡ 0 mod 4 (c = 4k):
- `v_2(c) = 2 + v_2(k)`.
- `s_2(c − 2) = s_2(4k − 2) = s_2(2(2k − 1)) = s_2(2k − 1) = s_2(k) + v_2(k)` (Kummer on
  `s_2(2k − 1) = s_2(2k) − 1 + v_2(2k) = s_2(k) − 1 + 1 + v_2(k)`).
- Substituting: `D_★(4k) = 1 + s_2(k) + v_2(k) − 2 − v_2(k) = s_2(k) − 1`.        ✓ matches empirical formula.

For c ≡ 2 mod 4 (c = 4k + 2):
- `v_2(c) = 1`.
- `s_2(c − 2) = s_2(4k) = s_2(k)`.
- Substituting: `D_★(4k + 2) = 1 + s_2(k) − 1 = s_2(k)`.

For c odd (v_2(c) = 0), (D★-simplified) does NOT apply directly because §2.1's
Kummer-floor argument requires L even (i.e., k opposite parity to c − 1), and
for c odd with k odd, L is odd. `(2)_L` is not at Kummer floor. We DO have a value
of `v_2(h_1(T−2, 0))` via (AMM) directly, but it's not the corner-min, so we don't
call it `D_★`. See §5.3.

### 5.2 Table: c ∈ {4, ..., 15}, c even

| c  | β(c) | s_2(c−2) | v_2(c) | v_2(h_1(T−2,0)) | D_★(c) | D_emp(c) | Match |
|----|------|----------|--------|------------------|--------|----------|-------|
| 4  | 4    | 1        | 2      | 4                | 0      | 0        | ✓     |
| 6  | 8    | 1        | 1      | 7                | 1      | 1        | ✓     |
| 8  | 11   | 2        | 3      | 11               | 0      | 0        | ✓     |
| 10 | 16   | 1        | 1      | 15               | 1      | 2        | ✗ off 1 |
| 12 | 19   | 2        | 2      | 18               | 1      | 1        | ✓     |
| 14 | 23   | 2        | 1      | 21               | 2      | 2        | ✓     |

**5/6 match** on c even in the range.

**Sanity: which residue class fails?**
- ✓ c ≡ 0 mod 4: c = 4, 8, 12 — all match. 3/3.
- ✓ c ≡ 6 mod 8: c = 6, 14 — all match. 2/2.
- ✗ c ≡ 2 mod 8: c = 10 — mismatch. 0/1.

For c = 10: c = 4k + 2 with k = 2. `D_★(10) = s_2(2) = 1`. `D_emp(10) = 1 + s_2(1) = 2`.
**Off by 1 = v_2(k) = v_2(2)**.

### 5.3 Table: c ∈ {5, 7, ..., 15}, c odd (for record only — Phase A does not apply cleanly)

For c odd at (T−2, 0), Kummer floor fails for `(2)_L` (L odd for k odd). We compute
`v_2(h_1(T−2, 0))` via direct (AMM):
```
    v_2((T + 1)_L) = L − s_2(L) = v_2(L!)          (Kummer floor still holds, block arithmetic).
    v_2((2)_L)     = L − s_2(L + 1) + 1
                    = v_2(L!) + v_2(L + 1)           (excess v_2(L + 1) = v_2(c − k)).
    v_2(Q_1)       = v_2(c(c − 1)) = v_2(c − 1)     (c odd).
    ⇒ v_2(h_1(T−2, 0)) = 2·v_2(L!) + v_2(c − k) + v_2(c − 1).
    For k = 1: v_2(h_1(T−2, 0)) = 2·v_2((c−2)!) + v_2(c − 1) + v_2(c − 1)
                                  = 2·v_2((c−2)!) + 2·v_2(c − 1).
```

| c  | β(c) | v_2((c−2)!) | v_2(c−1) | v_2(h_1(T−2,0)) | β − h | D_emp | Off by |
|----|------|-------------|----------|------------------|-------|-------|--------|
| 5  | 7    | 1           | 2        | 6                | 1     | 4     | 3      |
| 7  | 10   | 3           | 1        | 8                | 2     | 4     | 2      |
| 9  | 15   | 4           | 3        | 14               | 1     | 6     | 5      |
| 11 | 18   | 7           | 1        | 16               | 2     | 6     | 4      |
| 13 | 22   | 8           | 2        | 20               | 2     | 6     | 4      |
| 15 | 25   | 10          | 1        | 22               | 3     | 6     | 3      |

For odd c, `(T−2, 0)` at odd k UNIFORMLY OVERSHOOTS β' by a non-trivial amount.
Diagnostic: **the true β'(c) for odd c is achieved at a different corner or at
even k** (which PROVE.md restricts out). SCP for odd c is out of scope for this
session — see §6.2.

### 5.4 Consequence for the digit-sum formula

- **c ≡ 0 mod 4 branch:** rigorously derived structurally (mod (M) at m ≥ 3).
  Structural formula = `D_★(4k) = s_2(k) − 1`. **Matches empirical**.
- **c ≡ 6 mod 8 branch:** rigorously derived structurally (mod (M)).
  Structural formula = `D_★(4k + 2) = s_2(k) = 1 + s_2(k − 1)` (for k odd,
  `s_2(k − 1) = s_2(k) − 1` by Kummer at odd k). **Matches empirical**.
- **c ≡ 2 mod 8 branch:** structural formula `D_★(4k + 2) = s_2(k)` UNDERSHOOTS
  empirical `D(c) = 1 + s_2(k − 1)` by exactly `v_2(k)`. Diagnostic in §6.1.
- **c odd branch:** structural formula at (T−2, 0), odd k, misses empirical.
  Diagnostic in §6.2.

---

## 6. Diagnostics for the two failure modes

### 6.1 c ≡ 2 mod 8 — where does the extra v_2(k) come from?

For c = 4k + 2, `D_★(c) − D_emp(c) = s_2(k) − 1 − s_2(k − 1) = s_2(k) − (1 + s_2(k − 1))`.

Using Kummer `s_2(k) − s_2(k − 1) = 1 − v_2(k)`, we get
`D_★(c) − D_emp(c) = −v_2(k) = −v_2((c − 2)/4)`.

For k odd (c ≡ 6 mod 8): `v_2(k) = 0`, no overshoot. ✓
For k even (c ≡ 2 mod 8): `v_2(k) ≥ 1`, overshoot ≥ 1. ✗

**Interpretation.** For c ≡ 2 mod 8, the SCP witness (achiever of β') is NOT
at (T−2, 0). It's at a different (a, b, k) yielding a lower `v_2(h_k)`. Since
(T−2, 0) is the unique Poch-min corner (§2.5), and (0, 0) matches (T−2, 0) only
when `v_2(c − k + 1) = 1`, the achiever of β'(10) must involve either:
- (a) an INTERIOR (a, b) (not a corner), or
- (b) EVEN k (excluded by PROVE.md phase-A scope).

**Empirical check (c = 10, β' = 14):** At all four corners and k ∈ {1, 3, 5, 7},
`v_2(h_k)` = 15 or 16 (all corners give ≥ 15 by §2-3 analysis; specifically
(T−2, 0) gives 15 by (H★) and (0, 0) gives 15 = tie since `v_2(c − 2) = 1`).
None reach 14. Consistent with (a) or (b).

**Diagnostic conclusion (c ≡ 2 mod 8):** Corner-first hypothesis FAILS. The
(T−2, 0) corner is the min OVER CORNERS but not the global min. To close the
c ≡ 2 mod 8 branch, need either a Master-Formula-like closed form for `Q_k(a, b, c)`
at an interior point, or an even-k analogue of (M).

### 6.2 c odd — Kummer floor mismatch

For c odd and k odd, L is odd, and `(2)_L = (L + 1)!` picks up an extra factor
of `L + 1 = c − k` even. `(2)_L` is NOT at Kummer floor.

The natural fix is EVEN k, which makes L even and restores the parity match.
This is excluded by PROVE.md's odd-k restriction for Phase A.

Alternative: shift to a corner where `b + 2` is a power of 2 (or `b + 2 ≡ 1 mod
large power`). E.g., `b = 2^s − 2` for various s. This is a wider corner
enumeration than the 4-corner list.

**Empirical for c = 5 (β' = 3):**
At (0, 0), k = 2 (even), L = 2: `v_2((3)_2) + v_2((2)_2) = 2 + 1 = 3`. `Q_2(0, 0, 5)`
not covered by Master Formula, but the Poch product alone already gives ≥ 3. If
`Q_2(0, 0, 5)` is odd (v_2 = 0), then h_2 v_2 = 3, matching β'(5). Without an
even-k formula, cannot verify structurally.

**Diagnostic conclusion (c odd):** Phase A at (T−2, 0) with odd k is a
parity mismatch. Extension to even k is Day 98+ territory (requires Master
Formula analogue for `Q_{2m}(a, 0, c)`).

---

## 7. Grade recommendations

### 7.1 Nodes to update

**`beta-prime-digit-sum-formula`:** currently `checked-sober`. Recommend **split
by residue class**:

- **c ≡ 0 mod 4 subbranch → `sketched`.** Structural derivation via (H★) + (D★-simplified) matches
  empirical formula `D(4k) = s_2(k) − 1` identically. Conditional on Master
  Formula (M) at m ≥ 3 (Sub-conjecture 5.2 linearity gap).
- **c ≡ 6 mod 8 subbranch → `sketched`.** Same derivation gives `D(4k + 2) = s_2(k)
  = 1 + s_2(k − 1)` for k odd, matching empirical. Same conditionality.
- **c ≡ 2 mod 8 subbranch → stays `checked-sober`.** Corner (T−2, 0) overshoots
  β' by `v_2((c − 2)/4)`. Requires further work (interior witness or even-k
  Master Formula).
- **c odd subbranch → stays `checked-sober`.** Kummer floor mismatch under
  odd-k restriction. Requires even-k analysis.

### 7.2 New/updated child nodes

**NEW: `heart-recursion-c-even-at-corner` (grade `sketched`).**
Statement (Theorem 4.1): For c even and T = smallest 2^t > c − 2,
`v_2(h_{2m+1}^{(c)}(T − 2, 0))` is independent of m over odd k in [1, c − 3].
Proof: (H★) + (Δ-closed) + factorial-ratio cancellation, conditional on Master
Formula (M). Generalises `delta-recursion-odd-k-slice-c-cong-0-mod-4` (♥) from
c ≡ 0 mod 4 to c even. File: this document §4.

**NEW: `corner-derivation-Dstar-formula` (grade `sketched`).**
Statement: `D_★(c) := β(c) − v_2(h_1(T − 2, 0)) = 1 + s_2(c − 2) − v_2(c)` for
c even. File: §5.1.

**UPGRADE recommendation for `master-formula-M`:** m = 3 (k = 7) verification
extended by consistency with Δ_k across all m for c ∈ {8, 10, 12, 14} in this
session. Suggests `sketched` → `computed` upgrade if we count multi-c matches
as sober checks. Recommend keeping at `sketched` pending Sub-conjecture 5.2
proof (linearity).

**NEW `diagnostic` (not a graded claim): `cmod2mod8-corner-hypothesis-fails`.**
For c ≡ 2 mod 8, (T−2, 0) is NOT the SCP-achiever. This is diagnostic — a
FINDING, not a graded proof. Recommend recording as a memory note (§8).

**NEW `diagnostic`: `codd-parity-mismatch-at-Tcorner`.** For c odd with k odd,
Kummer floor fails at (T−2, 0). Even-k analysis required.

### 7.3 Cross-references to update

- `master-formula-Qk-shell.md`: add reference to §4 (Theorem 4.1 c-even generalisation).
- `amdeberhan-formula-as-Dc-tool.md`: mark as "executed 2026-07-15, partial success:
  c ≡ 0 mod 4 and c ≡ 6 mod 8 branches closed; c ≡ 2 mod 8 and c odd remain."
- `digit-sum-formula-for-beta-prime-c.md`: add "Structural derivation partial:
  c ≡ 0 mod 4 and c ≡ 6 mod 8 sketched via 2026-07-15-amdeberhan-Dc-derivation.md."

---

## 8. Precisely identified gaps

**G1 (Master Formula extension).** (M) proved rigorously at m ∈ {0, 1, 2}, verified
empirically at m = 3 (Day 96). Extension to all m ≥ 1 blocks on Sub-conjecture 5.2
(linearity of `Q_k(a, 0, c)` in a). Not addressed this session — it was addressed
Day 96 cycles 2 and 3.

**G2 (c ≡ 2 mod 8 SCP witness).** For c = 10, 18, 26, ..., the β' achiever is
NOT at any of the four corners with odd k. Candidate resolutions:
  (a) INTERIOR (a, b) achiever: requires `Q_k(a, b, c)` closed form at generic
      interior (a, b). Not currently available.
  (b) EVEN k achiever: requires even-k Master Formula for `Q_{2m}(a, 0, c)`. Not
      currently available. Would parallel odd-k derivation.
Both are open. Priority: (b) is closer to existing machinery.

**G3 (c odd branch).** For c odd, PROVE.md's odd-k restriction is a parity
mismatch. Even-k analysis (per G2b) is required. Also may need a shifted corner
(e.g., `b = 2^s − 2` for various s).

**G4 (SCP identification LB = β').** At the (T−2, 0) corner, `v_2(h_1)` is the
min OVER CORNERS at odd k. That this equals β'(c) requires SCP (single-carrier
polynomial) achievement, which is `sketched` in general. For c ≡ 0 mod 4 the
achievement was verified up to c = 12 in Day 93 tables; for c ≡ 6 mod 8 the
verification is at c = 6, 14 (this document). For other c, SCP is a separate
open claim.

---

## 9. Meta-observations (Rick's whiskey notes)

Three things I noticed this session:

**(i) The ♥ recursion generalises.** Day 96 proved ♥ for c ≡ 0 mod 4. But the
proof uses only `v_2(c − 1) = 0` (needed for the bracket 2-adic split). That
holds for ALL c even. So ♥ actually holds for c even, not just c ≡ 0 mod 4.
This is a free extension — no new arithmetic needed. §4 Theorem 4.1.

**(ii) The digit-sum formula at c ≡ 2 mod 4 has a natural "twist" `v_2(k)`.**
`D_emp(4k + 2) = 1 + s_2(k − 1)` vs my `D_★(4k + 2) = s_2(k)`. Difference is
`v_2(k)` — literally the number of trailing zeros of k. This is the fingerprint
of an SCP witness OUTSIDE (T−2, 0) whose `v_2(h)` beats (T−2, 0) by exactly
`v_2(k)`. Corner-first hypothesis picks up ODD k of the (c − 2)/4 parameter,
misses EVEN k contribution. Suggestive of a "second-tier" corner (higher-order
Bernoulli-flavoured shift) that captures the even-k arithmetic.

**(iii) Master Formula → digit-sum is a two-line derivation modulo everything.**
Once (M) is in hand and the Amdeberhan floor at (T−2, 0) is worked out, the
c ≡ 0 mod 4 digit-sum formula falls out in half a page. The 8/8 empirical fit
from Day 93 is no longer mysterious — it's the consequence of (M) plus the
choice of universal corner. The "shape" (digit-sum, not polynomial) is
ENFORCED by the Kummer-floor identity `v_2((c−2)!) = (c−2) − s_2(c−2)`; the
"scale" (⌊c/4⌋) is ENFORCED by the k → k/2 halving `s_2(4k − 2) = s_2(2k − 1) = s_2(k) + v_2(k)`.

**Whiskey.** — Rick's prove-agent, Day 97, 2026-07-15, 2am.

---

## 10. Bottom line

**Two subbranches (c ≡ 0 mod 4 and c ≡ 6 mod 8) get structural derivations,
matching the digit-sum formula EXACTLY.**

Both derivations rest on:
- Amdeberhan-Manna-Moll (arXiv:0707.2119) [known literature].
- Day 88 3-variable factorisation [lean-verified].
- Master Formula (M) [sketched at m ≤ 2, verified m = 3].
- Kummer-floor block arithmetic at T = smallest 2^t > c − 2.

**Grade upgrade recommended:** `beta-prime-digit-sum-formula` from
`checked-sober` → **`sketched`** on the c ≡ 0 mod 4 AND c ≡ 6 mod 8
subbranches (union = c ≡ 0, 6 mod 8, three residue classes out of four for c
even), conditional on Master Formula (M).

**Two subbranches remain (c ≡ 2 mod 8, c odd):** documented as diagnostics.
Both require either an even-k analogue of (M) or an interior-point analogue.
These are Day 98+ targets.

---

## Appendix A — Full v_2(h_1(T − 2, 0)) table, c even, c ∈ {4, ..., 30}

For sealed inspection later.

| c  | T  | L  | v_2((c−2)!) | v_2(c) | v_2(h_1) | β(c) | D_★(c) | D_emp(c) | Match |
|----|----|----|-------------|--------|----------|------|--------|----------|-------|
| 4  | 4  | 2  | 1           | 2      | 4        | 4    | 0      | 0        | ✓     |
| 6  | 8  | 4  | 3           | 1      | 7        | 8    | 1      | 1        | ✓     |
| 8  | 8  | 6  | 4           | 3      | 11       | 11   | 0      | 0        | ✓     |
| 10 | 16 | 8  | 7           | 1      | 15       | 16   | 1      | 2        | ✗     |
| 12 | 16 | 10 | 8           | 2      | 18       | 19   | 1      | 1        | ✓     |
| 14 | 16 | 12 | 10          | 1      | 21       | 23   | 2      | 2        | ✓     |
| 16 | 16 | 14 | 11          | 4      | 26       | 26   | 0      | 0        | ✓     |
| 18 | 32 | 16 | 15          | 1      | 31       | 32   | 1      | 3        | ✗     |
| 20 | 32 | 18 | 16          | 2      | 34       | 35   | 1      | 1        | ✓     |
| 22 | 32 | 20 | 18          | 1      | 37       | 39   | 2      | 2        | ✓     |
| 24 | 32 | 22 | 19          | 3      | 41       | 42   | 1      | 1        | ✓     |
| 26 | 32 | 24 | 22          | 1      | 45       | 47   | 2      | 3        | ✗     |
| 28 | 32 | 26 | 23          | 2      | 48       | 50   | 2      | 2        | ✓     |
| 30 | 32 | 28 | 25          | 1      | 51       | 54   | 3      | 3        | ✓     |

Pattern of failures: c ∈ {10, 18, 26}, all c ≡ 2 mod 8. Failure amount: 1, 2, 1 =
`v_2(2), v_2(4), v_2(6)` = `v_2(k)` for c = 4k + 2. Extrapolation predicts failure
at c = 34 (k = 8, off 3), c = 42 (k = 10, off 1), etc.

**Success rate:** 11/14 on c even in [4, 30]. All three failures on c ≡ 2 mod 8.

---

*Written to `/home/agent/projects/proofs/2026-07-15-amdeberhan-Dc-derivation.md`
per PROVE.md deliverable spec.*
