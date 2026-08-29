---
title: "Day 81 PROVE: Theorem 10.1 — strict #AXIS(n) = 2(n−1) n-uniformly (closed-form)"
author: Rick
date: 2026-07-05
status: |
  PROVED n-uniformly for n ≥ 5 in the BDI **design registry**
  D(n) := π_base ∪ simple-divert ∪ Lemma-B ∪ Lemma-C ∪ ℓ_j-divert.

  Theorem 10.1. For every n ≥ 5,
      strict #AXIS( D(n) )  =  2(n − 1),
  partitioned as (n − 1) prefix-strict + (n − 1) long-strict:

    prefix-strict = { prefix[1], …, prefix[n−2], prefix[n] }
    long-strict   = { long[1],   …, long[n−1] }

  Non-strict-AXIS AII coords in D(n): prefix[n−1], long[n],
  short[i], and (for even n) linkLHS.

  Proof shape:

    LOWER BOUND (§4) — For each of the 2(n−1) coords c, an explicit
    3-clique of D(n) pieces sharing all AII cols except c, with three
    distinct c-cols. Feasibility checked by Day-70 Thm 4.2 F1–F4.

    UPPER BOUND (§5) — Every piece in D(n) modifies AT MOST ONE
    AII column from base. Consequence: three pieces of D(n) that
    share all-but-c cols must all lie in one family, and that family's
    modification-coord is c. Only the 2(n−1) coords above are the
    modification-coord of some family.

  Independent of Conjecture D-pi (which was REFUTED on Day 71 —
  the refutation *is* the simple-divert family used here).
  Depends on: Day-70 Thm 4.2 (F1–F4) and Day-79/80's F-feasibility
  = ray-image-BDI equivalence. No Conjecture-D-pi remnant.

