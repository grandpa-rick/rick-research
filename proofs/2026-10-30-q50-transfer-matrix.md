# Q50: Σ_{ρ⊆κ} V(κ/ρ) ∏ q_diag = ∏_{d=0}^{m−1} (2+q_d)  — PROVED (two proofs: transfer matrix + explicit bijection)

PROVE 264, 2026-10-29 (file dated 10-30 as PROVE.md asked). Registry node `q488-Q50-3m-transfer-matrix`.
Bounded jewel: proofs/ only, no draft edit. Scripts: `proofs/wake264/` (`q50_count.py`, `q50_refine.py`, `q50_diag.py`, `q50_bij.py`).

## Statement

Setting and definitions as in `proofs/2026-10-30-q48-ls-vmap.md`. Strict partitions with parts ≤ m ↔ shifted diagrams
D(·) ⊆ staircase Σ_m = {(a,b): 0 ≤ a ≤ b ≤ m−1} (row a, column b, diagonal d = b−a), with componentwise order. For ρ ⊆ κ,
V(κ/ρ) = #V-maps on θ = κ/ρ = #{λ : ρ ⊆ λ ⊆ κ, λ/ρ and κ/λ antichains, κ/λ diagonal-free} (Q48 Step 2).

**Theorem Q50.** Σ_{ρ⊆κ⊆Σ_m} V(κ/ρ) ∏_{x∈κ/ρ} q_{diag(x)} = ∏_{d=0}^{m−1} (2+q_d).

Equivalently: (a) if V(κ/ρ) > 0 then κ/ρ has at most one box on each diagonal; (b) for every D ⊆ {0,…,m−1}, the
V-weighted number of pairs ρ ⊆ κ with {diag(x): x ∈ κ/ρ} = D is 2^{m−|D|}.
Corollaries: q_d = q gives (2+q)^m; q = 1 gives Σ V = 3^m.

## Step 0: dictionary (antichain skews = sets of addable boxes = parallel hops)

Shifted diagrams are exactly the order ideals of the poset Σ_m. (Row a of a strict λ is {(a,a),…,(a,a+λ_a−1)}; the ideal
condition at (a,b) is "(a−1,b) and (a,b−1) present when they lie in Σ_m", i.e. λ_{a−1} > λ_a — strictness.)

**Lemma 0.1.** For order ideals ρ ⊆ λ of a poset, λ/ρ is an antichain ⇔ λ = ρ ⊔ A with every x ∈ A addable to ρ
(i.e. ρ ∪ {x} an ideal). Any subset A of the addable set Add(ρ) gives an ideal ρ ⊔ A with antichain skew.

*Proof.* (⇒) x ∈ λ/ρ; any y < x lies in λ (ideal) and not in λ/ρ (antichain), so y ∈ ρ: x is addable. (⇐) If x < y are
both addable to ρ, addability of y forces x ∈ ρ, contradiction; so Add(ρ) is an antichain. ρ ⊔ A = ∪_{x∈A}(ρ ∪ {x}) is a
union of ideals. ∎

**Lemma 0.2 (particles).** Identify λ with the set S(λ) ⊆ {1,…,m} of its parts ("occupied sites"); put a permanently
occupied reservoir at site 0. The addable boxes of λ are:
- for each part p = λ_a with p < m and p+1 ∉ S(λ): the box (a, a+p), on **diagonal p** ("hop p → p+1");
- if 1 ∉ S(λ): the box (ℓ, ℓ), ℓ = ℓ(λ), on **diagonal 0** ("injection 0 → 1").
Adding a set A ⊆ Add(λ) performs all the corresponding hops simultaneously, and S(λ ⊔ A) is the resulting occupied set.

