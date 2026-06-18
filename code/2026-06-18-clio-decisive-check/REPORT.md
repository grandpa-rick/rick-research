# REPORT — Clio's decisive check (Day 78, 2026-06-18)

**Question (Clio review §9 Q1, sharpened in CODE.md Day 78):**

> Over ALL feasible n = 6 pieces (not just the 53-piece augmented
> registry), is the lattice point `e_{B_i} + 2 e_S ∈ T_n` coverable by
> any piece whose `p_i`-column is *not* `e_{B_i} + 2 e_S` (i.e., via a
> lifted `p_{i-1} + l_i` or `p_{i-1} + s_i` pair/triple ray)?

Same question for `α = 1`. Repeated for `n = 5, 6, 7`.

---

## 1. Headline

**YES — at every n ∈ {5, 6, 7}, every interior i ∈ {2, ..., n-2}, every α ∈ {1, 2}.**

The single-piece answer is unambiguous: explicit, F-feasible piece
witnesses exist with `π^{p_i} ≠ e_{B_i} + α e_S` and
`e_{B_i} + α e_S ∈ Im(π)`. All 12 of the n=6 witnesses are **OUTSIDE** the
53-piece augmented registry.

This puts the gap precisely where Clio relocated it: not in
feasibility, but in **whether the replacement piece's image is
compatible with the rest of a minimal cover** — i.e., whether dropping
`simpdiv_p_i_a_α` and adding a non-`α` carrier keeps the joint image ⊇ T_n.
The 3-clique on `{p_i = 0, 1, 2}` at interior `i` is *droppable* in the
single-piece sense.

---

## 2. The support-reduction lemma (the key combinatorial fact)

The all-feasible enumeration looks intractable a priori. It is not —
because the target T has very small coord-sum (2 or 3), and BDI rules
out e_S as a standalone ray. Concretely:

**Lemma (proven in `decisive_check.py` docstring; verified
computationally in `verify_support_lemma_corollary`):**

Let T = e_{B_i} + α e_S with α ∈ {1, 2}, 1 ≤ i ≤ n-1. Suppose
T = Σ_k a_k r_k where each r_k is a BDI vector (= ray-image of some
F-feasible piece) and a_k ∈ ℤ_{≥0}. Then exactly one r_k contributes
(with multiplicity 1) and equals T itself.

**Sketch:** any contributing ray r_k must have supp(r_k) ⊆ supp(T) =
{B_i, S} and r_k ≤ T coordinate-wise. The only BDI candidates are
{0, e_{B_i}, e_{B_i}+e_S, e_{B_i}+2e_S} — because e_S alone fails BDI
(S=1 > P_{n-1}=0) and BDI on supp ⊆ {B_i, S} forces S ≤ 2 B_i. A 2-
equation count (B_i-sum=1, S-sum=α) then uniquely identifies the
contributing-ray decomposition as a single ray equal to T.

**Corollary (defensive computational check, 18/18 cases ✓):**
in a piece whose every column is supported on {B_j : j ≠ i} (no S
contribution anywhere), T is NOT in the image semigroup. Confirms
the lemma by example.

This reduces Clio's question to:

> Does an F-feasible piece exist with `p_i ≠ T` but some OTHER ray = T?

The piece has 3n-1 rays; excluding the p_i slot, 3n-2 candidate ray-
slots remain. Each is a finite F-feasibility check.

---

## 3. Task A — single-piece enumeration (n = 5, 6, 7)

`decisive_check.py` enumerates witness pieces for every alternative
ray-slot at every (n, i, α):

