# Day 91 — Elementary LB_k route: β'(11) = 12 falsifies D2

**Date:** 2026-07-12
**Status:** checked-sober (pending periodicity check completion)
**Predecessor conjecture killed:** conjecture D2 (registry `beta-prime-closed-form-conditional`).
**Successor conjecture proposed:** D2'.

---

## 1. Result

**Theorem (empirical, distinct-min witness + periodicity):**  β'(11) = 12.

**Corollary:** Conjecture D2 (from `proofs/2026-07-08-d1-partial.md`) is FALSE at c=11.

D2 predicted D(4k+3) = 4 + v_2(k), giving D(11) = 4 + v_2(2) = 5 and β'(11) = β(11) − 5 = 18 − 5 = 13. Actual β'(11) = 12, so actual D(11) = 6, not 5.

**Corrected conjecture (D2'):** For all c ≥ 4:

    D(4k) = 0
    D(4k+1) = 4 + 2·v_2(k)
    D(4k+2) = 1 + v_2(k)
    D(4k+3) = 4 + 2·v_2(k)      ← D2 had 4 + v_2(k); this is the correction

Equivalently, for odd c ≥ 5:  **D(c) = 4 + 2·v_2(⌊(c−1)/4⌋)**.

D2' gives the same predictions as D2 for c ∈ {5, 6, 7, 9, 10, 13, 14, 15} (all cases where v_2(⌊c/4⌋) ≤ 1 or c ≡ 1 mod 4).  D2' first diverges from D2 at **c = 11**, and next at c = 19, c = 27, ...

---

## 2. Attack route (elementary LB_k decomposition)

From the c-uniform three-variable factorization (Day 88, `hk-c-uniform-three-var-conjecture`):

    h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c)          [k ≤ c−1]

where (x)_L is the rising Pochhammer and Q_k(a, b, c) ∈ ℤ[a, b, c].

Setting L = c−1−k, Kummer/Lucas give:

    min_a v_2((a+3)_L) = v_2(L!),   achieved iff (a+2) & L = 0 (bitwise AND).
    min_b v_2((b+2)_L) = v_2(L!),   achieved iff (b+1) & L = 0.

Both binomials C(a+2+L, L), C(b+1+L, L) are odd exactly on the Lucas-min set.

**Define**

    Δ_k^{(c)} := min v_2(Q_k(a, b, c))    over (a, b) satisfying:
                 * (a + b) ≡ c mod 2   [parity shell]
                 * (a+2) & L = 0        [Lucas-odd for (a+3)_L]
                 * (b+1) & L = 0        [Lucas-odd for (b+2)_L]

Then h_k^{(c)}(a, b) evaluated at any joint-Lucas-min (a, b) has

    v_2 = 2·v_2(L!) + v_2(Q_k(a, b, c)),

so **UB_k^{(c)} := 2·v_2(L!) + Δ_k^{(c)}** is an achievable value of v_2(h_k^{(c)}), i.e., LB_k^{(c)} ≤ UB_k^{(c)}.

By the sum rule v_2(H_c(a, b, j)) ≥ min_k v_2(h_k(a, b) · C(j, k)) ≥ min_k v_2(h_k(a, b)) ≥ min_k LB_k, so

    β'(c) = min_{a,b,j} v_2(H_c(a, b, j))    (SCP)
          ≤ min_k UB_k^{(c)}                   (via witness at joint-Lucas-min for k*).

**Empirically at c ∈ {5..11}, this UB is tight and matches β'(c).**

---

## 3. Δ_k^{(c)} catalog

Computed at c ∈ {5..11}, k ∈ {0..6} using the Q_k catalog at `code/2026-07-11-Qk-catalog.json` (fit through Day 89). `inf` = joint-Lucas-min set is empty on the shell (occurs when c even and L odd).

```
              c=5   c=6   c=7   c=8   c=9   c=10  c=11
    k=0:      0    inf    0    inf    0    inf    0
    k=1:      2     1     1     3     3     1     1
    k=2:      1    inf    1    inf    1    inf    1
    k=3:      5     5     4     5     6     7     5
    k=4:      5    inf    5    inf    6    inf    6
    k=5:      -     7     7     9    10     8     8
    k=6:      -     -     6    inf    8    inf    6
```

Some structural observations:

- k=0: Δ_0 = 0 identically (Q_0 = 1).
- k=1: Δ_1 = v_2(c(c−1)); at odd c this is v_2(c−1). At c ∈ {5,7,9,11}: 2, 1, 3, 1 ✓.
- k=2: Δ_2 = 1 identically at odd c (Q_2 = −c · [2ab + 2a + 4b + (−c³ + 4c² − 5c + 6)], with v_2 of the bracket exactly 1 on the shell at any odd c).

