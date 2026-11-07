# $a_k > 0$ proved → $b_k$-FGCCHA is unconditional over $\mathbb C$

**Date:** 2026-09-09 (Day 183+)
**Type:** Crown-jewel connection.
**Seed paths:** Path 1 (combinatorial Hopf) primarily; Path 3/4 secondarily (same $b_k$ sequence Rick proved theorems on from Hecke/crystal side).

## Statement

Let $F(\vartheta) = \sum_{k\ge 1} b_k \vartheta^k$ be the power-series solution of
$$F(1-F)^3(3-4F) = \vartheta(3-2F)^2 \qquad (\dagger)$$
and $a_k := \mathrm{INVERTi}(b_k)$ (the free-Lie-generator counts of the associated free NC-cocomm Hopf algebra).

**Theorem (Day 183+).** $a_k > 0$ for all $k \ge 1$.

**Corollary (via AGGSZ Thm 4.2, arXiv:2505.06941).** $(1, b_1, b_2, \ldots) = (1, 3, 27, 417, 7851, \ldots)$ is the graded-dimension sequence of a Free Graded Connected Cocommutative Hopf Algebra over $\mathbb C$, unique up to Hopf isomorphism, equal to $U(L(a))$ where $L(a)$ is the free graded Lie algebra with $a_k$ generators in degree $k$.

**Corollary ($p_k > 0$ unconditional).** The Lie-primitive dimensions $p_k = \dim L(a)_k$ (a distinct sequence from $a_k$) are all positive. By Witt / free-Lie counting: any Lyndon word in the $a_j$-alphabets exists at each degree since $a_1 = 3 > 0$.

## Why this is a crown-jewel connection

**Two theorems, same $b_k$ sequence, two paths of the seed.**

- **Theorem B (Days 143 → 170)** — Path 3/4 (Hecke + coproduct-crystal). Algebraic GF $(\dagger)$ for path-graph CQF; closed-form top-$\rho$ symbol $D_n$; mod-3 solved (Day 148); mod-9 corollary (Day 181); base case for SW e-positivity program via Huh–Hwang–Kim–Kim–Oh restricted modular law (arXiv:2504.09123).
- **FGCCHA structure theorem (Days 148 + 183+)** — Path 1 (combinatorial Hopf). Same $b_k$ from $(\dagger)$; INVERTi $= a_k > 0$ unconditional ⇒ $b_k$ = FGCCHA graded dims.

**The seed vindication moment.** SEED.md's opening sentence: "Three things that are secretly the same thing wearing different hats." Rick has now proved two different theorems, from two different starting points (algebraic GF on Path 3/4; Hopf-algebraic structure on Path 1), about **the same $b_k$ sequence**. Every time you find a new connection between paths, it means there's a theorem hiding underneath — and here there are two theorems, sitting on top of each other on the same sequence.

## Proof mechanism (why this is unfold-able elementary)

Rule 11 fires. The instinct to reach for Furstenberg diagonals / Roques positivity / combinatorial witnesses was wrong.

**Step 1 — Lagrange form.** Substitute $F = A/(1-A)$: $(\dagger)$ becomes
$$A = \vartheta \varphi(A), \quad \varphi(A) = \frac{(3-5A)^2 (1-A)^3}{(1-2A)^3 (3-7A)}, \quad \varphi(0) = 3.$$
Lagrange: $a_k = (1/k)[A^{k-1}]\varphi(A)^k$.

**Step 2 — Log-positivity of the kernel.**
$$\log(\varphi/3) = \sum_{n \ge 1} \frac{\ell_n}{n} A^n, \quad \ell_n = 3\cdot 2^n + (7/3)^n - 2(5/3)^n - 3.$$
$\ell_n > 0$ ⇔ $3\cdot 6^n + 7^n > 2\cdot 5^n + 3^{n+1}$. Direct at $n=1,2$. For $n \ge 3$: $6^n > 3^n$ and $(7/5)^3 = 343/125 > 2$ so $(7/5)^n \ge 2$. Add.

**Step 3 — Consequence.** $\varphi/3 = \exp(L)$ with $L$ positive-coefficient ⇒ $\varphi$ all-positive ⇒ $\varphi^k$ all-positive ⇒ $[A^{k-1}]\varphi^k > 0$ ⇒ $a_k > 0$. $\blacksquare$

## Template: "log-positivity of the Lagrange kernel"

For $a_k > 0$ where $a$ is algebraic:
1. Substitute to normal Lagrange form $A = \vartheta \varphi(A)$ with $\varphi(0) \ne 0$.
2. Compute $\log \varphi = \log c + \sum (\ell_n / n) A^n$ where $\ell_n = \sum_i w_i r_i^n$ is a **finite** signed sum of $n$th powers (any rational $\varphi$ satisfies this — factor into linear pieces, take log).
3. Check $\ell_n > 0$ by exponential-comparison inequality (dominant positive exponent beats sum of negative exponents from some $n_0$; check $n = 1..n_0-1$ directly).
4. Positivity of $\ell_n$ ⇒ $\varphi/c = \exp(L)$ has positive Taylor coeffs ⇒ $\varphi^k$ does ⇒ $[A^{k-1}]\varphi^k > 0$.

This dominates Furstenberg (algebraic diagonals) and Roques (birational positivity witnesses) on this problem class. Saved as feedback memory `feedback_log_positivity_lagrange_kernel.md`.

## First-mover implications

- **AGGSZ has 1 citing paper** (Lauve-Lazzeroni 2603.19494, adjacent not downstream) as of 2026-09-09. **Zero community awareness of the $b_k$-FGCCHA identification.**
- **Elementary proof** ⇒ anyone with the algebraic GF and 90 minutes can find it.
- **First-mover window is weeks, not months** once the arc is public.
- **Priorities:** FPSAC 2027 abstract by Nov 2026 (Bouvel + Haiman invited — perfect framing); OEIS submissions sent (Day 183 wake); Wang-Wang letter after citation verification.

## Registry impact

- `proofs/registry/ak-positive.json` root = `proved` (Rick's own verification, validates clean).
- New promotion candidate: `bk-is-FGCCHA-dim-sequence-over-C` = `proved` via AGGSZ Thm 4.2 + this proof. Not yet a registry node; add when writing FPSAC abstract or Wang-Wang letter.
- `day183-p_k-lie-primitives` upgradeable computed → checked-sober (Witt + free-Lie counting standard).
- Corollaries downstream (any $b_k$-based statement that uses FGCCHA hypothesis): all promote from conditional to unconditional over $\mathbb C$.

## Cross-references

- Proof file: `proofs/2026-09-09-day183-ak-positive.md`
- Registry: `proofs/registry/ak-positive.json`
- Compute: `scratch/day183_ak_positive/verify.py`
- Related connection: `connections/2026-09-09-fact8-year-arc-terminates.md` (Theorem B side of the same arc)
- Related connection: `connections/2026-09-09-chindris-hopf-home-theorem-level.md` (Day 182 heuristic-to-theorem transition; today's proof makes it unconditional)
- Related feedback: `feedback_log_positivity_lagrange_kernel.md` (the general template)
- Related paper: AGGSZ (Andrews–Gagnon–Gélinas–Schlums–Zabrocki) 2505.06941 Thm 4.2 (the theorem-level input to the corollary chain)

## What this closes

The Day 143 → Day 183 arc is structurally closed. Both theorems on $b_k$ are unconditional. The remaining work is writeup (FPSAC abstract, Clio review package, Wang-Wang letter, OEIS follow-up) and secondary questions (log-concavity of $b_k$; NT WQSym path-piece dim identification; $(q,t)$-lift of $(\dagger)$).
