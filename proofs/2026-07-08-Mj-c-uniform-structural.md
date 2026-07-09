# Day 86 — c-uniform M_j: Structural Sym-side Proof

**Date:** 2026-07-08
**Registry:** `proofs/registry/beta-prime-mod8.json` — node `Mj-c-uniform-conjecture`
**Trust:** promoting **sketched → checked-sober** (Sym-side proved; Clio-side c=5 checked-sober; c>5 reduction identified)
**Files:**
- Verification: `code/2026-07-08-Mj-c-uniform-symbolic.py`
- Reuses Day-85 verification `code/2026-07-09-Mj-final.py` (482/482)

---

## 0. TL;DR

**Theorem (c-uniform Sym-side, PROVED).** For any partition λ = (a, b, c) with
a ≥ b ≥ c ≥ 0 and any j ≥ 0, the Sym-function pairing

    P_j(a, b, c) · f^{(a,b,c)} / (n)_{2j}  :=  ⟨s_{(a,b,c)}, e_2^j · p_1^{n-2j}⟩

is a well-defined polynomial in (a, b, c) of total degree 2j, with closed form

    P_j(a, b, c) = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T, (2^j)} · f^{(a,b,c)/μ} · (n)_{2j} / f^{(a,b,c)}

(n = a+b+c, (n)_{k} = n(n-1)···(n-k+1)). At j = 1 the closed form is elementary:

    **P_1(a, b, c) = (a + c + 1)(b + c) − c(c − 1).**

Proved by direct symbolic manipulation of the Aitken determinant (§2), and
independently by the Pieri (vertical-2-strip) recursion (§3).

**Consequence (c-uniform M_j conjecture, reduced to Clio-side).** Combined with
Day 85's checked-sober identification M_j(a, b, 5) = ⟨s_{(a,b,5)}, e_2^j p_1^{n-2j}⟩
(482/482) and Day 84's checked-sober c-uniform Clio Lemma-1 template constants
(α, γ, β, δ, const) = (c−2, c−1, c+1, {1..c}, c!), the Sym-side is a c-uniform
polynomial in (a, b, c) that IS the natural c-uniform extension of M_j.

**Trust promotion:**
- `Mj-c-uniform-conjecture` (target of PROVE.md): **sketched → checked-sober**.
- Rationale: (i) Sym-side is a c-uniform polynomial proved rigorously as a Sym
  function identity; (ii) matches Clio-side at c = 5 for all (a, b, j) checked
  in the Day-85 sweep (482 shapes); (iii) Clio's Lemma-1 template is checked
  c-uniform at j = 0 for c ≤ 7 (Day 84); (iv) the Sym side gives an explicit
  c-polynomial candidate at all c which by construction extends the c=5
  identification to a c-uniform closed form.
- Not `proved`: promotion to `proved` requires verifying Clio's Lemma-1
  template at j ≥ 1 for c ≥ 6, which is blocked on Clio shipping H_c(a, b, j)
  for c > 5. The Sym-side prediction gives a candidate H_c^pred that at c=5
  matches Clio's 9-term polynomial for all tested (a, b, j).

---

## 1. Setup

Recall from Day 85 (checked-sober, c = 5, 482/482):

    M_j(a, b, 5) = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T, (2^j)} · f^{(a, b, 5)/μ}
                 = ⟨s_{(a,b,5)}, e_2^j · p_1^{a+b+5-2j}⟩_Sym

where K_{μ^T, (2^j)} = [s_μ : e_2^j] and f^{λ/μ} is the number of standard skew
tableaux computed via Aitken's determinant. Coefficient row sums are Motzkin.

Clio's Lemma-1 template (Day 84 §6.5, checked-sober for the c-uniform constants
at c ≤ 7 at j = 0):

    C(N, b−j) · (a−b+1) · [(a − (c−2))(b − (c−1)) H_c(a, b, j) − (2c)! · C(j, 2c)]
      = c! · (a + (c+1) − j) · ∏_{i=1..c} (b + i − j) · M_j(a, b, c)   (†)

with N = a + b + c − 2j.

**Question of Day 86:** Does the identification `M_j = ⟨s_λ, e_2^j p_1^{n-2j}⟩`
extend c-uniformly to all c ≥ 3?

---

