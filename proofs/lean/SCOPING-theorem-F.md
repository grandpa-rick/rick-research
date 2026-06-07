# Lean Scoping: Theorem F (BDI Carry-Polytope Facet Structure)

**Date.** 2026-06-06 (created); 2026-06-07 (updated through `U_1`-redundancy).
**Status.** In progress. Lemmas 1 + 6 + 7 of §3 are type-checked under
lean 4.30.0 (pure stdlib, no Mathlib). See `bdi-polytope/BdiPolytope.lean`.
**Source.** `2026-05-21-bdi-kobayashi-faces.md` (Day-28 proof).
**Lean toolchain.** lean 4.30.0, lake 5.0.0, Mathlib (target: a recent release matching 4.30.0).

---

## 0. Goal

Formalize, in Lean 4 + Mathlib, the BDI carry-fence facet theorem:

> For $n \ge 2$, among the $2n - 1$ carry-derived candidate fences ($L_a, U_a$ for
> $a = 1, \dots, n-1$ and $E$) defining the HW chain polytope $\mathcal{P}_n$:
> (1) $L_1$ is dimension-collapsing (forces $M_1 = 0$);
> (2) $U_1$ is redundant;
> (3) the remaining $2n - 3$ are non-redundant facets.

This is a *combinatorial polyhedral* statement. The bulk of the work is **arithmetic
on prefix sums**, not deep convex geometry; only the facet-codim-1 verification really
needs polytope machinery, and we can sidestep most of it.

---

## 1. Data types

### 1.1 The configuration

A chain configuration at $B_n$ has coordinates
$$(M_a, B_a, T_a)_{a=1}^{n-1}, \qquad S,$$
all in $\mathbb{Z}_{\ge 0}$. Dimension $3(n-1) + 1$.

**Three options:**

**(A) Plain structure.**
```
structure ChainConfig (n : ℕ) where
  M : Fin (n-1) → ℕ
  B : Fin (n-1) → ℕ
  T : Fin (n-1) → ℕ
  S : ℕ
```
*Pros:* Closest to math. Direct field access. **Cons:** `Fin (n-1)` requires `n ≥ 1`;
for `n = 1` the type degenerates (empty Fin). For `n ≥ 2` it's fine.

**(B) Function on Fin.**
```
def ChainConfig (n : ℕ) := (Fin (n-1) → ℕ) × (Fin (n-1) → ℕ) × (Fin (n-1) → ℕ) × ℕ
```
*Pros:* Cleaner for sums/indexing. *Cons:* Tuple projections are ugly.

**(C) Single function over the disjoint union.**
Too clever; rejected.

**Decision: (A) with `n : ℕ` and `[hn : 2 ≤ n]` assumed as a global hypothesis** (or
parametrize over `n : ℕ` with the understanding that `n = 0, 1` cases are trivially
true via empty `Fin`). Use `Fin (n - 1)` directly — Mathlib handles `Fin 0` well.

### 1.2 Prefix sum $P_a$

$P_a = \sum_{b=1}^{a} 2(B_b - T_b)$, with $P_0 = 0$.

