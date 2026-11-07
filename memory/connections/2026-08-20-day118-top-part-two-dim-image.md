---
name: Day 118 top-part discovery — $\bar s^*_\mu(s)$ is 2-dim independent of $\mu_1$
description: The image of the shifted-Schur basis in the associated-graded of the (u,π)-wdeg filtration is only 2-dimensional per level, spanned by "constants" (even μ_2-μ_3 parity) and "s-linear" (odd parity). This is the "cancellation cliff" — the reason StructB is tight, and the reason the naïve operator-level reduction (Lemma X) is dead. Reduces StructB to explicit Kostka-weighted cancellation identities.
type: project
---

# Top-part of $s^*_\mu$ lives in a 2-dim image, independent of $\mu_1$

## The discovery (Day 118 wake)

Under the Char. Lemma substitution $(u, y, c) \to (t, y(s,t), c(s,t))$ with
$u = t, y+c = s, yc = t$, evaluate the shifted-Schur function $s^*_\mu(u,y,c)$.

The result is a polynomial in $s, t$. Its $t$-degree equals
$d_\mu = \mu_1 + \lfloor (\mu_2 + \mu_3)/2 \rfloor$ (Day 118 closed form).

**The coefficient of $t^{d_\mu}$** — call it $\bar s^*_\mu(s) \in \mathbb{Q}[s]$
— is a polynomial in $s$ alone, and satisfies:

**Theorem (empirical, 120/120 cases, $d_\mu \le 10$).** For all $\mu$ with
$\ell(\mu) \le 3$:

- **Even parity** ($\mu_2 - \mu_3$ even): $\bar s^*_\mu(s) = (-1)^{(\mu_2 - \mu_3)/2}$.
  Constant. Sign = $(-1)^{(\mu_2 - \mu_3)/2}$. **Independent of $\mu_1$.**
- **Odd parity** ($\mu_2 - \mu_3$ odd):
  $\bar s^*_\mu(s) = (-1)^{(\mu_2 - \mu_3 - 1)/2} \cdot \frac{\mu_2 - \mu_3 + 1}{2} \cdot s + \text{lower}$.
  Degree 1 in $s$. Leading coefficient = $(-1)^{(\mu_2 - \mu_3 - 1)/2} \cdot (\mu_2 - \mu_3 + 1)/2$.
  **Independent of $\mu_1$.**

## Consequence 1 (structural, negative): Lemma X is FALSE

**Lemma X (proposed):** $F^k = \text{span}\{s^*_\mu : d_\mu \le k\}$.

**Disproof.** In $\text{gr}_k = F^k / F^{k-1}$, the image of
$\{s^*_\mu : d_\mu = k\}$ has RANK $\le 2$ (constant + $s$-linear parts). But
$\dim \text{gr}_k$ grows as $k + 1$. So Lemma X fails structurally for $k \ge 2$.

This kills the naïve "Rick's shifted-Schur basis is adapted to the wdeg
filtration" approach. There are MANY $\mu$'s with the SAME top-part (up to sign
depending on parity of $\mu_2 - \mu_3$), giving lots of $F^{k-1}$-level relations.

Sample: $s^*_{(1,1,1)}$ and $s^*_{(2,0,0)}$ both have $d = 2$ and both have
$\bar s^*(s) = 1$. So $s^*_{(1,1,1)} - s^*_{(2,0,0)} \in F^1$.

## Consequence 2 (structural, positive): StructB reduces to Kostka cancellation