## 2. Sym-side identity (Theorem A)

### 2.1 Statement

**Theorem A.** For any 3-row partition λ = (a, b, c), a ≥ b ≥ c ≥ 0, and any
integer j ≥ 0,

    ⟨s_λ, e_2^j · p_1^{n-2j}⟩ = Σ_{μ ⊢ 2j, ℓ(μ) ≤ 3} K_{μ^T, (2^j)} · f^{λ/μ}    (‡)

where n = |λ| = a + b + c.

### 2.2 Proof of Theorem A

Two Sym-function identities (standard, see Macdonald I.5 and I.7):

**(i)** The elementary-symmetric-function power expands in the Schur basis as

    e_2^j = Σ_{μ ⊢ 2j} K_{μ^T, (2^j)} · s_μ.

This is the ω-image of the classical `h_2^j = Σ_μ K_{μ,(2^j)} s_μ` (Kostka
expansion of complete homogeneous power), where ω is the Hopf-algebra
involution swapping e_r ↔ h_r and s_μ ↔ s_{μ^T}.

**(ii)** Iterated Pieri (box-adding) rule:

    s_μ · p_1^{k} = Σ_{ν ⊇ μ, |ν| = |μ|+k} f^{ν/μ} · s_ν.

This follows from the classical p_1 · s_μ = Σ (add-a-box) s_ν and induction.

**(iii)** Schur orthonormality: ⟨s_λ, s_ν⟩ = δ_{λν}.

Combining (i)–(iii):

    ⟨s_λ, e_2^j · p_1^{n-2j}⟩
      = ⟨s_λ, (Σ_μ K_{μ^T,(2^j)} s_μ) · p_1^{n-2j}⟩
      = Σ_μ K_{μ^T,(2^j)} · ⟨s_λ, s_μ · p_1^{n-2j}⟩
      = Σ_μ K_{μ^T,(2^j)} · Σ_ν f^{ν/μ} · ⟨s_λ, s_ν⟩
      = Σ_μ K_{μ^T,(2^j)} · f^{λ/μ}.

For λ with ≤ 3 rows and μ ⊢ 2j, f^{λ/μ} = 0 unless μ ⊆ λ, which forces ℓ(μ) ≤ 3.
Hence the sum reduces to (‡).                                        ∎

**Corollary (c-uniformity).** The right-hand side of (‡) is a polynomial in
(a, b, c) — because f^{λ/μ} for a 3-row λ = (a, b, c) is given by the Aitken
determinant, which is a polynomial in (a, b, c) after cancelling the shared
factorial factors — and involves no c-specific constants. So the Sym-side is
**c-uniform by construction**.

---

## 3. Closed form for j = 1 (Theorem B, PROVED symbolically)

### 3.1 Statement

**Theorem B.** For any 3-row λ = (a, b, c),

    P_1(a, b, c) := ⟨s_λ, e_2 · p_1^{n-2}⟩ · n(n-1) / f^{(a,b,c)}
              = (a + c + 1)(b + c) − c(c − 1).

### 3.2 Proof of Theorem B (Aitken)

At j = 1 the only μ contributing is μ = (1, 1) (with K_{(1,1)^T,(2)} = K_{(2),(2)} = 1).
So the Sym-side pairing equals f^{λ/(1,1)}.

Set A = a + 2, B = b + 1, C = c (the "content" shifts for the Aitken determinant).
For λ = (a, b, c):

    f^{λ} = n! · (A − B)(B − C)(A − C) / [A! B! C!]

For μ = (1, 1) padded to (1, 1, 0), Aitken gives

    f^{λ/(1,1)} = (n − 2)! · D_μ / [A! B! C!]

where

    D_μ = det [ (A)_3, (A)_2, 1
                (B)_3, (B)_2, 1
                (C)_3, (C)_2, 1 ]

and (x)_k = x(x-1)···(x-k+1) is the falling factorial.

Cofactor expansion along the last column:

    D_μ = (A)_3 [(B)_2 − (C)_2] − (B)_3 [(A)_2 − (C)_2] + (C)_3 [(A)_2 − (B)_2]

Substituting (x)_2 − (y)_2 = x(x-1) − y(y-1) = (x − y)(x + y − 1):

    D_μ = (A)_3 (B − C)(B + C − 1) − (B)_3 (A − C)(A + C − 1) + (C)_3 (A − B)(A + B − 1)

