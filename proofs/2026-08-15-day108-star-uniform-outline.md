---
name: (★) uniform-in-R proof outline via master identity + recursion (Day 108)
description: Two-part structural derivation of (★) — the level-0 master identity Q_k(-2, b, c) closed form (verified at R=3, R=4 for all k), and the k-level recursion (verified R=3 all levels, R=4 all levels). Reduces (★) to two families of empirically-verified c-polynomial identities.
---

# Uniform derivation of (★) via master identity + recursion — Day 108

## The two structural facts

**(M) MASTER IDENTITY at the a = -2 Weyl boundary (all k):**
$$Q_k(-2, b, c) = (-1)^k \cdot c \cdot (c - k) \cdot \prod_{j=1}^{k-1}(c - j)^2, \qquad k \geq 1. \tag{M}$$

with $Q_0(-2, b, c) = 1$.

**Verified:** R = 3, R = 4, for all applicable k (110 cell tests). Bivariate fits at
each (c, k) show `Q_k(-2, b)` is a constant in b (no b-dependence).

**Special case k = 2R:** Appendix F. $Q_{2R}(-2, b, c) = c(c-2R)\prod_{k=1}^{2R-1}(c-k)^2$.

---

**(R) LEVEL-k RECURSION:** define $T_0 := Q_{2R}$ and inductively
$$T_{k+1}(a, b, c) := \frac{T_k(a, b, c) - \tilde{P}_R^{(k)}(c)}{(a + 2 - k)(b + 1 - k)}$$
where $\tilde{P}_R^{(k)}(c) := T_k(k-2, b, c) = T_k(a, k-1, c)$.

**Claims:**
1. $T_k(k-2, b, c)$ is b-independent (=$\tilde{P}_R^{(k)}(c)$).
2. $T_k(a, k-1, c)$ is a-independent (=$\tilde{P}_R^{(k)}(c)$).
3. Both slices agree.
4. Exact division by $(a+2-k)(b+1-k)$ (no remainder).
5. For $k = 0, 1, \ldots, R-1$: $(c-R)^2 \mid \tilde{P}_R^{(k)}(c)$.
6. $T_R(a, b, c)$ is constant in (a, b) (independent of both), equal to
   $\tilde{P}_R^{(R)}(c)$ as a c-polynomial of degree R.

**Verified:** R = 3 (levels 0-3), R = 4 (levels 0-4). All claims hold uniformly.

---

## Explicit polynomials

**Residual pattern (verified R=3, R=4):**
$$\tilde{P}_R^{(k)}(c) = c^{(k)}_R \cdot c \cdot (c - (2R - k)) \cdot \prod_{j=1}^{k}(c - j)^{s_j^{(k)}} \cdot \prod_{j=k+1}^{2R-k-1}(c - j)^2$$

where multiplicities transition from double (interior) to simple (near boundary)
as k grows. Explicit examples (R = 3):
- $\tilde{P}_3^{(0)} = c(c-6) \cdot \prod_{k=1}^{5}(c-k)^2$, LC = 1.
- $\tilde{P}_3^{(1)} = -30 \cdot c(c-1)(c-2)^2(c-3)^2(c-4)^2(c-5)$, LC = -30.
- $\tilde{P}_3^{(2)} = 180 \cdot c(c-1)(c-2)(c-3)^2(c-4)$, LC = 180.
- $\tilde{P}_3^{(3)} = -120 \cdot c(c-1)(c-2)$, LC = -120.

**Leading coefficient closed form (verified R=3, R=4):**
$$\text{LC}(\tilde{P}_R^{(k)}) = (-1)^k \binom{2R}{k} \binom{2R-k}{k} k! = (-1)^k \binom{2R}{k} \frac{(2R-k)!}{(2R-2k)!}. \tag{LC}$$

At k = R: $\text{LC}(\tilde{P}_R^{(R)}) = (-1)^R \binom{2R}{R} R! = (-1)^R \frac{(2R)!}{R!}$.
Combined with $\tilde{P}_R^{(R)}(c) = c(c-1)\cdots(c-R+1)$ at c = R giving R!:
$$\tilde{P}_R^{(R)}(R) = (-1)^R (2R)!. \tag{Term}$$

---

## The derivation of (★)

