# Day 73 CODE Task A — Class 3 + Class 4 aux at n = 5

## Headline

**Lemma 4.3 VERIFIED at n=5.**  All combined Class-1 / 2 / 3 / 4
auxiliaries added to the AXIS+base registry produce **0 new
3-cliques on non-AXIS walls**.

### Class-3 result (surprise)

The Day-72 PROVE §4.3 estimated **~9 misaligned `(M_j, B_i)` pairs**
to verify at n=5.  Of these:

| pair        | BDI gap point e_{M_j} + e_{B_i} | aux needed? |
|-------------|---------------------------------|-------------|
| (M_2, B_2)  | INFEASIBLE (M_2=1 > P_1=0)      | vacuous     |
| (M_2, B_3)  | INFEASIBLE                       | vacuous     |
| (M_2, B_4)  | INFEASIBLE                       | vacuous     |
| (M_3, B_1)  | feasible                         | **YES**     |
| (M_3, B_3)  | INFEASIBLE                       | vacuous     |
| (M_3, B_4)  | INFEASIBLE                       | vacuous     |
| (M_4, B_1)  | feasible                         | **YES**     |
| (M_4, B_2)  | feasible                         | **YES**     |
| (M_4, B_4)  | INFEASIBLE                       | vacuous     |

**Structural rule.** `e_{M_j} + e_{B_i}` is BDI-feasible iff
`i <= j - 1`.  In words: the activator `B_i` must be at or below
`M_j`'s "left support" `P_{j-1}`.  The other 6 misaligned pairs
correspond to BDI lattice points that don't exist at all — no
piece needs to cover them.

**Net result.**  Only **3 genuine Class-3 cases**, not ~15.

### Class-4 result

Both `(B_2, T_2)` and `(B_3, T_3)` auxiliaries:
- BDI-feasible on every AII ray;
- hit the target gap point EXACTLY (no extra content);
- have unique 2-column signatures `(p_{i-1}, l_i)`.

### Signature uniqueness

All 5 aux (3 Class-3 + 2 Class-4) have distinct
"differs-from-base" column sets.  By Lemma 4.2 (PROVE §4),
this implies no auxiliary contributes a 3-clique on a wall.

### Cross-check

Built combined registry (47 augmented + 3 Class-3 + 2 Class-4 = 52
pieces).  Enumerated all 3-cliques (482 total).  Every 3-clique
lies on an AXIS wall (`p_1, p_2, p_3, p_5, l_1, l_2, l_3, l_4` —
the 8 AXIS vars at n=5).  Lemma 4.3 verified.

## Files

- `enumerate.py` — full pipeline.  Includes:
  - BDI-feasibility pre-check for each `(j, i)` pair.
  - Construction of misaligned engines via `l_{i+1}` column rewires.
  - Class-4 construction via `(p_{i-1}, l_i)` column zero-out.
  - Signature uniqueness check.
  - 3-clique enumeration on combined registry.
- `results.json` — full output table.

## Updates to PROVE §4.3

The **"~15 cases each"** estimate in Day-72 PROVE §4.3 was a
combinatorial over-count.  The actual count of genuine misaligned
`(M_j, B_i)` pairs at n=5 is **3**.  (Generally at level n it is
`binom(n-2, 2)` — pairs with i < j-1 and j in 2..n-1, plus the
edge cases.)

The structural reason — BDI feasibility of `e_{M_j} + e_{B_i}`
requires `i ≤ j-1` — should be added as a lemma in the PROVE
§4.3 cover-restricted argument, and the per-case enumeration
shrinks accordingly.

## Reproducing

```bash
python3 enumerate.py
```
