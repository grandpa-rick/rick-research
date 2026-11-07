---
name: Day 119 — Kostka = ballot for spine shapes; (2B) → (2A) 1-line reduction
description: At $d = d_{\max}$, the Kostka multiplicities in Rick's StructB reduction are ballot numbers $\binom{a+b}{b} - \binom{a+b}{b-1}$ via a forced-column-1 lattice-path bijection on the "spine" shapes $(3^{l-m}, 2^{2m+\epsilon}, 1^{l-m})$. Alternating identities (2A), (2B) become elementary binomial identities; (2B) is $(2l+1)$ times (2A) via the identity $(n-2r)\binom{n}{r} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$. Self-contained mini-theorem; stands independent of StructB.
type: project
---

# Kostka = ballot for spine shapes at $d_{\max}$

## Summary

At $d = d_{\max}(j) = j + \lfloor j/2 \rfloor$, the Kostka multiplicities $K_{\mu', (2^j)}$ appearing in Rick's StructB reduction are **ballot numbers**. The alternating cancellation identities (2A), (2B) become elementary binomial identities. In particular:

- **Kostka = ballot** for shape $(3^{l-m}, 2^{2m+\epsilon}, 1^{l-m})$ with content $(2^j)$, via a forced-column-1 + lattice-path bijection.
- **Identity (2A)** (even $j$) reduces to $(1-1)^{2l} = 0$ + binomial symmetry.
- **Identity (2B)** (odd $j$) equals $(2l+1) \cdot (\text{2A at } 2l)$, via $(n-2r)\binom{n}{r} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$.

This closes the top-$t$ part of StructB at $d = d_{\max}$ modulo the two auxiliary identities (C1), (C2) for the odd-$j$ $s^0$-part.

## The setup

$\mu = (\mu_1, \mu_2, \mu_3)$ a partition of $2j$ with $\ell(\mu) \le 3$. Rick's Day 118 closed form:

$$d_\mu = j + \lfloor \mu_1 / 2 \rfloor.$$

Empirical $d_{\max}(j) = j + \lfloor j/2 \rfloor$ (verified $j \le 14$). At $d = d_{\max}$, the $\mu$'s are:

- **Odd $j = 2l+1$:** $\mu = (2l+1, l+1+m, l-m)$ for $m = 0, \ldots, l$. Odd parity ($\mu_2 - \mu_3 = 2m+1$).
- **Even $j = 2l$:** $\mu = (2l, l+m, l-m)$ for $m = 0, \ldots, l$. Even parity ($\mu_2 - \mu_3 = 2m$).

Their conjugates are **spine shapes**:

$$\mu' = (3^{l-m}, 2^{2m+\epsilon}, 1^{l-m}), \qquad \epsilon = 1 \text{ (odd } j\text{)},\ 0 \text{ (even } j\text{)}.$$

## The Kostka = ballot lemma

**Lemma.** For $\lambda = (3^{l-m}, 2^{2m+1}, 1^{l-m})$:

$$K_{\lambda, (2^{2l+1})} = \binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}.$$

Similarly for even $j = 2l$: $K_{(3^{l-m}, 2^{2m}, 1^{l-m}), (2^{2l})} = \binom{2l}{l-m} - \binom{2l}{l-m-1}$.

**Proof (odd $j$).** Column lengths: $2l+1$, $l+m+1$, $l-m$.

**Step 1: Column 1 is forced.** Column 1 has $2l+1$ strictly increasing entries drawn from labels $\{1, \ldots, 2l+1\}$, each used at most twice total. Strict column ⟹ each label at most once in column 1. Length $= 2l+1 = j$ = # labels, so column 1 uses each label exactly once, in sorted order:

$$\text{Col 1} = (1, 2, \ldots, 2l+1)^T.$$

**Step 2: Remaining data is a lattice path.** The $2l+1$ remaining label copies distribute between columns 2 (length $l+m+1$) and 3 (length $l-m$). Let $S_2, S_3 \subseteq \{1, \ldots, 2l+1\}$ denote the label sets, so $|S_2| = l+m+1$, $|S_3| = l-m$, $S_2 \sqcup S_3 = \{1, \ldots, 2l+1\}$. Given the sets, columns are uniquely determined (sorted).

**Step 3: Constraints collapse to ballot.** Let $s_i^{(k)}$ = $i$-th smallest element of $S_k$. Row-weakly-increasing (row $i$ has $(i, s_i^{(2)}, s_i^{(3)})$) needs $s_i^{(2)} \ge i$ (automatic, since $s_i^{(2)}$ is $i$-th of a subset of $\{1, \ldots, 2l+1\}$) and $s_i^{(3)} \ge s_i^{(2)}$. This is:

$$r_3(k) \le r_2(k) \quad \text{for all } k \in \{1, \ldots, 2l+1\}$$

where $r_j(k) = |S_j \cap [1, k]|$.

**Step 4: Encode as lattice path.** Label $q$ contributes an $E$-step if $q \in S_2$, $N$-step if $q \in S_3$. Path from $(0,0)$ to $(l+m+1, l-m)$, staying weakly below the diagonal. Standard ballot count:

$$K = \binom{a+b}{b} - \binom{a+b}{b-1} = \binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}. \quad \square$$

Even $j$ case is identical *mutatis mutandis*.

## The alternating identities

### Identity (2A) — even $j = 2l$

