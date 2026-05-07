# The spin-shift mechanism: why bigraded BGG–Verma is acyclic for spin λ in type B

**Status (2026-05-07):** Phenomenon empirically nailed in B_2 and B_3 (200/200 spin pairs at λ_1 ≤ 7/2). Mechanism partially understood (regular-orbit picture solid; "support absorption" is the right shape). Structural proof open. Three attack vectors sketched.
**Author:** Rick.
**Antecedents:** `2026-05-06-remark-47-obstruction.md` (B_2 obstruction, dual problem); `2026-05-07-B3-acyclicity-test.md` (B_3 verification); `memory/connections/acyclicity-is-positivity.md`; `memory/questions/q-KL-from-crystal.md`.

---

## 1. Setup

Type B_n: long positive roots $R^+_L = \{e_i \pm e_j\}_{i<j}$ ($n(n-1)$ total), short $R^+_S = \{e_i\}$ ($n$ total). $\rho = (n-\tfrac12, \dots, \tfrac12) \in \tfrac12(1,\dots,1) + \mathbb Z^n$ — half-integer. $W = (\mathbb Z/2)^n \rtimes S_n$. Dot action: $w\!\cdot\!\lambda := w(\lambda+\rho) - \rho$. Bigrade $\mathrm{Sym}(\mathfrak n_+)$ by long-root degree $q$, short-root degree $t$; the (q,t)-Kostant function $K_{q,t}(\beta)$ equals $\dim_{q,t} M(w\!\cdot\!\lambda)_\mu$ for $\beta = w\!\cdot\!\lambda - \mu$. Then (Theorem 3.1 of the Remark-4.7 note):

$$\boxed{\;\mathrm{KL}^{B_n}_{\lambda,\mu}(q,t) = \sum_w (-1)^{\ell(w)}\, K_{q,t}(w\!\cdot\!\lambda - \mu) = \chi_{q,t}\bigl(\mathrm{BGG}^\bullet(\lambda)_\mu\bigr) = \mathcal E^+ - \mathcal E^-,\;}$$

where $\mathcal E^\pm$ collect even/odd-length Verma weight-spaces. Positivity ⟺ **bigraded acyclicity**: $\mathcal E^- \le \mathcal E^+$ pointwise.

## 2. The phenomenon

**Spin lattice.** $\Lambda^{\mathrm{spin}} := \tfrac12(1,\dots,1) + \mathbb Z^n$ (half-integer coordinates). For $\lambda \in \Lambda^{\mathrm{spin}}$ dominant, $\lambda + \rho$ is *integer*, so $w(\lambda+\rho) \in \mathbb Z^n$ for every $w$, hence $w\!\cdot\!\lambda = w(\lambda+\rho) - \rho \in \Lambda^{\mathrm{spin}}$. For $\mu \in \Lambda^{\mathrm{spin}}$ the difference $w\!\cdot\!\lambda - \mu \in \mathbb Z^n$ — necessary for any Kostant decomposition over the (integer) root lattice.

**Spin acyclicity claim (the phenomenon).**

> For every $\lambda \in \Lambda^{\mathrm{spin}}$ dominant and every $\mu \in \Lambda^{\mathrm{spin}}$, the bigraded BGG–Verma complex $\mathrm{BGG}^\bullet(\lambda)_\mu$ is **acyclic in positive bigraded degrees**. Equivalently:
>
> $$\sum_{\ell(w)\,\text{odd}} \mathrm{mult}^{i,j}_{w\cdot\lambda}(\mu) \;\le\; \sum_{\ell(w)\,\text{even}} \mathrm{mult}^{i,j}_{w\cdot\lambda}(\mu) \qquad \text{at every bidegree } (i,j) \in \mathbb Z^2_{\ge 0}.$$

This is the conjectural strengthening of CKL Theorem 4.6 (positive (q,t)-energy formula on spin B) to the *bigraded* level: not just the alternating sum, but every individual bidegree, is dominated.

## 3. Empirical evidence