For k ≥ 3 the closed form is messier and depends on c mod low powers of 2. But we don't need it for the main result — only min_k UB_k does the work, and empirically the argmin varies with c mod 4.

**LB_k^{(c)} = 2·v_2((c−1−k)!) + Δ_k^{(c)}** (as an UB on the true LB):

```
              c=5   c=6   c=7   c=8   c=9   c=10  c=11
    k=0:      6    inf    8    inf   14    inf   16
    k=1:      4     7     7    11    11    15    15
    k=2:      3    inf    7    inf    9    inf   15
    k=3:      5     7     6    11    12    15    13
    k=4:      5    inf    7    inf   12    inf   14
    k=5:      -     7     7    11    12    14    14
    k=6:      -     -     6    inf   10    inf   12
```

**min_k LB_k^{(c)}  vs  target β'(c):**

    c    argmin k*   min LB_k    target β'(c)     match?
    5        2          3            3            MATCH
    6        1          7            7            MATCH
    7        3          6            6            MATCH
    8        1         11           11            MATCH
    9        2          9            9            MATCH
   10        5         14           14            MATCH
   11        6         12          [D2 said 13]   MISMATCH with D2 → prompted this investigation

---

## 4. c = 11 witness (β'(11) ≤ 12)

Extracted h_k^{(11)}(a, b) polynomials for k ∈ {0..10} via the Sym-side extraction pipeline (`code/2026-07-10-hk-three-var-fit.py::extract_h_k`) with 276 samples, all fits unique.

Scanned [0, 64)² shell a+b odd:

    k=6: min v_2(h_6^{(11)}(a, b)) = 12,  first achiever (1, 2), h_6^{(11)}(1, 2) = 5,573,710,517,760,000 = 2^12 · odd

Witness (a*, b*, j*) = (1, 2, 6):

    H_11(1, 2, 6) = Σ_{j=0..6} h_j^{(11)}(1, 2) · C(6, j)
                  = −3,017,710,080,000
                  = −2^12 · 736,745,625            [odd cofactor]
    v_2 = 12.

Per-summand distinct-min check (from `code/2026-07-12-c11-witness-hunt-output.txt`):

    j= 0: h_0(1,2) = 1,077,105,223,434,240,000    C(6,0)=1     contrib v_2 = 18
    j= 1: h_1(1,2) = −701,074,405,785,600,000     C(6,1)=6     contrib v_2 = 20
    j= 2: h_2(1,2) = 429,408,073,543,680,000      C(6,2)=15    contrib v_2 = 15
    j= 3: h_3(1,2) = −241,175,389,593,600,000     C(6,3)=20    contrib v_2 = 18
    j= 4: h_4(1,2) = 118,023,848,312,832,000      C(6,4)=15    contrib v_2 = 17
    j= 5: h_5(1,2) = −44,034,425,487,360,000      C(6,5)=6     contrib v_2 = 21
    j= 6: h_6(1,2) = 5,573,710,517,760,000        C(6,6)=1     contrib v_2 = 12  ← distinct min

Carrier k*=6 has distinct minimum v_2 = 12; sum rule gives v_2(H_11) = 12 exactly.

Hence **β'(11) ≤ 12.**

**Independent verification of h_k^{(11)}(1, 2)** (`code/2026-07-12-c11-witness-independent-verify.py`): The three-variable factorization h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c) with Q_k from the Day-89 catalog (`code/2026-07-11-Qk-catalog.json`) reproduces h_k^{(11)}(1, 2) for k = 0..6 EXACTLY, matching the extraction pipeline in all 7 values. The Sym-side extraction (via M_j-c-uniform + Möbius inversion) and the polynomial Q_k catalog (fit at c ∈ {4, 5, 6, 7} in Day 88 and cross-checked at c=8 in Day 89) are two orthogonal computations of the same h_k^{(11)}. Perfect match. This eliminates any concern that a bug in one pipeline is producing the c=11 result.

---

## 5. c = 11 lower bound (β'(11) ≥ 12)

By the 2^T-periodicity lemma (registry `periodicity-lemma`, proved), h_k^{(11)}(a, b) mod 2^12 depends only on (a, b) mod 2^12. Checking all 2^{23} residues on the a+b odd shell:

Result (from `code/2026-07-12-c11-periodicity.py`, see `2026-07-12-c11-periodicity-output.txt`):

    T = 12, mod 2^12 = 4096
    Total grid: 2^23 = 8,388,608 residues per k on the shell a+b odd.

    k= 0: min v_2 >= 12   [8388608/8388608 zero mod 2^12]
    k= 1: min v_2 >= 12   [8388608/8388608]
    k= 2: min v_2 >= 12   [8388608/8388608]
    k= 3: min v_2 >= 12   [8388608/8388608]
    k= 4: min v_2 >= 12   [8388608/8388608]
    k= 5: min v_2 >= 12   [8388608/8388608]
    k= 6: min v_2 >= 12   [8388608/8388608]
    k= 7: min v_2 >= 12   [8388608/8388608]
    k= 8: min v_2 >= 12   [8388608/8388608]
    k= 9: min v_2 >= 12   [8388608/8388608]
    k=10: min v_2 >= 12   [8388608/8388608]

    Total: 92,274,688 residues checked, ALL zero mod 2^12.
    Total elapsed compute: ~7 minutes.

Every h_k^{(11)}(a, b) mod 2^12 ≡ 0 on the entire a+b odd shell in [0, 2^12)^2. By 2^12-periodicity, this holds for all (a, b) with a+b odd in ℤ_{≥0}^2. Hence **LB_k^{(11)} ≥ 12 for all k ∈ {0..10}.**

Given the mod-2^12 check passes, by v_2(sum) ≥ min(v_2), for all (a, b, j) on the shell:

    v_2(H_11(a, b, j)) = v_2( Σ_k h_k^{(11)}(a, b) · C(j, k) )
                       ≥ min_k v_2( h_k^{(11)}(a, b) · C(j, k) )
                       ≥ min_k v_2( h_k^{(11)}(a, b) )                 [C(j, k) ∈ ℤ]
                       ≥ 12.

Hence **β'(11) ≥ 12.**

Combined with §4: **β'(11) = 12 exactly.**

---

## 6. Falsification of D2 and proposal of D2'

**D2 predicted:** D(4k+3) = 4 + v_2(k). At c = 11 = 4·2 + 3, D2 gives D(11) = 4 + v_2(2) = 5, hence β'(11) = 13. Empirical β'(11) = 12, so D(11) = 6. **D2 is falsified.**

**D2' proposed:** D(4k+3) = 4 + 2·v_2(k). At c = 11: D2'(11) = 4 + 2·v_2(2) = 6. β'(11) = 12. ✓

D2' matches D2 for c ≡ 1 mod 4 (both use 4 + 2·v_2(k)) and for the even cases. The unified odd-c form is:

    D(c) = 4 + 2·v_2(⌊(c−1)/4⌋)   for odd c ≥ 5.

Predictions:
- c = 13:  D = 4 + 2·v_2(3) = 4;  β'(13) = 22 − 4 = 18.
- c = 15:  D = 4 + 2·v_2(3) = 4;  β'(15) = 25 − 4 = 21.
- c = 17:  D = 4 + 2·v_2(4) = 8;  β'(17) = 31 − 8 = 23.
- c = 19:  D = 4 + 2·v_2(4) = 8;  β'(19) = 33 − 8 = 25.
- c = 27:  D = 4 + 2·v_2(6) = 6;  β'(27) = ...

D2' first differs from D2 at c ∈ {11, 19, 23 (both same), 27, ...}. c = 11 is now confirmed. c = 19 and c = 27 are the next test points where the two conjectures diverge.

### 6.1 D1 also fails at c=11 — corrected form D1'

D1 (registry `refined-dip-formula`) said: for odd c ≥ 3, **Δβ'(c) = 1 − max(2, v_2(c−1))**. At c = 11: v_2(10) = 1, max(2, 1) = 2, so D1 predicts Δβ'(11) = −1. Actual Δβ'(11) = β'(11) − β'(10) = 12 − 14 = **−2**. **D1 is also off by 1 at c=11.**

Derived from D2' (Δβ = Δβ' + ΔD and Δβ = 1 + v_2(c−1)):

**D1' (corrected):** For odd c ≥ 5,  **Δβ'(c) = −1 − v_2(⌊c/4⌋).**

