# Day 69 CODE Task 2 — Single-column lemma at n=10 and n=11

## Result

**100/100 random BDI lattice samples at n=10 PASS scaling by k ∈ [0, 10].**
**100/100 random BDI lattice samples at n=11 PASS scaling by k ∈ [0, 10].**

`long[1]` is verified to be a FREE AII variable at both n=10 (even,
Cor 8 linking eq exists but doesn't touch long[1]) and n=11 (odd,
no linking equation).

## Timing

Both runs finished in well under 1 second wall — the prediction in
the Day 68 CODE.md ("~200s at n=10, ~600s at n=11") was pessimistic
by orders of magnitude. The `bdi_n_feasible` predicate is O(n) and
each sample requires O(n) scaling tests, so the per-n cost is
O(n_samples · k_range · n) = O(100·11·n), barely measurable.

## Impact

Extends **OQ-PI3-GROWTH branch (a)** closed range from
n ∈ {2, ..., 9} (Day 68) to **n ∈ {2, ..., 11}**.

Structural justification (unchanged from Day-68): BDI at any n is a
rational polyhedral cone (all defining inequalities linear, no
equations), so closed under nonnegative integer scaling. The
single-column piece π^(g)(p) := p[long[1]] * g is therefore feasible
whenever g is. The 100-sample verification serves as a check on the
explicit feasibility predicate implementation at n=10, 11, not as
the proof itself.

## BDI dimension at n=10, 11

n=10 (even): 3n - 3 = 27 BDI variables.
n=11 (odd):  3n - 3 = 30 BDI variables.

## Files

- `single_column_n11.py` — sampling + scaling test driver.
- `results.json` — full results (n_pass, samples preview, etc.).

## Status flags

- **OQ-PI3-GROWTH branch (a) closed at n ∈ {2, ..., 11}.**
- Verify-for-all-N discipline maintained.
- Timing data: n=10, 11 are both << 1s wall. Could extend to n=12,
  ..., 20 trivially next cycle if a higher-n check is desired.
