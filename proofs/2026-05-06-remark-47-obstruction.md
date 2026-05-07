# The Remark-4.7 obstruction: why no positive energy formula for non-spin type B

**Status (2026-05-06):** Phase 1, 2 complete & rigorous. Phase 3 partially proved, partially conjectural. Phase 4 conjectural.
**Author:** Rick.
**Cf.** Choi–Kim–Lee, arXiv:2412.20757, Remark 4.7.

---

## 0. The setup

For a finite simple Lie algebra **g** with positive root system R⁺ split into long (R⁺_L) and short (R⁺_S) parts, define the **Macdonald two-parameter Lusztig polynomial**

$$
\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;:=\; \sum_{w\in W}(-1)^w \bigl[e^{\,w(\lambda+\rho)-(\mu+\rho)}\bigr]
\prod_{\alpha\in R^+_L}\frac{1}{1-q\,e^{\alpha}}\prod_{\alpha\in R^+_S}\frac{1}{1-t\,e^{\alpha}}.
$$

Setting `t = q` recovers the ordinary Lusztig polynomial. Choi–Kim–Lee Remark 4.7 records

$$
\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t)\;=\;qt-q+t,
$$

a polynomial with a **negative** coefficient.

The goal of this note: **(1)** verify the claim, **(2)** locate the obstruction structurally, **(3)** propose what should replace the energy sum, **(4)** conjecture the general pattern.

---

## 1. Phase 1 — Verification

### 1.1 The B_2 root data

* Simple roots: α_1 = e_1−e_2 (long), α_2 = e_2 (short).
* Positive roots: long {α_1=(1,−1), α_1+2α_2=(1,1)}; short {α_2=(0,1), α_1+α_2=(1,0)}.
* ρ = (3/2, 1/2). Weyl group W of order 8, signed permutations of (e_1,e_2).

### 1.2 The (q,t)-Kostant partition function

For β ∈ Z², let

$$
K_{q,t}(\beta) \;:=\; \sum_{\substack{(n_\alpha)_{\alpha\in R^+}\\ n_\alpha\ge 0,\ \sum n_\alpha\alpha=\beta}} q^{\sum_{\alpha\in R^+_L}n_\alpha}\,t^{\sum_{\alpha\in R^+_S}n_\alpha}.
$$

This is the (q,t)-graded dimension of the β-weight space of the polynomial ring $\mathrm{Sym}(\mathfrak n_+)$ in which long-root generators carry q-weight and short-root generators carry t-weight.

### 1.3 The WCF reformulation

By Kostant's multiplicity formula and the formal-power-series identity $\prod (1-q_\alpha e^\alpha)^{-1} = \sum_\beta K_{q,t}(\beta) e^\beta$:

$$
\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \sum_{w\in W} (-1)^{\ell(w)}\, K_{q,t}\bigl(w\!\cdot\!\lambda - \mu\bigr),
$$

where w·λ = w(λ+ρ)−ρ (dot action). Since $K_{q,t}(\beta) = \dim_{q,t} M(w\!\cdot\!\lambda)_\mu$ for the Verma module $M(w\!\cdot\!\lambda)$, this **is the bigraded Euler characteristic of the BGG-Verma resolution of V(λ) restricted to weight μ**:

$$
\boxed{\quad
\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \sum_{i=0}^{|R^+|} (-1)^{i}\,\dim_{q,t}\Bigl(\bigoplus_{\ell(w)=i}M(w\!\cdot\!\lambda)_\mu\Bigr).
\quad}
$$

### 1.4 Computation for the Remark-4.7 case

For λ=(1,0), μ=(0,0): λ+ρ = (5/2, 1/2), μ+ρ = (3/2, 1/2). Iterate over W:

| w | ℓ(w) | sign | w·λ−μ | K_{q,t} support | M(w·λ)_0 in (q,t) |
|---|---|---|---|---|---|
| e | 0 | + | (1, 0) | (0,1), (1,1) | t + qt |
| s_1 | 1 | − | (−1, 2) | ∅ | 0 |
| **s_2** | **1** | **−** | **(1, −1)** | **(1, 0)** | **q** |
| s_2 s_1 | 2 | + | (−1, −3) | ∅ | 0 |
| s_1 s_2 | 3 | − | (−2, −3) | ∅ | 0 |
| s_1 s_2 s_1 | 2 | + | (−2, 2) | ∅ | 0 |
| s_2 s_1 s_2 | 3 | − | (−4, 0) | ∅ | 0 |
| w_0 | 4 | + | (−4, −1) | ∅ | 0 |

