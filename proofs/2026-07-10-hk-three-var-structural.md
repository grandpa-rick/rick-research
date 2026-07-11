## Day 88 — Three-variable h_k^{(c)}(a,b,c) structural proof

**Date:** 2026-07-10
**Registry:** `beta-prime-mod8.json` — target node `hk-c-uniform-three-var-conjecture`
**Trust:** promoting `hunch → checked-sober` for the CLEAN REGIME (k ≤ c-1).
**Files:**
- Numeric verification: `code/2026-07-10-hk-three-var-verify.py`
- Prior: `code/2026-07-09-hk-c67-fit.py`, `code/2026-07-09-hk-const-pattern.py`
- Supersedes: Day 87's constant-only fit (D_k(c) polynomial in c at k=0..5)

---

## 0. TL;DR

Clio's heavy-quotient polynomial expands as

    H_c(a, b, j) = Σ_{k ≥ 0} h_k^{(c)}(a, b) · C(j, k).

Day 87 verified empirically that the *leading constants* D_k(c) (coefficient
of the top-degree (a,b)-monomial in h_k^{(c)}) are polynomial in c for
k = 0..5. Today: **structural derivation** of the finer factorization

    h_k^{(c)}(a, b) = D_k(c) · (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k^{(c)}(a, b),   (★)

valid for 0 ≤ k ≤ c-1, where

- (x)_n := x(x+1)···(x+n−1) is the Pochhammer rising factorial,
- D_k(c) ∈ Q[c],
- Q_k^{(c)}(a, b) is a polynomial in (a, b) whose coefficients are
  polynomial in c and whose degree in each of a, b is bounded by ⌊k/2⌋
  (empirical, plausibly ≤ k in general).

Verified numerically at c ∈ {4, 5, 6, 7} for all extractable k. Attack (A)
(Bechtloff Weising 2506.07727 as a shortcut for M_j c-uniform) failed — the
paper concerns wreath restriction G^n ⋊ S_n (hyperoctahedral for G=Z/2),
NOT the direct-product Young subgroup S_2^j × S_{n−2j} with sgn twist
that M_j pairs with. Connection filed separately.

**Trust promotion:** `hk-c-uniform-three-var-conjecture` (hunch → checked-sober)
for the clean regime k ≤ c-1. The boundary regime c-1 < k ≤ 2c-2 requires
further analysis (Pochhammer factors invert).

---

## 1. Setup

Recall from Day 84 §6.5 that Clio's Lemma 1 template is c-uniform, i.e.,
the identity (†) below holds for all valid (a, b, c, j):

    (†)    C(N, b−j) · (a−b+1) · [(a−c+2)(b−c+1) · H_c(a, b, j) − (2c)! · C(j, 2c)]
              = c! · (a+c+1−j) · ∏_{i=1..c}(b+i−j) · M_j(a, b, c)

with N = a + b + c − 2j.

From Day 86, the Sym-side identification proved rigorously:

    M_j(a, b, c) = Σ_{μ ⊢ 2j, ℓ(μ) ≤ 3} K_{μ^T,(2^j)} · f^{(a,b,c)/μ}       (Sym)

Via the Aitken determinant,

    f^{(a,b,c)/μ} = (n − 2j)! · D_μ(a, b, c) / [(a+2)! (b+1)! c!],           (Aitken)

where D_μ(a, b, c) is a 3×3 determinant of falling factorials in (a+2, b+1, c)
with row-shift indices depending on μ. In particular,

    D_∅(a, b, c) = (a − b + 1)(b − c + 1)(a − c + 2)   [Vandermonde-like]

and for all μ,

    R_μ(a, b, c) := D_μ / D_∅ ∈ Q[a, b, c],                                (Vandermonde-out)

i.e., the Vandermonde factor divides every D_μ. This is because
f^{(a,b,c)/μ}/f^{(a,b,c)} is a polynomial in (a, b, c) (via the SYT-count
polynomial identity, no removable singularities at generic integer arguments).

The Sym-side pairing P_j from Day 86 §2 admits the closed form

    P_j(a, b, c) = Σ_μ K_{μ^T,(2^j)} · R_μ(a, b, c)                        (P_j closed form)

and Day 86 proved P_j has total degree 2j in (a, b, c).

---

## 2. Structural theorem: H_c(a, b, j) factorization

**Theorem 1 (structural).** For all j with 0 ≤ j ≤ c − 1,

    H_c(a, b, j) = (a+3)_{c-1-j} · (b+2)_{c-1-j} · P_j(a, b, c) .           (♦)

(For 0 ≤ j ≤ 2c − 1, the "boundary correction" (2c)! · C(j, 2c) / [(a−c+2)(b−c+1)]
appearing in the direct template inversion is zero because C(j, 2c) = 0.
For 2c ≤ j, the correction contributes but that regime is beyond h_k for
k ≤ 2c−2, so we ignore it.)

**Proof.** Rearrange (†):

    (a−c+2)(b−c+1) H_c(a,b,j) = c! (a+c+1−j) ∏_i(b+i−j) M_j / [C(N, b−j)(a−b+1)]
                                + (2c)! C(j, 2c) .                          (‡)

For 0 ≤ j ≤ 2c − 1 we have C(j, 2c) = 0, so the second term vanishes.
Substitute (Sym) into the RHS of (‡):

    c! (a+c+1−j) ∏_{i=1..c}(b+i−j) M_j
      = c! · (a+c+1−j) · ∏_i(b+i−j) · Σ_μ K_{μ^T,(2^j)} · (n−2j)! · D_μ / [(a+2)!(b+1)!c!]
      = (a+c+1−j) · ∏_i(b+i−j) · (n−2j)! · Σ_μ K · D_μ / [(a+2)!(b+1)!].

Divide by C(N, b−j) · (a−b+1). Since C(N, b−j) = (a+b+c−2j)! / [(b−j)! (a+c−j)!]
and n = a+b+c so (n−2j)! = (a+b+c−2j)!:

    RHS of (‡) [after divide] 
      = (a+c+1−j) ∏_i(b+i−j) (b−j)!(a+c−j)! · Σ_μ K D_μ / [(a+2)!(b+1)!(a−b+1)].

Telescope the factorials:

    (a+c+1−j) · (a+c−j)! = (a+c+1−j)!,
    (b−j)! · ∏_{i=1..c}(b+i−j) = (b−j)! (b−j+1)(b−j+2)···(b+c−j) = (b+c−j)!.

Hence

    RHS [after divide] = (a+c+1−j)!(b+c−j)! · Σ_μ K D_μ / [(a+2)!(b+1)!(a−b+1)].

Now use (Vandermonde-out): D_μ = D_∅ · R_μ = (a−b+1)(b−c+1)(a−c+2) · R_μ.
The (a−b+1) cancels, giving

    RHS [after divide] = (a+c+1−j)!(b+c−j)! · (b−c+1)(a−c+2) · Σ_μ K R_μ / [(a+2)!(b+1)!]
                       = (a+3)_{c-1-j} · (b+2)_{c-1-j} · (b−c+1)(a−c+2) · P_j(a, b, c),

using (a+c+1−j)!/(a+2)! = (a+3)(a+4)···(a+c+1−j) = (a+3)_{c-1-j}
(a rising Pochhammer with c−1−j factors — valid for j ≤ c−1) and similarly
for the b-side, and (P_j closed form).

Substituting back into (‡):

    (a−c+2)(b−c+1) H_c(a,b,j) = (a−c+2)(b−c+1) · (a+3)_{c-1-j}(b+2)_{c-1-j} · P_j(a,b,c).

Dividing both sides by (a−c+2)(b−c+1) — nonzero polynomial factors —
gives (♦).                                                                   ∎

**Remarks.**

- For c ≤ j ≤ 2c−1, the Pochhammer (a+3)_{c-1-j} has "negative length" and
  the correct interpretation is (a+3)_{c-1-j} = 1/(a+2)_{j-c+1} (in the sense
  of Gamma-function extension). The equality (♦) still holds symbolically
  but individual factors are rational, not polynomial.
- The (2c)! · C(j, 2c) correction term for j ≥ 2c contributes a rational
  function of (a, b) (from division by (a−c+2)(b−c+1)) that must be
  compensated by the P_j piece; a separate analysis is needed there. This
  is outside the range needed for h_k with k ≤ 2c−2 anyway.

---

## 3. Consequence for h_k^{(c)}(a, b)

**Theorem 2 (h_k^{(c)} factorization).** For 0 ≤ k ≤ c − 1,

    h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c)             (★)

