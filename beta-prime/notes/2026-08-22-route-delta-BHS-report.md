# Route δ — BHS 2502.02841 §7 report

**Date:** 2026-08-22
**Paper:** Bump, Hardt, Scrimshaw, *On the boson-fermion correspondence for
factorial Schur functions*, arXiv:2502.02841v1, 5 Feb 2025, 26 pp.
**Target:** decide whether §7 gives (or feeds into) a proof of
$w_{112}(\Psi(e_2^b)) \le b$.

---

## 1. Locating "descending degree" in BHS

The phrase "descending degree" appears **only in the introduction** of BHS
(page 2, lines 58–61), and it is a *summary phrase* for a claim proved in
**§5** (not §7):

> "In Section 5, ... In particular, we can see that the classical
> supersymmetric functions are finite sums of double Schur functions of
> descending degree (i.e. lower filtered). These in turn are finite sums in
> the usual supersymmetric function bases. Therefore, the product of any
> two double supersymmetric functions is a finite sum, which includes the
> Murnaghan–Nakayama rule [3, Thm. 5.23] and the product of two double
> Schur functions."

So Rick's "descending degree = StructB in different language" hypothesis
targeted §7, but the definition actually lives in §5.

In the body of the paper the property is realised as follows:

- **Basis of shifted powers** $(z^{-1}|\alpha)^k = \prod_{i=k+1}^{0}(z^{-1}-\alpha_i)^{-1}\prod_{i=1}^k(z^{-1}-\alpha_i)$, indexed by $k \in \mathbb Z$. In the standard Laurent-series valuation on $\mathbb Z[\alpha]((z))$, $(z^{-1}|\alpha)^k$ has valuation $-k$, so the shifted powers form a **triangular** ($=$ lower-filtered) basis of $\mathbb Z[\alpha]((z))$. (Prop. 2.3, and the sentence following it, page 3.)
- **Consequence for symmetric functions.** After Thm. 5.1 the deformed Murnaghan–Nakayama rule gives, at $\beta=0$, a *finite* expansion of every power-sum $p_\lambda(\mathbf x/\mathbf y)$ into double Schur functions $s_\mu(\mathbf p\Vert\alpha)$. See Example 5.4 (page 20) which computes $p_3 s_{(8,3,1)}$ as a sum of 12 $s_\mu$'s, and Example 5.5 which expands $p_k$ itself.

"Descending degree / lower filtered" therefore means: **when you expand a
polynomial in the shifted (factorial) Schur basis, the shapes $\mu$ that
appear satisfy $|\mu| \le \deg$-of-the-input**, and, dually, expanding a
double Schur $s_\mu(\mathbf p\Vert\alpha)$ in classical basis produces
$s_\mu(\mathbf x/\mathbf y)$ plus terms of *strictly smaller degree* (this
is precisely the Okounkov–Olshanski top-degree property).

## 2. §7 content

§7 (pages 23–25) is titled **"Skew-Pieri rule"** — not "descending
degree." It contains:

- **Cor. 7.1** (= [3, Cor. 6.15] specialised to $\beta=0$): expansions of
  $h_k(\mathbf p'\Vert\alpha) s_{\mu/\nu}(\mathbf p'\Vert\alpha)$ and
  $e_k(\mathbf p'\Vert\alpha) s_{\mu/\nu}(\mathbf p'\Vert\alpha)$ as
  contour-integral sums over pairs $(\lambda,\eta)$ with $\lambda/\mu$ a
  strip and $\nu/\eta$ a strip.
