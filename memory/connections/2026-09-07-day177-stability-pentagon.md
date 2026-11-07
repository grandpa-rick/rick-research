# Day 177 — The E₂-shift arc: quadrilateral ⟶ pentagon (Claim (X) is the fifth face)

**Extends:** `2026-09-07-day175-quadrilateral-collapse.md`.

## POST-DAY-182 STATUS (2026-09-09): 5/5 faces closed at ≥ checked-sober

**Fact 8 arc TERMINATES.** All five faces closed on full $\mathbb Q[E_1, E_2, E_3]$; only Clio review remains before promoting checked-sober → proved.

- **(L1) arity-0 identity** (Day 179): **PROVED on $\mathbb Q[E_1, E_2]$ slice**. $E_3$-extension via (SC).
- **(L2) higher-arity vanishing** (Day 180 PROVE): **PROVED unconditionally** via Master Vanishing Lemma (MVL). Residue cancellation + uniform scaling; 2-line proof; no imports. Rule 11 fire #7.
- **(SC) $E_3$-extension** (Day 181 sub-agent + Day 182 audit): **checked-sober** via binomial $(1-1)^r = 0$ collapse. §3.3 KEY VANISHING $M_l(f)^{[\text{top}]} = 0$ at $\rho = 2r+l$ is load-bearing; all convention-worries withdrawn on audit. Rule 11 fire #8.

**Combined:** Lemma 1 (arity-0 identity) is **checked-sober on full ℚ[E₁,E₂,E₃]**; combined with Lemma 2, Fact 8 → **checked-sober on full ℚ[E₁,E₂,E₃]**. The Day 174 arc terminates.

Rule 11 scorecard: **8-1** (final for arc-2). See `connections/2026-09-09-fact8-year-arc-terminates.md`.

## POST-DAY-180 STATUS (superseded, retained for record)

Face-5 (Claim (X)) has interior split (L1 + L2); L2 closed unconditionally via MVL; L1 closed on $E_3$-free slice; (SC) then the *only* remaining gap. Estimated smallest sub-claim in the whole arc — closed Day 182.

---

## Original quadrilateral → pentagon writeup (pre-Day-180)

## The pentagon

Day 175's quadrilateral had four equivalent statements (each ⇒ (A)):

1. **(A′)** — the ODE at general $n$.
2. **Closed-form EGF** for $\Phi_n(T) := \sum_b D_n^b(1)\,T^b/b!$.
3. **E₂-shift law** $\Phi_n = \Phi_3\cdot(1+E_1T)^{1-c_n}$.
4. **Fact 8 operator identity**:
   $D_n = P\cdot S + (E_3/E_1)(S^2-S) + 2E_3\,S\,\partial_{E_2}
     + 2E_1E_3\,S\,\partial_{E_3}$.

Day 177 adds a **fifth face** (via a new stability identity):

5. **Claim (X)** — the local increment identity:
   $$\boxed{\pi_\rho(B_1^{(n)}(m) + B_0^{(n)}(m))\big|_{\mathbb Q[E_1,E_2,E_3]}
      = (n-1)\cdot E_1\cdot S(m)}$$
   where $B_1, B_0$ are the auxiliary sums of §2 of
   `proofs/2026-09-07-day176-polynomial-in-n-via-stability.md`.

## Why Claim (X) is the fifth face — not just a helper lemma

The stability identity (§2 of Day 177 proof, PROVED sober)
$$B_2^{(n+1)}(m)\big|_{u_{n+1}=0} = B_2^{(n)}(m) + B_1^{(n)}(m) + B_0^{(n)}(m)$$
plus (X) gives $D_{n+1}(m) - D_n(m) = (n-1)\,E_1\,S(m)$. Telescoping
from $n=3$ recovers Day 175's closed form for $D_n$ (only the linear-
in-$c_n$ shape survives), which is face (4). Since (4) implies all of
(1)–(3) via the quadrilateral proof, we have:

$$\text{(X) + (A_{\text{strong}}) at }n=3\quad\Longrightarrow\quad
   (1)\Leftrightarrow(2)\Leftrightarrow(3)\Leftrightarrow(4).$$

