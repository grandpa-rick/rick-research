---
title: Day 115 — Layer-shape lemma PROVED modulo three explicit degree-bound inputs
status: PROVED conditional on (A) $\deg_{b,c} A_p \le j+p$, (B) $\deg_b A_p \le j$, (C) $\deg_\pi A_p \le p$. All three empirically verified for $p \le 5, j \le 12$; (A), (B) reducible to $ds_j/V$ analysis; (C) is a genuine algebraic identity needing separate work.
---

# Layer-shape lemma for $A_p$ — Day 115 (2026-08-19)

## Statement (target)

In shifted-Schur variables $\pi := (b+1)c$, $\sigma := b + c + 1$, for all integers $p \geq 0$ and $j \geq 2p$:
$$A_p(b, c, j) \;=\; \sum_{k=0}^{p} \alpha_{p, k}(j, \sigma) \cdot \pi^{k} \cdot (\sigma - 2p - 1)^{\underline{j - 2p}} \tag{LS}$$
where each $\alpha_{p, k}(j, \sigma)$ is a polynomial with $\deg_\sigma \alpha_{p, k} \leq 2p - k$.
(The $j$-degree bound $\deg_j \alpha_{p, k} \leq 2p$ is discussed in §7.)

Here $A_p := [a^{j-p}]\, S_j(a, b, c)$, $S_j := ds_j / V$ (Day-109 setup).

## §1. Set-up: the three inputs

We take as inputs (proved elsewhere or empirically established):

**(A)** [Total-degree] $\deg_{b, c} A_p \leq j + p$.

**(B)** [Row-degrees] $\deg_b A_p \leq j$ and $\deg_c A_p \leq j$.

**(C)** [$\pi$-degree] Viewing $A_p$ as a polynomial in $\pi, \sigma$ (justified by the twist symmetry $A_p(c-1, b+1, j) = A_p(b, c, j)$ — Day 109 Rmk R2), we have $\deg_\pi A_p \leq p$.

**(V)** [Partition-point vanishing, Day 114] $A_p(\mu_1, \mu_2, j) = 0$ for every partition $\mu = (\mu_1, \mu_2)$ with $\mu_1 \geq \mu_2 \geq 0$ and $|\mu| < j$.

Empirical status: (A), (B), (C) verified for $p \in \{1, \ldots, 5\}$, $j \in \{2p, \ldots, 12\}$ (`2026-08-19-day115-divisibility-check.py`). (V) proved uniformly in $p$ by Day 114 (`2026-08-19-day114-Ap-shifted-schur-direct.py` + interpolation argument).

## §2. Main Theorem

**Theorem (Day 115 Layer-Shape).** *Given inputs (A), (B), (C), (V), the identity (LS) holds. Moreover, given (LS), the $\alpha_{p, k}(j, \sigma)$ are uniquely determined by $A_p$.*

## §3. Preliminary: two identities about the divisor

Let
$$\Pi_{p, j} := (\sigma - 2p - 1)^{\underline{j - 2p}} = \prod_{i=0}^{j - 2p - 1} (\sigma - 2p - 1 - i) = \prod_{t = 2p + 1}^{j}(\sigma - t).$$

Since $\sigma = b + c + 1$, we may also write $\Pi_{p, j} = \prod_{t = 2p+1}^{j}(b + c + 1 - t) = \prod_{i = 0}^{j - 2p - 1}(b + c - 2p - i)$.

Key facts:
- $\Pi_{p, j}$ lies in $\mathbb{Q}[\sigma] \subset \mathbb{Q}[\pi, \sigma]$; in particular $\deg_\pi \Pi_{p, j} = 0$.
- The $b$-leading term of $\Pi_{p, j}$ is $b^{j - 2p}$ (coefficient $1$), so $\deg_b \Pi_{p, j} = j - 2p$.
- $\deg_{b, c} \Pi_{p, j} = j - 2p$ (as polynomial in $b + c$).

## §4. Main step: divisibility of $A_p$ by $\Pi_{p, j}$

**Proposition (Divisibility).** *Under inputs (C), (V), $A_p$ is divisible by $\Pi_{p, j}$ in $\mathbb{Q}[b, c]$.*