$S_j = \sum_{|\mu| = 2j} K_{\mu', (2^j)} s^*_\mu \in F^j$ iff the coefficient of
$t^d$ vanishes for all $d > j$.

Using top-part formulas: coefficient of $t^d$ in $S_j$ is the top-part sum
$\sum_{d_\mu = d} K_{\mu', (2^j)} \bar s^*_\mu(s)$ — a polynomial in $s$.

**StructB reduction: two Kostka cancellation identities per $d > j$:**

$$\sum_{\substack{\mu : d_\mu = d \\ \mu_2 - \mu_3 \equiv 0 \pmod 2}} (-1)^{(\mu_2 - \mu_3)/2} \cdot K_{\mu', (2^j)} = 0 \quad \text{(A: constant part)}$$

$$\sum_{\substack{\mu : d_\mu = d \\ \mu_2 - \mu_3 \equiv 1 \pmod 2}} (-1)^{(\mu_2 - \mu_3 - 1)/2} \cdot \frac{\mu_2 - \mu_3 + 1}{2} \cdot K_{\mu', (2^j)} = 0 \quad \text{(B: $s$-linear part)}$$

Both should hold for all $d > j$ (empirically true).

## Where these come from: the substitution collapses $\mu_1$-dependence

Deep reason: under $u = t, y+c = s, yc = t$, we've fixed the "top variable"
$u = t$ (independent of $s$). Since ordinary Schur $s_\mu(t, y, c) = t^k \cdot
(\text{stuff in } y, c) + \text{lower}$ via branching, and the "stuff in $y, c$"
after Jacobi-Trudi becomes $t^q h_{p-q}(y,c)$ (for a 2-part $\mu' = (p, q)$
branching), the $s$-dependence enters only through $h_{p-q}(y,c)$. But
$h_k(y,c) = \sum_{a+2b=k} c_{a,b} s^a t^b$, so the $s$-degree of the
$t^{\text{top}}$-coefficient equals $a$ subject to $a + 2b = p - q$. For the
$t$-degree to be maximal (all $b$'s), we need $a = (p - q) \mod 2$; that's
either 0 (even, $\bar h_{p-q} = $ constant) or 1 (odd, $\bar h_{p-q} = c \cdot s$).

This is why the top-part image is 2-dimensional. It's the shadow of the fact
that $h_k$ has $\deg_t = \lfloor k/2 \rfloor$ but leading $s$-degree exactly
$k \mod 2$.

## Path to close identities (A) and (B)

Both identities look like sign-weighted sums of $K_{\mu', (2^j)}$ with signs
depending on $\mu_2 - \mu_3$ parity. Expected structure: **sign-reversing
involution on $\text{SSYT}(\mu', (2^j))$** that pairs up SSYT with different
$\mu_2 - \mu_3$ parities.

Candidates for the involution:
- Bender-Knuth involution (permutes content) — doesn't obviously touch shape.
- Column-swap involution on $\mu'$.
- Promotion or evacuation on the SSYT.
- Molev-Sagan barred/unbarred switch (from their factorial LR rule).

None obvious yet. Robin/Clio may have insight.

## Related "top-part depends on μ_2 - μ_3 only" phenomena in the literature

- **Vertex operator character formulas** (Kac, Frenkel): character of a
  representation as a "level-1 shifted" Verma module often has degree bounded
  by $\lambda_2 - \lambda_3$ in a specific variable.
- **Two-row Kostka-Foulkes** $\tilde K_{(\lambda_1, \lambda_2), (2^j)}(q)$ has
  known closed forms in $q$-degree $j(\lambda_1 - \lambda_2)$ range.
- **Duality functors** on shifted Schurs (Naprienko 2301.12110) may explain
  the 2-dim collapse via a boson-fermion correspondence.

## Files

- `beta-prime/notes/2026-08-20-day118-lemma-X-check.md` — full numerical study
  and derivation.
- `beta-prime/code/day118/verify_lemma_X.py` — verification code.
- `for-collaborator/2026-08-20-day118-double-star-proved.md` — Robin update.

## Meta

This is a **new master technique**: when the naïve filtration-adapted basis
fails, LOOK AT THE TOP PARTS EXPLICITLY. If they live in low-dim images with
clean parametric closed forms, the operator-level statement REDUCES TO
COMBINATORIAL CANCELLATION on the coefficient/multiplicity side.

Day 115's rule ("divisibility beats coefficient extraction") gets a sibling:
**"top-part explicit forms beat filtration-adapted bases when the basis fails."**

— Rick, Day 118, 2026-08-20
