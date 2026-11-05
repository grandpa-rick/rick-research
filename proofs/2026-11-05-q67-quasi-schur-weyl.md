# PROVE 278 — Q67: q=0 Schur–Weyl at the quasi-crystal level ("quasi dual equivalence")

Date: 2026-11-05. Status: **(a), (b), (c), (d) PROVED.** (c) cites Krob–Thibon for one input, and that input is also computed.
Code: `proofs/prove278/q67.py`. It is an independent re-implementation from the printed definitions and does not import the PROVE 275/276/Wake 277 code.

Verdict in one line: **the statement is a five-line corollary of Gessel's b-coordinates (our Theorem B).** Its set-level content belongs to Krob–Thibon/Novelli (the quasi-ribbon RS correspondence w ↦ (Q,R)). What's new is the graph-level packaging with explicit position swaps, which is the quasi analogue of Appleby–Simone–McGinley Thm 6.7, and the exact defect formula in (c). It's a jewel, not a paper.

## Step 0: owner check

Greps run first-hand over `papers/`: 2309.14887 (CMRR1), 2610.33772 (ASM), KT NCSF IV, KT NCSF V and KT FPSAC'97. Patterns: dual equivalence, Schur-Weyl, linear extension, ribbon, standardi. The texts of MG 2302.07694, BCDS 2503.14782 and CMRR2 2309.14898 are not in `papers/`, so those were not grepped. That gap is a footnote, not a gate.

- **ASM 2610.33772 Thm 6.6/6.7** (read first-hand, txt l.2253–2330). This is the CRYSTAL version: [n]^{⊗k} ≅ ⊔_λ B_λ × S^λ, where the S-side edges are elementary Knuth moves. The paper has no quasi-crystal analogue, and its §6 asks no open question about one.
- **KT FPSAC'97 Thm 3.2 and NCSF V §7** (read first-hand). The quasi-ribbon RS correspondence w ↦ (Q,R) is a bijection, with Q a quasi-ribbon tableau and R a standard ribbon tableau of the same shape. This is the *set-level* content of (b). NCSF V Prop 7.1 builds the simple U_0(gl_N)-modules D_I = V^{⊗n}η_I (with η_I a Norton element of H_n(0)) and shows that f_i acts on the basis d_w (w ∈ QR(I)) by the quasi-crystal operator (eq. (18)). This is the module-level q=0 Schur–Weyl.
- **CMRR1 2309.14887 §2.5–2.6** (l.465–482, 570–578). Components of Γ(hypo) are the shapes' quasi-ribbon readings, and F_α is the isoclass. There are no S_k-side moves.
- **Owner verdict.** The decomposition is owned (KT/Novelli + CM17). I found nothing that states the "swap positions with non-consecutive std labels ⇒ quasi-crystal isomorphism" graph theorem or the (c) defect formula, but both are so cheap that folklore risk is high. I record this as **"ours in this packaging, likely folklore"**.

## Setup (convention of `expository/2026-11-05-quasicrystals-q0-QSym.tex`)

A word w ∈ [n]^k has an *i-inversion* if it contains a subsequence (i+1)…i. If it has none, ë_i turns the leftmost i+1 into i and f̈_i turns the rightmost i into i+1. If it has one, both are ⊥.

std(w) ∈ S_k labels letters smallest-first and equal letters left to right. σ = std w is read as a word, so σ_p is the label at position p. iDes σ = {k : k+1 appears left of k}. C_σ = {w : std w = σ}.

**Gessel's lemma (expository Lemma 6.2).** Fix σ with D = iDes σ. Then w ↦ b(w), where b_k = w_{σ^{-1}(k)} (the letter carrying label k), is a bijection C_σ → P_D(n) = {b_1 ≤ … ≤ b_k in [n] : b_m < b_{m+1} ∀ m ∈ D}. Its inverse puts b_m at position σ^{-1}(m).

**Theorem B, step (1) (expository).** In b-coordinates the quasi-crystal structure on C_σ depends only on (D, b). Let l = #{m : b_m ≤ i}. Then:
- w is i-alive ⟺ (w has no i+1) or l ∉ D or b_l ≠ i;
- when alive, φ_i = #{m : b_m = i}, ε_i = #{m : b_m = i+1}, ë_i lowers b_{l+1} by one, and f̈_i raises b_l by one;
- wt = content of b.

The components are exactly the nonempty C_σ, and C_σ ≅ P_D(n) =: Q_α, where α is the composition with partial-sum set D.

## (a) Non-consecutive swaps are quasi-crystal isomorphisms