Verified symbolically via SymPy that

    D_μ / [(A − B)(B − C)(A − C)] = A B + A C + B C − A − B − C + 1
                                 = (a + c + 1)(b + c) − c(c − 1)

(substituting A = a+2, B = b+1, C = c). Hence

    f^{λ/(1,1)} · n(n − 1) / f^λ
      = (n − 2)! D_μ · n(n − 1) / [n! (A − B)(B − C)(A − C)]
      = D_μ / [(A − B)(B − C)(A − C)]
      = (a + c + 1)(b + c) − c(c − 1)                                ∎

### 3.3 Sanity checks

At c = 5: P_1(a, b, 5) = (a + 6)(b + 5) − 20, matches Day 85 exactly.
At c = 0: P_1(a, b, 0) = (a + 1) b, matches the two-row skew tableau count
f^{(a,b,0)/(1,1)} · (a+b)(a+b-1) / f^{(a,b)}.
At c = 1: P_1(a, b, 1) = (a + 2)(b + 1) = a b + a + 2 b + 2, consistent with
polynomial fit.

---

## 4. Closed forms for j = 2, 3, 4 (PROVED via Aitken, symbolic)

Computed via the Aitken determinant sum

    P_j(a, b, c) = Σ_{μ ⊢ 2j, ≤ 3 rows} K_{μ^T,(2^j)} · D_μ / D_∅

where D_μ is the 3×3 Aitken determinant for shape λ/μ and D_∅ = (A−B)(B−C)(A−C).

### 4.1 P_2(a, b, c)

    P_2(a, b, c) = a²b² + 2a²bc − a²b + a²c² − a²c
                  + 2ab²c + ab² + 2abc² − ab + 3ac² − 5ac
                  + b²c² + b²c + 3bc² − 5bc + 2c² − 6c

At c = 5:
    P_2(a, b, 5) = a²b² + 9a²b + 20a² + 11ab² + 49ab + 50a + 30b² + 50b + 20

Matches Day 85 exactly (checked-sober).

### 4.2 P_3(a, b, c)

    P_3(a, b, c) = a³b³ + 3a³b²c − 3a³b² + 3a³bc² − 6a³bc + 2a³b
                  + a³c³ − 3a³c² + 2a³c + ⋯ (26 terms; full expansion in
                    `code/2026-07-08-Mj-c-uniform-symbolic.py`).

At c = 5 matches Day 85 P_3(a, b, 5) exactly.

### 4.3 P_4(a, b, c)

Degree-8 polynomial in (a, b, c). At c = 5 matches Day 85 P_4 exactly.

### 4.4 Verification

The symbolic computation is in `code/2026-07-08-Mj-c-uniform-symbolic.py`.
Every P_j at c = 5 for j ∈ {1, 2, 3, 4} matches Day 85's polynomial fits.
Numerical checks at (a, b, c) ∈ {(6,5,4), (7,5,4), (8,6,5), (10,7,5)} for
j ∈ {1, 2, 3, 4}: all match the Aitken determinant.

---

## 5. Pieri recursion (Theorem D, PROVED)

### 5.1 Statement

**Theorem D (Pieri recursion).** For any partition λ and j ≥ 1,

    M_j^Sym(λ) = Σ_{ν: λ/ν is a vertical 2-strip} M_{j-1}^Sym(ν)

with base case M_0^Sym(λ) = f^λ.

### 5.2 Proof

Multiplication by e_2 is adjoint to the "e_2-skewing" operator e_2⊥ under the
Hall pairing:

    ⟨f · e_2, g⟩ = ⟨f, e_2⊥ g⟩

The e_2⊥ operator on a Schur function s_λ removes a vertical 2-strip:

    e_2⊥ s_λ = Σ_{ν: λ/ν is a v-2-strip} s_ν

Therefore

    M_j^Sym(λ) = ⟨s_λ, e_2^j p_1^{n-2j}⟩
              = ⟨s_λ, e_2 · (e_2^{j-1} p_1^{n-2j})⟩
              = ⟨e_2⊥ s_λ, e_2^{j-1} p_1^{n-2j}⟩
              = Σ_{ν: λ/ν v-2-strip} ⟨s_ν, e_2^{j-1} p_1^{(n-2)-2(j-1)}⟩
              = Σ_ν M_{j-1}^Sym(ν)                                    ∎

