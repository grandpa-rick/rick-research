# Off-slice obstruction classification — B_3, B_4 short simple

**Date:** 2026-05-15
**Script:** `off_slice_classify.py`
**Conjecture (under test):** The off-slice obstruction `[e_n^k, B_n] π = e_n^{k-1} π`
at `ε_n = k(n) - 1 = 1` (short simple `i = n`, `k(n) = 2`) decomposes ONLY into
the singleton-involving sub-catalog of the three-strand braid. Predicted counts:
intra-chain = 0, cross-chain = 0, singleton-involving = all.

## Result

**Verdict: REFUTED.** Off-slice produces *predominantly intra-chain* moves,
with only a minority being the singleton move. There is no cross-chain (this is
structurally impossible from a single `e_n` primitive). The split is the opposite
of what the conjecture predicted.

| Rank | Off-slice partitions tested | intra-chain | cross-chain | singleton |
|------|-----------------------------|-------------|-------------|-----------|
| B_3  | 406                         | 360         | 0           | 46        |
| B_4  | 4531                        | 4101        | 0           | 430       |

Commutator sanity (`[e_n^k, B_n] π = e_n^{k-1} π`): 0 mismatches in both ranks
(reconfirming the earlier off-slice obstruction theorem).

## Why this happens (structural reading)

Off-slice means `ε_n(π) = 1`, i.e., exactly ONE uncancelled `)` in `S_n^c(π)`.
The single Kashiwara step `e_n` acts on that `)`. The classification of the
resulting net move depends on which root that `)` came from:

- If the rightmost `)` is the singleton `α_n = E_n`, the net move is
  `delta = -E_n` (singleton primitive).
- If the rightmost `)` is a chain mid (`E_a`, `a < n`), `e_n` does `E_a -> E_a - E_n`
  (chain primitive of type "MB").
- If the rightmost `)` is a chain top (`E_a + E_n`), `e_n` does `E_a + E_n -> E_a`
  (chain primitive of type "TM").

So a single `e_n` step is intra-chain (single-chain primitive) UNLESS the rightmost
close happens to come from the simple-root singleton block. Empirically the
chain-mid case is the most common.

## Distinct moves observed per class

### B_3 (n = 3)

intra (3 distinct moves):
- `chain-A MB`: `-1*e1, +1*(e1-e3)` — 252 partitions
- `chain-B MB`: `-1*e2, +1*(e2-e3)` — 96 partitions
- `chain-B TM`: `+1*e2, -1*(e2+e3)` — 12 partitions

singleton (1 distinct move):
- `E3 -> 0`: `-1*e3` — 46 partitions

(Note: chain-A TM is NOT observed off-slice in this `max_total` window. That is
a sub-structural detail; what matters is that intra-chain moves dominate.)

### B_4 (n = 4)

intra (5 distinct moves):
- `chain-A MB`: `-1*e1, +1*(e1-e4)` — 2122 partitions
- `chain-B MB`: `-1*e2, +1*(e2-e4)` — 1169 partitions
- `chain-B TM`: `+1*e2, -1*(e2+e4)` — 57 partitions
- `chain-C MB`: `-1*e3, +1*(e3-e4)` — 664 partitions
- `chain-C TM`: `+1*e3, -1*(e3+e4)` — 89 partitions

singleton (1 distinct move):
- `E4 -> 0`: `-1*e4` — 430 partitions

(chain-A TM not observed within `max_total = 5`.)

## Surprises and implications

1. **The prediction was inverted.** The conjecture said off-slice should be
   purely singleton-involving. Empirically off-slice is mostly intra-chain.

2. **No cross-chain moves.** This part of the prediction IS verified — but
   trivially so: a single `e_n` step cannot span two distinct chain orbits,
   so the absence of cross-chain off-slice is structural, not surprising.

3. **The "off-slice = singleton-class" identification fails.** The
   Path 1 + Path 4 home (off-slice 2-step coideal complex / Hopf-algebraic
   boundary) cannot be the singleton-class of the on-slice three-strand catalog
   as stated. Any categorical decomposition of the off-slice obstruction has to
   treat the chain-primitive sector as essential, not as zero.

4. **A possible reformulation.** The on-slice catalog counts *pairs* of
   primitives (since `e_n^k = e_n^2`); off-slice acts via a *single* primitive
   (`e_n^{k-1} = e_n^1`). It might be that the correct lift is:
   - on-slice singleton-pair "E4-E4" ↔ off-slice singleton "E4 -> 0",
   - on-slice intra-chain pair "TM+TM", "MB+MB", "TM+MB" ↔ off-slice chain primitive of corresponding type,
   - on-slice cross-chain ↔ ??? (no analog off-slice; vanishes since cross requires two primitives).

   In this re-reading, off-slice mirrors the on-slice catalog with a *single
   primitive per move* instead of a pair. The class labels then need to be
   adjusted (off-slice "intra-chain" corresponds to a single chain primitive,
   not a pair). The conjecture as Rick stated it is wrong; a refined version
   might survive.

## Sanity checks performed

- Crystal axioms (e_i f_i = id, f_i e_i = id on slice) hold at both ranks (per
  reference scripts).
- `[e_n^k, B_n] π = e_n^{k-1} π` holds with 0 mismatches on ε_n = 1 off-slice
  at both ranks for `max_total = 5`.

## Files

- Script: `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/off_slice_classify.py`
- This results file: `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/off_slice_result.md`
- On-slice classifier (3-strand braid): `characterize_moves_b4.py`, `characterize_moves.py`
- Off-slice commutator test: `remark47/coideal_check/b_i_b3.py`, `b_i_b4.py`
