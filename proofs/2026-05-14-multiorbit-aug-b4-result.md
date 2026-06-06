# B_4 multi-orbit verification result (2026-05-15)

Companion to `2026-05-14-multiorbit-aug-b3-result.md`. Tests the three-strand
braid hypothesis for the structural decomposition of `e_4^{k(4)} = e_4^2` on
slice `S_4 = {pi : eps_4(pi) >= 2}` of `Kp(infty)` for type B_4.

## Scope of compute
- Crystal axioms tested on all partitions with `max_total <= 3` (969 partitions).
- On-slice / off-slice commutativity tested on all partitions with `max_total <= 5`.
- Multi-orbit catalog enumerated on all partitions with `max_total <= 5`.
- All tests completed in well under 10s on the container.

## Results

### Crystal axiom check: PASS
At `max_total = 3`, all 969 Kostant partitions of B_4 satisfy
- `e_i f_i = id` for all i in {1, 2, 3, 4}: 969/969 each.
- `f_i e_i = id on slice` ({eps_i >= 1}): 538/538 for i=1,2,3 and 626/626 for i=4.
- `e_i pi = None iff eps_i(pi) = 0`: 0 failures.

### On-slice `[e_i^{k(i)}, B_i] = 0` at B_4 (max_total = 5)
| i | k(i) | on-slice partitions | falsifiers |
|---|------|---------------------|------------|
| 1 | 1    | 13272               | **0**      |
| 2 | 1    | 13272               | **0**      |
| 3 | 1    | 13272               | **0**      |
| 4 | 2    | 10447               | **0**      |

### Off-slice obstruction at B_4 (max_total = 5)
At `eps_i = k(i) - 1`, predicted `[e_i^k, B_i] pi = e_i^{k-1} pi`.
| i | k | target_eps | tested | matches | mismatches |
|---|---|------------|--------|---------|------------|
| 1 | 1 | 0          | 7077   | 7077    | **0**      |
| 2 | 1 | 0          | 7077   | 7077    | **0**      |
| 3 | 1 | 0          | 7077   | 7077    | **0**      |
| 4 | 2 | 0          | 5371   | 5371    | **0**      |
| 4 | 2 | 1          | 4531   | 4531    | **0**      |

### Catalog size at alpha_4 (short simple)
Stable across max_total in {3, 4, 5}: **28 distinct net moves** (predicted 28).

### Three-strand braid split: CONFIRMED
| Class                  | Observed | Predicted |
|------------------------|----------|-----------|
| intra-chain            | **9**    | 9         |
| cross-chain            | **12**   | 12        |
| singleton-involving    | **7**    | 7         |
| **Total**              | **28**   | 28        |

All 28 predicted (chain, primitive) pair signatures match exactly the 28
empirically observed root-multiplicity deltas. No unmatched observations,
no missing predictions.

Concrete examples:
- intra-A T-B (one `T->M` plus one `M->B` on chain A): delta `[-(e_1+e_4), +(e_1-e_4)]`, 1341 cases on-slice.
- cross-BC TM+TM: delta `[+e_2, -(e_2+e_4), +e_3, -(e_3+e_4)]`, 67 cases.
- singleton self-pair: delta `[-2*e_4]`, 421 cases.

## VERDICT
Three-strand braid hypothesis **CONFIRMED at B_4**. The B_3 structure (15 moves =
5 primitives squared via stars-and-bars) extends type-uniformly to B_4 (28 = C(8,2)
from 7 primitives), with the predicted (intra, cross, singleton) split (9, 12, 7).

This is consistent with the conjecture that at B_n short simple, the n(2n-1)
net moves of e_n^{k(n)} decompose into:
- (n-1) intra-chain blocks of 3 moves each = 3(n-1),
- C(n-1, 2) cross-chain blocks of 4 moves each = 2(n-1)(n-2),
- (2(n-1) + 1) singleton-involving moves (1 self-pair + 2(n-1) singleton-chain pairs).

At n=4: 3*3 + 2*3*2 + 7 = 9 + 12 + 7 = 28 ✓.

## Files
- `/home/agent/projects/proofs/remark47/coideal_check/b_i_b4.py` — B_4 commutativity test (axioms + on-slice + off-slice).
- `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/verify_catalog_b4.py` — 28 net moves enumeration.
- `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/characterize_moves_b4.py` — three-class characterization with explicit predicted deltas.
