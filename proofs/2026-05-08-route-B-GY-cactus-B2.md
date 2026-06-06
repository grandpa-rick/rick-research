# Route B for Aug~ in type B: Gossow–Yacobi cactus ψ_J on W(B_2) vs Rick's Aug~

**Date:** 2026-05-08
**Author:** Agent (Opus 4.7), under Rick's direction
**Antecedents:**
- `papers/gossow-yacobi-2023-notes.md` — orientation notes on GY 2023.
- `proofs/2026-05-07-SA-B2-proof-and-Bn-program.md` — Aug~ for B_2/B_n.
- `proofs/remark47/aug_tilde_B2.py` — Rick's Aug~ for B_2.
- arXiv:2306.08857 (GY 2023) — definitions B.7, B.8, B.10 specifically.

**Scripts:** `proofs/remark47/route_B/{kl_W_B2.py, mathas_involution_B2.py, psi_J_B2.py, full_comparison.py, orbit_analysis.py}`

---

## 1. Summary

| Question | Answer |
| --- | --- |
| Did GY's ψ_J for W(B_2) get implemented? | **YES** — fully, all 4 subsets J ⊆ {s_0, s_1}. |
| Does Aug~ project to ψ_J at the w-level for any J? | **NO** — for 43/140 dominant spin pairs, no J works. For the matching 97/140, all four J's match equally — but only because Aug~ acts trivially on w in those pairs. |
| Single biggest finding | Aug~ at the w-level always changes ℓ(w) by ±1 (single simple reflection), but ψ_I in W(B_2) changes ℓ(w) by ±2 (cell-internal swap). Structural mismatch. |
| Single biggest blocker for B_3/B_n | We have not yet computed Mathas's ψ_C on W(B_3) cells; even at B_2 we found ψ_J does not match Aug~ in any direct projection sense. |

---

## 2. GY's ψ_J for W(B_2) — explicit computation

### 2.1 Setup

