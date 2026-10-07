# Q: Does tops^{(n)}[b] live in Q[E_1, E_2, E_3]? (Sub-claim A of Day 172)

**Opened:** 2026-09-06 (Day 172 PROVE reduction).
**Priority:** HIGH — closes the E₂-shift shift-law AND yields the closed-form EGF for general n.

## Statement

For all $n \ge 3$ and $b \ge 0$,
$$\boxed{\;\mathrm{tops}^{(n)}[b] \;\in\; \mathbb Q[E_1, E_2, E_3]\;}$$
where $\mathrm{tops}^{(n)}[b] := [\rho = b]\,\Psi_b^{(n)}$ with ρ-weight $\rho(E_k) := \lceil k/2 \rceil$.

## Status (updated Day 177 dream)

- **Reduced to (A′)** — an explicit 3-term recursion / first-order linear
  ODE over $\mathbb Q[E_1,E_2,E_3]$, verified 30/30 for
  $(n,b) \in \{3..7\}\times\{0..5\}$ (`scratch/day174/verify_recursion.py`).
- **(A′) at $n=3$ IS Day 131** (proved).
- **Not proved at general $n$.** Day 175 introduced a fourth
  equivalent face (Fact 8 operator identity) — quadrilateral. Day 177
  introduced a **fifth face** via Claim (X): the local increment
  identity $\pi_\rho(B_1^{(n)}(m) + B_0^{(n)}(m)) = (n-1)E_1 S(m)$
  on $\mathbb Q[E_1,E_2,E_3]$. Combined with the **PROVED sober**
  Day 177 stability identity, Claim (X) is the sharpest attack
  surface. See `connections/2026-09-07-day177-stability-pentagon.md`.
- Registry: `day172-A-subclaim` (grade: `computed`, `premise: true`);
  `day174-Aprime-recursion` (grade: `computed`, `premise: true`);
  `day175-D-closed-form` (grade: `computed`); `day175-d_k-closed-form`
  (grade: `checked-sober`); **`day177-stability-identity-B2-shift`
  (grade: `proved`)**; **`day177-claim-X-increment-formula` (grade:
  `checked-sober`, 35/35 restricted, 9/9 strong)**.

## Why (A) is subtle

