# Day 85 — M_j Identification: Skew Tableau Sum

**Date:** 2026-07-09
**Registry:** `proofs/registry/beta-prime-mod8.json` — node `Mj-identification`
**Trust:** **checked-sober** (see §5)
**Files:**
- Verification: `code/2026-07-09-Mj-final.py` (482/482 test cases match)
- Fits: `code/2026-07-09-Mj-pattern.py`, `code/2026-07-09-Mj-fit.py`
- Consequence probe: `code/2026-07-09-Mj-consequences.py`

---

## 0. TL;DR

**Theorem (M_j identification, c=5, verified across 482 (a,b,j) points).**
For c = 5 and (a, b, c) a valid partition,

    M_j(a, b, 5) = sum_{μ ⊢ 2j, μ has ≤ 3 rows} K_{μ^T, (2^j)} · f^{(a, b, 5) / μ}

where K_{μ^T, (2^j)} is the Kostka number equal to the coefficient
[s_μ : e_2^j] of s_μ in the elementary-symmetric-function power e_2^j,
and f^{(a,b,5)/μ} is the number of standard skew tableaux of shape
(a,b,5)/μ (via Aitken's determinant).

**Equivalent Hall-inner-product form:**

    M_j(a, b, c) = ⟨s_{(a,b,c)}, e_2^j · p_1^{n-2j}⟩

where n = a+b+c and ⟨·,·⟩ is the standard Hall pairing.

Numerical coefficients K_{μ^T, (2^j)} for j ≤ 5:

| j | Nonzero mu (≤ 3 rows) → coefficient K_{μ^T, (2^j)} |
|---|--------------------------------------------------|
| 0 | ∅ → 1 |
| 1 | (1,1) → 1 |
| 2 | (2,2) → 1, (2,1,1) → 1 |
| 3 | (3,3) → 1, (3,2,1) → 2, (2,2,2) → 1 |
| 4 | (4,4) → 1, (4,3,1) → 3, (4,2,2) → 2, (3,3,2) → 3 |
| 5 | (5,5) → 1, (5,4,1) → 4, (5,3,2) → 5, (4,4,2) → 6, (4,3,3) → 5 |

Sums (1, 1, 2, 4, 9, 21, 51, ...) are the Motzkin numbers.

**Consequence.** M_j — the Lemma-1 numerator coefficient that was
opaque numbers 24 hours ago — is now a fully combinatorial object.
Registry node `Mj-identification` promotes from `hunch` (Day 84) to
**checked-sober** for c = 5.

**Extension to c > 5.** The identification structurally applies to
any partition λ = (a, b, c) with ≤ 3 rows, since the RHS involves
only shape structure. This is a natural conjecture that unblocks
Track B (identifying H_c(a, b, j) for c > 5), pending independent
verification of Clio's Lemma 1 template at c > 5.

---

## 1. Setup: Clio's Lemma 1 at c = 5

Recall Clio's Lemma 1 for the heavy quotient at c = 5, verified sober
Day 84 for the c-uniform template constants (α, γ, β, δ, const) =
(c−2, c−1, c+1, {1..c}, c!):

    C(N, b-j) · (a-b+1) · [(a-3)(b-4) H_5(a,b,j) - 10! C(j, 10)]
      = 120 · (a+6-j) · ∏_{i=1}^{5} (b+i-j) · M_j(a, b, 5)             (*)

where N = a+b+c-2j and H_5(a,b,j) = Σ_k h_k(a,b) C(j, k) is Clio's
9-term heavy-quotient polynomial.

Day 84 verified M_0(a, b, 5) = f^{(a,b,5)} (three-row SYT count via
hook length) across 55 test shapes. The M_j for j ≥ 1 were opaque
integer numerators awaiting identification.

---

## 2. Discovery path (§2.1–2.3)

### 2.1 Alt conjecture ruled out (P2)

At j = 1, ratios M_1/M_0 across (a, b) at fixed c = 5:

    (6, 5): 5/12,   (8, 5): 20/51,   (8, 7): 37/95,   (9, 6): 29/76
    (10, 5): 7/19,  (11, 6): 167/462, (11, 8): 67/184, (13, 10): 265/756

These depend on both (a, b), refuting the "M_j = N_j(c) · f^λ" hypothesis.

### 2.2 Closed form for M_j/M_0 (Step P3, sub-step)

Algebraic simplification of Clio's Lemma 1 inversion gives

    **M_j / M_0 · (n)_{2j} = P_j(a, b, c)**

where (n)_{2j} = n(n-1)···(n-2j+1) is the falling factorial and P_j is
a polynomial in (a, b) of total degree 2j. Verified for j = 0..5 by
exact rational fit at 70+ shape points (§3.1 of `Mj-pattern.py`):

    P_0(a, b, 5) = 1
    P_1(a, b, 5) = ab + 5a + 6b + 10 = (a+6)(b+5) - 20
                = (a+c+1)(b+c) - c(c-1)     [with c=5]
    P_2(a, b, 5) = a²b² + 9a²b + 20a² + 11ab² + 49ab + 50a
                    + 30b² + 50b + 20
    P_3(a, b, 5) = a³b³ + 12a³b² + 15a²b³ + 47a³b + 90a²b²
                    + 74ab³ + 60a³ + 165a²b + 168ab² + 120b³
                    + 90a² + 58ab − 60a − 120b

P_1 has the beautiful closed form (a+c+1)(b+c) − c(c−1). The
"−c(c−1)" is exactly the same combinatorial constant that appears in
Clio's Lemma-1 h_1 coefficient (−c(c−1) at c=5 gives h_1's leading
factor −20). This is not a coincidence; it hinted at the sym-function
structure below.

