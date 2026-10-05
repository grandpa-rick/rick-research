# Day 194 — Sanity check of Day 191 $e_2 \star e_r$ formula: $t=0$ and $q\to\infty$ specializations, vs. van Diejen–Emsiz–Zurrián (arXiv:2305.01931)

**Date.** 2026-09-16
**Priority.** P4 (~20 min compute)
**Registry.** `hikita-star-e2-e2.json` node `e2-star-er-pieri-conjecture` (`computed`, r≤6 verified through Day 193).

---

## 0. The formula under test

Rick's Day 191 closed form (Hikita $\star$-product at parameters $(q,t)$, in the multiplicative $e$-basis):

$$e_2 \star e_r \;=\; \frac{1}{q^{2}}\,e_2 e_r \;+\; \frac{1-q^{-1}}{q}\,[r]_t\,e_1 e_{r+1} \;+\; (1-q^{-1})\,\frac{[r+2]_t}{[2]_t}\!\left([r+1]_t - \frac{t\,[r-1]_t}{q}\right)\! e_{r+2}$$

with $[k]_t := 1 + t + \dots + t^{k-1}$, and $[0]_t := 0$.

---

## 1. $t = 0$ specialization (elementary)

At $t=0$: $[k]_t = 1$ for all $k \ge 1$, $[0]_t = 0$. In particular $[2]_t = 1$, $[r+1]_t = [r+2]_t = [r-1]_t$ all $=1$ (for $r \ge 2$; for $r=1$ the last one is $[0]_t=0$).

Case $r \ge 2$. Third bracket $\bigl([r+1]_t - t[r-1]_t/q\bigr) \big|_{t=0} = 1 - 0 = 1$. So

$$\boxed{\;e_2 \star e_r \big|_{t=0} \;=\; \frac{1}{q^{2}}\,e_2 e_r \;+\; \frac{q-1}{q^{2}}\,e_1 e_{r+1} \;+\; \frac{q-1}{q}\,e_{r+2}\quad(r \ge 2).\;}$$

Equivalently, multiplying by $q^2$:

$$q^{2}\bigl(e_2 \star e_r\bigr)\big|_{t=0} \;=\; e_2 e_r \;+\; (q-1)\,e_1 e_{r+1} \;+\; q(q-1)\,e_{r+2}.$$

Case $r = 1$. $t[r-1]_t = t \cdot [0]_t = 0$, so the bracket is still $1$, and the formula agrees; the $e_1 e_{r+1}=e_1 e_2$ and $e_2 e_r=e_2 e_1$ merge:

$$e_2 \star e_1 \big|_{t=0} \;=\; \tfrac{1}{q^{2}}\,e_2 e_1 + \tfrac{q-1}{q^{2}}\,e_1 e_2 + \tfrac{q-1}{q}\,e_3 \;=\; \tfrac{1}{q}\,e_1 e_2 + \tfrac{q-1}{q}\,e_3.$$

**Sanity at $q=1$.** All three coefficients become $(1,\,0,\,0)$, so $e_2 \star e_r \big|_{q=1} = e_2 e_r$ (ordinary commutative product) — consistent with the classical limit of Hikita's $\star$-product.

**Structural observation.** At $t=0$ the formula loses all $t$-quantum structure (all $[k]_t \to 1$); only the $q$-quantum deformation of the multiplicative rule survives. The three coefficients are polynomials in $q$ with total sum equal to $q^2 - q + q(q-1) + \ldots$ (checked $q=1$ collapse above).

## 2. $q \to \infty$ specialization (general $t$)

Take leading term in $q$ for each coefficient:

| term | coefficient | $q\to\infty$ limit |
|---|---|---|
| $e_2 e_r$ | $1/q^2$ | $0$ |
| $e_1 e_{r+1}$ | $(1-q^{-1})[r]_t / q$ | $0$ |
| $e_{r+2}$ | $(1-q^{-1})\,[r+2]_t/[2]_t \cdot ([r+1]_t - t[r-1]_t/q)$ | $[r+2]_t\,[r+1]_t/[2]_t$ |