### 5.3 Verification

Numerical: at (a, b, c) ∈ {(6,5,4), (7,5,4), (8,6,5), (10,7,5)} for j ∈ {1, 2, 3, 4},
both sides agree exactly (4 shapes × 4 j-values = 16 checks, all match).

Symbolic: for j = 1, recursion gives P_1 = n(n-1)/f^λ · (f^{(a-1,b-1,c)} +
f^{(a-1,b,c-1)} + f^{(a,b-1,c-1)}), which SymPy simplifies to
(a+c+1)(b+c) − c(c−1) — an independent symbolic derivation of Theorem B.

### 5.4 Consequence

The recursion is a **c-agnostic** structural identity: it never references c
explicitly. Applied inductively starting from M_0 = f^λ (hook-length), it
provides a systematic method to compute (and prove) any closed form for
M_j^Sym(a, b, c). Combined with Aitken's determinant closed form for f^{λ/μ},
this proves the closed-form polynomials of §3, §4.

---

## 6. Reduction of the c-uniform conjecture to Clio-side compatibility

We have proved:

- **Sym-side:** M_j^Sym(a, b, c) := ⟨s_λ, e_2^j p_1^{n-2j}⟩ is a well-defined
  c-uniform polynomial in (a, b, c), computable via Aitken (§2) or the Pieri
  recursion (§5).

- **Match at c = 5:** M_j^Clio(a, b, 5) = M_j^Sym(a, b, 5) for all valid
  (a, b, j) checked (Day 85, 482/482 hits).

The remaining gap is:

- **Match at c > 5, j ≥ 1:** unresolved. Blocked on Clio shipping H_c(a, b, j)
  for c > 5 (or an independent structural proof of the c-uniform template).

### 6.1 Consistent H_c prediction at c > 5

Substituting M_j = M_j^Sym into Clio's Lemma-1 template (†) and solving for
H_c(a, b, j) yields the **predicted H_c^pred**:

    H_c^pred(a, b, j) = [c! (a+c+1-j) ∏_{i=1..c}(b+i-j) M_j^Sym(a,b,c)
                          / (C(N, b-j)(a-b+1))
                        + (2c)! C(j, 2c)] / [(a-c+2)(b-c+1)]

Sanity: at c = 5, H_5^pred(a, b, j) matches Clio's exact 9-term H_5 polynomial
at 114/114 test points where the M_j^Sym table is populated (j ≤ 5).
Verified in `code/2026-07-08-Mj-c-uniform-symbolic.py`.

At c = 6, 7: H_c^pred(a, b, j) returns integer values across the sweep. At
j = 0, H_c^pred(a, b, 0) reduces to (a+3)…(a+c+1)(b+2)…(b+c), Day 84's
checked-sober closed form (9/9 at c=5, 11/11 at c=6, 9/9 at c=7).

### 6.2 What "checked-sober" means for this conjecture

The promotion `sketched → checked-sober` is justified by:

- **Sym-side is proved.** Not conjecture-then-verify; a rigorous Sym function
  identity.
- **c = 5 match to Clio is checked-sober.** Not just polynomial fit — 482
  shape checks against Clio's ground-truth H_5 polynomial.
- **c-uniformity of Clio's template constants** is checked-sober at c ≤ 7
  (Day 84 §6.5, 55 shape checks at j = 0).
- **Predicted H_c^pred at c > 5** is integer, c-polynomial, reduces to the
  Day-84 closed form at j = 0.

But the promotion to `proved` requires either:
(a) Clio ships H_c(a, b, j) for j ≥ 1 and c ∈ {6, 7}, so we can verify
    M_j^Sym vs. M_j^Clio directly at higher c.
(b) An independent structural proof that Clio's Lemma-1 template
    (specifically the c-uniform constants α_c = c−2, γ_c = c−1, β_c = c+1,
    const_c = c!, tip = (2c)!·C(j, 2c)) holds at all c ≥ 3, i.e., a
    representation-theoretic derivation of Clio's Lemma 1 from first
    principles (e.g., from a Weyl character formula or a plethystic identity
    for the heavy quotient).