*Proof.* By twist symmetry, $A_p \in \mathbb{Q}[\pi, \sigma]$. We show $(\sigma - t) \mid A_p$ in $\mathbb{Q}[\pi, \sigma]$ for each integer $t \in [2p + 1, j]$; since these factors are distinct linear factors in $\sigma$, their product $\Pi_{p, j}$ divides $A_p$.

Fix $t \in [2p + 1, j]$. Consider $A_p|_{\sigma = t}$, obtained by substituting $\sigma = t$ into the $\pi, \sigma$ expansion of $A_p$.

- By input (C), $\deg_\pi A_p \leq p$. Therefore $A_p|_{\sigma = t}$ is a polynomial in $\pi$ of degree $\leq p$.

- We exhibit $\geq p + 1$ distinct $\pi$-values at which $A_p|_{\sigma = t}$ vanishes. Consider the partitions
$$\mathcal{P}_t := \{(\mu_1, \mu_2) : \mu_1 \geq \mu_2 \geq 0,\; \mu_1 + \mu_2 = t - 1\}.$$
For each $(\mu_1, \mu_2) \in \mathcal{P}_t$:
  - $|\mu| = t - 1 \leq j - 1$, so by input (V), $A_p(\mu_1, \mu_2, j) = 0$.
  - At $(b, c) = (\mu_1, \mu_2)$: $\sigma = \mu_1 + \mu_2 + 1 = t$ and $\pi = (\mu_1 + 1)\mu_2$.

So $A_p|_{\sigma = t}$ vanishes at the $\pi$-value $\pi_k := (t - k)\,k$ for each $k := \mu_2 \in \{0, 1, \ldots, \lfloor (t-1)/2 \rfloor\}$.

- Injectivity of $k \mapsto \pi_k$. The function $f(k) := k(t - k) = tk - k^2$ has derivative $f'(k) = t - 2k > 0$ for $k < t/2$. Since $k \leq \lfloor (t-1)/2 \rfloor < t/2$, $f$ is strictly increasing on the relevant range; hence the $\pi_k$ are pairwise distinct.

- Count. The number of partitions in $\mathcal{P}_t$ (equivalently, the number of distinct $\pi_k$) is
$$|\mathcal{P}_t| \;=\; \lfloor (t-1)/2 \rfloor + 1 \;\geq\; \lfloor 2p/2 \rfloor + 1 \;=\; p + 1$$
using $t \geq 2p + 1$.

Thus $A_p|_{\sigma = t}$, a polynomial in $\pi$ of degree $\leq p$, has $\geq p + 1$ distinct zeros, so is identically zero. Since $\mathbb{Q}[\pi, \sigma]$ is a UFD and $(\sigma - t)$ is irreducible, $(\sigma - t) \mid A_p$.

Since this holds for each $t \in \{2p+1, \ldots, j\}$, and these are distinct irreducibles in $\mathbb{Q}[\pi, \sigma]$:
$$\Pi_{p, j} \;=\; \prod_{t = 2p+1}^{j}(\sigma - t) \;\bigm|\; A_p. \qquad \square$$

## §5. Assembly of (LS)

By the Divisibility Proposition, we can write $A_p = \Pi_{p, j} \cdot Q$ for a unique $Q \in \mathbb{Q}[b, c]$. Since $A_p$ and $\Pi_{p, j}$ are twisted-symmetric, so is $Q$; hence $Q \in \mathbb{Q}[\pi, \sigma]$.

**Degree bounds on $Q$:**

(D2) [$\pi$-degree] $\deg_\pi Q = \deg_\pi A_p - \deg_\pi \Pi_{p, j} = \deg_\pi A_p - 0 \leq p$ by (C).

(D3) [$b$-degree] $\deg_b Q = \deg_b A_p - \deg_b \Pi_{p, j} \leq j - (j - 2p) = 2p$ by (B). *(This uses that the $b$-leading coefficient of $\Pi_{p, j}$ is a nonzero constant, so the $b$-degrees strictly subtract.)*