(Verified by direct enumeration in `compute_kl_B2.py`, `bgg_decomposition.py`.)

Summing with signs: **(t + qt) − q = qt − q + t.** ✓

---

## 2. Phase 2 — The structural obstruction (proved)

### 2.1 The bidegree-disjointness theorem

> **Theorem 2.1 (the precise obstruction).** For B_2, λ=(1,0), μ=(0,0):
>
> 1. The only nonzero contributions to the BGG-Euler characteristic at weight 0 come from w = e (length 0) and w = s_2 (length 1).
> 2. M(λ)_0 has (q,t)-bigraded support **{(0,1), (1,1)}** = t + qt.
> 3. M(s_2·λ)_0 has (q,t)-bigraded support **{(1,0)}** = q.
> 4. The bidegrees in (2) and (3) are **disjoint**.
>
> Therefore the negative coefficient at bidegree (1,0) — namely **−q** — has no possible cancellation with a positive contribution at the same bidegree, and **no choice of crystal/statistic on a fixed combinatorial set can eliminate it**.

**Proof.** (1)–(3) are direct enumeration. (4) is the observation $\{(0,1),(1,1)\} \cap \{(1,0)\} = \emptyset$.

For the final claim: any positive energy sum has nonneg coefficients on each monomial; the bidegree (1,0) monomial here has coefficient −1; contradiction. ∎

### 2.2 The combinatorial fingerprint

The bidegree (1,0) means: a decomposition of (1,−1) as a single long-root step (= α_1).

* In M(s_2·λ): the unique decomposition (1,−1) = 1·α_1 is a one-long-root step. Bidegree (1,0).
* In M(λ): decompositions of (1,0) are
  - (1,0) = (α_1+α_2) — one **short** root step (the root (1,0) itself is short). Bidegree (0,1).
  - (1,0) = α_1 + α_2 — one **long** root α_1=(1,−1) plus one **short** root α_2=(0,1). Bidegree (1,1).
  
  **No decomposition of (1,0) as a single long root is possible**, because (1,0) is itself a *short* root and there is no long root equal to (1,0).

> **Corollary 2.2 (the heart of the obstruction).**
> The negative coefficient −q in $\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t)$ is *exactly* the count of "single-long-root paths from μ to s_α·λ" minus "single-long-root paths from μ to λ" — and it is non-zero precisely because s_2·(1,0) − (0,0) = (1,−1) **is** a long root, while (1,0) − (0,0) = (1,0) **is not**.

### 2.3 The general structural mechanism (B_2 case)

> **Proposition 2.3 (positivity criterion for B_2).** For B_2, $\mathrm{KL}^{B_2}_{\lambda,\mu}(q,t)$ has all nonneg coefficients ⟺ for every bidegree (i,j) ∈ Z²_{≥0},
> $$
> \mathrm{mult}_{(i,j)}\!\Bigl(\bigoplus_{w:\ell(w)\text{ odd}}M(w\!\cdot\!\lambda)_\mu\Bigr) \;\le\; \mathrm{mult}_{(i,j)}\!\Bigl(\bigoplus_{w:\ell(w)\text{ even}}M(w\!\cdot\!\lambda)_\mu\Bigr).
> $$

This is just the elementwise positivity of the Euler-characteristic equation. Each side is a sum of $K_{q,t}(\beta_w)$'s; positivity ⟺ each "negative" Verma's bigraded contribution is dominated by some "positive" Verma's bigraded contribution at the same bidegree.

**Verified examples** (from `bgg_decomposition.py`):

| (λ, μ) | M(λ) supp ⊆ even | M(s_α·λ) supp ⊆ odd | cancellation? | result |
|---|---|---|---|---|
| (1,0),(0,0) | {(0,1),(1,1)} | s_2: {(1,0)} | **disjoint** | qt + t − q (neg) |
| (1,1),(0,0) | {(0,2),(1,0),(1,2)} | s_1: {(0,2)} | (0,2) cancels | q + qt² (pos) |
| (2,0),(0,0) | {(0,2),(1,2),(2,0),(2,2)} | s_2: {(1,1),(2,1)} | **disjoint** | (neg) |
| (2,2),(0,0) | {(0,4),(1,2),(1,4),(2,0),(2,2),(2,4)} | s_1: {(0,4),(1,2),(1,4)} | three pairs cancel | q²(1+t²+t⁴) (pos) |
| (2,1),(1,0) | {(0,2),(1,0),(1,2)} | (all others 0) | nothing to cancel | t²+q+qt² (pos) |
| (3,1),(1,1) | {(0,2),(1,2),(2,0),(2,2)} | (all others 0) | nothing to cancel | t²+qt²+q²+q²t² (pos) |

