## Lean Scoping: Theorem G (BDI Weight-Space Simplicial Cone)

**Date.** 2026-06-10 (Day 60 LEAN).
**Status.** Scoping; some definitions+sanity lemmas typecheck (see §8).
**Source.** `proofs/2026-05-21-weight-space-projection.md` (Day-29 deep work).
**Lean toolchain.** Lean 4.30.0, Lake 5.0.0, **pure stdlib (no Mathlib)** —
continuing the (F-easy) stdlib bundle in `BdiPolytope.lean`.

---

### 0. Goal

Formalize Theorem G:

> For $n \ge 2$, the weight-space image cone $\mathcal{K}_n \subseteq \mathbb{R}^n$ is the
> rational polyhedral cone with H-representation
> $$
> \lambda_1 + \cdots + \lambda_k \ge 0 \quad (k = 1, \dots, n-2),
> \quad \sum_{i=1}^{n} \lambda_i \ge 0,
> \quad \lambda_n \le \lambda_1 + \cdots + \lambda_{n-1}.
> $$
> These $n$ inequalities are pairwise non-redundant facets; equivalently
> $\mathcal{K}_n$ is a **simplicial cone**.

The $n$ extreme rays of $\mathcal{K}_n$ (1D faces obtained by intersecting $n-1$
of the $n$ facets) are explicitly:

* "Pair rays" $r_k = e_k - e_{k+1}$ for $k = 1, \dots, n-2$ (math 1-indexed;
  $n - 2$ rays).
* "Sum ray" $r_{\text{sum}} = e_{n-1} + e_n$.
* "$E$ ray" $r_E = e_{n-1} - e_n$.

Total: $(n-2) + 2 = n$ rays. Note: **the rays have negative entries**, so
they live in $\mathbb{Z}^n$, not $\mathbb{Z}_{\ge 0}^n$. This is important
for the type signature — `Nat → Int`, not `Nat → Nat`.

---

### 1. Data design

Following the (F-easy) `BdiPolytope.lean` convention:

* Use **`Int`** for weight coordinates (rays have $-1$ entries).
* Use **`Nat`** indexing on `Nat → Int` total functions, with the user
  responsible for staying in `{0, ..., n-1}`.
* Keep `n : Nat` as the type-level parameter (passed by argument to defs).
* **No `Fin n`** unless forced; stdlib bundle.

Pure-stdlib means: no `Finset.sum`. Partial sums defined by recursion.

```lean
def partialSum (v : Nat → Int) : Nat → Int
  | 0      => 0
  | k + 1  => partialSum v k + v k
```

So `partialSum v k = v 0 + v 1 + ... + v (k-1)`, which under "v i = λ_{i+1}"
gives `partialSum v k = λ_1 + ... + λ_k` (math 1-indexed).

### 1.1 Cone membership predicate

```lean
def InKone (n : Nat) (v : Nat → Int) : Prop :=
  (∀ k : Nat, 1 ≤ k → k ≤ n - 2 → 0 ≤ partialSum v k)
  ∧ (0 ≤ partialSum v n)
  ∧ (v (n - 1) ≤ partialSum v (n - 1))
```

* First conjunct: partial-sum facets $\lambda_1 + \cdots + \lambda_k \ge 0$
  for $k = 1, \dots, n-2$.
* Second conjunct: full-sum facet $\sum_{i=1}^{n} \lambda_i \ge 0$.
* Third conjunct: $E$-facet $\lambda_n \le \sum_{i=1}^{n-1} \lambda_i$.

Degeneracies:
* $n = 2$: first conjunct vacuous (range $k = 1$ to $0$ empty). Two
  facets: $\lambda_1 + \lambda_2 \ge 0$, $\lambda_2 \le \lambda_1$. Matches §4.1.
* $n = 0, 1$: degenerate (formula returns `True` for first two; "v (n-1)" is
  v 0 or v (-1) = v 0 due to Nat subtraction). Not in scope.

### 1.2 The $n$ extreme rays

Single function indexed by `i : Nat` in `{0, ..., n-1}`:

```lean
def extremeRay (n : Nat) (i : Nat) (j : Nat) : Int :=
  if i + 2 ≤ n - 1 then
    -- pair ray: e_i - e_{i+1}  (0-indexed; math i+1 = 1, ..., n-2)
    if j = i then 1 else if j = i + 1 then -1 else 0
  else if i + 1 = n - 1 then
    -- sum ray: e_{n-2} + e_{n-1}  (0-indexed)
    if j = n - 2 then 1 else if j = n - 1 then 1 else 0
  else  -- i = n - 1
    -- E ray: e_{n-2} - e_{n-1}  (0-indexed)
    if j = n - 2 then 1 else if j = n - 1 then -1 else 0
```

