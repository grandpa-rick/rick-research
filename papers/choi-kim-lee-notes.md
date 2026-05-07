# Notes on Choi–Kim–Lee, "Lusztig q-weight multiplicities and Kirillov–Reshetikhin crystals"

**arXiv:** 2412.20757 (v2, 26 Jan 2025)
**Authors:** Hyeonjae Choi, Donghyun Kim, Seung Jin Lee
**PDF:** `/home/agent/projects/papers/choi-kim-lee-2412.20757.pdf`

---

## 1. Bird's-eye view (Abstract + Introduction)

The paper provides a **positive combinatorial formula** for the **Lusztig q-weight multiplicity**

$$\operatorname{KL}^{\mathfrak{g}_n}_{\lambda,\mu}(q) = \sum_{w\in W} (-1)^w [e^{w(\lambda+\rho)-(\mu+\rho)}]\prod_{\alpha\in R^+}\frac{1}{1-q\, e^\alpha}$$
(equation (1.2) with $L\equiv 1$, denoted $\operatorname{KL}^{\mathfrak{g}_n}_{\lambda,\mu}(q)$),

at $q=1$ this is the ordinary weight multiplicity $\dim V(\lambda)_\mu$. **Nonnegativity is known via affine Kazhdan–Lusztig polynomials [Lus83]** but no positive combinatorial formula was known beyond type $A$.

In type $A_{n-1}$ this is the Kostka–Foulkes polynomial, equipped with the charge statistic of Lascoux–Schützenberger.

**Main contribution.** They prove:
- (Type $C$, dominant weights) $\operatorname{KL}^{C_n}_{\lambda,\mu}(q) = \sum_T q^{\overline{D}(\phi_c(T))}$ over generalized semistandard oscillating tableaux (Theorem 4.1).
- (Type $B$, dominant **spin** weights) a $q,t$-version $\operatorname{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t)$ is a sum of $q,t$-energies over GSSOT (Theorem 4.6).
- A "level-restricted" $q$-weight multiplicity for $B$, $C$, $D$, also given by KR-energy (Theorem 5.4).

The energy comes from the **affine combinatorial $R$-matrix on Kirillov–Reshetikhin (KR) crystals**.

---

## 2. The Energy Function (the core definition)

### Local energy $\overline{H}$ on $B_2 \otimes B_1$ (page 5, item (2))

For each pair of KR crystals $B_1, B_2$ in the category $\mathscr{C}$ (tensor products of KR crystals) there is a unique (up to additive constant) **local energy function** $\overline{H} = \overline{H}_{B_2,B_1}: B_2\otimes B_1 \to \mathbb{Z}$, characterized by:

- $\overline{H}$ is constant on each classical component (each $J$-component, where $J$ are the finite Dynkin nodes);
- under the affine $0$-arrow $e_0$,
$$\overline{H}(e_0(b_2\otimes b_1)) = \overline{H}(b_2\otimes b_1) + \begin{cases} +1 & \text{if LL}\\ -1 & \text{if RR}\\ 0 & \text{otherwise}\end{cases}$$
where for $b_2\otimes b_1\in B_2\otimes B_1$ and $R(b_2\otimes b_1) = b_1'\otimes b_2'\in B_1\otimes B_2$, "LL" (resp. "RR") means $e_0$ acts on the **left** (resp. **right**) factor in **both** representations.

### Global energy $\overline{D}_B$ on a tensor product (page 6, eq. (2.7) and the recursive formula)

For a single KR crystal $B^{r,s}(\diamond)$ and $b\in B(\lambda)$ (where $B^{r,s}(\diamond) = \bigoplus_\lambda B(\lambda)$):
$$\overline{D}_{B^{r,s}(\diamond)}(b) = \frac{rs - |\lambda|}{|\diamond|}\quad\text{(eq. 2.7)}.$$

For $B = B_n\otimes\cdots\otimes B_1$ with $b = b_n\otimes\cdots\otimes b_1$:
$$\boxed{\;\overline{D}_B(b) = \sum_{1\le i<j\le n}\overline{H}(b_j^{(i+1)}\otimes b_i) + \sum_{j=1}^n \overline{D}_{B_j}(b_j^{(1)})\;}$$
where $b_j^{(i)}\in B_j$ is determined by sliding via the combinatorial $R$-matrices:
$$B_j\otimes\cdots\otimes B_{i+1}\otimes B_i \xrightarrow{R\cdots R} B_{j-1}\otimes\cdots\otimes B_i\otimes B_j,\qquad b_j\otimes\cdots\otimes b_{i+1}\otimes b_i\mapsto b_{j-1}'\otimes\cdots\otimes b_i'\otimes b_j^{(i)}.$$

In words: **slide each $b_j$ all the way to the rightmost position by repeatedly applying the combinatorial $R$-matrix; sum the local energies of the consecutive pairs along this sliding; add a "single-tensor" correction.**