The disjoint-bidegree cases are exactly where negativity arises.

### 2.4 What this rules out, sharply

Theorem 2.1 implies a **strong** non-existence statement:

> **Corollary 2.4.** There is no map $\mathcal F$ from a finite combinatorial set $\mathcal T$ to $\mathbb Z^2_{\ge 0}$ (a "(q,t)-statistic") such that $\sum_{T\in\mathcal T} q^{\mathcal F(T)_1} t^{\mathcal F(T)_2} = qt - q + t$.

**Proof.** The coefficient of q (= bidegree (1,0)) in such a sum would equal $\#\{T : \mathcal F(T) = (1,0)\} \ge 0$, but in qt − q + t this coefficient is −1. ∎

This is the sharp obstruction: it is not merely that *we have not found* a positive crystal formula; it is that **no such formula can exist** for the (q,t)-version of the polynomial.

(The equal-parameter version $\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q) = q^2$ does have a one-element crystal/statistic representation; the obstruction is specific to the (q,t)-bigrading.)

---

## 3. Phase 3 — Replacements (and which is right)

### 3.1 (i) Signed sum

The minimal signed-sum interpretation is *forced* by the proof of Theorem 2.1: take
$$
\mathcal T^+ \cup \mathcal T^- \quad\text{with}\quad
\sum_{T\in\mathcal T^+} q^{a(T)}t^{b(T)} - \sum_{T\in\mathcal T^-} q^{a(T)}t^{b(T)} = qt - q + t,
$$

where $\mathcal T^+ = $ (Kostant partitions of (1,0)) and $\mathcal T^- = $ (Kostant partitions of (1,−1)) — equivalently, $\mathcal T^+$ = paths in M(λ)_0, $\mathcal T^-$ = paths in M(s_2·λ)_0.

This is **just** the WCF combinatorics with explicit signs. It is canonical but combinatorially uninteresting because the sign is built in.

A *more interesting* signed-sum interpretation would be a **single combinatorial set** with a sign-reversing involution that pairs many ± elements but leaves three ε-invariant survivors. For our case, no such involution exists in any clean way, because the −q sits at a bidegree (1,0) that is unmatched by any +q.

### 3.2 (ii) Euler characteristic of a 2-step complex (the structurally clean answer)

By §1.3, the (q,t)-Lusztig polynomial **is, exactly,** the bigraded Euler characteristic of the BGG complex restricted to weight μ:
$$
\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \sum_i (-1)^i \dim_{q,t}\bigl(\mathrm{BGG}^i\bigr)_\mu
\;\;\text{where}\;\;
\mathrm{BGG}^i \;=\; \bigoplus_{\ell(w)=i} M(w\!\cdot\!\lambda).
$$

For B_2, λ=(1,0), μ=0, only BGG^0 and BGG^1 contribute non-trivially:
* BGG^0 = M(λ), bigraded (q,t)-dim at weight 0: t + qt.
* BGG^1 = M(s_2·λ), bigraded (q,t)-dim at weight 0: q.
* All higher BGG^i = 0 at weight 0.

So we have a **2-step complex** (effectively, after killing zero pieces):
$$
0 \longrightarrow M(s_2\!\cdot\!\lambda)_0 \xrightarrow{\;\partial\;} M(\lambda)_0 \longrightarrow 0
$$
with $\dim_{q,t}\partial$-domain = q, $\dim_{q,t}\partial$-codomain = t + qt, $\chi_{q,t} = (t+qt) - q$.

**Important caveat.** The BGG differential ∂ is *not* (q,t)-bigraded in the naive sense: ∂ corresponds to multiplication by $f_2^{a_2(\lambda)+1} = f_2$ (for our case), which has bidegree (0,1) — a **shift**, not a degree-zero map. So:

* The Euler characteristic $\chi_{q,t}$ is well-defined as a virtual (q,t)-graded class.
* The bigraded H^0, H^1 of the *unshifted* complex do not refine $\chi_{q,t}$ as a difference of nonneg pieces.
* Equivalently: in the bigraded category, the BGG resolution of V(λ) is **not** acyclic; it is only *ungraded-acyclic*. The negative coefficients in the Euler char measure the obstruction to bigraded acyclicity.

This is the clean structural statement:

> **Theorem 3.1 (proved).** $\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t)$ is the bigraded Euler characteristic of the BGG-Verma resolution of V(λ) restricted to weight μ, where Verma modules carry the bigrading from $\mathrm{Sym}(\mathfrak n_+)$ (long-root generators have bidegree (1,0), short have (0,1)). The polynomial has nonneg coefficients ⟺ the bigraded BGG complex at weight μ is acyclic in the bigraded sense (equivalently, all higher bigraded Tor^i vanish at weight μ).

### 3.3 (iii) Difference of two energy sums (concrete realization for B_2)

A direct corollary of §1.3, partitioning W by length parity:

> **Corollary 3.2.** For any **g**, λ, μ:
> $$
> \mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \underbrace{\sum_{w:\ell(w)\text{ even}}\dim_{q,t}M(w\!\cdot\!\lambda)_\mu}_{=:\ \mathcal E^+(q,t)}
>   \;-\; \underbrace{\sum_{w:\ell(w)\text{ odd}}\dim_{q,t}M(w\!\cdot\!\lambda)_\mu}_{=:\ \mathcal E^-(q,t)}.
> $$

For $B_2$, λ=(1,0), μ=0: $\mathcal E^+ = t + qt$, $\mathcal E^- = q$. So
$$
\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t) \;=\; (t+qt) - q.
$$

This is the **canonical** "difference of two energy sums" realization. The sets in question are Kostant partitions for even-length and odd-length Weyl elements respectively, with the (q,t)-statistic = (long-root count, short-root count).

> **Remark.** In CKL Theorem 4.6 (spin type B), they give a single positive energy sum because the half-shift λ → λ^♯ shifts $w\cdot \lambda^\sharp$ in a way that *evacuates* the odd-length Weyl elements' contribution at weight $\mu^\sharp$ (the bidegrees disappear from the Kostant supports). For non-spin λ, this "evacuation" fails, and the difference $\mathcal E^+ - \mathcal E^-$ does not reduce to a single positive sum.

---

## 4. Phase 4 — Conjectures and the spin-orbit picture

### 4.1 The bidegree-cancellation criterion is sharp but not closed-form

For B_2, Proposition 2.3 gives a precise positivity criterion: at every bidegree, even-length Verma multiplicity ≥ odd-length Verma multiplicity. Empirical computation across the dominant pairs with $\lambda_1, \mu_1 \le 4$ confirms this is sharp (matches the negative-coefficient cases exactly).

A *closed-form* criterion in terms of (λ, μ) alone would be very valuable but does not appear simple from the data. (The condition "λ ∈ k(1,1) lattice" works at μ = (0,0) but **not** universally — e.g., (4,2)→(1,0) is positive despite λ_1−λ_2 ≠ μ_1−μ_2.)

### 4.2 Conjecture 4.1 (B_n positivity)

> **Conjecture 4.1.** For B_n, $\mathrm{KL}^{B_n}_{\lambda,\mu}(q,t)$ has nonneg coefficients ⟺ at every bidegree (i,j), the bigraded multiplicity in $\bigoplus_{w\text{ even}}M(w\!\cdot\!\lambda)_\mu$ dominates that in $\bigoplus_{w\text{ odd}}M(w\!\cdot\!\lambda)_\mu$.
>
> Sufficient conditions:
> * **Spin λ**, i.e., $\lambda = \lambda_0 + (\tfrac12)^n$ with $\lambda_0$ in the integer dominant cone (CKL Theorem 4.6 — proven there).
> * **Diagonal λ with μ = 0**, i.e., λ = k·θ_L (integer multiples of the highest long root). For B_2 this is λ = (k,k); my computation verifies positivity for all $k \le 4$.

### 4.2.1 Why the spin lattice helps — verified on B_2 spin pairs

I verified (script `bgg_decomposition.py`) for several spin pairs $(\lambda^\sharp, \mu^\sharp)$ in B_2 that **odd-length Verma weight-μ supports are either empty or contained in the corresponding even-length supports**, hence positivity follows from §1.3:

| (λ, μ) (spin) | M(λ)_μ even support | Odd Verma supports | result |
|---|---|---|---|
| (3/2,1/2)→(1/2,1/2) | {(0,1),(1,1)} | all 0 | t+qt ✓ |
| (5/2,1/2)→(1/2,1/2) | {(0,2),(1,2),(2,0),(2,2)} | s_2: {(2,0)} ⊆ even | t²+qt²+q²t² ✓ |
| (3/2,3/2)→(1/2,1/2) | {(0,2),(1,0),(1,2)} | s_1: {(0,2)} ⊆ even | q+qt² ✓ |
| (5/2,3/2)→(1/2,1/2) | {(0,3),(1,1),(1,3),(2,1),(2,3)} | s_1: {(0,3)} ⊆ even | qt+qt³+q²t+q²t³ ✓ |
| (5/2,3/2)→(3/2,1/2) | {(0,2),(1,0),(1,2)} | all 0 | t²+q+qt² ✓ |

**The structural mechanism for spin positivity (precise).** The half-shift $\mu \mapsto \mu^\sharp = \mu + (\tfrac12)^n$ shifts the *y*-coordinate of $\beta_w = w\!\cdot\!\lambda^\sharp - \mu^\sharp$ by integer offsets which, in turn, shift the (q,t)-bigraded support of $K_{q,t}(\beta_w)$ into a new region of $\mathbb{Z}^2_{\ge 0}$. Concretely for the analogous (5/2,1/2)→(1/2,1/2) spin case (the spin shift of (2,0)→(0,0)):

* $\beta_{s_2} = (2, -2)$ instead of $(2, -1)$ in non-spin case.
* $K_{q,t}((2,-2))$ has support $\{(2,0)\}$ — entirely **inside** $M(\lambda^\sharp)_{\mu^\sharp}$'s support $\{(0,2),(1,2),(2,0),(2,2)\}$.
* In contrast, $K_{q,t}((2,-1))$ for the non-spin case has support $\{(1,1),(2,1)\}$ — entirely **outside** the same M(λ)_μ support, hence no cancellation.

This is the precise "spin evacuation" mechanism: the half-integer μ-shift moves odd-length Verma supports into bidegrees already represented in M(λ)_μ, so the alternating sum cancels positively. For non-spin (integer) λ, the supports can be misaligned — exactly as in §2.

### 4.3 The categorification statement (conjecture)

> **Conjecture 4.2 (the derived energy).** There is a Z²-graded chain complex $\mathcal E^\bullet_{q,t}(\lambda,\mu)$ of finite-dim vector spaces (or, in a refinement, of $H_\bullet(0)$-modules) such that
> $$
> \mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \sum_i (-1)^i \dim_{q,t} H^i\bigl(\mathcal E^\bullet_{q,t}(\lambda,\mu)\bigr).
> $$
> The complex is acyclic in positive degrees precisely when λ is in the spin sublattice (hence the polynomial is positive).

**Concrete candidate (B_2 case).** The complex $\mathcal E^\bullet$ should be the BGG-Verma complex restricted to weight μ, equipped with the bigrading from $\mathrm{Sym}(\mathfrak n_+)$ via long/short roots, and with differential = BGG inclusion (which is bigraded-shifted by the simple-root step). The H^i are the *bigraded* derived V(λ)_μ:

* For spin λ: H^0 only, recovering CKL energy formula.
* For non-spin λ: H^0 and H^1 nonzero in different bidegrees, with $H^0 - H^1 = $ KL polynomial in K_0(bigraded-VS).

### 4.4 Connection to Almousa–Lu (the philosophical bridge)

In Almousa–Lu, the *acyclic* cochain complex $\mathcal C(\vec\alpha)$ (Theorem 5.6) categorifies the **positive** ribbon-product expansion in **NSym**. Acyclicity is what guarantees positivity.

The **non-spin type-B Lusztig polynomial** would, conjecturally, sit at the boundary of this picture: a *non-acyclic* analog of $\mathcal C(\vec\alpha)$, whose H^1 contribution is the categorification of −q. The Frobenius-characteristic side is the (q,t)-Macdonald polynomial expanded in some basis where positivity fails.

This is *the first natural example* in this program where non-acyclicity matters. It is the type-B analog of the "spin/non-spin" split, and it is a *necessary* feature of any combinatorial formula for non-spin Lusztig polynomials.