Note: $B_b - T_b$ can be negative (we're working over $\mathbb{Z}$, not $\mathbb{N}$).
So **$P_a$ must be an integer**, not a natural. This is the first design wrinkle.

**Two options:**

**(α) Make $M, B, T, S : \mathbb{Z}$ throughout** and add nonneg hypotheses as `Mₐ ≥ 0` etc.
*Pros:* No coercion noise. $P_a$ is naturally an `ℤ`-valued sum. Tactics like `linarith`,
`omega` work uniformly.

**(β) Keep $M, B, T, S : \mathbb{N}$ and cast** to ℤ when defining $P_a$.
*Pros:* Nonneg is structural. *Cons:* Constant `Int.coe_natCast` rewriting.

**Decision: (α) — work over `ℤ` with explicit nonneg hypotheses.** Mathlib's `omega`
and `linarith` are far happier on `ℤ`. Save coercion pain for later.

### 1.3 Should $P_a$ be a `def` or a derived field?

**`def`**, recursively or as a `Finset.sum`. Both work; pick `Finset.sum` for
algebraic identities or `Nat.rec` for the carry recursion. Probably:
```
def P (c : ChainConfig n) : Fin n → ℤ
  | ⟨0, _⟩ => 0
  | ⟨a+1, h⟩ => P c ⟨a, _⟩ + 2 * (c.B ⟨a, _⟩ - c.T ⟨a, _⟩)
```
or equivalently `∑ b in Finset.range (a+1), 2 * (B b - T b)`.

**Use the `Finset.sum` form** for `simp`-friendliness; prove the recursion as a lemma.

### 1.4 The HW predicate

```
def IsHW (c : ChainConfig n) : Prop :=
  (∀ a, c.M a ≥ 0) ∧ (∀ a, c.B a ≥ 0) ∧ (∀ a, c.T a ≥ 0) ∧ c.S ≥ 0 ∧
  (∀ a, c.M a ≤ P c (predecessor a))   -- L_a
  ∧ (∀ a, c.M a ≤ P c a)               -- U_a
  ∧ c.S ≤ P c (last n)                  -- E
```

(Index gymnastics on `Fin n` vs `Fin (n-1)` will need care; `predecessor` and `last`
need clean Mathlib names.)

### 1.5 The fence inequalities as a labeled family

```
inductive Fence (n : ℕ) where
  | L : Fin (n-1) → Fence n   -- L_a, a ∈ {0, ..., n-2}, corresponding to math indices 1..n-1
  | U : Fin (n-1) → Fence n
  | E : Fence n
```

Then `satisfies : ChainConfig n → Fence n → Prop` and `IsHW c ↔ ∀ f, satisfies c f ∧ nonneg`.

This is useful for stating "non-redundant" uniformly.

---

## 2. Statement of Theorem F (pseudo-Lean)

### Part 1: $L_1$ collapses dimension

```
theorem L1_collapse {n : ℕ} (hn : 2 ≤ n) (c : ChainConfig n) (h : IsHW c) :
    c.M 0 = 0 := by
  -- L_1 says M_1 ≤ P_0 = 0; nonneg says M_1 ≥ 0.
  have h1 : c.M 0 ≤ P c 0 := h.L 0
  have h2 : P c 0 = 0 := P_zero c
  have h3 : c.M 0 ≥ 0 := h.nonneg.M 0
  linarith
```

### Part 2: $U_1$ redundancy

```
theorem U1_redundant {n : ℕ} (hn : 2 ≤ n) (c : ChainConfig n)
    (hNonneg : ∀ a, c.M a ≥ 0) (hNonneg_S : c.S ≥ 0)
    (hL1 : c.M 0 ≤ P c 0)
    (hRest : if n = 2 then c.S ≤ P c (n-1) else c.M 1 ≤ P c 0) :
    c.M 0 ≤ P c 1 := by
  -- M_1 = 0 by L_1 + nonneg; P_1 ≥ 0 by next-downstream constraint + nonneg
  sorry
```

(The dependence on `n = 2 vs n ≥ 3` makes this slightly fiddly; might split into two
theorems.)

### Part 3: Each remaining fence is a non-redundant facet

Non-redundancy is the easier half — exhibit a witness:

```
theorem L_a_nonredundant {n : ℕ} (hn : 3 ≤ n) (a : Fin (n-1)) (ha : 1 ≤ a.val) :
    ∃ c : ChainConfig n,
      (∀ f : Fence n, f ≠ Fence.L a → satisfies c f) ∧
      ¬ satisfies c (Fence.L a) := by
  -- Construct: M_a = 1, B_a = 1, else 0. Compute P, check.
  sorry
```

Similar for `U_a_nonredundant` (`a ≥ 2`) and `E_nonredundant`.

**Facet** (codim-1) is harder. Two routes:

**(F-easy)** Prove only non-redundancy. This is a fully *combinatorial* statement;
"facet" is just a *name* for "non-redundant codim-1 face." If we don't formalize the
ambient `convexHull` / `Polyhedron` infrastructure, we lose nothing combinatorial.
**Recommended for first pass.**

**(F-hard)** Formalize the polytope $\mathcal{P}_n \subset \mathbb{R}^{3(n-1)+1}$ as a
convex set, prove its dimension is $3(n-1)$ (one less than ambient, due to $M_1 = 0$),
prove the saturation locus of each non-redundant fence has dimension $3(n-1) - 1$.
**Substantial work; defer to a Day-50+ project.**

**Decision: Aim for (F-easy) only.** Replace "facet" in the statement by
"non-redundant inequality" and "saturation locus has an interior point" by "there
exists a configuration where this fence is tight and all others are strict."

---

## 3. Decomposition into tractable lemmas

In rough order of difficulty:

1. **`P_zero : P c 0 = 0`** — definitional. ✅ Done (Day 55).
2. **`P_succ : P c (a+1) = P c a + 2 * (c.B a - c.T a)`** — definitional (the recursion). ✅ Done (Day 55).
3. **`L1_implies_M1_zero`** — Part 1 of the theorem. One-step `linarith`. ✅ Done (Day 55).
4. **`P1_nonneg_from_L2_M2_nonneg` (n ≥ 3)** — chain $L_2 \wedge M_2 \ge 0 \Rightarrow P_1 \ge 0$. ✅ Absorbed into omega in lemma 6 — no need to factor out.
5. **`P1_nonneg_from_E_S_nonneg` (n = 2)** — chain $E \wedge S \ge 0 \Rightarrow P_1 \ge 0$. ✅ Absorbed into omega in lemma 7 — no need to factor out.
6. **`U1_redundant_n_ge_3`** — combines 3, 4 to derive $U_1$. ✅ Done (Day 56) — single `omega` after invoking lemma 3.
7. **`U1_redundant_n_eq_2`** — combines 3, 5 to derive $U_1$. ✅ Done (Day 56) — same shape using `S_nonneg` and `hE : S ≤ P_1`.
8. **`L_a_witness_satisfies_other_fences` (a ≥ 2)** — bulk arithmetic on prefix sums.
9. **`L_a_witness_violates_L_a`** — single-line check.
10. **`U_a_witness_satisfies_other_fences` (a ≥ 2)** — same shape as 8.
11. **`U_a_witness_violates_U_a`** — single line.
12. **`E_witness_satisfies_others`** — trivial; only $S = 1$ is nonzero.
13. **`E_witness_violates_E`** — `1 > 0`.
14. **Bundle 8–13 into `nonredundancy_thm`**.
15. *(Optional, hard)* **`facet_interior_witnesses`** — type-uniform interior witnesses
    from §"Facet verification" of the proof doc; saturate exactly one fence.

Lemmas 1–7 are the entire "structural" part. **Through Day 56, 1+6+7 are done; 4 and 5
collapse into them so the structural half of Theorem F is complete in 18 lines of Lean,
no Mathlib.**

Lemmas 8–13 are bookkeeping over `Fin (n-1)` that `omega` + `decide` should handle
after the right `simp` normalization. *Open question:* my current `ChainConfig` indexes
`M, B, T` by `Nat` (total functions) rather than `Fin (n-1)`. For witnesses we'll need
to either (a) commit to `Fin` (and add an `n : Nat` field to `ChainConfig`), or
(b) keep `Nat` indexing and construct witnesses as explicit `Nat → Int` functions with
`Nat.casesOn`-style definitions. **(b)** keeps us stdlib-only; **(a)** is closer to the
math but introduces a `Fin (n-1)` empty-when-`n=0` corner case that needs `[hn : 2 ≤ n]`.
Decide next session — probably **(b)** to stay Mathlib-free as long as possible.

### Re-ranking remaining lemmas by easiness (Day 56)

The next-cheapest lemmas to attack:

- **13 (`E_witness_violates_E`)** — literally `1 > 0`. Trivial; do it as a warmup.
- **12 (`E_witness_satisfies_others`)** — construct the witness `S = 1`, all else 0,
  then unfold P recursively. Should be `simp` + `omega`.
- **9 (`L_a_witness_violates_L_a`)** — single inequality at one index. `omega`.
- **11 (`U_a_witness_violates_U_a`)** — same shape as 9.
- **8, 10** — bulk arithmetic; the real work. Need a lemma about $P$ on the carry witness.

Recommend: next session = lemmas 12 + 13 (the `E` witness, fully done).

---

## 4. First lemma to try

**`L1_implies_M1_zero`** (lemma 3 above).

```
theorem L1_implies_M1_zero {n : ℕ} (hn : 2 ≤ n) (c : ChainConfig n)
    (hL1 : c.M ⟨0, by omega⟩ ≤ P c ⟨0, by omega⟩)
    (hNonneg : 0 ≤ c.M ⟨0, by omega⟩) :
    c.M ⟨0, by omega⟩ = 0 := by
  have : P c ⟨0, by omega⟩ = 0 := P_zero c
  linarith
```

This is a one-step `linarith` after evaluating $P_0 = 0$. It's the right first lemma
because:

- It exercises the data type (`ChainConfig`, `Fin`, `P`).
- It hits the `P_zero` definitional lemma (forces us to commit to the def).
- No witness construction needed.
- Trivial Mathlib dependency (`Mathlib.Tactic.Linarith` only).
- If it compiles, the data design is sound.

**Effort estimate: 1 session** (including type design + getting `P_zero` to fire).

---

## 5. Mathlib dependencies anticipated

For the (F-easy) approach:

- `Mathlib.Data.Fin.Basic` — `Fin (n-1)`, `Fin.succ`, `Fin.castSucc`, `Fin.last`.
- `Mathlib.Algebra.BigOperators.Basic` — `Finset.sum` for $P_a$.
- `Mathlib.Tactic.Linarith` and `Mathlib.Tactic.Omega` — the workhorses.
- `Mathlib.Data.Int.Basic` — just `ℤ`.
- `Mathlib.Logic.Basic` — `Or`/`And` manipulation.
- `Mathlib.Tactic.FinCases` — case analysis on small `Fin`.

For (F-hard), additionally:

- `Mathlib.Analysis.Convex.Hull` / `Mathlib.Analysis.Convex.Polytope` — convex hulls.
- `Mathlib.LinearAlgebra.AffineSpace.AffineSubspace` — affine span, codimension.
- `Mathlib.Analysis.Convex.Cone.Pointed` — possibly for the recession cone.

**For first session: only `Linarith`, `Omega`, `Fin.Basic`, `Int.Basic`.**

---

## 6. Effort estimate

**(F-easy) full theorem.** Lemmas 1–14:

- Session 1: install + `lakefile` + `ChainConfig` design + `P_zero` + lemma 3. *(Today's
  goal once we start.)*
- Session 2: `P_succ`, `IsHW` predicate, lemmas 4–7 (`U_1` redundancy).
- Session 3: `Fence` inductive + witness for $E$ (lemmas 12, 13).
- Session 4: Witnesses for $L_a$ — bulk index manipulation + prefix-sum computation.
- Session 5: Witnesses for $U_a$ — similar shape.
- Session 6: Bundling, statement of `theorem_F_easy`, cleanup.

**Total: ~6 sessions for the (F-easy) version. Lemma 1 alone: 1 session.**

**(F-hard) full facet codim-1.** Add ~4 sessions for the polytope-machinery infrastructure
(saturation locus dim arguments, interior witnesses). Realistic total: 10 sessions, plus
risk that Mathlib's convex polytope API is thin (still under development as of Mathlib
2025–2026) and we end up rolling our own affine-span arguments.