* **B_2** (Remark-4.7 note §4.2.1): 5 representative spin pairs, all clean. E.g. $\lambda^\sharp = (5/2,1/2),\,\mu^\sharp = (1/2,1/2)$: $\beta_{s_2} = (2,-2)$, $K_{q,t} = q^2$, support $\{(2,0)\} \subset \{(0,2),(1,2),(2,0),(2,2)\}$ = $M(\lambda^\sharp)_{\mu^\sharp}$ support.
* **B_3** (`bgg_decomposition_B3.py`, results `B3_results.md`, summary `2026-05-07-B3-acyclicity-test.md`): **200/200** non-trivial dominant spin pairs with $\lambda_1 \le 7/2$ acyclic-and-positive. Compare integer side: 94/200 = 47% non-acyclic-negative. Clean, total split.

Rank jump 2→3: $|W|$ goes 8→48, $|R^+|$ goes 4→9 — many more odd-length Vermas, many more chances for a bidegree to escape. Nothing escaped. Empirical anchor.

## 4. The structural why — what we know and what we're guessing

### 4.1 Regularity of the orbit (solid)

For $\lambda \in \Lambda^{\mathrm{spin}}$ dominant, $\lambda+\rho \in \mathbb Z^n$ generically has **all coordinates distinct and nonzero**, hence its W-stabilizer is trivial: the orbit $W\cdot(\lambda+\rho)$ has full size $|W| = 2^n n!$. So all $2^n n!$ Vermas $M(w\!\cdot\!\lambda)$ are *distinct*. (For non-spin $\lambda$, $\lambda+\rho$ is half-integer and similarly generically regular, so this regularity is *not* what distinguishes spin from non-spin. It's necessary but not sufficient.)

### 4.2 The half-integer offset shifts supports into alignment

The mechanism in concrete terms: take a non-spin negative case and its spin partner ($\lambda, \mu$ both shifted by $(\tfrac12,\dots,\tfrac12)$):

* **Non-spin** $(2,0)\to(0,0)$: $\beta_{s_2} = (2,-1)$, support $\{(1,1),(2,1)\}$ — **disjoint** from $M(\lambda)_\mu$ support $\{(0,2),(1,2),(2,0),(2,2)\}$. Negative.
* **Spin** $(5/2,1/2)\to(1/2,1/2)$: $\beta_{s_2} = (2,-2)$, support $\{(2,0)\} \subset$ even-length support. Positive.

The half-shift moves $\mu$ in the *short-root direction* (each $e_i$ shifts by $\tfrac12$), reducing $\beta_w$'s short-root demand for the offending odd-length $w$ enough to push it from "needs short roots to decompose" into "purely long-root" — which is already in the even-length support. Works in every spin B_2/B_3 example. **Why uniformly?** That's what we're after.

### 4.3 Three candidate structural explanations

**(a) Schur–Weyl / spin-tensor factorization (speculative).** The basic spinor $V(\sigma) = V(\tfrac12,\dots,\tfrac12)$ has dimension $2^n$. Naive factorization $V(\lambda^\sharp) \cong V(\sigma)\otimes V(\lambda^\sharp-\sigma)$ is *false* (the RHS decomposes into many spin irreducibles). But a categorified version may hold: $V(\sigma)$ is essentially the projective generator on the spin block of category $\mathcal O$, and projection onto the $\lambda^\sharp$-isotypic should split BGG$(\lambda^\sharp)$ off $V(\sigma)\otimes \mathrm{BGG}(\lambda^\sharp - \sigma)$. Since $V(\sigma)$ is a finite-dim irrep (rigid bigrading), tensoring against the integer-side acyclic BGG and projecting would force bigraded acyclicity. Conjectural; the bigrading compatibility is the unproven step.

**(b) Kostant spin character formula (most concrete lead).** The classical identity $\mathrm{ch}\,V(\sigma) = \prod_{\alpha\in R^+}(1 + e^{-\alpha})$ exhibits the spinor character as a sum-over-subsets-of-roots with positive coefficients. The spin shift $\lambda \mapsto \lambda + \sigma$ in our setup *is* the shift by the spinor highest weight, so whatever cancellation this identity performs at the character level, the spin-shifted BGG complex inherits at the bigraded-multiplicity level. The precise target:

$$\sum_w (-1)^{\ell(w)}\, K_{q,t}(w\!\cdot\!\lambda^\sharp - \mu^\sharp) = (\text{positive expression in } q, t)$$

via a re-indexing that pairs odd-length supports against even-length supports. **This is what an actual proof should look like.** Pairing not yet constructed.

**(c) The "support absorption" lemma directly.** The blunt combinatorial form:

> **(SA)** *For every spin $\lambda$, spin $\mu$, every odd-length $w \in W$, and every bidegree $(i,j)$ with $K_{q,t}^{(i,j)}(w\!\cdot\!\lambda - \mu) \ge 1$: there exists even-length $w'$ with $K_{q,t}^{(i,j)}(w'\!\cdot\!\lambda - \mu) \ge 1$.*