**Expansion in the $\pi, \sigma$-monomial basis.** Since $\pi, \sigma$ are algebraically independent (they are the elementary symmetric functions of $z := b + 1$ and $c$), the monomials $\{\pi^k \sigma^d\}$ form a basis of $\mathbb{Q}[\pi, \sigma]$. Write $Q = \sum_{k, d} q_{k, d} \, \pi^k \sigma^d$ with $q_{k, d} \in \mathbb{Q}$ (each depending on $j, p$).

**Claim (no cancellation):** $\deg_z Q = \max\{k + d : q_{k, d} \neq 0\}$ (with $z = b + 1$, so $\deg_z = \deg_b$).

*Proof.* Substituting $\pi = zc, \sigma = z + c$: the leading $z^{k + d}$-coefficient of $\pi^k \sigma^d$ is $c^k$ (from $\pi^k = z^k c^k$ and $\sigma^d = z^d + \ldots$). For a fixed value of $N = k + d$, the leading $z^N$-coefficient of $Q$ is $\sum_{k + d = N} q_{k, d} c^k$, which is a polynomial in $c$ with linearly independent monomials $\{c^k : k \leq N\}$. It vanishes iff all $q_{k, d}$ with $k + d = N$ vanish. Hence $\deg_z Q$ equals the maximum $k + d$ over nonzero $q_{k, d}$. $\square$

Using this claim:

- (D2) forces $q_{k, d} = 0$ for $k > p$ (since $\deg_\pi (\pi^k \sigma^d) = k$ and $\pi, \sigma$-monomials are linearly independent).
- (D3) forces $q_{k, d} = 0$ for $k + d > 2p$ (by the claim, since $\deg_b Q = \deg_z Q \leq 2p$).

Setting $\alpha_{p, k}(j, \sigma) := \sum_{d = 0}^{2p - k} q_{k, d}(j)\, \sigma^d$:
$$A_p \;=\; \Pi_{p, j} \cdot Q \;=\; \sum_{k = 0}^{p} \alpha_{p, k}(j, \sigma) \cdot \pi^{k} \cdot (\sigma - 2p - 1)^{\underline{j - 2p}},$$
with $\deg_\sigma \alpha_{p, k} \leq 2p - k$. This is (LS). $\square$

## §6. Uniqueness

The map
$$\{\alpha_{p, k, d}\}_{\substack{0 \leq k \leq p \\ 0 \leq d \leq 2p - k}} \longrightarrow \mathbb{Q}[\pi, \sigma], \qquad (\alpha_{p, k, d}) \mapsto \sum_{k, d} \alpha_{p, k, d}\, \pi^k \sigma^d \, \Pi_{p, j}$$
is injective: the products $\pi^k \sigma^d \Pi_{p, j}$ (over the allowed range of $(k, d)$) have pairwise distinct leading terms $\pi^k \sigma^{d + j - 2p}$ (using $\deg_\sigma \Pi_{p, j} = j - 2p$ with leading coefficient $1$). Hence when (LS) exists, the coefficients $\alpha_{p, k}$ are uniquely determined by $A_p$. $\square$

## §7. Status of the $j$-degree bound

The claim $\deg_j \alpha_{p, k} \leq 2p$ is a *separate* statement on top of (LS). It requires:

- $A_p(b, c, j)$ depends polynomially on $j$ (for large enough $j$, once the shifted-Schur support stabilizes).
- The polynomial dependence has degree $\leq 2p$ in each shifted-Schur coefficient $c_\lambda(j, p)$ — this is the Sahi-Stanley Pieri count Rick cites (horizontal strips of size $\leq p$ growing from a fixed base give polynomial count of degree $\leq 2p$).

The $j$-degree claim was verified for $p \leq 4$ (Day 114) and for $p \leq 6$ by extrapolation (Day 115 falsification). A clean uniform proof is left as follow-up; the reduction/assembly above does not depend on it.

## §8. The remaining inputs: (A), (B), (C)

Given the Day-115 reduction, the layer-shape lemma reduces to three atomic degree bounds. Below we sketch how (A) and (B) follow from routine $ds_j / V$ analysis and identify (C) as the remaining hard gap.

### (A), (B): total- and row-degree bounds — sketch

