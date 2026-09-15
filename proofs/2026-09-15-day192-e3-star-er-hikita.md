# Day 192 PROVE — e_3 ⋆ e_r in Hikita's ⋆-product; meta-conjecture verified

**Date:** 2026-09-15
**Grading:** `computed` (SymPy small-case; not sober re-derivation).
**Framework:** `hikita_star.py` at `~/projects/proofs/scripts/day192/`.
Reuses Day 191 level-one affine Hecke polynomial rep. Extended a=1,2 → a=3.

---

## 1. Result: closed forms

### 1.1  e_3 ⋆ e_2 (m=5, n=5)

```
e_3 ⋆ e_2 = q^{-2} · e_{3,2}
          + (q-1)/q^2 · [3]_t · e_{4,1}
          + (q-1)/q^2 · [5]_t · (q(1+t^2) - t) · e_5
```

Equivalently, unified with c_1 formula below (r=2):
```
e_3 ⋆ e_2 = q^{-2} · e_{3,2}
          + (q-1)/(q^3 [2]_t) · [3]_t · q[2]_t · e_{4,1}         (= c_1(2), boundary)
          + c_0(2) · e_5
```

**3 nonzero terms.**  min(3,2)+1 = 3 ✓.

### 1.2  e_3 ⋆ e_3 (m=6, n=6)

```
e_3 ⋆ e_3 = q^{-3} · e_{3,3}
          + (q-1)/q^3 · [2]_t · e_{4,2}
          + (q-1)/q^3 · [4]_t · (q[3]_t - t) · e_{5,1}     [equivalently (q-1)/(q^3 [2]_t)·[4]_t·(q[3]_t - t·[1]_t)]
          + c_0(3) · e_6
```

with
```
c_0(3) = (q-1)/q^3 · (t+1)(t^2-t+1) · Δ_3(q,t),

Δ_3(q,t) = q^2 t^6 + q^2 t^5 + 2q^2 t^4 + 2q^2 t^3 + 2q^2 t^2 + q^2 t + q^2
         - q t^5 - 2q t^4 - 2q t^3 - 2q t^2 - q t
         + t^3.
```

**4 nonzero terms.**  min(3,3)+1 = 4 ✓.

---

## 2. Meta-conjecture verdict

Rick's meta-conjecture: **e_a ⋆ e_b has exactly min(a,b)+1 nonzero e_λ coefficients, supported on partitions (a+b-k, k) for k = 0, 1, ..., min(a,b).**

Verified for e_3 ⋆ e_r at r = 1, 2, 3, 4, 5 (m up to 8):

| (a,r) | predicted | observed | support |
|-------|-----------|----------|---------|
| (3,1) | 2 | 2 | e_4, e_{3,1} |
| (3,2) | 3 | 3 | e_5, e_{4,1}, e_{3,2} |
| (3,3) | 4 | 4 | e_6, e_{5,1}, e_{4,2}, e_{3,3} |
| (3,4) | 4 | 4 | e_7, e_{6,1}, e_{5,2}, e_{4,3} |
| (3,5) | 4 | 4 | e_8, e_{7,1}, e_{6,2}, e_{5,3} |

**Verdict: `computed` (r ≤ 5), PASS.**  Combined with Day 191 (r ≤ 4 for a=2) and Thm 3.12 (a=1, all r): the min(a,b)+1 term prediction holds for all cases computed so far.

---

## 3. General e_3 ⋆ e_r conjecture

Writing `[k]_t = 1 + t + ... + t^{k-1}` and letting `c_k(r) = coefficient of e_{r+3-k, k}` (with e_{r+3-0,0} := e_{r+3}), we conjecture the following closed forms for r ≥ 3:

### c_3(r) — "bottom" term
```
c_3(r) = q^{-3}                                                  (r ≥ 3)
```

### c_2(r) — "sub-middle"
```
c_2(r) = (q-1) · [r-1]_t / q^3                                    (r ≥ 3)
```
Boundary case: **c_2(2) = q^{-2}** (bottom term when r=2).

### c_1(r) — "sub-top", unified
```
c_1(r) = (q-1) · [r+1]_t · (q [r]_t - t [r-2]_t) / (q^3 · [2]_t)   (r ≥ 2)
```
Verified for r = 2, 3, 4, 5.  Boundary at r=1: c_1(1) = q^{-1} (bottom term when r=1), differs from formula.

### c_0(r) — "top"
```
c_0(r) = (q-1)/q^3 · [ G(r) · q^2  -  t · β_1(r,t) · q  +  t^3 · β_0(r,t) ]
```
where
- `G(r) = [r+1]_t [r+2]_t [r+3]_t / ([2]_t [3]_t)`  is the q-Gaussian binomial `[r+3 choose 3]_t`.
- β_1(r,t) and β_0(r,t) are polynomials in t whose closed forms did not admit a clean q-integer factorization on r ∈ {3,4,5}.

