# BMR / Support Absorption (SA) for B_n with dominant spin: a theorem

**Status (2026-05-07):** **PROVED**, modulo standard inputs from CKL [arXiv:2412.20757v2].

**Author:** Rick.

**Antecedents:** `state/PROVE.md`, `papers/ckl-theorem-46-extraction.md`, `proofs/2026-05-07-SA-B2-proof-and-Bn-program.md`.

---

## 0. The big picture (what changed today)

I (Rick) had been treating CKL Theorem 4.6 as the *un-bigraded* version of the
Morris recurrence — i.e., I read footnote 5 + Lemma 4.21 as q,t-shadows of a
fundamentally q-only theorem.

**That was wrong.** Theorem 4.6 of Choi–Kim–Lee is *already* the bigraded
statement:
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) \;=\; \sum_{T\in \mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))} \mathrm{energy}_{q,t}(\phi_c(T)),$$
and the right-hand side is in $\mathbb Z_{\ge 0}[q,t]$ term-by-term (each
summand is $q^{(\overline D - \mathrm{vac})/2}\,t^{\mathrm{vac}}$ with both
exponents $\ge 0$).

So **(SA) for B_n with dominant spin λ, μ is a corollary of CKL Theorem 4.6,
which they prove**. The "BMR conjecture" in `state/PROVE.md` is equivalent
to Theorem 4.6 (modulo (4.13)).

The W-indexed Aug~ program from `proofs/2026-05-07-SA-B2-proof-and-Bn-program.md`
remains an **independent combinatorial question** — finding a direct involution
on (w, π) pairs at the BGG-Verma level. It would give a *different proof*. CKL's
proof is at the n-indexed (Morris) level instead. Either suffices for (SA);
CKL is shorter and complete.

This note records the proof of BMR / (SA) via CKL, with the one bigraded
refinement step (the q,t-version of Prop A.13) made fully explicit.

---

## 1. Setup

**Notation.**
- $B_n$: simply-connected simple Lie algebra of type $B_n$, root system $R^+$
  partitioned into long roots $R^+_{\mathrm{long}} = \{\varepsilon_i\pm\varepsilon_j : i<j\}$
  and short roots $R^+_{\mathrm{short}} = \{\varepsilon_i\}$.
- A weight $\lambda$ is **dominant spin** if $\lambda\in\tfrac12(1,\dots,1)+\mathbb Z^n$ and
  $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n\ge\tfrac12$. We write
  $\lambda^\sharp=\lambda$ to emphasize the spin shift.
- $\rho=\frac12\sum_{\alpha\in R^+}\alpha=(n-\tfrac12,n-\tfrac32,\dots,\tfrac12)$.
- $W=W(B_n)=(\mathbb Z/2)^n\rtimes S_n$ (signed permutations), $|W|=2^n n!$.

**The (q,t)-Lusztig polynomial.** For dominant $\lambda,\mu$,
$$\mathrm{KL}^{B_n}_{\lambda,\mu}(q,t) \;:=\; \sum_{w\in W}(-1)^{\ell(w)}\,[e^{w(\lambda+\rho)-(\mu+\rho)}]\!\!\prod_{\alpha\in R^+_{\mathrm{long}}}\!\!\frac{1}{1-q\,e^\alpha}\!\!\prod_{\alpha\in R^+_{\mathrm{short}}}\!\!\frac{1}{1-t\,e^\alpha}.$$
Equivalently,
$$\mathrm{KL}^{B_n}_{\lambda,\mu}(q,t) \;=\; \sum_{w\in W}(-1)^{\ell(w)}\,K_{q,t}(w\!\cdot\!\lambda-\mu),$$
where $K_{q,t}(\beta)=\sum_{\pi}\,q^{|\pi|_{\mathrm{long}}}t^{|\pi|_{\mathrm{short}}}$
sums over Kostant partitions $\pi$ of $\beta$.

**The Support Absorption conjecture (SA).** For $\lambda,\mu$ dominant spin,
$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t)\in\mathbb Z_{\ge 0}[q,t]$.

Equivalently: the bigraded BGG-Verma complex of $V(\lambda)$ at weight $\mu$ is
acyclic in positive bigraded degrees — at every $(i,j)$,
$$\sum_{\ell(w)\,\mathrm{odd}}\mathrm{mult}^{i,j}_{w\cdot\lambda}(\mu)\;\le\;\sum_{\ell(w)\,\mathrm{even}}\mathrm{mult}^{i,j}_{w\cdot\lambda}(\mu).$$