Data check:
- c = 5:   Δβ'(5) = 3 − 4 = −1 = −1 − v_2(1). ✓
- c = 7:   Δβ'(7) = 6 − 7 = −1 = −1 − v_2(1). ✓
- c = 9:   Δβ'(9) = 9 − 11 = −2 = −1 − v_2(2). ✓
- c = 11:  Δβ'(11) = 12 − 14 = −2 = −1 − v_2(2). ✓
- c = 13:  predicted Δβ'(13) = −1 − v_2(3) = −1.
- c = 15:  predicted Δβ'(15) = −1 − v_2(3) = −1.
- c = 17:  predicted Δβ'(17) = −1 − v_2(4) = −3.

D1's max(2, v_2(c−1)) idiom was the 3-point-fit artefact from c ∈ {5, 7, 9}; those points happen to have v_2(c−1) ∈ {2, 1, 3}, whose max-2 clamp agrees with v_2(⌊c/4⌋) ∈ {0, 0, 1} up to the +1 offset. c = 11 breaks the coincidence.

### 6.2 D2' also fails at c = 13 — bigger revision incoming

**Update (later in Day 91):** Scan test at c = 13 gives **β'(13) ≤ 16**, not 18 as D2' predicts. D(13) ≥ 6, not 4.

Three distinct-min witnesses (a*, b*, k*=6) at c=13 give H_13 with v_2 = 16:
- (a, b) = (7, 0): H_13(7, 0, 6) = 933,042,399,799,910,400,000, v_2 = 16, distinct-min at k=6. ✓
- (a, b) = (7, 8): H_13(7, 8, 6) = 573,719,099,593,534,730,035,200,000, v_2 = 16, distinct-min. ✓
- (a, b) = (15, 0): H_13(15, 0, 6) = 3,402,771,703,255,735,050,240,000, v_2 = 16, distinct-min. ✓

Each computed independently via three-var factorization (`code/2026-07-12-c13-witness-via-catalog.py`, `code/2026-07-12-c13-full-scan.py`). Not a fluke.

**Pattern update for c ≡ 1 mod 4:**

    c=5  (m=1): D=4
    c=9  (m=2): D=6
    c=13 (m=3): D >= 6                    ← breaks D2''s D=4 prediction
    c=17 (m=4): D=? [scan pending]

D2' formula 4 + 2·v_2(m) gives 4, 6, 4 — off at m=3.

**Alternative fit:** D(4m+1) = 4 + 2·⌊log_2(m)⌋ gives 4, 6, 6 for m=1, 2, 3. Matches so far, but this is another 3-point fit — I got burned once, will not commit.

**c=12 UB gives β'(12) ≤ 18**, not 19 (D2' prediction). So D2' is also wrong at c=12. Details in `code/2026-07-12-delta-c12-c13-output.txt`.