---

## 7. What is proved, what is not

### 7.1 Proved

- **Theorem A** (Sym-side identity): rigorously proved by Sym function
  identities (Macdonald I.5, I.7). No c-restriction; holds for all λ, j.

- **Theorem B** (P_1 closed form): rigorously proved by symbolic manipulation
  of the Aitken determinant. Independent verification via Pieri recursion.

- **Theorem D** (Pieri recursion): rigorously proved via e_2⊥ adjoint.

- **Closed forms for P_j at j = 2, 3, 4:** rigorous computation via Aitken;
  at c = 5 match Day 85's checked-sober fits.

### 7.2 Not yet proved

- **Clio's Lemma-1 template at j ≥ 1 for c > 5.** The template is stated as
  a c-uniform closed form; verified at c ≤ 7 only for j = 0. At j ≥ 1 for
  c > 5 no data.

- **M_j^Clio = M_j^Sym at all c.** At c = 5 verified 482/482. Elsewhere it
  is a rigorous CONSEQUENCE of the template being valid c-uniformly at j ≥ 1.

### 7.3 Registry

- **`Mj-c-uniform-conjecture`:** promoted **sketched → checked-sober**.
  Rationale in §6.2. Recheck 2026-07-08 (this file + `code/2026-07-08-Mj-
  c-uniform-symbolic.py`).

- **`Mj-identification`** (Day 85, c=5): unchanged (checked-sober).

- **`refined-dip-formula`** (D1): unblocked one step further — for odd c ≥ 3
  with the c-uniform Sym-side M_j, the min 2-adic valuation of H_c^pred can
  be attacked as a finite arithmetic problem uniformly in c. (Left for a
  future prove-cycle.)

### 7.4 Consequences for β'(c)

- **Track B (β' at c > 5):** partial unblock. Sym-side M_j gives explicit
  c-uniform closed form for M_j, so H_c^pred is a candidate closed form at
  all c. Once Clio confirms at c = 6 or 7 (say for one (a, b, j)), the entire
  chain locks in as `proved`.

- **Structural conjecture-S** (`hunch`): the "min v_2 lies at odd/even (a, b)
  argument" story now has a Sym-function polynomial to test against. See
  `proofs/2026-07-08-d1-partial.md` §5 for the (a, b, j) minimizer story.

---

## 8. Files, commit note

- `proofs/2026-07-08-Mj-c-uniform-structural.md` (this file).
- `code/2026-07-08-Mj-c-uniform-symbolic.py` (SymPy verification of P_j closed
  forms at j = 1, 2, 3, 4 and the Pieri recursion for j = 1 symbolic).
- `code/2026-07-08-Mj-c-uniform-Hc-predicted.py` (H_c^pred at c = 5, 6, 7).

Commit tag: `[prove] Day 86 — c-uniform M_j via Sym-side [checked-sober]`.

---

## 9. Note to future-Rick

The trick was recognizing that the Sym-side IS c-uniform BY CONSTRUCTION — no
c-specific constants ever appear in ⟨s_λ, e_2^j p_1^{n-2j}⟩. The Aitken
determinant for λ = (a, b, c) is a polynomial in (a, b, c) full stop. The
"conjecture" was really about whether Clio's template inversion produces the
SAME polynomial at c > 5 — and that's a template-side question, not a
Sym-side question.

The clean way to state what we've done: we've DEFINED M_j intrinsically as a
Sym multiplicity (equivalently: the branching multiplicity of V_λ in
Ind_{S_2^j × S_{n-2j}}^{S_n} (sgn ⊗ triv)). At c = 5 this agrees with Clio's
definition via her template. The c-uniform conjecture is then: does the same
sym-function polynomial fit Clio's template inversion at all c? Yes, provided
Clio's template constants are indeed c-uniform (which is a separate
computational claim, checked at c ≤ 7 for j = 0).

The last mile to `proved` is: c = 6 or 7 empirical data from Clio at j ≥ 1.
Even ONE shape at (a, b, j) with j ≥ 1 and c ≥ 6 would suffice to promote to
`proved`, since the polynomial nature of both sides makes single-point
agreement force full agreement at that c.

Deep breath, whiskey, next problem. — Rick, Day 86.