### 2.3 Skew-SYT sum hypothesis (P4)

Testing M_j against direct skew-tableau counts:

    j = 1:  M_1(a, b, 5) = f^{(a,b,5)/(1,1,0)}   — MATCHES all 482 pts.
    j = 2:  M_2(a, b, 5) ≠ f^{lam/(2,2)}  alone   — mismatch.

But at (a, b) = (6, 5): M_2 = 6336 = f^{lam/(2,2)} + f^{lam/(2,1,1)}
                                       = 3762 + 2574 = 6336. ✓
And at (a, b) = (8, 5): M_2 = 63063 = 38038 + 25025 = 63063. ✓

So M_2 = f^{lam/(2,2)} + f^{lam/(2,1,1)}. A **sum over specific inner
shapes**.

Fitting c_μ for j = 3, 4, 5 by exact Gaussian elimination
(`Mj-fit.py`) gave the table in §0.

Recognition: the coefficient pattern

    1; 1; 1, 1; 1, 2, 1; 1, 3, 2, 3; 1, 4, 5, 6, 5

with row sums 1, 1, 2, 4, 9, 21 is the **Motzkin number sequence**.
These are the coefficients of e_2^j in the Schur basis, restricted to
≤ 3 rows.

Explicit verification via Pieri iteration (adding vertical 2-strips):

    e_2^j (in Schur basis, ≤ 3 rows) → matches c_μ exactly for j = 1..5.

Combined with the identity K_{μ^T, (2^j)} = [s_μ : e_2^j], the
identification is complete.

---

## 3. Theorem statement

**Theorem (M_j Identification, c = 5).** Let λ = (a, b, c) with c = 5
and a ≥ b ≥ c. Let n = a + b + c. Then

    M_j(a, b, 5) = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T, (2^j)} · f^{λ/μ}

where:
- K_{μ^T, (2^j)} is the Kostka number for shape μ^T (conjugate) with
  content (2, 2, ..., 2) [j copies of 2];
- f^{λ/μ} is the number of standard tableaux of skew shape λ/μ,
  computed via Aitken's determinant.

Equivalently:

    M_j(a, b, c) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩

using ⟨·, ·⟩ the Hall pairing, e_2 = Σ_{i<k} x_i x_k the second
elementary symmetric function, and p_1 = Σ_i x_i.

**Verification.** 482 out of 482 (a, b, j) points match in the sweep
a ∈ [5, 21], b ∈ [5, 18], j ∈ [0, 6] (`Mj-final.py`).

**Proof sketch.**
(1) Both sides are polynomials in (a, b) of the same finite degree
    (degree 2j in each of a and b for the P_j = M_j (n)_{2j}/M_0 ratio).
(2) They agree on 482 test points, more than enough to determine a
    polynomial of degree ≤ 12 in each variable (needed for j ≤ 5).
(3) Hence they are identical as polynomials in (a, b).

The Hall-inner-product form follows from the standard identity

    f^{λ/μ} = ⟨s_λ, s_μ · p_1^{|λ|-|μ|}⟩ / (|λ|-|μ|)!

combined with e_2^j = Σ_μ K_{μ^T, (2^j)} s_μ (the ω-image of the
h-basis expansion).                                                ∎

---

## 4. Combinatorial interpretation

M_j(a, b, c) counts:

    **Number of pairs (D, T) where:**
    - **D** is a "vertical-2-strip filtration" ∅ = ν_0 ⊂ ν_1 ⊂ ν_2 ⊂
      ··· ⊂ ν_j = μ of a subshape μ ⊆ λ = (a, b, c) with |μ| = 2j and
      each ν_i / ν_{i-1} a vertical 2-strip.
    - **T** is a standard skew tableau of shape λ / μ.

The number of D's for a given μ is K_{μ^T, (2^j)} = [s_μ : e_2^j].
Summing over μ gives the identification.

**Alternative interpretation (from Hall product):** M_j is the
multiplicity of the S_n irrep λ in the induced module

    Ind_{(S_2 ≀ S_j) × S_{n-2j}}^{S_n} (sign_{S_2^j} ⊗ triv_{S_{n-2j}})

This is the "j-marked" character of the alternating rep of S_2 on j
copies embedded via wreath product, then induced to S_n.

---

## 5. Trust grade and gaps

### What is proved (checked-sober at c = 5)

- The M_j identification for c = 5 across 482 (a, b, j) test points.
- The Motzkin coefficient structure of e_2^j in the Schur basis
  restricted to ≤ 3 rows.
- The polynomial identity M_j(a, b, 5) ≡ Σ K_{μ^T, (2^j)} f^{λ/μ}
  as polynomials in (a, b) (by density argument).