### Explicit formula on $b\in (B^{1,1}(\diamond))^{\otimes n}$ (page 7)

Write $b = b_n\otimes\cdots\otimes b_1$ with each $b_i$ a single letter (or empty word $\emptyset$, allowed only when $\diamond=\square$ in row case). Then:

- For $\diamond \in \{\square\square,\textsf{B}\}$ (column KR for $C_n$ and the spin column for $B_n^{(1)}$):
$$\overline{D}(b) = \sum_{i=1}^{n-1}(n-i)\,\overline{H}_\diamond(b_{i+1},b_i)$$
where (for $\diamond=\textsf{B}$, type $B_n^{(1)}$ spin column)
$$\overline{H}_\textsf{B}(x,y) = \begin{cases}2 & x=\bar 1,\ y=1\\ 1 & x>y\ \text{and}\ (x,y)\ne(\bar1,1)\\ 0 & x\le y\end{cases}$$
(and $\overline{H}_{\square\square}(x,y)=1$ if $x>y$, else $0$).
- For $\diamond=\square$ (row case, type $A_{N-1}^{(1)}$):
$$\overline{D}(b) = \sum_{i=1}^{n-1}2(n-i)\overline{H}_\square(b_{i+1},b_i) + \mathrm{vac}$$
where $\mathrm{vac}$ is the count of $\emptyset$'s. **For $\diamond=\emptyset$ (type $A_{N-1}^{(1)}$) this reproduces Lascoux–Schützenberger charge.**

### Vacancy and $q,t$-energy (for type $B$ spin, page 15)

For $v\in B^{r,1}(\square\square)$ in $B(\omega_s)$ (with $0\le s\le r$), $\mathrm{vac}(v) := r - s$. Extend additively to tensors. Then
$$\mathrm{energy}_{q,t}(b) := q^{(\overline{D}(b)-\mathrm{vac}(b))/2}\, t^{\mathrm{vac}(b)}.$$

This is the statistic in Theorem 4.6.

---

## 3. The Splitting Map (page 8)

A **classical-crystal embedding** $S_\mu: \otimes_i B^{r_i,s_i}\hookrightarrow (B^{1,1})^{\otimes \sum r_is_i}$ that **preserves $\overline{D}$ up to an explicit global shift** (Lemmas 2.1, 2.4). It is a "generalized standardization map" extending Lascoux's standardization which preserves cocharge.

This is the workhorse: although in general $\overline{D}$ is hard to compute, on $(B^{1,1})^{\otimes n}$ it is the explicit nearest-neighbor sum above. The splitting map reduces all energy computations to this simple form.

---

## 4. Combinatorial Objects (Section 3)

Three classes of tableaux indexed by triples of partitions:

- **SSOT** (semistandard oscillating tableaux): sequences $T=(T_1,\dots,T_n)$ where each $T_i = (\mu_{i-1},\nu_i,\mu_i)$ is an oscillating horizontal strip; $\nu_i/\mu_{i-1}$ and $\nu_i/\mu_i$ horizontal strips of total size $|\nu_i/\mu_{i-1}|+|\nu_i/\mu_i|=\mu_i$.
- **GSSOT** (generalized SSOT): same, but total size $=\mu_i$ or $\mu_i-1$ (allowing one "ghost cell"). Used in type $B$ spin case.
- **SSROT** (reverse OT): the dual where $\mu/\nu$ are horizontal strips. Used in type $D$ level-restricted.

Each carries a $g$-bound $c(T)\le g$. Lemmas 3.5, 3.7 give bijections to **classical highest weight elements** in the appropriate KR crystal; the bijection $\phi_c$ is the engine of the main theorems.

The bijection $\phi_c$ is described as: $\phi_c(T) = \mathrm{red}(\mathrm{cind}(T_n))\otimes \cdots\otimes \mathrm{red}(\mathrm{cind}(T_1))$, where $\mathrm{cind}$ records column indices of the oscillating strip and $\mathrm{red}$ "reduces" by deleting non-admissible $i,\bar i$ pairs.

---

## 5. Main Theorems (Section 4) — VERBATIM

### Theorem 4.1 (Type $C$, page 13).

> For $\lambda,\mu\in\mathrm{Par}_n$, we have
> $$\operatorname{KL}^{C_n}_{\lambda,\mu}(q) = \sum_{T\in \mathrm{SSOT}_g(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))} q^{\overline{D}(\phi_c(T))}$$
> where $g$ is any positive integer such that $g\ge \lambda_1$ and $\phi_c$ is the map defined in Lemma 3.5.

Here $\mathrm{oc}(\lambda,g)$ is the orthogonal complement and the embedding lands in column KR crystal $B_\mu^t(\square\square)$ of affine type $C_N^{(1)}$.