Or, for clarity in proofs, three separate functions `pairRay`, `sumRay`,
`eRay`. **Decision:** three separate functions. Better targeting for `omega`
in lemma proofs. (Single function would mean every lemma starts with
case-split on `i + 2 ≤ n - 1`.)

```lean
def pairRay (k : Nat) (j : Nat) : Int :=
  if j = k then 1 else if j = k + 1 then -1 else 0

def sumRay (n : Nat) (j : Nat) : Int :=
  if j = n - 2 then 1 else if j = n - 1 then 1 else 0

def eRay (n : Nat) (j : Nat) : Int :=
  if j = n - 2 then 1 else if j = n - 1 then -1 else 0
```

---

### 2. Theorem G (Lean form)

```lean
theorem K_simplicial (n : Nat) (hn : 2 ≤ n) :
    -- "K_n is simplicial cone with n rays" =
    -- (a) every cone-membership v in InKone n
    -- (b) admits a nonneg integer combination
    --     v = c_1 · r_1 + ... + c_n · r_n
    -- (c) and (b) coefficients are unique.
    ∀ v : Nat → Int, InKone n v →
      ∃! (c : Nat → Nat), ∀ j : Nat, j < n →
        v j = (∑_{i = 0}^{n-1} (c i : Int) * (extremeRay n i j))
```

(`∑` here is a stdlib recursion / fold over Nat, not Mathlib.) The
"existence" half is the constructive content; "uniqueness" follows from
the rank-$n$ linear independence of the rays.

---

### 3. Decomposition into lemmas

In order of (anticipated) difficulty:

1. **`partialSum_zero`** — `partialSum v 0 = 0`. Definitional `rfl`.
2. **`partialSum_succ`** — `partialSum v (k+1) = partialSum v k + v k`. `rfl`.
3. **`pairRay_eval_at_k`**, **`pairRay_eval_at_k_plus_one`**, etc. —
   evaluation sanity. `decide` or `rfl` + `simp`.
4. **`pairRay_in_Kone`** (n ≥ 3) — `InKone n (pairRay k)` for
   $0 \le k \le n - 3$. **Easiest non-trivial lemma.** Each facet
   inequality reduces to `0 ≤ 0` or `0 ≤ 1` after evaluating partialSum
   at the relevant `k`s, modulo `omega`.
5. **`sumRay_in_Kone`** (n ≥ 2) — `InKone n (sumRay n)`. Same shape, fewer
   nonzeros.
6. **`eRay_in_Kone`** (n ≥ 2) — `InKone n (eRay n)`. Same shape.
7. **`extremeRay_lin_indep`** — the $n \times n$ matrix of rays has
   `det = ±2`. Lower-triangular structure (see scratch §4 below) reduces
   to a $2 \times 2$ determinant computation. **Hard without Mathlib's
   `Matrix.det`** — stdlib has no `det`. Alternative: prove a custom
   "decomposition uniqueness" lemma by exhibiting an explicit inverse.
8. **`Kone_subset_conic_hull`** (the hard half of `K_simplicial`) — every
   `v` satisfying the H-rep is a nonneg integer combination of the rays.
   Constructive proof: read off coefficients via partial-sum differences.
9. **`Kone_eq_conic_hull`** — combines 4–8.

### 3.1 Re-ranking by easiness (post-scoping)

Lemmas 1, 2 are `rfl`. Lemmas 3 are `decide` (small finite checks). The
first real proof obligations are lemmas 4–6 (each ray $\in K_n$).

Step 3 of LEAN.md says "pick the easiest of the five lemmas and attempt".
**Decision: attempt lemma 5 (`sumRay_in_Kone`) first**, then 6, then 4.
The sumRay and eRay are simpler than pairRay because they only have
nonzero entries at the last two positions $n - 2, n - 1$; partial sums
$\le n - 2$ all vanish, and the facet inequalities all reduce to one of
$\{0 \le 0, 0 \le 1, 0 \le 2, -1 \le 1\}$ after evaluation.

---

### 4. Linear-independence: matrix structure

For $n = 3$ the ray matrix (rows = rays in math 1-indexed coords):
$$
\begin{pmatrix} r_1 \\ r_{\text{sum}} \\ r_E \end{pmatrix} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & -1 \end{pmatrix}, \quad \det = -2.
$$

General $n$: rows $0, \dots, n - 3$ are pair rays with leading 1 at
distinct columns $0, \dots, n - 3$. Rows $n - 2, n - 1$ (sum, E) both
have leading 1 at column $n - 2$. After row reduction (subtract row
$n - 2$ from row $n - 1$): the resulting $(n - 2 \times n - 2)$ identity
block + $2 \times 2$ block $\begin{pmatrix} 1 & 1 \\ 0 & -2 \end{pmatrix}$
at bottom-right. So $|\det| = 2$ for all $n \ge 2$.

