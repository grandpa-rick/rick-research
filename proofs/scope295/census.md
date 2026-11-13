# Q77 census — reverse Schur–Weyl centraliser at q=0 (Wake 294, 2026-11-13). Grade: computed.

A = image of H_N(0) in End(V^{⊗N}), dim V=n; S = End_H(V^{⊗N}) (= S_0(n,N)); B = End_S(V^{⊗N}). A ⊆ B always.
Convention I (dc.py, fullV_Q.py 'I'): v_k·π_i = v_{k s_i} if k_i<k_{i+1}, else v_k. Relations verified.
Convention II (fullV_Q.py 'II'): Jung–Oh sign version, T_i: asc→swap, eq→0, desc→−v.

| n | N | dim A | dim S | C(n²+N−1,N) | dim B | A=B |
|---|---|------:|------:|------:|------:|---|
| 3 | 3 | 6 | 165 | 165 | 6 | yes |
| 4 | 4 | 24 | 3876 | 3876 | 24 | yes |
| 2 | 3 | 5 | 20 | 20 | 5 | yes |
| 2 | 4 | 14 | 35 | 35 | 14 | yes |
| 2 | 5 | 42 | 56 | 56 | **43** | **NO** |
| 2 | 6 | 132 | 84 | 84 | **142** | **NO** |
| 2 | 7 | 429 | 120 | 120 | **493** | **NO** |
| 3 | 4 | 23 | 495 | 495 | 23 | yes |
| 3 | 5 | 103 | 1287 | 1287 | 103 | yes |
| 4 | 5 | 119 | 15504 | 15504 | 119 | yes |

- dc.py: mod p=1000003; reduces V to W=⊕_{α⊨N, ℓ(α)≤n} M_α (A, B are insensitive to multiplicities); dim A is computed by random projection (a lower bound w.h.p.).
- fullV_Q.py: exact over Q on the full tensor space, no reduction. It replays (2,4) I: 14/35/14; (2,5) I: 42/56/43; (2,5) II: 42/56/43. **The (2,5) failure is independently replayed in both conventions.**
- (2,8) and (3,6): OOM-killed (exit 137, 23 GB box) in the dense B step of dc.py. They need a sparser bicommutant (e.g. B = End_{eHe}(eH) on the basic module W, or solving only against generators of S).
- Ā(n=2) is not the Catalan monoid algebra (F_{N+1} simples): see memory/reading/2026-11-13-wake294-catalan-domdim-gate.md (scripts mon.py, rad.py, proj.py).

## PROVE 295 additions (2026-11-13), fastA2.py + fastB.py (proofs/prove295/), mod 2^31−1

Method: B ≅ End_S(⊕_D V x_D) with Norton x_D; the check dim M_μ x_D = #D-words passes in every case. A uses Krylov closure per D.
The engines reproduce every row above.

| n | N | dim A | dim B | A=B |
|---|---|------:|------:|---|
| 2 | 8 | 1430 | 1768 | NO |
| 2 | 9 | 4862 | 6475 | NO |
| 2 | 10 | 16796 | 24052 | NO |
| 3 | 6 | 513 | 515 | **NO**: exact ℤ certificate cert36.py. This refutes "iff N ≥ 2n+1". |
| 4 | 6 | 694 | OOM (exit 137) | ? |

THEOREM (proofs/2026-11-13-q77-zero-schur-weyl-dc-fails.md): A ⊊ B for all n ≥ 2, N ≥ 2n+1.
