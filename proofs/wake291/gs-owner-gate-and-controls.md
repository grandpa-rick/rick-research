# G_s owner gate + negative controls + blind tests (Wake 291 sub-task, 2026-11-12)

Convention follows `hjv-scoping.md` / `cap_rank.py`. s is a binary string of length L, d = L+1, and bit 1 marks a descent (a cut). So alternating `0101…` has composition (2^k) for L = 2k−1 and (2^k,1) for L = 2k. All results below are graded **computed** at most.
Scripts and outputs are in `wake291/gs/`.

## 0. Engine
- `gs/fastcap.py` is a DP-over-shuffles engine for c^s_{u,v} = [F_s]F_uF_v. Ranks are taken mod two primes (2^31−1 and 10^9+7) and the max is used. This is a lower bound on the Q-rank and is exact generically.
- Replay (`check_fast.py`): DP versus the brute-force `cap_rank.coeff` on all s with L ≤ 6 and all u, v ⊑ s gives **6042 entries, 0 mismatches**. Alternating ranks for L ≤ 11 reproduce `out_alt_ranks.txt` exactly.

## 1. Owner gate: NOT FOUND (no prior work on G_s or on its Sym shadow)
sources.json (781 entries) has no hit on Gorenstein, inverse system, apolar, or annihilator combined with QSym/NSym/ribbon. The only hits are off-target: 2508.07166 and 2609.03195, both "Gorenstein" in other senses.

Searches run:
- arXiv abstract search (all words): "quasisymmetric Gorenstein" returned 0 hits. "quasisymmetric "inverse system"", "noncommutative symmetric Gorenstein", "Schur polynomial apolar", "Schur "dual generator"", "ribbon Gorenstein" and "quasisymmetric Lefschetz" returned 0 relevant hits. "toric Richardson" returned 24 hits, scanned.
- Semantic Scholar: mostly rate-limited. The query that ran ("annihilator ribbon Schur function") returned only ribbon-equality papers.
- WebSearch: 9 queries covering the Macaulay/apolar/Lefschetz plus Schur/symmetric angle, the Hall-pairing/skewing Gorenstein angle, and the PD-defect/cap-product toric angle.

Papers opened first-hand:
- **Bergeron–Gagnon–Spink–Tewari, 2604.24903, "The Quasisymmetric Grassmannian"** (PDF in `wake291/gate/`). This is the closest geometry. Verbatim (§1.2): "While QGr(r,n) does not enjoy Poincaré duality, we find a Kronecker dual of this basis under the natural pairing H^k ⊗ H_k → Z". They state the PD failure and nothing more: no cap with a fundamental class and no Gorenstein quotient. Not an owner, but it **should be cited**. It is not in sources.json.
- **Boij–Migliore–Miró-Roig–Nagel, 2009.13002** (PDF in `gate/`). Verbatim: "we show that the complete symmetric polynomials are dual generators of compressed artinian Gorenstein algebras satisfying the Strong Lefschetz Property. This is the first example of an explicit dual form with these properties." This is the commutative analogue for h_d in x-variables (standard apolarity). It is a different action and a different object. It counts as adjacent prior art only.
- Abstracts read only: 2511.08780 (Aligholi–Maxim–Schürmann, L-classes; not about cap rank); 2603.29260 (Gorsky–Kim–Sherman-Bennett, toric Richardsons; nothing on PD); 1407.7228 (S_n-stable Gorenstein algebras; a different object); 0909.1112 (noncommutative inverse systems of QSym in noncommuting variables; a different object).

Verdict: **NOT FOUND.** The residual risk is in the commutative world (see §3: P1a is really a Sym question).

## 2. Negative controls (`gs/controls.py` → `out_controls.txt`)
For each case I compute the Hilbert function of QSym/Ann(X) for X ∈ NSym_d, at alternating α, L ≤ 9.

| X | L=5 | L=7 | L=8 | L=9 |
|---|---|---|---|---|
| R_s (P1a) | 1,1,2,2,2,1,1 | 1,1,2,2,3,2,2,1,1 | 1,1,1,2,2,2,2,1,1,1 | 1,1,2,2,3,3,3,2,2,1,1 |
| S^α | 1,1,2,3,2,1,1 | 1,1,2,3,5,3,2,1,1 | 1,1,2,3,5,5,3,2,1,1 | …,5,8,5,… (Fibonacci) |
| Λ^α | = S^α | = S^α | = S^α | = S^α |
| Ψ^α | 1,0,1,0,1,0,1 | 1,0,1,0,… | all 1 | 1,0,1,0,… |
| random ∈ NSym_d | 1,1,2,4,2,1,1 | 1,1,2,4,8,4,2,1,1 (compressed) | compressed | compressed |
| R_s + R_(d) | 1,1,2,3,2,1,1 | 1,1,2,3,4,3,2,1,1 | 1,1,2,3,3,3,3,2,1,1 | 1,1,2,3,4,4,4,3,2,1,1 |
| R_s + R_{s, last bit flipped} | 1,1,1,2,1,1,1 | 1,1,1,2,3,2,1,1,1 | 1,1,2,3,4,4,3,2,1,1 | 1,1,1,2,3,4,3,2,1,1,1 |