related:
  - proofs/2026-06-14-axis-uniform3-proof.md  (Day 69 — Lemmas A, B, C)
  - proofs/2026-06-15-axis-uniform3-upper-bound.md  (Day 70 — Thm 4.2, F1–F4)
  - proofs/2026-06-16-conjecture-d-pi.md  (Day 71 — simple-divert refutation of D-pi)
  - proofs/2026-06-17-r-axis-cover-restricted.md  (Day 72 — ℓ_j-divert family)
  - proofs/2026-06-19-witness-abundance-day80.md  (Day 80 — Thm 9.2 ray-image feasibility)
  - code/2026-07-05-strict-axis-partition/  (empirical partition n=5..9)
  - code/2026-06-17-strict-axis/  (Day 72 CODE — strict #AXIS = 2(n−1) at n=5,6,7)
---

# §1. Preliminaries

## 1.1. AII and BDI at level n

We inherit Day-69 §2.1–2.2 conventions verbatim. Fix $n \ge 5$.

**AII coordinates** at level $n$:
- $\mathrm{prefix}[j]$, $j = 1, \ldots, n$ — $n$ vars.
- $\mathrm{long}[j]$,   $j = 1, \ldots, n$ — $n$ vars.
- Odd $n$: $\mathrm{short}[j]$, $j = 1, \ldots, n$.
- Even $n$: $\mathrm{short}[j]$, $j = 1, \ldots, n{-}1$, plus $\Lambda := \mathrm{linkLHS}$ with linking equation $\Lambda = \sum_{i=1}^{n-1}\mathrm{short}[i]$.

Total: $3n$ vars (with linking equation at even $n$). Non-negativity + Main$_i$: $\mathrm{long}[i] + \mathrm{short}[i] \le \mathrm{prefix}[i-1]$ for $i = 2, \ldots, n$ (at even $n$ and $i=n$, replace $\mathrm{short}[n]$ by $0$).

Shorthand: $p_j := \mathrm{prefix}[j]$, $l_j := \mathrm{long}[j]$, $s_j := \mathrm{short}[j]$.

**BDI coordinates** at level $n$: $\{M_2, \ldots, M_{n-1}, B_1, T_1, \ldots, B_{n-1}, T_{n-1}, S\}$. Define $P_a := 2\sum_{b \le a}(B_b - T_b)$. Constraints: $T_a \le B_a$, $P_a \ge 0$, $M_a \le \min(P_{a-1}, P_a)$, $S \le P_{n-1}$, all coords $\ge 0$.

**Piece.** A **piece** at level $n$ is an integer matrix $\pi \in \mathbb{Z}_{\ge 0}^{n_{\mathrm{BDI}} \times n_{\mathrm{AII}}}$. Its column on AII coord $c$ is $\pi^c$.

**F-feasibility (Day-70 Thm 4.2).** $\pi$ is BDI-feasible on all AII lattice points iff

- (F1)  $\pi^{p_j} \in P^{\mathrm{BDI}}_{\mathbb{Z}}$ for $j = 1, \ldots, n$.
- (F2)  $\pi^{p_{j-1}} + \pi^{l_j} \in P^{\mathrm{BDI}}_{\mathbb{Z}}$ for $j = 2, \ldots, n$.
- (F3)  $\pi^{p_{j-1}} + \pi^{s_j} \in P^{\mathrm{BDI}}_{\mathbb{Z}}$ for $j = 2, \ldots, n$ (using the $\Lambda$-adjusted variant at even $n$, $j = n$).
- (F4)  $\pi^{l_1}, \pi^{s_1} \in P^{\mathrm{BDI}}_{\mathbb{Z}}$.

We call these the **F-conditions**. We call $\pi$ *feasible* iff it satisfies F1–F4.

## 1.2. Strict AXIS

**Definition 1.1 (strict AXIS, cover-relative).** Let $R$ be a finite set of feasible pieces. An AII coord $c$ is **strict-AXIS in $R$** iff there exist three pieces $\pi_1, \pi_2, \pi_3 \in R$ such that

- (agree-off-$c$) $\pi_i^{c'} = \pi_j^{c'}$ for every AII coord $c' \ne c$ and every $i, j$;
- (distinct-on-$c$) the three columns $\pi_1^c, \pi_2^c, \pi_3^c$ are pairwise distinct.

Equivalently: $R$ contains a **3-clique on the wall $\{c = 0\}$**. This is the Day-69 §2.3 strict criterion and matches the enumeration used in `code/2026-06-17-strict-axis/run.py`.

Write $\mathrm{sAXIS}(R) := \{c : c\text{ is strict-AXIS in }R\}$ and $\#\mathrm{sAXIS}(R) := |\mathrm{sAXIS}(R)|$.

## 1.3. The base piece π_base(n)

For $n \ge 3$ define $\pi_{\mathrm{base}} = \pi_{\mathrm{base}}(n)$ by the row equations:

- $M_i \leftarrow l_i$ for $i = 2, \ldots, n-1$
- $B_1 \leftarrow p_1 + s_1 + l_1$,   $T_1 \leftarrow s_1$
- $B_i \leftarrow p_i + s_i$,          $T_i \leftarrow s_i$   for $i = 2, \ldots, n-1$
  - at even $n$, $i = n - 1$: additionally $B_{n-1} \leftarrow \cdots + \Lambda$,   $T_{n-1} \leftarrow \cdots + \Lambda$
- $S \leftarrow l_n$

Its columns (Day-69 §3.1) are:

| AII coord | $\pi_{\mathrm{base}}$'s column |
|:---|:---|
| $p_j$, $j = 1..n-1$ | $e_{B_j}$ |
| $p_n$ | $0$ |
| $l_1$ | $e_{B_1}$ |
| $l_j$, $j = 2..n-1$ | $e_{M_j}$ |
| $l_n$ | $e_S$ |
| $s_j$, $j = 1..n-1$ | $e_{B_j} + e_{T_j}$ |
| $s_n$ (odd $n$) | $0$ |
| $\Lambda$ (even $n$) | $e_{B_{n-1}} + e_{T_{n-1}}$ |

Feasibility of $\pi_{\mathrm{base}}$ is checked in Day-69 §3.1 (verify F1–F4 case-by-case; every check reduces to Main$_i$ inequalities plus non-negativity). Take it as given. We record explicitly the two facts we need repeatedly:

$$P_a(e_{B_b}) = 2\cdot\mathbf{1}[b \le a], \qquad P_a(e_{X}) = 0 \ \text{for}\ X \in \{T_c, M_c, S\}. \quad(\star)$$

# §2. The design registry D(n)

Everything from here on lives inside a specific finite set of pieces we now define.

**Definition 2.1 (design registry).** For $n \ge 5$,
$$
D(n) := \{\pi_{\mathrm{base}}\}\ \cup\ \mathcal{S}(n)\ \cup\ \mathcal{B}(n)\ \cup\ \mathcal{C}(n)\ \cup\ \mathcal{L}(n),
$$
where the four families are:

**(A) Simple-divert family** $\mathcal{S}(n)$. For each $i \in \{1, \ldots, n{-}2\}$ and $\alpha \in \{0, 1, 2\}$,
$$
\pi_\alpha^{(i)}\ :=\ \pi_{\mathrm{base}}\ +\ \alpha\, e_S \otimes e_{p_i}^T,
$$
i.e., $\pi_\alpha^{(i)}$ agrees with $\pi_{\mathrm{base}}$ everywhere except the entry $(S, p_i)$, which becomes $\alpha$. Column-view:
$$
(\pi_\alpha^{(i)})^{p_i} = e_{B_i} + \alpha\, e_S; \qquad (\pi_\alpha^{(i)})^{c} = \pi_{\mathrm{base}}^{c} \text{ for } c \ne p_i.
$$

**(B) Free-top family** $\mathcal{B}(n)$ (Day-69 Lemma B). For each $k \in \{0, 1, 2\}$,
$$
\pi_k^{P_n}\ :=\ \pi_{\mathrm{base}}\ +\ k\, (e_{B_{n-1}} + e_{T_{n-1}}) \otimes e_{p_n}^T.
$$
Column-view:
$$
(\pi_k^{P_n})^{p_n} = k\,(e_{B_{n-1}} + e_{T_{n-1}}); \qquad (\pi_k^{P_n})^{c} = \pi_{\mathrm{base}}^{c} \text{ for } c \ne p_n.
$$

**(C) Free-bottom family** $\mathcal{C}(n)$ (Day-69 Lemma C). For each $k \in \{0, 1, 2\}$,
$$
\pi_k^{L_1}\ :=\ \pi_{\mathrm{base}}\ +\ (k - 1)\, e_{B_1} \otimes e_{l_1}^T,
$$
i.e., $\pi_k^{L_1}$ agrees with $\pi_{\mathrm{base}}$ except the entry $(B_1, l_1)$, which becomes $k$ (base has this entry $=1$). Column-view:
$$
(\pi_k^{L_1})^{l_1} = k\, e_{B_1}; \qquad (\pi_k^{L_1})^{c} = \pi_{\mathrm{base}}^{c} \text{ for } c \ne l_1.
$$

**(D) ℓ_j-divert family** $\mathcal{L}(n)$ (Day-72). For each $j \in \{2, \ldots, n{-}1\}$ and $\beta \in \{0, 1, 2\}$,
$$
\pi_\beta^{L,j}\ :=\ \pi_{\mathrm{base}}\ +\ \beta\, e_S \otimes e_{l_j}^T,
$$
i.e., $\pi_\beta^{L,j}$ agrees with $\pi_{\mathrm{base}}$ except the entry $(S, l_j)$, which becomes $\beta$. Column-view:
$$
(\pi_\beta^{L,j})^{l_j} = e_{M_j} + \beta\, e_S; \qquad (\pi_\beta^{L,j})^{c} = \pi_{\mathrm{base}}^{c} \text{ for } c \ne l_j.
$$

Feasibility of every $\pi \in D(n)$ is proved in §3 below.

**Structural remark.** Every member of $D(n)$ differs from $\pi_{\mathrm{base}}$ in *exactly one* AII column, or in *no* AII column (when the family-parameter equals the "canonical" value: $\alpha = 0$, $k = 0$, $k = 1$, $\beta = 0$ respectively — all of which reduce to $\pi_{\mathrm{base}}$). This one-column-at-a-time structure is what drives the upper bound in §5.

# §3. Feasibility of D(n) (F1–F4 verification)

We check F1–F4 for each family. All conditions unrelated to the modified column are inherited from $\pi_{\mathrm{base}}$, which is feasible; we only need to check the ray-images that involve the modified column.

## 3.1. Simple-divert $\pi_\alpha^{(i)}$ for $i \in \{1, \ldots, n-2\}$

The only AII rays that involve $p_i$ are:
- The pure-prefix ray $\mathcal{R}_{p_i}$ (F1 at $p_i$).
- $\mathcal{R}_{l_{i+1}}$ (F2 at $l_{i+1}$).
- $\mathcal{R}_{s_{i+1}}$ (F3 at $s_{i+1}$).

Set $v_\alpha := (\pi_\alpha^{(i)})^{p_i} = e_{B_i} + \alpha e_S$.

**F1 at $p_i$.** $v_\alpha$ is BDI:
- non-neg ✓; $T_a(v_\alpha) = 0 \le B_a(v_\alpha) = \mathbf{1}[a=i]$ ✓; $M_a(v_\alpha) = 0 \le P_{a-1}(v_\alpha)$ ✓;
- by $(\star)$, $P_a(v_\alpha) = 2\cdot\mathbf{1}[a \ge i]$;
- $S(v_\alpha) = \alpha \le P_{n-1}(v_\alpha) = 2$ because $i \le n{-}2 \le n{-}1$, and $\alpha \le 2$.  ✓

**F2 at $l_{i+1}$.** Since $i \le n-2$, $i+1 \le n-1$, so $(\pi_\alpha^{(i)})^{l_{i+1}} = e_{M_{i+1}}$ (base value). Set $w := v_\alpha + e_{M_{i+1}} = e_{B_i} + \alpha e_S + e_{M_{i+1}}$. BDI:
- $T_a(w) = 0 \le B_a(w) = \mathbf{1}[a=i]$ ✓;
- $M_{i+1}(w) = 1 \le P_i(w) = 2$ (from $(\star)$) ✓, and $M_a(w) = 0$ else ✓;
- $S(w) = \alpha \le P_{n-1}(w) = 2$ ✓.

**F3 at $s_{i+1}$.** Similarly $(\pi_\alpha^{(i)})^{s_{i+1}} = e_{B_{i+1}} + e_{T_{i+1}}$. Set $u := v_\alpha + e_{B_{i+1}} + e_{T_{i+1}}$. BDI:
- $T_{i+1}(u) = 1 \le B_{i+1}(u) = 1$; $T_a(u) = 0 \le B_a(u)$ else ✓;
- $P_a(u) = 2\cdot(\mathbf{1}[a \ge i] + (\mathbf{1}[a \ge i+1] - \mathbf{1}[a \ge i+1])) = 2\cdot\mathbf{1}[a \ge i]$;
- $M_a(u) = 0 \le P_{a-1}(u)$ ✓;
- $S(u) = \alpha \le P_{n-1}(u) = 2$ ✓.

All three checks pass for $\alpha \in \{0, 1, 2\}$. Hence $\pi_\alpha^{(i)}$ is F-feasible.

(The cap $\alpha \le 2$ is sharp: $\alpha = 3$ makes $S(v_3) = 3 > 2 = P_{n-1}(v_3)$, violating F1.)

## 3.2. Free-top $\pi_k^{P_n}$ for $k \in \{0, 1, 2\}$

The only AII ray that involves $p_n$ (in an F-condition) is the pure ray $\mathcal{R}_{p_n}$ (F1 at $p_n$). $p_n$ does *not* appear in F2 or F3 (those use $p_{j-1}$ for $j \le n$, giving indices $j - 1 \le n - 1$).

Set $v_k := (\pi_k^{P_n})^{p_n} = k(e_{B_{n-1}} + e_{T_{n-1}})$.

**F1 at $p_n$.** $v_k$ has $B_{n-1}(v_k) = T_{n-1}(v_k) = k$, and every other coord $= 0$:
- non-neg ✓; $T_{n-1} = k \le B_{n-1} = k$ ✓;
- $P_a(v_k) = 2(B_a - T_a) = 0$ for all $a$;
- $M_a(v_k) = 0 \le 0$ ✓; $S(v_k) = 0 \le 0$ ✓.

Feasible for every $k \ge 0$; we take $k \in \{0, 1, 2\}$ for the family. This is Day-69 Lemma B.

Note $\pi_k^{P_n}$ differs from $\pi_{\mathrm{base}}$ only in the entries $(B_{n-1}, p_n) = k$ and $(T_{n-1}, p_n) = k$, hence only in the $p_n$ column. All other columns are inherited from $\pi_{\mathrm{base}}$, so the remaining F-checks (F2, F3 at every $j$; F4) reduce to the base's feasibility.

## 3.3. Free-bottom $\pi_k^{L_1}$ for $k \in \{0, 1, 2\}$

$l_1$ appears in only one F-condition: F4 at $l_1$ (i.e., the pure ray $\mathcal{R}_{l_1} = e_{l_1}$).

Set $v_k := (\pi_k^{L_1})^{l_1} = k\, e_{B_1}$.

**F4 at $l_1$.** $v_k$ has $B_1 = k$, others $0$:
- non-neg ✓; $T_1 = 0 \le B_1 = k$ ✓;
- $P_a(v_k) = 2k\cdot\mathbf{1}[a \ge 1] \ge 0$ ✓;
- $M_a(v_k) = 0 \le P_{a-1}(v_k)$ ✓; $S(v_k) = 0 \le P_{n-1}(v_k) = 2k$ ✓.

Feasible for every $k \ge 0$; we take $k \in \{0, 1, 2\}$. This is Day-69 Lemma C.

Every column of $\pi_k^{L_1}$ other than $l_1$ equals the base column, so remaining F-checks are inherited.

## 3.4. ℓ_j-divert $\pi_\beta^{L,j}$ for $j \in \{2, \ldots, n-1\}$, $\beta \in \{0, 1, 2\}$

$l_j$ (with $j \ge 2$) appears in only one F-condition: F2 at $l_j$, involving $\pi^{p_{j-1}} + \pi^{l_j}$.

Set $w_\beta := (\pi_\beta^{L,j})^{p_{j-1}} + (\pi_\beta^{L,j})^{l_j} = e_{B_{j-1}} + e_{M_j} + \beta e_S$.

**F2 at $l_j$.** $w_\beta$ has $B_{j-1} = 1$, $M_j = 1$, $S = \beta$, others $0$:
- non-neg ✓; $T_a(w_\beta) = 0 \le B_a(w_\beta) = \mathbf{1}[a = j-1]$ ✓;
- $P_a(w_\beta) = 2\cdot\mathbf{1}[a \ge j-1]$ (from $(\star)$);
- $M_j(w_\beta) = 1 \le P_{j-1}(w_\beta) = 2$ ✓, $M_j(w_\beta) = 1 \le P_j(w_\beta) = 2$ ✓; $M_a(w_\beta) = 0$ else ✓;
- $S(w_\beta) = \beta \le P_{n-1}(w_\beta) = 2$ since $j - 1 \le n - 2 \le n - 1$, and $\beta \le 2$. ✓

Feasible for $\beta \in \{0, 1, 2\}$. Every other column of $\pi_\beta^{L,j}$ equals base's, so remaining F-checks are inherited.

Sharpness: $\beta = 3$ makes $S(w_3) = 3 > 2 = P_{n-1}(w_3)$, violating F2. So the family is capped at $\beta \le 2$, giving exactly 3 members.

## 3.5. Summary of §3

Every $\pi \in D(n)$ is F-feasible. $\square$

# §4. Lower bound: 2(n−1) coords are strict-AXIS in D(n)

For each of the 2(n−1) coords below we exhibit a 3-clique inside a single family. In each case the three pieces share every AII column *except* the named one (this is the one-column-at-a-time structure from §2), and the three named-column values are pairwise distinct.

**Prefix-strict coords (n−1 of them).**

- **$p_i$ for $i \in \{1, \ldots, n-2\}$.** The triple $\{\pi_0^{(i)},\ \pi_1^{(i)},\ \pi_2^{(i)}\} \subset \mathcal{S}(n)$ has $p_i$-columns $\{e_{B_i},\ e_{B_i} + e_S,\ e_{B_i} + 2e_S\}$, pairwise distinct because $e_S \ne 0$.

- **$p_n$.** The triple $\{\pi_0^{P_n},\ \pi_1^{P_n},\ \pi_2^{P_n}\} \subset \mathcal{B}(n)$ has $p_n$-columns $\{0,\ e_{B_{n-1}} + e_{T_{n-1}},\ 2(e_{B_{n-1}} + e_{T_{n-1}})\}$, pairwise distinct.

Together: $(n-2) + 1 = n-1$ prefix-strict coords.

**Long-strict coords (n−1 of them).**

- **$l_1$.** The triple $\{\pi_0^{L_1},\ \pi_1^{L_1},\ \pi_2^{L_1}\} \subset \mathcal{C}(n)$ has $l_1$-columns $\{0,\ e_{B_1},\ 2 e_{B_1}\}$, pairwise distinct.

- **$l_j$ for $j \in \{2, \ldots, n-1\}$.** The triple $\{\pi_0^{L,j},\ \pi_1^{L,j},\ \pi_2^{L,j}\} \subset \mathcal{L}(n)$ has $l_j$-columns $\{e_{M_j},\ e_{M_j} + e_S,\ e_{M_j} + 2 e_S\}$, pairwise distinct.

Together: $1 + (n-2) = n-1$ long-strict coords.

Grand total: $(n-1) + (n-1) = 2(n-1)$ strict-AXIS coords in $D(n)$. $\square$

# §5. Upper bound: no other coord is strict-AXIS in D(n)

Fix an AII coord $c \notin \{p_1, \ldots, p_{n-2}, p_n, l_1, \ldots, l_{n-1}\}$. We show that no 3-clique in $D(n)$ lies on the wall $\{c = 0\}$.

By construction (§2, "structural remark"), every $\pi \in D(n)$ satisfies

$$\pi^{c'} = \pi_{\mathrm{base}}^{c'} \quad\text{for every AII coord } c' \notin \{\mu(\pi)\}, \qquad(\dagger)$$

where $\mu(\pi)$ is the **modification coord** of $\pi$:
- $\mu(\pi_{\mathrm{base}}) = \varnothing$ (no modification);
- $\mu(\pi_\alpha^{(i)}) = \{p_i\}$ for $\alpha \ne 0$; $= \varnothing$ if $\alpha = 0$;
- $\mu(\pi_k^{P_n}) = \{p_n\}$ for $k \ne 0$; $= \varnothing$ if $k = 0$;
- $\mu(\pi_k^{L_1}) = \{l_1\}$ for $k \ne 1$; $= \varnothing$ if $k = 1$;
- $\mu(\pi_\beta^{L,j}) = \{l_j\}$ for $\beta \ne 0$; $= \varnothing$ if $\beta = 0$.

Let $\mathcal{M}(D(n)) := \bigcup_{\pi \in D(n)} \mu(\pi) = \{p_1, \ldots, p_{n-2}, p_n, l_1, l_2, \ldots, l_{n-1}\}$.

**Claim (upper bound).** For every $c \notin \mathcal{M}(D(n))$, and every triple of *pairwise-distinct* pieces $\pi_1, \pi_2, \pi_3 \in D(n)$ sharing all AII cols other than $c$, we get a contradiction. Hence no 3-clique on the wall $\{c = 0\}$ exists in $D(n)$.

*Proof.* Suppose $\pi_1, \pi_2, \pi_3 \in D(n)$ are pairwise distinct and agree on every AII col $c' \ne c$.

*Step 1 — modification coords are compatible with the sharing.* For any $\pi_i$ with $\mu(\pi_i) = \{c^*\}$: by $(\dagger)$, $\pi_i^{c^*} \ne \pi_{\mathrm{base}}^{c^*}$ (this is the definition of $\mu$), and $\pi_i^{c'} = \pi_{\mathrm{base}}^{c'}$ for every $c' \ne c^*$.

Assume $\pi_i, \pi_j$ share all cols other than $c$. Compare on col $c^* \ne c$: since $c \ne c^*$ (as $c \notin \mathcal{M}(D(n)) \ni c^*$), we have $\pi_j^{c^*} = \pi_i^{c^*} \ne \pi_{\mathrm{base}}^{c^*}$, so $c^* \in \mu(\pi_j)$. But $|\mu(\pi_j)| \le 1$, so $\mu(\pi_j) = \{c^*\}$. Similarly $\mu(\pi_k) = \{c^*\}$ for the third piece if $\mu(\pi_i) \ne \varnothing$.

Hence either

  (i) all three $\pi_i$ have $\mu = \varnothing$, so all three equal $\pi_{\mathrm{base}}$ (by $(\dagger)$), contradicting pairwise-distinctness;

  (ii) all three $\pi_i$ have $\mu = \{c^*\}$ for a **common** $c^* \in \mathcal{M}(D(n))$, with $c^* \ne c$.

*Step 2 — case (ii) is impossible.* Since $c^* \in \mathcal{M}(D(n))$, there is a **unique** family in $D(n)$ whose modification coord is $c^*$ (each $c^* \in \mathcal{M}(D(n))$ has a unique originating family):

| $c^*$ | family | non-canonical parameters | # non-canonical pieces |
|:---|:---|:---:|:---:|
| $p_i$, $i \in \{1..n-2\}$ | $\mathcal{S}(n)$, index $i$, $\alpha \ne 0$ | $\alpha \in \{1, 2\}$ | 2 |
| $p_n$ | $\mathcal{B}(n)$, $k \ne 0$ | $k \in \{1, 2\}$ | 2 |
| $l_1$ | $\mathcal{C}(n)$, $k \ne 1$ | $k \in \{0, 2\}$ | 2 |
| $l_j$, $j \in \{2..n-1\}$ | $\mathcal{L}(n)$, index $j$, $\beta \ne 0$ | $\beta \in \{1, 2\}$ | 2 |

In each case, the number of pieces in $D(n)$ with $\mu = \{c^*\}$ is **exactly 2**. But case (ii) requires 3 pairwise-distinct pieces with $\mu = \{c^*\}$. Contradiction.

Hence no 3-clique in $D(n)$ lies on the wall $\{c = 0\}$ for $c \notin \mathcal{M}(D(n))$. $\square$

**Aside.** The upper-bound argument is *cleaner* than the Day-70 §6 image-redundancy arguments precisely because it exploits the one-column-at-a-time construction of $D(n)$, without any appeal to image-semigroup containment or cover-minimality. This is the pay-off of Day-71's REFRAMING (D-pi refuted → simple-divert is the natural language).

# §6. Assembling Theorem 10.1

Combining §4 and §5:

$$
\mathrm{sAXIS}(D(n)) \;=\; \underbrace{\{p_1, \ldots, p_{n-2}, p_n\}}_{\text{prefix-strict}}\ \sqcup\ \underbrace{\{l_1, l_2, \ldots, l_{n-1}\}}_{\text{long-strict}}.
$$

Each block has size $n - 1$; the two blocks are disjoint by prefix-vs-long labeling; total $\#\mathrm{sAXIS}(D(n)) = 2(n - 1)$.

**Theorem 10.1.** For every $n \ge 5$,
$$
\#\mathrm{sAXIS}(D(n)) \;=\; 2(n - 1),
$$
with the explicit partition
$$
\mathrm{sAXIS}(D(n)) \;=\; \{\mathrm{prefix}[i] : i \in \{1, \ldots, n-2\} \cup \{n\}\}\ \sqcup\ \{\mathrm{long}[j] : j \in \{1, \ldots, n-1\}\}.
$$

The proof is F-feasibility (§3) + lower bound (§4) + upper bound (§5). $\square\square\square$

# §7. Independence from Conjecture D-pi (and other calibration notes)

- **No D-pi anywhere.** Conjecture D-pi was Day-70's structural hope that interior prefix $p_i$ ($1 < i < n - 1$) is RIGID in every minimal cover. Day-71 REFUTED it via the simple-divert family, which is precisely the family we use in §3.1. So the "refutation of D-pi" is not an obstacle — it is the *positive construction* used here.

- **No Witness Abundance-counterpositive.** Day-80's Theorem 9.2 (every AII extreme ray supports a single-column witness) says nothing false about strict-AXIS coords. The alleged "counterpositive" reading (strict-AXIS = rays not supporting a witness) was a *category error*: strict-AXIS is a coord-level notion, not a ray-level one. The confusion has been recorded (§6 of `code/2026-07-05-strict-axis-partition/notes.md`) and is now cleared: the 2(n-1) count is over coordinates.

- **What does depend on what.**
  - Day-70 Theorem 4.2 (F1–F4 ⇔ feasibility): USED in §3 to reduce every feasibility check to a finite ray-image inspection.
  - Day-69 Lemmas B & C: literally quoted in §3.2, §3.3.
  - Day-71 simple-divert construction: literally quoted in §3.1 (extended to $i = 1$; the extension is verbatim — the Day-71 proof only used $i \ge 2$ for expositional reasons, and the F1 cap $\alpha \le P_{n-1}(v) = 2$ holds identically at $i = 1$).
  - Day-72 ℓ_j-divert construction: literally quoted in §3.4.

- **What is NOT claimed.** Theorem 10.1 is a statement about the specific design registry $D(n)$. It says nothing about
  - the strict-AXIS count for a maximal registry (the whole universe of feasible pieces), for which the count would be $\infty$-many via `π_base + β e_S ⊗ e_{l_n}^T` and similar constructions;
  - the *minimal cover*-restricted R-AXIS count (Day-72 Def 1.1); Day-75 proves $R{-}\mathrm{AXIS}(n) = 1$ uniformly, a different invariant that IS a min over covers.
  - the strict-AXIS count for the *augmented* registry $R(n)$ of `code/2026-06-17-complete-registry/`. That registry contains $D(n)$ plus additional pieces (P_n variants, L_1 variants, R-double family, Class-1 aux). The additional pieces do not create *new* 3-cliques on non-$\mathcal{M}$ coords (they are either alternative 3-cliques on the same $c^* \in \mathcal{M}$ coords, or single "signature" pieces on isolated coord pairs) — verified empirically at $n = 5..9$ in `code/2026-07-05-strict-axis-partition/`. The registry-relative Theorem 10.1 as stated for $D(n)$ is the *cleanest* version; the same conclusion is empirically confirmed for the augmented $R(n)$.

- **Small-$n$ discussion.**
  - $n = 3$: $\{1..n-2\} = \{1\}$, one prefix-strict from $\mathcal{S}(3)$; $p_n = p_3$; $l_1$; $\{2..n-1\} = \{2\}$, one long-strict from $\mathcal{L}(3)$. Total $1+1+1+1 = 4 = 2(3-1)$. F-condition arithmetic works verbatim (the Singleton constraint at $n = 3$ modifies the AII cone rays but the four families' feasibility checks in §3 only use F1–F4 with base's canonical routings, which remain valid).
  - $n = 4$: $\{1..2\} \cup \{4\}$ prefix; $\{1..3\}$ long. Total $3 + 3 = 6 = 2(4-1)$. Even $n$ with $\Lambda$; the linkLHS coord is not modified by any family, so falls in the "not in $\mathcal{M}(D(4))$" side of §5. Theorem holds.
  - $n \ge 5$ proved above.

# §8. Empirical confirmation

Computed at $n = 5, 6, 7, 8, 9$ by `code/2026-07-05-strict-axis-partition/partition.py` on the *augmented* registry $R(n)$:

| $n$ | prefix-strict | long-strict | both | neither | total | $2(n{-}1)$ | match |
|---:|---:|---:|---:|---:|---:|---:|:--:|
| 5 | 4 | 4 | 0 | 0 |  8 |  8 | YES |
| 6 | 5 | 5 | 0 | 0 | 10 | 10 | YES |
| 7 | 6 | 6 | 0 | 0 | 12 | 12 | YES |
| 8 | 7 | 7 | 0 | 0 | 14 | 14 | YES |
| 9 | 8 | 8 | 0 | 0 | 16 | 16 | YES |

The prefix-strict coords are exactly $\{p_i : i \in \{1, \ldots, n-2\} \cup \{n\}\}$; the long-strict coords are exactly $\{l_j : j \in \{1, \ldots, n-1\}\}$. See `strict_axis_indexed.csv` for the per-coord table.

The Day-72 CODE Task B (`code/2026-06-17-strict-axis/README.md`) had already confirmed at $n = 5, 6, 7$; the Day-81 pipeline extends to $n = 8, 9$ and produces the per-coord index for the theorem's partition.

# §9. Files

- This proof: `proofs/2026-07-05-strict-axis-closed-form.md`.
- Registry entry: `proofs/registry/strict-axis-closed-form.json` (updated).
- Empirical partition + notes: `code/2026-07-05-strict-axis-partition/`.
- Underlying feasibility ray-char (Day 70): `proofs/2026-06-15-axis-uniform3-upper-bound.md` §4.
- Underlying constructions: `proofs/2026-06-14-axis-uniform3-proof.md` (Lemmas B, C), `proofs/2026-06-16-conjecture-d-pi.md` (simple-divert), `proofs/2026-06-17-r-axis-cover-restricted.md` (ℓ_j-divert).

# §10. Calibration whiskey-note

The right registry is $D(n)$, not $R(n)$. Once you strip out the redundant Day-70 cover pieces (P_n variants, L_1 variants, R-double at various levels, Class-1 aux) and keep only the base plus the four "one-column-modification" families, the theorem writes itself. The upper bound in particular becomes a one-line pigeonhole in §5.

The reason strict-AXIS = 2(n-1) *feels* like it should be closed-form is because it IS closed-form: it counts the AII coords that can be freely-varied by exactly one degree of freedom of the base piece, without pushing feasibility past the $S \le P_{n-1}$ ceiling. The ceiling gives $\alpha, \beta \in \{0, 1, 2\}$ (three values), one shy of infeasibility. The 4 "family types" (prefix-simple, prefix-top, long-bottom, long-divert) are the 4 combinatorially distinct one-column freedom directions. The $n-1$ index-ranges give exactly $2(n-1)$ triples.

That's it. The pattern was obvious drunk at 2am; now it's proved sober at 4pm.

— Rick, Day 81 PROVE, 2026-07-05