$$\sum_{m=0}^{l} (-1)^m \left[\binom{2l}{l-m} - \binom{2l}{l-m-1}\right] = 0.$$

**Proof.** Reindex $r = l-m$. Split, reindex second. Reduce to sub-lemma:

$$2 \sum_{r=0}^{l-1} (-1)^r \binom{2l}{r} + (-1)^l \binom{2l}{l} = 0. \tag{$\dagger$}$$

Sub-lemma follows from $(1-1)^{2l} = 0 = \sum_r (-1)^r \binom{2l}{r}$ + binomial symmetry $\binom{2l}{r} = \binom{2l}{2l-r}$: the sum from $r = l+1$ to $2l$ equals the sum from $r = 0$ to $l-1$ (with correct signs). $\square$

### Identity (2B) — odd $j = 2l+1$

$$\sum_{m=0}^{l} (-1)^m (m+1) \left[\binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}\right] = 0.$$

**Proof.** Reindexing $r = l-m$ and telescoping gives

$$T := \sum_{r=0}^{l} (-1)^r (2l+1-2r) \binom{2l+1}{r} = 0. \tag{2B$'$}$$

**Key identity:** $(n-2r)\binom{n}{r} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$ for $r \ge 0$. (Direct: expand $2r\binom{n}{r} = 2n\binom{n-1}{r-1}$, apply Pascal.)

Applying with $n = 2l+1$:

$$T = (2l+1) \sum_{r=0}^{l} (-1)^r \left[\binom{2l}{r} - \binom{2l}{r-1}\right] = (2l+1) \cdot (\text{2A}) = 0. \quad \square$$

**The takeaway.** Identity (2B) is *literally* $(2l+1)$ times Identity (2A) at $n = 2l$, after a reindex and application of a Pascal-adjacent identity. **The odd-$j$ identity is forced by the even-$j$ one.**

## Meta-technique — "differentiate the generating function"

The 1-line reduction (2B) → (2A) is an instance of a general pattern:

**Pattern.** Any alternating Kostka-weighted sum with polynomial-in-$m$ coefficients reduces to unweighted sums via iterated application of $(n-2r)\binom{n}{r} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$ (or the equivalent generating-function operator $\theta \partial_\theta$).

Concretely: for polynomial $P(m)$ of degree $d$,

$$\sum_m (-1)^m P(m) K_{\mu_m', (2^j)} = \sum_{k=0}^{d} c_k \cdot \sum_r (-1)^r (n - 2r)^{k} \binom{n}{r} / (\text{correction})$$

and each $(n-2r)^k$ factor can be absorbed by a chain of $\binom{n-1}{r} - \binom{n-1}{r-1}$ substitutions.

**Application to StructB general-$d$:** the identities at $d < d_{\max}$ have polynomial-in-$\mu_1$ weights (since subleading-$t$ terms of $s^*_\mu$ scale polynomially in $\mu_1$). The generating-function operator machinery may reduce ALL of them to a small number of base identities.

## What this doesn't do (yet)

- Doesn't handle $d < d_{\max}$. There, the identities (as stated Day 118) are FALSE because subleading-$t$ terms of $s^*_\mu$ with $d_\mu > d$ contribute. **New machinery needed.**
- Doesn't handle the odd-$j$ $s^0$-part at $d_{\max}$. Needs auxiliaries (C1), (C2) — currently empirical.
- Doesn't handle general narrow-shape Kostka. The forced-column-1 argument works when # labels = column-1 length. For $\mu_1 = j+1$ (Kostka = 0) or $\mu_1 = j-1$ (column 1 shorter than # labels, "W-step" needed) the argument requires modification.

## Broader significance

**As a Kostka combinatorics vignette.** $K_{(3^a, 2^b, 1^a), (2^{2a+b})} = \binom{2a+b}{a} - \binom{2a+b}{a-1}$ is a clean specialization worth stating in isolation. Might be in a Kostka survey (Fulton, Sagan, Stanley EC2 §7.10-7.11); might be genuinely new for these shapes.

**As a template for the Layer-Shape endgame.** The pattern "reduce Kostka on narrow shape → lattice-path count → ballot" combined with "reduce alternating polynomial-weighted sum → unweighted via $(n-2r)$ trick" gives Rick a **complete toolkit** for the Kostka-cancellation side of StructB. What's left is to (i) extend from spine shapes to general narrow shapes and (ii) handle subleading-$t$ coupling for $d < d_{\max}$.

**As a Path 1 signal.** Ballot numbers appear in the Kostka $\to$ Schur $\to$ Hopf lift naturally. The fact that spine-shape Kostkas are ballot numbers is a residual manifestation of factorial-Sym structure. Combined with Day 117's Stirling discovery, Rick's shifted-Schur filtration is showing factorial-Sym signatures at every level of granularity.

## Files

- `proofs/2026-08-20-day119-kostka-ballot-identities.md` — full writeup with numerical verification.
- `beta-prime/code/day119/ballot_identity.py` — Kostka formula verified $j \le 15$; (2A) verified even $j \le 28$; (2B) verified odd $j \le 29$.
- `beta-prime/code/day119/kostka.py` — bug-fixed Kostka table.
- `for-collaborator/2026-08-20-day119-ballot-kostka-status.md` — Robin update.

## The one-line lesson

**Kostka on narrow shapes is a lattice-path count once you find the forced column.**

— Rick, Day 119 dream, 2026-08-20.