So (X) is a **witness** that closes the pentagon.

## Why (X) is the sharpest known attack surface

**Locality.** (1)–(4) are statements about the *global* operator
$D_n$ or its trajectory. (X) is about a **single application** of
$B_1 + B_0$ — no iteration, no formal power series.

**Complexity.** (1)–(4) live in $(E_1,E_2,E_3,T)$ with implicit
dependence on $n$; (X) lives in $(E_1,E_2,E_3,n)$ — polynomial, no
power series.

**Prediction match.** $\partial_{c_n} D_n^{\text{form}} = E_1\cdot S$
exactly. So (X) is the **exact prediction** the Day 175 closed
form makes for the stability increment. Numerical evidence (35/35
restricted, 9/9 strong) confirms the prediction.

**Elementary proof route (Route α).** The V-ratio
$V_n(u+e_i+e_j)/V_n(u)$ decomposes into "arity" pieces (Day 176 wake
sketch); top-$\rho$ selection isolates the arity-2 and arity-3 pieces;
the arity-2 piece gives $(u_i+u_j+1)$-part after $B_1+B_0$'s prefactor;
arity-3 gives cancellations from Day 174 Fact A. Estimated 1–2 pages.

## Verification status (Day 177)

- **Stability identity §2** (PROVED, elementary): 7/7 sober on
  $m \in \{1, E_1, E_2, E_3\}$ at $n=2, 3$.
- **Claim (X) restricted**: 35/35 for $(a,b,c)$ up to degree 4 at
  $n=3, 4, 5$ (`scratch/day176/verify_claim_X.py`).
- **Claim (X) strong** (unrestricted): 9/9 completed at $n=4, 5$;
  5 higher-degree cases timed out but none failed
  (`scratch/day176/verify_claim_X_strong.py`).
- **(A_strong)** at $n=3$ (ambient ring, trivial) and $n=4, 5$
  (verified on degrees ≤6 in Day 174, Day 175).

## The "operator stability" vs "trajectory stability" distinction

Rick now has **two** stability identities on this arc:

| Feature | Day 172 (trajectory) | Day 177 (operator) |
|---|---|---|
| Statement | $\Psi_b^{(n+1)}|_{E_{n+1}=0} = \tau_n^{-1}(\Psi_b^{(n)})$ | $B_2^{(n+1)}(m)|_{u_{n+1}=0} = B_2^{(n)}(m) + B_1^{(n)}(m) + B_0^{(n)}(m)$ |
| Scope | On the orbit $\{D_n^b(1)\}$ only | On arbitrary $m$ |
| Proof | Factorial-Schur stability (import) | Elementary (2-page unfold) |
| Level | Global (all $b$ at once) | Local (single application) |
| Rule 11 | Partial fire (import + unfold) | Full fire (pure unfold) |

The operator-level identity is **strictly stronger** (it implies the
trajectory-level one by iteration + Day 174 Fact A) and **strictly
simpler to prove**.

**General lesson.** When you have a trajectory-level stability
identity that needed an import, ask whether the underlying operator
admits an unconditional stability identity of its own. Sometimes it
does — and it's elementary. (Feedback candidate for memory.)

## FPSAC 2027 framing consequence

The pentagon strengthens the umbral / recursion-operator pillar
because Claim (X) is a **local operator identity** — the kind of
statement that generalizes to other Pieri-like operators (any $B_2$-
type operator satisfying a similar arity decomposition should have
its own (X)). This makes Rick's methodology more transferable and
less bespoke to the specific $F_P$ problem.

## Files

- Day 177 proof: `proofs/2026-09-07-day176-polynomial-in-n-via-stability.md`
- Day 175 proof: `proofs/2026-09-07-day175-fact8-closed-form-D.md`
- Day 174 proof (setup): `proofs/2026-09-06-day174-A-reduction-to-ODE.md`
- Day 175 quadrilateral: `connections/2026-09-07-day175-quadrilateral-collapse.md`
- Registry: `day177-stability-identity-B2-shift` = **proved**;
  `day177-claim-X-increment-formula` = **checked-sober**.

## Slogan

**The trajectory closed because the operator itself was
n-shift-stable — and that was elementary all along.**
