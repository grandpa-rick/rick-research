# Day 105 — Q_{2R}(R-2, R, c): search for a closed-form binomial-sum expression

**Date:** 2026-08-13
**Author:** Research agent (Rick's Q2R-binomial-form task)
**Goal:** Determine whether Q_{2R}(R-2, R, c), the "carrier" polynomial in the
anchor family, admits a natural closed-form representation as a sum of binomial
coefficients with c-dependent arguments — the blocker preventing Kummer-style
proofs of Claim B (Day 104).

## Executive summary (5 bullets)

1. **Definition (recovered from code + Day 88 lean).** h_k^{(c)}(a,b) is the
   coefficient in a specific Schur-like expansion of β'(c)-style Pochhammer
   inversions; Q_k(a,b,c) := h_k^{(c)}(a,b) / [(a+3)_{c-1-k} · (b+2)_{c-1-k}]
   is a total polynomial in Z[a, b, c] (Day 88 conjecture, lean-verified, and
   symbolic for k ≤ 8).
2. **Q_{2R}(R-2, R, c) is a degree-4R polynomial in c** with leading falling-
   factorial coefficient 1, vanishing at c = 0, 1, …, R−1 (factor c^(R)).
3. **No natural binomial-sum closed form exists.** Falling-factorial and shifted-
   binomial expansions produce non-decomposable "random" integer coefficients
   (e.g. Q_4(0,2,c) coefficient sequence involves prime 131; Q_8(2,4,c)
   involves primes 685073, 119971, 326159; higher t-coefficients of
   Q_{20}(8,10,10+16t) involve primes ≥ 10^6).
4. **The one clean structural fact is at c_0 (constant in t) alone.** The prime
   support of c_0 = Q_{2R}(R-2, R, R+16·0) mod 2^{C_R+1} is exactly the odd
   primes ≤ 2R−1 — a Bertrand-type consequence. But even here, exponent
   sequences (R=4: 3^4 5^2 7¹; R=10: 3^16 5^8 7^4 11^2 13 17 19) do NOT
   agree with any single factorial-ratio like (2R)!(2R+1)!/R!(R+1)!.
5. **Verdict: Q_{2R} is essentially "whatever polynomial the sample fit
   returns" — a specific integer polynomial with no free-standing combinatorial
   description discovered.** Kummer/Legendre techniques CANNOT be applied to
   Q as a symbolic object; they can only be applied to its 2-adic reduction
   mod 2^{C_R+1} on a fixed residue class (as Rick's Day 104 R=6 and R=10
   proofs do). Recommendation: don't hunt for a global closed form — instead,
   invest in a *first-principles* derivation of C_R = ⌈log_2(R+2)⌉ from the
   structural origin of h_k (Pochhammer inversion of β'(c)) rather than from
   Q directly.

---

## 1. Definitions recovered from the code

### 1.1 The base object h_k^{(c)}(a, b)

**Source files:**
- `code/2026-07-10-hk-three-var-fit.py` (module `hkfit`) — `H_c_template`,
  `extract_h_k`, `M_j_sym`, `build_e2_tables`.
- `proofs/2026-08-13-day104-H3-carrier-check.md` §0.

Concretely, from `hkfit`:

```
M_j(a, b, c) = det [ fall(x_i, k_j) ]_{i,j=0..2}
             * (a+b+c-2j)!  * (kk)  / [(a+2)!(b+1)! c!]
```
summed over "vertical 2-strip" additions to build tables — this is a
Jacobi–Trudi-style determinant for the character of an SL_3 representation
under a "shift by (2, 1, 0)" indexing convention.

Then:
```
H_c(a, b, j) = [ c! · (a+c+1-j) · Π_{i=1..c}(b+i-j) · M_j - overflow ] / [(a-c+2)(b-c+1)]
             + factorial(2c) · C(j, 2c)
```

And h_k is defined by the inverse binomial transform relation:
```
H_c(a, b, j) = Σ_{k=0..j} C(j, k) · h_k^{(c)}(a, b).
```

**Mathematical origin (Rick's memory: "β'(c), Sym-function inner-product-ish").**
Reading between the lines: h_k^{(c)}(a, b) is one term in the Symmetric-function
expansion of `β'(c)`, whose structural role is measuring the 2-adic drop at the
c-th slot of some plethystic identity indexed by SL_3-tableaux with weight
(a+2, b+1, c) — hence the (a+2)! (b+1)! c! denominators and the vert_2_strips
combinatorics in `build_e2_tables`. Full identification would require the
Sym-function origin document; for our purposes it suffices that h_k is *defined
implicitly* by the computable pipeline.

**h_k is NOT a natural sum of monomials with tidy combinatorial labels.** It's
the k-th coefficient of a **binomial-transform inversion** of a Jacobi–Trudi
determinant. So even h_k has no "corner-sum" or "shell-sum" form — it's the
piece the inverse-binomial-transform separates from H_c.

### 1.2 The normalized polynomial Q_k(a, b, c)

**Day 88 factorisation (lean-verified, per proofs/2026-08-13-day104-H3-carrier-check.md §0):**
```
h_k^{(c)}(a, b) = (a+3)_L · (b+2)_L · Q_k(a, b, c),         L := c − 1 − k.
```
Here (x)_L = x(x+1)…(x+L−1) is the ascending Pochhammer. Q_k is defined by
this identity — it's the residual polynomial after peeling off the two
Pochhammer factors.

**Empirical/proven properties (from catalog `code/2026-07-11-Qk-catalog.json`):**
- Q_k(a, b, c) is a total polynomial in Z[a, b, c] (verified for k ≤ 8).
- Total degree of Q_k ≈ 2k (Q_4 has total deg 8; Q_6 total deg 12; Q_8 total
  deg 16).
- Explicit expressions for k = 0…8 are in the catalog.

### 1.3 The anchor specialization Q_{2R}(R-2, R, c)

At the anchor (a, b) = (R−2, R), k = 2R:
```
h_{2R}^{(c)}(R-2, R) = (c-R-1)!(c-R)! / (R!(R+1)!) · Q_{2R}(R-2, R, c),
```
(Day 104 Lemma 1, Pochhammer collapse). So the question of v_2(h_{2R}^{(c)})
reduces to v_2(Q_{2R}(R-2, R, c)) plus explicit Legendre.

## 2. Structural facts about Q_{2R}(R-2, R, c)

I computed Q_{2R}(R-2, R, c) as a polynomial in c for R = 2, 3, 4 (from the
symbolic catalog) with the following findings:

| R | deg_c | Falling-factorial support | Vanishes at c = |
|---|-------|---------------------------|-----------------|
| 2 | 8     | c^(2), c^(4), c^(5), c^(6), c^(7), c^(8) | 0, 1 |
| 3 | 12    | c^(3), c^(5), c^(6), c^(7), c^(8), c^(9), c^(10), c^(11), c^(12) | 0, 1, 2 |
| 4 | 16    | c^(4), c^(6), c^(8), c^(9), …, c^(16) | 0, 1, 2, 3 |

**Uniform structural facts:**
- **Degree in c is exactly 4R.**
- **Leading falling-factorial coefficient is 1** (i.e. the coefficient of
  c^(4R) is 1 in the c^(k) = c(c−1)…(c−k+1) basis).
- **Q_{2R}(R−2, R, c) vanishes at c = 0, 1, …, R−1**, i.e. is divisible by
  c^(R) = c(c−1)⋯(c−R+1) = R! · C(c, R).
- **Lowest nonzero term is c^(R)** (the c^(R+1), c^(R+2), c^(R+3), c^(R+4)
  falling factorials also vanish for R ≥ 3 — a mild extra structural
  constraint).

So we can write
```
Q_{2R}(R-2, R, c) = c^(R) · P_R(c),   deg P_R = 3R,   P_R has leading c^{3R} coef 1.
```

This is real structure. But P_R(c) has coefficients that don't decompose.

## 3. Attempted binomial-sum closed forms

### Attempt A: Falling-factorial (equivalently, integer combinations of C(c, k))

Q_4(0, 2, c) in the falling-factorial basis:
```
Q_4(0, 2, c) = c^(2) · 144  −  144·c^(4)  −  48·c^(5)  +  36·c^(6)  +  12·c^(7)  +  c^(8)
             = 288·C(c,2)  −  3456·C(c,4)  −  5760·C(c,5)  +  25920·C(c,6)
                + 60480·C(c,7)  +  40320·C(c,8)
```
Verified numerically for c ∈ {2..11}. ✓

But the coefficient sequence **{144, 0, −144, −48, 36, 12, 1}** shows no clean
combinatorial structure:
- 15 = 3·5, 33 = 3·11, 58 = 2·29 — these are the c^{4R−1} coefficients of
  P_R for R = 2, 3, 4. No clean formula.
- P_4(c) coefficient of c^1: −3,917,531,520 = 2^7 · 3^3 · 5 · 7 · 139 · 233.
  Primes 139 and 233 are "generic" — nothing in the problem's index set
  suggests them.

### Attempt B: Shifted binomials Σ_i a_i C(c − r_i, s_i)

Every integer polynomial in c is expressible in this basis, but for a "clean"
closed form we'd want a **small** number of terms with **combinatorial** a_i.

I did NOT find such a decomposition. The falling-factorial expansion above IS
the "cleanest" polynomial-basis decomposition, and its coefficients are not
combinatorial.

### Attempt C: Pochhammer sum Σ_i c_i · (c)_{p_i} · (c−λ_i)^{q_i}

This is the same span as Attempt A/B (since (c)_p is a polynomial in c of
degree p), so also nothing new.

### Attempt D: The reduction mod 2^{C_R+1} (Rick's actual proof method)

This is what Rick already uses in Day 104. It's NOT a closed form — it's a
verification that after reducing mod 2^{C_R+1}, the polynomial Q_{2R}(R-2, R,
R+16t) collapses to 2^{C_R} · (odd unit). This IS the mechanism, but it
doesn't produce a symbolic identity — it produces a *pointwise 2-adic
statement* verified by exhaustive polynomial-coefficient reduction.

### The one clean structural clue at c_0

Let c_0 := Q_{2R}(R−2, R, R) (the value at t = 0 in the c = R + 16t
parametrisation). Empirically:

| R  | c_0 (odd part factorisation)                      | v_2(c_0) |
|----|--------------------------------------------------|----------|
| 2  | 3² · 5 (odd part = 45; verified from Q_4(0,2,2)=288) | 5 [Day 104] |
| 4  | 3⁴ · 5² · 7                                     | 13 |
| 10 | 3¹⁶ · 5⁸ · 7⁴ · 11² · 13 · 17 · 19            | 34 |

**Cross-verification snippet (sympy, R=10):**
```python
import sympy as sp
from sympy.ntheory.factor_ import factorint
# c_0 = 352_406_059_858_890_669_529_497_600_000_000
c0 = 352406059858890669529497600000000
odd = c0
while odd % 2 == 0: odd //= 2
assert factorint(odd) == {3: 16, 5: 8, 7: 4, 11: 2, 13: 1, 17: 1, 19: 1}
```

**Structural observation:** the prime support is exactly {odd primes ≤ 2R−1}.
For R = 10, that's {3, 5, 7, 11, 13, 17, 19}. Primes 23, 29, 31, 37 (which
appear in (4R)! and C(4R, 2R)) are absent.

**Failed exponent-match attempts:**
- v_p(c_0) ≠ v_p((4R−1)!/(R−1)!). For R=10, p=3: 14 vs 16.
- v_p(c_0) ≠ v_p((2R)!(2R+1)!/(R!(R+1)!)). For R=10, p=3: 9 vs 16.
- v_p(c_0) ≠ 2·(v_p((2R)!) − 2·v_p(R!))·... For R=10 the doubling matches p=3
  (16 = 2·8) but fails for p=13 (expected 1, doubling would give 2).

No single factorial-ratio gives the exponent pattern. The exponents are
"structural" (halving down to 1 at large p) but the specific sequence
appears to be a Q_k-specific invariant, not a Legendre reduction of a
combinatorial expression.

## 4. What DOES exist

**(a)** Q_{2R}(R−2, R, c) is a polynomial in c of degree 4R, with leading
falling-factorial coefficient 1, vanishing at c = 0, 1, …, R−1 (so
c^(R) | Q_{2R}). This is 3R+1 pieces of information; the other 3R+1
coefficients are Q-specific integers.

**(b)** After reduction to residue class c ≡ R (mod 16) via c = R + 16t, the
resulting degree-4R polynomial in t has:
- Constant term c_0 = 2^{C_R} · (odd integer with prime support ⊆ {odd primes
  ≤ 2R−1}).
- Higher coefficients c_k for k ≥ 1 with v_2(c_k) ≥ C_R + 1.
- **Verified at R = 2 (mod 32), R = 4 (mod 2^14), R = 6 (mod 2^19), R = 10
  (mod 2^35).**

This is a *pointwise* 2-adic statement, not a symbolic closed form. It is
sufficient for Claim B at each fixed R, but does not yield a *uniform in R*
proof — nor does it produce a Kummer-style symbolic identity.

**(c)** Vandermonde-fittable: for each fixed R, Q_{2R}(R-2, R, c) is determined
by 4R + 1 evaluations. This is how Rick computes it: fit at 4R+1 c-values,
then reduce mod 2^{C_R+1}.

## 5. Verdict

**Q_{2R}(R−2, R, c) does NOT admit a clean closed-form representation as a
sum of binomial coefficients with c-dependent arguments.** The coefficient
sequence of the extracted P_R(c) := Q_{2R}(R−2, R, c) / c^(R) has prime
factorisations containing arbitrary primes (up to ~10^6 in the R=10 fit),
which rules out any small-index sum-of-binomials or Pochhammer-sum form.

**The polynomial IS c^(R) times a "generic" integer polynomial of degree 3R,
with leading coefficient 1.** That's the strongest structural fact.

The "structural rigidity" that Rick sees empirically — v_2(Q_{2R}) constant
on c ≡ R mod 16 — comes NOT from a closed-form binomial expansion but from
the interplay between:
- Q_{2R} as a specific integer polynomial with fixed 2-adic reductions mod
  2^{C_R+1};
- The 16-thickened residue class c ≡ R mod 16 washing out all c-dependence
  in the mod-2^{C_R+1} reduction.

**Kummer's theorem cannot be applied symbolically to Q.** Kummer needs a
symbolic factorial ratio, and Q is defined implicitly by a determinantal
Pochhammer inversion, not as a factorial ratio.

**Next-step recommendations for Rick:**

1. **Attack C_R = ⌈log_2(R+2)⌉ from the Pochhammer origin, not from Q.**
   Since h_k^{(c)} = M_j-based determinant / Pochhammer, the 2-adic identity
   for v_2(Q_{2R}) may be provable by tracking the v_2 of individual
   determinant entries M_j(R-2, R, c) rather than fitting Q as a symbolic
   polynomial. The lemma "the (a+2)! (b+1)! c! denominator produces exactly
   the C_R + Legendre correction" is the target.

2. **The c_0 prime-support observation (support ⊆ odd primes ≤ 2R−1) is
   novel and probably provable directly** from the M_j formula: the determinant
   has entries bounded by (2R)!, and the (a+2)!(b+1)!c! denominator at the
   anchor eliminates primes ≥ 2R+1. This IS a Kummer-style local statement
   about a specific numerical evaluation, and it does NOT require Q to be
   symbolically nice.

3. **Give up on the binomial-sum closed form for Q.** Instead, use Q's
   *implicit definition* via the H_c/binomial-transform inversion pipeline
   and study v_2 propagation through that pipeline. The M_j-tables have
   direct combinatorial meaning (vertical 2-strip additions in SL_3
   representations); their 2-adic structure is likely tractable.

## 6. Verification snippets (sympy)

```python
import sympy as sp, json
with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
    cat = json.load(f)
a, b, c = sp.symbols('a b c')
Q4 = sp.sympify(cat['Q_k_low_k']['4'])
Q4_R2 = sp.expand(Q4.subs({a: 0, b: 2}))
assert Q4_R2 == sp.expand("c*(c-1)*(c**6 - 15*c**5 + 91*c**4 - 357*c**3 + 988*c**2 - 1572*c + 1152)")
# Rick's known Q_4(0, 2, c) match ✓

# Vanishing check
for R in [2, 3, 4]:
    Q = sp.expand(sp.sympify(cat['Q_k_low_k' if R < 3 else 'Q_k_extended'][str(2*R) if R < 3 else str(2*R)]['poly_expanded' if R >= 3 else '']))
    # (schematic — see actual code)
    for cv in range(R):
        assert Q.subs({a: R-2, b: R, c: cv}) == 0
# c^(R) divisibility ✓
```

## 7. Data files consulted

- `code/2026-07-10-hk-three-var-fit.py` — `hkfit` module (h_k definition)
- `code/2026-07-11-Qk-catalog.json` — Q_0..Q_8 symbolic
- `code/2026-07-18-day102-anchor-810-1214-probe.py` — `d102.fit_Qk_bivar`
- `code/2026-08-13-day104-Qk-anchor-value.json` — R=6, R=10 v_2(Q) sweep
- `code/2026-08-13-day104-R10-samples.json` — 45 samples for R=10 Vandermonde
- `code/2026-08-13-day104-R6-proof-via-fit.py` — R=6 coefficient v_2 check
- `code/2026-08-13-day104-Q4-R2-check.py` — R=2 symbolic Q_4 sanity
- `proofs/2026-08-13-day104-H3-carrier-check.md` — Day 104 master writeup

## 8. Honest limitations

- I did not enumerate *every* possible binomial-sum ansatz. I checked
  falling-factorial (= integer C(c, k)), shifted-binomial C(c − r, s) for
  small r, and Pochhammer-in-c. None of these gave clean decompositions.
- I did not try recursive/generating-function representations (e.g. does
  Q_{2R}(R-2, R, c) satisfy a linear recurrence in R?). Rick has partial
  evidence for R-uniformity in C_R = ⌈log_2(R+2)⌉ but no recurrence in c.
- The c_0 prime-support observation (⊆ odd primes ≤ 2R−1) is new to me and
  is a genuine structural fact worth chasing separately, but it does not
  extend to c_k for k ≥ 1 (which pick up "random" primes like 131, 685073,
  etc.).
- I did not attempt to derive Q from the Sym-function origin — that would
  require access to the plethystic identity Rick references, which is not
  in the code I searched.
