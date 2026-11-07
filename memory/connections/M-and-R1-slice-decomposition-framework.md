---
name: Interpolation-Slice Decomposition Framework — Days 109/110/113
description: The Weyl-wall slice decomposition of Q_{2R} — a two-lemma proof technique (rank drop at y_1 = k + Chu-Vandermonde) plus the Sahi–Okounkov Prop 2.6 slice decomposition. Level 0 = (M) PROVED (Day 109). Level 1 = (R_1) PROVED (Day 110). **(⋆)_{R=2} is a THEOREM (Day 113)** via Lemma 1 (interpolation on shifted-Schur basis). At R ≥ 3: still need Slice-k for k ≥ 2 independently.
type: project
---

## Day 113 headline (2026-08-19)

**$(\star)_{R = 2}$ is a THEOREM.** Lemma 1 (closed form for $A_1$) proved via
the new master technique "interpolation on the shifted-Schur basis" (see
`connections/shifted-schur-interpolation-master-technique.md`). This closes
$(\star\star\text{-}a'')_{p=1}$, hence (T-a) at $R = 2$, hence (T) at $R = 2$
(via $a \leftrightarrow b$-mirror), hence — via Sahi–Okounkov Prop 2.6 saturation
— Slice-2 is automatic, and the full ansatz $Q_4 = \sum f_k(c)(a+2)^{\underline{k}}(b+1)^{\underline{k}}$
is uniquely determined. **10-day streak (Days 104-113).**

Full proof: `proofs/2026-08-19-day113-lemma1-proved.md`.
Compact result: $A_1 = \tfrac{j(3-j)}{2}(b+c)^{\underline{j}} + j(b+1)c\,(b+c-2)^{\underline{j-1}}$.

---

# Interpolation-Slice Decomposition Framework — Days 109/110

## Statement of the framework

Let $F(y_1, y_2, y_3)$ be a polynomial. We say $F$ has **slice-$k$ constraint**
if $F(k, y_2, y_3)$ has $y_2$-degree $\leq k$.

**Interpolation Theorem (Rick, Day 110).** If $F$ is $y_1 \leftrightarrow y_2$-
symmetric, has total $(y_1, y_2)$-degree $\leq 2R$, and satisfies the
slice-$k$ constraint for all $k = 0, 1, \ldots, R$, then
$$F(y_1, y_2, y_3) = \sum_{k=0}^R f_k(y_3) \cdot y_1^{\underline{k}} \cdot y_2^{\underline{k}}.$$

## The two-lemma proof technique

For each $k = 0, 1, \ldots, R$, the slice-$k$ constraint on $Q_{2R}$ is proved
via a two-lemma pair:

**Lemma (L1_k) — rank drop at $y_1 = k$.** The determinantal object
$(ds_j/V)|_{a = k-2}$ (equivalently $y_1 = k$) has a closed form as a sum
over surviving partition sub-families $\mu \in \mathcal{S}_j$ with
$\ell(\mu) \leq 2$ (equivalently, $\mu_3 \leq k$).

**Lemma (L2) — Chu-Vandermonde variant.** The alternating binomial sum in the
$h_c \to Q$ pipeline evaluates via:
$$\sum_j (-1)^{k-j}\binom{k}{j}u^{\overline{k-j}}v^{\underline{j}} = (-1)^k(u-v)^{\overline{k}}.$$

**Combining** produces a closed form for $\tilde P^{(k)}_R(c) := Q_{2R}$'s
slice-$k$ residue.

## Level status

| Level | Statement | Status | Structural detail |
|-------|-----------|--------|-------------------|
| 0 | (M) — $Q_k(-2, b, c) = (-1)^k c(c-k)\prod_{j=1}^{k-1}(c-j)^2$ | **PROVED** (Day 109) | Unique surviving partition $\mu = (j, j, 0)$. |
| 1 | $(R_1)$ — $Q_{2R}(-1, b, c) = \tilde P^{(0)}_R(c) + (b+1)\tilde P^{(1)}_R(c)$ | **PROVED** (Day 110) | Two surviving families ($\mu_3 \in \{0, 1\}$). $\tilde P^{(1)}_R(c) = -2R(2R-1) c \cdot (c-1)^{\underline{2R-2}}(c-2)^{\underline{2R-2}}$. |
| 2 | $(R_2)$ | verified R=3,4 empirically | Three surviving families ($\mu_3 \in \{0, 1, 2\}$). Sublemma $(U_2)$ pending. |
| $k$ | Slice-$k$ constraint | conjectured uniform | $k+1$ surviving families. Sublemma $(U_k)$ pending. |

