# Wake 284 scoping: Q68 in type D_n (dominated twins), 2026-11-08

Sources: memory/questions/q-type-D-KL-optimization.md; proofs/2026-11-08-q68-typeA-closure.md;
proofs/registry/seedQ2-kl-cone.json; code in proofs/wake279, prove282, prove283.

## 1. The question

Setting: W = W(D_n), simply laced, Coxeter graph with branch node s_{n-2} and leaves s_{n-1}, s_n.
Γ is a left cell. The cell module is GW convention C at v=1: (1+s)e_x = 0 if s ∈ L(x), else 2e_x + Σ_{s∈L(y)} μ̃(x,y)e_y.

**Dominated twin**: x ≠ z ∈ Γ with L(z) ⊆ L(x), and (TW) μ̃(y,z) ≥ μ̃(y,x) for every y ∈ Γ with L(y) ⊄ L(x).
By Lemma A, a twin makes C_KL(Γ) non-maximal.

**Q68-D**: for which n does some left cell of D_n contain a dominated twin? Let n_D be the least such n.

What is known (all computed, `wake279/out_twin_D5.txt`, `interior.py`):
- D4 and D5 have 0 twins, and (★) holds in every cell.
- The D4 reducible cells (dims 10, 14) fail the maximality scan without a twin. That is a separate, non-twin obstruction, like the H3 5_2 node, which has hunch grade.

## 2. Tool transfer

**Verbatim for any W, or any simply-laced W** (registry grade in brackets):
- Q68-twin-lemma, Lemma A [proved]. Needs μ ≥ 0, which is Elias–Williamson for any Coxeter group.
- Q68-c-star-kill, C1/C2 [proved]. Any m=3 pair. C2 holds in any simply-laced W, so a twin needs ∅ ≠ L(z) ⊆ int L(x) **computed with the D graph**: the branch node needs all 3 neighbours in L(x).
- Q68-c-caseB-lemma, Lemma C4 [proved, simply-laced].
- Q68-witness-completeness, Thm W + Cor W2 [proved, any finite W / connected simply-laced].
- Q68-parity-lemma [proved]. Q68-ii-parity-half and Q68-ii-reduce-to-lemmaI [proved]; they use only lengths and monotonicity of int.
- Q68-lemmaS-star-invariance, Lemma S [proved, any W with m=3].
- Q68-layer-lemma [proved, any Coxeter; folklore Billey–Braden].
- Prop C certificate types 1 and 2, as logic.
- Prop Q steps 2–4 generalise. A right star maps a left cell bijectively onto a left cell and preserves L and μ̃; the image cell Γ″ satisfies ρ(Γ″) ⊆ Γ, which replaces the f^λ count. So verdicts transport along **right-star orbits of cells**.

**Type-A only:**
- Prop Q's step 1 (Knuth connectivity, Lemma K). In D_n, left cells of a two-sided cell can carry different constructible modules, so they are not all star-connected. Cell independence holds only within a star-orbit.
- Thm C3 ("no twins S_n, n≤13"), which is the RSK/Kostka dominance check.
- Props D/K/R (Young layers), Prop M, Q68-mu-in0.
- All census code: `dominance_star.py`, `listn.py`, `certifyn.py`, `verifyn_*.py`, `verify_red.py`.
- Thm B (Q68-b-thmB) is vacuous, since there is no m ≥ 4 bond.

**Code inventory:**
- `wake279/coxkl.py`: generic, takes a Coxeter matrix, handles D. It stores a dense N×N×deg P array, used by twin_criterion/interior/lemI_cox. D5 runs in 20 s. D6 needs about 50 GB, so it is infeasible.
- `prove282/lemI_cox.py`: generic, has D4/D5 entries, built on coxkl.
- `prove283/dyer2.c`, `dyer.c`, `verify_indep/{kl,parab}.py`: S_n permutations only. dyer2 packs values in 4 bits, so n ≤ 16.
- No GAP, Sage or Coxeter3 on the box. 4 cores, 23 GB RAM.

## 3. Feasibility and structure

**New lemma (proved in this scoping, using F1, F2, Thm W and the subword property).**
*Boundary kill.* Let J ⊊ S and x, z ∈ W_J, and suppose some s ∈ L(x) is adjacent (m=3) to some t ∉ J. Then (x,z) is not a twin in W.

*Proof.*
1. x has type {s} for {s,t}. Since sx ∈ W_J has neither s nor t as a left descent, the star is *x = tx, and F2 puts tx in Γ.
2. Thm W(d) then requires μ̃(tx, z) ≥ 1.
3. tx < z is impossible by the subword property, since tx ∉ W_J and z ∈ W_J.
4. If z < tx, then t ∈ L(tx) \ L(z), and F1 forces z = x.
5. So μ̃(tx, z) = 0, and (x,z) is not a twin. ∎

*Consequence.* The S_14 twins do **not** lift naively to D_14 ⊃ A_13. All four have s_12 ∈ L(x), and s_12 is the branch node, adjacent to the omitted leaf. So type D twins must be "genuinely D", and n_D could exceed 14. There is no structural upper bound yet.

**Feasibility:**

| n | \|D_n\| | method | verdict |
|---|---|---|---|
| 6 | 23040 | new generic C full-KL (extremal-pair/double-coset reduction), validated against coxkl on A5/D4/D5 | about 10^8 comparable pairs, ≤ 2 GB; **one session** |
| 7 | 322560 | full KL | ~5·10^10 pairs, out of reach for homemade code |
| 7, 8 | 322560, 5160960 | Geck-count route (below) | possible; second session; needs D_n character code written from scratch |

The Geck-count route needs #{w ∈ Γ : L(w) ⊇ J} = ⟨[Γ], Ind_{W_J} sgn⟩. This rests on Geck 2003 restriction of cells (recall-only) together with left-cell modules being constructible characters (Lusztig; symbols). That gives a (★)-check, the analog of C3, with no KL at all. Twins at a (★)-violator would then need star certificates plus a D-capable Dyer code.

## 4. Candidate PROVE problem

**Theorem D6 (target).** No left cell of W(D_n), n ≤ 6, contains a dominated twin. Hence every failure of maximality there is non-twin.

Proof plan:
1. Prove the Boundary-kill lemma in-file.
2. Build cells and μ for D6 with a new generic C KL code. Validate it against coxkl on A5, D4 and D5 (full P equality) and against `out_twin_D5.txt`.
3. Run C2/(★) on every cell.
   - If (★) holds, the theorem follows from C2 alone, since C2 is proved. The grade is computed for the cells, proved for the logic.
   - If (★) fails, decide each candidate exactly with the Thm W witness inequality, using the full μ.
4. Report the D6 (★)-violators, if any, as the first D-native data, and prepare the Geck-count route for D7/D8.

Evidence: D4 and D5 have 0 twins and (★) holds. C2 is stricter in D because of the branch node.

Main risks:
- (a) The C KL code is the only engine with no independent replay above D5. Mitigation: a dense-Python spot check on random intervals, plus left-cell counts matching the Lusztig/known D6 left-cell count (recall-only).
- (b) The result is likely negative-and-vacuous, like A_n for n ≤ 13. "No twins D6" is weak evidence about n_D, and the interesting regime is probably n ≥ 10, where only the character route reaches.