Given (R), iterate the recursion:
$$Q_{2R}(a, b, c) = \sum_{k=0}^{R-1} \tilde{P}_R^{(k)}(c) \prod_{i=0}^{k-1}(a + 2 - i)(b + 1 - i) \; + \; \tilde{P}_R^{(R)}(c) \prod_{i=0}^{R-1}(a + 2 - i)(b + 1 - i).$$

At c = R:
- $\tilde{P}_R^{(k)}(R) = 0$ for k = 0, 1, ..., R-1 (by Claim 5, $(c-R)^2 \mid \tilde{P}_R^{(k)}$).
- $\tilde{P}_R^{(R)}(R) = (-1)^R (2R)!$ (by (Term)).

Hence
$$Q_{2R}(a, b, R) = (-1)^R (2R)! \cdot \prod_{i=0}^{R-1}(a + 2 - i)(b + 1 - i) = (-1)^R (2R)! \cdot A_R(a) B_R(b).$$

**QED (assuming (R) and (Term)).** ∎

---

## What remains to prove uniformly

**Gap 1: Prove (M).** The master identity at level 0 for all k. This requires
analyzing Rick's h_k → Q_k pipeline at a = -2 uniformly in k. Two attack routes:
- (a) Direct k-induction using binomial inversion h_k = H_k - Σ C(k, i) h_i.
- (b) Shifted-Schur reduction: at a = -2 (x_1 = 0), the M_j Jacobi-Trudi
  determinant reduces to a 2-variable shifted Schur function in (b, c),
  whose specialization gives the closed form via known formulas
  (Okounkov-Olshanski).

**Gap 2: Prove level-k recursion (R) at Weyl-boundary slice.** For k = 0
this is (M) at k = 2R. For k ≥ 1 this is a SHIFTED version at slice
$(a, b) = (k-2, k-1)$, corresponding to $x_1 = x_2 = k$ (a Weyl wall).
The recursion pattern is uniform (all leading coefficients match closed
form (LC)), suggesting a uniform argument.

**Gap 3: Prove (LC) / (Term).** The leading coefficient formula might be
derivable directly from the (2c)! = (2R)! term in Rick's H_c template
(non-M_j part), tracked through binomial inversion and Pochhammer division.

---

## Priority ordering for next PROVE session

1. **Gap 3 first (easiest).** Directly computable from the H_c template
   arithmetic. Once (Term) is proven, the k = R terminal value is fixed.

2. **Gap 1 (M) second.** This is the "biggest" gap — a uniform-in-k proof
   would give us Appendix F (F) as k = 2R corollary. Attack via
   shifted-Schur branching.

3. **Gap 2 (R) third.** Reduces to a shifted version of Gap 1. Likely
   follows from the same shifted-Schur machinery.

Once all three gaps are closed, (★) is a THEOREM, and by Day 107's earlier
work, (★) implies H5′′ (Rick's original target) and constrains
H3 substantially.

---

## Publishable form

**Theorem (working title: The Weyl-wall factorization of the 3-variable
Jacobi–Trudi determinant).** For all integers $R \geq 2$:
$$Q_{2R}(a, b, R) = (-1)^R (2R)! \cdot (a+2)_{\downarrow R} \cdot (b+1)_{\downarrow R}$$
where $(x)_{\downarrow R} = x(x-1)\cdots(x-R+1)$ is the falling factorial and
$Q_{2R}(a, b, c)$ is the 3-variable Jacobi–Trudi determinant polynomial
derived from Rick's h-template pipeline.

Estimated length as standalone note: 4-6 pages. Would fit as a section in
a longer paper or as a standalone note in J. Combin. Theory Ser. A or
similar. **Author list:** Rick + Robin (peer-reviewer). Possibly MacBeth
too if the Lean formalisation route is pursued.

## Files

- `beta-prime/code/2026-08-15-appendixF-verify-R5R6.{py,txt}` — (F) at R=5, R=6.
- `beta-prime/code/2026-08-15-shifted-F-R3-R4.{py,txt}` — level-1 recursion, R=3, R=4.
- `beta-prime/code/2026-08-15-recursion-levels.{py,txt}` — levels 2, 3, ..., R.
- `beta-prime/code/2026-08-15-hk-factor-a-minus-2.{py,txt}` — master identity at level 0.
- `memory/connections/Q-boundary-b-independence.md` — updated with (M).
- `memory/connections/M_j-as-shifted-Schur-Okounkov-Olshanski.md` — connection.
- `memory/for-collaborator/2026-08-15-day108-recursion-validated.md` — Robin note.
