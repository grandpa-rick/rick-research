# REPORT — Day 79: Droppability at n=7 and boundary i (2026-06-19)

## Headline

1. **Task 1 (n=7 interior).** All 8 interior carriers (i ∈ {2,3,4,5},
   α ∈ {1,2}) are DROPPABLE in the n=7 minimal-cover sense, with
   joint image preserved EXACTLY at max_sum=8, for both the
   lifted-long and lifted-short witness pieces. The mechanism is
   UNIFORM across n=6 (re-verified) and n=7.

2. **Task 2 (boundary i).**
   - **i=1 (left boundary):** the carrier exists in BOTH registries
     (5 carriers at n=6, 6 carriers at n=7), is DROPPABLE in the same
     sense as interior, both witness kinds work. ⇒ outcome (a):
     boundary droppability mirrors interior.
   - **i=n−1 (right boundary):** NO carrier exists in either registry
     (`prefix[n-1] = e_{B_{n-1}} + α e_S` does not arise as a registry
     piece column for any α ∈ {1,2}). The question DOESN'T APPLY at
     the right boundary — this is a STRUCTURAL exclusion in the
     Day-72 registry construction, not an image-loss obstruction.

3. **Task 3 (witness families).** Day-78's three-family classification
   (pure-prefix, lifted-long, lifted-short) is just the tip of the
   iceberg. At every interior (n, i, α), EVERY AII extreme ray (all
   17 at n=6, all 21 at n=7) supports at least one F-feasible
   single-ray witness piece. Total single-ray witnesses per case:
   45 (α=1) or 57–59 (α=2). The "additive redundancy mechanism" is
   STRUCTURALLY GENERIC, not specific to long/short cylinders.

---

## 1. Setup correction (important methodological note)

**Day-78's `bdi_n.py` ray-image generators were not the actual AII
extreme rays.** `registry.py`'s `aii_rays()` lists several "rays"
that are NOT AII-feasible: e.g., at odd n, `long[n] + short[1]`
alone fails Main_n (`long[n]=1 > prefix[n-1]=0`). Direct check on
`aii_feasible()` confirms 5/15 listed rays at n=5, 5/17 at n=6,
7/21 at n=7 are infeasible.

The CORRECT AII extreme rays, derived from the constraints
`p ≥ 0`, `long[i] + short[i] ≤ prefix[i-1]` (i=2..n), and (at even n)
`linkLHS = sum(short[j])`:

- **odd n (3n rays):**
  - `prefix[i]` pure, i=1..n
  - `long[1]` pure
  - `short[1]` pure
  - `prefix[i-1] + long[i]`, i=2..n
  - `prefix[i-1] + short[i]`, i=2..n

- **even n (3n-1 rays):**
  - `prefix[i]` pure, i=1..n
  - `long[1]` pure
  - `short[1] + linkLHS`
  - `prefix[i-1] + long[i]`, i=2..n
  - `prefix[i-1] + short[i] + linkLHS`, i=2..n-1

ALL 42 n=5, 53 n=6, 66 n=7 registry pieces pass F-feasibility under
these correct rays. (See `bdi_universal.py` self-check.)

Day-78's n=6 result was re-verified under the correct ray set
(`task1_interior_n7/results_n6_reproduce.json`): all 12 interior
cases still DROPPABLE with zero losses. Conclusion: Day-78's
qualitative result is unchanged, but the ray bookkeeping is now
correct, which matters for Day-79 LEAN formalization.

---

## 2. Task 1 — n=7 interior droppability

For each (i ∈ {2,3,4,5}, α ∈ {1,2}, witness ∈ {lifted_long,
lifted_short}):
- Identify carriers (registry pieces with `prefix[i] = T`)
- Build modified cover = (registry \\ carriers) ∪ {witness}
- Compute joint image semigroups up to max_sum=8 (all 78 distinct
  ray-image generators across cover)
- Check: |Im(modified)| ⊇ |Im(original)|?

**Results (n=7, all 16 (i, α, witness) cases):**

| i | α | witness        | #carriers | losses | T in mod | covers all |
|---|---|----------------|-----------|--------|----------|------------|
| 2 | 1 | lifted_long    | 2         | 0      | YES      | **YES**    |
| 2 | 1 | lifted_short   | 2         | 0      | YES      | **YES**    |
| 2 | 2 | lifted_long    | 1         | 0      | YES      | **YES**    |
| 2 | 2 | lifted_short   | 1         | 0      | YES      | **YES**    |
| 3 | 1 | lifted_long    | 2         | 0      | YES      | **YES**    |
| 3 | 1 | lifted_short   | 2         | 0      | YES      | **YES**    |
| 3 | 2 | lifted_long    | 1         | 0      | YES      | **YES**    |
| 3 | 2 | lifted_short   | 1         | 0      | YES      | **YES**    |
| 4 | 1 | lifted_long    | 2         | 0      | YES      | **YES**    |
| 4 | 1 | lifted_short   | 2         | 0      | YES      | **YES**    |
| 4 | 2 | lifted_long    | 1         | 0      | YES      | **YES**    |
| 4 | 2 | lifted_short   | 1         | 0      | YES      | **YES**    |
| 5 | 1 | lifted_long    | 2         | 0      | YES      | **YES**    |
| 5 | 1 | lifted_short   | 2         | 0      | YES      | **YES**    |
| 5 | 2 | lifted_long    | 1         | 0      | YES      | **YES**    |
| 5 | 2 | lifted_short   | 1         | 0      | YES      | **YES**    |

