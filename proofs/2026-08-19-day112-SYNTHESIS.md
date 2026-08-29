---
title: Day 112 (2026-08-19) — Wake synthesis and punch-list
status: SYNTHESIS — proved, reduced, and still-empirical items sorted
---

# Day 112 Synthesis

A punch-list summary of the Day 112 wake session. Sorts every result into one of
three bins: **PROVED**, **REDUCED-modulo-lemma**, or **EMPIRICAL** (not yet
proved). Deliberately honest about status.

---

## Big-picture headline

**$(\star)_{R=2}$ is a theorem modulo a single technical lemma** — Sublemma
$(\star\star\text{-}a'')_{p=1}$ (and its $b$-mirror). Everything else that
appeared to block $(\star)_{R=2}$ has closed:

- Slice-0 = (M), PROVED (Day 109).
- Slice-1 = $(R_1)$, PROVED (Day 110).
- (T) = total-degree bound, PROVED **modulo $(\star\star\text{-}a'')$** (Day 112).
- Slice-2 at $R = 2$: unnecessary — Sahi–Okounkov consequence.

---

## Bin 1 — PROVED (unconditional)

Nothing new PROVED unconditionally today. Standing base:
- (M) — Day 109 proof file.
- $(R_1)$ — Day 110 proof file.
- Layer formula $(\star)$ (Day 112) — a purely bookkeeping identity separating
  $P_j$ and $S_j$ contributions to $[a^{c-1-d}] H_c$.
- Sub-lemma (E) — elementary-symmetric $e_i(3, \ldots, c+1-j)$ is a polynomial
  in $j$ of degree $\leq i$ (Day 112, standard).
- Lemma 1 — $\deg_a S_j \leq j$ (Day 112, via vertical-2-strip walk-count bound
  $\mu_1 \leq j$; each vertical strip places at most one cell per row).
- Special case $(\star\star\text{-}a'')_{p=0}$: telescope
  $Q_j(b) \cdot (b+c)^{\underline{j}} = (b+2)_{c-1}$, a Chu-Vandermonde-style
  Pochhammer identity.

---

## Bin 2 — REDUCED (proved modulo a stated lemma)

### (T-a): $\deg_a Q_{2R} \leq R$

**PROVED modulo $(\star\star\text{-}a'')_{p \geq 1}$.** The full assembly is in
`/home/agent/projects/proofs/2026-08-19-day112-Ta-proved.md`. Structure:

1. Layer formula $(\star)$ decomposes $[a^{c-1-d}] H_c(a, b, j)$ into a sum
   over $p \in \{0, \ldots, d\}$ of $E_{d-p}(j) \cdot Q_j(b) \cdot A_p(b, c, j)$.
2. Sub-lemma (E) bounds $j$-degree of $E_{d-p}$ by $d - p$.
3. Sub-lemma $(\star\star\text{-}a'')_p$ factors $Q_j(b) \cdot A_p(b, c, j) =
   (b+2)_{c-1-2p} \cdot R_p(b, c, j)$ with per-$b$-slot $j$-degree of $R_p$
   bounded by $2p$.
4. Product $j$-degree per slot $\leq (d-p) + 2p = d + p \leq 2d$.
5. For $d \leq R - 1$, $2d < 2R$, so the order-$2R$ finite difference
   $\Delta^{2R}$ kills the layer.

Every step is proved except the general case of $(\star\star\text{-}a'')$.
Empirical: $(\star\star\text{-}a'')_p$ verified for $p \in \{0, 1, 2, 3, 4\}$
at $c \in \{12, 15, 18\}$.

### (T-b): $\deg_b Q_{2R} \leq R$

**PROVED modulo $(\star\star\text{-}b'')$** by verbatim swap $(a \leftrightarrow
b)$ of the (T-a) argument. The $a \leftrightarrow b$ symmetry of $Q_{2R}$
(Day 109 Rmk R2) makes this immediate.

### (T): total $(a, b)$-degree $\leq 2R$

**PROVED modulo $(\star\star\text{-}a'')$ + $(\star\star\text{-}b'')$.**
Reason: (T-a) says every monomial has $a$-power $\leq R$; (T-b) says every
monomial has $b$-power $\leq R$; sum $\leq 2R$.

### $(\star)_{R=2}$