| n | interior i | α | # routes tried | # routes that work | answer |
|---|----:|---:|---:|---:|:---:|
| 5 | 2 | 1 | 27 | 25 | **YES** |
| 5 | 2 | 2 | 27 | 25 | **YES** |
| 5 | 3 | 1 | 27 | 25 | **YES** |
| 5 | 3 | 2 | 27 | 25 | **YES** |
| 6 | 2 | 1 | 34 | 32 | **YES** |
| 6 | 2 | 2 | 34 | 32 | **YES** |
| 6 | 3 | 1 | 34 | 32 | **YES** |
| 6 | 3 | 2 | 34 | 32 | **YES** |
| 6 | 4 | 1 | 34 | 32 | **YES** |
| 6 | 4 | 2 | 34 | 32 | **YES** |
| 7 | 2 | 1 | 41 | 39 | **YES** |
| 7 | 2 | 2 | 41 | 39 | **YES** |
| 7 | 3 | 1 | 41 | 39 | **YES** |
| 7 | 3 | 2 | 41 | 39 | **YES** |
| 7 | 4 | 1 | 41 | 39 | **YES** |
| 7 | 4 | 2 | 41 | 39 | **YES** |
| 7 | 5 | 1 | 41 | 39 | **YES** |
| 7 | 5 | 2 | 41 | 39 | **YES** |

The 2 "failing" routes in each row are the two `p_{j-1} + (l|s)_j = T`
decompositions in which `j-1 = i` AND the decomposition routes the whole
of T through `p_{j-1} = p_i`, which would set `p_i = T` and violate the
constraint. They are not feasibility failures — they are constraint
violations of the witness construction itself.

### Three families of witnesses (each gives YES on its own)

For each (n, i, α), at least three independent routes succeed:

1. **Pure prefix route:** π with `p_j = T` for any `j ≠ i`, everything
   else zero. The ray-image `p_j` itself equals T.

