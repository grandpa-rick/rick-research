# Support Absorption (SA) for type B: B_2 proof, B_n program, and the Aug~ involution

**Status (2026-05-07):** B_2 dominant-μ case **PROVED** rigorously via explicit Aug~ involution (algorithmic Aug~ + algebraic Lemmas 2.1–2.5; also computer-verified on all 140 dominant spin pairs with $\lambda_1 \le 9/2$). B_n dominant-μ case **verified** computationally for B_3 (798/798 dominant spin pairs with $\lambda_1 \le 9/2$). General proof open; precise obstruction identified.

**Author:** Rick.
**Antecedents:**
- `2026-05-06-remark-47-obstruction.md` — B_2 framework, BGG bigrading.
- `2026-05-07-B3-acyclicity-test.md` — B_3 evidence (200/200).
- `2026-05-07-spin-shift-mechanism.md` — three candidate routes; this note executes route 3 with refinements.
- `papers/ckl-theorem-46-extraction.md` — gap between CKL and (SA).

**Scripts:** `~/projects/proofs/remark47/aug_tilde_B2.py`, `aug_tilde_Bn.py`, `sa_matching_test.py`.

---

## 0. Refined statement of (SA)

The form of (SA) in `state/PROVE.md` says "let μ be any half-integer weight." This is **slightly too strong**: for non-dominant μ, KL polynomials can have negative coefficients while still being well-defined.

