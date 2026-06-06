# BGGD type-uniform proof — induction strategy notes

**Status:** Synthesis from research-agent dispatch on 2026-05-13. **F_4 confirmation landed same day (see post-F_4 update below).** Doubly-laced uniformity now verified at B_2, B_3, C_3, AND F_4. The "opposite-direction iff mixed-unit-scale orbits" characterization held at F_4.

## Post-F_4 update (2026-05-13)

F_4 BGGD test ran: **78,428/78,428 pairs, both (A) and (B′) at 100.00%.** 218/218 BGG signed-sum consistency. Largest single basis 72,992 items at λ=(2,1,1,1). ~225 s compute.

Structural confirmation:
- F_4 **short** simples s_2, s_3 carry MIXED unit-scale orbits: 4 × 1-unit + 3 × 2-unit. **Predicted by the characterization** (the agent's note about C_n simples being "long-exchange" looks like a convention mis-recollection; both C_n and F_4 have mixed-unit at SHORT simples). Opposite-direction mixed swaps within s_3 (long-pair forward + short-half backward) verified, captured correctly.
- Mixed-pair share 4–11%, comparable to C_3's 12.6%. Below the "Falsifier #3" threshold of 50% which was never triggered.
- Files: `aug_tilde_F4.py`, `bgg_aug_compare_F4.py`, `F4_run_log.txt`, `F4_quick_results.md`.

**Implication for SU1.** The Diophantine uniqueness claim at the C_n short exchange simples extends to F_4 short simples (same structural feature: mixed unit-scale orbits). SU1 should be stated for general "mixed unit-scale" simples, not just C_n. The proof technique should be type-uniform within doubly-laced.

## Inductive hypothesis IH(n)

For every dominant integer/spin pair (λ, μ) for a rank-n doubly-laced root system (B_n with spin λ, C_n with integer λ), every bidegree (a, b), and every odd-length (w, π) basis vector with c_i := ⟨w·tilde_a, α_i^∨⟩ ≠ 0 for some simple reflection s_i, there exists a multiset distribution D = {((subtype, sign): count)} indexed by s_i-orbit-swap subtypes within ONE fixed s_i such that:

  (i) total α_i-shift of D equals −c_i α_i (bidegree-preserving net shift);
  (ii) donor capacities in π are respected;
  (iii) the resulting partner (s_i·w, π+ΔD) is even-length at the same bidegree;
  (iv) the resulting partner is the unique partner Aug~ assigns — bipartite graph admits perfect matching of all odds modulo BGG cohomology, coinciding with BGG-Verma chain differential restricted to bidegree (a, b).

Load-bearing: **(iv) oracle existence + uniqueness of BGG-chain partner.** (i)–(iii) constructive by move-set design.

## Oracle existence in non-graph form

> Given odd-length (w, π) at bidegree (a, b) with at least one simple s_i having c_i ≠ 0:
> there exists s_i with c_i ≠ 0 AND a multiset M = ⊔_{(st, ε)} m_{st,ε} of s_i-orbit-swap subtype st in direction ε ∈ {+, −}, satisfying
>   Σ_{st,ε} ε · m_{st,ε} · units(st) = c_i
> with non-negative donor capacity constraints, such that the resulting partner is bidegree-preserving and unique up to BGG cohomology classes.

I.e.: **the BGG-Verma matrix entry between (w, π) and (s_i·w, π') in the same bidegree, when nonzero, is realised by exactly one allowable Aug~-swap multiset.** Equivalent: a linear Diophantine system (with sign-flexible coefficients) over `(subtype, direction)`, with non-negative donor-capacity bounds, has at least one solution and the solution is unique up to BGG kernel.

## Opposite-direction characterization (the C_n surprise made structural)

**Opposite-direction within one s_i is forced ⟺ s_i acts on positive roots with orbits of MORE THAN ONE unit-scale.**

Equivalent: |⟨α_i, α^∨⟩| takes more than one nonzero value as α ranges over s_i-orbits on positive roots — i.e., s_i has both rank-1 (unit) and rank-2 (long-pair) orbits simultaneously.

Per-simple in doubly-laced classical:

| Type | Simple | Orbit structure | Opposite-dir needed? |
|---|---|---|---|
| B_n | long exchange α_i = e_i − e_{i+1} (i < n−1) | uniform 1-unit | No |
| B_n | short flip α_{n−1} = e_{n−1} | uniform 1-unit | No |
| C_n | long flip α_{n−1} = 2 e_{n−1} | uniform 1-unit | No |
| **C_n** | **short exchange α_i = e_i − e_{i+1} (i < n−1)** | **MIXED — 2-unit LL + 1-unit b/c** | **YES** |
| F_4 | (predicted) short simples | predicted MIXED | predicted YES |

**Structural footprint:** opposite-direction-within-one-s_i = "long roots fixed by an exchange simple on each side" — feature of C_n short exchanges, absent in B_n because B_n's long exchanges don't fix a 2-unit orbit.

## Literature verdict

**In the literature** (BGG 1971/75; Rocha-Caridi-Wallach 1982; Humphreys 2008 Ch. 6; Lepowsky 1977): existence of the BGG differential d_k = Σ_{w → s_iw} ±can_{w,s_iw} as a chain complex with d² = 0, acyclic in neg degrees. Each M(w·λ) → M(s_iw·λ) is a unique standard Verma embedding (up to ±1).

**NOT in the literature (apparently — needs verification):** the matrix expansion of this embedding in the **Kostant-partition basis at fixed bidegree (a, b)**, with the explicit statement that each non-zero matrix entry = exactly one s_i-orbit-swap multiset (the unique Diophantine solution).

**Closest known formulation:** Shapovalov / Jantzen-style embedding via multiplication by a divided power of a root vector e_{−α}^{(c)} in PBW coordinates — see Humphreys §6.5, Soergel "Kategorie O" survey. Gives entries exist; doesn't give the orbit-swap formula.

**Tentative claim:** the (A) + (B′) Kostant-partition-basis unwrapping is Rick's contribution. *Verify before publication* by careful literature search (Maple, OEIS-style — search BGG resolution + Kostant partition + Verma matrix entries + PBW basis).

## Recommended proof path (hybrid)

**Step 1 (literature import).** Take Humphreys §6 / RCW 1982: chain complex with d² = 0, M(w·λ) → M(s_iw·λ) unique standard Verma embedding. EXISTENCE HALF of oracle existence.

**Step 2 (unwrapping at PBW basis).** Compute the matrix of the standard Verma embedding e_{−α_i}^{(c_i)} : M(w·λ) → M(s_iw·λ) in Kostant-partition coordinates at bidegree (a, b). Show: each non-zero entry = exactly one s_i-orbit-swap multiset (unique non-negative Diophantine solution).

**Step 3 (rank induction).** Parabolic restriction to a rank-(n−1) Levi: at simples s_i (i < n−1), the action on positive roots factors through Levi P_i, and Aug~ moves at s_i depend only on the P_i-restricted Kostant partition. Apply IH(n−1) at Levi level. The remaining simple s_{n−1} (long flip C_n, short flip B_n) is 1-unit-uniform — directly at any rank without induction.

## Concrete next sub-task — SU1

> **SU1 (uniqueness of orbit-swap-multiset Diophantine solution at C_n short exchanges).** Given c_i ∈ Z, given donor multiplicities π(r) for each r in the s_i-orbit decomposition (one 2-unit LL pair + multiple 1-unit b/c pairs), prove the equation Σ ε · m · units(st) = c_i has at most one solution compatible with the standard BGG embedding e_{−α_i}^{(c_i)} acting on π's PBW monomial.

Hint: compute the expansion `e_{−α}^{(c)} · ∏ f_β^{n_β}` for short-exchange α; observe the orbit-swap monomial structure.

If SU1 succeeds for C_n short exchanges (the only non-trivial case), the full IH(n) inductive step reduces to existence-at-bidegree, which follows from Step 1 — and **BGGD is proved type-uniformly in doubly-laced rank n by induction with parabolic restriction.**

## Caveats / things to check

- [ ] F_4 short simples predicted to have C_n-like mixed structure — confirm with F_4 test (pending).
- [ ] Verify "Kostant-basis unwrapping is not in literature" claim — agent's literature search was inferential; do a careful search before claiming priority.
- [ ] Parabolic restriction step: check that the Levi-restricted Kostant partition + Levi-induced bidegree make sense (it should — bidegree is by α_i, and α_i is in the Levi).
- [ ] G_2 is OUT of scope (triply-laced); but a G_2 test would still inform unit-scale-orbit predictions for triply-laced.

## Files referenced

- `proofs/remark47/aug_tilde_C3_richer.py`
- `proofs/remark47/bgg_aug_compare_C3.py`
- `proofs/2026-05-13-bgg-aug-test-C3.md`
- `proofs/2026-05-12-bgg-aug-test-B3.md`
- `memory/connections/aug-tilde-as-bgg-differential.md`
- `memory/connections/aug-tilde-as-almousa-lu-shadow.md`