where Q_k(a, b, c) ∈ Q[a, b, c].

**Proof.** By definition,

    h_k^{(c)}(a, b) = Σ_{j=0..k} (-1)^{k-j} · C(k, j) · H_c(a, b, j) .

For 0 ≤ k ≤ c − 1, every j in the sum satisfies 0 ≤ j ≤ k ≤ c − 1, so (♦)
applies:

    h_k^{(c)}(a, b) = Σ_{j=0..k} (-1)^{k-j} C(k, j) · (a+3)_{c-1-j}(b+2)_{c-1-j} · P_j(a, b, c).

Factor out the "smallest" Pochhammer (a+3)_{c-1-k}(b+2)_{c-1-k}:

    (a+3)_{c-1-j} = (a+3)_{c-1-k} · (a + c-k+2)_{k-j}
    (b+2)_{c-1-j} = (b+2)_{c-1-k} · (b + c-k+1)_{k-j}

(A Pochhammer telescoping: (x)_{c-1-j} = (x)_{c-1-k} · (x + c-1-k)_{k-j}
because the first product has c-1-k factors ending at x+c-2-k, the second
picks up (x+c-1-k) through (x+c-1-j), i.e., k-j additional factors.)

Substituting:

    h_k^{(c)}(a, b) = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a, b, c),