**Recommendation: lock in (F-easy) as the deliverable. Treat (F-hard) as a stretch.**

---

## 7. Open questions for Robin

1. **Is "non-redundant inequality" enough, or do you want the full "codim-1 facet"
   statement?** The former is cleanly Lean-able in 6 sessions; the latter adds ~4
   more and depends on Mathlib's convex API maturity.
2. **Polynomial ring vs explicit coordinate type?** A more abstract approach would
   define $\mathcal{P}_n$ as `{x : Fin (3*(n-1)+1) → ℤ // ...}` and let Mathlib's
   polytope machinery do the work. Probably premature.
3. **Should we use `ℕ` everywhere with subtraction-safe lemmas, or `ℤ` with
   nonneg hypotheses?** Recommend `ℤ` (see §1.2(α)); confirm.
4. **Naming.** I'm using `ChainConfig`, `IsHW`, `Fence`, `P`. Any preferred conventions?

---

## 8. Status

- Lean 4.30.0 + Lake 5.0.0 installed; toolchain works.
- ~~Scoping doc complete. **No Lean code written yet** — that's session 1's work.~~
- **Day 55:** `ChainConfig`, `P`, `P_zero`, `P_succ`, `L1_implies_M1_zero` ✅
- **Day 56:** `U1_redundant_n_ge_3`, `U1_redundant_n_eq_2` ✅. Structural half of
  Theorem F (lemmas 1–7) is done in `BdiPolytope.lean` (~80 lines, pure stdlib).
- Decision validated: pure `Int` + `omega` is enough for the structural half. No
  Mathlib has been needed so far, contrary to the §5 anticipation.
- Open question for Robin: should we keep `Nat`-indexing for witnesses (lemmas 8–13)
  or switch to `Fin (n-1)`? See §3 re-ranking discussion above.

— Rick
