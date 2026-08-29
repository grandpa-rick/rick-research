---
title: Day 112 — Sub-claim (⋆⋆) verification and proof progress toward (T)
status: EMPIRICAL — (⋆⋆) VERIFIED for R = 2, 3, 4, 5. Proof partial.
---

# Sub-claim (⋆⋆) — empirical verification and proof progress

## Setting (recap)

We want to prove **(T):** $Q_{2R}(a, b, c)$ has total $(a, b)$-degree $\leq 2R$.

The proof mechanism (Day 111 sketch):

$$H_c(a, b, j) := (a+3)_{c-1-j}(b+2)_{c-1-j} \cdot (ds_j / V), \qquad
h_{2R} := \sum_{j=0}^{2R}(-1)^{2R-j}\binom{2R}{j} H_c(a, b, j).$$

$H_c(a, b, j)$ has $(a, b)$-total-degree $\leq 2(c-1) =: \text{TOP}$ (equality when $\mu = (j, j, 0)$ contributes).

**Sub-claim (⋆⋆):** For each $d \in \{0, 1, \ldots\}$, the coefficient of the $(a, b)$-layer at total degree $\text{TOP} - d$ in $H_c(a, b, j)$, at each monomial slot $a^i b^k$ with $i + k = \text{TOP} - d$, is a polynomial in $j$ (for fixed $c$) of degree $\leq d$.

Consequence via finite-difference annihilation: $h_{2R}$ has $(a, b)$-degree $\leq \text{TOP} - 2R = 2c - 2 - 2R$, hence $Q_{2R}$ has $(a, b)$-degree $\leq 2R$.

## Empirical verification (Day 112)

**Script:** `/home/agent/projects/beta-prime/code/2026-08-19-T-sub-claim-verify.py`.
**Log:** `/home/agent/projects/beta-prime/code/2026-08-19-T-sub-claim-verify.txt`.

Fixed $c = 25$ (so $\text{TOP} = 48$), computed $H_c(a, b, j)$ for $j = 0, \ldots, 2R + 4$
(enough samples to fit and validate polynomial-in-$j$ of degree up to $\sim 2R + 3$).

For every layer $d \in \{0, 1, \ldots, 2R + 2\}$ and every monomial slot $(i, k)$ in that layer,
we extracted the coefficient as a function of $j$ and fit its $j$-degree exactly.

**Result: (⋆⋆) holds for R = 2, 3, 4, 5. Zero violations across 91 slots at R = 5.**

Moreover, the per-layer maxima follow a strikingly clean pattern:

| $d$ | max $j$-deg over slots in layer $d$ |
|-----|--------------------------------------|
| 0   | 0                                    |
| 1   | 0                                    |
| 2   | 2                                    |
| 3   | 2                                    |
| 4   | 4                                    |
| 5   | 4                                    |
| 6   | 6                                    |
| ... | ...                                  |
| $d$ | $2 \lfloor d / 2 \rfloor$            |

So the bound $j\text{-deg} \leq d$ is **almost tight** but always **even**:
$j\text{-deg} = 2 \lfloor d/2 \rfloor$ at the "central" slot of the layer.

**Finer structure — j-degree by slot displacement from corner:**

For slot $(i, k)$ with $i + k = \text{TOP} - d$, write $i = 24 - p$ and $k = 24 - q$ so $p + q = d$.
Then

$$j\text{-deg of coef at }(i, k) = 2 \min(p, q).$$

That is, the $j$-degree is determined by the SMALLER of the two displacements from the corner
$(24, 24)$. Layers arranged as a "staircase": corner slot has $j$-deg $0$, one-off-corner
has $j$-deg $0$ (still one coordinate at 24), two-off-corner central has $j$-deg $2$, etc.

Formally: on the "off-diagonal" slots (where $p \neq q$), one coordinate is closer to
the corner and the finite-difference-order-$d$ annihilation actually kicks in earlier,
with room to spare.

## Interpretation

The bound $j\text{-deg} \leq d$ is confirmed. But the *tightness pattern* reveals more:
only the "central" slots ($p \approx q$) approach the bound, and even they cap out at
$2\lfloor d/2 \rfloor$, one less than allowed for odd $d$. This suggests a
Pochhammer-symmetry proof is available: the two-Pochhammer decomposition
$P_j(a) Q_j(b)$ contributes to slots symmetrically, and $ds_j/V$ has a
$(y_1, y_2)$-symmetry (or rather $(a, b)$-symmetry up to a sign from Vandermonde) that
forces even $j$-degrees at the diagonal.

## Proof progress on Sub-claim (⋆⋆)

**Structure of proof (partially formal):**

Write $H_c(a, b, j) = P_j(a) \cdot Q_j(b) \cdot S_j(a, b, c)$ with:

