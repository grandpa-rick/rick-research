# Day 99 PROVE — G1: SCP single-carrier at (0, 2, j=4) for c ≡ 2 mod 4

**Date:** 2026-07-16
**Author:** Rick's prove-agent
**Prior:** `2026-07-16-c-cong-2-mod-8-interior-anchor.md` (Day 98) closed the
interior anchor derivation modulo G1 (single-carrier SCP), G2 (Theorem 4.1
analogue), G3 (matching lower bound), G4 (c odd branch).
**Target gap:** G1 — c-uniform structural proof that at (a, b) = (0, 2),
j = 4, the min-carrier is UNIQUELY at k = 4 for all c ≡ 2 mod 4 with c ≥ 6.
**Novelty:** medium — the technique is the same Q_j catalog + AMM Kummer
floor calculation as Day 98, but now applied to k ∈ {0, 1, 2, 3} to close
the strict-inequality side of the SCP argument.

---

## 0. Executive summary — what this session buys

**Headline result (G1 CLOSED).** For every c ≡ 2 mod 4 with c ≥ 6, at
(a, b) = (0, 2), j = 4:
```
    v_2(C(4, k) · h_k^{(c)}(0, 2))  >  v_2(h_4^{(c)}(0, 2))     for all k ∈ {0, 1, 2, 3}.   (♦)
```

Consequently, by the distinct-min sum rule, the sum
`H_c(0, 2, 4) = Σ_{k=0}^{4} C(4, k) · h_k^{(c)}(0, 2)` has
```
    v_2(H_c(0, 2, 4))  =  v_2(h_4^{(c)}(0, 2))  =  β(c) − D_anchor(c)
```
where `D_anchor(c) = s_2(m) + v_2(m)`, m = (c − 2)/4. Combined with Day 98
Theorem 2.3, this UNCONDITIONALLY gives the structural upper bound
```
    β'(c)  ≤  β(c) − (s_2(m) + v_2(m))  =  β(c) − (1 + s_2(m − 1)).
```

**Strict margins proved.** Explicitly (Δ_k := v_2(C(4, k) h_k) − v_2(h_4)):
- Δ_0 = 1 + v_2(m) + v_2(m + 1)      ≥ 2.
- Δ_1 = 2 + v_2(m)                    ≥ 2.
- Δ_2 = v_2(Q_2(0, 2, 4m+2)) + v_2(m) − 1  ≥ 3.
- Δ_3 = v_2(Q_3(0, 2, 4m+2)) + v_2(m) − 1  ≥ 5.

Numerical verification (§4.5): all closed forms match for m ∈ {1, ..., 50}
(250 h_k values, 200 Δ values).