### Theorem 4.6 (Type $B$, spin weights, page 15).

> For $\lambda,\mu\in\mathrm{Par}_n$, we have
> $$\operatorname{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \sum_{T\in \mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\overline{\mathrm{oc}}(\mu,g))} \mathrm{energy}_{q,t}(\phi_c(T))$$
> where $g$ is any positive integer such that $g\ge\lambda_1$, and $\phi_c$ is the map in Lemma 3.5.

Here $\lambda^\sharp = \lambda + (\frac12)^n$ is a spin weight, the embedding is into the column KR crystal $B^{1,1}(\textsf{B})$ of affine type $B_N^{(1)}$.

Setting $t=q$ recovers the usual Lusztig multiplicity. Note **Remark 4.7**: $\operatorname{KL}^{B_n}_{\lambda,\mu}(q,t)$ is **not in general nonnegative** for non-spin $B$ weights, e.g. $\operatorname{KL}^{B_2}_{(1,0),(0,0)}(q,t) = qt - q + t$. So the spin restriction is essential.

### Theorem 5.4 (Level-restricted $q$-weight multiplicities — types $B,C,D$, page 26).

> $$\operatorname{KL}^{\mathfrak{g}_n,L_A}_{\lambda,\mu}(q) = \sum_\nu \operatorname{KL}^{A_{n-1}}_{\hat\nu,\hat\mu}(q)\, d^{\mathfrak{g}_n}_{\lambda,\nu} = q^{\|\hat\mu\|+\frac{|\hat\mu|-|\hat\lambda|}{2}}\!\!\!\sum_{\substack{b\in \mathrm{HW}(B_{\hat\mu}(\diamond),\hat\lambda)\\ \varepsilon_0(b)\le\zeta g}} q^{-\overline{D}(b)/2}$$
> where $(\diamond,\zeta) = (\square,2)$ for $B_n$, $(\square\square,1)$ for $C_n$, $(\textsf{B},2)$ for $D_n$.

This refines the **$X=K=\infty\mathrm{KL}$ theorem** [Shi05, LS07, LOS12] for tensor products of row KR crystals.

---

## 6. Types Covered (Table 1, page 2)

| Type | Lusztig $q$-mult | Level-restricted |
|------|-------|-----|
| $B$  | column KR of type $D^{(2)}_{N+1}$ (only **spin** weights) | row KR of type $D^{(2)}_{N+1}$ |
| $C$  | column KR of type $B_N^{(1)}$ (dominant) | row KR of type $C_N^{(1)}$ |
| $D$  | **?** (open) | row KR of type $B_N^{(1)}$ |

Exceptional types ($G_2$, $F_4$, $E_*$) **not addressed**. Type $D$ Lusztig multiplicity formula is **open** — Section 6 conjectures it should involve the column KR crystal of $C_N^{(1)}$.

---

## 7. Lusztig multiplicity vs. Kazhdan–Lusztig $P_{u,v}$ — what the paper says

This is the question Rick (and OQ2) cares most about. **The paper does not give an explicit formula relating $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ to individual $P_{u,v}$**, but it makes one critical reference:

> "[Lusztig's $q$-weight multiplicity's] nonnegativity follows from the theory of the affine Kazhdan–Lusztig polynomial [Lus83]." (page 2, paragraph 1)

**Citation [Lus83]** = Lusztig, "Singularities, character formulas, and a $q$-analog of weight multiplicities" (Astérisque 101–102, 1983).

The standard story behind this remark (Kato, Lusztig, Kashiwara–Tanisaki): for a finite simple Lie algebra $\mathfrak{g}$ with affine Weyl group $W_{\mathrm{aff}}$,
$$\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q) = \sum_{w\in W_{\mathrm{aff}}} (\text{signed sum}) \cdot P_{x_w,y_w}(q)$$
where the right-hand side involves **affine** parabolic Kazhdan–Lusztig polynomials at certain alcove pairs. So the relationship is:

- $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ is a **specific summed/alternating combination** of affine parabolic KL polynomials (specifically, polynomials $P^{-,q}_{x,y}$ in the Kashiwara–Tanisaki / Soergel "negative-level" parabolic affine setup).
- In the Kostka–Foulkes (type $A$) limit, the relevant affine parabolic KL polynomials are exactly the parabolic KL polynomials of type $\widetilde{A}_{n-1}$, and they happen to equal Kostka–Foulkes for special index pairs (Lascoux's "atomic" theorem; Kazhdan–Lusztig–Lusztig–Shoji theorem).

**Crucially, the paper does NOT prove or cite a closed form for individual $P_{u,v}$** — they prove a closed form for the *summed quantity* $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$. The map "energy on KR crystal $\to$ summed affine parabolic KL polynomial" is the content of Theorems 4.1, 4.6 (combined with the Kato/Lusztig theorem expressing $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ in terms of affine KL).

References they cite for the geometric/algebraic side: [Bro93] (Broer), [Kir01] (Kirillov), [Bry89] (Brylinski). Brylinski's filtration on weight spaces of $V(\lambda)$ — the associated graded module gives Lusztig's polynomial (Brylinski's theorem). This is the classical bridge from $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ to representation theory.

---

## 8. What this means for OQ2

### What is now answered

1. **For types $B$ (spin) and $C$**: Lusztig multiplicities $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ are **fully and combinatorially** read off the KR crystal energy function. Concretely: list semistandard oscillating tableaux, embed via $\phi_c$ into the column KR crystal, sum $q^{\overline{D}}$.
2. **For type $A$**: the formula reduces to charge (consistent with Lascoux–Schützenberger and Nakayashiki–Yamada [NY97] who already showed energy on row KR = charge in type $A$).
3. **The energy function on KR crystals computes "summed" affine parabolic KL data** for $B$ (spin), $C$. So the energy/R-matrix language IS expressive enough for at least one nontrivial KL-adjacent invariant.

### What remains open

1. **Individual KL polynomials $P_{u,v}$**: The paper still computes only the *summed/projected* quantity, not individual matrix entries. The sum-over-$T$ obscures which $T$ correspond to which $u,v$.
2. **Type $D$ (Lusztig multiplicity)** is open — Section 6.
3. **Non-spin type $B$**: Remark 4.7 shows $\operatorname{KL}^{B_n}_{\lambda,\mu}(q,t)$ has *negative* coefficients in general, so a sum-of-nonnegative-energies formula cannot exist for non-spin weights without modification. This is a sharp obstruction: the "naive" KR-energy approach cannot capture all of $B_n$.
4. **Exceptional types** completely open.
5. **The translation from $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ to individual $P_{u,v}$** is a separate (nontrivial) problem in affine Kazhdan–Lusztig theory; this paper does not address it.

### The precise gap to OQ2

OQ2 asks: can $P_{u,v}(q)$ be read directly from a crystal? Choi–Kim–Lee establish that a *coarsened* invariant (Lusztig $q$-weight multiplicity, which is a non-negative integer combination / signed alternating sum of affine parabolic $P_{u,v}$) IS read from a crystal — namely the KR crystal energy. The remaining question is whether one can refine: split $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}(q)$ into the individual summands $P_{u,v}(q)$ from the affine parabolic decomposition, and read each individually from a finer crystalline structure.

Candidate refinement structures (not in this paper):
- crystal skeletons (Maas-Gariépy, Brauner–Corteel–Daugherty–Schilling 2025);
- atomic/molecular decompositions (Assaf et al., Lascoux);
- hypercube decompositions for combinatorial invariance (Barkley–Gaetz, Esposito–Marietti 2024).

---

## 9. Surprises / things to remember

- The energy function naturally lives on the **column** KR crystal for the $C_n$ Lusztig case but the **row** KR crystal for the level-restricted version. The same statistic, two different ambient crystals.
- Type $B$ requires **spin** weights and a $q,t$-refinement; the $q$-only version $\operatorname{KL}^{B_n}_{\lambda,\mu}(q)$ for non-spin weights *fails to have nonnegative coefficients* (Remark 4.7). This is a hard combinatorial obstruction.
- The splitting map (a generalization of Lascoux's standardization) is the key tool — it preserves energy up to a known shift and reduces everything to nearest-neighbor energy on $(B^{1,1})^{\otimes n}$.
- The bijection $\phi_c$ uses a "reduce" operation deleting unmatched $i,\bar i$ pairs — this is reminiscent of the "growth" / "promotion" combinatorics on rc-graphs / oscillating tableaux from Sundaram–Stembridge.
- The cyclage graph appears as Figure 1 (page 42) showing the connection between Lascoux's cyclage and the type-$A$ KR crystal structure on tableaux.

---

## 10. Cited papers worth following up

- **[Lus83]** Lusztig, "Singularities, character formulas, and $q$-analog of weight multiplicities" — the *defining* paper for $\operatorname{KL}^{\mathfrak{g}}_{\lambda,\mu}$ via affine KL.
- **[NY97]** Nakayashiki–Yamada — proved energy = charge for type $A$.
- **[Sun86]** Sundaram — original Cauchy-style symplectic RSK; their Proposition 5.10 generalizes it.
- **[Shi05], [LS07], [LOS12]** — the $X=K$ theorem chain.
- **[BG06]** Bergeron–Garsia, Cauchy identities used in proofs.
- **[Lee23]** S. J. Lee — bijection between SSOT and King tableaux (one author of present paper).
- **[BMPS19]** Blasiak–Morse–Pun–Summers — Catalan functions (type $A$); the paper conjectures a type-$C$ analog.
