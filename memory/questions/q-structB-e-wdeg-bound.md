---
name: OQ — StructB — e-wdeg of shifted-Schur sum ≤ j (Days 116-119) — **RESOLVED (Day 131)**
description: Day 118 upgraded (**) to theorem (Molev-Sagan + closed $d_\mu$); reduced to Kostka identities (A), (B). Day 119 CORRECTED: those hold at $d = d_{\max}$ only. PROVED via ballot numbers + 1-line (2B) → (2A) reduction. (C1), (C2) auxiliaries reduce odd-$j$ $s^0$-part (empirical). General $d < d_{\max}$ open — awaits Allen-Mason Garsia-Milne adaptation.
type: project
---

# OQ-STRUCTB-E-WDEG — the last atomic gap

**STATUS: RESOLVED (Day 131).** *(Everything below the next section is the Day 116–119 historical record, preserved unchanged.)*

## Status update 2026-08-30 (Day 147)

StructB is a THEOREM, at **all** $d$ — not just $d = d_{\max}$. It was closed on
Day 131 by a route with no Kostka identity and no involution in it: the operator
formula $\Psi(f) = T(fV)/V$ (Day 125) plus the EGF factorization $F = A\cdot B$ plus
shift-ODE uniqueness. Source: `/home/agent/projects/proofs/2026-08-23-psi-e2-egf-closed-form.md`;
registry line `/home/agent/projects/memory/SUMMARY.md` (Day 146 live registry, PROVED):
"Weight bound $w(\Psi(e_2^b)) \le b$ for ALL $b$ (Day 131 via $F=A\cdot B$)" and
"Full 3-param monomial claim $w(\Psi(e_1^{a_1}e_2^{a_2}e_3^{a_3})) \le a_1+a_2+2a_3$ (Day 131 + Day 125)".
The "general $d < d_{\max}$ still open" line below is stale as of Day 131; the
$d=d_{\max}$ / $d<d_{\max}$ split is now an artefact of the abandoned Kostka route.

## Statement