*Proof.* Row a has boxes (a,a),…,(a,a+λ_a−1), so its only candidate is (a, a+λ_a), on diagonal λ_a = p. For a = 0 it
needs only the staircase bound a+λ_a ≤ m−1, i.e. p < m (and p+1 ∉ S holds trivially since p is the largest part). For
1 ≤ a < ℓ it needs (a−1, a+λ_a) ∈ λ, i.e. λ_{a−1} ≥ p+2, i.e. p+1 ∉ S; the staircase bound then follows from
λ_{a−1} ≤ m−(a−1). The new-row candidate (ℓ,ℓ) needs (ℓ−1,ℓ) ∈ λ, i.e. λ_{ℓ−1} ≥ 2, i.e. 1 ∉ S (vacuous if ℓ = 0).
Adding the box raises the part p to p+1 (and the new row has part 1). Distinct addable boxes lie in distinct rows, so the hops have distinct sources. Their targets
p+1 are empty, hence distinct from every source, so the simultaneous update is well defined and keeps the row order. ∎

(Machine: `q50_bij.py` checks λ/ρ ⊆ Add(ρ) for every step-1 move and κ/λ ⊆ Add(λ) diagonal-free for every step-2 move,
m ≤ 8, 0 failures. Together with Q48's brute-force V-map counts it gives 0 mismatches for m ≤ 5.)

**Consequence.** By Lemmas 0.1–0.2, V(κ/ρ) counts the two-step histories S(ρ) →₁ S(λ) →₂ S(κ). Step 1 is any set of
legal hops, injection allowed. Step 2 is any set of legal hops, no injection (diagonal-free). A box created by a hop
out of site d sits on diagonal d. So the LHS of Q50 is

  Z = Σ_{histories} ∏_{hops} q_{source site}.

## Step 1: (a) is the obvious point, and it is one line

Let f_t(d) ∈ {0,1} be the flow on bond d → d+1 at step t (d = 0,…,m−1; f_2(0) = 0). If f_1(d) = 1 then site d+1 is
occupied after step 1, so no hop d → d+1 is legal at step 2: **f_1(d) f_2(d) = 0.** Diagonal d carries f_1(d)+f_2(d) ≤ 1
boxes. That is (a). (A single antichain step has at most one box per diagonal anyway, since Lemma 0.2 gives one hop per source site. So (a)
says exactly that the two steps never both use the same bond.)

## Step 2: localisation (the history is local data at each site)

A history is the data (n_0, f_1, f_2): the initial occupation n_0 ∈ {0,1}^{1..m} and the flows. Then n_1, n_2 are
determined by conservation, n_t(j) = n_{t−1}(j) + f_t(j−1) − f_t(j) (with f_t(m) := 0). Legality of hop d → d+1 at step t
says n_{t−1}(d) = 1 and n_{t−1}(d+1) = 0. Each of these conditions involves **one** site. So the legality conditions are
the conjunction over sites j = 1..m of the local conditions

  L_j: [out_t ⇒ n_{t−1}(j) = 1] and [in_t ⇒ n_{t−1}(j) = 0] for t = 1,2,   where in = (f_1(j−1), f_2(j−1)), out = (f_1(j), f_2(j)).

The reservoir condition at site 0 is vacuous (it is always occupied, and f_2(0) = 0 is imposed). Under L_j, n_t(j) ∈ {0,1}
automatically, because in_t and out_t cannot both be 1. Conversely, any (n_0, f) satisfying all L_j is a legal history.
For fixed flows, n_0(j) is chosen independently at each site, so

  Z = Σ_{f} ∏_{d} q_d^{f_1(d)+f_2(d)} ∏_{j=1}^m c(in_j, out_j),  c(a,b) := #{n_0(j) ∈ {0,1} satisfying L_j}.

By Step 1, flows on a bond lie in {00, 10, 01}. Table of c (rows a = in, cols b = out, order 00,10,01), by direct check:
- a=00: b=00 → n_0 free (2); b=10 → n_0=1 (1); b=01 → n_1=n_0=1 (1).
- a=10: n_0=0, n_1=1−b_1: b=00 → 1; b=10 → needs n_0=1, **0**; b=01 → n_1=1 ok, 1.
- a=01: needs n_1=0: b=00 → n_0=0 (1); b=10 → n_0=1, n_1=0 (1); b=01 → needs n_1=1, **0**.

  M = [[2,1,1],[1,0,1],[1,1,0]].

## Step 3: transfer matrix and eigenvector

Bond 0 (injection): in-state of site 1 is 00 or 10, so u = (1, q_0, 0). Site m has no out-bond: out = 00. With
W_d = diag(1, q_d, q_d):

  Z = u · M W_1 M W_2 ⋯ M W_{m−1} M e_{00}.

x := M e_{00} = (2,1,1). Then M W_d x = M(2, q_d, q_d) = (4+2q_d, 2+q_d, 2+q_d) = (2+q_d) x. Hence
Z = (2+q_1)⋯(2+q_{m−1}) · u·x = (2+q_0)(2+q_1)⋯(2+q_{m−1}). ∎

(b) is read off: the coefficient of ∏_{d∈D} q_d in ∏(2+q_d) is 2^{m−|D|}.

## Step 4: second proof — the bijection {histories} ↔ {0,1,2}^m (letter 2 ↔ box on diagonal d)

Fix the support D = {d : f_1(d)+f_2(d) = 1}. Split D into maximal blocks of consecutive bonds [a,b].
- Inside a block, consecutive hops alternate in type: c(10,10) = c(01,01) = 0, c(10,01) = c(01,10) = 1. So each block
  has exactly 2 type patterns, except the block containing bond 0, which must start with 10 (injection is step 1 only)
  and has 1.
- A site touched by a hop (c-entry with a or b ≠ 00) has n_0 forced (all such c are 0 or 1). A site with in = out = 00
  ("free site") has 2 choices.
A block [a,b] touches sites a..b+1 (only 1..b+1 if a = 0). Blocks are separated by a non-D bond, so these sets are
disjoint. Hence #free sites = m − Σ_blocks(|B|+1) + [0∈D] = m − |D| − #blocks + [0∈D], and the count for support D is
2^{#free + #blocks − [0∈D]} = 2^{m−|D|}. This is (b) again, with no matrices.

Explicit bijection. For a history, define w ∈ {0,1,2}^m indexed by diagonals d = 0..m−1:
- w_d = 2 if diagonal d carries a box of κ/ρ (d ∈ D);
- else, if d+1 ≤ m−1 and d+1 ∈ D: w_d = 0/1 according to whether the box on diagonal d+1 is in λ/ρ or κ/λ (it fixes the
  type of the block starting at d+1);
- else w_d = [d+1 ∈ S(ρ)] (site d+1 is free: in-bond d ∉ D, out-bond d+1 ∉ D).
The non-D diagonals split into "just before a block" (↔ blocks not containing 0) and "d+1 ∉ D" (↔ free site d+1), and
this splitting is a bijection, by the count above. So w ↦ history is well defined and inverse. Weight ∏ q_{diag} = ∏_{w_d=2} q_d.
Machine: `q50_bij.py`, m ≤ 8: injective, image = all 3^m words, 0 failures.

## Symmetry check (the mirror)

Injection allowed at step 2 only: u' = (1, 0, q_0), u'·x = 2+q_0, same product. That is the R-rotation mirror
of PROVE.md. Controls: injection in both steps gives u'' = (1, q_0, q_0) (the state 11 on bond 0 is still impossible,
since f_1(0) = 1 fills site 1), so u''·x = 2+2q_0, i.e. 4·3^{m−1} at q = 1. No injection gives u = (1,0,0), i.e. 2·3^{m−1}.
Both match the Wake 264 controls, from the same eigenvector.

## Owner hunch (noted, not chased)

∏(2+q_d) is a principal-specialisation-shaped product. It smells like the character of a tensor power of a 3-dim crystal
(B(ω_1) of sl_2 ⊗ trivial?) or a vertex-model/TASEP partition function with a rank-1 transfer matrix eigenvector. Not chased.

## Verification
- `q50_count.py`: particle model = brute V-maps per (κ,ρ), m ≤ 5; totals 3^m for m ≤ 10 (Wake 264).
- `q50_refine.py` / `q50_diag.py`: per-diagonal product for m ≤ 6 (Wake 264).
- `q50_bij.py` (PROVE 264): dictionary Lemmas 0.1/0.2, (a), the explicit bijection, and V-map recount, m ≤ 8, 0 failures.

## Gaps
None. Logical inputs: the V(θ) ↔ λ reformulation (Q48 Step 2, elementary) and the shifted-diagram conventions. No literature.