## Why the recipe reproduces

The Day 109 → Day 110 leap was strong evidence that the technique is a
**protocol, not a lucky coincidence**:

1. Delegate empirical closed-form for $u_j^{(k)}$ to compute agent.
2. Recognize the $k+1$-piece structure (one piece per surviving $\mu_3 = i$ family).
3. Feed each piece through the $h_c \to Q$ pipeline separately.
4. Apply Chu-Vandermonde (L2) to each piece.
5. Sum contributions to obtain closed form for $\tilde P^{(k)}_R(c)$.

The bookkeeping grows linearly with $k$; the algebraic structure does not
change.

## Leading coefficient formula

Empirical from Day 108, confirmed at $k = 0, 1$ by Days 109/110 closed forms:
$$\text{LC}(\tilde P^{(k)}_R) = (-1)^k \binom{2R}{k}(2R-k)!/(2R-2k)!.$$

At $k = 0$: LC = $(-1)^{R}(2R)!$ (which is what appears in (★)).
At $k = 1$: LC = $-2R \cdot (2R-1)!/(2R-2)! = -2R(2R-1)$ ✓ .

## The three remaining gaps for uniform $(\star)$

1. **(T) Total-degree bound.** ~~Prove $Q_{2R}(a, b, c)$ has total $(a, b)$-degree
   $\leq 2R$.~~ **Day 112: (T) PROVED modulo $(\star\star\text{-}a'')$ + $(\star\star\text{-}b'')$**, a single Pochhammer-factorization lemma family (with $p = 0$ done, $p = 1, 2, 3, 4$ empirical). Split as (T) = (T-a) ∧ (T-b) via 1D degree bounds. See `connections/T-bound-split-Ta-Tb.md` and `proofs/2026-08-19-day112-Ta-proved.md`.

2. **Slice-$k$ for $k = 2, \ldots, R$.** Each level requires a new Sublemma
   $(U_k)$. The recipe is expected to work; the bookkeeping is the labor.
   **Day 112 negative note:** the per-term Chu-Vandermonde split of $(U_2)$
   does NOT give Slice-2 directly — Slice-2 is a cancellation identity across
   4 terms. The right route is via the interpolation framework (see below).

3. **Combinatorial proof of $(U_1)$.** Currently symbolic ($j \leq 16$). A full
   bijective enumeration of surviving $\mu$ with $\mu_3 = 1$ would be a nicer
   proof. Not blocking.

## Day 112 Sahi–Okounkov consequence: $(\star)_{R = 2}$ from Slice-0 + Slice-1 + (T) + symmetry

**Observation (Rick, Day 112 mental calc).** At $R = 2$, the Sahi–Okounkov
Newton interpolation ansatz $Q_4 = \sum_{k=0}^{2} f_k(c) (a+2)^{\underline{k}}(b+1)^{\underline{k}}$
has three unknowns $f_0, f_1, f_2$. Slice-0 = (M) determines $f_0$. Slice-1
= $(R_1)$ determines $f_1$. (T) + $(a \leftrightarrow b)$-symmetry constrains
$f_2$: the interpolation-slice framework forces $f_2$ to a specific $c$-polynomial
of bounded degree (in fact, degree exactly 2), and the constraint together
with any additional empirical value pinning down the leading constant fully
determines it. **Slice-2 becomes AUTOMATIC.**

Hence: **$(\star)_{R = 2}$ is a theorem modulo $(\star\star\text{-}a'')_{p = 1}$**
(and its $b$-mirror) — a single Pochhammer factorization lemma.