Strong version: a multiplicity-respecting matching $w \mapsto w'$ per bidegree. (SA) is exactly what B_3's 200/200 verifies pointwise. Proof would reduce to Kostant-decomposition combinatorics of half-shifted root-lattice elements — most likely via induction on $\ell(w)$ or a sign-reversing involution.

Honest: **I don't know yet why spin acyclicity holds.** What I have is the regular-orbit picture (necessary), the local "half-shift aligns supports" mechanism, and three candidate routes; (b) feels closest, (a) most ambitious.

## 5. What B_3 added

1. **Scope:** 200 spin pairs at $\lambda_1 \le 7/2$, 100% acyclic. Mechanism robust at rank $\ge 3$.
2. **Integer-side closed form breaks; spin-side does not.** B_2's "$\lambda = (k,k)$" positivity criterion (long-highest-root ray, $\mu = 0$) does *not* lift: B_3's $(k,k,0)$ fails — $(1,1,0)\to(0,0,0)$ is non-acyclic-negative. Spin criterion ($\lambda \in \Lambda^{\mathrm{spin}}$) is rank-uniform. Structural evidence that spin positivity is a *different* phenomenon from lucky integer positivity, not a continuation.
3. **The $t - q + qt$ residue.** Three distinct B_3 integer pairs produce *exactly* the Remark-4.7 polynomial — a "single long-root mismatch" residue. Their spin partners are positive. Spin shift kills these uniformly.

## 6. Open program

(a) **Prove (SA).** Likely route: the (q,t)-refined Kostant spin-character identity (§4.3.b), re-indexed to give term-by-term dominance of even over odd. Write the half-shifted alternating sum as a determinant/Pfaffian/positive-Schur expansion.

(b) **Type D.** CKL leaves type-D Lusztig multiplicity open. The acyclicity-is-positivity framework predicts a type-D "spin lattice" whose half-shift gives bigraded acyclicity. `bgg_decomposition_B3.py` ports almost verbatim. **Concrete next experiment.**

(c) **CKL Theorem 4.6's proof.** Their positive (q,t)-energy formula must implicitly use bigraded acyclicity somewhere; re-read with that lens to extract the mechanism.

(d) **Almousa–Lu bridge** (`acyclicity-is-positivity.md`): if (SA) lifts to an actual acyclic complex of indecomposable projectives over an affine-Hecke-tower-style algebra, that's the type-B analog of $\mathcal C(\vec\alpha)$ — the positive endpoint in the dichotomy.

---

## 7. Honest assessment

* **Solid:** the phenomenon (200/200 B_3, all B_2 examples), the BGG/WCF reformulation, the regular-orbit observation, the local "half-shift aligns Kostant supports" mechanism in every spin example computed.
* **Conjectural:** the uniform (SA) lemma, the Schur–Weyl-style factorization, the Kostant-identity-based pairing, type-D.
* **Don't know:** the structural proof. Right next move: write the (q,t)-Kostant spin-character identity explicitly and see if it directly furnishes the bidegree-by-bidegree pairing.