1. $P_j(a) = (a+3)_{c-1-j}$ — polynomial in $a$ of degree $c-1-j$.
2. $Q_j(b) = (b+2)_{c-1-j}$ — polynomial in $b$ of degree $c-1-j$.
3. $S_j(a, b, c) = ds_j/V$ — polynomial in $(a, b, c)$ of $(a,b)$-total-degree $\leq 2j$.

**Step 1 (Pochhammer expansion in $j$).** For $c$ fixed, the coefficient of $a^{c-1-j-i}$
in $P_j(a) = (a+3)_{c-1-j}$ is the elementary symmetric polynomial
$e_i(3, 4, \ldots, c-1-j+2)$. As a polynomial in $j$, this has degree exactly $i$:

*Proof.* $e_i(3, 4, \ldots, L)$ for $L = c-1-j+2 = c+1-j$ is a polynomial in $L$ of
degree $i$ (elementary symmetric of the segment $\{3, \ldots, L\}$ is a polynomial in $L$
of degree $i$: think $\binom{L-2}{i}$-like combinatorics). Since $L$ is linear in $j$,
$e_i$ is a polynomial in $j$ of degree $i$. $\square$

More explicitly: pull out $a^{c-1-j}$ from $P_j(a) = \prod_{s=0}^{c-2-j}(a+3+s)$;
in the expansion, the coefficient of $a^{c-1-j-i}$ is $e_i(3, 4, \ldots, c-1-j+2)$.
But we want the coefficient of $a^{c-1-j-i}$ as a monomial in the ORIGINAL
$(a, b)$-layer indexed by $(a, b)$-total-degree, so we need to convert exponent.

Wait: after multiplying $P_j(a) Q_j(b) S_j(a, b, c)$, the total $(a, b)$-degree is
$(c-1-j) + (c-1-j) + (\text{something} \leq 2j) = 2c - 2 + (\text{drop}_{S_j})$
where $\text{drop}_{S_j}$ ranges over $[-2c+2+2j, 0]$... actually the top layer is
achieved when $S_j$ contributes its max $(a,b)$-degree part, which is $a^j b^j$
(empirically for $\mu = (j, j, 0)$, top is $y_1^{j-2} y_2^{j-1}(y_1 + y_2 - 2y_3)$?
no — see below).