- **Eq. (27), (28)**: closed-form coefficient
  $c^\lambda_{k\mu}(\alpha) = \sum_{s+t=k-|\lambda/\mu|} h_s(\{\alpha_{c(b)}\mid b\in\lambda/\mu\}\cup\alpha_{[1,\ell]}) e_t(\{-\alpha_{j-\lambda'_j}\} \cup -\alpha_{(0,k)})$
  for the straight-shape Pieri $h_k \cdot s_\mu = \sum c^\lambda_{k\mu} s_\lambda$.
- **Prop. 7.2**: a supertableau formula for $c^\lambda_{k\mu}(\iota\alpha)$
  and the remark that no cancellations of monomials occur (although
  Graham positivity is *not* established).
- **Examples 7.3, 7.4** and the pointer that §7 does **not** establish
  Graham positivity.

**Crucially: §7 contains no theorem or corollary stated as a
degree/weight bound.** It is a rule (with an explicit combinatorial
coefficient), not a filtration statement.

## 3. Translation to Rick's setting

Rick's $\Psi$ maps $s_\mu \mapsto s^*_\mu$ where $s^*_\mu$ is the
shifted (Okounkov–Olshanski) Schur function, i.e. the $\alpha_i = i-1$,
$\mathbf y=0$, no-$\beta$ specialisation of the BHS double Schur
$s_\mu(\mathbf x\Vert\alpha)$. In BHS notation:
- $s^*_\mu(x_1,\dots,x_n) = s_\mu(\mathbf x\Vert\alpha)\big|_{\alpha_i = i-1}$.
- $\Psi(f) = T(f\cdot V)/V$ with $T(u^\beta)=\prod_i [u_i]_{\beta_i}$ is
  exactly the shift/normal-ordering operator that, at $\beta = 0$,
  converts classical Schurs to shifted Schurs.

BHS §5's "descending degree" translated into Rick's language is:

> **BHS-descending-degree (Rick-translated):** if $f$ is symmetric of
> $\deg f = d$ then $\Psi(f) = \sum_\mu c_\mu(\alpha) s^*_\mu$ with all
> $|\mu| \le d$, and the top-degree part is $\sum_{|\mu|=d} c_\mu \cdot s_\mu$.

This is the **classical degree filtration**, i.e. Rick's Path (a) fact
"$\deg(\Psi(f) - T(f)) < \deg f$" from `2026-08-22-day124-psi-vs-t.md`
§3(a). It is *not* the $(1,1,2)$-weight $w_{112}$; total degree ≠
$w_{112}$-weight.

## 4. Does BHS §7 give $w_{112}(\Psi(e_2^b)) \le b$?

**No, not directly.** The mismatch is stark:

| Property | BHS §5/§7 gives | Rick needs |
|---|---|---|
| Filtration | total degree $|\mu|$ | $(1,1,2)$-weight $a_1+a_2+2a_3$ in $e$-basis |
| Object | expansion of $p_\lambda$ or $h_k s_\mu$, $e_k s_\mu$ | expansion of $\Psi(e_2^b)$ in $e$-basis |
| Grading | monomial degree in $\mathbf x/\mathbf y$ | weighted degree with $w(e_3)=2$ |

BHS §7 controls a *Pieri* expansion into shifted Schurs $s^*_\lambda$
with shape constraints $\lambda/\mu \in$ strip. But $\Psi(e_2^b)$ is
already known (elementary): $e_2 = s_{(1,1)}$, so
$e_2^b = s_{(1,1)}^b = \sum_\mu K_{\mu,(2^b)} s_\mu$ (Kostka numbers),
and $\Psi(e_2^b) = \sum_\mu K_{\mu,(2^b)} s^*_\mu$. This is a straight
consequence of $\Psi$ being basis-defined, and does not require §7.
The nontrivial step is re-expanding each $s^*_\mu$ back into $e_1,e_2,e_3$
and checking the $(1,1,2)$-weight of the result — precisely the step
BHS §7 does *not* address.

## 5. What §5/§7 *does* give us that helps

Two useful borrowables:

**(i) The lower-filtered structure (§5, from shifted-power triangularity,
Prop. 2.3).** This is a rigorous restatement of "top of $s^*_\mu$
equals $s_\mu$", which Rick already used empirically in
`day124-psi-vs-t.md` §3(a). BHS gives a clean $\beta=0$ algebraic proof
(no analytic assumptions on $\alpha$). This closes Rick's "Step 1" in
that note: **$\deg(\Psi(f) - T(f)) < \deg f$ for all symmetric $f$**
is now a citeable theorem (chain: Prop. 2.3 → triangularity of shifted
power basis → Cor. 5.14 / Prop. 4.6 → top of $s^*_\mu$ is $s_\mu$).
This is the "degree bound" leg, not the $(1,1,2)$-weight leg.

**(ii) Explicit Pieri coefficient formula (Eq. 27, 28).** Setting
$\mu = \varnothing$, $\alpha_i = i-1$ (Rick's specialisation),
$c^\lambda_{k,\varnothing}$ becomes an explicit factor-$e/h$ integral
in the $\alpha_i - \alpha_j = i-j$ values. Iterating with $k=1$ (or
using $e_2 = s_{(1,1)}$ = one application of the $e_k$ variant Cor.
7.1(24b) with $k=2$, $\mu=\varnothing$) gives an *explicit* expansion
$e_2^b = \sum c^\lambda \cdot s^*_\lambda$-style formulas at the level
of $\mathbf x\Vert\alpha$. But this still requires an *external*
degree/weight input to conclude $w_{112} \le b$. The coefficients
$c^\lambda_{k,\mu}$ live in $\mathbb Z[\alpha]$; when specialised to
$\alpha_i = i-1$ they become integers, and there is no natural
$(1,1,2)$-grading visible in Eq. 27.

## 6. Missing step to get StructB from BHS

The path BHS provides:

1. $\Psi(e_2^b) = \sum_{|\mu|\le 2b} K_{\mu,(2^b)} s^*_\mu$ (trivial).
2. Each $s^*_\mu$ re-expands as an element of $\mathbb Q[e_1,e_2,e_3]$
   (rank-3 case) with $\deg_{\text{total}} \le |\mu|$ (BHS §5, or
   classical Okounkov–Olshanski).

Steps 1 + 2 give the **total-degree** bound $\deg_{\text{tot}} \Psi(e_2^b) \le 2b$.
But StructB wants $w_{112} \le b$, which is a **stronger** bound because
$w_{112}(e_3) = 2 = \deg_{\text{tot}}(e_3)$ but $w_{112}(e_1^a) = a =
\deg_{\text{tot}}(e_1^a)$. Total degree $\le 2b$ allows monomials like
$e_1^{2b}$ with $w_{112} = 2b$; StructB forbids these.

**Missing step:** we need to know that, in the $e$-basis expansion of
each $s^*_\mu$ under Rick's specialisation ($n=3$, $\alpha_i = i-1$),
the coefficient of any monomial $e_1^{a_1}e_2^{a_2}e_3^{a_3}$ with
$a_1 + a_2 + 2a_3 > $ (some function of $\mu$ that sums correctly to
$b$ under Kostka) vanishes. **BHS does not provide this.** Its
descending-degree property is w.r.t. classical total degree, not
$w_{112}$.

## 7. Verdict

- **Route δ (BHS §7) does not close StructB.** The "descending degree"
  is $\ne$ $(1,1,2)$-weight; it is the classical total-degree filtration
  Rick already knows.
- **Route δ gives one solid citation** (Prop. 2.3 + §5 lower-filtered
  theorem) for Rick's day-124 Step 1: *$\deg(\Psi(f) - T(f)) < \deg f$
  for symmetric $f$*.
- **§7 itself** (the skew-Pieri formulas) is an *expansion result*, not
  a *bound* result. Not usable without extra input.
- The mismatch is fundamental: $w_{112}$ weighs $e_3$ by 2, while any
  degree filtration coming from a shape-based indexation (like
  $\lambda \vdash n$) weighs $e_3$ by 3 (a $3$-box column). No amount of
  Pieri manipulation in BHS is going to convert one grading into the
  other.

## 8. Recommendation

- **De-prioritise Route δ (BHS §7)** for closing StructB directly. Keep
  BHS §5 in the citation list for the total-degree fact.
- **Prioritise Route M (Molev shifted Pieri) and Route Stirling.** The
  $(1,1,2)$-weight is essentially a $t$-degree count under Rick's
  substitution $u_1\to t+j$, $u_2\to t(j+1)$, $u_3\to t^2$; that is a
  *substitution*, not a *grading on the Pieri rule*. StructB should
  fall from a direct analysis of how many $t$'s can survive in
  $s^*_\mu(t+j, t(j+1), t^2)$ — the shifted-Schur-in-$t$ approach —
  which is closer to Molev's explicit $s^*_\mu$ formulas than to BHS's
  Pieri rule.
- **One concrete borrow from BHS:** apply the shifted-power basis Prop.
  2.3 to write $s^*_\mu(t+j, t(j+1), t^2)$ as a Laurent series in
  $t^{-1}$; the triangularity may make the $t$-degree count immediate.
  This is worth 20 minutes of paper before abandoning Route δ.

## 9. Files

- Paper: `/home/agent/papers/BHS-2502.02841.pdf` (26 pp).
- These notes: `/home/agent/projects/beta-prime/notes/2026-08-22-route-delta-BHS-report.md`.
- Companion (Rick's day-124 analysis): `2026-08-22-day124-psi-vs-t.md`.
