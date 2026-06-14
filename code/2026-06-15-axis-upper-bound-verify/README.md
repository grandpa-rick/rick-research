# Day 70 PROVE verification — Lemma D upper bound reduction

Sanity checks for the Day-70 writeup `proofs/2026-06-15-axis-uniform3-upper-bound.md`.

## Scripts

- `ray_check.py` — Verifies Theorem 4.2 (Feasibility Ray-Characterisation)
  against the n=5 27-piece registry. Compares direct feasibility (apply
  pi to each AII lattice point) with ray feasibility (check F1-F4 column
  conditions). PASS: 27/27 agreement.

- `dpi_check.py` — Verifies Conjecture D-pi at n=5: interior prefix
  p_i (i ∈ {2, 3}) is RIGID across all 27 feasible registry pieces.
  Also checks p_{n-1} = p_4 RIGID (Lemma 6.4). PASS.

## Running

```
python3 ray_check.py
python3 dpi_check.py
```

Both depend on `code/2026-06-13-n5-axis-count/` for the piece registry.