In particular: the rays span $\mathbb{Z}^n$ with index 2 (i.e., the lattice
they generate has index 2 in $\mathbb{Z}^n$). This means *some* integer
points of $\mathcal{K}_n$ may NOT be nonneg integer combinations of the
rays — they'd be nonneg *half-integer* combinations. So the simpliciality
statement is over $\mathbb{Q}_{\ge 0}$, not $\mathbb{N}$.

**For Lean:** state lemma 8 over `Int`-coefficients with a `2 |` (divides 2)
correction factor, or restrict to even-multiplicity points, or just state
it qualitatively without uniqueness witnessing the coefficients.

This is an important wrinkle the trigger LEAN.md missed.

---

### 5. Stdlib dependencies anticipated

* `Mathlib` — none.
* `Nat`, `Int`, `Decidable`.
* Tactics: `decide`, `simp`, `omega`, `rfl`, `split`.
* Avoid `Finset.sum` (Mathlib) — use recursive `partialSum`.

---

### 6. Effort estimate

* Session 1 (today): scoping doc, definitions, lemmas 1–3, attempt 5 (sumRay).
* Session 2: lemmas 4, 6 (pairRay, eRay in Kone).
* Session 3: lemma 7 (linear independence) via explicit inverse construction.
* Session 4: lemma 8 (conic hull). HARD without Mathlib; may need
  inductive coefficient extraction.
* Session 5: bundling, statement of `K_simplicial`.
* Session 6: cleanup.

**Total: 6 sessions (matches F-easy effort).**

---

### 7. Open questions for Robin

1. **Lattice index 2.** The ray lattice has index 2 in $\mathbb{Z}^n$.
   Statement target: $\mathbb{Q}_{\ge 0}$-cone equality, or refined
   integer statement with index-2 correction? §4 above.
2. **Indexing.** Still pending (Nat vs `Fin (n-1)`). Continuing with Nat
   per (F-easy) precedent.
3. **Is the `sorry`-bundle approach OK** (state `K_simplicial` with a
   sorry, get the wrappers shipped, then prove lemmas in subsequent
   sessions), or "incremental: only state what is proved"?

---

### 8. Status (Day 60, this session)

**Headline.** All three "each ray ∈ K_n" lemmas proved.  Lemma 2 of §3 is
DONE in three forms (pair ray, sum ray, E ray).  Lemma 3 (lin-indep) NOT
attempted this session.

In the Lean source `BdiPolytope.lean`:

* §1, §2 design committed.
* `partialSum`, `pairRay`, `sumRay`, `eRay`, `InKone` definitions added.
* `partialSum_zero`, `partialSum_succ` (`@[simp]`, `rfl`).
* Sanity eval lemmas: `pairRay_at_k`, `pairRay_at_succ`, `pairRay_off`,
  `sumRay_at_n_minus_two`, `sumRay_at_n_minus_one`, `sumRay_off`,
  `eRay_at_n_minus_two`, `eRay_at_n_minus_one`, `eRay_off`.
* Partial-sum profiles: `partialSum_sumRay_low/n_minus_one/n`,
  `partialSum_eRay_low/n_minus_one/n`, `partialSum_pairRay_le_k/at_succ/
  ge_k_plus_two`.
* **Lemmas G-4, G-5, G-6**: `pairRay_in_Kone`, `sumRay_in_Kone`,
  `eRay_in_Kone`.  Each verifies an extreme ray of `K_n` is in `K_n`.
* `pairRay_in_Kone` requires `3 ≤ n` and `k + 3 ≤ n` (matching math
  range `k = 1, …, n - 2`, 0-indexed `0, …, n - 3`).
* `sumRay_in_Kone` and `eRay_in_Kone` require `2 ≤ n`.

`lake build` clean: zero errors, zero warnings, zero sorries.
**File: 371 lines** (was 109 at start of session).

**Pending for next LEAN session:**
* Lemma 3: linear independence of the `n` rays.  Approach: explicit
  inverse-matrix construction (no Mathlib `det`).  The lower-triangular
  structure (see §4) reduces to a `2 × 2` determinant `= -2`.
* Lemma 4: cone-hull surjection — every `v ∈ K_n` is a nonneg
  combination of the `n` rays.  Index-2 caveat from §4 means the
  combination is over `(1/2) ℕ`, not `ℕ` — state target carefully.
* Lemma 5: uniqueness of coefficients, from rank-`n` independence.
* Bundle: state `K_simplicial` corollary.

— Rick (Day 60 LEAN, this session)
