# Deep read: Erdős #728 (arXiv 2601.07421) — Kummer carry technique for Claim B?

**Paper:** *Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof*
**Author:** Nat Sothanaphan
**Date:** Jan 27, 2026 (v5)
**arXiv:** 2601.07421
**One-line thesis:** Establishes a *logarithmic-gap window* for the factorial-divisibility problem
`a!b! | n!(a+b−n)!` by proving `κ_p(m) − V_p(m,k) ≥ c₂ log m / log p` for all small primes
`p ≤ 2k`, via a probabilistic "carry-rich but spike-free" existence argument on `m ∈ [M, 2M]`.
The paper does what Rick's memory said: **it uses Kummer's theorem as a carry-counting tool**,
but the mechanism is a **union-bound + Chernoff argument on base-p digit statistics**, not a
literal binomial-sum-stratification-by-carry-pattern.

---

## 1. The Erdős #728 problem

Given naturals `a, b, n ∈ ℕ³` with the divisibility `a! b! | n! (a+b−n)!`, and `k := a+b−n`,
how large can `k` be relative to `n`? Trivially large-`k` families exist by taking `a, b`
huge, so a lower bound `a, b ≤ (1−ε)n` is imposed. Equivalently, writing `N = a+b`, one asks
for large `k` such that `C(N, k) | C(N, a)`.

## 2. Main theorem (Theorem 1 — "Logarithmic gap window")

Fix `0 < C₁ < C₂` and `0 < ε < 1/2`. Then there exist infinitely many triples
`(a, b, n) ∈ ℕ³` with `εn ≤ a, b ≤ (1−ε)n` such that

```
    a! b! | n! (a+b−n)!    and    C₁ log n < a+b−n < C₂ log n.
```