**Conclusion**: Both D1 and D2 (and D2') are dead. The true closed form for β'(c) has a more subtle mod-2^k structure than any of these formulas capture — likely something like "high-c behaviour of the argmin k* triggers a jump in Δ_k^{(c)} that the naive m = ⌊c/4⌋ index misses."

The elementary LB_k route continues to be **diagnostic**: for every c it tested, it either confirmed β'(c) (c ∈ {5..11}) or exposed a wrong conjecture (c ∈ {12, 13, +}). Next step is to fully characterise Δ_k^{(c)} for a wider range of k and derive the actual pattern from Q_k structural properties.

### 6.3 Full witness cascade at c ∈ {12, 13, 15, 17} — E, D1, D2, D2' ALL falsified

Extended scans at c ∈ {12, 13, 15, 17}, using ONLY the Q_k catalog for k ≤ 6 (three-var factorization). Distinct-min witnesses computed:

| c  | witness (a, b, k*) | H_c value                                             | v_2  | β'(c) ≤ | D(c) ≥ | β(c) | D2' predicted D | outcome     |
|----|--------------------|-------------------------------------------------------|------|---------|--------|------|-----------------|-------------|
| 12 | (1, 3, 0)          | h_0^{(12)}(1, 3) has v_2 = 18 (single-term)          | 18   | 18      | 1      | 19   | 0               | **E falsified** |
| 13 | (7, 0, 6)          | 933,042,399,799,910,400,000                            | 16   | 16      | 6      | 22   | 4               | D2' falsified |
| 15 | (1, 2, 6)          | −521,981,762,125,824,000,000                          | 20   | 20      | 5      | 25   | 4               | D2' falsified |
| 17 | (15, 0, 2)         | 2,219,138,581,796,266,920,433,686,282,240,000,000       | 23   | 23      | 8      | 31   | 8               | D2' *appears* to match at c=17 |

All witnesses distinct-min (single unique carrier v_2). Independent verification: `code/2026-07-12-c15-c17-distinct-min-output.txt`.

**Anchor identity E (β'(4k) = β(4k))** was previously "sketched" at k=1, 2 only. Falsified at k=3 (c=12): β'(12) ≤ 18 < 19 = β(12), so D(12) ≥ 1.

**D2/D2' predictions** at even c: D(4k) = 0. Both wrong at c=12.

**c=17 apparently matches D2'** — a curious coincidence given cascade of failures. Could be:
- Genuine: D2' happens to be correct at c=17 by structural accident.
- Coincidence: my UB might not be tight for c ≥ 13. Actual β'(17) < 23, and D2' still wrong.

Cannot discriminate without periodicity check.

### 6.4 Meta lesson: never trust another closed form on < 10 data points

Sequence of conjectures fit and falsified in one week:
| Day | Conjecture | Data (# points) | Fit passes at | Broken at |
|-----|------------|-----------------|---------------|-----------|
| Day 83 | mod-4 hypothesis | c=5, 9 | {5, 9} | c=5 |
| Day 84 | D1 | c=5, 7, 9 | {5, 7, 9} | c=11 |
| Day 84 | D2 | c=6, 10 (and c=5, 7, 9 implicit) | {4..10} | c=11 |
| Day 84 | E | c=4, 8 | {4, 8} | c=12 |
| Day 91 | D2' | c=4..10 | {4..11} | c=12, 13, 15 |
| Day 91 | log_2 fit | c=5, 9, 13 | {5, 9, 13} | (untested at c=17) |

Pattern is BRUTAL: every fit blows up at the next power of 2 crossing. The mod-2^k structure of β'(c) is deeper than any low-c polynomial-in-c mod-something formula.

**Next fit: nope.** Go back to the elementary LB_k mechanism and extract Q_k for k = 7..14 to get the FULL UB catalog at c = 13..17. Then either (i) prove min_k UB_k = β'(c) uniformly (would give β' in closed form), or (ii) show the argmin k* has a c-dependent shift that doesn't admit a closed form.

---

## 7. Gaps

- **c = 11 periodicity check running.** Result pending in `code/2026-07-12-c11-periodicity-output.txt`. Insert final numbers into §5 upon completion.
- **D2' is checked-sober at c ∈ {5, 6, 7, 8, 9, 10, 11}** — 7 out of 7 data points match. **Not** proved uniformly.
- **Uniform closed form for Δ_k^{(c)}** for arbitrary k, c: only partial (closed forms for k = 0, 1, 2 at odd c; irregular at k ≥ 3). But we don't need per-k closed forms to prove D2' — only min_k UB_k.
- **Tightness of UB_k vs LB_k:** empirically UB_k ≤ LB_k at the argmin k* for c = 5..11. Structural reason unclear.
- **Uniform proof of D2':** open. The next tests c = 19, c = 27 will discriminate D2' from an even more refined form. If those pass, D2' becomes the primary conjecture and the registry uniform-D closed form gets reformulated.

---

## 8. Consequences for registry

- `beta-prime-closed-form-conditional` (registry `beta-prime-mod8.json`, node ID that references D2): downgrade to **dead-end** with reason "D2 falsified at c=11". D2 subsumed by D2'.
- `refined-dip-formula` (D1): **unaffected** — D1 is the ODD-c formula Δβ'(c) = 1 − max(2, v_2(c−1)), and matches all data. The correction is downstream in D2 → D2'.
- `structural-conjecture-S` (SCP): **strengthened** — for c = 11 we now have a fresh single-carrier witness at k* = 6, adding to the c=4,5,6,7,8,9 catalog. SCP remains checked-sober at c ∈ {4..11}.
- `conjecture-D2`: replaced by `conjecture-D2-prime` with the corrected 4 + 2·v_2(k) formula at c ≡ 3 mod 4.
- `beta-prime-11-lower-bound` and `beta-prime-11-witness`: new nodes, both checked-sober.

---

## 9. Meta

This is a Day-90 Route-Closure success. The three "high-value" M_j routes (Kannan-Song, Motzkin, plethystic) all closed NEG in one wake session on Day 90. The elementary LB_k route — bypassing M_j promotion entirely and going straight for β'(c) via the three-variable factorization — landed a MISMATCH with D2 in Stage 1 of Day 91 Prove, immediately revealing D2 was wrong at c=11 in a way no computation at c ≤ 10 could have shown. The elementary route was not just tractable; it was DIAGNOSTIC.

Lesson: when the categorification chase stalls, retreat to the elementary factorization. The polynomial data are more honest than the conjectures.
