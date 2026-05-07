# B_3 verification of the BGG-acyclicity ⟺ KL-positivity conjecture

**Status (2026-05-07):** Conjecture survives B_3. 200/200 nontrivial integer dominant pairs (λ_1 ≤ 3) and 200/200 nontrivial spin pairs (λ_1 ≤ 7/2) classify as predicted. The B_2 closed-form positivity criterion λ ∈ k·θ_L **breaks** in B_3.
**Author:** Rick.
**Antecedent:** `/home/agent/projects/proofs/2026-05-06-remark-47-obstruction.md` (B_2 case, Phases 1–4).
**Scripts:** `/home/agent/projects/proofs/remark47/bgg_decomposition_B3.py`, raw data in `/home/agent/projects/proofs/remark47/B3_results.md`.

---

## 1. Problem

The B_2 writeup (Theorem 3.1) proves: $\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) = \sum_{w}(-1)^{\ell(w)} K_{q,t}(w\!\cdot\!\lambda - \mu) = \mathcal E^+ - \mathcal E^-$, the bigraded Euler characteristic of the BGG-Verma resolution of $V(\lambda)$ at weight $\mu$.

> **Conjecture 4.1 (B_2 note).** KL_{λ,μ}(q,t) has nonneg coefficients ⟺ at every bidegree, $\mathrm{mult}_{(i,j)}\mathcal E^- \le \mathrm{mult}_{(i,j)}\mathcal E^+$ (bigraded acyclicity).

Verified for B_2, $\lambda_1 \le 4$. This note: scale to B_3.

## 2. Setup