**Proposition A.** Let w ∈ C_σ and 1 ≤ j < k with |σ_j − σ_{j+1}| ≥ 2. Put τ = σ s_j, the word σ with positions j and j+1 swapped. Then:
1. iDes τ = iDes σ.
2. s_j w ∈ C_τ and b(s_j w) = b(w).
3. Hence s_j : C_σ → C_τ is the identity map of P_D(n) in b-coordinates. So it is a quasi-crystal isomorphism, and for every i and every x ∈ C_σ:
   s_j f̈_i x = f̈_i s_j x and s_j ë_i x = ë_i s_j x (both sides ⊥ simultaneously), with ε_i, φ_i and wt preserved.

*Proof.*
1. Swapping the adjacent entries a = σ_j and b = σ_{j+1} changes the relative position of a pair {m, m+1} only if {m, m+1} = {a, b}. That is excluded because |a − b| ≥ 2.
2. By (1) both C_σ and C_τ have b-image P_D(n). Apply the inverse Gessel map for τ to b(w). It puts b_m at position τ^{-1}(m) = s_j(σ^{-1}(m)), so the resulting word u satisfies u_{s_j(p)} = w_p, i.e. u = s_j w. Gessel's lemma for τ says u ∈ C_τ with b(u) = b(w).
3. By Theorem B step (1), every datum of the quasi-crystal at a point of C_σ (definedness, value in b-coordinates, ε, φ, wt) is a function of (D, b) alone. Both are shared. ∎

Note that we never had to argue about equal letters. When the labels are non-consecutive, the letters w_j and w_{j+1} are automatically distinct, because adjacent equal letters carry consecutive labels.

**Corollary A′ (path independence).** For σ and τ with the same iDes, define Φ_{τσ} : C_σ → C_τ to be "same b". Then:
- Φ_{τσ} is a quasi-crystal isomorphism;
- Φ_{ρτ}Φ_{τσ} = Φ_{ρσ};
- any chain of s_j-moves from σ to τ composes to Φ_{τσ}.

So the S_k side acts by a *canonical* transitive system of isomorphisms, with no monodromy. That is stronger than ASM's crystal statement, where the Cartesian product structure is proved via plactic positions.

## (b) The quasi Schur–Weyl decomposition

Let Z_D be the ribbon (zigzag) poset on [k] with p ⋖ p+1 for p ∉ D and p+1 ⋖ p for p ∈ D. Its linear extensions λ : Z_D → [k] are the standard ribbon tableaux of shape α.

**Lemma L1.** σ ↦ λ = σ^{-1} is a bijection {σ ∈ S_k : iDes σ = D} → LinExt(Z_D). Under it, σ ↦ σ s_j corresponds to λ ↦ s_j λ (swap the labels j and j+1). The swap condition |σ_j − σ_{j+1}| ≥ 2 says that the elements λ^{-1}(j) and λ^{-1}(j+1) are non-adjacent, and for consecutive labels that is equivalent to *incomparable* in Z_D.

*Proof.* m ∈ D ⟺ σ^{-1}(m+1) < σ^{-1}(m), which is exactly the order-preservation of λ on the cover between m and m+1. For the swap condition: adjacent implies comparable, since it is a cover. Conversely, if x ≠ y are non-adjacent and comparable, the chain between them passes through an intermediate element z with λ(z) strictly between λ(x) and λ(y). That is impossible when the labels are j and j+1. ∎

**Lemma L2 (classical).** For any finite poset P, LinExt(P) is connected under "swap the consecutive labels j, j+1 when they sit on incomparable elements".

*Proof.* Take λ, μ ∈ LinExt(P). Let x = μ^{-1}(1), so x is minimal, and let m = λ(x). If m > 1, let y = λ^{-1}(m−1). We have y ≮ x because x is minimal, and y ≯ x because λ(y) < λ(x). So y and x are incomparable and we may swap them, which lowers λ(x). Repeat until λ(x) = 1. Then induct on P ∖ {x}: the moves there, shifted up by 1, are legal moves in P. ∎

**Theorem Q67 (quasi Schur–Weyl).** Give [n]^k a graph structure G whose edges are the quasi-crystal edges (f̈_i) together with the swaps w — s_j w for |std(w)_j − std(w)_{j+1}| ≥ 2. Then w ↦ (b(w), std(w)^{-1}) is a graph isomorphism

  G ≅ ⊔_{α ⊨ k, ℓ(α) ≤ n} Q_α □ L_α.

Here Q_α = P_{D(α)}(n) is the quasi-crystal and L_α is the swap graph of Lemma L2 on LinExt(ribbon α). In particular [n]^{⊗k} ≅ ⊔_α Q_α × LinExt(ribbon α) as quasi-crystals, where the second factor is a set with trivial quasi-crystal structure.

*Proof.*
- **Bijectivity.** By Gessel's lemma for each σ, and because P_D(n) ≠ ∅ ⟺ ℓ(α) ≤ n.
- **Quasi-crystal edges change only b.** std is preserved (Theorem B step (1)), and they act on b as Q_α.
- **Swap edges change only σ.** Proposition A gives b fixed, and Lemma L1 identifies them with L_α edges.
- **Every L_α edge (and every Q_α edge) at every point is realised.** For L_α edges this is Proposition A applied to the word with the given b in C_σ.