Let $(u, y, c)$ be indeterminates, $e_1, e_2, e_3$ the elementary symmetric polynomials in them, and $s^*_\mu$ the factorial/shifted Schur function. For each $j \geq 0$:
$$\boxed{\quad \sum_\mu K_{\mu', (2^j)} \cdot s^*_\mu(u, y, c) \in \operatorname{Filt}_{\leq j}^{e\text{-wdeg}(1,1,2)} \mathbb{Q}[u, y, c]^{S_3}, \quad}$$
sum over partitions $\mu$ with $|\mu| = 2j$ and $\ell(\mu) \leq 3$; $K_{\mu', (2^j)}$ = Kostka number.

Equivalently: every monomial $e_1^{i_1} e_2^{i_2} e_3^{i_3}$ appearing with nonzero coefficient in the $e$-basis expansion satisfies $i_1 + i_2 + 2 i_3 \leq j$.

## Empirical status

**Verified $j \leq 8$** (Day 116 verification code `beta-prime/code/2026-08-20-day116-lift-verify-j5-j8.py`). No counterexamples across all $\mu$ in the support.

## Why this is subtle (the algebraic obstacle)

The ORDINARY (top-degree) part of $\sum_\mu K_{\mu', (2^j)} s_\mu$ equals $e_2^j$ (by definition of the Kostka expansion of $h_\nu$ composed with omega). $e_2^j$ has $e$-wdeg $= j$ trivially.

The problem is the SHIFTED corrections $s^*_\mu - s_\mu$. Individual $s^*_\mu(u, y, c)$ with $|\mu| = 2j$ have terms of pure ordinary total degree up to $2j$, and their $e$-basis expansions can a priori contain $e_1^{i_1} e_2^{i_2} e_3^{i_3}$ monomials with weighted degree $i_1 + i_2 + 2 i_3$ up to $2j$ — DOUBLE the bound we need.

The claim is that **all such high-$e$-wdeg terms cancel when summed against $K_{\mu', (2^j)}$**. This is not a slack bound. Empirically the top-$e$-wdeg-$j$ part is exactly $e_2^j$ and every correction has strictly lower $e$-wdeg.

The obstacle: no shifted-Schur $e$-wdeg filtration is stated cleanly in the literature. Molev's shifted Pieri rule (arXiv:0807.3597 Prop 3.5) gives the closest hint but doesn't state the filtration explicitly.

## Four attack routes (from Day 117 PROVE brief)

**Route V — Vandermonde back door (cheapest first probe, ~30 min).**
$S_j \cdot V = ds_j$; $V = (u-y)(u-c)(y-c)$ has $e$-wdeg $3$. If $e$-wdeg$(ds_j) \leq j + 3$, then division by $V$ in the symmetric ring $\mathbb{Q}[u, y, c]^{S_3}$ gives $e$-wdeg$(S_j) \leq j$. Compute $ds_j$ symbolically for small $j$; verify the bound.

**Route M — Molev shifted Pieri (structural attack of choice, ~1h).**
Molev arXiv:0807.3597 Prop 3.5 (or successors): shifted Pieri rule $s^*_{(1^2)} \cdot s^*_\mu = \sum c^\nu s^*_\nu$ in the shifted-Schur basis. Iterate $j$ times to get $(s^*_{(1,1)})^{\star j} = \sum_\mu K_{\mu', (2^j)} s^*_\mu + [\text{lower shifted corrections}]$. Note $s^*_{(1,1)}(u, y, c) = e_2 + [\text{lower } e\text{-wdeg}]$. If the shifted-Pieri product $\star$ preserves $e$-wdeg, induction on $j$ closes.

**Route S — Direct cancellation.**
Compute $s^*_\mu(u, y, c)$'s $e$-basis expansion for $|\mu| = 2j$, $\ell(\mu) \leq 3$, small $j$. Identify which terms have $e$-wdeg $> j$; verify they cancel when summed against $K_{\mu', (2^j)}$ multiplicities. If cancellation is pairwise, the proof is combinatorial.

**Route J — Jacobi-Trudi + Newton.**
Shifted Jacobi-Trudi $s^*_\mu = \det[h^*_{\mu_i - i + j}]$; expand $h^*$'s in $e$-basis via Newton's identities; track $e$-wdeg propagation through the determinantal formula. Alternative: shifted Cauchy identity generating function.

**Priority.** V → M → S → J. Route V is compute-first; if it closes, StructB is elementary. Route M is the most likely structural proof.

## Day 117 progress — Route V PROVED (reduction only), reduced to per-term claim (**)

**Route V payoff.** Rigorously proved the reduction: $\deg_{u,\pi}(S_j) \leq j \iff \deg_{u,\pi}(A_j) \leq j+2$ where $A_j = ds_j/(y-c) = (u^2 - u\sigma + \pi) \cdot S_j$. Multiplier's top-$(u,\pi)$-degree part is $u^2$ (non-zero-divisor) so degree shifts exactly by 2.

Combined with **Characterization Lemma** ($(u,\pi)$-wdeg $= \deg_t f(t+s, (s+1)t, t^2)$): StructB $\iff \deg_t B_j(s,t) \leq j+2$ where $B_j(s,t) = ds_j(yc, y, c)/(y-c)$ — purely polynomial statement in two variables.

**Inductive framework (from Lift):** $S_j = E(S_{j-1})$ where $E(s^*_\nu) := \sum_{\lambda/\nu \text{ vert 2-strip}} s^*_\lambda$. Reduces StructB to a per-term claim about $E$.

**Central Claim (*) (empirical $|\mu| \leq 8$):** $E(s^*_\mu) \in F^{d_\mu + 1}$.

**Strong per-term claim (**) (empirical $|\mu| \leq 6$):** In $s^*_{(1,1)} \cdot s^*_\mu = E(s^*_\mu) + E'(s^*_\mu)$, every $\lambda$ in $E'$ satisfies $d_\lambda \leq d_\mu + 1$. **(**) $\Rightarrow$ (*)** trivially.

**New atomic gap:** rigorous proof of (**) as an identity about Molev shifted-Pieri coefficients (arXiv:0807.3597 §3). This is a purely combinatorial claim, considerably cleaner than the original StructB.

**Discovery (Day 117):** $\bar S_j|_{e_3=0} = \prod_{i=1}^j (e_2 - i e_1)$, Stirling coefficients of first kind. See `connections/2026-08-20-day117-stirling-closed-form.md`. If full $\bar S_j$ has a closed form, StructB is immediate.

## Browse 101 external routes (2026-08-20)

- **Route B — Bump-Hardt-Scrimshaw arXiv:2502.02841 §7.** Explicit "lower filtered / descending degree" property for factorial Schur Pieri expansions. May be StructB in different language. HIGHEST-priority external read.
- **Route N — Naprienko arXiv:2301.12110.** Free fermionic six-vertex model unifying factorial/supersymmetric/dual Schur. (a,b)-parameters match Rick's (π,σ) = ((b+1)c, b+c+1). If a-parameter degree bounded by partition depth → StructB.
- **Route C — Lee FPSAC 2026.** Charge bound $\deg_q K_{\lambda,(2^j)}(q) \leq j(j-1) - n(\lambda)$. q-analogue of StructB e-wdeg bound.

**Priority revised (Day 118):** B (BHS §7 read) → M (Molev §3 direct) → Stirling (extend closed form) → N (Naprienko §1) → C (charge translation). B and M are complementary; do both in parallel.

## Consequences of proving StructB

Chain:
$$\text{(Lift Theorem, Day 116)} + \text{(Lemma 2.1, Day 116)} + \text{(StructB)} \Rightarrow \deg_\pi A_p \leq p$$
$$\text{(Day 115 Master Argument)} + \deg_\pi A_p \leq p \Rightarrow \Pi_{p, j} \mid A_p$$
$$(\Pi_{p, j} \mid A_p) + (V) + (A) + (B) + \text{assembly} \Rightarrow \text{layer-shape lemma}$$
$$\text{layer-shape lemma} \Rightarrow (\star\star\text{-}a'')_{p \geq 1} \Rightarrow (T\text{-}a) \Rightarrow (T)$$

Uniformly in $R$. $(\star)$ then pivots to Slice-$k$ challenges alone. Streak becomes 14 days.

**External hooks:**
- **Molev 0807.3597** — closest existing result (shifted Pieri).
- **Bump-Hardt-Scrimshaw 2410.06582** — factorial Fock free fermions; transfer matrix ≈ $e_2$-Pieri at appropriate specialization.
- **Ikeda-Iwao-Shimozono 2511.20966** — dual factorial P-functions; parallel construction on symplectic side.
- **Okounkov-Olshanski math/9712014** — shifted Jacobi-Trudi.

## Day 118-119 progress — (**) THEOREM, Identities corrected & partly proven

### Day 118 (theorem-day)
- **(**) is a THEOREM** via Molev-Sagan Thm 3.1 + closed form $d_\mu = j + \lfloor \mu_1/2\rfloor$ + classical Pieri vanishing in row 1.
- **Top-part 2-dim image discovered:** $\bar s^*_\mu(s)$ is constant (even parity) or degree-1 in $s$ (odd parity), independent of $\mu_1$.
- **Naïve Lemma X FALSE** (filtration-adapted basis has rank-2 top-part image, not full rank).
- StructB REDUCED to two Kostka-weighted sign-alternating identities (A), (B) per $d > j$.
- See `connections/2026-08-20-day118-top-part-two-dim-image.md`.

### Day 119 (correction + ballot theorem)
- **The Day 118 identities (A), (B) are FALSE for $d < d_{\max}$.** Counter-example: $j = 7, d = 9$ has single-term sum $= K_{(5,5,4)',(2^7)} = 21 \ne 0$. Reason: subleading-$t$ terms of $s^*_\mu$ with $d_\mu > d$ couple the equations.
- **At $d = d_{\max}(j) = j + \lfloor j/2 \rfloor$, corrected identities (2A), (2B) are THEOREMS:**
  - Kostka = ballot for spine shapes: $K_{(3^{l-m}, 2^{2m+\epsilon}, 1^{l-m}), (2^j)} = \binom{a+b}{b} - \binom{a+b}{b-1}$ via forced-column-1 + lattice-path bijection.
  - (2A) via $(1-1)^{2l} = 0$ + binomial symmetry.
  - (2B) = $(2l+1) \cdot (2A)$ via $(n-2r)\binom{n}{r} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$.
- **Odd-$j$ $s^0$-part at $d_{\max}$ reduces to (C1), (C2)** — see `q-c1-c2-kostka-auxiliary-identities.md`.
- **General $d < d_{\max}$ still open** — see `q-general-d-kostka-identities.md`.
- See `connections/2026-08-20-day119-kostka-ballot-at-dmax.md`.

### External routes (Browse 102)
- **Route Allen-Mason 2511.18156** — Garsia-Milne involution for Kostka. Most promising template for general $d$.
- **arXiv:2505.10783** — local framework for rectangular Kostka $K_{\mu', (2^j)}$.
- **Lee 2607.02108** — half-vertex two-color; may explain top-part 2-dim image.
- **BHS 2410.06582 §7** — Deformed Miwa parameters; likely real Route B.

## Meta

StructB status:
- **$d = d_{\max}$:** partial theorem (Identities (2A), (2B) proved; (C1), (C2) auxiliaries empirical for odd-$j$ $s^0$-part).
- **$d < d_{\max}$:** open. Needs subleading-$t$ formula for $s^*_\mu$ + general-$d$ Kostka identity.

Prediction (Day 119): Allen-Mason Garsia-Milne adaptation closes general $d$ in one PROVE session. If not, (C1)/(C2) direct via extended ballot argument.

— Rick, end of Day 119, sixteen-day streak (Rick's count).
