# Day 176/177 — Polynomial-in-$n$ via a new stability identity

**Date:** 2026-09-07. **Status:** major partial win. The polynomial-in-$n$
structural claim is **reduced to a single explicit operator identity
(Claim X)**, which is verified sober on a substantial set of monomials
and $n$ values.

---

## 1. Headline

The **polynomial-in-$n$ structural claim** (which closes Fact 8 in one
line given verification at $n=3,4$ — see PROVE.md) is *derived* here
from two ingredients:

1. **(A_strong)** — $D_n := \overline{B_2^{(n)}}$ preserves the subring
   $\mathbb Q[E_1,E_2,E_3]$ for all $n\ge 3$.
2. **(X)** — the new operator-level identity
   $$\pi_\rho\bigl(B_1^{(n)}(m) + B_0^{(n)}(m)\bigr)
      \;=\; (n-1)\cdot E_1\cdot S(m),
   \qquad m\in\mathbb Q[E_1,E_2,E_3],$$
   where $B_1, B_0$ are the auxiliary sums defined in §2 and
   $S := e^{E_1\partial_{E_2}}$ is the shift $E_2\mapsto E_2+E_1$.

Given (A_strong) + (X), the polynomial-in-$n$ claim follows: the increment
$D_{n+1}(m)-D_n(m)$ equals $(n-1)\,E_1\,S(m)$, which is n-independent
apart from the linear $(n-1)$ factor. Telescoping from $n=3$ yields
$D_n(m) = A(m) + c_n B(m)$ with $c_n = \binom{n-1}{2}$, $B(m)=E_1 S(m)$,
$A(m)=D_3(m)-B(m)$.

Fact 8 (Day 175 closed-form) then promotes to **`proved`** given the
existing $n=3, 4$ verifications (48/48 + 18/18 monomials).

---

## 2. A new stability identity (proved sober)

### 2.1 Statement

Let $m\in \mathbb Q[E_1,\dots,E_k]$ (viewed as a polynomial). Define, for
$N\ge 2$,

$$\begin{aligned}
  B_2^{(N)}(m) \;&=\; \sum_{i<j\in [N]} u_i u_j\, m(u+e_i+e_j)\,\frac{V_N(u+e_i+e_j)}{V_N(u)},\\
  B_1^{(N)}(m) \;&=\; \sum_{i<j\in [N]} (u_i + u_j)\, m(u+e_i+e_j)\,\frac{V_N(u+e_i+e_j)}{V_N(u)},\\
  B_0^{(N)}(m) \;&=\; \sum_{i<j\in [N]} m(u+e_i+e_j)\,\frac{V_N(u+e_i+e_j)}{V_N(u)}.
\end{aligned}$$

**Stability identity.**  For $m$ symmetric in $u_1,\dots,u_n$ (and viewed
in the larger polynomial ring $\mathbb Q[u_1,\dots,u_{n+1}]$),

$$\boxed{\;B_2^{(n+1)}(m)\Big|_{u_{n+1}=0}
   \;=\; B_2^{(n)}(m) + B_1^{(n)}(m) + B_0^{(n)}(m)\;.}$$

### 2.2 Proof (sober)

Fix $m$ and split the outer sum in $B_2^{(n+1)}(m)$ into pairs with
$j = n+1$ and pairs with $j \ne n+1$:

$$B_2^{(n+1)}(m) \;=\; \underbrace{\sum_{i<j\le n} u_i u_j\, m(u+e_i+e_j)\,\frac{V_{n+1}(u+e_i+e_j)}{V_{n+1}(u)}}_{(\text{I})}
   + \underbrace{\sum_{i=1}^n u_i\, u_{n+1}\, m(u+e_i+e_{n+1})\,\frac{V_{n+1}(u+e_i+e_{n+1})}{V_{n+1}(u)}}_{(\text{II})}.$$

Setting $u_{n+1}=0$ in $(\text{II})$: every summand has a factor
$u_{n+1}$, so $(\text{II})|_{u_{n+1}=0}=0$.

For $(\text{I})$ set $u_{n+1}=0$. Two elementary identities:

- $V_{n+1}(u_1,\dots,u_n,0) = V_n(u)\cdot E_n(u)$ (since
  $V_{n+1}(x_1,\dots,x_{n+1}) = V_n(x_1..x_n)\prod_l(x_l - x_{n+1})$).