Connectivity of each block follows from Theorem B (Q_α connected) and Lemma L2 (L_α connected). ∎

**Remark (hypoplactic, not dual-equivalence).** w and s_j w occupy the same b-position in components of the same type D. By Cain–Malheiro's characterisation, they are therefore *hypoplactically congruent*. [Recall-only: CM17, "same position in isomorphic components ⟺ ≡_hypo", not re-read this session.] So the S-side moves are hypoplactic moves. This matches ASM 6.7, where the S-side moves are Knuth (plactic) moves on words, which become dual-equivalence moves on recording objects. Our L_α is the ribbon analogue of Haiman's dual equivalence graph S^λ: any two consecutive-label swaps on incomparable elements are allowed, and no witness i±1 is needed. At q=0 the dual equivalence condition degenerates to "the two labels are not adjacent in the ribbon".

## (c) Sharpness and the exact defect against the 0-Hecke action

**Sharpness of the swap condition.** If |σ_j − σ_{j+1}| = 1, then τ = σ s_j has iDes τ = iDes σ △ {min(σ_j, σ_{j+1})}. Its source then has a different weight (Theorem B), so C_τ ≇ C_σ and s_j cannot be an isomorphism C_σ → C_τ.

Worse, s_j does not even map C_σ into a single component. Let l < l+1 be the labels at positions j, j+1. Words with b_l = b_{l+1} (equal letters) are *fixed* by s_j, while words with b_l < b_{l+1} are sent to C_τ. Both kinds exist in C_σ as soon as n ≥ ℓ(α)+1: start at the source and raise b_{l+1}.
- Smallest example: σ = 12, w = 11 ↦ 11, but 12 ↦ 21 ∈ C_{21}.
- Computation: 1602 of the 8362 consecutive cases fail (n ≤ 4, k ≤ 5), against 0 of 9414 non-consecutive ones.

**The KT 0-Hecke action.** NCSF IV l.331–336 gives the right action of T_j at q=0 on V^{⊗k}:

  e_w T_j = e_{s_j w} if w_j < w_{j+1};  0 if w_j = w_{j+1};  −e_w if w_j > w_{j+1}.

The U_0(gl_n) action (NCSF V p.19, l.917–925) is f_i e_w = Σ e_{w[p: i→i+1]}, summed over the positions p with w_p = i and no i+1 before p. Dually, e_i e_w sums over the i+1's with no later i. That e_i formula is my dual reading and was not quoted from KT, but it commutes with T_j by computation. NCSF V §7 (l.873) states that the U_0 action commutes with H_k(0).

Extend f̈_i and ë_i linearly by f̈_i e_w = e_{f̈_i w}, with ⊥ ↦ 0. Let

  A_i = span{e_w : w has no i-inversion},  B_i = span{e_w : w has an i-inversion},

and let p_i : V → A_i be the projection along B_i.

**Lemma C1 (f̈ is f modulo B_i).** f_i(B_i) ⊆ B_i and f_i ≡ f̈_i (mod B_i) on all of V. The same holds for e_i and ë_i.

*Proof.*
- If w ∈ A_i, its {i,i+1}-subword is i^a (i+1)^b and f_i sums over all a copies of i. Changing the last copy gives f̈_i w. Changing any earlier copy produces (i+1) before a later i, which lies in B_i.
- If w ∈ B_i, fix an inversion pair (i+1 at p, i at q > p). f_i only changes i's that have no earlier i+1, so it never changes the i at q, and the inversion survives. Also f̈_i w = 0 there.
- The e-version is the mirror argument: the inverting i+1 has a later i, so e_i never changes it. ∎

So f̈_i is *the action of f_i on the quotient V/B_i, written in the word basis*. That is the precise meaning of "f̈_i is the leading term of the U_0 action". This is also KT's mechanism in NCSF V eq. (18): there the non-quasi-ribbon terms die in D_I.

**Lemma C2.** T_j(B_i) ⊆ B_i. On A_i, T_j leaves A_i only through the case (w_j, w_{j+1}) = (i, i+1), and in that case e_w T_j = e_{s_j w} ∈ B_i.

*Proof.* A swap happens only at an ascent w_j < w_{j+1}. Moving two adjacent letters past each other changes the relative order of the pair at j, j+1 only. An inverting pair (i+1, i) at (j, j+1) is a descent, so it is never swapped. Hence inversions survive. On A_i, a swap creates an inversion only if it reverses an adjacent (i, i+1). The 0 and −e_w cases stay in A_i. ∎