Recall the Gaussian binomial: $\binom{r+2}{2}_t = \tfrac{[r+2]_t\,[r+1]_t}{[2]_t\,[1]_t} = \tfrac{[r+2]_t\,[r+1]_t}{[2]_t}$.

$$\boxed{\;\lim_{q\to\infty}\bigl(e_2 \star e_r\bigr) \;=\; \binom{r+2}{2}_t\,e_{r+2}.\;}$$

This is exactly Rick's stated "Pieri limit" shape $\binom{a+r}{a}_t e_{a+r}$ at $a=2$. **Consistent.** ✓

**Cross-check at $t=1$.** $[k]_t \big|_{t=1}=k$, so $\binom{r+2}{2}_t \big|_{t=1} = \binom{r+2}{2} = (r+2)(r+1)/2$.
From the general formula at $t=1$:
$$e_2 \star e_r \big|_{t=1} = \tfrac{1}{q^2} e_2 e_r + \tfrac{r(q-1)}{q^2} e_1 e_{r+1} + \tfrac{(q-1)(r+2)((r+1)q - (r-1))}{2q^2}\,e_{r+2}.$$
As $q\to\infty$: coefficient of $e_{r+2}$ tends to $(r+2)(r+1)/2$. ✓

---

## 3. van Diejen–Emsiz–Zurrián arXiv:2305.01931 — what it actually says

**Paper.** J.F. van Diejen, E. Emsiz, I.N. Zurrián, *Affine Pieri rule for periodic Macdonald spherical functions and fusion rings*, arXiv:2305.01931.

**Downloaded to** `/home/agent/papers/vDEZ-2305.01931.pdf` (367 KB, extracted `.txt` 96 KB).

**Setting.** For an affine root system with level $c$, they study a $t$-deformation of the WZW fusion ring, built from a basis of *periodic Macdonald spherical functions* $M_\lambda^{(c)}$. In type $\hat A_{n-1}$ this is Korff's cylindric Hall–Littlewood setup.

**The one Pieri rule they give explicitly (Eq. 1.2 / Cor. 4.2 / Thm 2.4).** For $\lambda \in \Lambda^{(n,c)}$ and a minuscule fundamental weight $\omega_r$,

$$R^{(c)}_\lambda \cdot R^{(c)}_{\omega_r} \;=\; c_{\omega_r}(t) \sum_{J\subseteq\{1,\dots,n\},\,|J|=r,\;\lambda + \bar e_J \in \Lambda^{(n,c)}} R^{(c)}_{\lambda + \bar e_J}\;\prod_{\substack{1\le j<k\le n\\ j\in J,\,k\notin J\\ \lambda_j=\lambda_k}}\!\!\frac{1-t^{k-j+1}}{1-t^{k-j}}\;\prod_{\substack{1\le j<k\le n\\ j\notin J,\,k\in J\\ \lambda_j=\lambda_k+c}}\!\!\frac{1-t^{n+1-k+j}}{1-t^{n-k+j}}.$$

**$t=0$ specialization (their Eq. 1.5, WZW/Verlinde fusion).**
$$s^{(c)}_\lambda \cdot s^{(c)}_{\omega_r} \;=\; \sum_{\substack{J\subseteq\{1,\dots,n\},\,|J|=r\\ \lambda + \bar e_J \in \Lambda^{(n,c)}}} s^{(c)}_{\lambda + \bar e_J}.$$

Since in type $A_{n-1}$ we have $s_{\omega_r} = e_r$ (elementary sym.), this rule expresses $s_\lambda \cdot e_r$ in the truncated Schur basis at level $c$.

---

## 4. Convention translation and verdict

There are **four independent structural gaps** between Rick's setup and vDEZ's, none of which look bridgeable by a simple substitution.

**Gap A (parameter count).** vDEZ has one parameter $t$. Rick's $\star$-product has two, $(q,t)$. There is no independent "$q$" knob in vDEZ; specialising Rick's formula at $t=0$ leaves the entire $q$-dependence intact.