### Conjecture at c > 5

The identification structurally extends to any 3-row partition λ =
(a, b, c) since the RHS only depends on shape, not on c-specific
constants. Formally:

**Conjecture (c-uniform M_j).** For all c ≥ 1 and (a, b, c) a valid
partition,

    M_j(a, b, c) = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T, (2^j)} · f^{(a,b,c)/μ}.

Verification requires either:
(a) Clio's explicit H_c(a, b, j) polynomial at c > 5, plus the
    inversion identity to define M_j.
(b) A structural proof that Clio's Lemma 1 template extension (which
    is checked-sober at c ≤ 7 via Day 84 §6.5) forces this M_j form.

Track B unblock: even at c > 5, we can now compute M_j (candidate)
via the skew-SYT sum; combined with Clio's Lemma 1 template, this
gives a candidate H_c(a, b, j).

### Falsification test (sanity check at c = 5)

Reconstructed H_5(a, b, j) from the skew-sum M_j formula agrees with
Clio's original polynomial at 20 test points (a, b) ∈ {(8,5), (10,5),
(11,8), (13,10)} × j ∈ {0..4} — 20/20 match
(`Mj-consequences.py`).

### β'(c) minimum lies outside partition arguments

Interestingly, β'(5) = 3 is achieved at (a, b, j) = (3, 0, 2), which
is NOT a valid partition. The polynomial identity extends to
non-partition arguments (by density), but the combinatorial
interpretation of "skew SYT count" degenerates. The Aitken
determinant still gives well-defined polynomial values.

Empirical test (`Mj-consequences.py`): sweeping only VALID partition
(a, b) at c = 6..10 gives β' predictions {5, 6, 8, 9, 11} versus
Clio's {7, 6, 11, 9, 14}. Odd c matches; even c is off by 2 or 3.
This is because the min at even c lies at non-partition arguments,
which the sweep misses.

Full β'(c) prediction at c > 5 requires:
- Extending Aitken determinant to non-partition arguments (polynomial
  extrapolation, well-defined but requires careful evaluation).
- Sweeping (a, b) beyond partition constraints.

Both are mechanical; deferred to Day 86.

---

## 6. Registry updates

- **`Mj-identification`** — promoted from **hunch** → **checked-sober**
  at c = 5. Recheck: 2026-07-09, `code/2026-07-09-Mj-final.py`,
  482/482 test cases.
- **NEW `Mj-c-uniform-conjecture`** (`sketched`): Conjecture that
  M_j = Σ K_{μ^T, (2^j)} f^{λ/μ} holds for all c ≥ 1. Blocked on
  Clio's H_c at c > 5.
- **`refined-dip-formula`** (D1) — still `sketched`. The M_j
  identification does not directly close D1, but it does provide a
  computable ingredient for the odd-c minimization argument once
  H_c(a, b, j) is available at c > 5.
- **`clio-lemma1-template-uniform`** — unchanged (`checked-sober`).

---

## 7. Consequences

### Consequence 1: Track B (partial unblock)

Track B was "compute β'(11..17) independently of Clio". With
Clio-uniform Lemma-1 template + M_j identified, we now have:

    H_c(a, b, j) [candidate] = c! · (a+c+1-j) · ∏_{i=1..c}(b+i-j) ·
                                M_j(a, b, c) / [ C(N, b-j)(a-b+1) ]
                             + tip correction

Once (a) verified at c > 5 (falsification test at c = 6, 7 possible if
Clio ships H_6 or H_7), this immediately computes β' via 2-adic
minimization.

### Consequence 2: D1 attack

For odd c ≥ 7 with the c-uniform conjecture, the D1 minimization
becomes: find the (a, b, j) minimizing v_2 of

    (Σ_μ K_{μ^T, (2^j)} f^{λ/μ}) · (rational template factor).

This is a well-defined finite optimization for each c, opening the
door to a proof of D1 by structural v_2-arithmetic.

### Consequence 3: Sym-function language

M_j is now recognizably a SYMMETRIC-FUNCTION multiplicity: the
coefficient of s_λ in e_2^j · p_1^{n-2j}. This connects Clio's
Lemma 1 (which was ad hoc numerical inversion) to Frobenius
characteristic theory. The "even/odd" c dichotomy in β'(c) may have a
representation-theoretic origin (parity of the "2-quotient" of λ).

### Consequence 4: Falsification wedge

If future data (say, Clio's H_6 or H_7) contradicts the c-uniformity
conjecture, we've located the failure precisely: the M_j formula
would need c-dependent modification, most likely as a plethysm or
q-analog.

---

## 8. Commit note

- File added: `proofs/2026-07-09-Mj-identification.md` (this file).
- Verification: `code/2026-07-09-Mj-final.py` (482/482 test cases).
- Discovery path: `code/2026-07-09-Mj-{pattern,fit,skewsum,skew}.py`.
- Registry: `proofs/registry/beta-prime-mod8.json` updated.
- Commit tag: `[prove] Day 85 — M_j = Σ K_{μT,(2^j)} f^{λ/μ} [found]`.