In our (and GY's) conventions, for B_2 we use simple roots
- α_0 = e_0 − e_1 (long), s_0 = swap of coordinates 0, 1
- α_1 = e_1 (short), s_1 = sign-flip on coordinate 1.

W(B_2) = ⟨s_0, s_1 ∣ s_0² = s_1² = 1, (s_0 s_1)⁴ = 1⟩, |W| = 8.

### 2.2 KL polynomials and left cells of W(B_2)

By direct recursion (script `kl_W_B2.py`), all KL polynomials P_{x,w}(q) ≡ 1 for x ≤ w in W(B_2) (this is well known). Consequently
$$C_w = \sum_{x \le w} x \in \mathbb Z[W], \quad w \in W(B_2).$$

The left preorder ≤_L gives **four** left cells:

| Cell | Elements | Length pattern |
| --- | --- | --- |
| C₀ | {e} | {0} |
| C₁ | {s_1, s_0 s_1, s_1 s_0 s_1} | {1, 2, 3} |
| C₂ | {s_0, s_1 s_0, s_0 s_1 s_0} | {1, 2, 3} |
| C₃ | {s_0 s_1 s_0 s_1 = w_0} | {4} |

(Note: This matches the standard representation theory of B_2: cells correspond to two-sided cells / families of irreducibles; the rank-2 cells correspond to the 2-dim irreps of W(B_2).)

### 2.3 Mathas's involution ψ_C on each cell

By Proposition B.4 of GY (= Theorem 3.1 of Mathas 1995), there is an involution ψ_C: C → C such that w_I · [C_x] = ±[C_{ψ_C(x)}] modulo lower-order terms in C^<.

I computed ψ_C for each cell of W(B_2) by:
1. Forming C_x = sum of all y ≤ x in Bruhat order (group ring element).
2. Left-multiplying by w_I = s_0 s_1 s_0 s_1 in C[W].
3. Re-expanding in the KL basis triangularly.
4. Reading off the coefficient on the cell.

**Result** (file `mathas_involution_B2.py`):
- C₀ = {e}: w_I · C_e = +C_e + (lot in C^<). So ψ_C₀(e) = e, sign = +1.
- C₁ = {s_1, s_0 s_1, s_1 s_0 s_1}:
  - w_I · C_{s_1} = −C_{s_1 s_0 s_1} + (lot). So ψ_C₁(s_1) = s_1 s_0 s_1.
  - w_I · C_{s_0 s_1} = −C_{s_0 s_1} + (lot). So ψ_C₁ fixes s_0 s_1.
  - w_I · C_{s_1 s_0 s_1} = −C_{s_1} + (lot). So ψ_C₁ swaps with s_1.
  - Sign = −1, constant on the cell.
- C₂ = {s_0, s_1 s_0, s_0 s_1 s_0}: by symmetry,
  - ψ_C₂(s_0) = s_0 s_1 s_0, ψ_C₂(s_1 s_0) = s_1 s_0, ψ_C₂(s_0 s_1 s_0) = s_0.
  - Sign = −1.
- C₃ = {w_0}: w_I · C_{w_0} = C_{w_0}. ψ_C₃(w_0) = w_0, sign = +1.

### 2.4 ψ_J for each parabolic subset J ⊆ {0, 1}

Definition B.7 (GY): ψ_J(x) = ψ_{C(u)}(u) · π_J(x) where x = u · π_J(x), u = Res_J(x) ∈ W_J, π_J(x) ∈ ^J W min coset rep.

Since W_J for |J| ≤ 1 is either trivial or A_1, and A_1 has only singleton left cells, ψ_C is the identity for all cells of W_J in those cases. Therefore:

| J | W_J | ψ_J |
| --- | --- | --- |
| ∅ | {e} | identity on W(B_2) |
| {s_0} | {e, s_0} | identity on W(B_2) |
| {s_1} | {e, s_1} | identity on W(B_2) |
| {s_0, s_1} = I | W(B_2) | nontrivial: s_1 ↔ s_1 s_0 s_1, s_0 ↔ s_0 s_1 s_0; e, s_0 s_1, s_1 s_0, w_0 fixed |

So **the only nontrivial ψ_J in B_2 is ψ_I**, the longest-element / Schützenberger involution. ψ_I fixes the even-length elements {e, s_0 s_1, s_1 s_0, w_0} and swaps the length-1 elements with the length-3 elements within their cell.

This is a very natural object: the Schützenberger / evacuation involution restricted to W. **It changes Bruhat length by ±2 (within each 3-element cell).**

---

## 3. Comparison with Rick's Aug~

### 3.1 Structural observations

Aug~ acts on (w, π) pairs. Its action on the w-component is:
- M_1 (long-swap): w → s_0 · w (changes ℓ(w) by ±1).
- M_2 (short-swap): w → s_1 · w (changes ℓ(w) by ±1).
- Fixed point: w → w (no change).

ψ_I, in contrast, changes ℓ(w) by ±2 within each non-singleton cell. ψ_∅, ψ_{s_0}, ψ_{s_1} are all the identity on W(B_2).

**These cannot agree on nontrivial w's.** The only case Aug~ matches ψ_J at the w-level is when Aug~ at w is the identity (i.e., the (w, π) pair is Aug~-fixed) AND ψ_J(w) = w.

### 3.2 Numerical comparison (script `full_comparison.py`)

Tested on all **140 dominant spin pairs (λ, μ)** with λ_0 ≤ 9/2, totaling **518 (w, π) pairs**:

| J | Aug~_w(w, π) = ψ_J(w) at item level | At pair level |
| --- | --- | --- |
| ∅ | 316/518 (61.0%) | 97/140 |
| {s_0} | 316/518 (61.0%) | 97/140 |
| {s_1} | 316/518 (61.0%) | 97/140 |
| I | 316/518 (61.0%) | 97/140 |

The 316 matching items are exactly the Aug~-fixed-points (= 316 fixed points across all spin pairs). For these, Aug~'s w-action is trivial, so it matches all four ψ_J trivially because ψ_J fixes each of these w's.

The remaining 202 items are **Aug~-flipped** pairs (e.g., (e, π) ↔ (s_0, π') via M_1). For these:
- ψ_∅, ψ_{s_0}, ψ_{s_1}: would predict w → w (no flip).
- ψ_I: would predict s_0 → s_0 s_1 s_0 (length-3, not s_0).

So none of the four ψ_J's predicts Aug~'s flips correctly.

### 3.3 Pairs (λ, μ) where some ψ_J fully matches Aug~

97 of 140 pairs match — these are the (λ, μ) for which Aug~ has *no flips* at all (every contributing (w, π) is Aug~-fixed). Roughly: small (λ, μ) with all KL contributions on length-zero w = e.

The 43 mismatching pairs include all the "interesting" ones: λ = (3/2, 3/2), λ = (5/2, ...), where Aug~ does flip pairs. For these, Aug~ ≠ ψ_J for any J.

### 3.4 Orbit-level comparison (script `orbit_analysis.py`)

**Q1: Aug~-fixed (at w-level) ⊆ ψ_I-fixed?**
Yes — **140/140 pairs**. This is essentially the statement that fixed points of Aug~ have even Coxeter length (Lemma 2.5 of `2026-05-07-SA-B2-proof-and-Bn-program.md`), and ψ_I fixes exactly the even-length elements {e, s_0 s_1, s_1 s_0, w_0}. So Aug~'s fixed-point set is *consistent* with ψ_I's, but is a much stronger condition (Aug~ must actually have a Kostant partition that's M-applicable-free).

**Q2: Does Aug~(w, π) stay in the ψ_I-orbit of w?**
Only **316/518 (61.0%)**. The 202 "out-of-orbit" cases are Aug~ flips like e → s_0 (where ψ_I-orbit of e is just {e}).

So **Aug~ is not a refinement of ψ_J on (w, π) pairs**, in any of the natural senses (w-level matching, orbit preservation, fixed-point inclusion-as-equality).

---

## 4. Honest assessment

### 4.1 What worked

- Computed the KL basis of C[W(B_2)] from scratch. P_{x,w} ≡ 1 (well-known but verified).
- Computed all 4 left cells of W(B_2).
- Computed Mathas's involution ψ_C on each cell directly from the action of w_I on the KL basis (no need to look up a closed form).
- Computed ψ_J for all four subsets J ⊆ {s_0, s_1}.
- Compared with Aug~ over 140 dominant spin pairs (518 (w, π) items).

### 4.2 What's the discrepancy structurally

Aug~ is parametrized by π and changes w by a single simple reflection. ψ_J in W(B_2) is parameter-free and changes w by an involution on cells (length-2 swaps). They are doing fundamentally different things.

A possible resolution: **Aug~ may correspond to an iterated/composed ψ_J construction**. Specifically:
- For B_2, ψ_I = (action of cactus generator c_I) is one cactus generator.
- Aug~ "decorates" the (w, π) pair with finer combinatorics that distinguish flips of different Kostant partitions.
- It is plausible Aug~ encodes the action of multiple cactus generators applied iteratively, but THIS NEEDS TO BE TESTED. Specifically: define ψ_iterated(w, π) by a sequence of cactus generators c_{J_1} c_{J_2} ... applied in some order determined by the bidegree (i, j). Compare to Aug~.

### 4.3 Remark B.10 — the cactus group action

GY remark B.10 states: the cactus group of W (defined by c_J for J ⊂ I connected with W_J finite, with cactus relations) acts on W via c_J · x = ψ_J(x). For W(B_2), the connected J's with W_J finite are:
- {s_0}, {s_1}, {s_0, s_1}.
Each gives a cactus generator. {s_0} and {s_1} act trivially (id on W). Only {s_0, s_1} = I acts nontrivially. So the cactus group action on W(B_2) is generated by ONE involution ψ_I.

This is much weaker than what Aug~ encodes. **Aug~'s action involves both s_0 and s_1 simple reflections, not just w_I.** So the GY cactus framework on W alone is *too coarse* to recover Aug~.

### 4.4 What Aug~ would correspond to in GY's framework

If Aug~ projects to anything in GY's framework, it would have to be a finer object than ψ_J on W. Candidates:
- The **action of individual T_i (= s_i in C[W])** on the KL basis at q = 1, restricted to certain bigraded submodules. This would correspond to BGG complex differentials in the Verma resolution, NOT to the cactus action.
- The **cactus action on a *bigraded* / *Kostant-partition-decorated* version of W**. This would be a new construction not in GY 2023.

GY's ψ_J is built from the cactus group / Schützenberger involution. Aug~ is built from the BGG / Verma resolution differentials. These are **different categorical structures**: cactus action acts on the CATEGORY's Grothendieck group, while BGG differentials live INSIDE the resolution. They could very well give different combinatorics.

### 4.5 Single biggest finding

**Aug~ is not ψ_J for any J in W(B_2), at the w-level.** The reason is structural: Aug~ encodes BGG-resolution differentials (one simple reflection at a time, with a Kostant-partition decoration), whereas ψ_J encodes cactus / Schützenberger involutions (swapping endpoints of cells via the longest element w_J). These are different combinatorics for different objects. Aug~'s consistency with ψ_J is at the level of *fixed-point parities* (both fix even-length elements, in different senses), but not as a w-level projection.

### 4.6 Single biggest blocker for B_3 / B_n

To extend this comparison to B_3, we'd need:
1. KL polynomials for W(B_3) — not all 1; the recursion is more involved and produces nonconstant polys (e.g., P_{x, w_0}(q) = 1 + q for some pairs in B_3).
2. Left cells of W(B_3) — there are several, with sizes related to 2-dim and 4-dim irreps.
3. Mathas's involution ψ_C on each — requires computing w_I action on KL basis through nontrivial cells.
4. **Most importantly:** even after doing this, we already see in B_2 that Aug~ ≠ ψ_J at the w-level. Without a deeper structural insight (e.g., Aug~ corresponds to an iterated cactus or a different categorical object), running the same comparison for B_3 is mechanical but unlikely to be illuminating.

The real blocker is **conceptual**: do we expect Aug~ to project to ψ_J at all? The B_2 evidence suggests **NO**, and we should look for a different categorical interpretation of Aug~ (e.g., BGG resolution differentials, or a *bigraded* refinement of GY's framework that GY don't develop).

---

## 5. Where to look next

1. **CKL Theorem 4.6 / Aug-on-horizontal-strips**: the original combinatorial sign-reversing involution on which Rick's Aug~ is modeled lives there. Compare CKL's involution to ψ_J directly.
2. **Bonnafé "Cells and cacti" 2016** — earlier than GY, may give finer combinatorics on cells. Worth checking if Bonnafé's cell-level description of c_J reveals Kostant-partition structure.
3. **Liao–Yang–Yu 2025 (arXiv:2510.12046)** — A↔B separable bijection. Could give the missing link if Rick's A-side Aug~ analog is known to project to ψ_J in type A.
4. **Lift ψ_J to (w, π)-pairs**: extend GY's parabolic-coset decomposition x = u·a to a decomposition on the bigraded KL-positivity object. Define ψ_J^{ext}(w, π) = (ψ_C(Res_J(w)) · π_J(w), some_action_on_π) and check if a natural "some_action_on_π" exists that recovers Aug~.

Honest verdict: **Route B (GY's cactus) is *consistent* with Aug~ at the parity / fixed-point level, but does not project to Aug~ at the (w, π) level. They are two different sign-reversing involutions for the same KL polynomial, coming from two different categorical setups (cactus action vs BGG differentials).** This is interesting but not the cactus-realization-of-Aug~ Rick was hoping for.