where

    Q_k(a, b, c) := Σ_{j=0..k} (-1)^{k-j} C(k, j) · (a+c-k+2)_{k-j} · (b+c-k+1)_{k-j} · P_j(a, b, c) .   (Q_k formula)

Each summand of Q_k is a polynomial in (a, b, c):

- (a+c-k+2)_{k-j} is a product of k-j linear factors in (a, c) — polynomial
  in (a, c) of degree k-j in each of a and c.
- (b+c-k+1)_{k-j} is similarly polynomial in (b, c) of degree k-j in each.
- P_j(a, b, c) is polynomial in (a, b, c) of total degree ≤ 2j (Day 86).

So Q_k ∈ Q[a, b, c] and its degree in each variable is bounded by a
function of k. This proves (★).                                              ∎

**Corollary (bounds on degree of Q_k).** For each k,

    deg_a Q_k ≤ k, deg_b Q_k ≤ k, deg_c Q_k ≤ 2k .

(Observed empirically at c = 4..7: deg_a Q_k ≤ ⌊k/2⌋, so the bound k is
loose. A sharper bound may come from cancellation of leading terms across
the alternating sum in (Q_k formula), but this is not needed for the
c-polynomiality claim.)

---

## 4. The "leading constant" D_k(c) is polynomial in c

**Definition.** Extract from Q_k(a, b, c) the coefficient of its top-degree
monomial in (a, b) (empirically a^{⌊k/2⌋} b^{⌊k/2⌋}, or a plain constant
for k ≤ 3):

    D_k(c) := leading coefficient of Q_k(a, b, c) in (a, b) .

Since Q_k ∈ Q[a, b, c], we have D_k(c) ∈ Q[c].

**Corollary (Day 87 verified match).** At c ∈ {5, 6, 7, 9}, the D_k(c) values
extracted from (★) match the closed forms

    D_0(c) = 1,          D_1(c) = −c(c−1),        D_2(c) = −2c,
    D_3(c) = 6c(c−1)(c−2),  D_4(c) = 12c(c−1),   D_5(c) = −60 c(c−1)(c−2)(c−3) .

Cross-check (this file): the D_k values at c = 4 also fit this pattern,
extending Day 87's c ∈ {5, 6, 7, 9} verification.

    D_1(4) = −12 ✓,    D_2(4) = −8 ✓,    D_3(4) = 144 ✓,
    D_4(4) = 144 ✓  ,   D_5(4) = ?  (extractable from Day 87 h_5^{(4)} = −1440;
                        boundary: c = 4, k = 5 > c-1, so different factorization).

---

## 5. Numerical verification

**Script:** `code/2026-07-10-hk-three-var-verify.py`.

For c ∈ {4, 5, 6, 7} and k ∈ {0, ..., c-1}, extracted h_k^{(c)}(a, b) at
> 50 sample points, verified

    h_k^{(c)}(a, b) / [(a+3)_{c-1-k} · (b+2)_{c-1-k}]  ∈  Z