**Gap B (structure being computed).** vDEZ's Pieri rule is $R_\lambda \cdot R_{\omega_r}$: a *minuscule times HL-basis element*. Rick's formula is $e_2 \star e_r$: a *product of two elementaries* under the Hikita $\star$-product. To get from one to the other one must either
(i) expand $e_2 = R_{\omega_2}$ and use vDEZ Pieri (once) to compute $e_2 \cdot e_r$ in the HL basis, then re-expand into products of $e$'s — but $\omega_2$ is minuscule so this is a *single* Pieri step, producing an HL-basis sum, not a three-term $e$-basis formula; or
(ii) iterate two Pieri steps for the ordinary product $e_2 \cdot e_r$ — but the ordinary product $e_2 e_r$ is trivially given by the multiplicative basis, so vDEZ says nothing extra here.

**Gap C (ring truncation).** vDEZ works in the level-$c$ truncated ring $\Lambda^{(n,c)}$ (WZW fusion at level $c$). Rick's $\star$-product lives on the untruncated $\Lambda[[q,t]]$. Rick's three terms $e_2 e_r,\, e_1 e_{r+1},\, e_{r+2}$ do not carry any level cap.

**Gap D (product vs. star-product).** vDEZ's `·` is the ordinary commutative product on the (finite-dimensional) fusion algebra. Rick's `$\star$` is a $q$-deformation of the ordinary Sym product. At $q=1$ Rick's $\star$-product reduces to the ordinary product on $\Lambda$ (checked in §1: coefficients $(1,0,0)$), which is not the WZW fusion product — that's obtained by a further $t=0$ AND level-truncation.

**Verdict.** **Inconclusive — probably no direct match; needs Rick's judgement.**

The natural specialization of Rick's formula that could plausibly touch WZW fusion is $q=1$ (recovering ordinary Sym product) followed by $t=0$ (recovering Schur product), then level truncation — but that's just the trivial commutative $e_r e_2 = e_r e_2$, giving no test of the interesting content of Rick's $\star$-Pieri conjecture.

The $q\to\infty,\,t$ general limit gives $\binom{r+2}{2}_t e_{r+2}$: a *single* $e$-partition on the RHS. **This shape does resemble a Pieri output**, and might be the true "Pieri limit" of Rick's $\star$-Pieri (with the Gaussian binomial $\binom{r+2}{2}_t$ playing the role of a multiplicity). But vDEZ's rule at $t=0$ produces a *sum* over $J$, and the two lattice structures (compositions vs. weight-lattice offsets $\bar e_J$) are not obviously commensurable when the LHS is $e_2 \cdot e_r$ rather than a HL-basis product.

**Concrete open question for Rick.** Is Hikita's $\star$-product related to a *shifted* version of Korff's cylindric HL product where $q$ plays the role of an *additional* boundary-shift parameter (perhaps the cylindric shift $c$ analytically continued, or a $q$-deformation of the level)? If so, the $t=0$ limit of Rick's formula (§1) is a candidate for the $t=0$ specialization of that shifted product, and vDEZ's $s_\lambda \cdot s_{\omega_r}$ Pieri would be recoverable only at some further specialization $q \to ?$. Answering this is above the pay grade of a 20-min compute check.

**No hallucinated match.** I do not claim §1 matches any specific formula in vDEZ.

---

## 5. What was and wasn't done

- **Done.** $t=0$ specialization of Rick's formula (§1). $q\to\infty$ specialization at general $t$ giving $\binom{r+2}{2}_t e_{r+2}$ (§2). Cross-check at $t=1$ (§2). Fetched and read the vDEZ paper, extracted the Pieri rules and $t=0$ WZW specialization (§3).
- **Not done / not doable in 20 min.** A meaningful convention dictionary between Hikita's $\star$-product $(q,t)$ and vDEZ's cylindric HL product $(t, c)$. This would need (a) an independent computation of $e_2 \cdot e_r$ in vDEZ's setup (iterated Pieri, expansion back to $e$-basis at some level $c$), and (b) a hypothesis about how Rick's $q$ maps into $c$ or an auxiliary parameter. Estimated $\ge 1$ session.

**Registry impact.** No change. `e2-star-er-pieri-conjecture` remains at `computed` (verified $r \le 6$). The $t=0$ limit in §1 and the $q\to\infty$ limit in §2 are new sanity checks and are internally consistent with Rick's Pieri-limit statement. No cross-validation against vDEZ obtained.