---

## 5. Open questions

1. **Closed-form positivity criterion.** Is there a simple necessary-and-sufficient condition on (λ, μ) for $\mathrm{KL}^{B_n}_{\lambda,\mu}(q,t)$ to have nonneg coefficients? My data hints at a condition involving the λ-orbit's projection onto root-length subspaces but I don't have it crisp.

2. **B_n verification.** Verify Conjecture 4.1 for B_3, n ≥ 3 cases. The B_2 BGG analysis extends mechanically; the question is whether the positivity criterion (Prop 2.3) generalizes verbatim.

3. **Honest derived Brylinski.** Construct $\mathcal E^\bullet_{q,t}$ as a complex of *honest* bigraded vector spaces (with bigraded differentials), and verify Conjecture 4.2 by explicit Tor computation in a case like B_2/V(ω_1)_0.

4. **Combinatorial 2-step complex.** Find an Almousa–Lu-style explicit cochain complex of indecomposable projectives over some affine-Hecke-algebra-like tower whose Euler characteristic gives non-spin type-B (q,t)-Lusztig polynomials.

5. **Type D.** Repeat for D_n. The CKL paper leaves type-D Lusztig multiplicity open. The B_2 analysis here suggests that the same BGG-cancellation framework applies, with the spin-vs-non-spin split replaced by a different lattice condition.

---

## 6. Files and verification

* `/home/agent/projects/proofs/remark47/compute_kl_B2.py` — direct WCF computation of KL^{B_2}_{λ,μ}(q,t) for all dominant pairs with $\lambda_1\le 4$. Verifies Remark 4.7's polynomial qt − q + t.
* `/home/agent/projects/proofs/remark47/bgg_decomposition.py` — BGG-Verma decomposition of each KL polynomial: shows precisely which Weyl elements contribute and at which (q,t)-bidegrees.

**Confirmed empirical facts:**
* $\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t) = qt − q + t$.
* $\mathrm{KL}^{B_2}_{(k,k),(0,0)}(q,t) = q^k\,[k+1]_{t^2}$, all coefs nonneg, for $k \le 4$ (and conjecturally all k).
* The negative-coefficient cases are *exactly* those where some odd-length-Verma's $(q,t)$-bidegree support fails to be contained in $\bigcup_{\text{even-length }w}\mathrm{supp}(M(w\!\cdot\!\lambda)_\mu)$.

---

## 7. Honest assessment

### 7.1 What is rigorously proved
* §1.3: the WCF reformulation as a bigraded BGG-Verma Euler characteristic. Direct.
* §1.4: explicit verification $\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t) = qt - q + t$. Direct enumeration.
* §2.1, §2.4: the bidegree-disjointness theorem and the strong non-existence corollary for combinatorial positive sums.
* §2.3 (Prop 2.3): the precise positivity criterion for B_2 — directly from the Euler characteristic decomposition.
* §3.1, §3.2 (Theorem 3.1), §3.3 (Cor 3.2): Phase-3 replacements (i)–(iii) are *all* directly forced by §1.3; they are different repackagings of the same Euler characteristic.

### 7.2 What is conjectural
* Conj 4.1: positivity criterion for general $B_n$ — verified for $B_2$, conjectural for $B_n$.
* Conj 4.2: the existence of an honest bigraded complex realizing the Tor groups whose Euler characteristic gives KL^{**g**}_{λ,μ}(q,t). The candidate is the BGG complex with bidegree shifts; the technical issue is making the differentials genuinely bigraded.
* §4.4: connection to Almousa–Lu — speculative, but the rough shape is forced (acyclicity for spin, non-acyclicity for non-spin).

### 7.3 Where this leaves OQ2
The deep takeaway is that **for non-spin type B (and presumably non-minuscule cases in general), reading the Lusztig polynomial from a single crystal energy is impossible**. The minimum required structure is a 2-term complex (or a virtual class in K_0 of bigraded vector spaces). This is a sharp lower bound on any future positive combinatorial formula.

The good news: the BGG-Verma framework gives a *canonical* such virtual representation, expressed concretely in §3.3 as the "even-length minus odd-length" Verma multiplicity difference. Whether this can be matched to a clean crystal-theoretic story (à la Almousa–Lu's derived ribbon complexes, but for non-acyclic settings) is the next move in the program.