Terry Tao noted this is not sharp — the true rate is `k = exp(c √log n)`.
The generalized form (Theorem 2, used for Erdős #728, #729, #401) is:

> The set of `m` such that `ν_p(C(2m,m)) − ν_p(C(m+k, k)) ≥ c₂ · log m / log p`
> holds *for all primes `p ≤ 2k`* has asymptotic density 1, provided
> `0 ≤ k ≤ exp(c₁√log m)`.

## 3. Setup — the reduction to a valuation inequality

Set `n = 2m`, `b = m`, `a = m + k` (so `a+b−n = k`, and `b = n/2` while `a` is only slightly
larger than `n/2`). Then

```
    a! b! | n! k!    ⇔    (m+k)! m! | (2m)! k!    ⇔    C(m+k, k) | C(2m, m).
```

Define the three key p-adic quantities:

```
    κ_p(m)   := ν_p(C(2m, m))                    (central binomial)
    W_p(m,k) := ν_p( ∏_{i=1..k} (m+i) )          (rising product)
    V_p(m,k) := max_{1 ≤ i ≤ k} ν_p(m+i)         (max valuation "spike")
```

Since `C(m+k,k) = ∏(m+i)/k!`, Legendre + Kummer give exactly

```
    ν_p( C(m+k,k) ) = W_p(m,k) − ν_p(k!)                (identity (4))
    κ_p(m) = # carries when adding m + m in base p.     (Kummer, Lemma 3)
```

**The target inequality**, needed for every prime `p`, is

```
    W_p(m,k) ≤ κ_p(m) + ν_p(k!).                        (⋆)
```

**Interval bound (Lemma 4).** Legendre-style counting of multiples of `p^j` among `k`
consecutive integers gives `W_p(m,k) ≤ ν_p(k!) + V_p(m,k)`. So it suffices to show

```
    V_p(m,k) ≤ κ_p(m)    for every prime p.             (⋆⋆)
```

This is the heart of the paper. Note the clean separation: the LHS is a **spike**
(how deeply `p` divides one of `m+1, …, m+k`), the RHS is a **carry count** for `m+m`
in base `p`.

## 4. The proof of (⋆⋆)

### 4.1 Large primes `p > 2k` (Lemma 5)

Handled cleanly by a base-`p` digit argument: if `V_p(m,k) = J`, write `m+i = p^J u` with
`p ∤ u`; because `k < p/2`, the last `J` base-`p` digits of `m` are `≥ (p+1)/2` (they come
from `p^J − i`), and adding `m+m` forces a carry at each such position. So `κ_p(m) ≥ J`.

### 4.2 Small primes `p ≤ 2k` — the probabilistic core

Fix a scale `M` and search `m ∈ [M, 2M]`. Set

```
    η := 1/10,    L_p := ⌊(1−η) log M / log p⌋,   J_p := ⌊log_p k⌋,   t(M) := ⌈10 log log M⌉.
```

Let `X_p(m)` = number of the first `L_p` base-`p` digits of `m` that are `≥ ⌈p/2⌉`.
The key elementary lemma:

**Lemma 6 (Forced carries from large digits).**  `κ_p(m) ≥ X_p(m)`. Because when doubling
`m` in base `p`, a digit `a_j ≥ ⌈p/2⌉` forces a carry at position `j`, regardless of
incoming carry.

Set `θ(p) = 1/2` if `p = 2`, else `(p−1)/(2p)`, and `μ_p := L_p θ(p)`, the expected number
of large digits.

Call `m` **good for `p`** if it satisfies both:

```
    X_p(m) ≥ μ_p / 2         (carry condition)
    V_p(m,k) < J_p + t(M)    (no-spike condition)
```

**Lemma 7 (Threshold).** For large `M`, `μ_p / 2 ≥ J_p + t(M) + 3`. So on the good event,
`κ_p(m) ≥ μ_p/2 > J_p + t(M) > V_p(m,k)`, i.e. (⋆⋆).

### 4.3 Existence of a globally-good `m` (Lemma 14)

The bad events are:

```
    BadCarry_p(M) := { m ∈ [M,2M] : X_p(m) < μ_p/2 }
    BadSpike_p(M) := { m ∈ [M,2M] : V_p(m,k) ≥ J_p + t(M) }
```

Both are **unions of residue classes**: BadCarry mod `p^{L_p}`, BadSpike mod `p^{J_p+t(M)}`.

- **BadCarry bound (Lemmas 8, 10, 11).** `X(r)` on random residues mod `p^{L_p}` is exactly
  `Bin(L_p, θ(p))`. Chernoff: `P(X ≤ μ_p/2) ≤ e^{−μ_p/8}`. Multiply by count in interval:
  `|BadCarry_p(M)| ≤ (M+1) e^{−μ_p/8} + 2 p^{L_p}`.
- **BadSpike bound (Lemma 12).** For each `i ∈ {1,…,k}`, `p^{J_p+t(M)} | (m+i)` puts `m`
  in one residue class; sum over `i`: `|BadSpike_p(M)| ≤ (M+1) p^{1−t(M)} + 2k`.
- **Union bound over all primes `p ≤ 2k`** (Lemma 13): total bad set is `< M+1`, so a
  good `m ∈ [M, 2M]` exists.

Finally, `k := ⌊c log M⌋` for `c ∈ (C₁, C₂)`, and `log n = log M + O(1)`, giving the window.

## 5. Extracted key lemma / key identity

The whole load-bearing statement, cleanly extracted:

> **(Key inequality.)** For each prime `p`, `V_p(m, k) ≤ κ_p(m)`,
> equivalently `max_{1 ≤ i ≤ k} ν_p(m+i)  ≤  #{carries in m+m base p}`.

The **method** is:

1. Bound the RHS *below* by an elementary digit statistic: `κ_p(m) ≥ X_p(m)`, the count
   of large base-`p` digits (Lemma 6). This is a **purely local, per-digit** lower bound —
   no cross-digit correlation needed.
2. Bound the LHS *above* by declaring "spikes" — high `p`-power divisibility of `m+i` — as
   rare exceptional residue classes (Lemma 12).
3. Union-bound the bad residue classes across all `p ≤ 2k`.

The **algebraic object** manipulated is not a sum of binomial coefficients — it is
`ν_p` of a **single central binomial** vs. `ν_p` of a **rising product**. The carry
interpretation via Kummer's theorem is applied to one binomial coefficient, not summed
over an index. **This is a valuation-inequality technique, not a valuation-of-a-sum
technique.**

## 6. Structural match to Claim B

Rick's Claim B asks about `v_2 ( Q_{2R}(R−2, R, c) )` for `c ≡ R (mod 16)`. The claim
is that this is constant on the residue class `c ≡ R (mod 16)` and equals `C_R`.

**What is `Q_{2R}(a, b, c)`?** Not stated in the brief — likely a q-Hecke / crystal
character or Kostka-like polynomial specialized at parameters. **This is the pivotal
question.** The paper's technique will transfer *if and only if* `Q_{2R}(R−2, R, c)` can
be written as either

  (a) a **single binomial coefficient** or product of binomials whose arguments are
      linear in `c`, whose 2-adic valuation is then a Kummer carry count, or
  (b) a **short sum** of such where one term dominates 2-adically and the others are
      forced into higher valuation by a spike/carry inequality.

### The concrete match

**Analogy** (paper ↔ Claim B):

| Paper #728                                | Claim B                                    |
| ----------------------------------------- | ------------------------------------------ |
| `ν_p(C(2m,m))` vs `ν_p(∏(m+i))`           | `v_2(Q_{2R}(R−2, R, c))`                   |
| `m` ranges over `[M, 2M]`                 | `c ≡ R (mod 16)` — fixed residue class     |
| Uniform in `p ≤ 2k`                       | Uniform in `R`?                            |
| Show inequality via digit statistics      | Show *equality* of a valuation             |

Two structural mismatches to flag:

1. **Direction of the statement.** #728 proves a one-sided *inequality* (`V ≤ κ`).
   Rick wants an *equality* (`v_2 = C_R`, i.e. two-sided). #728's method gives lower
   bounds on carry counts and upper bounds on spikes with a Chernoff gap; it does not
   pin down valuations exactly. To get *constancy* one needs both `v_2 ≥ C_R` and
   `v_2 ≤ C_R`. The paper's toolkit provides one direction.
2. **Class-invariance in the paper is mod `p^{L_p}`, not mod a fixed small power like
   16.** The residue mod `p^{L_p}` determines `X_p(m)` and thus the carry-based lower
   bound. In Claim B, the residue mod 16 = 2⁴ is fixed *first* and constancy is claimed
   *within* that class. This is stronger than what #728 proves: within a fixed residue
   class mod 16, both `X_2(c)` (fluctuates with digits beyond position 3) and `V_2(m,k)`
   (fluctuates with which `c+i` is divisible by a huge power of 2) will vary. #728
   would only give constancy after averaging, not pointwise.

### What would Rick need to do to make this transfer

Concretely:

1. **Write `Q_{2R}(R−2, R, c)` as a product of falling factorials / binomials.** If
   `Q_{2R}(R−2, R, c) = C(f(c,R), g(c,R)) · (rational units in R)` for some integer-valued
   polynomials `f, g`, then `v_2` reduces to a carry count via Kummer. The empirical
   evidence — that `v_2` is *exactly* `C_R` (not just bounded below) — is consistent with
   a shape where **the number of carries in some base-2 addition is invariant under
   `c ↦ c + 16t`**.
2. **Look for a "stable digit prefix" phenomenon mod 16.** For `c ≡ R (mod 16)`, the
   *low 4 base-2 digits* of `c` are fixed. Rick's `C_R` presumably comes from carries
   in these low positions. Additions `x + y` where `x, y` are polynomials in `c` will
   have most of their carry activity in some fixed low-digit region if the polynomial
   coefficients are appropriately controlled. This is the "sub-Kummer" observation that
   could plausibly give Claim B.
3. **Note that R ∈ {2, 4, 6, 10} are all even.** Sample so far skips `R = 8`. The
   pattern `C_2 = 4, C_4 = 13, C_6 = 18, C_{10} = 34` — is there an obvious `R`-uniform
   formula? A closed form for `C_R` would strongly hint at the underlying binomial /
   carry structure.

## 7. Plausibility verdict

**MEDIUM.** The paper is definitely about `v_p` of binomial coefficients via Kummer carry
counting, so Rick's memory is directionally correct. But:

- The paper's key move is an **upper bound** on `V_p(m,k)` via probabilistic exclusion of
  spikes and a **lower bound** on `κ_p(m)` via forced carries. This produces an *inequality*
  on almost all `m`, not an *equality* on a fixed residue class.
- Claim B needs pointwise-exact valuation on a residue class mod 16. The paper's residue-
  class-of-badness framework (Lemma 8: "bad events are unions of residue classes mod
  `p^L`") is philosophically the right frame, but the machinery outputs "density-1 goodness",
  not "exact value on the class".
- **HIGH plausibility that #728's *framework*** — writing things as carry counts, exploiting
  that the low base-2 digits of `c` are fixed on `c ≡ R (mod 16)`, and using Legendre/Kummer
  identities — is the right first step. **LOW plausibility that #728's *specific main
  argument* (Chernoff + union bound)** transfers, because Claim B is a finite-precision
  algebraic identity, not a density-1 asymptotic.

### Better structural neighbors than #728 itself

The paper cites two more directly relevant works for *residue-class* valuation control:

- **Pomerance, *Divisors of the middle binomial coefficient*, AMM 122 (2015).** Fixed-`k`
  version — for each `k`, the set of `n` with `n+k | C(2n,n)` has density 1. Uses Kummer
  and base-`p` digit patterns. Closer to Claim B in that `k` is fixed.
- **Ford–Konyagin, TAMS 374 (2021).** Density formulas for `n^ℓ | C(2n,n)` — this is
  fixed-exponent, residue-class type control, exactly the flavor of Claim B.
- **Croot–Mousavi–Schmidt, Mathematika 70 (2024).** *Carry-poor* integers in multiple
  simultaneous bases. Also relevant for the multi-modulus flavor.

**These look like more direct model literature for Claim B than #728 itself.**

## 8. Next step for Rick

1. **State `Q_{2R}(a, b, c)` explicitly**, ideally as a closed form or as a sum of
   binomial coefficients. Without this the paper's technique cannot be applied because
   Kummer's theorem needs a specific binomial to act on.
2. **Compute `v_2(C_R)` for `R = 8, 12`** to check the pattern is truly `R`-uniform
   and to extend the numerical evidence for a closed form of `C_R`.
3. **If `Q_{2R}(R−2, R, c)` decomposes as a short sum of binomials `∑ ±C(f_i(c), g_i(c))`,**
   compute Kummer carries for each term at `c = R + 16t` symbolically in `t`. Claim B
   would then reduce to: "one binomial has exactly `C_R` carries at every `c ≡ R (mod 16)`,
   the others have strictly more."
4. **Read Pomerance 2015 (AMM) and Ford–Konyagin 2021 (TAMS)** — these look like closer
   structural analogues than #728 for the *exact-valuation-on-a-residue-class* flavor
   Rick actually needs.
5. If the binomial-sum form of `Q_{2R}` exists, the technique to try is: fix the low 4
   bits of `c`; show that carries in the relevant base-2 additions in bits 0–3 are
   determined by `R mod 16`, while carries beyond bit 3 cancel across the sum (via an
   involution on carry configurations, perhaps). This is a **structural refinement** of
   #728's forced-carry lemma (Lemma 6), specialized to a fixed low-digit pattern.
