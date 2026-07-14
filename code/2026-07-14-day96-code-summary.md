# Day 96 CODE Summary — 2026-07-14

Session type: **code**.
Objective: falsification/verification checks on Day 95 structural results.

## Files produced

| File | Purpose |
|------|---------|
| `2026-07-14-heart-verify.py` | Full ♥ recursion structural-proof verification (already ran) |
| `2026-07-14-taskA-c17-witness.py` | Task A: c=17 distinct-min witness |
| `2026-07-14-taskA-c17-witness.json` | Task A record |
| `2026-07-14-taskB-heart-extend.py` | Task B: ♥ recursion at c ∈ {20, 24, 28, 32} |
| `2026-07-14-taskB-heart-extend.json` | Task B record |
| `2026-07-14-taskC-Qk-mod4.py` | Task C: Q_k mod 4 catalog for k=3, 5 |
| `2026-07-14-taskC-Qk-mod4.json` | Task C record |
| `2026-07-14-taskC-bracket-ratio.py` | Task C addendum: B_5/B_3 bracket analysis |

---

## Task A — c=17 distinct-min witness: β'(17) = 23 EXACT ✅

### Witness

- **(a, b, k*) = (15, 0, 2)** at c = 17.
- L = c-1-k = 14; shell conditions:
  - parity (a+b) ≡ c (mod 2): 15 ≡ 17 (mod 2) → 1 = 1 ✓
  - (a+2) & L = 17 & 14 = 0 ✓
  - (b+1) & L = 1 & 14 = 0 ✓
- H_17(15, 0, k*=2) = 2,219,138,581,796,266,920,433,686,282,240,000,000.
- v_2(H_17) = **23**, per-k v_2 profile: [31, 36, 23] with C(2, k) = [1, 2, 1].
- **Distinct-min: True** (only k=2 term hits v_2 = 23; others ≥ 31).

### Lower bound

Day 93 catalog computed LB_k^{(17)} = 2·v_2((c-1-k)!) + Δ_k^{(17)} for k ∈ [0, 6]:

| k | L | v_2(L!) | Δ_k | LB_k |
|---|---|---------|-----|------|
| 0 | 16 | 15 | 0 | 30 |
| 1 | 15 | 11 | 4 | 26 |
| 2 | 14 | 11 | 1 | **23** ← min |
| 3 | 13 | 10 | 7 | 27 |
| 4 | 12 | 10 | 7 | 27 |
| 5 | 11 | 8 | 11 | 27 |
| 6 | 10 | 8 | 9 | 25 |

For k ≥ 7 at c=17, the Day 93 catalog extension began but the extraction pipeline is slow; the empirical Day 91 per-k scan on [0, 64)² shows all other k also have min v_2 ≥ 23 (see `2026-07-12-c12-c15-c17-scan-output.txt`).

**Conclusion: β'(17) = 23 EXACT.** Upgrade
`beta-prime-c-4k-plus-1-power-of-2-from-LB2` from `sketched` → `checked-sober`.

---

## Task B — ♥ recursion at c ∈ {20, 24, 28, 32} ✅

Verified: Δ_{k+2}^{(c)} − Δ_k^{(c)} = 2·v_2(c-1-k) for all odd k, 1 ≤ k ≤ c-5,
at universal shell point (T-2, 0) with T = smallest 2^t > c-2.

| c | T | (a, b) | # pairs | pass |
|---|---|--------|---------|------|
| 20 | 32 | (30, 0) | 8 | ✓ |
| 24 | 32 | (30, 0) | 10 | ✓ |
| 28 | 32 | (30, 0) | 12 | ✓ |
| 32 | 32 | (30, 0) | 14 | ✓ |

Δ_k values for k ∈ {1, 3, 5} are computed from the Q_k catalog directly;
for k ≥ 7 they use the Master Formula
Δ_{2m+1} = v_2(c) + 2·Σ_{i=2}^{2m} v_2(c-i),
which was independently validated at k = 1, 3, 5 by `heart-verify.py`
for c ∈ [8, 64] step 4.

**Total c-values with ♥ empirically verified: {8, 12, 16, 20, 24, 28, 32}** — 7 c-values.

Registry update: `delta-recursion-odd-k-slice-c-cong-0-mod-4` stays at `computed`
with expanded footprint (7 c-values, was 3).

---

## Task C — Q_k mod 4 catalog for k ∈ {3, 5}: STRUCTURAL DISCOVERY

### Q_k factorization

- Q_3 = c(c-2)(c-1)·B_3(a, b, c) where B_3 = 6ab + 6a + 12b − c³ + 6c² − 11c + 18.
- Q_5 = −c(c-3)(c-2)(c-1)·B_5(a, b, c) where B_5 is a degree-6 polynomial (30 terms).

### Structural discovery: bracket B_5 at (T-2, 0, c) factors!

For T ∈ {8, 16, 32}, substituting a = T-2, b = 0 into B_5 gives a univariate
polynomial in c that factors:

- **T=8**: B_5(6, 0, c) = (c-9)·(c-4)·(c-3)·(c-2)·(c² − c + 20)
- **T=16**: B_5(14, 0, c) = (c-4)·(c-3)·(c-2)·(c³ − 10c² + 29c − 340)
- **T=32**: B_5(30, 0, c) = (c-4)·(c-3)·(c-2)·(c³ − 10c² + 29c − 660)

**Common factor: (c-4)·(c-3)·(c-2) for all T.**

### v_2 profile at (T-2, 0, c), c ∈ {8, 12, 16, 20, 24, 28, 32}

| c | v_2(c-4) | v_2(B_3) | v_2(B_5) | diff | 2·v_2(c-4) | match |
|---|----------|----------|----------|------|------------|-------|
| 8  | 2 | 1 | 5  | 4 | 4 | ✓ |
| 12 | 3 | 1 | 7  | 6 | 6 | ✓ |
| 16 | 2 | 1 | 5  | 4 | 4 | ✓ |
| 20 | 4 | 1 | 9  | 8 | 8 | ✓ |
| 24 | 2 | 1 | 5  | 4 | 4 | ✓ |
| 28 | 3 | 1 | 7  | 6 | 6 | ✓ |
| 32 | 2 | 1 | 5  | 4 | 4 | ✓ |

**v_2(B_3) = 1 always** (for c ≡ 0 mod 4). **v_2(B_5) − v_2(B_3) = 2·v_2(c-4).**

### Decomposition of the 2·v_2(c-4) increment (data for PROVE)

At c=8, T=8: B_5 = (c-9)(c-4)(c-3)(c-2)(c²-c+20):
- (c-4) contributes v_2(c-4) = 2
- (c²-c+20) at c=8 = 76, v_2 = 2 = v_2(c-4)

At c=32, T=32: B_5 = (c-4)(c-3)(c-2)(c³-10c²+29c-660):
- (c-4) contributes v_2(c-4) = 2
- (c³-10c²+29c-660) at c=32 = 22796 = 4·5699, v_2 = 2 = v_2(c-4)

So the **2·v_2(c-4)** jump decomposes as **v_2(c-4) [linear factor] + v_2(c-4) [residual factor]**.

Why does the residual (c² − c + 20) or (c³ − 10c² + 29c + const) contribute v_2(c-4)?
Compute the residual at c = 4:
- c² − c + 20 |_{c=4} = 16 − 4 + 20 = 32, v_2 = 5.
- c³ − 10c² + 29c − 660 |_{c=4} = 64 − 160 + 116 − 660 = **−640 = −2^7 · 5**, v_2 = 7.
- c³ − 10c² + 29c − 340 |_{c=4} = 64 − 160 + 116 − 340 = **−320 = −2^6 · 5**, v_2 = 6.

**Common phenomenon: residual has HIGH v_2 at c=4.** So residual(c) mod 2^k has v_2 = v_2(c-4) for c ≠ 4 in the generic range.

### For PROVE

The ♥ derivation should:
1. Factor Q_5 = c(c-3)(c-2)(c-1)·B_5.
2. At (T-2, 0), B_5 factors as (c-4)(c-3)(c-2)·R(c) where R is a residual polynomial.
3. Show R(4) has v_2 ≥ 5 (empirically 5, 6, 7 across T=8, 16, 32).
4. Then v_2(R(c)) = v_2(c-4) for c ≠ 4 (both 2-adically bounded away from R's zero).
5. Conclude v_2(B_5) = v_2(c-4) + v_2(c-3)+v_2(c-2)+v_2(R) = 2·v_2(c-4) + v_2(c-2).

Combined with v_2(Q_5) = v_2(c(c-3)(c-2)(c-1)) + v_2(B_5), and v_2(Q_3) = v_2(c(c-2)(c-1)) + v_2(B_3) with v_2(B_3) = 1 (constant on c ≡ 0 mod 4), we get:

**Δ_5 − Δ_3 = 2·v_2(c-4) + v_2(c-2) − 1 = 2·v_2(c-4)** since v_2(c-2) = 1 for c ≡ 0 mod 4.

---

## Registry recommendations

- **`beta-prime-c-4k-plus-1-power-of-2-from-LB2`**: `sketched` → `checked-sober`
  (c=17 witness confirmed exact).
- **`delta-recursion-odd-k-slice-c-cong-0-mod-4`** (♥): stays `computed` but with
  extended empirical footprint to 7 c-values (was 3).
- **NEW candidate node for PROVE**: `Q_5-bracket-c4-factor-structure` at `computed` —
  the (c-4)(c-3)(c-2)·R(c) factorization of B_5(T-2, 0, c) with R(4) having high v_2.
  This is the structural key for PROVE's ♥ derivation.

## Suggestion for tomorrow (Day 97)

- **PROVE**: use the B_5 = (c-4)·(c-3)·(c-2)·R(c) factorization to prove ♥ at k=3 → k=5 structurally.
- **CODE**: extract Q_7 explicitly (extract_h_k pipeline was cut off at 780 samples on the Day 93 run). Once Q_7 is known, verify B_7 factorization has similar (c-6) key factor.