**Circularity check.** The Q_j(0, 2, c) closed forms are pulled from the
Q_k catalog (Day 88/89, `checked-sober`). AMM Pochhammer valuations
(arXiv:0707.2119) are cited external. The comparison is structural at every
step — no empirical D(c) is consulted. Numerical verification is done
against Q_k catalog directly (not against β'(c)).

**Registry recommendation (§6).**
- `interior-anchor-02-unified-c-cong-2-mod-4`: `sketched` → **`sketched-with-G1-closed`**
  (upgrade). Full `proved` requires G2 (Theorem 4.1 analogue at k ∈ {5, 6})
  and G3 (matching LB extension). G1 is now closed.
- **NEW node:** `scp-single-carrier-at-02-j4` grade `proved`. Contents:
  Lemmas 2.1, 2.2, 2.3 of this document and §4 case analysis.

---

## 1. Setup

**Day 88 three-variable factorisation** (`lean-verified`):
```
    h_k^{(c)}(a, b)  =  (a + 3)_L · (b + 2)_L · Q_k(a, b, c),           L := c − 1 − k.
```

**Amdeberhan-Manna-Moll** (`arXiv:0707.2119`). For every integer a ≥ 1
and k ≥ 0:
```
    v_2((a)_k)  =  k − s_2(a + k − 1) + s_2(a − 1).                     (AMM)
```

**Q_k catalog** (Day 88/89, source: `code/2026-07-11-Qk-catalog.json`):
```
    Q_0(a, b, c)  =  1
    Q_1(a, b, c)  =  −c(c − 1)
    Q_2(a, b, c)  =  −c(2ab + 2a + 4b − c³ + 4c² − 5c + 6)
    Q_3(a, b, c)  =  c(c − 2)(c − 1)(6ab + 6a + 12b − c³ + 6c² − 11c + 18)
    Q_4(a, b, c)  =  c(c − 1)(12a²b² + 12a²b + 36ab² − 12abc³ + 84abc²
                                − 192abc + 180ab − 12ac³ + 84ac² − 192ac
                                + 144a + 24b² − 24bc³ + 168bc² − 384bc
                                + 312b + c⁶ − 15c⁵ + 91c⁴ − 309c³
                                + 652c² − 804c + 432).
```

**Distinct-min sum rule** (elementary, `proved`): if
`v_1, ..., v_r` are the 2-adic valuations of `x_1, ..., x_r ∈ Z`, and
the minimum `v = min_i v_i` is attained at exactly one index i*, then
`v_2(Σ x_i) = v`.

**Sum expansion at j = 4.** Since C(4, k) = 0 for k > 4:
```
    H_c(a, b, 4)  =  Σ_{k=0}^{4} C(4, k) · h_k^{(c)}(a, b)
                  =  h_0 + 4 h_1 + 6 h_2 + 4 h_3 + h_4.                 (H₄)
```

The 2-adic prefactors have v_2 in the pattern (0, 2, 1, 2, 0).

**What we need to prove.** For c = 4m + 2 with m ≥ 1:
```
    v_2(C(4, k) · h_k^{(c)}(0, 2))  >  v_2(h_4^{(c)}(0, 2))    for k ∈ {0, 1, 2, 3}.  (♦_k)
```
By the distinct-min sum rule, (♦) implies `v_2(H_c(0, 2, 4)) = v_2(h_4^{(c)}(0, 2))`.

---

## 2. Q_j(0, 2, 4m+2) closed forms (j = 0..4)

Substitution `a = 0, b = 2` into the catalog Q_k, then `c = 4m + 2`. All
computations are direct polynomial substitutions, verified in
`code/2026-07-16-day99-Qj-at-02.py`.

### 2.1 Q_j(0, 2, c) as polynomials in c

Direct evaluation (§Appendix A):
```
    Q_0(0, 2, c)  =  1
    Q_1(0, 2, c)  =  −c(c − 1)
    Q_2(0, 2, c)  =  c · (c³ − 4c² + 5c − 14)
    Q_3(0, 2, c)  =  −c(c − 2)(c − 1)(c³ − 6c² + 11c − 42)
    Q_4(0, 2, c)  =  c(c − 1) · R_4(c)                    [R_4 as in Day 98]
```

### 2.2 Substitution c = 4m + 2 and 2-adic factorisation

```
    Q_1(0, 2, 4m+2)  =  −2 · (2m + 1) · (4m + 1).                       (Q_1♠)
    Q_2(0, 2, 4m+2)  =  8 · (2m + 1) · P_2(m),   P_2(m) := 16m³+8m²+m−3.   (Q_2♠)
    Q_3(0, 2, 4m+2)  =  −32 · m · (2m + 1) · (4m + 1) · P_3(m),
                                 P_3(m) := 16m³ − m − 9.                  (Q_3♠)
    Q_4(0, 2, 4m+2)  =  32 · (2m + 1) · (4m + 1) · R(m),
                                 R(m) := 256m⁶−192m⁵+16m⁴−276m³+70m²+9.   (Q_4♠)
```

*Verification.* Direct sympy expansion in
`code/2026-07-16-day99-Qj-at-02.py`. The 2-adic factorisations
(Q_1♠)–(Q_4♠) are `factor()` output.

### 2.3 v_2 constants

**Lemma 2.1 (P_2 mod 2).** For every m ≥ 0, `P_2(m) ≡ m + 1 (mod 2)`.

*Proof.* `P_2(m) = 16m³ + 8m² + m − 3`. Mod 2, only the linear and constant
terms survive: `m − 3 ≡ m + 1 (mod 2)`. □

**Lemma 2.2 (P_3 mod 2).** For every m ≥ 0, `P_3(m) ≡ m + 1 (mod 2)`.

*Proof.* `P_3(m) = 16m³ − m − 9`. Mod 2, `−m − 9 ≡ m + 1 (mod 2)`. □

**Lemma 2.3 (R mod 2).** For every m ≥ 0, `R(m) ≡ 1 (mod 2)`.

*Proof.* `R(m) = 256m⁶ − 192m⁵ + 16m⁴ − 276m³ + 70m² + 9`. All coefficients
except the constant term are even. Constant term is 9. So `R(m) ≡ 9 ≡ 1 (mod 2)`. □

**Corollary (v_2 of Q_j at anchor).** For every m ≥ 1:
- `v_2(Q_0(0, 2, 4m+2)) = 0`.
- `v_2(Q_1(0, 2, 4m+2)) = 1`.   (2 · odd · odd)
- `v_2(Q_2(0, 2, 4m+2)) = 3 + v_2(P_2(m))`,
  where by Lemma 2.1, `v_2(P_2(m)) = 0` iff m even; `v_2(P_2(m)) ≥ 1` iff m odd.
- `v_2(Q_3(0, 2, 4m+2)) = 5 + v_2(m) + v_2(P_3(m))`,
  where by Lemma 2.2, `v_2(P_3(m)) = 0` iff m even; `v_2(P_3(m)) ≥ 1` iff m odd.
- `v_2(Q_4(0, 2, 4m+2)) = 5` c-uniformly, by Lemma 2.3.

---

## 3. AMM Kummer floors for (3)_L and (4)_L at L = 4m + 1 − k

For c = 4m + 2 and k ∈ {0, 1, 2, 3, 4}, `L_k := c − 1 − k = 4m + 1 − k`.
Applying (AMM):
```
    v_2((3)_{L_k})  =  L_k − s_2(L_k + 2) + s_2(2)  =  L_k − s_2(L_k + 2) + 1.
    v_2((4)_{L_k})  =  L_k − s_2(L_k + 3) + s_2(3)  =  L_k − s_2(L_k + 3) + 2.
```

Total contribution:
```
    v_2((3)_{L_k}) + v_2((4)_{L_k})  =  2·L_k + 3 − s_2(L_k + 2) − s_2(L_k + 3).   (Poch_k)
```

### 3.1 s_2 auxiliary identities at c = 4m + 2

For every m ≥ 0:
- `s_2(4m) = s_2(m)`               (leading zero-block; digits of m shifted 2 places).
- `s_2(4m + 1) = s_2(m) + 1`.
- `s_2(4m + 2) = s_2(m) + 1`.
- `s_2(4m + 3) = s_2(m) + 2`.
- `s_2(4m − 1) = s_2(m) + v_2(m) + 1`   for m ≥ 1.

*Proofs.* The first four are immediate — 4m in binary is m shifted left by
2 bits, so adding 1, 2, or 3 fills the low bits without carry. The last
follows from the Kummer identity `s_2(n) − s_2(n + 1) = v_2(n + 1) − 1`
applied to n = 4m − 1:
`s_2(4m − 1) = s_2(4m) + v_2(4m) − 1 = s_2(m) + (2 + v_2(m)) − 1 = s_2(m) + v_2(m) + 1`. □

### 3.2 Per-k Pochhammer sum

Apply (Poch_k) for k = 0, 1, 2, 3, 4. The arguments L_k + 2 and L_k + 3
are consecutive integers.

**k = 0:** L_0 = 4m + 1, L_0 + 2 = 4m + 3, L_0 + 3 = 4m + 4 = 4(m + 1).
- s_2(4m + 3) = s_2(m) + 2.
- s_2(4(m + 1)) = s_2(m + 1).
- Poch_0 = 2(4m+1) + 3 − (s_2(m) + 2) − s_2(m+1) = 8m + 3 − s_2(m) − s_2(m+1).

**k = 1:** L_1 = 4m, L_1 + 2 = 4m + 2, L_1 + 3 = 4m + 3.
- s_2(4m + 2) = s_2(m) + 1.
- s_2(4m + 3) = s_2(m) + 2.
- Poch_1 = 2·4m + 3 − (s_2(m) + 1) − (s_2(m) + 2) = 8m − 2·s_2(m).

**k = 2:** L_2 = 4m − 1, L_2 + 2 = 4m + 1, L_2 + 3 = 4m + 2.
- s_2(4m + 1) = s_2(m) + 1.
- s_2(4m + 2) = s_2(m) + 1.
- Poch_2 = 2(4m−1) + 3 − (s_2(m) + 1) − (s_2(m) + 1) = 8m − 1 − 2·s_2(m).

**k = 3:** L_3 = 4m − 2, L_3 + 2 = 4m, L_3 + 3 = 4m + 1.
- s_2(4m) = s_2(m).
- s_2(4m + 1) = s_2(m) + 1.
- Poch_3 = 2(4m−2) + 3 − s_2(m) − (s_2(m) + 1) = 8m − 2 − 2·s_2(m).

**k = 4:** L_4 = 4m − 3, L_4 + 2 = 4m − 1, L_4 + 3 = 4m.
- s_2(4m − 1) = s_2(m) + v_2(m) + 1  (needs m ≥ 1).
- s_2(4m) = s_2(m).
- Poch_4 = 2(4m−3) + 3 − (s_2(m) + v_2(m) + 1) − s_2(m) = 8m − 4 − 2·s_2(m) − v_2(m).

---

## 4. Closed forms for v_2(h_k(0, 2, 4m+2)) and case-by-case (♦_k)

Combining (Q_j♠) + (Poch_k):
```
    v_2(h_k^{(c)}(0, 2))  =  v_2(Q_k(0, 2, 4m+2)) + Poch_k.
```

### 4.1 k = 0

`v_2(h_0)  =  0 + (8m + 3 − s_2(m) − s_2(m + 1))  =  8m + 3 − s_2(m) − s_2(m + 1)`.

Recall `v_2(h_4)  =  5 + Poch_4  =  8m + 1 − 2·s_2(m) − v_2(m)`.

```
    Δ_0  :=  v_2(h_0) − v_2(h_4)   [since v_2(C(4,0)) = 0]
         =  (8m + 3 − s_2(m) − s_2(m + 1)) − (8m + 1 − 2·s_2(m) − v_2(m))
         =  2 + s_2(m) − s_2(m + 1) + v_2(m).
```

Using Kummer `s_2(m + 1) − s_2(m) = 1 − v_2(m + 1)`:
```
    Δ_0  =  1 + v_2(m) + v_2(m + 1).                                          (Δ₀)
```

Since m and m + 1 are consecutive integers, exactly one is even, so
`v_2(m) + v_2(m + 1) ≥ 1`. Hence **Δ_0 ≥ 2 > 0**. ✓

### 4.2 k = 1

`v_2(h_1)  =  1 + (8m − 2·s_2(m))  =  8m + 1 − 2·s_2(m)`.

Interestingly this equals `v_2(h_4) + v_2(m)`. With `v_2(C(4, 1)) = 2`:
```
    Δ_1  =  2 + (8m + 1 − 2·s_2(m)) − (8m + 1 − 2·s_2(m) − v_2(m))
         =  2 + v_2(m).                                                       (Δ₁)
```

Since m ≥ 1, `v_2(m) ≥ 0`. Hence **Δ_1 ≥ 2 > 0**. ✓

### 4.3 k = 2

`v_2(h_2)  =  v_2(Q_2) + (8m − 1 − 2·s_2(m))`.

With `v_2(C(4, 2)) = 1`:
```
    Δ_2  =  1 + v_2(Q_2) + (8m − 1 − 2·s_2(m)) − (8m + 1 − 2·s_2(m) − v_2(m))
         =  v_2(Q_2) + v_2(m) − 1.                                            (Δ₂)
```

**Case m even (m ≥ 2).** By Lemma 2.1, `v_2(P_2(m)) = 0`, so `v_2(Q_2) = 3`.
Then `Δ_2 = 3 + v_2(m) − 1 = 2 + v_2(m) ≥ 3`  (since v_2(m) ≥ 1 for m even).

**Case m odd (m ≥ 1).** By Lemma 2.1, `v_2(P_2(m)) ≥ 1`, so `v_2(Q_2) ≥ 4`.
Then `Δ_2 ≥ 4 + 0 − 1 = 3`.

Hence **Δ_2 ≥ 3 > 0** uniformly in m ≥ 1. ✓

### 4.4 k = 3

`v_2(h_3)  =  v_2(Q_3) + (8m − 2 − 2·s_2(m))`.

With `v_2(C(4, 3)) = 2`:
```
    Δ_3  =  2 + v_2(Q_3) + (8m − 2 − 2·s_2(m)) − (8m + 1 − 2·s_2(m) − v_2(m))
         =  v_2(Q_3) + v_2(m) − 1.                                            (Δ₃)
```

**Case m even (m ≥ 2).** By Lemma 2.2, `v_2(P_3(m)) = 0`, so `v_2(Q_3) = 5 + v_2(m)`.
Then `Δ_3 = (5 + v_2(m)) + v_2(m) − 1 = 4 + 2·v_2(m) ≥ 6` (since v_2(m) ≥ 1).

**Case m odd (m ≥ 1).** By Lemma 2.2, `v_2(P_3(m)) ≥ 1`, so `v_2(Q_3) ≥ 6`.
Then `Δ_3 ≥ 6 + 0 − 1 = 5`.

Hence **Δ_3 ≥ 5 > 0** uniformly in m ≥ 1. ✓

### 4.5 Numerical verification

`code/2026-07-16-day99-scp-verify.py` checks the five closed forms
(§2.3 + §3.2) against direct computation of h_k^{(c)}(0, 2) via the
three-variable factorisation, for m ∈ {1, 2, ..., 50}. All 250 h_k
predictions match exactly. All 200 Δ_k values (for k = 0..3) match the
formulas (Δ₀)–(Δ₃), and all are ≥ 2 (with min Δ_0 = 2, Δ_1 = 2, Δ_2 = 3,
Δ_3 = 5 in the tested range — consistent with the case-analysis bounds).

**Sample values** (c ∈ {6, 10, 14, ..., 130}):

| m | c | Δ_0 | Δ_1 | Δ_2 | Δ_3 |
|---|----|-----|-----|-----|-----|
| 1 | 6  | 2   | 2   | 3   | 5   |
| 2 | 10 | 2   | 3   | 3   | 6   |
| 3 | 14 | 3   | 2   | 5   | 6   |
| 4 | 18 | 3   | 4   | 4   | 8   |
| 5 | 22 | 2   | 2   | 3   | 5   |
| 8 | 34 | 4   | 5   | 5   | 10  |
| 15| 62 | 5   | 2   | 4   | 7   |
| 32|130 | 6   | 7   | 7   | 14  |
| 50|202 | 2   | 3   | 3   | 6   |

All strict. All match closed-form predictions.

---

## 5. Corollaries

**Corollary 5.1 (single-carrier SCP at (0, 2, j=4)).** For every c ≡ 2 mod 4
with c ≥ 6, in the sum
`H_c(0, 2, 4) = h_0 + 4·h_1 + 6·h_2 + 4·h_3 + h_4`,
the term `h_4` has strictly smaller v_2 than any other. By the distinct-min
sum rule:
```
    v_2(H_c(0, 2, 4))  =  v_2(h_4^{(c)}(0, 2))  =  β(c) − (s_2(m) + v_2(m)).      (SCP-carrier)
```

**Corollary 5.2 (unconditional structural upper bound).** For every c ≡ 2 mod 4:
```
    β'(c)  ≤  β(c) − D_anchor(c),   D_anchor(c) := s_2(m) + v_2(m) = 1 + s_2(m − 1).   (UB)
```

*Proof.* By definition `β'(c) := min_{a, b, j} v_2(H_c(a, b, j))`. Taking
(a, b, j) = (0, 2, 4) and applying (SCP-carrier) gives the bound. □

This closes G1. Day 98's `sketched` interior anchor derivation now stands on
a `proved` SCP node.

---

## 6. Grade recommendations

### 6.1 Nodes to update

**Existing node `interior-anchor-02-unified-c-cong-2-mod-4`**
(from Day 98): `sketched` → **`sketched-with-G1-closed`**.

**NEW node `scp-single-carrier-at-02-j4`** grade `proved`.
- Statement: Corollary 5.1 (single-carrier SCP at (0, 2, j = 4)).
- Proof: §2 + §3 + §4 of this document.
- File: `proofs/2026-07-16-day99-G1-scp-single-carrier.md`.
- Rests on:
  - Q_k catalog at k ∈ {0, 1, 2, 3, 4} (Day 88/89, `checked-sober`).
  - AMM (arXiv:0707.2119, external `proved`).
  - Elementary Kummer-identity s_2 arithmetic (Day 87, `proved`).
  - Distinct-min sum rule (`proved` elementary).
- Sources for external: `arXiv:0707.2119` Amdeberhan-Manna-Moll,
  Proposition 1.2 (v_2 of Pochhammer).

**NEW node `P2-mod-2` grade `proved`** — Lemma 2.1: P_2(m) ≡ m + 1 mod 2.
**NEW node `P3-mod-2` grade `proved`** — Lemma 2.2: P_3(m) ≡ m + 1 mod 2.
**NEW node `R-mod-2` grade `proved`** — Lemma 2.3: R(m) ≡ 1 mod 2.
(All three by direct polynomial coefficient inspection.)

### 6.2 Registry effect on parent

With G1 closed, the derivation of `β'(c) ≤ β(c) − D_anchor(c)` is
structurally complete for c ≡ 2 mod 4. What remains for the full
identification `β'(c) = β(c) − D_anchor(c)`:
- **G2** (Theorem 4.1 analogue): `v_2(h_k(0, 2, c))` constancy for
  k ∈ {4, 5, 6} — needed only if we want (a, b, j) = (0, 2, 5 or 6) also.
  Not needed for the UB claim itself.
- **G3** (matching LB): `β'(c) ≥ β(c) − D_anchor(c)`. Independent of this
  session; still open past c = 11.
- **G4** (c odd): separate mechanism. Phase 2 below hunts the anchor.

---

## 7. Meta — Rick's whiskey notes

**(i) The clean split.** When I sat down I expected the k = 2 and k = 3
cases to fight — they're right next to k = 4 and their Q_k polynomials
look nasty. Turns out the Q_j(0, 2, 4m+2) factorisation splits into
(low-power-of-2 constant) · (2m + 1) · (4m + 1) · (P_j(m)), and the P_j's
have mod-2 pattern that FLIPS with m. Even m makes j = 2, 3 pick up
their v_2 from v_2(m); odd m makes P_j pick up v_2 from a hidden factor.
The two mechanisms conspire — the total v_2(Q_j) ≥ (fixed floor) + (v_2(m) OR extra bit).

**(ii) The margin is safety-net-generous.** Min Δ over j ∈ {0, 1, 2, 3}
is 2 (at Δ_0 or Δ_1 depending on m). That means the argument is stable
against small errors in the Q_k catalog (which is `checked-sober`, so
already trustworthy) — a one-bit slip anywhere still leaves margin > 0.

**(iii) The lemmas are one-liners.** Lemma 2.1, 2.2, 2.3 are trivial mod-2
reductions of polynomials with tiny constant terms. The heavy lifting is
NOT in the number theory — it's in getting the Q_k catalog RIGHT (Day 88
work). This is the pattern: **the hard part is the setup, the finish is
easy**. AMM does the Pochhammer floor; Kummer does the s_2 arithmetic;
we plug and chug.

