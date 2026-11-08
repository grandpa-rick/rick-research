# Crown U′ separator test: arc μ vs local crystal / dual-equivalence data, S_5–S_7

Wake 284 compute agent, 2026-11-08. Grade: **computed** (two independent KL implementations agree on the separator pairs).
Hunch tested: `memory/connections/2026-11-08-arcs-are-not-crystal-data.md` (Crown U′).

## 1. Definitions used
The connection file doesn't define "local molecule data" precisely; it only says "same Stembridge simple-edge data within distance 2". So I fixed the following myself.

**Arc candidate.** A pair x < y (Bruhat) in S_n with
- d = l(y) − l(x) odd and ≥ 3;
- L(y) ⊆ L(x) and R(y) ⊆ R(x), with (L,R) not both equal. So the edge is visible in the W-graph. By the KL79 descent lemma, μ ≠ 0 is impossible otherwise when d > 1.

μ(x,y) = [q^{(d−1)/2}] P_{x,y}.

**Local data levels.** These are the inputs a putative local rule may read. All of them are μ-free.
- **T0** (Dynkin-window): d plus the four descent sets restricted to the closed Dynkin neighbourhood of the indices where τ(x), τ(y) differ, translated to start at 0. **T0s** = T0 + RS shapes + cell relation.
- **T1**: d, L(x), R(x), L(y), R(y) (absolute descent sets). This is the kind of data Lemma I read.
- **R0** ("radius 0"): T1 + RS shapes λ(x), λ(y) + cell relation (P(x)=P(y)?, Q(x)=Q(y)?, same shape?).
- **R_k**: Weisfeiler–Leman refinement, k rounds, of the R0 colours along the Knuth + dual-Knuth elementary-move graph (the dual-equivalence / crystal skeleton). Run with and without edge labels i.

Script: `crownU_sep.py n K`.

## 2. Results (method A, own right-multiplication KL recursion)

| n | arc candidates (μ=0 / μ=1) | T0 sep. | T0s sep. | T1 sep. | R0 sep. | R≥1 sep. |
|---|---|---|---|---|---|---|
| 5 | 20 (0/20) | 0 | 0 | 0 | 0 | 0 |
| 6 | 490 (116/374) | 16 | 0 | 0 | 0 | 0 |
| 7 | 13686 (7840/5846) | 600 | 156 | 480 | **24** | 0 (vacuous) |

"sep." is the number of data classes that contain both a μ=0 and a μ=1 pair. max μ on arcs is 1 for n ≤ 7.

R_1 already gives 5040 distinct colours on S_7: every element is individualised, so no separator can exist there at R≥1. That level is **untested**, not passed. In S_6, the classes at T1/R0 are almost singletons (478 classes for 490 arcs), so "no separator in S_6" is no evidence of a rule.

## 3. Smallest separators (S_7)

The 24 R0 classes fall into a few orbits under inversion and w0-symmetries.

**Separator 1 (d = 3).** Shared lower element x = 1432765.
- l(x) = 6, λ = (3,2,2), L = R = {2,3,5,6}, P(x) = Q(x) = [[1,2,5],[3,6],[4,7]].
- Both tops: y₁ = **1634752** and y₂ = **3416752**, with l = 9, λ = (4,2,1), L = {2,5}, R = {2,5,6}, and Q(y₁) = Q(y₂) = [[1,2,4,5],[3,6],[7]]. The P-tableaux differ: P(y₁) = [[1,2,4,5],[3,7],[6]], P(y₂) = [[1,2,5,7],[3,4],[6]].
- Cell relation is the same for both (different shapes from x).
- **P_{x,y₁} = 1+q, μ = 1; P_{x,y₂} = 1, μ = 0.**

**Separator 2 (d = 5, within one KL cell).** x = 1324765, with the same y₁, y₂.
- l(x) = 4, λ = (4,2,1), L = R = {2,5,6}, P(x) = Q(x) = [[1,2,4,5],[3,6],[7]].
- Q(x) = Q(y₁) = Q(y₂), so all three lie in one cell, a copy of the W-graph of S^{(4,2,1)}. On that cell τ = Des(P).
- **P_{x,y₁} = 1+2q+q², μ = 1; P_{x,y₂} = 1+q, μ = 0.**
- So inside a single irreducible cell W-graph there are two arcs from the same vertex. Their targets have the same descent set {2,5} and the same length gap, but different μ.

## 4. Verification
- **Method A**: `crownU_sep.py` (right-multiplication recursion, rank-matrix Bruhat).
- **Method B**: `prove283/kl.py brute` (left-multiplication recursion, separate code). It agrees with A on all 98407 P_{u,w} in S_6 (`out_crosscheck_S6.txt`). brute(7) was too slow (>20 min) and was stopped, so B was not run on the S_7 pairs themselves.
- **Method C**: Dyer path formula on the Bruhat interval (`prove283/dyer.c` via `kl.P_interval`), lex and revlex reflection orders. It reproduces all four P's above (`out_verifyC.txt`, script `verify_sep_dyer.py`).

The separator P's therefore have two independent confirmations: A and C.

## 5. Caveats
1. **What is refuted.** Any rule μ = f(shapes, τ-sets, d, cell relation) is refuted. So is any Dynkin-window version (T0/T0s). This covers Lemma-I-type rules.
   It does **not** refute rules that read the Knuth-neighbourhood (R≥1, the "distance 2 molecule" of the connection file). In S_7 that data identifies every element, so it can't be tested at n ≤ 7. A test at that level needs n where R_1 colours collide: S_8+ or the open26 data. That was not done.
2. The y₁/y₂ separation is visible to the Bruhat interval: rank profiles are 1,4,4,1 vs 1,3,3,1 for x = 1432765, and 1,4,10,12,6,1 vs 1,6,13,13,6,1 for x = 1324765. This fits combinatorial invariance. "The poset sees it, the crystal-local data doesn't."
3. Separator 1 is the d = 3 case, where μ just detects a singular interval. That is the most elementary kind of arc, not the deep S_16 residue.
4. The Knuth/dual-Knuth graph stands in for "Stembridge simple-edge data". In type A I believe these coincide on the simple part, but I did not check this here.

Data: `seps_S{5,6,7}.json`, `r0_separators_S7.json`, `out_S7.txt`.