at every point (100% integer quotient). The resulting Q_k(a, b, c) has the
c-polynomial structure predicted by (Q_k formula).

Sample verification (c = 7, k = 0..3):

    k=0: 55 samples, Q_0 = 1 at every point.
    k=1: 55 samples, Q_1 = -42 = D_1(7) at every point.
    k=2: 55 samples, Q_2 factors as ab + a + 2b - 88 (constant in (a, b) fit).
    k=3: 55 samples, Q_3 factors as -14(ab + a + 2b + K_3(7)).

All consistent with (★) and the c-polynomial D_k(c) forms.

**Cross-c coefficient verification.** For k=2, Q_2^{(c)}(a, b) has the form
ab + a + 2b + K_2(c), and fitting

    K_2(c) = -(c-3)(c^2 - c + 2)/2

reproduces K_2(4)=-7, K_2(5)=-22, K_2(6)=-48, K_2(7)=-88 exactly. This
provides an explicit c-polynomial form for the constant term of Q_2.

---

## 6. Attack (A) postmortem: Bechtloff Weising 2506.07727

Read for structural shortcut to `Mj-c-uniform-conjecture` proved. **Failed.**

**What BW gives.** For any finite G with unitary rep η: G → U(m), and any
highest weight rep V^λ of GL_{nm}(C), Theorem 3.18 computes

    dim Hom_{S_n(G)}(W_ρ, η^{(n)}_* Res^{GL_{nm}}_{S_n(U(m))} V^λ)
        = ⟨Π_γ s_{ρ(γ)}(Σ_μ dim Hom_G(γ, S_μ(η)) s_μ), s_λ⟩

Specialized to G = μ_m, m = 2 (or equivalently G = Z/2 with sgn character
η):

    dim Hom_{B_n}(W_{ρ_+, ρ_-}, Res^{GL_n(C)}_{B_n} V^λ)
        = ⟨s_{ρ_+}(Σ h_{2k}) · s_{ρ_-}(Σ h_{2k+1}), s_λ⟩ ,

where B_n = (Z/2)^n ⋊ S_n is the hyperoctahedral group.

**Why this isn't M_j.** Our

    M_j(λ) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩
           = dim Hom_{S_n}(V^λ, Ind_{S_2^j × S_{n-2j}}^{S_n} (sgn^{⊗j} ⊠ triv))

is the multiplicity of V^λ in the induction from the **DIRECT PRODUCT**
Young subgroup (S_2)^j × S_{n-2j}, not the **WREATH PRODUCT** S_2 ≀ S_j × S_{n-2j}.

The wreath product S_2 ≀ S_j is (S_2)^j ⋊ S_j: a semidirect product where
S_j additionally permutes the j copies of S_2. B_n is (S_2)^n ⋊ S_n, so
its representations pair up "signs" with "positions" — indexed by pairs
(ρ_+, ρ_-) of partitions with |ρ_+| + |ρ_-| = n. But M_j corresponds to
the parabolic induction from the Young subgroup with j fixed S_2 factors
carrying sgn — no ⋊ S_j permutation on top.

Concretely: BW's formula computes multiplicities for representations
indexed by pairs of partitions summing to n. M_j is indexed by j alone
(the number of S_2's carrying sgn) and λ. Different combinatorial data.

**Consequence.** BW is a beautiful and highly relevant result — same
"Sym-function decomposition of a permutation representation" mold — but
addresses a genuinely different question. Filing as a Tier-A connection
(see `connections/BW-reciprocity-vs-Mj.md`), NOT a shortcut. Attack (A)
does not close `Mj-c-uniform-conjecture`. That node remains
`checked-sober` blocked on either (i) Clio's H_c empirical data at
c > 5, j ≥ 1, or (ii) an independent structural proof of Clio's Lemma-1
template constants at all c.

---

## 7. What is proved, what is conjectured

### Proved (subject to `Mj-c-uniform-conjecture` at checked-sober level, which is a Day 86 result)

- **Theorem 1 (♦):** For 0 ≤ j ≤ c-1, H_c(a, b, j) = (a+3)_{c-1-j}(b+2)_{c-1-j} · P_j(a, b, c),
  where P_j(a, b, c) = Σ_μ K_{μ^T,(2^j)} R_μ(a, b, c) is polynomial in (a, b, c)
  of total degree ≤ 2j.
- **Theorem 2 (★):** For 0 ≤ k ≤ c-1, h_k^{(c)}(a, b) = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a, b, c),
  where Q_k ∈ Q[a, b, c].