**Whiskey.** — Rick's prove-agent, Day 99, 2026-07-16.

---

## 8. Bottom line

**G1 is CLOSED.** SCP single-carrier at (0, 2, j = 4) is `proved` for all
c ≡ 2 mod 4, c ≥ 6, via the four strict inequalities (Δ₀)–(Δ₃), each of
which is an elementary consequence of:
- Q_k(0, 2, 4m+2) closed forms (§2.2).
- P_2, P_3 mod-2 lemmas (§2.3).
- R mod-2 lemma (§2.3).
- AMM Pochhammer valuations (§3).
- Kummer s_2 identities at 4m + i (§3.1).

The Day 98 interior-anchor derivation now stands on a `proved` SCP node,
upgrading from `sketched` to `sketched-with-G1-closed`.

**Next targets** (Day 100+):
- **G3 (matching LB at c > 11)** — the last algebraic gap for
  `β'(c) = β(c) − D_anchor(c)` for c ≡ 2 mod 4.
- **G4 (c odd branch)** — Phase 2 sweep at c = 11, 13 below hunts the
  analogous interior anchor.

---

## Appendix A — Verification code

- `code/2026-07-16-day99-Qj-at-02.py` — Q_k(0, 2, 4m+2) symbolic
  substitution and 2-adic factorisation. Prints v_2 table for m ∈ {1..20}.
- `code/2026-07-16-day99-scp-verify.py` — verifies §2.3 + §3.2 + §4
  closed forms against direct h_k computation, m ∈ {1..50}. 250/250 h_k
  match, 200/200 Δ_k match, min Δ_k > 0.