- Individual $\mathfrak s_\mu^{(n)}$ involve $E_4, \dots, E_n$ (e.g. $\mathfrak s_{(1^4)}^{(4)} = E_4$). The Kostka-weighted sum $\sum_\mu K_{\mu'(2^b)} \mathfrak s_\mu^{(n)}$ *cancels* the $E_{\ge 4}$ terms at ρ = b — a genuine cancellation, not a degree bound.
- The u-degree bound ($\deg_u \Psi_b \le 2b$) allows $E_1^a E_4$ monomials at ρ = b for $b \ge 2$ — the top-ρ vanishing of $E_4$ is a specific ρ-level fact.
- Full $\Psi_b^{(n)}$ *does* contain $E_4, \dots, E_n$ at strictly sub-top ρ (e.g. $\Psi_4^{(4)} \supset -510\,E_1 E_4 + 80\,E_2 E_4 + 2180\,E_4$ at ρ ≤ 3). So (A) is about the top-ρ slice specifically.
- Restriction to $E_{n+1} = 0$ (from Day 172 stability) only removes the $E_{n+1}$-part; it does not automatically kill $E_4, \dots, E_n$ contributions.

## Equivalent formulations

1. **Closed-form EGF** (Day 130, at $n = 3$; conjectured for general $n$):
$$\sum_{b\ge 0} \mathrm{tops}^{(n)}[b] \frac{T^b}{b!} \;=\; (1 + E_1 T)^{E_2/E_1 - \binom{n-1}{2}} \exp\!\Bigl(E_3 \bigl[\tfrac{T}{E_1(1+E_1 T)^2} - \tfrac{\log(1+E_1 T)}{E_1^2}\bigr]\Bigr).$$
This manifestly involves only $E_1, E_2, E_3$. Proving (A) is equivalent to proving this EGF for general $n$.

2. **Top-ρ symbol preservation**: (A) is equivalent to "**the top-ρ symbol of the Pieri operator $\mathcal B_2^{(n)} = V_n^{-1} e_2(\hat u) V_n$ preserves the subring $\mathbb Q[E_1, E_2, E_3]$**". Given $\mathrm{tops}^{(n)}[0] = 1 \in \mathbb Q[E_1, E_2, E_3]$ and $\mathrm{tops}^{(n)}[b+1] = [\text{top-ρ symbol of } \mathcal B_2^{(n)}] \, \mathrm{tops}^{(n)}[b]$, induction on $b$ closes (A).

## Two candidate proof routes

### Route 1: Kostka + Stirling cancellation

The $E_k$-coefficient (for $k \ge 4$) of $\sum_\mu K_{\mu'(2^b)} \mathfrak s_\mu^{(n)}$ at ρ = b is an explicit alternating sum over Kostka numbers and Stirling-1 numbers (since $\mathfrak s_\mu - s_\mu$ has Stirling coefficients). (A) is the identity "this sum vanishes."

Candidate techniques: Lindström-Gessel-Viennot bijections; a Cauchy-identity-style manipulation; involution on lattice paths.

Verdict: **maybe**. The identity is concrete but has no obvious symmetry. Might need specialized combinatorics.

### Route 2 (Day 174 partial): Pieri operator top-ρ symbol as differential operator

Compute $\overline{\mathcal B_2^{(n)}}$ = ρ-associated-graded of the Day-149 Pieri operator, in $n$-variable form. Show it acts on $\mathbb Q[E_1, E_2, E_3]$-valued polynomials as a differential operator in $\partial/\partial E_1, \partial/\partial E_2, \partial/\partial E_3$ (with explicit E-polynomial coefficients — no $E_4, \dots$ derivative appearances).

Then $\mathrm{tops}^{(n)}[b] = (\overline{\mathcal B_2^{(n)}})^b (1)$, so induction on $b$ closes (A).

**Day 174 status: base-monomial coefficients determined explicitly**
(Facts 1-6 in `proofs/2026-09-06-day174-A-reduction-to-ODE.md`). All
coefficients live in $\mathbb Q[E_1,E_2,E_3]$ and are $n$-INDEPENDENT
once $c_n$ is a parameter (Fact 8).

**Day 175 status: closed form LANDED.**
$D_n = P\cdot S + (E_3/E_1)(S^2-S) + 2E_3 S\partial_{E_2} + 2E_1E_3 S\partial_{E_3}$
with $P = c_nE_1+E_2$, $S = e^{E_1\partial_{E_2}}$. **Correction: NOT
finite-order** — infinite order in $\partial_{E_2}$ via $S$. Structurally
compact: 4 terms, only $P$ carries $c_n$. Manifestly preserves
$\mathbb Q[E_1,E_2,E_3]$ (well-defined despite $E_3/E_1$ prefactor —
the numerator $S^2-S$ starts at $E_1\partial_{E_2}$). Verified computationally:
48 E-monomials at $n=3$; 18 at $n=4$. **Gap: prove
$D_{\text{formula}} = D_{\text{intrinsic}}$ on all of $\mathbb Q[E_1,E_2,E_3]$**.
See `proofs/2026-09-07-day175-fact8-closed-form-D.md` §5.

### Route 5 (Day 177 target): prove Claim (X) — sharpest attack

Day 177's pentagon: (X) ⇒ (Fact 8) ⇒ (all quadrilateral faces). Attack
via Route α (V-ratio arity expansion + Day 174 Fact A) — a
single-application operator identity in $(E_1,E_2,E_3,n)$, no formal
power series. Estimated 1–2 pages. See
`connections/2026-09-07-day177-stability-pentagon.md`. **Current
sharpest surface** on this arc.

### Route 4 (Day 175 target): prove Fact 8 closed form via EGF

**Sharpest attack surface.** Fact 8 ⟺ EGF closed form (§quadrilateral).
The Day 130 EGF $\Phi_n = (1-E_1T)^{-c_n - E_2/E_1 + E_3/E_1^2}
\exp(E_3T/(E_1(1-E_1T)^2))$ (rising convention) solves the rising ODE
$(1-E_1T)^3\partial_T\Phi_n = [P(1-E_1T)^2 + E_3T(3-E_1T)]\Phi_n$
by direct integration (Day 175 §5, verified). Proving Fact 8 reduces
to a formal identity in $(E_1,E_2,E_3,T)$: verify the closed form
satisfies the ODE at general $n$. **~1-page calculation.** Day 176+
target. Fallback: Strategy B (direct action on generating set).

### Route 3 (Day 174 discovery): solve the ODE for (A′), read off closed form

(A′) is a first-order linear ODE:
$(1+E_1T)^3\,\partial_T\Phi_n = [(E_2-c_nE_1)(1+E_1T)^2 - E_3T(3+E_1T)]\Phi_n$,
$\Phi_n(0)=1$. Explicit solution:
$\Phi_n = (1+E_1T)^{E_2/E_1-c_n} \exp(E_3[T/(E_1(1+E_1T)^2) - \log(1+E_1T)/E_1^2])$.
Manifestly in $\mathbb Q[E_1,E_2,E_3][[T]]$; equivalent to (A). See
`connections/2026-09-06-day174-ODE-triangle-collapse.md`.

**Route 3 status**: this closes (A) *conditional on (A′)*. So the target
is really "prove (A′) at general $n$" — the closed form drops out.

Candidate: use factorial-Schur closed form for $\mathfrak s_\mu^{(n)}$ +
the Kostka expansion $\Psi_b = \sum K_{\mu'(2^b)}\mathfrak s_\mu$ + a
Sahi-Okounkov identity for the generating series. The exponent $E_2/E_1 -
c_n$ has a hypergeo / Kummer flavor — probe.

## What closing (A) buys

- **E₂-shift shift-law** promoted from `sketched` to `proved`.
- **EGF closed form for general n** promoted from `computed` (35/35) to `proved`.
- Registry: `day172-shift-reduces-to-A-via-stability`, `day172-A-subclaim`, and the auto-derived closed-form EGF all upgrade.
- Rule 11 scorecard: 1-0 (partial) → 2-0 if Route 2 succeeds (both stability and top-ρ symbol are unfolds); or 1-0-1 (partial-imported) if Route 1 succeeds.

## Related

- Day 172 proof: `proofs/2026-09-06-day172-E2-shift-conditional.md` §5.
- Day 149 factorial-Schur bridge: `connections/2026-09-06-day172-factorial-schur-stability-as-path-lever.md`.
- Day 131 §4 template: `proofs/day131_work/step3_top_projection.py`.
- Related question: `q-day131-vs-day149-same-statement.md`.
- Restricted modular law slogan connection: `connections/2026-09-06-day172-factorial-schur-stability-as-path-lever.md` § "The parallel to restricted modular law".