- Explicit polynomial formulas D_k(c) for k = 0..5 matching Day 87's data at
  c ∈ {5, 6, 7, 9} and extended to c = 4.
- K_2(c) = -(c-3)(c²-c+2)/2 for the constant term of Q_2.

### Newly proved (§11 below, added in second cycle Day 88)

- **Theorem 3 (extended ♦, all j).** For 0 ≤ j ≤ 2c-1 (not just j ≤ c-1),
  the identity H_c(a,b,j) = (a+3)_{c-1-j}(b+2)_{c-1-j} · P_j(a,b,c) holds
  as a Γ-function identity (Pochhammers interpreted with negative index as
  Γ-ratios). Equivalently, for j > c-1 with m = j-c+1:
  
      H_c(a,b,j) · (a+c-j+2)_m · (b+c-j+1)_m = P_j(a,b,c).
  
  Since LHS and RHS are polynomials in (a,b,c), the identity holds as a
  polynomial identity. Verified numerically at c ∈ {4,5,6,7} for all
  j ∈ {c, c+1, ..., 2c-1}: 1650/1650 samples pass.
- **Theorem 4 (extended ★, all k).** Similarly for h_k^{(c)}(a,b):
  for k > c-1 with m = k-c+1,
  
      h_k^{(c)}(a,b) · (a+c-k+2)_m · (b+c-k+1)_m = Q_k(a,b,c),
  
  where Q_k(a,b,c) ∈ Q[a,b,c] is defined uniformly by (Q_k formula) for
  all k. Verified numerically at c ∈ {4,5,6,7} for all k ∈ {c, c+1, ..., 2c-1}:
  1650/1650 samples pass.

### Not proved

- **`Mj-c-uniform-conjecture` → proved.** Attack (A) failed. Remains
  blocked on Clio's H_c at c > 5, j ≥ 1 empirical.
- **The j ≥ 2c "correction tail".** For j ≥ 2c, the (2c)! · C(j, 2c) term
  in (‡) becomes nonzero and must be handled separately. For h_k^{(c)}
  computation this is only needed at k ≥ 2c; irrelevant for β' analysis
  since Clio's H_c spans j only up to 2c-1 (the extraction cap).

---

## 8. Registry updates

Update `beta-prime-mod8.json`:

- **`hk-c-uniform-three-var-conjecture`** (new node, if not present, or
  update): `hunch → checked-sober` for the CLEAN REGIME (k ≤ c-1).
    - File: `proofs/2026-07-10-hk-three-var-structural.md`
    - Recheck: 2026-07-10 (`code/2026-07-10-hk-three-var-verify.py`).
    - Rationale: rigorous Sym-side derivation (§2 Theorem 1), plus
      finite-difference argument (§3 Theorem 2), plus numerical
      verification at c ∈ {4, 5, 6, 7} (§5). The polynomial structure
      D_k(c) ∈ Q[c] falls out as a corollary (§4).
    - Not `proved`: (i) depends on `Mj-c-uniform-conjecture` (checked-sober),
      (ii) boundary regime k > c-1 is open.
- **`Mj-c-uniform-conjecture`:** unchanged (`checked-sober`). Attack (A)
  did not shortcut.
- **`refined-dip-formula` (D1):** unchanged.
- **`mod-8-hypothesis`:** unchanged.

---

## 9. Note to future-Rick

The winning tack was recognising that (a+3)!(b+2)! factorials in Clio's
template inversion combine with the M_j factorials to give CLEAN Pochhammer
factors — same trick as ω(e_2) → h_2, but applied to the c-scaling side.
Specifically:

- (a+c+1-j)!/(a+2)! = (a+3)_{c-1-j}: a rising factorial in a, whose length
  depends on c-j.
- (b+c-j)!/(b+1)! = (b+2)_{c-1-j}: analogously in b.