The empirical observation from Part C exploration:
**top $(a, b)$-part of $ds_j/V$ is exactly $a^j b^j$**, i.e., $(a, b)$-degree $2j$
with monic leading coefficient. This is CONSTANT in $j$ (as a normalized coefficient
of $a^j b^j$: it's $1$).

**Step 2 (top of $S_j$).** For $j \geq 1$, $S_j(a, b, c) = a^j b^j + \text{lower}$
in $(a, b)$. So the highest $(a, b)$-degree in $H_c(a, b, j)$ is
$(c-1-j) + (c-1-j) + 2j = 2c - 2$, coefficient of $a^{c-1} b^{c-1}$ is
$1 \cdot 1 \cdot 1 = 1$ (from $a^{c-1-j}$ in $P_j$, $b^{c-1-j}$ in $Q_j$, $a^j b^j$ in $S_j$).

This is $j$-INDEPENDENT (constant $1$), matching the $d = 0$ case: layer at
$\text{TOP} - 0 = 2c - 2$ has one slot $(c-1, c-1)$ with coefficient $1$; $j$-deg $= 0$. ✓

**Step 3 (convolution for $d > 0$).** The coefficient of $a^i b^k$ with $i + k = \text{TOP} - d$
in $H_c(a, b, j)$ is:

$$[a^i b^k] H_c = \sum_{i_P, i_Q, r} [a^{i_P}] P_j(a) \cdot [b^{i_Q}] Q_j(b) \cdot [a^{i - i_P} b^{k - i_Q}] S_j(a, b, c)$$

where the sum is over $(i_P, i_Q)$ with $i_P \leq c-1-j$, $i_Q \leq c-1-j$, and
$(i - i_P) + (k - i_Q) \leq 2j$ (so this term of $S_j$ makes sense).

Set $p_P := (c-1-j) - i_P$ = drop of $P_j$ from top in $a$;
$p_Q := (c-1-j) - i_Q$ = drop of $Q_j$ from top in $b$;
$p_S := 2j - [(i - i_P) + (k - i_Q)]$ = drop of $S_j$ from top in $(a, b)$.

Then: total drop $= p_P + p_Q + p_S = (c-1-j - i_P) + (c-1-j - i_Q) + 2j - (i - i_P + k - i_Q)$
$= 2(c-1) - i - k = 2(c-1) - (\text{TOP} - d) = d$.

So $p_P + p_Q + p_S = d$.

**Sub-lemma (Pochhammer part):** $[a^{i_P}] P_j(a) = e_{p_P}(3, 4, \ldots, c+1-j)$ is a polynomial
in $j$ of degree $\leq p_P$. Similarly for $[b^{i_Q}] Q_j(b)$: degree $\leq p_Q$ in $j$.

**Sub-sub-claim (⋆⋆⋆):** $[a^{i - i_P} b^{k - i_Q}] S_j(a, b, c)$ has $j$-degree $\leq p_S$
(as a function of $j$, for fixed $c$).

Given (⋆⋆⋆), the product has $j$-degree $\leq p_P + p_Q + p_S = d$; summing over
$(i_P, i_Q, r)$ (finitely many terms) preserves the $j$-degree bound. **This proves (⋆⋆).**

So the remaining question is (⋆⋆⋆), which is about $S_j$ alone.

**Empirical check of (⋆⋆⋆):** the "top of $S_j$" (at $(a, b)$-degree $2j$) is
just $a^j b^j$, $j$-independent → $j$-deg $\leq 0$. Good, matches $p_S = 0$ layer.

At layer $2j - r$ of $S_j$ (with $r \geq 1$), coefficients depend on $j$
polynomially. Empirical (U_1) and (U_2) confirmations:
- (U_1) at $r = 0$: coefficient of $b^{2j-r}$ in $S_j|_{a=0}$ is $j$-poly deg $0$. ✓
- (U_1) at $r = 2$: $j$-poly deg $2$. Matches $\leq r = 2$. ✓
- (U_2) $\mu_3 = 0, 1, 2, 2$ contributions have $j$-degrees $0, 1, 2, 2$
  respectively (max $= 2 = r$). ✓

**Proof strategy for (⋆⋆⋆):** the layer of $S_j$ at $(a, b)$-total-degree $2j - r$
receives contributions ONLY from partitions $\mu \in \mathcal{S}_j$ with $\mu_3 \geq r$
(the "rank-drop" observation from Day 111). The number of such partitions is
$O(1)$ as $j \to \infty$ (they are $\mu = (\mu_1, \mu_2, \mu_3)$ with $\mu_1 + \mu_2 + \mu_3 = 2j$
and $\mu_3 \geq r$, so with $\mu_3 - r = s \geq 0$ fixed and $\mu_1 - \mu_2$ free, the family
is parameterized). Each such $\mu$ contributes $\kappa_\mu \cdot s^*_\mu(a+2, b+1, c)$ to $S_j$;
the "top-part-in-$(a,b)$" of $s^*_\mu$ is a specific polynomial in $c$ (independent of $j$)
times a fixed monomial in $(a, b)$, and $\kappa_\mu$ is a combinatorial coefficient that
depends polynomially on $j$ with degree bounded by... **this is the technical remaining piece.**

**Where the $\kappa_\mu$ $j$-degree comes from:** $\kappa_\mu$ is the count of paths in
the walk on $\mathcal{S}_\bullet$ from $(0,0,0)$ to $\mu$. From Day 108-111 work, this
appears to be a polynomial in $j$ of degree $= \mu_3$ (empirically at $\mu_3 = 0$: 1;
$\mu_3 = 1$: $2(j-1)$, degree 1; $\mu_3 = 2$ pieces: $(j-1)(j-2)$ and $j(j-3)$, degree 2).

**Conjecture:** $\kappa_\mu$ at $\mu = (\mu_1, \mu_2, r)$ with $\mu_1 + \mu_2 = 2j - r$
is a polynomial in $j$ of degree $\leq r$.

**Sketch of proof:** $\kappa_\mu$ counts walk endings at $\mu$ in $j$ steps; each step
adds a domino from a box choice. For $\mu_3 = r$, we need $r$ steps that increment
$\mu_3$; these $r$ steps can be placed in the $j$-step walk in $\binom{j}{r}$-like ways,
giving a polynomial in $j$ of degree $r$. Confirmed empirically (U_2). *This should be
provable by direct enumeration of the walk on the shape.*

## Structural alternative to (T)?

The identity (I): $Q_{2R} = \sum_{k=0}^R \tilde P^{(k)}_R(c) (a+2)^{\underline k}(b+1)^{\underline k}$
holds empirically for $R = 2, 3$. Since each summand has $(a, b)$-degree $2k$, (I) implies (T).

**But (I) is stronger than (T)** — it's the full interpolation ansatz, of which (T) is a
consequence. Rick's calibration was: (I) is the Slice-$k$-for-$k \leq R$ family + (T);
Sahi-Okounkov's interpolation theorem then bridges (Slice) + (T) $\Rightarrow$ (I).

**Alternative route to (I) that bypasses (T)?**

Idea: prove (I) directly by fixing enough interpolation points. The 2-variable version of
the Sahi-Okounkov Newton-interpolation setup for symmetric polynomials characterizes
interpolation of degree $\leq d$ by their values on a $\Omega$-grid. If we can:

1. Show $Q_{2R}$ vanishes on some large family of points.
2. Bound its degree in $a$ AND $b$ separately by $R$.
3. Then $Q_{2R}$ is uniquely determined by finitely many values, and (I) provides an
   explicit form.

The catch: (T) is essentially "total-$(a, b)$-degree $\leq 2R$", which is stronger than
individual $a$- and $b$-degree bounds. Yet **empirically $a$-degree $= R$, $b$-degree $= R$
separately**. So (T)/(I) can be split:

- **(T-a):** $a$-degree of $Q_{2R} \leq R$.
- **(T-b):** $b$-degree of $Q_{2R} \leq R$.
- **(T):** total $(a, b)$-degree $\leq 2R$ (equivalent to (T-a) + (T-b) + a diagonal condition).

Note: **(T-a) + (T-b) alone do NOT imply (T).** Example: $a^R b^R$ has $a$-degree $R$,
$b$-degree $R$, but total degree $2R$. So they're CONSISTENT with total $\leq 2R$; but
$a^R + b^R$ has $(a, b)$-total $R$, not $2R$. So (T-a) + (T-b) leave room for total up
to $2R$ (which is exactly what (T) says). So **actually (T-a) + (T-b) IMPLIES total $\leq 2R$.**

Wait: (T-a) says every monomial has $a$-power $\leq R$. (T-b) says every monomial has
$b$-power $\leq R$. So every monomial has $(a$-power$)$ + $(b$-power$)$ $\leq 2R$.

**YES: (T) = (T-a) $\wedge$ (T-b).** So proving them separately suffices!

**This is a cleaner split.** Can we prove (T-a) alone using a specialized argument
(e.g., substituting $b = $ specific value to reduce to a univariate problem)?

**Empirical check needed:** verify that the $a$-degree of $Q_{2R}(a, b, c)$ (viewed as
poly in $a$ with $(b, c)$-coefficients) equals $R$ for $R = 2, 3, 4, 5$. From Day 111
Part A of the T-bound investigation, this was reported as YES. So the split (T-a) + (T-b)
is empirically verified.

**Proof plan for (T-a):** by the same alternating sum, apply degree-in-$a$-only analysis
to $H_c(a, b, j)$. The $a$-degree of $H_c(a, b, j) = (a+3)_{c-1-j}(b+2)_{c-1-j} \cdot S_j$
is $(c-1-j) + (a$-deg of $S_j)$. Empirically top $a$-part of $S_j$ is $a^j \cdot (\ldots)$,
so $a$-deg of $H_c(a, b, j) = c - 1$ (in $a$), $j$-independent, coefficient a
polynomial in $b$. And each drop in $a$-degree corresponds to a $j$-poly of degree $\leq$
the drop. **Same finite-difference argument as for (T), but 1D instead of 2D.**

This might be genuinely easier because we only need to track one variable at a time.

## Summary

1. **Sub-claim (⋆⋆) is empirically verified for $R = 2, 3, 4, 5$** — zero violations
   across all 91 monomial slots at $R = 5$. Bound is tight but only at $\lfloor d/2 \rfloor \cdot 2$
   parity (even $j$-degrees only).

2. **Proof of (⋆⋆) reduced to (⋆⋆⋆):** the $(a, b)$-layer at $(a, b)$-deg $2j - r$ of
   $S_j = ds_j/V$ has coefficients that are polynomials in $j$ of degree $\leq r$.

3. **(⋆⋆⋆) reduced to Conjecture:** $\kappa_\mu$ for $\mu_3 = r$ is a polynomial in $j$
   of degree $\leq r$. **This is a combinatorial statement about walk-counts on shifted
   Young diagrams that should be provable by direct enumeration.** Empirically confirmed
   through (U_1) and (U_2).

4. **Structural alternative:** (T) splits as (T-a) $\wedge$ (T-b) via individual variable
   degree bounds. This may be easier to prove: 1D finite-difference argument in $a$ alone.

## Next steps

- **Prove (⋆⋆⋆) / $\kappa_\mu$-degree conjecture** by walk enumeration on $\mathcal{S}_\bullet$.
- **Prove (T-a) individually** as a warm-up (may be doable with univariate methods).
- Cross-check the parity structure ($j$-deg is always EVEN) via the $(a, b)$-symmetry
  of $ds_j/V$.

## Files

- Verification script: `/home/agent/projects/beta-prime/code/2026-08-19-T-sub-claim-verify.py`
- Verification log: `/home/agent/projects/beta-prime/code/2026-08-19-T-sub-claim-verify.txt`
- Preceding sketch: `/home/agent/projects/proofs/2026-08-18-day111-T-bound-proof-sketch.md`
- Day 111 summary: `/home/agent/projects/proofs/2026-08-18-day111-U2-and-T-empirical.md`
