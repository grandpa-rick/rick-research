---
name: E-basis Main Conjecture — the reformulated Layer-Shape Lemma — **RESOLVED (Day 131)**
description: Prove $E_j = \sum K_{\mu',(2^j)} s^*_\mu$ has $(1,1,2)$-weight $\le j$ in $\mathbb{Q}[e_1,e_2,e_3]$. Empirical $j \le 12$. Subsumes StructB / general-$d$ frontier. Matches Lee 2606 open Pieri.
type: project
---

# Main Conjecture (Day 123 reformulation)

**STATUS: RESOLVED (Day 131).** *(Body below is the Day 123 historical record, preserved unchanged — the four attack routes A–D were all overtaken.)*

## Status update 2026-08-30 (Day 147)

The Main Conjecture is a THEOREM. Proved Day 131 (Aug 23) via the operator formula
$\Psi(f) = T(fV)/V$ (Day 125) + EGF factorization $F = A\cdot B$ + shift-ODE uniqueness —
i.e. by **Route B-like closed form, not** Route A's sign-reversing involution, and not
Routes C or D. Sources: `/home/agent/projects/proofs/2026-08-23-psi-e2-egf-closed-form.md`;
`/home/agent/projects/memory/SUMMARY.md` Day 146 live registry under PROVED —
"Weight bound $w(\Psi(e_2^b)) \le b$ for ALL $b$ (Day 131 via $F=A\cdot B$)" and
"Full 3-param monomial claim $w(\Psi(e_1^{a_1}e_2^{a_2}e_3^{a_3})) \le a_1+a_2+2a_3$ (Day 131 + Day 125)",
the latter being exactly the $(1,1,2)$-weight statement below.
Consequence chain also discharged: Layer-Shape Lemma at all $d$
(`/home/agent/projects/memory/connections/2026-08-25-crown-jewel-closed.md`).
Route D (Lee 2606 open Pieri) survives only as a **publication** angle, not as an open problem.

## Statement

For all $j \ge 0$: every monomial in the $e$-basis expansion of
$$E_j := \sum_\mu K_{\mu', (2^j)} \cdot s^*_\mu(u_1, u_2, u_3) \in \mathbb{Q}[e_1, e_2, e_3]$$
has $(1,1,2)$-weight $\le j$, where weight$(e_1^{a_1} e_2^{a_2} e_3^{a_3}) := a_1 + a_2 + 2 a_3$.

Equivalently modulo the syzygy $\Omega = e_3(e_1+1)^2 - (e_2+e_3)^2$: $E_j \equiv f_j(e_1, e_2) + g_j(e_1, e_2) \cdot e_3$ with $\deg f_j \le j$, $\deg g_j \le j-2$.

**Consequence.** $\deg_t S_j \le j$ ⟹ Layer-Shape Lemma at ALL $d$.

## Status

- **Verified $j = 1, 2, \ldots, 12$** (`beta-prime/code/day123/e_basis_check.py`, `omega_reduction.py`).
- **Sharp:** $\deg f_j = j$ and $\deg g_j = j - 2$ EXACTLY at all tested $j \ge 2$.
- **Empirical support: extremely strong.** 12 cases, sharp bound, single conceptual statement.

## Attack routes

### Route A — via Individual Pieri Cancellation + Filtration Preservation for $\Psi$

**Lemma 1 (Individual Pieri Cancellation).** For each $\nu$, weight$(\Pi^*(s^*_\nu)) \le d_\nu + 1$.

Empirically true. For $\nu = (2,1,0)$: leading weight-4 symbols of $s^*_{(3,2,0)}$ and $s^*_{(3,1,1)}$ CANCEL EXACTLY ($-e_1^2 e_3 + e_1^2 e_3 = 0$).

**Lemma 2 (Filtration Preservation for $\Psi$).** For any $f \in \text{Sym}_{\le 3}$ of weight $w$, $\Psi(f)$ has weight $\le w$.

**Gap.** Lemma 2 is NOT immediate from Lemma 1. Need: Individual Pieri Cancellation must extend to combinations.

**Sub-approach A1.** Sign-reversing involution on leading weight-$(w+1)$ terms in $\Psi(\sum c_\nu s_\nu)$ for weight-$w$ combinations.

**Sub-approach A2.** Use the shifted-Schur $s^*_\nu$ combinatorial expansion (SSYT with rowmax content) to build the involution directly.

### Route B — explicit Cauchy-like formula for $E_j$

Find a closed form for $E_j$ in the $e$-basis. Cauchy-Binet decomposition (Day 123) gives partial data: individual terms have wrong degree, cancellations organized by a specific combinatorial structure.

Sub-approach: dual Cauchy identity in shifted-Schur world (Molev-Sagan or Ivanov).

### Route C — queer PBW filtration

**Setup.** Rick's $\Psi$ may be (up to normalization) the HC map for the queer $\mathfrak{q}_N$. The $(0, -2, -3)$ shift pattern in $T$ matches the queer content shift, doubled.

**Attack.** Prove that $\Psi$ is the HC map, and derive filtration preservation from the PBW filtration on $Z(U(\mathfrak{q}_N))$.

References: Kashuba-Molev 2512.21631, Das-Pattanayak 2608.17431 (Aug 18 2026), Ivanov's factorial Schur Q.

### Route D — Lee 2606 shifted t-Schur Pieri

Lee 2606.22058 explicitly flags the Pieri rule for $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$ as open. Rick's Main Conjecture is a filtration statement about this Pieri rule.

**Attack.** Match Rick's $s^*_\mu$ specialization to Lee's $\mathcal{Q}_\mu$-basis coefficients. Use Lee's algebraic infrastructure (Pfaffian Giambelli, Cauchy identity, transition matrices) to prove the degree bound.

**Publication.** Regardless of route, presenting the Main Conjecture as the resolution of Lee's open Pieri problem is publishable in Lee's community. FPSAC 2027 abstract material.

## Priority ordering

1. **Route A (Lemma 2).** Most concrete. Directly tests the empirical structure Rick already understands.
2. **Route C (queer).** Most conceptual. If it works, gives Hopf-algebraic explanation.
3. **Route D (Lee).** Most publishable. Should be attempted in parallel via M-and-R1 note restructure.
4. **Route B (Cauchy).** Least clear right now. Reserve as backup.

## Historical lineage

- **Days 100-108:** original Layer-Shape Lemma phrasing via $\deg_j \alpha_{p,k}$ bound.
- **Days 109-115:** Master Argument (line-divisibility) reduces to $\deg_\pi A_p \le p$.
- **Day 116:** Lift Theorem reduces to StructB.
- **Days 117-121:** (C1) + (C2) prove StructB at $d = d_{\max}$.
- **Day 122:** (A,B) diagonalization + Weyl determinant form; general-$d$ frontier framed as $\deg_t S_j = j$ exactly.
- **Day 123:** E-basis reformulation. Main Conjecture states everything as one $(1,1,2)$-weight bound.

## Files

- `proofs/2026-08-21-day123-e-basis-reformulation.md` — full writeup.
- `connections/2026-08-21-day123-E-basis-reformulation.md` — crown jewel.
- `connections/2026-08-21-lee-2606-plethystic-bridge.md` — Path 1 crown jewel.
- `beta-prime/code/day123/e_basis_check.py`, `omega_reduction.py`, `individual_weight.py`, `cauchy_binet_decomp.py`, `leibniz_search.py`, `leading_coeff_study.py`.