**THEOREM modulo $(\star\star\text{-}a'')_{p=1}$ + $(\star\star\text{-}b'')_{p=1}$.**
Reason (Rick's Sahi–Okounkov mental calc):

At $R = 2$, the Sahi–Okounkov Newton interpolation ansatz $Q_4 = \sum_{k=0}^2
f_k(c) (a+2)^{\underline{k}}(b+1)^{\underline{k}}$ has three unknowns
$f_0, f_1, f_2$. Slice-0 = (M) fixes $f_0$. Slice-1 = $(R_1)$ fixes $f_1$.
(T) says the total $(a, b)$-degree is $\leq 4 = 2R$, which forces
$\deg f_2 \leq 0$ in the free parameter $a_{12}$ — i.e., only the constant part
of $f_2$ remains free relative to what's already determined; and this constant
is fixed by any additional evaluation. So Slice-2 is **automatic** at $R = 2$
from (M) + $(R_1)$ + (T) + symmetry.

At $R = 3$ this fails: a free parameter $a_{14}$ remains after Slice-0 +
Slice-1 + (T) + symmetry, so Slice-2 must be proved independently.

---

## Bin 3 — EMPIRICAL (not yet proved)

### $(\star\star\text{-}a'')_p$ for $p \geq 1$

Verified $p \in \{1, 2, 3, 4\}$ at $c \in \{12, 15, 18\}$. **This is the ONLY
remaining lemma between Day 112 and full $(\star)_{R=2}$.** Structure of
factorization is empirically compatible with a Chu-Vandermonde-style Pochhammer
identity plus a $\kappa_\mu$ walk-count bound.

### Sub-claim $(\star\star)$ at $H_c$-level

Verified for $R = 2, 3, 4, 5$ at fixed $c = 25$, 91 slots, zero violations.
Bound is that $[a^i b^k] H_c(a, b, j)$ has $j$-degree $\leq \text{TOP} - i - k$.

**Tighter observed pattern:** $j$-degree at slot $(24 - p, 24 - q)$ with $p + q = d$
equals **exactly $2 \min(p, q)$** — a min-of-two-displacements structure. Only
even $j$-degrees occur, and only slots with $p \approx q$ approach the naive
bound.

Note: $(\star\star)$ is NOT needed for the Day 112 proof of (T-a); the layer-formula
+ $(\star\star\text{-}a'')$ route bypasses $(\star\star)$ entirely.

### Sub-claim $(\star\star\star)$ — FALSE as originally stated

Empirical (Day 112) $j$-degree of $[a^{j-u} b^{j-v}] S_j$ is $\sim 2(u + v)$,
**not** $\leq u + v$. Naive reduction $H_c$-level $(\star\star)$ → $S_j$-level
$(\star\star\star)$ is invalid. Cancellation happens INSIDE the convolution
$P_j \cdot Q_j \cdot S_j$, not at $S_j$ alone.

**Consequence:** the Day 111 proof-sketch strategy for $(\star\star)$ is dead;
however the Day 112 (T-a) route sidesteps the failure — because $(\star\star\text{-}a'')$
factors $Q_j \cdot A_p$ together and only bounds the combined polynomial's $j$-degree.

### Slice-2 per-term via Chu-Vandermonde — DOES NOT SPLIT

Splitting $(U_2)$ into 4 pieces $T_0, T_1, T_{2A}, T_{2B}$ and running each
through the pipeline gives four $Q^{(X)}_{2R}$ each of $b$-degree $2R$ (or $2R-1$).
The Slice-2 bound $\deg_b Q_{\text{sum}} \leq 2$ is a CANCELLATION IDENTITY across
all 4 pieces, verified for $R = 2, 3, 4$ (explicit closed forms).

**Consequence:** direct per-term Chu-Vandermonde attack on Slice-2 does not
suffice. The right route is via the Sahi–Okounkov interpolation framework
(with (T) doing the work).

### $\kappa_\mu$ walk-count $j$-degree

Empirical: $\kappa_\mu$ for $\mu = (2j - 2r - s, r + s, r) \in \mathcal{S}_j$
is a polynomial in $j$ of degree $\leq r$ (probably tight bound $\lfloor r/2 \rfloor$
by parity). Would follow from direct enumeration of vertical-2-strip walks.

---

## Structural insights

1. **The (T-a) + (T-b) split is a game-changer.** (T) = total-degree $\leq 2R$
   was a 2D problem. Splitting it into (T-a) $\wedge$ (T-b) reduces it to two
   1D problems, each solvable by 1D finite differences applied to the layer
   formula. The 2D convolution cancellation that killed $(\star\star\star)$ is
   not needed for either 1D problem — each 1D problem has enough room to
   accommodate the factor-of-2 slack.

2. **The factor of 2 in $j$-degree per $S_j$-slot is REAL.** Attempts to prove
   a $j$-degree bound $\leq p$ on $[a^{j-u} b^{j-v}] S_j$ will fail; the true
   bound is $\leq 2p$. This slack is absorbed by the Pochhammer factor $Q_j(b)$
   via the $(\star\star\text{-}a'')$ factorization: $Q_j(b) \cdot A_p =
   (b+2)_{c-1-2p} \cdot R_p$, where dividing out the $(b+2)_{c-1-2p}$ subtracts
   $c - 1 - 2p$ from the $b$-degree count — exactly the counter-move that
   makes the finite-difference argument work.

3. **Sahi–Okounkov at low $R$ is much stronger than at high $R$.** At $R = 2$,
   Slice-0 + Slice-1 + (T) + symmetry saturates the ansatz. At $R = 3$, one
   free parameter remains; Slice-2 must be proved. Growth of the "gap" is
   $R - 2$ slice-lemmas per $R$. So a uniform proof of $(\star)$ needs an
   argument that scales in $R$ — the Interpolation-Slice framework is
   exactly this.

4. **The $H_c$-level $(\star\star)$ pattern $j$-deg $= 2 \min(p, q)$ points
   to a hidden symmetric-function identity.** Only slots on the "diagonal"
   $p \approx q$ approach the naive bound; the off-diagonal slots have
   $j$-degree strictly smaller. This begs for a shifted-Schur / plethystic
   interpretation. Not needed for $(\star)_{R=2}$, but likely the key to a
   clean proof of $(\star\star)$ for general $R$.

---

## What's next

**Immediate next PROVE-session target:** prove $(\star\star\text{-}a'')_{p=1}$
(and its $b$-mirror). This closes $(\star)_{R=2}$ FULLY.

**Structural approach:** enumerate the $\mathcal{S}_j$-partitions with $\mu_1 =
j - 1$ (contributing to $A_1$), compute their aggregate shifted-Schur
contribution, and verify the Pochhammer factorization. The $p = 0$ case's
Chu-Vandermonde telescope $(b+2)_{c-1-j}(b+c)^{\underline{j}} = (b+2)_{c-1}$
suggests the $p = 1$ analogue should be a two-step Pochhammer telescope with
a residual quadratic factor.

**Alternative:** direct symbolic proof of the factorization for $p = 1$ using
sympy or Lean. The $p = 1$ case is small enough to be tractable by hand.

**Secondary:** prove $(\star\star\text{-}a'')_p$ uniformly in $p$ (needed for
$(\star)$ at all $R$). This is the general-$R$ endgame.

---

## Files (Day 112)

- Per-term Slice-2 analysis: `/home/agent/projects/proofs/2026-08-19-day112-slice2-per-term.md`
  and script `.../beta-prime/code/2026-08-19-slice2-per-term.{py,txt}`.
- $(\star\star)$ empirical verification: `.../proofs/2026-08-19-day112-T-verification.md`
  and script `.../beta-prime/code/2026-08-19-T-sub-claim-verify.{py,txt}`.
- $(\star\star\star)$ negative result: `.../proofs/2026-08-19-day112-star-star-star-attempt.md`
  and scripts `.../beta-prime/code/2026-08-19-star-star-star-verify{,-v2}.{py,txt}`.
- (T-a) proved modulo $(\star\star\text{-}a'')$: `.../proofs/2026-08-19-day112-Ta-proved.md`
  and script `.../beta-prime/code/2026-08-19-Ta-verify.{py,txt}`.
- This synthesis: `.../proofs/2026-08-19-day112-SYNTHESIS.md`.

## Meta

The Day 112 wake shifted the endgame from "prove (T) as a 2D convolution
cancellation" to "prove a single Pochhammer factorization $(\star\star\text{-}a'')$
as a 1D lemma family". This is a much smaller target. The dead-end on
$(\star\star\star)$ was worth its cost — it revealed the factor-of-2 slack
that the correct proof structure must absorb via $Q_j(b)$.

**Streak: Days 104–112, NINE consecutive wake sessions delivering escalating
results.**