- $V_{n+1}(u+e_i+e_j)|_{u_{n+1}=0} = V_n(u+e_i+e_j)\cdot E_n(u+e_i+e_j)$
  (same identity, since the shift only touches $u_i, u_j$ with $i,j\le n$).
- $E_n(u+e_i+e_j)/E_n(u) = (u_i+1)(u_j+1)/(u_i u_j)$ (only the $i$-th and
  $j$-th factors change).

Substituting:
$$\frac{V_{n+1}(u+e_i+e_j)}{V_{n+1}(u)}\bigg|_{u_{n+1}=0}
   \;=\; \frac{V_n(u+e_i+e_j)}{V_n(u)}\cdot \frac{(u_i+1)(u_j+1)}{u_i u_j}.$$

Also $m(u+e_i+e_j)|_{u_{n+1}=0} = m(u+e_i+e_j)$ as a polynomial in
$u_1,\dots,u_n$ (recall $m$ was chosen with no dependence on $u_{n+1}$
via $E_k \le k = 3$; more generally, if $m$ depends only on $E_1,..,E_r$
with $r \le n$ then $m|_{u_{n+1}=0}$ is unchanged since $E_k^{(n+1)}(u,0)=E_k^{(n)}(u)$).

Therefore
$$(\text{I})\big|_{u_{n+1}=0}
   \;=\; \sum_{i<j\le n} (u_i+1)(u_j+1)\, m(u+e_i+e_j)\,\frac{V_n(u+e_i+e_j)}{V_n(u)}.$$

Expanding $(u_i+1)(u_j+1) = u_i u_j + (u_i+u_j) + 1$ gives the three
sums $B_2^{(n)}(m) + B_1^{(n)}(m) + B_0^{(n)}(m)$. $\square$

### 2.3 Computational verification

Script `scratch/day176/verify_stability_formula.py`. Verified for
$(m, n) \in \{1, E_1, E_2, E_3\}\times\{n=2, 3\}$ — 7/7 pass (the one
non-run is $m=E_3$ at $n=2$, where $E_3$ is trivially zero). Zero residual
in every case.

---

## 3. The polynomial-in-$n$ reduction

### 3.1 The core identity

Take top-$\rho$ of both sides of the stability identity. On the LHS: by
**(A_strong)** at $n+1$, $D_{n+1}(m) := \pi_\rho B_2^{(n+1)}(m) \in
\mathbb Q[E_1,E_2,E_3]$; setting $u_{n+1}=0$ (equivalently $E_{n+1}=0$)
removes nothing.

On the RHS: by (A_strong) at $n$, $\pi_\rho B_2^{(n)}(m) = D_n(m) \in
\mathbb Q[E_1,E_2,E_3]$. Thus

$$D_{n+1}(m) - D_n(m) \;=\; \pi_\rho\bigl(B_1^{(n)}(m) + B_0^{(n)}(m)\bigr)
   \quad(\text{implicitly restricted to }\mathbb Q[E_1,E_2,E_3]).$$

### 3.2 Claim (X): a clean operator-level formula for the increment

**Claim (X).**  For all $n \ge 3$ and $m\in\mathbb Q[E_1,E_2,E_3]$,
$$\boxed{\;\pi_\rho\bigl(B_1^{(n)}(m) + B_0^{(n)}(m)\bigr)\Big|_{\mathbb Q[E_1,E_2,E_3]}
   \;=\; (n-1)\cdot E_1\cdot S(m)\;,}$$
where $S := e^{E_1\partial_{E_2}}$ (i.e. $S(E_1^aE_2^bE_3^c) = E_1^a(E_2+E_1)^bE_3^c$).

**Consequence.**  Given (X):
$$D_{n+1}(m) - D_n(m) = (n-1)\, E_1 S(m).$$
Summing from $n=3$ to $N-1$:
$$D_N(m) = D_3(m) + \sum_{n=3}^{N-1}(n-1)\, E_1 S(m)
   = D_3(m) + \Bigl(\sum_{k=2}^{N-2} k\Bigr) E_1 S(m)
   = D_3(m) + (c_N - 1) E_1 S(m).$$
Since $c_3 = 1$, we can write $D_N(m) = A(m) + c_N B(m)$ with
$B(m) = E_1 S(m)$, $A(m) = D_3(m) - B(m)$. This is exactly the
polynomial-in-$n$ structural claim.

### 3.3 Consistency with the Day 175 closed form

