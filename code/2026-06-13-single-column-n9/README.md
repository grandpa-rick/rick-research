# Day 68 CODE Task 2 — Single-column lemma at n=9

## Result

**100/100 random BDI lattice samples at n=9 pass scaling by k ∈ [0, 10].**

`long[1]` is verified to be a FREE AII variable at n=9 (no Main_i,
no linking eq — n is odd so no Cor-8 link).

## Impact

Extends **OQ-PI3-GROWTH branch (a)** closed range from
n ∈ {2, ..., 8} (Day-67) to **n ∈ {2, ..., 9}**.

Structural justification: BDI at any n is a rational polyhedral cone
(all defining inequalities linear, no equations), so closed under
nonnegative integer scaling. The single-column piece π^(g)(p) :=
p[long[1]] * g is therefore feasible whenever g is. The 100-sample
verification serves as a check on the explicit feasibility predicate
implementation at n=9, not as the proof itself.

## Files

- `single_column_n9.py` — sampling + scaling test driver.
- `results.json` — full results (n_pass, samples preview, etc.).

## BDI at n=9

24 variables: M_2..M_8, B_1..B_8, T_1..T_8, S (= 3·9 − 3 = 24, matches).