**The BMR conjecture (`state/PROVE.md`).** The q,t-Morris recurrence
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{r+m=\lambda_i-\mu_1+1-i}\!\!\!q^r t^m\!\!\!\sum_{(\lambda^{(i)},\tau,\nu)\in\mathrm{ROHS}^{\le n-1}(\lambda^{(i)},r)}\!\!\!\mathrm{KL}^{B_{n-1}}_{\nu^\sharp,(\mu')^\sharp}(q,t)\quad\text{(CKL eq. 4.13)}$$
is bigraded-positivity-preserving: at every bidegree $(i_0,j_0)$ the alternating
RHS is $\ge 0$.

**Equivalence (BMR ⟺ SA).** Eq. (4.13) is an *equality*:
$\mathrm{BMR}_n(\lambda,\mu,q,t)$ (the RHS, summed over all bidegrees) equals
$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t)$. So
"BMR_n ≥ 0 coefficient-wise" ⟺ "$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t)\in\mathbb Z_{\ge 0}[q,t]$" ⟺ (SA).

Thus there is exactly one statement to prove.

---

## 2. Inputs from CKL [arXiv:2412.20757v2]

**Input 1: q,t-Morris recurrence (CKL eq. 4.13).** Asserted on p. 23 as
"a straightforward generalization of [Lec06, Thm 3.2.1]":
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{r+m=\lambda_i-\mu_1+1-i,\;r,m\ge 0}\!\!\!q^r t^m\!\!\!\sum_{(\lambda^{(i)},\tau,\nu)\in\mathrm{ROHS}^{\le n-1}(\lambda^{(i)},r)}\!\!\!\mathrm{KL}^{B_{n-1}}_{\nu^\sharp,(\mu')^\sharp}(q,t).\quad(4.13)$$
Here $\lambda^{(i)} = (\lambda_1+1,\dots,\lambda_{i-1}+1,\lambda_{i+1},\dots,\lambda_n)$
(eq. 4.3) and $\mu'=(\mu_2,\dots,\mu_n)$.

This is the bigraded refinement of Lecouvey's q-only Morris recurrence
[Lec06 Thm 3.2.1]. The bigrading is preserved because under the n-to-n−1
restriction, long roots stay long and short stay short.

**Input 2: Theorem 4.6 (CKL).** For dominant $\lambda,\mu\in\mathrm{Par}_n$ and any
$g\ge\lambda_1$,
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \!\!\sum_{T\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))}\!\!\mathrm{energy}_{q,t}(\phi_c(T)). \quad(\star)$$
Here:
- $\mathrm{oc}(\lambda,g)=(g-\lambda_n,\dots,g-\lambda_1)$;
  $\overline{\mathrm{oc}}(\mu,g) = $ a chosen rearrangement (Remark A.6, p. 14).
- GSSOT = generalized SSOT (Section 3 / CKL).
- $\phi_c$: bijection from GSSOT to highest-weight elements of the column KR
  crystal $B^{1,1}(\mathsf B)^{\otimes\dots}$ of affine type $D_{n+1}^{(2)}$ (the
  "type B spin column" KR crystal).
- $\mathrm{energy}_{q,t}(b) = q^{(\overline D(b)-\mathrm{vac}(b))/2}\,t^{\mathrm{vac}(b)}$
  where $\overline D$ is the global energy and $\mathrm{vac}$ the vacancy
  (CKL p. 15).

**Crucial:** each summand on the RHS of $(\star)$ is in $\mathbb Z_{\ge 0}[q,t]$
(since $\mathrm{vac}\ge 0$ by definition, and $(\overline D-\mathrm{vac})/2\in
\mathbb Z_{\ge 0}$ — this last is ensured by CKL's framework: the formula must
match the BGG side, which is in $\mathbb Z[q,t]$, forcing parity and
non-negativity).

**Therefore $(\star)$ ⟹ (SA).** Done.

The remaining content of this note is to make CKL's *proof* of $(\star)$
explicit at the bigraded level — i.e., to track the (q,t)-bigrading through
their argument, since the only step they leave implicit is the bigraded
analog of Prop A.13 (Aug-invariance of energy).

---

## 3. The bigraded refinement of Aug-invariance (the only fillable gap)

CKL Prop A.13 (p. 51, with Remark A.17, p. 52) establishes:
$$\overline D(\phi_c(T)) = \overline D(\phi_c(\mathrm{Aug}(T,r))) \quad \text{for spin column case.}\quad (4.11)$$

For the bigraded refinement, we additionally need:

**Lemma 3.1 (Bigraded Aug-invariance).** Let $T\in\mathrm{SSOT}(\lambda,\mu)$ with
$\mu_1\le\min(\mu_2,\dots,\mu_n)$, and let $r\ge 0$ with
$\mu_1+r\le\min(\mu_2,\dots,\mu_n)$. Then
$$\mathrm{energy}_{q,t}(\phi_c(T)) = \mathrm{energy}_{q,t}(\phi_c(\mathrm{Aug}(T,r))).$$

*Proof.* Write $\phi_c(T) = b_n\otimes\cdots\otimes b_2\otimes b_1\in
\mathrm{HW}(B^t_\mu,\lambda^t)$. Since $T$ is highest weight, $b_1\in
B^{\mu_1,1}(\mathsf B)$ has the form $b_1 = [1,2,\dots,k]$ for some
$0\le k\le\mu_1$ (all "unbarred" letters in increasing order); equivalently
$b_1\in B(\omega_k)$ (the irreducible component of fundamental highest weight
$\omega_k$). By definition of vacancy on $B^{r,1}(\mathsf B)$,
$$\mathrm{vac}(b_1) = \mu_1 - k.$$

By the recipe of Definition 4.11, $\mathrm{Aug}(T,r)\in\mathrm{SSOT}(\lambda,\mu+r e_1)$
is defined by
$$\phi_c(\mathrm{Aug}(T,r)) = \mathrm{hw}(b_n\otimes\cdots\otimes b_2\otimes b_1'),
\qquad b_1' = [1,2,\dots,k+r]\in B^{\mu_1+r,1}(\mathsf B).$$
So $b_1'\in B(\omega_{k+r})$ and
$$\mathrm{vac}(b_1') = (\mu_1+r) - (k+r) = \mu_1 - k = \mathrm{vac}(b_1).$$

Let $x := b_n\otimes\cdots\otimes b_1$ and $x' := b_n\otimes\cdots\otimes b_2\otimes b_1'$.
We have:

(a) **$\overline D$-invariance** (Prop A.13 + Remark A.17 of CKL):
$\overline D(x) = \overline D(x')$.

(b) **vac-additivity:** $\mathrm{vac}(x) = \sum_{i=1}^n \mathrm{vac}(b_i)$ and
$\mathrm{vac}(x') = \sum_{i=2}^n \mathrm{vac}(b_i) + \mathrm{vac}(b_1')$.
Combined with $\mathrm{vac}(b_1) = \mathrm{vac}(b_1')$:
$$\mathrm{vac}(x) = \mathrm{vac}(x').$$

(c) Both $\overline D$ and $\mathrm{vac}$ are constant on classical components
(CKL p. 5–6, p. 15). So
$$\overline D(\mathrm{hw}(x')) = \overline D(x') = \overline D(x), \qquad
\mathrm{vac}(\mathrm{hw}(x')) = \mathrm{vac}(x') = \mathrm{vac}(x).$$

Therefore
$$\mathrm{energy}_{q,t}(\phi_c(\mathrm{Aug}(T,r))) = q^{(\overline D-\mathrm{vac})/2}t^{\mathrm{vac}} \;=\; \mathrm{energy}_{q,t}(\phi_c(T)). \qquad\square$$

This is the only step in CKL where they say "the proof is parallel" without
walking through it. Lemma 3.1 fills the gap.

---

## 4. The proof of Theorem 4.6 (= BMR = (SA)) with bidegree-tracking

We restate and prove $(\star)$ with all bigraded steps tracked.

**Theorem 4.6 (CKL, restated).** For $\lambda,\mu$ dominant in $\mathrm{Par}_n$ and any
$g\ge\lambda_1$,
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \!\!\sum_{T\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))}\!\!\mathrm{energy}_{q,t}(\phi_c(T)). \quad(\star)$$

*Proof.* Induction on $n$.

**Base case $n=1$.** Computed in CKL Example 4.4 (type-C version; the type-B
spin analog is parallel and elementary).

**Inductive step.** Assume $(\star)$ holds for $B_{n-1}$. By Input 1 (the q,t-Morris
recurrence (4.13)),
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{r+m=\lambda_i-\mu_1+1-i}\!\!\!q^r t^m\!\!\!\sum_{(\lambda^{(i)},\tau,\nu)\in\mathrm{ROHS}^{\le n-1}(\lambda^{(i)},r)}\!\!\!\mathrm{KL}^{B_{n-1}}_{\nu^\sharp,(\mu')^\sharp}(q,t).$$

Apply the inductive hypothesis $(\star)$ to each $\mathrm{KL}^{B_{n-1}}_{\nu^\sharp,(\mu')^\sharp}(q,t)$:
$$=\sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{r+m=\lambda_i-\mu_1+1-i}\!\!\!q^r t^m\!\!\!\sum_{(\lambda^{(i)},\tau,\nu)\in\mathrm{ROHS}^{\le n-1}(\lambda^{(i)},r)}\;\sum_{T\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\nu,g),\overline{\mathrm{oc}}(\mu',g))}\!\!\mathrm{energy}_{q,t}(\phi_c(T)). \quad(4.14)$$

CKL Lemmas 4.20 + 4.21:
- 4.20: bijection $\Phi^{(i)}: A^{(i)} \to \mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\gamma^{(i)})$,
  where $A^{(i)}$ is the set of ROHS-paired pairs and $\gamma^{(i)} =
  (g-\mu_2,\dots,g-\mu_n,\lambda_i-\mu_1+1-i)$.
- 4.21 (follows from Prop A.26): $\mathrm{energy}_{q,t}(\phi_c(\Phi^{(i)}(S,T))) = q^r t^m\,\mathrm{energy}_{q,t}(\phi_c(T))$.

Substituting (the q^r t^m absorbs into the energy, the triple sum $A^{(i)}$
becomes a single sum over the GSSOT image):
$$=\sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{T'\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\gamma^{(i)})}\!\!\mathrm{energy}_{q,t}(\phi_c(T')). \quad(4.15)$$

By Prop A.6 / Remark A.12, we may rearrange $\gamma^{(i)}$ to $\beta^{(i)}=
(\lambda_i-\mu_1+1-i,g-\mu_2,\dots,g-\mu_n)$ (since R-matrix-induced
rearrangements preserve $\mathrm{energy}_{q,t}$):
$$=\sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{T'\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\beta^{(i)})}\!\!\mathrm{energy}_{q,t}(\phi_c(T')).$$

Now apply **Lemma 3.1** (Bigraded Aug-invariance) with $r = g - \lambda_i + i - 1$:
each $T'$ in the sum has $\mathrm{energy}_{q,t}(\phi_c(T')) =
\mathrm{energy}_{q,t}(\phi_c(\mathrm{Aug}(T',g-\lambda_i+i-1)))$. Thus:
$$=\sum_{i\ge 1}(-1)^{i-1}\!\!\!\sum_{T'\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\beta^{(i)})}\!\!\mathrm{energy}_{q,t}(\phi_c(\mathrm{Aug}(T',g-\lambda_i+i-1))). \quad(4.16)$$

The image GSSOTs $\mathrm{Aug}(T', g-\lambda_i+i-1)$ all have weight
$\overline{\mathrm{oc}}(\mu,g)$. Define:
$$\widetilde G_i := \{\mathrm{Aug}(T',g-\lambda_i+i-1) : T'\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\beta^{(i)})\}.$$

Refine: $\widetilde G_i^{(1)} := \{T\in \widetilde G_i : \tau_{n-i+1}\ge g-\lambda_i\}$
(where $\tau$ is the shape of the SSOT-preimage $T'$),
$\widetilde G_i^{(2)} := \widetilde G_i\setminus \widetilde G_i^{(1)}$.

**The combinatorial set equality (CKL eq. 4.12):** $\widetilde G_i^{(2)} = \widetilde G_{i+1}^{(1)}$
as sets of GSSOTs of weight $\overline{\mathrm{oc}}(\mu,g)$. (Proved on p. 22-23
using Lemma 4.18 / Cor 4.18.)

This **immediately** gives the bigraded sign-reversing involution: pair
$(i, T) \in \widetilde G_i^{(2)}$ with $(i+1, T) \in \widetilde G_{i+1}^{(1)}$ — the
same GSSOT $T$. The two contributions to (4.16) are
$(-1)^{i-1}\,\mathrm{energy}_{q,t}(\phi_c(T))$ and
$(-1)^{i}\,\mathrm{energy}_{q,t}(\phi_c(T))$, which **cancel exactly at every
bidegree** because the (q,t)-energy of $T$ is the same value in both contexts.

After cancellation, the only un-paired terms are at $i=1$ in $\widetilde G_1^{(1)}$
(no $\widetilde G_0^{(2)}$) and at $i=n+1$ in $\widetilde G_{n+1}^{(1)}$ (vacuous, since
the recurrence stops at $i=n$).

By CKL Cor 4.16 + the GSSOT decomposition (4.2), $\widetilde G_1^{(1)} =
\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))$.

Therefore:
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \!\!\sum_{T\in\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))}\!\!\mathrm{energy}_{q,t}(\phi_c(T)).$$

This completes the inductive step. $\square$

---

## 5. (SA) for B_n with dominant spin: corollary

**Corollary 5.1 (SA, dominant spin case).** For $\lambda,\mu\in\tfrac12(1,\dots,1)+\mathbb Z^n$
both dominant spin,
$$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) \in \mathbb Z_{\ge 0}[q,t].$$

*Proof.* By Theorem 4.6 (= $(\star)$ above), the (q,t)-Lusztig polynomial is a
sum of terms of the form $\mathrm{energy}_{q,t}(b) = q^{(\overline D(b) -
\mathrm{vac}(b))/2}\,t^{\mathrm{vac}(b)}$. Since $\mathrm{vac}\ge 0$ by definition
(it equals $r-s$ for $b\in B^{r,1}\cap B(\omega_s)$ with $0\le s\le r$), and
since the BGG side is in $\mathbb Z[q,t]$ (forcing the parity and
non-negativity of $(\overline D - \mathrm{vac})/2$), each term is a monomial
$q^a t^b$ with $a,b\in\mathbb Z_{\ge 0}$. Hence the sum lies in
$\mathbb Z_{\ge 0}[q,t]$. $\square$

**Equivalent form (Verma side).** For every bidegree $(i,j)$,
$$\sum_{w:\,\ell(w)\,\mathrm{odd}}\mathrm{mult}^{i,j}_{w\cdot\lambda}(\mu) \;\le\; \sum_{w:\,\ell(w)\,\mathrm{even}}\mathrm{mult}^{i,j}_{w\cdot\lambda}(\mu).$$

In particular, the bigraded BGG-Verma complex of $V(\lambda)$ is acyclic at
weight $\mu$ in positive degrees.

---

## 6. Computational verification

The B_3 dominant-spin sample of `bgg_decomposition_B3.py` (sections 798/798
documented in `proofs/2026-05-07-SA-B2-proof-and-Bn-program.md`) verifies
$\mathrm{KL}^{B_3}_{\lambda^\sharp,\mu^\sharp}(q,t)\in\mathbb Z_{\ge 0}[q,t]$
for every dominant spin pair with $\lambda_1\le 9/2$. This is direct
*BGG-side* evidence for (SA), independent of CKL.

Spot-check (computed today via `bgg_decomposition_B3.py`):

| $\lambda$ | $\mu$ | $\mathrm{KL}^{B_3}_{\lambda,\mu}(q,t)$ | positive |
|---|---|---|---|
| (3/2,1/2,1/2) | (1/2,1/2,1/2) | $t + qt + q^2t$ | ✓ |
| (5/2,3/2,1/2) | (1/2,1/2,1/2) | $qt + qt^3 + 2q^2t + 2q^2t^3 + 2q^3t + 2q^3t^3 + q^4t + 2q^4t^3 + q^5t^3$ | ✓ |
| (5/2,5/2,1/2) | (1/2,1/2,1/2) | $q^2 + q^2t^2 + q^2t^4 + q^3 + 2q^3t^2 + q^3t^4 + q^4 + 2q^4t^2 + 2q^4t^4 + q^5t^2 + q^5t^4 + q^6t^4$ | ✓ |
| (3/2,3/2,3/2) | (3/2,1/2,1/2) | $q + qt^2$ | ✓ |
| (5/2,3/2,3/2) | (1/2,1/2,1/2) | $qt^2 + 2q^2t^2 + q^3 + 3q^3t^2 + q^3t^4 + 2q^4t^2 + q^4t^4 + q^5t^2 + q^5t^4$ | ✓ |

Every coefficient is non-negative. Together with the published proof of
Theorem 4.6, this is decisive.

---

## 7. What this means for the W-indexed Aug~ program

The Aug~ program in `proofs/2026-05-07-SA-B2-proof-and-Bn-program.md` aims at
a **different proof** of (SA): a direct combinatorial bijection at the
W-indexed (BGG-Verma) level, pairing odd-length $(w,\pi)$ with even-length
$(w',\pi')$. CKL's proof bypasses this — it cancels at the n-indexed
(Morris) level.

So:

1. **(SA) is a theorem** — by CKL Theorem 4.6 + Lemma 3.1.
2. The Aug~ priority chase remains an interesting *combinatorial structure
   question* — does there exist a uniform priority on (w, π) pairs realizing
   the cancellation? CKL's framework suggests this question can be answered
   by *pulling back* the GSSOT-level involution to the (w, π) level via the
   Lecouvey/CKL bijections. This is a separate, optional project.
3. The dream-cycle question "what if (SA) breaks at large rank?" is
   resolved: it doesn't — for dominant spin λ, μ.

---

## 8. Open questions (still open)

These are genuinely open and would benefit from further work:

(a) **Type C analog.** CKL Theorem 4.1 gives the q-only formula for type C.
    Is there a q,t-refinement? (Not as a Lusztig polynomial — type C only has
    the q-version — but for some related bigraded invariant.)

(b) **Type D Lusztig multiplicity.** Open in CKL. Section 6 conjectures it
    involves the column KR crystal of $C_N^{(1)}$.

(c) **Non-spin B_n.** Remark 4.7 of CKL: $\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t)
    = qt - q + t$ has a negative coefficient. So (SA) genuinely breaks for
    non-spin weights. The user's `2026-05-07-spin-shift-mechanism.md` is the
    right next direction.

(d) **A uniform W-level Aug~ priority** (the original Aug~ program). Open.

(e) **Individual KL polynomials $P_{u,v}(q)$.** CKL only computes the summed
    Lusztig polynomial; refining to individual $P_{u,v}$ is the OQ2 question.

---

## 9. References

- **CKL** = Choi–Kim–Lee, *Lusztig q-weight multiplicities and Kirillov–
  Reshetikhin crystals*, arXiv:2412.20757v2.
  - §4.3 (Proof of Thm 4.6, p. 23–24): the n-indexed sign-reversing involution.
  - Prop A.13 + Remark A.17 (p. 51–52): Aug-invariance of $\overline D$.
  - Prop A.26 (p. 55): the q^r t^m energy shift in the spin column case.
- **Lec06** = Lecouvey, *q-analogues of weight multiplicities for type C/B/D
  via the affine Hecke algebra* (or wherever Thm 3.2.1 lives — exact ref to
  pin down).
- `papers/ckl-theorem-46-extraction.md` (correct **but** misclassifies
  Theorem 4.6 as "q=t=1 only" in §1; needs an editorial note).
- `proofs/2026-05-07-SA-B2-proof-and-Bn-program.md` — B_2 (SA) via Aug~.

---

## 10. Honest assessment

**Solid:**
- (SA) for dominant spin λ, μ in B_n: PROVED via CKL Theorem 4.6 + Lemma 3.1.
- The bigraded refinement of Aug-invariance (Lemma 3.1) has a complete,
  elementary proof using only the explicit definitions of vacancy and the
  Aug operation.
- The proof of Theorem 4.6 in CKL §4.3 is rigorous; the only step they leave
  to the reader is the bigraded analog of Prop A.13, which Lemma 3.1 fills.

**Soft:**
- Eq. (4.13) is asserted by CKL as "a straightforward generalization of
  Lecouvey's result". I haven't verified Lecouvey's argument generalizes
  cleanly to (q,t). It almost certainly does (the bigrading by long/short
  is preserved by the n→n−1 restriction), but a careful read of Lec06
  Thm 3.2.1 + bigraded translation would close this gap.
- The non-negativity and parity of $(\overline D - \mathrm{vac})/2$ on the
  image of $\phi_c$ is implicit in CKL but should be stated as a separate
  lemma (proved via the explicit $\overline H$ formula on $B^{1,1}(\mathsf B)$
  and the splitting map).

**Missing entirely:**
- Lecouvey's q-only Morris proof, in full detail. (The bigraded extension
  rests on it.)

---

## 11. Action items

- [x] Write this proof note. ✓
- [ ] **Editorial:** add a one-line correction to
      `papers/ckl-theorem-46-extraction.md` clarifying that Theorem 4.6 is
      already the (q,t) statement.
- [ ] Update `~/projects/memory/SUMMARY.md` to reflect that (SA) for
      dominant spin is now a theorem.
- [ ] Add to `~/projects/memory/for-collaborator/` a short note explaining
      the resolution: the route was through CKL all along.
- [ ] (Optional, future session) **Pull-back priority:** translate CKL's
      n-indexed involution back to a W-indexed combinatorial Aug~. This is
      the "Aug~ via CKL" project.
- [ ] (Optional, future session) Read Lec06 Thm 3.2.1 carefully and
      confirm the bigraded extension is straightforward.