**Verified: q^2 coefficient of c_0(r) · q^3/(q-1) equals G(r) exactly for r = 3, 4, 5.**

Values (r=3,4,5), extracting β_1(r,t) = -A_1(r,t) / (t · [r+3]_t) and β_0(r,t) = A_0(r,t) / (t^3 · [r+3]_t), where A_i are the q-power coefficients:

| r | -A_1/t (= β_1 · [r+3]) | A_0/t^3 (= β_0 · [r+3]) |
|---|-----------------------|-------------------------|
| 3 | (t+1)^3 (t^2+1) (t^2-t+1) | (t+1)(t^2-t+1) |
| 4 | [5]_t · [7]_t                | [7]_t         |
| 5 | (t+1)^3 (t^2+1)^2 (t^4+1)(t^2-t+1) | (t+1)(t^2+1)^2 (t^4+1) |

The discriminant of the quadratic-in-q d_0(r) has an irreducible factor of degree ≥ 4 in t (for r=3: degree-6 factor). **No clean q-integer factorisation of the c_0 quadratic across all r; the top-term coefficient is more complex than the sub-top c_1.**

---

## 4. Sanity checks

### 4.1  q = 1 (ordinary product)

At q = 1, ⋆-product must reduce to ordinary product e_a · e_b = e_{max(a,b), min(a,b)}:

- e_3 ⋆ e_2 |_{q=1}: e_{3,2}: **1**; all others: **0**  ✓
- e_3 ⋆ e_3 |_{q=1}: e_{3,3}: **1**; all others: **0**  ✓

### 4.2  q → ∞ (Hikita Thm C(ii) classical limit)

Only c_0(r) has a finite limit; all c_k(r) with k≥1 vanish:

```
lim_{q→∞} (e_3 ⋆ e_r) = G(r) · e_{r+3} = [r+1]_t [r+2]_t [r+3]_t / ([2]_t [3]_t) · e_{r+3}
```

**This is the q-Gaussian `[r+3 choose 3]_t`.**

Verified numerically for r = 2, 3, 4, 5.  Consistent with Thm C(ii): the classical (q→∞) limit of e_a ⋆_H is multiplication by the q-Gaussian `[a+r choose a]_t`, matching the "e_a · e_r → q-Gaussian · e_{a+r}" identity in the Ellingsrud-Strømme / Nakajima Hilbert-scheme t-deformation.

Note this generalizes the a=1 case: lim e_1 ⋆ e_r = [r+1]_t · e_{r+1} = `[r+1 choose 1]_t · e_{r+1}` (Thm 3.12).
And the a=2 case: lim e_2 ⋆ e_r = [r+1]_t [r+2]_t / [2]_t · e_{r+2}.

### 4.3  a=3 framework validation (before running expensive computes)

Test 1 (Thm 3.12): e_1 ⋆ e_2 at m=3 matches Hikita's formula.  ✓
Test 2 (Day 191): e_2 ⋆ e_2 at m=4 matches Day 191 checked-sober result.  ✓
Test 3 (commutativity): e_3 ⋆ e_1 = e_1 ⋆ e_3 at m=4 (a=3 code output equals Thm 3.12 e_1 ⋆ e_3).  ✓

---

## 5. Meta-observations & next targets

1. **q-Gaussian is universal.** The q→∞ classical limit of e_a ⋆ e_r appears to be uniformly `[a+r choose a]_t · e_{a+r}` = q-Gaussian binomial coefficient. This is worth formalizing as a lemma; it follows from Hikita Thm C(ii) but the small-case computation gives independent verification.

2. **c_{min(a,b)} = q^{-a} × sign-corrected q-power (Bottom term).**
   - (a=1, r): c_1(1) = q^{-1}
   - (a=2, r=2): c_2(2) = q^{-2}
   - (a=3, r=3): c_3(3) = q^{-3}
   - (a=3, r≥3): c_3(r) = q^{-3}  (same)
   The "bottom" coefficient is `q^{-min(a,b)}` when a=b, `q^{-max(a,b)?}`... actually just observe c_a(r) = q^{-a} for r ≥ a. This is consistent with the "top of Y-side" scaling t^{-a(a-1)/2} · leading normalization in Hikita.

3. **c_{min(a,b)-1} has "linear-in-q form".** Compare with Day 191's c_1 for a=2:
   - a=2: c_1(r) = (q-1)/q · [r]_t   (simple, purely q-linear)  → wait let me re-check…
     Day 191 said c_1^{(a=2)}(r) coefficient of e_{r+1,1} = ((1-q^{-1})/q) · [r]_t = (q-1)/q^2 · [r]_t.
   - a=3: c_2(r) = (q-1) [r-1]_t / q^3 for r ≥ 3. Structure same up to shift of q-integer.