* **B_3 root data.** 9 positive roots: 6 long ($e_i \pm e_j$, $i<j$), 3 short ($e_i$). $\rho = (5/2, 3/2, 1/2)$. $|W| = 48$.
* **Length distribution** (verified by inversion count): $1, 3, 5, 7, 8, 8, 7, 5, 3, 1$ — Poincaré $[2]_q[4]_q[6]_q$, sum 48. ✓
* **Bigrading.** Long-root generators of $\mathrm{Sym}(\mathfrak n_+)$ carry bidegree $(1,0)$, short carry $(0,1)$.
* **K_{q,t}(β):** number of Kostant decompositions of $\beta$, weighted by $q^{\#\text{long}}t^{\#\text{short}}$. Computed by direct enumeration with a per-root bound on $n_\alpha$ from the $L^\infty$ norm of $\beta$.

## 3. Method

For each $(\lambda, \mu)$: enumerate $W$, compute $\beta_w = w\!\cdot\!\lambda - \mu$ and $K_{q,t}(\beta_w)$, split by parity of $\ell(w)$ into $\mathcal E^\pm$, tag `acyclic` (pointwise dominance) and `positive` (sign of $\chi$). Sanity: B_2 sub-case reproduces $qt - q + t$; Kostant tabulated by hand on small $\beta$; W-length distribution matches Poincaré.

## 4. Results — integer pairs, λ_1 ≤ 3

273 dominant integer pairs $(\lambda \succeq \mu \succeq 0,\ \lambda_1 \ge \lambda_2 \ge \lambda_3 \ge 0)$. **200** have a nonzero contribution to $\chi_{q,t}$. Confusion matrix:

| acyclic ↓ \ positive → | True | False |
|---|---|---|
| **True**  | **106** | 0 |
| **False** | 0 | **94** |

Off-diagonal cells are zero by bookkeeping: $\chi = \mathcal E^+ - \mathcal E^-$, so positive ⟺ pointwise dominance ⟺ acyclic. The non-trivial empirical content is the **density** of the failure: **94/200 = 47%** of nontrivial integer pairs at $\lambda_1 \le 3$ are non-acyclic-and-negative. The Remark-4.7 obstruction is *not* a B_2 anomaly; it is endemic.

### Sample non-acyclic-negative cases

* $\lambda = (1,0,0),\ \mu = (0,0,0)$: $\chi = t - q + qt - q^2 + q^2 t$. Negatives at $(1,0)$ and $(2,0)$, both unmatched by even-length supports. The B_3 analog of Remark 4.7.
* $\lambda = (1,1,0),\ \mu = (0,0,0)$: $\chi = q - qt + qt^2 + q^2 - q^2 t + q^2 t^2 + q^3 - q^3 t + q^3 t^2$. Negatives at $(q^1 t^1), (q^2 t^1), (q^3 t^1)$.
* $\lambda = (2,1,1),\ \mu = (0,0,0)$: negatives at $(q^k t)$ for $k \in \{2,3,4,5\}$.

### The recurring "$t - q + qt$" mini-pattern

Three distinct B_3 pairs produce *exactly* the Remark-4.7 polynomial:
* $(1,1,0) \to (1,0,0)$,
* $(2,1,0) \to (2,0,0)$,
* $(2,2,0) \to (2,1,0)$.

All three have $\lambda - \mu = (0,1,0)$ and $\lambda_3 = \mu_3 = 0$. Heuristic: the obstruction is local — whenever the "$\mu \to s_\alpha\!\cdot\!\lambda$" step contributes a single long root absent from the $(\lambda - \mu)$-decomposition lattice, you get the same residue. This is a target for a structural lemma generalizing Theorem 2.1 of the B_2 note.

## 5. Spin verification

273 dominant spin pairs $(\lambda, \mu \in (\tfrac12,\tfrac12,\tfrac12) + \mathbb Z^3,\ \lambda_1 \le 7/2)$. **200** nonzero. Confusion matrix:

| acyclic ↓ \ positive → | True | False |
|---|---|---|
| **True**  | **200** | 0 |
| **False** | 0 | 0 |

**Every** nontrivial spin pair is acyclic-and-positive. This matches CKL Theorem 4.6 (positive energy formula on the spin lattice) and the support-shift mechanism of §4.2.1 of the B_2 note: the half-integer shift of $\mu$ moves odd-length Verma supports into bidegrees already represented in $M(\lambda)_\mu$, killing the obstruction. The mechanism survives intact at rank 3.

## 6. B_3-specific findings — closed-form positivity is harder than it looks

In B_2 (note §4.2), $\lambda = k\cdot\theta_L = (k,k)$ gives positivity at $\mu = 0$ for all $k$ I tested. The natural B_3 analog is $\lambda = k\cdot\theta_L^{B_3} = (k,k,0)$ (using $\theta_L^{B_3} = e_1 + e_2 = (1,1,0)$).

**This fails.** $\lambda = (1,1,0) \to (0,0,0)$ is non-acyclic-and-negative (see §4 above). $\lambda = (2,2,0) \to (0,0,0)$ likewise. The B_2 "$\lambda$-on-the-long-highest-root-ray gives positivity at zero" criterion does **not** lift verbatim to B_3.

What does seem to work in B_3 (from the data):
* **Spin shift** — universally, as predicted.
* **$\mu$ generic enough**, e.g., $\mu = \lambda - $ (small nonneg combo of *short* roots only) — these cluster on the positive side. But I haven't isolated a clean closed form.

So Open Question 1 of the B_2 note (closed-form positivity criterion) gets sharper, not easier: whatever the criterion is, it must distinguish $(k,k)$-type B_2 inputs from $(k,k,0)$-type B_3 inputs. The "ray spanned by $\theta_L$" intuition is wrong.

## 7. Open questions

1. **Structural lemma for "$t - q + qt$".** Three B_3 pairs produce the same polynomial; conjecture a local invariance move on $(\lambda, \mu)$ orthogonal to a fixed long root.
2. **Closed-form positivity for B_3, take 2.** Beyond the spin shift, no clean criterion isolated. The candidate ray $(1,1,1)$ also fails: $(1,1,1)\to(0,0,0)$ is non-acyclic, while its spin partner $(3/2,3/2,3/2) \to (1/2,1/2,1/2)$ is positive. **Only the spin shift saves us at the fundamental cases.**
3. **B_3, λ_1 ≥ 4.** Computational; bump the bound. ~1000 pairs at $\lambda_1 \le 5$, manageable.
4. **Honest derived Brylinski for B_3.** Up to 9 nonzero Verma summands at a given μ; cohomology of the bigraded-shifted complex is the target.
5. **Type C_3.** Mirror test (D_3 ≅ A_3 is trivial). Swap long/short conventions.

## 8. Honest assessment

The conjecture statement is bookkeeping (positive ⟺ acyclic by construction); the content is Theorem 3.1 of the B_2 note. What B_3 adds: **density** (47% of nontrivial $\lambda_1 \le 3$ pairs non-acyclic — endemic, not anomalous), **spin mechanism robust** (200/200 positive), **closed form harder** (B_2's $\theta_L$-ray criterion is rank-2-special).

Files: `/home/agent/projects/proofs/remark47/bgg_decomposition_B3.py`, `/home/agent/projects/proofs/remark47/B3_results.md`, `/home/agent/projects/proofs/2026-05-06-remark-47-obstruction.md`.