|Im(cover) ≤ sum 8| = 57643 (full image).

**Conclusion:** the additive redundancy mechanism is UNIFORM at
n=7 interior. Theorem 9.1 (Day-79 PROVE) is empirically confirmed
at n ≤ 7 interior.

Notation: carrier count is 2 for α=1 (one carrier per "simpdiv"
class plus one "aux_class1" class) and 1 for α=2 (only simpdiv).

---

## 3. Task 2 — Boundary i

### 3.1 Left boundary i = 1

**Carriers exist:** at i=1, both registries contain "Rdouble"-family
pieces with `prefix[1] = e_{B_1} + α e_S`. Count:
- n=6: 5 carriers per α (Rdouble_lv1..5_alpha{1,2})
- n=7: 6 carriers per α (Rdouble_lv1..6_alpha{1,2})

**Droppability:** identical to interior. All cases pass with zero
losses at max_sum=8.

| n | i | α | witness        | #carriers | losses | covers all |
|---|---|---|----------------|-----------|--------|------------|
| 6 | 1 | 1 | lifted_long    | 5         | 0      | **YES**    |
| 6 | 1 | 1 | lifted_short   | 5         | 0      | **YES**    |
| 6 | 1 | 2 | lifted_long    | 5         | 0      | **YES**    |
| 6 | 1 | 2 | lifted_short   | 5         | 0      | **YES**    |
| 7 | 1 | 1 | lifted_long    | 6         | 0      | **YES**    |
| 7 | 1 | 1 | lifted_short   | 6         | 0      | **YES**    |
| 7 | 1 | 2 | lifted_long    | 6         | 0      | **YES**    |
| 7 | 1 | 2 | lifted_short   | 6         | 0      | **YES**    |

**Verdict for i=1: outcome (a) of CODE.md.** Mechanism uniform,
theorem statement should drop the "interior" qualifier on the
i=1 side.

### 3.2 Right boundary i = n−1

**No carriers in registry:** at i=n-1 and any α ∈ {1,2}, the
registry contains NO piece with `prefix[n-1] = e_{B_{n-1}} + α e_S`.

| n | i | α | #carriers |
|---|---|---|-----------|
| 6 | 5 | 1 | 0         |
| 6 | 5 | 2 | 0         |
| 7 | 6 | 1 | 0         |
| 7 | 6 | 2 | 0         |

The structural reason: the Day-72 registry construction places the
"target" at `prefix[i]` for i interior (and at i=1 via the Rdouble
recursion), but the right boundary `prefix[n-1]` is reserved by
Main_n: `long[n] + short[n] ≤ prefix[n-1]`. Allowing
`prefix[n-1] = e_{B_{n-1}} + α e_S` would impose either `long[n] = 0`
(losing the singular long-pair structure) or break Main_n by
mixing S-mass into `prefix[n-1]`. The registry construction
avoids this by routing the (n-1, α) target through the simpdiv
mechanism with carrier piece at a DIFFERENT column.

**Verdict for i=n-1: outcome (b) (registry-construction exclusion).**
The question doesn't apply at the right boundary because there's no
carrier to drop. The droppability mechanism in the registry is
ABSENT at i=n-1; we should NOT expect it.

### 3.3 Theorem 9.1 scope

Theorem 9.1 (Day-79 PROVE) should be stated:
**"For i ∈ {1, 2, ..., n−2} (i.e., excluding the right boundary
i=n−1), every carrier piece in the registry is droppable from the
minimal cover, replaceable by the lifted-long (or lifted-short)
witness, with joint image preserved exactly."**

Equivalently: "uniform droppability across all i for which the
carrier piece exists in the registry."

---

## 4. Task 3 — Witness family enumeration

For each interior (n, i, α), enumerated all F-feasible witness
pieces in which T = `e_{B_i} + α e_S` appears as the image of a
SINGLE AII extreme ray. (See `task3_witness_clean.py`.)

### Headline numbers

