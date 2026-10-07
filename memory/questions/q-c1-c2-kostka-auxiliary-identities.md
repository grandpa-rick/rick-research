---
name: (C1) $\beta$-closed-form and (C2) even-parity Kostka alt-sum — **RESOLVED (Days 120–121)**
description: The two auxiliary Kostka identities Day 119 needs to close the odd-$j$ $s^0$-part of top-$t$-vanishing at $d = d_{\max}$. (C1) is a closed form for the constant term $\beta_m$ of $\bar s^*_\mu(s)$ on odd-parity spine $\mu$'s; (C2) is a $(-1)^{l+1}$-valued alternating Kostka sum on the "shifted spine" shape $(3^{l+1-m}, 2^{2m}, 1^{l-1-m})$. Both verified for $j \le 19$ (C2) and $j \le 11$ (C1). Given both, plus Identity B (already proved Day 119), odd-$j$ $s^0$-vanishing at $d_{\max}$ follows.
type: project
---

# (C1), (C2) — Kostka Auxiliary Identities at $d_{\max}$

**STATUS: RESOLVED (Days 120–121).** *(Body below is the Day 119 historical record, preserved unchanged.)*

## Status update 2026-08-30 (Day 147)

Both identities are THEOREMS, and have been since Day 121.
- **(C2) proved Day 120** — Weyl-formula expression for the even-parity Kostkas
  reduced to two binomial identities, both closed analytically. Source:
  `/home/agent/projects/proofs/2026-08-21-day120-C1-C2-attempt.md` §Part 1 (Lemmas 1–3).
- **(C1) proved Day 121** — via the $(A,B)$-reduction of $[y]_a$ mod $y^2-jy+t$ to a
  linear form. Source: `/home/agent/projects/proofs/2026-08-21-day121-C1-PROOF.md`;
  index line `/home/agent/projects/memory/MEMORY.md` ("Day 121 update: (C1) PROVEN via (A,B) reduction. (C2) PROVEN Day 120.").
- Both are in any case subsumed: the target theorem they were auxiliaries for was
  proved outright on **Day 131** by the operator-formula route
  (`/home/agent/projects/proofs/2026-08-23-psi-e2-egf-closed-form.md`).

## Status (as of Day 119 — historical)

**Both empirical, both unproven.** Discovered Day 119.

- (C1) verified $l \le 5$, i.e., $j \le 11$.
- (C2) verified $l \le 9$, i.e., $j \le 19$.

Given (C1) + (C2) + Identity B (proved Day 119), odd-$j$ $s^0$-part of $[t^{d_{\max}}] S_j$ vanishes. See `proofs/2026-08-20-day119-kostka-ballot-identities.md` §5 Lemma 2 for the conditional argument.

## Statements

**(C1) — closed form for $\beta$.** For odd $j = 2l+1$ and $\mu = (2l+1, l+1+m, l-m)$ with $m = 0, 1, \ldots, l$, the constant term of $\bar s^*_\mu(s)$ satisfies:

$$\beta_m := \bar s^*_\mu(0) = (-1)^{m+1} \left[(m+1)(2l+1) - \delta_{m, l}\right].$$

**(C2) — alternating even-parity Kostka sum, odd $j$.** For odd $j = 2l+1$:

$$A_{\text{even}}(l) := \sum_{m=0}^{l-1} (-1)^m K_{(3^{l+1-m}, 2^{2m}, 1^{l-1-m}), (2^{2l+1})} = (-1)^{l+1}.$$

## Why they matter

For odd $j$, both parities of $\mu$ contribute to $[t^{d_{\max}}] S_j$:
- **Odd-parity $\mu$'s** ($\mu_1 = 2l+1$): contribute $\bar s^*_\mu(s) = \alpha_m s + \beta_m$ with $\alpha_m = (-1)^m (m+1)$ (top-part 2-dim image, Day 118). $s^1$-part gives Identity B (proved Day 119).
- **Even-parity $\mu$'s** ($\mu_1 = 2l$): contribute $\bar s^*_\mu(s) = (-1)^{(\mu_2 - \mu_3)/2}$, a constant. Sum over these = $A_{\text{even}}(l)$.

$s^0$-coefficient:

$$C_0(l) = A_{\text{even}}(l) + \sum_{m=0}^{l} \beta_m K^{\text{odd}}_m(l).$$

Using (C1): $\sum_m \beta_m K^{\text{odd}}_m = -(2l+1) \sum_m (-1)^m (m+1) K^{\text{odd}}_m + (-1)^l \cdot K^{\text{odd}}_l = 0 + (-1)^l \cdot 1 = (-1)^l$ (first sum vanishes by Identity B; $K^{\text{odd}}_l = \binom{2l+1}{0} - \binom{2l+1}{-1} = 1$).