All controls **break** P1a for every L ≥ 4. For L ≤ 3 everything agrees, which is forced because the spaces are tiny. **P1a is not a generic-degree artifact.** Generic X is compressed (r_i = 2^{min(i,d−i)−1}).

## 3. Commutative shadow (`gs/shadow.py`, `gs/sym_big.py`)
**(A) Sym shadow.** Sym/Ann_Sym(r_s) under the Hall pairing, where r_s = χ(R_s) is the ribbon Schur function. Its Hilbert function is r^Sym_i = rank[⟨h_λh_μ, R_s⟩]_{λ⊢i, μ⊢d−i}. This is the weighted apolar algebra of r_s in the power sums p_k, using p_k^⊥ = k∂/∂p_k. The entries ⟨h_ν, R_s⟩ were computed two ways (shuffle products in QSym, and ribbon-filling counts), with 0 mismatches.
- **For alternating s, Hilb(G_s) = Hilb(Sym shadow) exactly**, L = 1..11 (`out_shadow.txt`). The Sym shadow equals the P1a/even formula for L = 1..16 (`out_sym_big.txt`).
- For non-alternating s they **differ**: 0010 gives QSym 1,1,2,2,1,1 against Sym 1,1,1,1,1,1; 0100110 gives QSym 1,1,2,4,8,4,2,1,1 against Sym 1,1,2,3,5,3,2,1,1.
- Since rank_Sym ≤ rank_QSym always, the alternating case says Sym → G_s is **surjective**: every F_u is congruent to a symmetric function mod Ann(R_s).
- Consequence: **P1a is equivalent to a Sym statement**, the apolar algebra of r_{(2^k)} or r_{(2^k,1)}, plus the surjectivity statement. That gives a cleaner proof route, and it is also the place where commutative owner risk lives. I searched for it and did not find it.

**(B) Polynomial shadow** (standard apolarity of r_s(x_1..x_n), n = 3, 4, 5, L ≤ 7). This shadow is unrelated: it is compressed or near-compressed. For example, L=7 with n=4 gives 1,4,10,20,35,20,10,4,1. **The QSym answer differs from the x-variable one.**

## 4. Blind tests (`gs/PREDICTION_L14.txt`, `gs/PREDICTIONS_all.txt` written before the runs; `out_alt_blind.txt`)
- Even L=14 prediction: [1,1,1,2,2,3,3,4,4,3,3,2,2,1,1,1]. The computed value is **identical (MATCH)**.
- Further runs, all predicted first: L = 15, 16, 17, 18, 19, 20 all MATCH (L=20 took 212 s). Odd P1a now holds for L ≤ 19, and the even formula for L ≤ 20.
- Closed form, conjectural (computed): for odd L, r_i = min(⌊i/2⌋, ⌊(d−i)/2⌋) + 1. This is the number of partitions of i into parts ≤ 2, truncated symmetrically.

## 5. P1b extension (`gs/p1b_scan.py` → `out_p1b_scan.txt`)
I scanned all 2^L strings for L = 2..14 (16384 strings at L=14). There are **0 violations**. r_2 = 1 holds for exactly 4 strings at even L and 2 strings at odd L, as predicted.

## Recommendation
- **P1b** is sound (computed L ≤ 14) and unowned. It is a 2-row rank question, so it fits one session, but it is thin and probably an exercise.
- **P1a (odd L)** is the better target. It is sound (computed L ≤ 19) and the controls break it. Prove it as two pieces:
  - (i) the Sym statement: the apolar algebra of r_{(2^k)} has Hilbert function equal to partitions into parts ≤ 2. Suggested route: show the Hall-pairing derivatives of r_{(2^k)} are generated by p_1, p_2.
  - (ii) Sym ↠ G_s for alternating s.
  - Part (i) alone is plausibly one session. Before claiming novelty, run a quick check of the commutative literature on ribbon Schur r_{(2^k)} under the Hall pairing.
