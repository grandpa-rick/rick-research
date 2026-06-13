# Day 69 PROVE verification scripts — # AXIS uniform lower bound

Supports `proofs/2026-06-14-axis-uniform3-proof.md`.

## Scripts

- **verify_n3.py** — Re-runs the actual MIN_COVER_26 n=3 R-double pieces
  (`R_double_m2345`, `P5d_Rdouble_plus_m2`, `P7_Rdouble_m2_dbl_S`)
  against the full Day-58 AII enumeration (Cor 6 + Main + Singleton).
  Verifies: (i) all 3 pieces BDI-feasible at sum ≤ 4; (ii) pairwise
  matrix differences supported ONLY on the (S, m_2) = (S, prefix[1])
  entry. Confirms the column-shape claim of Lemma A at n=3.

- **verify_uniform.py** — Naive uniform recipe (no p_n routing).
  Demonstrates the recipe FAILS at n=3 if we ignore the Singleton
  constraint and naively apply the abstract long+short ≤ prefix
  framework. Documents *why* the n=3 case needs the Singleton.

- **verify_v2.py** — Corrected uniform recipe V2 (p_n routed to
  (B_2, T_2) balanced). Verifies BDI-feasibility at n ∈ {3, 4, 5, 6, 7}
  for α ∈ {0, 1, 2}, and SHARP infeasibility at α = 3 — the
  rep-theoretic cap.

## How the scripts support the proof

- Lemma A: recipe V2 (verify_v2.py) for n ≥ 4; for n = 3 the
  Singleton-aware verification is in verify_n3.py against MIN_COVER_26.
- Lemma B: not separately verified — the construction is so direct
  (add k p_n to balanced (B_{n-1}, T_{n-1})) that the proof in §3.2
  of the writeup is self-contained.
- Lemma C: same as Lemma B — construction direct, proof in §3.3.

## Note on Lemma D

Not verified here. The empirical upper bound # AXIS ≤ 3 at n ∈ {3, 4, 5}
is in `code/2026-06-13-axis-n3-verify/` and `code/2026-06-13-n5-axis-count/`.