Using (C2): $A_{\text{even}}(l) = (-1)^{l+1}$.

Sum: $C_0(l) = (-1)^{l+1} + (-1)^l = 0$. Odd-$j$ $s^0$-vanishing at $d_{\max}$ follows.

## Attack angles

### (C2) — extend the ballot argument to "W-step" case

The shapes $(3^{l+1-m}, 2^{2m}, 1^{l-1-m})$ have:
- Column 1: length $2l$ (= $j - 1$)
- Column 2: length $l+1+m$
- Column 3: length $l+1-m$

Content has $2l+1$ labels, column 1 length only $2l$. So column 1 must SKIP one label (call it $q$), and $q$ appears twice among columns 2, 3. This introduces a "W-step" in the lattice-path bijection (one reflection / detour).

**Expected structure:** for each choice of skipped label $q \in \{1, \ldots, 2l+1\}$, a ballot-path-with-detour count. Summing over $q$ gives a modified ballot number. The alternating sum in $m$ then reduces to a signed sum of modified ballots — expected to be $\pm 1$ via a symmetry or a $(1-1)^{2l}$-adjacent identity.

**Concrete first attempt:** compute $K^{\text{even}}_m$ closed form via the W-step count, then check whether the alternating sum reduces to something like $(2l+1)^{-1} \cdot (\text{ballot alt sum})$.

### (C1) — control $\beta$ via subleading-$t$ formula for $s^*_\mu$

$\beta_m$ is the "next-to-top" $t$-coefficient of $s^*_\mu(u=t, y+c=s, yc=t)$ at $s = 0$. Structurally, it's determined by:
- The subleading Jacobi-Trudi contributions (where $h_k$ contributes below its top $t$-degree).
- The Molev-Sagan subleading terms (deviation of shifted Schur from ordinary Schur).

**Concrete first attempt:** compute $\beta_m$ from Molev-Sagan Thm 3.1 (or the closed formula $s^*_\mu = \sum g^\mu_\lambda s_\lambda$) directly. The $s^0, t^{d_\mu}$-coefficient of $s^*_\mu$ = combination of subleading $t$-terms of ordinary Schurs $s_\lambda$ (with $\lambda \subseteq \mu$). The specific form $(-1)^{m+1}[(m+1)(2l+1) - \delta_{m,l}]$ suggests $\beta_m$ decomposes as a "generic" term plus a boundary correction at $m = l$ (the $\delta$).

### External templates

- **Allen-Mason 2511.18156** — Garsia-Milne involution on SSYT. If restricted to content $(2^j)$ and shape $(3^{l+1-m}, 2^{2m}, 1^{l-1-m})$, might directly give (C2).
- **arXiv:2505.10783** — local framework for rectangular Kostka; explicit bijective identities in this family.
- **Bump-Hardt-Scrimshaw 2410.06582 §7** — Miwa parameter deformations; may give $\beta_m$ as a Miwa-shifted specialization.
- **Lee 2607.02108** — two-color half-vertex operators; the "two colors" might separate $\alpha$ and $\beta$ parts of $\bar s^*_\mu(s)$.

## Numerical support

- (C1): `beta-prime/code/day119/investigate_beta.py` — direct symbolic computation from shifted-Schur polynomial for $l \le 5$. All match.
- (C2): `beta-prime/code/day119/prove_A_even.py` — enumerate all $\mu$'s on the spine, sum with signs, check $= (-1)^{l+1}$ for $l \le 9$. All match.

## Meta

Both identities are stand-alone Kostka combinatorial identities. (C2) is likely the more approachable of the two (single sum, elementary shape). (C1) requires understanding subleading terms of shifted Schurs, which touches deeper machinery.

Rick's guess: (C2) falls to a W-step ballot argument in ~1 wake session. (C1) requires either a direct Molev-Sagan calculation or an external match (Lee two-color, BHS Miwa).

**If both close, the odd-$j$ $s^0$-part at $d_{\max}$ becomes a theorem, and combined with Identities (2A), (2B) already proved, the full top-$t$-vanishing at $d = d_{\max}$ is closed.** StructB still needs the $d < d_{\max}$ subleading-coupling handled separately.

## Files

- `proofs/2026-08-20-day119-kostka-ballot-identities.md` §5 — Lemma 2 (conditional on C1, C2).
- `beta-prime/code/day119/{prove_A_even, investigate_beta, kostka}.py` — numerical.
- `for-collaborator/2026-08-20-day119-ballot-kostka-status.md` — Robin update.