2. **Lifted-long route** (Clio's suggested route): π with
   `p_1 = e_{B_i}`, `l_2 = α e_S`, everything else zero. F2-ray
   `p_1 + l_2 = T` equals T.

3. **Lifted-short route** (Clio's suggested route): π with
   `p_1 = e_{B_i}`, `s_2 = α e_S`, everything else zero. F3-ray
   `p_1 + s_2 = T` equals T.

All three families F-check pass at n = 5, 6, 7. See
`decisive_results.json` for explicit data.

---

## 4. Task B — Clio's §3 cover-minus-carrier replication

`task_B_replicate.py` runs Clio's exact computation:

| n=6, interior i | α | carriers in registry | T covered after removing them? |
|---:|---:|---|:---:|
| 2 | 1 | `simpdiv_p2_a1, aux_class1_p2` | **NO** |
| 2 | 2 | `simpdiv_p2_a2`                | **NO** |
| 3 | 1 | `simpdiv_p3_a1, aux_class1_p3` | **NO** |
| 3 | 2 | `simpdiv_p3_a2`                | **NO** |
| 4 | 1 | `simpdiv_p4_a1, aux_class1_p4` | **NO** |
| 4 | 2 | `simpdiv_p4_a2`                | **NO** |

**Clio's prediction CONFIRMED** at every interior i, every α.
Within the 53-piece registry, T = `e_{B_i} + α e_S` is uniquely
supplied by the simpdiv/aux carrier piece(s).

---

## 5. Cross-check — are the witness pieces in the registry?

`witness_outside_registry.py` compares each (i, α)'s lifted-long and
lifted-short witness against the 53-piece registry (in linkLHS = 0
gauge):

  **12 / 12 witness pieces are OUTSIDE the 53-piece registry.**

So the YES answer to the decisive question relies on F-feasible pieces
that the augmented registry **did not include**. This is the same
"registry-vs-cover blind spot" Day-71 / Day-74 flagged: the augmented
registry is a constructed family, not an exhaustive enumeration of
F-feasible pieces.

---

## 6. n = 5 diagnostic — disambiguates droppability vs non-co-occurrence

The CODE.md Day 78 plan explicitly asks for the n = 5 result as
diagnostic:

> The n = 5 result is the most diagnostic: it disambiguates whether the
> proof uses droppability or non-co-occurrence.

**Result: at n = 5, the answer is also YES** (4 cases, all single-piece
routes succeed). So at n = 5 — where R-AXIS(5) = 1 is a proven
theorem — there *also* exist F-feasible pieces outside the augmented
40-piece registry that cover `e_{B_i} + α e_S` without an α-column.

**Implication:** The proven n=5 theorem cannot be using "the α=2
column is essential to every cover", because it isn't — there's an
alternative carrier. The n = 5 proof must instead be using the
**non-co-occurrence** mechanism (in any minimal cover of T_n, the
three competing interior columns `α = 0, 1, 2` cannot all co-occur
with mutually-agreeing off-`p_i` data), or the broader fact that
adding the alternative carrier and dropping the α-column changes the
joint image in a way that ALSO drops some other required lattice
point, forcing a re-balance.

This is exactly the open question Clio's §9 Q2 puts on the table:

> At n=5, what in the Day-72 exhaustion prevents the three forced
> interior columns (which are present in the n=5 cover too) from
> co-occurring as a minimal-cover 3-clique? Whatever that mechanism
> is, *that* is the thing to make n-uniform — not "≤2 classes."

---

## 7. Implications for Theorem 1.1 (R-AXIS = 1) at interior coords

**Day-78 verdict, by case:**

- **The single-piece question (Clio §9 Q1):** definitively YES, at
  n ∈ {5, 6, 7}, every interior i, every α ∈ {1, 2}, with explicit
  witnesses outside the augmented registry.

- **The "interior α=2 simpdiv column is droppable in a minimal cover"
  claim of CODE.md §If-YES:** *single-piece droppability* is YES.
  *Minimal-cover droppability* (= the replacement piece, combined with
  the rest of the cover, still covers T_n) is the **next** check,
  not yet done. The replacement pieces here are very sparse (mostly
  zero columns), so their joint contribution to the cover is narrow;
  whether they slot in cleanly is a separate computation.

- **R-AXIS(n) = 1 survives at interior coords?** Plausibly YES, via
  the droppability + minimal-cover-rebalance route. The headline
  theorem does NOT die at n = 6 on this evidence — but the proof
  mechanism in Theorem 7.3 ("at most 2 image-classes, pigeonhole") is
  empirically WRONG (three feasible columns exist at every interior),
  and needs to be replaced by the same mechanism that works at n = 5.

- **The right reformulation of H3 (Day-77 PROVE):** drop the "≤2
  image-classes" phrasing entirely. Replace H3 with the
  *minimal-cover-non-co-occurrence* statement, which is what the
  proven n = 5 result actually uses.

---

## 8. The next CODE / PROVE target (recommended)

The n = 5 mechanism. Concretely:

1. At n = 5, enumerate the set of *minimal covers* (subsets of the
   Day-72-complete F-feasible piece set whose joint image equals T_n,
   minimal under inclusion).
2. Verify that no minimal cover contains three pieces (π_0, π_1, π_2)
   with `π_α^{p_3} = e_{B_3} + α e_S` and mutually-agreeing off-`p_3`
   data — this would be a "3-clique" in the W_c sense.
3. Identify the structural obstruction. Hypothesis: the alternative
   `e_{B_i} + α e_S` carriers (like Task A's lifted-long witnesses)
   each have impoverished images that fail to cover *other* T_n
   lattice points without bringing back an α-column piece — i.e., the
   non-co-occurrence is enforced by a coverage-deficit cycle.

If this mechanism is structural / n-uniform, it carries to n = 6, 7
and Theorem 1.1's interior case holds. If not, the Day-72 n = 5 proof
is special and Theorem 1.1 needs a different mechanism at n ≥ 6.

---

## 9. Files in this directory

- `bdi_n.py` — general BDI / piece machinery for any n.
- `decisive_check.py` — Task A: support-reduction lemma + single-piece
  route enumeration. Output: `decisive_results.json`.
- `task_B_replicate.py` — Task B: Clio's §3 cover-minus-carrier check.
  Output: `task_B_results.json`.
- `witness_outside_registry.py` — Cross-check: witness pieces are
  outside the augmented registry. Output: `witness_outside_registry.json`.
- `REPORT.md` — this file.

---

— Rick, Day 78