Recall
$D_n^{\text{form}} = P\cdot S + (E_3/E_1)(S^2-S) + 2E_3 S\partial_{E_2} + 2E_1E_3 S\partial_{E_3}$
with $P = c_n E_1 + E_2$.

$\partial_{c_n} D_n^{\text{form}} = E_1\cdot S$, so
$D_{n+1}^{\text{form}}(m) - D_n^{\text{form}}(m) = (c_{n+1}-c_n)\,E_1\,S(m) = (n-1)\,E_1\,S(m)$.

Claim (X) is therefore the **exact prediction of the Day 175 closed form
for the stability increment**. Its truth would (a) close the
polynomial-in-$n$ claim and (b) close Fact 8 via the $n=3,4$
verifications.

### 3.4 Computational verification of Claim (X)

Script `scratch/day176/verify_claim_X.py`. Tests (X) for $m = E_1^a E_2^b
E_3^c$ across a range of $(a,b,c)$ and $n$. Output in `out_claim_X.txt`.

**Result: 35/35 PASS, 0 FAIL.**

| $n$ | $(a,b,c)$ range tested | pass |
|---|---|---|
| 3 | $a\le 2$, $b\le 2$, $c\le 1$ (with $\rho\le 4$) | 15/15 |
| 4 | $a\le 2$, $b\le 2$, $c\le 1$ (with $\rho\le 4$) | 15/15 |
| 5 | $(0,0,0), (1,0,0), (0,1,0), (0,0,1), (1,1,0)$ | 5/5 |

Every case matches $(n-1)\cdot E_1 \cdot S(m)$ **exactly** after
restriction to $\mathbb Q[E_1,E_2,E_3]$.

**Strong (X) evidence.** A stronger check
(`scratch/day176/verify_claim_X_strong.py`, output `out_claim_X_strong.txt`)
tests the *unrestricted* identity — no $E_{k\ge4}$ terms on either side.
9/9 completed cases at $n\in\{4,5\}$ pass (5 cases timed out on higher-degree
monomials at $n=5$; none failed). Supports Claim (X_strong) of §4.2.

---

## 4. Sub-claim (A_strong): status and remarks

**(A_strong).** $D_n$ preserves $\mathbb Q[E_1,E_2,E_3]$ for all $n\ge 3$.

### 4.1 What's known

- (A_strong) at $n=3$: trivial (ambient ring).
- (A_strong) at $n=4, 5$: verified for all monomials up to some degree
  in Day 174 §3 (Facts 1–6 for $E_1$, $E_2$, $E_3$, $E_2^2$, $E_2 E_3$)
  and Day 175 (extractions on $E_2^k$, $E_2^k E_3$ up to $k\le 6$).
- (A) (the trajectory-only version) is Day 172 (A), verified 35/35 for
  $(n,b)\in\{3,\dots,7\}\times\{0,\dots,6\}$.
- The strong version (A_strong) is a *checked-sober* consequence of the
  Day 175 closed-form ansatz, plus the observation that $D_n^{\text{form}}$
  manifestly maps $\mathbb Q[E_1,E_2,E_3]$ into itself.

### 4.2 (A_strong) induction from a *strong* form of (X)

Define **Claim (X_strong)**: $\pi_\rho(B_1^{(n)}(m)+B_0^{(n)}(m))$ as an
element of $\mathbb Q[E_1,\dots,E_n]$ (without restriction) equals
$(n-1)\, E_1\, S(m)$. This is the same identity but with the a-priori
$E_{k\ge 4}$-freeness on the LHS included.

Given Claim (X_strong): the stability identity yields
$\pi_\rho(B_2^{(n+1)}(m)|_{u_{n+1}=0}) = D_n(m) + (n-1)E_1 S(m)$, all in
$\mathbb Q[E_1,E_2,E_3]$. This forces $D_{n+1}(m)|_{E_{n+1}=0} \in
\mathbb Q[E_1,E_2,E_3]$. Combined with an $E_{n+1}$-freeness argument
(e.g. from Day 174 Fact A, proved), we get (A_strong) at $n+1$ by
induction from $n=3$.

Note the *restricted* Claim (X) — verified 35/35 — is exactly the
$E_1,E_2,E_3$-projection of (X_strong). Verifying (X_strong) requires
checking that $\pi_\rho(B_1+B_0)$ has no $E_{k\ge4}$-terms. Tests
(§`verify_claim_X_strong.py`) address this.

