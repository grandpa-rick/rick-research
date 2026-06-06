# B_5 multi-orbit verification result (2026-05-17)

Companion to `2026-05-14-multiorbit-aug-b3-result.md` and
`2026-05-14-multiorbit-aug-b4-result.md`. Tests the three-strand braid
hypothesis for the structural decomposition of `e_5^{k(5)} = e_5^2` on
the slice `S_5 = {pi : eps_5(pi) >= 2}` of `Kp(infty)` for type B_5.

## Arithmetic of the type-uniform formula at n = 5

`3(n-1) + 2(n-1)(n-2) + (2n-1) = n(2n-1)`.

At `n = 5`:
- intra: `3 * 4 = 12`
- cross: `2 * 4 * 3 = 24`
- singleton: `2 * 5 - 1 = 9`
- total: `12 + 24 + 9 = 45 = 5 * 9 = n(2n-1)`. Arithmetic checks.

## Scope of compute

- Catalog enumerated on all Kostant partitions of B_5 with `max_total in {3, 4, 5}`.
- Number of partitions at `max_total = 5`: 142,506. On-slice count: 66,404.
- Total wall time: ~4 s (catalog) + ~2 s (characterization) on the container.

## Catalog size at alpha_5 (short simple)

Stable across max_total in {3, 4, 5}: **45 distinct net moves** (predicted 45).

| max_total | on-slice partitions | distinct net moves |
|-----------|---------------------|--------------------|
| 3         | 1,142               | 45                 |
| 4         | 9,827               | 45                 |
| 5         | 66,404              | 45                 |

## Three-strand braid split: CONFIRMED

| Class                  | Observed | Predicted |
|------------------------|----------|-----------|
| intra-chain            | **12**   | 12        |
| cross-chain            | **24**   | 24        |
| singleton-involving    | **9**    | 9         |
| **Total**              | **45**   | 45        |

All 45 predicted (chain, primitive) pair signatures match exactly the 45
empirically observed root-multiplicity deltas. No unmatched observations,
no missing predictions.

The four length-3 alpha_5-chains used:
- Chain A: bot=e_1-e_5, mid=e_1, top=e_1+e_5
- Chain B: bot=e_2-e_5, mid=e_2, top=e_2+e_5
- Chain C: bot=e_3-e_5, mid=e_3, top=e_3+e_5
- Chain D: bot=e_4-e_5, mid=e_4, top=e_4+e_5

plus the alpha_5 singleton e_5.

Concrete examples observed:
- intra-D T-B (one `T->M` plus one `M->B` on chain D): delta
  `[-(e_4+e_5), +(e_4-e_5)]`, 7170 cases on-slice (max_total=5).
- cross-AB TM+MB: delta `[+e_1, -(e_1+e_5), -e_2, +(e_2-e_5)]`, 1644 cases.
- singleton self-pair: delta `[-2 e_5]`, 1504 cases.
- singleton + D_TM: delta `[+e_4, -(e_4+e_5), -e_5]`, 1699 cases.

## Anomalies / surprises

None. The catalog matches the prediction exactly with no unmatched
observations and no missing predictions. The catalog was already saturated
at `max_total = 3` (1,142 on-slice partitions sufficed to realize all 45
moves), which is consistent with the asymptotic plateau seen at B_3 and B_4.

## VERDICT

Three-strand braid hypothesis **CONFIRMED at B_5**.

Combined with the B_2 (6 = 3 + 0 + 3, degenerate), B_3 (15 = 6 + 4 + 5),
and B_4 (28 = 9 + 12 + 7) verifications, this is the fourth rank-confirmation
in the B_n family and the third in the non-degenerate regime (n >= 3 where
all three classes are nonempty and the cross-chain class scales as
2(n-1)(n-2)).

## Files

- `/home/agent/projects/proofs/remark47/coideal_check/b_i_b5.py` -
  B_5 crystal / bracketing module (ported from `b_i_b4.py`).
- `/home/agent/projects/proofs/2026-05-17-multiorbit-aug-b5/verify_catalog_b5.py` -
  45 net moves enumeration.
- `/home/agent/projects/proofs/2026-05-17-multiorbit-aug-b5/characterize_moves_b5.py` -
  three-class characterization with explicit predicted deltas.
- `/home/agent/projects/proofs/2026-05-17-multiorbit-aug-b5/run-log.txt` -
  raw stdout from both scripts.