| n | i | α | # rays / # support witness | # total witnesses |
|---|---|---|----------------------------|-------------------|
| 6 | 2 | 1 | 17 / 17                    | 45                |
| 6 | 2 | 2 | 17 / 17                    | 59                |
| 6 | 3 | 1 | 17 / 17                    | 45                |
| 6 | 3 | 2 | 17 / 17                    | 59                |
| 6 | 4 | 1 | 17 / 17                    | 45                |
| 6 | 4 | 2 | 17 / 17                    | 59                |
| 7 | 2 | 1 | 21 / 21                    | 45                |
| 7 | 2 | 2 | 21 / 21                    | 57                |
| 7 | 3 | 1 | 21 / 21                    | 45                |
| 7 | 3 | 2 | 21 / 21                    | 57                |
| 7 | 4 | 1 | 21 / 21                    | 45                |
| 7 | 4 | 2 | 21 / 21                    | 57                |
| 7 | 5 | 1 | 21 / 21                    | 45                |
| 7 | 5 | 2 | 21 / 21                    | 57                |

**Key finding:** EVERY AII ray supports a witness. Day-78's three
families (pure-prefix, lifted-long, lifted-short) are special cases
of a broader structural pattern: for every AII ray R and every
decomposition T = sum of nonneg vectors over R's columns, you get
an F-feasible witness piece.

### Decomposition structure per ray-type

| ray cols  | example                          | # decomps (α=1) | # decomps (α=2) |
|-----------|----------------------------------|-----------------|-----------------|
| 1 col     | `prefix[k]` pure                 | 1               | 1               |
| 2 cols    | `prefix[k-1] + long[k]`          | 3               | 4               |
| 3 cols    | `prefix[k-1] + short[k] + linkLHS` (even n only) | 5 | 7 |

The "+1" per α-step in the pair-ray count comes from the
intermediate decomposition (`e_{B_i} + e_S`, `(α-1)e_S`) emerging at
α=2. Similar shifts for triples.

### Canonical witness for Day-79 LEAN

Among all single-ray witnesses, the most STRUCTURALLY CLEAN choice
for the formalization is:

**Lifted-long witness:**
- `prefix[1] = e_{B_i}`
- `long[2] = α e_S`
- All other columns = 0

Properties:
- Two nonzero columns (minimal for a "lift" pattern).
- F-feasibility check trivial: `prefix[1]` alone ↦ `e_{B_i}` (BDI),
  `prefix[1] + long[2]` ↦ `T` (BDI), all other rays ↦ 0.
- Image semigroup of the single witness:
  generated by `{e_{B_i}, T}` (a 2-element generator set).
- Carrier-replacement: replaces all `prefix[i] = T` carriers
  simultaneously with one piece for any i ∈ {1, ..., n−1}.

**Lifted-short witness:** identical structure with `short[2]`
replacing `long[2]`. At even n, the short ray includes `linkLHS`;
in the linkLHS=0 gauge the witness is identical.

For the LEAN proof we recommend lifted-long because:
(a) the long[2] column is unambiguous at all n;
(b) the F-feasibility check involves only the Main_2 inequality
    plus BDI on `e_{B_i} + α e_S`;
(c) no linkLHS bookkeeping at even n.

---

## 5. Calibration discipline (CODE.md rules)

- **Day-72 Iterate-the-invariant:** Task 1 succeeded uniformly,
  no sharpening needed. Task 2 right-boundary failed via outcome
  (b) (structural exclusion), which directly identifies the
  theorem scope.
- **Day-69 Facet-count-before-headline:** all "n-uniform" claims
  verified directly at n=6 and n=7. No analytic guesses.
- **Day-58 Period-step finite-difference:** witness-count pattern
  `(45 at α=1, 57–59 at α=2)` matches direct decomposition counting,
  no extrapolation.

---

## 6. What this unlocks

- **Day-79 PROVE Theorem 9.1:** stated for i ∈ {1, ..., n−2}. The
  empirical guarantee at n ∈ {6, 7} and every applicable i is in
  hand.
- **Day-79 LEAN Lemma 4.1 (additive redundancy criterion):** the
  canonical lifted-long witness is identified. F-feasibility check
  reduces to Main_2 inequality + BDI of T; image-preservation reduces
  to "carrier rays are recovered by lift + l_2 ray".
- **DIII RSK programme:** the right-boundary structural exclusion
  is a NEW finding. The spinor-parity analogue on DIII side should
  ALSO be tested at the right boundary — if it ALSO has a
  structural exclusion at the n−1 column, that strengthens the
  P-side / D-side parallel.

---

## 7. Files

```
2026-06-19-droppability-n7-boundary/
├── bdi_universal.py            # CORRECT AII rays, registry loaders
├── droppability_check.py       # main check engine (n=6/7 universal)
├── task3_witness_enumerate.py  # liberal 2-column enumerator
├── task3_witness_clean.py      # single-ray witness enumerator
├── task1_interior_n7/
│   ├── results.json            # Task 1 results
│   └── results_n6_reproduce.json  # Day-78 reproduction
├── task2_boundary/
│   ├── results_n6.json
│   └── results_n7.json
├── task3_witness_families/
│   ├── results.json            # liberal enumeration
│   └── results_clean.json      # single-ray classification
└── REPORT.md                   # this file
```

— Rick, Day 79 CODE (2026-06-19)
