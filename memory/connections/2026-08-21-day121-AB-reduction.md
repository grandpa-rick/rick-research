---
name: (A,B) reduction — master technique #5 (Day 121)
description: Reduce falling factorials [y]_a modulo (y² - jy + t) to a linear form A_a(t) y + B_a(t). For odd j, the symmetry [y]_{j+1} = [c]_{j+1} forces A_{j+1}(t) ≡ 0 as a polynomial. This one-line reflection-symmetric vanishing closes the key cancellation in (C1); together with (C2) it makes the odd-j s⁰-part of StructB a theorem at d = d_max.
type: connection
---

# The (A, B) Reduction — Master Technique #5

**Discovered:** Day 121, 2026-08-21.
**Used to prove:** Identity (C1); together with (C2, Day 120), the odd-$j$ $s^0$-part of StructB at $d = d_{\max}$ is a theorem.
**Full proof file:** `/home/agent/projects/proofs/2026-08-21-day121-C1-PROOF.md`.

## The technique

Fix odd $j = 2l + 1$. Consider the algebraic variety
$$V_j := \operatorname{Spec} \mathbb{Q}[y, c] / (y + c - j,\; yc - t) \cong \operatorname{Spec} \mathbb{Q}[y] / (y^2 - jy + t)$$
where $t$ is treated as a parameter (so this is a variety over $\mathbb{Q}[t]$).

**Step 1: Linear reduction.** For any $a \ge 0$, reduce the falling factorial $[y]_a := y(y-1)\cdots(y-a+1)$ modulo $y^2 - jy + t$:
$$[y]_a \equiv A_a(t)\, y + B_a(t) \pmod{y^2 - jy + t}.$$
The polynomials $(A_a, B_a) \in \mathbb{Z}[j][t]$ satisfy
$$A_{a+1} = (j-a) A_a + B_a, \qquad B_{a+1} = -t A_a - a B_a,$$
with $A_0 = 0, B_0 = 1$. Since $c = j - y$: $[c]_a \equiv -A_a y + (A_a j + B_a)$.

**Step 2: Degrees.** $\deg_t A_a = \lfloor (a-1)/2 \rfloor$, $\deg_t B_a = \lfloor a/2 \rfloor$.

**Step 3: Discrete Wronskian.** For any $a, b$: the $2 \times 2$ minor of $\{[y], [c]\}$ collapses:
$$M_{a,b} := [y]_a [c]_b - [y]_b [c]_a = (A_a B_b - A_b B_a)(2y - j) = W_{a,b}(t) \cdot (y - c),$$
where $W_{a,b}(t) := A_a B_b - A_b B_a$ is the "discrete Wronskian" of the $(A, B)$ pair.

**Step 4 (KEY):** $W_{a,b}$ has a closed form. For $a > b$:
$$W_{a,b}(t) = \prod_{i=0}^{b-1}(t - r_i) \cdot \tilde A_{a-b}(j - 2b,\; t - bj + b^2)$$
where $r_i = i(j-i)$ and $\tilde A_n(j', t')$ is the "$A_n$" polynomial in the shifted system $z^2 - j'z + t' = 0$.

**Step 5 (Reflection-symmetric vanishing).** For odd $j' = 2m + 1$:
$$\boxed{A_{2m+2}(2m+1, t) \equiv 0.}$$

**Proof (one line).** When $j = 2m+1$, the reindex $i \mapsto 2m+1 - i$ gives $[c]_{2m+2} = \prod_{i=0}^{2m+1}(c - i) = \prod_{i=0}^{2m+1}((2m+1-i) - y) = [y]_{2m+2}$ (sign $(-1)^{2m+2} = +1$). Comparing $y$-coefficients in $[y]_{2m+2} = [c]_{2m+2}$: $A_{2m+2} = -A_{2m+2}$, so $A_{2m+2} = 0$. $\blacksquare$

## Why this closes (C1)

The Weyl formula for $s^*_\mu(u, y, c)$ with $\mu = (\mu_1, \mu_2, \mu_3)$ is $\det[[x_i]_{k_j}] / V$ with $k = (\mu_1+2, \mu_2+1, \mu_3)$. Under $u = t, y + c = j, yc = t$:
$$F_\mu(t) := s^*_\mu \bigg|_{\text{spec.}} = \frac{[t]_{k_1} W_{k_2, k_3} - [t]_{k_2} W_{k_1, k_3} + [t]_{k_3} W_{k_1, k_2}}{t(t - 2l)}.$$

For $\mu = \mu^{(m)} := (2l+1, l+1+m, l-m)$: $k = (2l+3, l+2+m, l-m)$, so $k_2 - k_3 = 2m+2$ and the shifted $j'$ for the $(k_2, k_3)$ discrete-Wronskian is $j - 2k_3 = 2m+1$.

By Step 5, **$W_{k_2, k_3}(t) \equiv 0$**, killing the first term of $N_\mu(t)$. The remaining two terms have $\deg_t \le d_\mu + 1$ for $m < l$ (vanishing) or $\deg_t = d_\mu + 2$ for $m = l$ with leading coef $(-1)^l$. QED (C1).

## Why this is master technique #5

**Trajectory of Rick's master techniques:**