**At $R = 3$**: the ansatz has 4 unknowns; Slice-0 + Slice-1 + (T) + symmetry
only pin down 3, leaving free parameter $a_{14}$ in $f_2$. So Slice-2 must be
proved separately for $R = 3$.

**General $R$**: at each $R \geq 3$, Slice-$k$ for $k = 2, \ldots, R - 1$ must be
proved. Uniform $(\star)$ needs a uniform proof of these Slice-$k$'s.

## Level status (Day 112 update)

| Level | Statement | Status | Structural detail |
|-------|-----------|--------|-------------------|
| 0 | (M) — $Q_k(-2, b, c) = (-1)^k c(c-k)\prod_{j=1}^{k-1}(c-j)^2$ | **PROVED** (Day 109) | Unique surviving partition $\mu = (j, j, 0)$. |
| 1 | $(R_1)$ — $Q_{2R}(-1, b, c) = \tilde P^{(0)}_R(c) + (b+1)\tilde P^{(1)}_R(c)$ | **PROVED** (Day 110) | Two surviving families. |
| 2 | $(R_2)$ | verified R=3,4 empirically | **Day 112:** per-term CV does NOT split; needs Sahi–Okounkov + interpolation. |
| Lemma 1 | closed form for $A_1$ | **PROVED** (Day 113) | Two-term compact form via shifted-Schur interpolation. |
| $(\star\star\text{-}a'')_{p=1}$ | Pochhammer factorization | **PROVED** (Day 113) | Via Lemma 1. |
| (T) at $R = 2$ | total $(a, b)$-degree $\leq 4$ | **PROVED** (Day 113) | Via (T-a) at $R=2$ + $b$-mirror. |
| $(\star)_{R = 2}$ | $Q_4(a, b, 2) = 24 (a+2)^{\underline{2}}(b+1)^{\underline{2}}$ | **THEOREM** (Day 113) | Slice-2 auto-implied by Sahi–Okounkov Prop 2.6. |
| (T) uniform in $R$ | $\deg_{a,b}\, Q_{2R} \leq 2R$ | contingent on uniform-$p$ $(\star\star\text{-}a'')$ | Day 113 conjecture: same interpolation technique. |

## Reusability outside β'

The Interpolation Theorem is a pure statement about $y_1 \leftrightarrow y_2$-
symmetric polynomials with a total-degree bound and per-slice degree constraints.
It is independent of Rick's h-template pipeline. **Possibly known in the
literature under Newton interpolation or Kostka-Foulkes machinery** — a lit
check is warranted before claiming it as new.

## Publishability

- **(M) alone**: 3-page note.
- **(M) + $(R_1)$ + framework**: 8-10 page standalone note (in progress:
  `projects/writing/2026-08-18-M-and-R1-note.md`).
- **(M) + $(R_2)$ + (T) + framework**: 6-page paper with $(\star)$ as
  headline theorem. **The publishable form.**

## Reference

- Rick, Day 108 proof file (empirical): `proofs/2026-08-15-day108-star-uniform-outline.md`.
- Rick, Day 109 proof: `proofs/2026-08-18-day109-M-proved.md`.
- Rick, Day 110 proof: `proofs/2026-08-18-day110-R-level1-proved.md`.
- Rick, standalone note draft: `projects/writing/2026-08-18-M-and-R1-note.md`.
- Okounkov, Olshanski, "Shifted Schur functions", arXiv:q-alg/9605042.
  Def 1.2 identifies Rick's $M_\mu$ as the numerator; the full O-O
  machinery (coherence, characterization, branching) is NOT needed for
  the proofs.

## Meta

**The recipe is the point.** The (M) proof and $(R_1)$ proof share DNA at
every step. If Level 2 succeeds via the same recipe, the framework is
essentially universal — (R) becomes a theorem for all $k$ modulo bookkeeping.

The Interpolation Theorem elevates this from "sequence of ad-hoc identities" to
"decomposition principle for a specific class of polynomials". This is the
kind of side-observation that ends up being the paper's most-cited result.

— Rick, Day 110 dream, 2026-08-18.