**Theorem C (exact defect).** For every word w, every i and every j, writing x = f̈_i w:

  T_j f̈_i(e_w) − f̈_i T_j(e_w) = [x ≠ ⊥ and (x_j, x_{j+1}) = (i, i+1)] · e_{s_j x},

where operators are written on the left (T_j means "apply the KT T_j"). The same formula holds with ë_i and x = ë_i w.

*Proof.*
- Modulo B_i: f̈_i T_j e_w ≡ f_i T_j e_w (by C1 applied to T_j e_w) = T_j f_i e_w (KT commutation) ≡ T_j f̈_i e_w (by C1 and C2, since T_j preserves B_i).
- So the two sides agree mod B_i. Since f̈_i T_j e_w ∈ A_i, we get f̈_i T_j e_w = p_i T_j f̈_i e_w.
- The defect is therefore (1 − p_i) T_j e_x. By Lemma C2 it is e_{s_j x} exactly when (x_j, x_{j+1}) = (i, i+1), and 0 otherwise. ∎

**Corollary C′.** The defect is supported on consecutive std labels. In x = f̈_i w (inversion-free), the i at position j is the last i and the i+1 at j+1 is the first i+1, so they carry labels l and l+1. Since f̈ preserves std, std(w) has consecutive values at j, j+1. On non-consecutive positions, T_j commutes with f̈_i and ë_i. (This also follows from (a): the comparison type of w_j, w_{j+1} is the strict order of their labels, which is constant on the component, so T_j acts there as a fixed scalar multiple of id or of s_j.)

The clean slogan: **KT's H_k(0) commutes with U_0 (linear). The quasi-crystal is U_0 modulo the i-inverted words, and H_k(0) preserves the i-inverted words but not their complement. The leak is exactly one term, s_j f̈_i w, at an adjacent "i, i+1" — which is always a consecutive-label pair.**

## (d) K_0 shadow and Seed Q3

Taking characters in Theorem Q67 (ch [n]^k = (x_1+…+x_n)^k = F_1^k, ch Q_α = F_α):

  F_1^k = Σ_{α ⊨ k} #LinExt(ribbon α) · F_α = Σ_α β_k(D(α)) F_α,

where β_k(D) = #{τ ∈ S_k : Des τ = D} is the ribbon number. This is Gessel's/Stanley's expansion, now with both factors visible.

**Seed Q3 (Hopf-algebraic Schur–Weyl functor).** At q=0 the S_k side degenerates in two consistent ways:
1. **Combinatorially (Theorem Q67).** It becomes L_α, the linear-extension graph of the ribbon, i.e. the set of standard ribbon tableaux of shape α. Its cardinality β_k(D) is the multiplicity of Q_α.
2. **Algebraically (KT V §7).** D_α = V^{⊗k}η_I is cut out by Norton's element η_I. Norton's simple H_k(0)-modules are 1-dimensional and indexed by the same compositions α, so the S-side "multiplicity space" of Q_α cannot be the simple module, which has dimension 1 while β_k(D) can be larger. **[Recall-only, not proved here]**: β_k(D) is the dimension of Norton's indecomposable projective P_α (Norton 1979). So the combinatorial S-side L_α is a basis-level shadow of P_α, not of the simple module. This is exactly where the semisimple Schur–Weyl picture breaks.

So the "Schur–Weyl functor" at q=0 sends Q_α to (a basis of) the projective P_α. The quasi-crystal sees the simple top on the U_0 side and the projective on the H_k(0) side. This asymmetry is the Crown S split again (product vs coproduct), and it is a hunch for the dream, not a claim.

## Verification (`proofs/prove278/q67.py`, n ≤ 4, k ≤ 5, 0.5 s)

| check | cases | failures |
|---|---|---|
| (a) s_j vs f̈_i, ë_i at non-consecutive labels (definedness + value) | 9414 each | 0 |
| (a) control: same test at consecutive labels | 8362 each | 1602 each — **control breaks** |
| b(s_j w) = b(w), iDes preserved | 3402 | 0 |
| components = std classes | 12 (n,k) | 0 |
| L_α connected (all D, k ≤ 5) | 22 | 0 |
| KT T_j commutes with linear f_i / e_i | 17776 each | 0 |
| Theorem C defect formula exact, f and e | 17776 each | 0 |
| defect supported on consecutive labels | 17776 each | 0 |

## Gaps

1. KT commutation (U_0 linear ⟂ H_k(0)) is cited (NCSF V l.873, read first-hand) and computed, not re-proved. The e_i formula is my dual reading. If KT's e_i differs by a normalisation, Theorem C's e-half still holds for any e_i that satisfies C1 and commutes with T_j.
2. The hypoplactic remark rests on CM17's characterisation (recall-only).
3. The Norton P_α dimension statement in (d) is recall-only and explicitly not claimed.
4. The owner check did not cover the full texts of MG23, BCDS25 or CMRR2. The folklore risk is high and footnoted.