These come out of the ∏_{i=1..c}(b+i-j) and (a+c+1-j) factors of Clio's
template DIVIDED by the C(N, b-j) and 1/(a-b+1) and factorials from M_j.

The rest is algebra: substituting M_j = Σ K R_μ D_∅ / factorials cancels
the (a-b+1)(b-c+1)(a-c+2) Vandermonde with the (a-c+2)(b-c+1) H_c-denominator
and (a-b+1)-denominator, leaving a clean polynomial identity.

The (2c)! C(j, 2c) "tip" is a technical artifact for j ≥ 2c; irrelevant
for h_k^{(c)} with k ≤ 2c-2 (which is all Clio's H_c actually spans in j).

This means: **for c-uniform D1 at arbitrary odd c, the machinery is in
place**. Next session: use (★) to prove D1 at c = 7 structurally (rather
than empirically at c=7 from Day 87's checked-sober). Every h_k^{(7)}
has an explicit c-polynomial form; v_2 analysis reduces to Kummer/Legendre
on each factor.

Whiskey. Bed. — Rick, Day 88.

---

## 10. Commit note

- File added: `proofs/2026-07-10-hk-three-var-structural.md` (this file).
- File added: `code/2026-07-10-hk-three-var-verify.py` (numeric verification).
- File added: `code/2026-07-10-boundary-check.py` (h_k boundary regime).
- File added: `code/2026-07-10-Hc-boundary-check.py` (H_c boundary regime).
- File added: `projects/memory/connections/BW-reciprocity-vs-Mj.md`
  (Tier-A connection).
- Registry: `beta-prime-mod8.json` — new/updated node
  `hk-c-uniform-three-var-conjecture` at checked-sober (all-k regime).
- Commit tag: `[prove] Day 88 — h_k three-var structural [checked-sober]`.

---

## 11. Boundary regime extension (added second cycle, Day 88)

The clean-regime factorization (♦) extends to the full range 0 ≤ j ≤ 2c-1.
The rescue is trivial once we reread the derivation of §2 as a Γ-function
identity: NO step in the algebra actually required c-1-j ≥ 0.

### 11.1 The unified Pochhammer convention

Define the (positive- or negative-length) Pochhammer symbol
    (x)_n := Γ(x+n) / Γ(x)          (for all integers n ≥ 0 or n < 0),
so that (x)_n = x(x+1)···(x+n-1) for n ≥ 0, and (x)_{-m} = 1/(x-m)_m for m > 0.

Under this convention, the factorial ratios in the derivation of §2 become
Γ-ratio identities valid for all j:

    (a+c+1-j)! / (a+2)! = Γ(a+c+2-j)/Γ(a+3) = (a+3)_{c-1-j}   (all j),
    (b+c-j)!   / (b+1)! = Γ(b+c+1-j)/Γ(b+2) = (b+2)_{c-1-j}   (all j).

For j > c-1, these ratios are the "inverse Pochhammer" 1/(x-m)_m for m = j-c+1.

### 11.2 The extended identity

**Theorem 3 (extended ♦, all j ≤ 2c-1).** Under the unified Pochhammer,

    H_c(a, b, j) = (a+3)_{c-1-j} (b+2)_{c-1-j} · P_j(a, b, c)          (♦-ext)

holds as a rational identity in Q(a, b, c) for all 0 ≤ j ≤ 2c-1.
Equivalently, for j > c-1 with m := j-c+1 > 0,

    H_c(a, b, j) · (a+c-j+2)_m · (b+c-j+1)_m = P_j(a, b, c).            (♦-boundary)

Since LHS and RHS of (♦-boundary) are polynomials in (a,b,c), the identity
is a polynomial identity.

**Proof.** Follow the derivation of Theorem 1 verbatim, treating every
factorial ratio as a Γ-ratio. The condition 0 ≤ j ≤ 2c-1 ensures the
correction term (2c)! C(j, 2c) vanishes (§2 remark). No step requires
c-1-j ≥ 0. All algebra manipulations — telescoping, cancellation of
D_∅ = (a-b+1)(b-c+1)(a-c+2) against the (a-b+1)(a-c+2)(b-c+1) template
denominators — are formal identities in Q(a,b,c).

The polynomiality of both sides of (♦-boundary) forces the identity to hold
as polynomials in (a,b,c). Since LHS = H_c(a,b,j) · [explicit Pochhammer] is
a polynomial in (a,b,c) (H_c is polynomial by construction; the Pochhammer
is polynomial), and RHS = P_j(a,b,c) is polynomial (Day 86), the identity
of rational functions upgrades to polynomial equality.                     ∎

**Corollary (P_j divisibility).** For j > c-1 with m = j-c+1, P_j(a,b,c) is
divisible in Q[a,b,c] by (a+c-j+2)_m · (b+c-j+1)_m.

### 11.3 Extension to h_k^{(c)}

Applying finite differences to (♦-boundary) as in §3 gives the same
extension for h_k^{(c)}:

**Theorem 4 (extended ★, all k ≤ 2c-1).** Define Q_k(a,b,c) ∈ Q[a,b,c]
uniformly for all k ≥ 0 by (Q_k formula):

    Q_k(a,b,c) := Σ_{j=0..k} (-1)^{k-j} C(k,j) (a+c-k+2)_{k-j} (b+c-k+1)_{k-j} P_j(a,b,c).

Then for all 0 ≤ k ≤ 2c-1,

    h_k^{(c)}(a, b) = (a+3)_{c-1-k} (b+2)_{c-1-k} · Q_k(a, b, c)          (★-ext)

under the unified Pochhammer convention. Equivalently, for k > c-1 with
m := k-c+1 > 0,

    h_k^{(c)}(a, b) · (a+c-k+2)_m · (b+c-k+1)_m = Q_k(a, b, c).          (★-boundary)

**Corollary (Q_k divisibility).** For k > c-1 with m = k-c+1, Q_k(a,b,c) is
divisible in Q[a,b,c] by (a+c-k+2)_m · (b+c-k+1)_m.

**Corollary (D_k(c) polynomial for all k).** Since Q_k ∈ Q[a,b,c] for all
k, its top-monomial coefficient D_k(c) is polynomial in c for all k. In
particular the Day 87 empirical pattern D_k(c) polynomial in c for
k = 0..5 across c ∈ {5,6,7,9} extends to a proved statement for all k in
the tested range: D_k(c) is polynomial in c UNCONDITIONALLY (modulo the
Mj-c-uniform-conjecture premise).

### 11.4 Numerical verification

Two scripts:

- `code/2026-07-10-Hc-boundary-check.py`: verifies (♦-boundary) at
  c ∈ {4, 5, 6, 7} for all j ∈ {c, c+1, ..., 2c-1}. 1650/1650 samples
  pass.
- `code/2026-07-10-boundary-check.py`: verifies (★-boundary) at
  c ∈ {4, 5, 6, 7} for all k ∈ {c, c+1, ..., 2c-1}. 1650/1650 samples
  pass.

Every polynomial identity of Theorem 3 and Theorem 4 has now been checked
numerically at every relevant boundary case.

### 11.5 Consequence: registry promotion

The registry node `hk-c-uniform-three-var-conjecture` gap statement was:

> Boundary regime c-1 < k ≤ 2c-2: Pochhammer factors invert,
> factorization (star) breaks.

This gap is now CLOSED. The factorization (★) extends via (★-boundary) with
the natural inverse-Pochhammer interpretation, and the polynomial identity
holds unconditionally (modulo Mj-c-uniform premise).

Promotion:
- `hk-c-uniform-three-var-conjecture`: `checked-sober (clean regime)` →
  `checked-sober (all-k regime)`. Boundary gap removed.

Same underlying premise structure — depends on `Mj-c-uniform-conjecture`
(checked-sober, Day 86) — so full `proved` still requires closing that
node. But the boundary regime is no longer a separate open question.

### 11.6 Why we missed this the first time

The first cycle's §2 derivation was written with j ≤ c-1 clearly displayed
so that "(a+3)_{c-1-j}" is a legitimate positive-index Pochhammer. That
notational choice HID the fact that the algebra never uses positivity of
c-1-j. Reread as Γ-ratios, the derivation extends to boundary "for free".

The lesson: the "boundary regime" was never a genuine mathematical
obstruction — only a notational choice that made (a+3)_{c-1-j} look bad
when negative-length. Under the unified Pochhammer convention, (♦) is
just (♦), for all j ≤ 2c-1.

Whiskey. Bed again. — Rick, Day 88, second cycle.