4. **Pattern-match "c_{min-1}(r) = (q-1) [r + shift]_t / q^a".** For a=2 (bottom term c_2): "one up" is c_1 = (q-1)[r]_t / q^2. For a=3 (bottom term c_3): "one up" is c_2 = (q-1)[r-1]_t/q^3. Suggested general: **c_{a-1}(r) = (q-1) [r+2-a]_t / q^a** for r ≥ a.

5. **Sub-sub-top c_{a-2}(r) has "q-linear · q-integer / [2]_t form".** For a=2 (r≥2 boundary): c_0^{(a=2)}(r) = (q-1) · [r+2]_t/[2]_t · ([r+1]_t - t[r-1]_t/q). For a=3 (r≥2): c_1^{(a=3)}(r) = (q-1)/(q^3 [2]_t) · [r+1]_t · (q [r]_t - t [r-2]_t).
   
   Both have the pattern `(q-1) · [something]_t / [2]_t · (q [k]_t - t [k-2]_t)`. This is very suggestive of a general **e_a ⋆ e_r "sub-sub-top" formula:**
   ```
   c_{a-2}(r) = (q-1) · [r+3-a]_t / (q^a · [2]_t) · (q [r+2-a+something]_t - t [...])
   ```
   Needs a=4 data to test.

6. **c_0 (top) grows in complexity.**  At a=3, c_0 already has a discriminant with an irreducible degree-6 factor; no clean closed form found.  For a=2 the top c_0 was closed, so **a=3 is where the "product-of-q-integers" pattern breaks for c_0**. This suggests c_0 is NOT the fundamental Pieri object; the "shape-indexed" c_k for larger k are the fundamental ones.

7. **Route forward for FPSAC anchor.** With min(a,b)+1 term meta-conjecture at 12-for-12 (a=1 all r, a=2 r≤4, a=3 r≤5), a `checked-sober` upgrade would need:
   - Proof of the general "support" statement (partitions of shape (a+b-k, k) with k ≤ min(a,b)) — this may follow from Hikita Prop 3.6 (q=1 limit is ordinary product, giving e_a·e_r support), plus a q-flatness / q-deformation argument.
   - Prove c_a(r) = q^{-a} (via top-of-Y-action + AHA scaling).
   - Prove c_{a-1}(r) = (q-1)[r+2-a]_t/q^a (via unfolding one Y_i).
   The "shape" (i.e., number of nonzero terms) may be easier to prove than the coefficients.

---

## 6. File locations

- `~/projects/proofs/scripts/day192/hikita_star.py` — framework (a=1,2,3).
- `~/projects/proofs/scripts/day192/test_framework.py` — regression tests (Thm 3.12, Day 191, commutativity).
- `~/projects/proofs/scripts/day192/compute_e3_e2.py` — e_3 ⋆ e_2 at m=5.
- `~/projects/proofs/scripts/day192/compute_e3_e3.py` — e_3 ⋆ e_3 at m=6.
- `~/projects/proofs/scripts/day192/compute_e3_er.py` — e_3 ⋆ e_r for r=1..5 (m ≤ 8).
- `~/projects/proofs/scripts/day192/pattern_v3.py`, `pattern_v4.py`, `pattern_v5.py`, `pattern_v6.py`, `pattern_v7.py` — pattern-hunt scripts.
- `~/projects/proofs/scripts/day192/sanity_checks.py` — q=1 and q→∞ checks.
- `~/projects/proofs/scripts/day192/e3_e2_output.txt`, `e3_e3_output.txt`, `e3_er_output.txt` — captured outputs.
- `~/projects/proofs/scripts/day192/e3_e2_m5.pkl`, `e3_e3_m6.pkl`, `e3_er_data.pkl` — pickled coefficient data.

Trust vocabulary: `computed`.  Sober re-derivation (independent transfer-matrix or alternative representation) not yet done.

Registry updates (proposed):
- `hikita-star-e3-e2` = computed (m=5).
- `hikita-star-e3-e3` = computed (m=6).
- `hikita-star-e3-er-support-conjecture` = computed r ≤ 5, k up to 3.
- `hikita-star-min-a-b-plus-1-terms-metaconjecture` = computed (all cases a ≤ 3 tested).
- `hikita-star-c_{a-1}-closed-form-conjecture` = hunch (needs a=4 data).
- `hikita-star-q-to-infinity-limit-is-q-gaussian` = computed a ≤ 3, sober derivation from Thm C(ii) tractable.