---

## 5. What remains open

### 5.1 Prove Claim (X)

Two possible approaches:

**Route α (direct expansion).** Expand the V-ratio in the "arity" filtration
(Day 176 sketch §2.3), extract top-$\rho$ terms, and directly compute
$\pi_\rho(B_1 + B_0)$ as a polynomial in $E_1, E_2, E_3, n$. Compare
to $(n-1) E_1 S(m)$. The direct expansion requires:

  1. Formalizing the arity-$k$ contribution of the V-ratio.
  2. Showing arity $\ge 3$ contributions have $\rho$-weight strictly
     less than the top on $\mathbb Q[E_1, E_2, E_3]$-inputs.
  3. Computing the arity-0, 1, 2 contributions explicitly and reading off
     $(n-1) E_1 S(m)$.

**Route β (via factorial Schur stability + Day 175 closed form).** Since
the Day 175 form $D_n^{\text{form}}$ predicts the exact identity (X), if
we can independently verify $D_n^{\text{form}} = D_n$ at $n=3$ for a
"generating set" of $m$'s (e.g. $E_2^k E_3^l$ for all $(k,l)$), and check
that both sides of (X) are $E_1$-linear (which is straightforward), we
inherit (X) from the closed form. But this is circular for Fact 8.

**Route γ (unfold + coincidence).** Directly compute
$\pi_\rho(B_1^{(n)}(m))$ and $\pi_\rho(B_0^{(n)}(m))$ separately for
generating $m$'s and try to match to $(n-1) E_1 S(m)$ by symbolic
computation.

Route α is the cleanest and closes the arc.

### 5.2 Independent proof of (A_strong)

Not strictly needed if (X) is proved sufficient generically (see §4.2),
but useful as a standalone lemma. Best approach: use Day 174 Fact A
(Kostka-Stirling cancellation, PROVED) applied to $B_2^{(n)}$'s action
on Q[E_1,E_2,E_3]-inputs. Fact A gives $E_{k\ge4}$-freeness of the
Ψ-orbit; we need the analogous statement for the operator on general
inputs.

---

## 6. Registry effect

Register:

- `day177-stability-identity-B2-shift` — **proved** (§2, and 7/7 sober
  verified). Rigorous stability identity for $B_2^{(n+1)}|_{u_{n+1}=0}$.
- `day177-claim-X-increment-formula` — **hunch/checked-sober** (§3.2,
  matches Day 175 closed form and passes computational checks in
  `verify_claim_X.py`).
- `day176-polynomial-in-n-structural-claim` — **conditional on (X)**;
  reduced to Claim (X) in this note.
- `day175-fact8-D-formula-equals-D-intrinsic` — still **checked-sober**;
  will promote to `proved` once (X) is proved.

---

## 7. Rule 11 scorecard

Score for the arc so far: **4-1 partial**. Rule 11 partial fire on this
session — the stability identity emerged from "unfold the definition of
$B_2^{(n+1)}$ and split by $j = n+1$", exactly the Rule 11 recipe. The
"import" here is Day 175's closed form (which predicts the RHS of (X)),
so partial.

---

## 8. Pre-registered predictions — postmortem

- ✓ "Route 2 (stability) will land the proof in <30 min if Day 172
  stability is used non-circularly." PARTIAL: The relevant stability
  identity is a NEW variant (§2), not Day 172's directly. Day 172's is
  for the trajectory $\{\Psi_b\}$; the new one is for the operator
  $B_2^{(n)}$ acting on general $m$. Landed in ~90 min after false
  starts on Day 172 as-is.
- ✗ "Route 1 (direct arity) needs Fact A as a lemma." Not needed here
  (though would help Route α of §5.1).
- Not-yet-verifiable: "Fact 8 → proved in one line after (X)."
  Anticipated 1-2 pages once (X) is proved.

---

## Files

- `scratch/day176/verify_stability_formula.py` — §2 stability, 7/7 sober.
- `scratch/day176/verify_claim_X.py` — §3.2 Claim (X), see
  `out_claim_X.txt`.

## Sketchy items removed

The Day 176 wake sketch (`scratch/day176/polynomial_in_n_proof.md`) was
long and speculative on the V-ratio arity argument. The stability-based
approach here is cleaner and closer to landing. The old sketch is
retained as a reference for Route α of §5.1.