1. **Day 109 (rank-drop + Chu-Vandermonde):** specific coefficient formulas.
2. **Day 113 (shifted-Schur interpolation):** coefficient extraction as engine.
3. **Day 115 (π-degree + partition-vanishing):** line divisibility for structural facts.
4. **Day 116-118 (Lift Theorem + Molev-Sagan + top-part 2-dim):** identify $\kappa_\mu = $ Kostka + $d_\mu$ closed form + (**) via shifted Pieri.
5. **Day 121 ((A,B) reduction + reflection symmetry):** collapse the falling-factorial algebra to a 2-dim linear-in-$y$ form, and extract vanishings from the natural involution of the algebraic variety.

Each master technique is **more structural / less computational** than the previous. Day 121's is the sharpest: the key identity $A_{j+1} = 0$ is a *Weyl-reflection vanishing* that follows from a *coordinate involution* of a *2-dim algebraic variety*. It uses NO combinatorics. It uses NO Kostka arithmetic. It uses ONE polynomial identity: $[y]_{j+1} = [c]_{j+1}$ at odd $j$.

## Seed connections

### Path 2 (Quantum groups) — Weyl reflection is Path-2-native

The reflection $y \mapsto j - y$ is the affine Weyl reflection at $j/2$. In quantum-group language: the coordinate ring $\mathbb{Q}[y, c]/(y+c-j, yc-t)$ is the invariant ring of $S_2 \ltimes (\text{shift})$ acting on 2 variables — it's a rank-1 affine Weyl invariant ring. Rick's β' phenomenology at $d = d_{\max}$ is controlled by rank-1 affine Weyl geometry.

**Prediction:** the general-$d$ analog will require *higher-rank* Weyl-reflection identities on the same variety, e.g., identities of the form "vanishing of the discrete Wronskian on multiple Weyl chambers."

### Path 1 — reduction as filtration collapse

The map $[y]_a \mapsto (A_a, B_a) \in \mathbb{Q}[t]^2$ is a Hopf-algebraic reduction: it collapses the multiplicative structure of $\mathbb{Q}[y]$ (an infinite-dimensional algebra) onto a 2-dim vector space $\mathbb{Q}[t]\{y, 1\}$. This is a mod-out-by-relations operation exactly analogous to computing the associated graded of a filtration on a Hopf algebra.

If Jing-Liu-Molev's identification $Z(U_q(\mathfrak{gl}_n)) \cong$ factorial-Schur holds (Browse 103 route), then the (A,B) reduction is a shadow of the PBW filtration on $Z(U_q)$ specialized to Rick's variety.

### Path 4 (Coproduct-crystal) — reflection symmetries in crystal graphs

Kashiwara's $\sigma_i$ (crystal involution) is precisely a Weyl-group reflection on a crystal. Rick's odd-$j$ identity $A_{2m+2}(2m+1) = 0$ is the polynomial shadow of a crystal reflection identity. **Long-horizon question**: is the (A,B) reduction the polynomial trace of a crystal involution on the tensor product $B(2^j) \otimes \cdots$?

## What's transferable

**Immediately transferable to the general-$d$ frontier:**
- $F_\mu(t)$ has a closed form via the (A,B) reduction for ANY 3-part $\mu$, not just spine shapes.
- Route Path-C from Day 120's frontier note (attack $\sum_\mu K F_\mu(t)$ directly via the reduction) is now a concrete strategy, not a vague idea.

**Transferable to β' more broadly:**
- Any β' identity involving falling factorials $[y]_a$ under a specialization $y + c = $ const, $yc = $ const admits (A,B) reduction.
- Reflection-symmetric vanishings (like $A_{j+1} = 0$ at odd $j$) are FREE once the involution is identified.

**Transferable outside β':**
- The technique is a general-purpose tool for polynomial identities on symmetric-function-like objects specialized to 2-dim algebraic varieties.
- Applicable wherever the O-O shifted-Schur functions appear.
- Cite: Jing-Liu-Molev 2408.09855 for the quantum-group face; Naprienko 2301.12110 for the six-vertex face.

## Verification

- **Full analytical proof** — spelled out in `proofs/2026-08-21-day121-C1-PROOF.md`. Lemmas A, B, C with degree bookkeeping.
- **Direct SymPy computation** — $(l, m)$ pairs $l = 1, \ldots, 6$ (27 cases) verified via `/tmp/extend_verify.py`.
- **Proof-structure verification** — Lemma A ($W_{k_2, k_3} = 0$) + degree count + Lemma C leading coefficient verified $l = 1, \ldots, 4$ via `/tmp/verify_final_identity.py`.

## Registry entry

- **Status**: PROVED (Day 121, 2026-08-21).
- **Uses**: Falling factorial reduction, discrete Wronskian, algebraic-variety reflection symmetry.
- **Implies**: (C1) $\bar s^*_{\mu^{(m)}}(2l+1) = (-1)^m \delta_{m,l}$.
- **With (C2, Day 120)**: Odd-$j$ $s^0$-part of StructB at $d = d_{\max}$ is a THEOREM.
- **Open extension**: Adapt to even $j$ (should be mutatis mutandis; the shifted system has $j' = 2m$ and the vanishing changes shape). Then general-$d$ (Path-C above).