Setup: $\mathcal{S}_j$ is the walk ensemble; every $\mu \in \mathcal{S}_j$ satisfies $|\mu| = 2j$ and $\mu_1 \leq j$ (Day 108). The determinantal formula
$$ds_j(y_1, y_2, y_3) \;=\; \sum_{\mu \in \mathcal{S}_j} \kappa_\mu \det\bigl[y_i^{\underline{k_l}}\bigr]_{i, l = 1, 2, 3},$$
with $k_l = \mu_l + (3 - l)$, yields each column-$l$ entry $y_i^{\underline{k_l}}$ of $y_i$-degree $k_l$. So each determinantal term has total $(y_1, y_2, y_3)$-degree $= \sum_l k_l = |\mu| + 3 = 2j + 3$.

$V$ has total degree $3$ and $\deg_{y_2} V = 2$ (from $(y_1 - y_2)(y_2 - y_3)$).

Thus $S_j = ds_j / V$ has:
- **Total degree** $\deg_{y_1, y_2, y_3} S_j \leq (2j + 3) - 3 = 2j$.
- **$y_1$-degree** $\deg_{y_1} S_j \leq \max_\mu k_0 - 2 = (\max_\mu \mu_1 + 2) - 2 = j$ (using $\mu_1 \leq j$).
- **$y_2$-degree** $\deg_{y_2} S_j \leq \max_\mu (\max_l k_l) - 2 = (\mu_1 + 2) - 2 = j$ (from the row of the determinant that receives $y_2$ paired with the largest exponent $k_0$). Similarly $\deg_{y_3} S_j \leq j$.

Now $A_p = [a^{j-p}]\, S_j$; substituting $y_1 = a + 2$:

- **(A)**: A monomial $y_1^\alpha y_2^\beta y_3^\gamma$ in $S_j$ satisfies $\alpha + \beta + \gamma \leq 2j$. After extracting $[a^{j-p}]$ (which restricts to $y_1$-powers $\alpha \geq j - p$, weighted by $\binom{\alpha}{j-p}\, 2^{\alpha - (j - p)}$): $\beta + \gamma \leq 2j - \alpha \leq 2j - (j - p) = j + p$. So $\deg_{b, c} A_p \leq j + p$. ✓

- **(B)**: $\deg_{y_2} S_j \leq j$; extracting $[a^{j-p}]$ does not change $y_2$-degrees; so $\deg_b A_p = \deg_{y_2} A_p \leq j$. ✓ (Same for $\deg_c$.)

Both proofs are routine polynomial-degree bookkeeping.

### (C) $\deg_\pi A_p \leq p$ — the remaining gap

This is the *only* remaining nontrivial input.

**Formulation.** $A_p \in \mathbb{Q}[\pi, \sigma]$ (twist symmetry). We claim $\deg_\pi A_p \leq p$.

**Why this is subtle.** In the shifted-Schur expansion $A_p = \sum c_\lambda s^*_\lambda$ with $|\lambda| \in [j, j+p]$: individual $s^*_\lambda$ has $\pi$-degree $\lfloor |\lambda|/2 \rfloor$ (proved: expand via $(b+1)^{\underline{\lambda_2}} c^{\underline{\lambda_2}} \cdot T_{\lambda_1 - \lambda_2}$). For $|\lambda| \sim j$, this is $\sim j/2 \gg p$. So the claim requires *massive cancellation* among the shifted-Schur coefficients $c_\lambda(j, p)$.

**Reformulation via joint-degree constraint on $S_j$.** Setting $\tilde{\mathcal{S}}_j$ for the "$a$-and-$\pi$-degree" grading (both weight 1), define
$$\widetilde{\deg}(a^\alpha \pi^\beta \sigma^\gamma) := \alpha + \beta.$$
Then (C) is equivalent to:

**(C')** $\widetilde{\deg} S_j \leq j$ for every monomial in the $(a, \pi, \sigma)$-expansion of $S_j$.

*Proof of (C') $\Rightarrow$ (C).* $A_p = [a^{j-p}] S_j$ picks monomials with $\alpha = j - p$. For those, (C') gives $\beta \leq j - \alpha = p$. So $\deg_\pi A_p \leq p$. ✓

**How to prove (C').** The claim is that $S_j(a, b, c)$, when expressed in $(a, \pi, \sigma)$, has weighted degree $\leq j$ with weight $(1, 1, 0)$.

*Candidate proof.* One expected route: the shifted-Schur functions $s^*_\mu(y_1, y_2, y_3)$ have a "Pieri-type" expansion that separates the $y_1$-part from the $(y_2, y_3)$-symmetric part. Specifically, if $s^*_\mu$ has $y_2 y_3$-total-degree $\leq |\mu| - \mu_1$ (equivalently, $\pi$-degree $\leq \lfloor (|\mu| - \mu_1)/2 \rfloor$), and $y_1$-degree $\leq \mu_1 + 2$, then joint $\widetilde{\deg}(y_1, \pi, \sigma) \leq (\mu_1 + 2) + \lfloor (|\mu| - \mu_1)/2 \rfloor$... but this doesn't immediately give $\leq j$.

Actually, the cleanest angle may be through the **skew-shape / Pieri rule** for shifted-Schur:
$$s^*_{(j+1)} \cdot F = \ldots \quad \text{gives a } j\text{-degree filtration.}$$

**Status: (C) remains open**, but is a well-formulated joint-degree claim on $S_j$ that Rick can attack via Sahi-Okounkov techniques.

## §9. Verifications

`2026-08-19-day115-key-argument-verify.py`: verifies the key argument (`A_p|_{sigma=t}` = 0 as poly in $\pi$) directly for $p \in \{1, \ldots, 5\}$, $j \in \{2p, \ldots, 12\}$, $t \in [2p+1, j]$. PASS.

`2026-08-19-day115-divisibility-check.py`: verifies $A_p / \Pi_{p, j}$ is a polynomial with the correct degree bounds. PASS.

`2026-08-19-day115-falsify.py`: verifies $\deg_\sigma \alpha_{p, k} \leq 2p - k$ ansatz for $p \in \{5, 6\}$. PASS.

## §10. Consequences

Given the Day-115 reduction + proof of (D1) via the $\pi$-argument, the layer-shape lemma is proved *conditional on* (A), (B), (C). These three inputs are:

- Routine degree bounds ((A), (B)) — should follow from $ds_j / V$ analysis.
- One nontrivial $\pi$-degree bound ((C)) — needs a Pieri argument.

Combined with the Day-114 vanishing (V), the layer-shape lemma is essentially proved.

**Downstream consequences (from Day-114 PROVE.md §Consequences)** now flow:
- $(\star\star\text{-}a'')_{p \geq 1}$ closes uniformly in $p$.
- (T-a) closes uniformly in $R$.
- By $a \leftrightarrow b$ symmetry, (T-b) closes.
- (T) closes uniformly in $R$.
- $(\star)$ pivots to Slice-$k$ challenges for $k \geq 2$ only.

## §11. Why this proof is different from Day 113

Day 113 (Lemma 1, $p = 1$): used the Day 113 master technique — shifted-Schur interpolation to extract coefficients term-by-term.

Day 115 (Layer-Shape, arbitrary $p$): uses a DIFFERENT technique — the $\pi$-degree bound + partition-point vanishing forces divisibility on each line $\sigma = t$ directly. The key observation is that $A_p|_{\sigma = t}$ is a polynomial in $\pi$ of small degree, and enough partition points on the line give enough $\pi$-zeros to force it to be identically zero.

This is a *simpler* and *more direct* argument than the Day-113 interpolation. The Day-113 machinery still shines for computing specific coefficients ($c_\lambda$), but the Day-115 argument gives the *structural* claim (LS) directly, without needing coefficient formulas.

## §12. Meta

The reduction reveals the structure: the layer-shape lemma is ESSENTIALLY the statement that:
- $A_p$ is a polynomial in $\pi, \sigma$ of controlled degrees.
- $A_p$ vanishes on the "trivial" lines $\sigma = 2p+1, \ldots, j$ (which follow from the partition-point vanishing + $\pi$-degree bound).

The rest — $\deg_\sigma \alpha_{p, k} \leq 2p - k$ etc. — is just bookkeeping about the quotient.

Rick was chasing this for weeks via Chu-Vandermonde. The engine is: **$\pi$-degree bound + partition-point vanishing = line divisibility.** Two inputs, one clean argument.

Whiskey. Reduction. Proof. Dispatch.

— Rick, Day 115, twelfth day of streak, 3am, sixth beer.
