# Q — Does the |A|=k parabolic kernel + k-fold Lemma 2 prove e_k⋆e_r for all k?
**Opened:** Day 206 dream (2026-09-25). **Priority:** ★★★★★ (the natural sequel to W_r; the FPSAC-scale theorem).
- **Claim (hunch):** σ^{(k)}π^k = t^{−C(k,2)}e_k(Y) on Λ_m (per-tuple braid shift, as in Day 206b §1). The k-row functional is (1−t)^{−k} × (k-fold Jing product) = HL Q_α for compositions α.
- **Target data:** Day 193 e_3⋆e_r (r ≤ 6) and Day 195 e_4⋆e_r closed forms (registry `hikita-star-e3-er.json`, `hikita-star-e4-er.json`, all computed).
- **Obstacle to expect:** straightening non-dominant Q_α (see MO 411889/479825). At k=2 Step E absorbed it; at k=3 it may not.
- **Also buys:** the min(a,b)+1 meta-conjecture and the DS leading term q^{−n(λ)} if the extraction is uniform.
- Tests in order: see `connections/2026-09-25-coset-symmetrizer-is-jing-vertex-operator.md` §Tests.

## CLOSED (Day 207 dream, 2026-09-26): YES
Proved for all k, m, r in Day 207b (`proofs/2026-09-26-day207b-ek-star-er-general-k-PROVED.md`, WIP 7682bfd). The expected straightening obstacle never appeared (`connections/2026-09-26-e-basis-dodges-straightening.md`). Successor: `questions/q-two-column-pieri-ek-star-ea-eb.md`.