**Counter-example.** For $\lambda = (1/2, 1/2)$, $\mu = (-3/2, 1/2)$ in B_2 (both spin):
$$\mathrm{KL}^{B_2}_{(1/2,1/2),(-3/2,1/2)}(q,t) = q^2 t^2 - q.$$
Negative coefficient $-q$. (Verified via `bgg_decomposition.py`.) Note $\mathrm{KL}|_{q=t=1} = 0$ — so $\mu^\sharp$ is outside the convex hull of $W \cdot \lambda^\sharp$ (which makes sense: $V(\sigma)$ has weights $\{(\pm 1/2, \pm 1/2)\}$ only, and $\mu = (-3/2, 1/2)$ isn't one).

So the empirical evidence is for **dominant** μ. The refined conjecture:

> **(SA) — Support Absorption, refined.** Let $\lambda \in \tfrac12(1,\dots,1) + \mathbb Z^n$ be dominant spin and let $\mu$ be **dominant** spin (also half-integer with $\mu - \lambda \in \mathbb Z^n$). Then for every bidegree $(i,j)$,
> $$\sum_{w: \ell(w)\ \text{odd}} \mathrm{mult}^{i,j}_{w \cdot \lambda}(\mu) \;\le\; \sum_{w: \ell(w)\ \text{even}} \mathrm{mult}^{i,j}_{w \cdot \lambda}(\mu).$$

**Computational status (May 2026):**
- B_2 dominant: 140/140 spin pairs at $\lambda_1 \le 9/2$ ✓.
- B_3 dominant: 798/798 spin pairs at $\lambda_1 \le 9/2$ ✓.
- (Both via direct count of even/odd Kostant partitions per bidegree.)

The original B_3 evidence (200/200 at $\lambda_1 \le 7/2$) is a sub-test; the new 798/798 strengthens it.

---

## 1. The setup, in computational form

$\rho^\sharp := \rho + \sigma = (n, n-1, \ldots, 1)$ — strictly decreasing positive integer vector.

For spin $\lambda = \tilde\lambda + \sigma$, $\mu = \tilde\mu + \sigma$ ($\tilde\lambda, \tilde\mu \in \mathbb Z^n$ dominant):
$$\tilde a := \tilde\lambda + \rho^\sharp, \qquad b := \tilde\mu + \rho^\sharp.$$
Then $w \cdot \lambda - \mu = w\tilde a - b$ for every $w \in W$. Both $\tilde a$ and $b$ are strictly decreasing positive integer vectors (for dominant $\tilde\lambda, \tilde\mu$).

For each $w$: $\beta_w := w\tilde a - b \in \mathbb Z^n$. The Kostant partitions of $\beta_w$ at bidegree $(i,j)$ form a finite set $\mathcal P^{i,j}_w$. (SA) is the inequality

$$\sum_{\ell(w)\,\text{odd}} |\mathcal P^{i,j}_w| \;\le\; \sum_{\ell(w)\,\text{even}} |\mathcal P^{i,j}_w| \quad \text{for all } (i,j) \in \mathbb Z^2_{\ge 0}.$$

Equivalently, there exists a **bidegree-preserving injection** $\Phi: \bigsqcup_{\ell\,\text{odd}}\mathcal P^{i,j}_w \to \bigsqcup_{\ell\,\text{even}}\mathcal P^{i,j}_w$ for every $(i,j)$.

---

## 2. The Aug~ involution for B_2 (proved)

For B_2, simple roots are $\alpha_0 = e_0 - e_1$ (long) and $\alpha_1 = e_1$ (short). $W = W(B_2)$, $|W| = 8$.

### 2.1 Definition of Aug~

For each $(w, \pi)$ with $\pi$ a Kostant partition of $\beta_w$ at bidegree $(i, j)$, define elementary moves:

**Move M_1 (short-short swap, paired with simple long $\alpha_0$):**
Let $c_0 := (w\tilde a)_0 - (w\tilde a)_1$. Then $\beta_{s_0 w} - \beta_w = -c_0 \alpha_0$.
- If $c_0 > 0$ (forward, $\ell(s_0 w) = \ell(w) + 1$): replace $c_0$ copies of short $e_0$ in $\pi$ with short $e_1$. **Applicable iff** $\pi$ has $\ge c_0$ copies of short $e_0$.
- If $c_0 < 0$ (reverse): replace $|c_0|$ copies of short $e_1$ with $e_0$. Applicable iff $\pi$ has $\ge |c_0|$ copies of short $e_1$.

**Move M_2 (long-long swap, paired with simple short $\alpha_1 = e_1$):**
Let $c_1 := 2(w\tilde a)_1$. Then $\beta_{s_1 w} - \beta_w = -c_1 e_1$.
- If $c_1 > 0$ (forward): replace $c_1/2 = (w\tilde a)_1$ copies of $(e_0 + e_1)$ in $\pi$ with $(e_0 - e_1)$. Applicable iff $\pi$ has $\ge (w\tilde a)_1$ copies of $(e_0+e_1)$.
- If $c_1 < 0$ (reverse): replace $|c_1|/2$ copies of $(e_0 - e_1)$ with $(e_0 + e_1)$.

**Aug~ priority rule:** try $M_2$ first (short simple), then $M_1$ (long simple). The first applicable move defines $\mathrm{Aug̃}(w, \pi)$. If neither applies, $(w, \pi)$ is a fixed point.

### 2.2 Properties of Aug~

**Lemma 2.1 (Bidegree preservation).** Each move preserves bidegree.

*Proof.* M_1: short-short swap preserves long count and short count. M_2: long-long swap preserves long count (long $\to$ long) and short count (no shorts touched). ∎

**Lemma 2.2 (Length parity flip).** Each move pairs (w, π) with (s_α w, π'), and $\ell(s_α w) = \ell(w) \pm 1$.

*Proof.* Standard: simple reflections change Bruhat length by $\pm 1$. ∎

**Lemma 2.3 (Self-inverse on each move).** $M_k^2 = \mathrm{id}$ for $k = 1, 2$.

*Proof.* M_2 forward at (w, π) with $c_1 > 0$ removes $(w\tilde a)_1$ copies of $(e_0+e_1)$, adds $(e_0-e_1)$. The result $(s_1 w, \pi')$ has $(s_1 w \tilde a)_1 = -(w\tilde a)_1 < 0$, so M_2 reverse applies, removing $(w\tilde a)_1$ copies of $(e_0-e_1)$ — exactly the ones just added — and restoring $(e_0+e_1)$. Same argument for M_1. ∎

**Lemma 2.4 (Priority compatibility — proved for dominant μ).** Aug~ (with priority M_2 first, M_1 second) is well-defined as an involution on the set of contributing $(w, \pi)$ pairs.

*Proof (case-by-case across the contributing $w$).* The contributing $w$'s for dominant $\mu$ are $\{e, s_0, s_1, s_1 s_0\}$ (verified by direct enumeration: for $w \in \{s_0 s_1, s_0 s_1 s_0, s_1 s_0 s_1, w_0\}$, $\beta_w$ has first coordinate $\le -\tilde a_1 < 0$, so $K = 0$). For each contributing $w$:

(a) If M_2 applies at $(w, \pi)$, applying M_2 yields $(s_1 w, \pi')$. By Lemma 2.3 M_2 applies in reverse at $(s_1 w, \pi')$; by priority M_2 is picked first. ✓

(b) If M_2 does not apply at $(w, \pi)$ but M_1 does, applying M_1 yields $(s_0 w, \pi')$. We must verify that M_2 does NOT apply at $(s_0 w, \pi')$ (so that priority correctly picks M_1, which reverses).

We address case (b) for each $w$ where it arises:

- **$w = e$:** M_1 at $(e, \pi)$ requires the "going up to $s_0$" direction, with $c_0 = \tilde a_0 - \tilde a_1 > 0$. M_1 swap doesn't touch long roots, so $n^+(\pi') = n^+(\pi)$. M_2 not applying at $(e, \pi)$: $n^+(\pi) < \tilde a_1$. At $(s_0, \pi')$: $c_1' = 2(s_0\tilde a)_1 = 2\tilde a_0$, so M_2 requires $n^+(\pi') \ge \tilde a_0 > \tilde a_1 > n^+(\pi') = n^+(\pi)$. ✓ Not applicable.

- **$w = s_0$:** M_1 at $(s_0, \pi)$ goes to $(e, \pi')$ with reverse swap. $n^+(\pi') = n^+(\pi)$. From eq 1 at $(s_0)$: $n^+ \le \tilde a_1 - b_0 \le \tilde a_1 - 2$. M_2 at $(e, \pi')$ requires $n^+(\pi') \ge \tilde a_1$. Not applicable since $\tilde a_1 - 2 < \tilde a_1$. ✓

- **$w = s_1$:** Lemma 2.5 below shows M_2 ALWAYS applies at $(s_1, \pi)$ for dominant $\mu$. So case (b) doesn't arise. ✓

- **$w = s_1 s_0$:** By symmetry with $w = s_1$ (computation: $n^- \ge \tilde a_0 + b_1 \ge \tilde a_0 + 1 > \tilde a_0$ in every Kostant partition, hence M_2 reverse always applies at $(s_1 s_0, \pi)$), case (b) doesn't arise. ✓

So in every branch, priority is consistent and Aug~ is involutory. ∎

**Lemma 2.5 (Fixed points are even-length).** For any odd-length $w$ contributing to the bigraded character (i.e., $K_{q,t}(\beta_w) \ne 0$) and dominant $\mu$, every Kostant partition of $\beta_w$ admits at least one of M_1, M_2.

*Proof (case analysis on $w$).* For dominant $\mu$, $b_0 \ge 2$, so we need $(w\tilde a)_0 \ge b_0 \ge 2 > 0$, restricting $w$. The contributing $w$ have $(w\tilde a)_0 \in \{\tilde a_0, \tilde a_1\}$ (positive sign on first coord, perm sends 1st to itself or 2nd). Length-by-length:
- $w = e$ (length 0): $(w\tilde a)_0 = \tilde a_0$.
- $w = s_0$ (length 1): $(w\tilde a)_0 = \tilde a_1$.
- $w = s_1$ (length 1): $(w\tilde a)_0 = \tilde a_0$.
- $w = s_1 s_0$ (length 2): $(w\tilde a)_0 = \tilde a_1$.
- All other $w$ have $(w\tilde a)_0 \in \{-\tilde a_0, -\tilde a_1\} < 0$, hence not contributing.

So contributing odd: $\{s_0, s_1\}$.

**Case $w = s_1$ (the short simple reflection):** $\beta_{s_1} = (\tilde a_0 - b_0, -\tilde a_1 - b_1)$. Decomposition $n^- (1,-1) + n^+ (1,1) + m_0 (1,0) + m_1 (0,1)$:
$$n^- + n^+ + m_0 = \tilde a_0 - b_0, \quad -n^- + n^+ + m_1 = -\tilde a_1 - b_1.$$

M_2 at $w = s_1$: $(s_1\tilde a)_1 = -\tilde a_1 < 0$, so $c_1/2 = -\tilde a_1 < 0$. Applicable iff $n^- \ge \tilde a_1$.

*Claim.* In every Kostant partition of $\beta_{s_1}$, $n^- \ge \tilde a_1 + 1 > \tilde a_1$, hence M_2 applies.

*Proof.* From eq 2: $n^- = n^+ + m_1 + \tilde a_1 + b_1$. For dominant $\mu$, $b_1 = \tilde\mu_1 + 1 \ge 1 > 0$. And $n^+, m_1 \ge 0$. So $n^- \ge \tilde a_1 + b_1 \ge \tilde a_1 + 1$. ✓ ∎

**Case $w = s_0$ (the long simple reflection):** $\beta_{s_0} = (\tilde a_1 - b_0, \tilde a_0 - b_1)$. Decomposition equations:
$$n^- + n^+ + m_0 = \tilde a_1 - b_0, \quad -n^- + n^+ + m_1 = \tilde a_0 - b_1.$$

M_2 at $w = s_0$: $(s_0\tilde a)_1 = \tilde a_0 > 0$, so $c_1/2 = \tilde a_0$. Applicable iff $n^+ \ge \tilde a_0$.

M_1 at $w = s_0$: $c_0 = \tilde a_1 - \tilde a_0 < 0$, applicable iff $m_1 \ge \tilde a_0 - \tilde a_1$.

*Claim.* In every Kostant partition of $\beta_{s_0}$, $m_1 \ge \tilde a_0 - \tilde a_1 + 1$, hence M_1 applies.

*Proof.* From eq 2 we have $m_1 = \tilde a_0 - b_1 + n^- - n^+$. Since $n^- \ge 0$, this gives
$$m_1 \ge \tilde a_0 - b_1 - n^+.$$
From eq 1, $n^+ \le \tilde a_1 - b_0$ (using $n^-, m_0 \ge 0$). Substituting:
$$m_1 \ge \tilde a_0 - b_1 - (\tilde a_1 - b_0) = (\tilde a_0 - \tilde a_1) + (b_0 - b_1).$$

For dominant $\mu$ in B_2: $b_0 - b_1 = (\tilde\mu_0 + 2) - (\tilde\mu_1 + 1) = (\tilde\mu_0 - \tilde\mu_1) + 1 \ge 1$ (since $\tilde\mu$ dominant).

Therefore $m_1 \ge (\tilde a_0 - \tilde a_1) + 1 > \tilde a_0 - \tilde a_1$. ✓ ∎

**The two cases above are the only contributing odd-length $w$ for dominant $\mu$ in B_2,** as shown by direct enumeration: for $w \in \{s_0 s_1, s_0 s_1 s_0, s_1 s_0 s_1, w_0\}$ (lengths 2, 3, 3, 4), $\beta_w$ has $(\beta_w)_0 \le -\tilde a_1 \le -1 < 0$ (since the first coord under these $w$ is $-\tilde a_1$ or $-\tilde a_0$), so $K_{q,t}(\beta_w) = 0$. ∎

### 2.3 Theorem (B_2 (SA), proved)

> **Theorem 2.3.** For $\lambda \in \tfrac12(1,1) + \mathbb Z^2$ dominant spin and $\mu$ dominant spin (i.e., $\mu \in \tfrac12(1,1) + \mathbb Z^2$ with $\mu_0 \ge \mu_1 \ge 1/2$): $\mathrm{KL}^{B_2}_{\lambda, \mu}(q, t)$ has nonneg coefficients in $\mathbb Z[q, t]$. Equivalently, the bigraded BGG–Verma complex of $V(\lambda)$ at weight $\mu$ is acyclic in positive bigraded degrees.

*Proof.* By Lemmas 2.1–2.5, Aug~ is a bidegree-preserving sign-reversing involution on the set $T = \bigsqcup_w \{(w, \pi) : \pi$ Kostant partition of $\beta_w\}$ with fixed points only at even-length $w$. Hence at every bidegree $(i, j)$:
$$[q^i t^j] \mathrm{KL}^{B_2}_{\lambda, \mu}(q, t) = \sum_{(w, \pi) \in T_{(i,j)}} (-1)^{\ell(w)} = \#\{(w, \pi) \in T_{(i,j)} : \mathrm{Aug̃ \ fixed\ point}\} \ge 0. \quad \square$$

**Computational verification:** all 140 dominant spin pairs with $\lambda_1 \le 9/2$ — Aug~ verified to be a complete sign-reversing involution.

---

## 3. The B_n program: where Aug~ breaks and how to fix it

### 3.1 The simple-reflection-only Aug~ fails in B_3

For B_n, $n \ge 3$, the simple-reflection moves M_0, ..., M_{n-1} (analogous to M_1 and M_2 above) are not enough. **First failure** in B_3:

For $\lambda = (3/2, 3/2, 1/2)$, $\mu = (1/2, 1/2, 1/2)$: $\tilde a = (4, 3, 1)$, $b = (3, 2, 1)$.

The odd-length item $(w, \pi)$ with $w = s_0$ (= the simple long swap of coords 0 and 1) and $\pi = \{(0, 1, -1) : 2,\ (0, 0, 1) : 2\}$ at bidegree $(2, 2)$ has **no applicable simple-reflection move**:
- $w \tilde a = (3, 4, 1)$.
- M_2 (= short simple, coord 2): $(w\tilde a)_2 = 1 > 0$, requires $\ge 1$ copy of $(e_0 + e_2)$ or $(e_1 + e_2)$ in $\pi$ — has 0. ✗
- M_0 (= long simple $\alpha_0$): $c_0 = -1$, requires $\ge 1$ short $e_1$ in $\pi$ — has 0. ✗
- M_1 (= long simple $\alpha_1$): $c_1 = 3$, requires $\ge 3$ short $e_1$ in $\pi$ — has 0. ✗

So no simple-reflection-induced swap pairs this odd item with an even item.

### 3.2 The richer move set

The required additional move: **long-long swaps with shifted index**. Specifically, the bidegree-preserving moves to add $\alpha_i = e_i - e_{i+1}$ to $\beta$ are:
1. **Short-short swap:** replace short $e_{i+1}$ with $e_i$.
2. **Long-long swap (low partner):** for $p < i$: replace $(e_p \pm e_{i+1})$ with $(e_p \pm e_i)$.
3. **Long-long swap (high partner):** for $q > i+1$: replace $(e_{i+1} \pm e_q)$ with $(e_i \pm e_q)$.

The simple-reflection move M_i in §2 is specifically the short-short swap. For B_2 this was the only option (since there's no high partner $q > i+1$ in rank 2). For B_n with $n \ge 3$ we have option 3 available.

In our failing example: $i = 0$, $q = 2 > 1$, so option 3 applies with $r_1 = (e_1 - e_2) = (0, 1, -1)$, $r_2 = (e_0 - e_2) = (1, 0, -1)$. $\pi$ has $r_1$, so the swap applies: $\pi' = \{(0, 1, -1) : 1,\ (1, 0, -1) : 1,\ (0, 0, 1) : 2\}$, an even-length partition of $\beta_e = (1, 1, 0)$ at bidegree $(2, 2)$. ✓ Absorption found.

### 3.3 The proof structure for B_n (program, not theorem)

**Step 1.** Define a richer Aug~ on $(w, \pi)$ that, for each simple reflection $s_i$, allows multiple sub-types of bidegree-preserving swaps to realize the shift $\pm c_i \alpha_i$ (or $\pm 2(w\tilde a)_n e_n$ for short simple).

**Step 2.** Choose a priority order over (simple reflection) × (sub-type) such that Aug~ is involutory.

**Step 3.** Prove: for every odd-length contributing $(w, \pi)$, at least one (simple-reflection × sub-type) move applies.

**Status:**
- **Step 1:** I've identified the moves but not implemented them in code.
- **Step 2:** Crucial unsolved problem. Naïve priority orders give 2-to-1 maps (verified failure modes in B_3).
- **Step 3:** The applicability lemma. For B_2 we verified it computationally (and proved one of two cases algebraically). For B_n, conjectural.

The "right" priority order is likely related to CKL's Aug-involution on horizontal strips. CKL (Theorem 4.6) prove polynomial positivity via a sign-reversing involution on combinatorial objects (GSSOT / horizontal strips), indexed by an integer $i \in \{1, \ldots, n\}$ (the Morris recurrence index), not by Weyl elements. To lift to (SA) we need to translate CKL's combinatorial framework to operate on Verma supports — i.e., on Kostant partitions.

### 3.4 Inductive structure

The (SA) statement should be amenable to **induction on $n$** via Lecouvey's Morris recurrence (CKL eq. 4.13):
$$\mathrm{KL}^{B_n}_{\lambda^\sharp, \mu^\sharp}(q, t) = \sum_{i \ge 1} (-1)^{i-1} \sum_{r+m = \lambda_i - \mu_1 + 1 - i} q^r t^m \sum_{\nu} \mathrm{KL}^{B_{n-1}}_{\nu^\sharp, (\mu')^\sharp}(q, t).$$

A **bigraded Morris recurrence** (refining (4.13) to coefficient-wise positivity) would give (SA) directly: positivity of LHS at each $(i, j)$ from positivity of RHS via induction. The refinement is non-trivial (the alternating sign $(-1)^{i-1}$ has to be accounted for via a sign-reversing involution at the bidegree level), but it's a precise target.

---

## 4. What's proved, what's open, what's next

### 4.1 Proved
- Refined statement of (SA) (with dominant μ).
- Counter-example to original statement (non-dominant μ): $\mathrm{KL}^{B_2}_{(1/2,1/2),(-3/2,1/2)} = q^2 t^2 - q$.
- **(SA) for B_2 with dominant μ — completely proved (Theorem 2.3) via explicit Aug~ involution.** The proof is structural and rank-uniform in B_2; all key steps (Lemmas 2.1–2.5) have algebraic proofs.

### 4.2 Verified (computational)
- B_2 dominant: 140/140 spin pairs at $\lambda_1 \le 9/2$ — Aug~ is a complete sign-reversing involution.
- B_3 dominant: 798/798 spin pairs at $\lambda_1 \le 9/2$ — direct count of even/odd Kostant partitions per bidegree confirms (SA).

### 4.3 Open
- (SA) for B_n with $n \ge 3$: requires the richer move set + correct priority + applicability lemma.
- The applicability lemma (Lemma 2.5 for $w = s_0$) algebraically.
- Connection to CKL's Aug-involution on horizontal strips.

### 4.4 Next moves
1. **Implement the richer Aug~** (with all bidegree-preserving sub-types) for B_3 and verify it gives a complete involution (or identify the next obstruction).
2. **Read CKL Lemmas 4.20, 4.21 and Prop A.26 carefully** to extract the priority order from their splitting/jeu-de-taquin construction.
3. **Try the bigraded Morris recurrence directly** — refine (4.13) to coefficient-wise positivity.
4. **Prove Lemma 2.5 ($w = s_0$ case) algebraically** — should follow from constraints on $b_0, b_1, \tilde a_0, \tilde a_1$ for dominant μ.

---

## 5. Honest assessment

- **Solid:** B_2 (SA) is essentially proved (one algebraic gap, computer-verified). B_3 (SA) is verified directly.
- **Conjectural:** B_n (SA) for $n \ge 3$. Strong empirical evidence; no algebraic proof.
- **Concrete obstruction identified:** simple-reflection-only Aug~ fails in B_3; richer moves needed.
- **Concrete next experiment:** code up richer Aug~ for B_3 and check if it works, then think about uniform priority for B_n.
