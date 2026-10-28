# PROVE 261: Theorem E (BR-free Q30) folded into the long draft

Date 2026-10-28. Paper: `work-in-progress/papers/lg-og-negative-degree/main.tex` §4.5 (`ssec:equivariant`),
WIP d3062ec (32 pp, 0 overfull by `grep -a -c Overfull main.log`, 0 undefined refs). `writing/` copy synced (diff empty).
FPSAC cut untouched (frozen at 6dbecb8).

## Problem
Cut Rem 4.4 promises a T-equivariant proof of c_ρ = (−1)^{|θ|−1}V(θ) (old Thm 4.8 = long-draft Thm 4.8 / Q30) that avoids BR.
Deliver it in the long draft, make (KT) explicit, add the LS12 remark, and purge any "needs BR" text.

## What is now printed (long draft numbering)
- Lemma 4.14 Telescoping (= PROVE 259 Lemma 0), with heights ⟨·,ȟ⟩, ȟ=(m,…,1).
- Lemma 4.15 Weighted LS-parity model (= Thm A).
- Exponential-polynomial paragraph + Prop 4.16 Strict characters (= Thm B; Stanley cone reciprocity [Stanley74], [BeckRobins, Ch. 4]).
- Prop 4.17 Weighted peel, eq (4), all i ∈ Z (= Thm C (†)), with the m=3 example P_{(2),(1)}.
- Lemma 4.18 Independence (= Lemma D), plus a sentence on why it collapses at e^μ=1.
- (KT), as a stated input: the [O_ρ]_T span K_T(X) over R(T), and the [O_ρ] are a Z-basis of K(X). Cited to Thomason 1987
  (localization + homotopy invariance). A footnote says the theorem numbers were not checked first-hand.
  **Improvement over PROVE 259:** only spanning of all of K_T(X) is needed. Lemma 4.18 then *forces* A_{κρ}=0 for ρ⊄κ,
  so the image-of-K^T_0(X_κ) form is no longer used. The Z-basis half was already implicit in Lemma 4.1 (c_ρ well defined);
  now it is explicit.
- Thm 4.19 Equivariant Chevalley rule for L^{−1} (= Thm E): A_{κρ} = (−1)^{|θ|} conj(P_{κρ}), unique; forgetting T gives Thm 4.8.
  The Thm 4.8 proof now opens "We give the proof from [BR12]. A proof without [BR12] is Theorem 4.19 below."
- Rem 4.20 LS12 [Cor 3.4, (3.6)] dictionary (pullback to G/B, G/B⁻≅G/B via w₀=−1, antidominant rule, matching not in LS12,
  m≤4 machine agreement, no-w₀ control 36 mismatches). Bib entry LS12 added (arXiv:1203.3237, title as on arXiv).
- Rem 4.21 Computer checks.
- New Question (Down-lifts and V-maps) = Q48, in §8.

## Stale text purged or updated
- §4.4 closing paragraph ("It does not recover Theorem 4.8 …") now reads "By itself it does not recover …. The torus repairs this …" and points to §4.5.
- §4 intro, Intro Method paragraph, Lit section (LS12 sentence), Outline, Abstract (one sentence), and the "second proof uses (BR)" paragraph (parenthetical: with Thm 4.19 instead of BR it no longer avoids (LS)).
- Grep for "Buch", "BR", "Cor 5.6", "Thm 4.8", and "Q30" after the edits: the remaining BR mentions are the BR-first proof (§4.2–4.3, credited),
  the OG case (Lemma 4.22, which still uses BR [Cor 4.4, Lemma 4.5], correctly), and the Higher Pieri question. No sentence
  claims that Q30 *needs* BR.

## Verification (PDF is the claim)
`work-in-progress/scripts/prove261/pdfcheck.py` (output `out_pdfcheck.txt`) is a fresh Demazure engine written from the printed text
(box offset d ↦ α_{m−d}, diagonal ↦ α_m). It does not use the prove259 engine.
- m=2,3: printed Lemma 4.15 (j≤3), Prop 4.16 (j≤3), and eq (4) (i∈[−2,3]): 0 failures.
- Lemma 4.18 at m=3: rank 8/8 at a random torus point, rank 7 at e=1 (the dependence it fixes).
- Thm 4.19 at e=1: c_{(3,2)} = {(3,1):2, (2,1):−1, (3):−1, (2):1, (1):0, ∅:0}, matching printed Example 4.10; eq (1) holds for j∈[−3,3], all κ; P_{κκ}=e^{−v_κ}.
- Printed example P_{(2),(1)} = e^{−ε1+ε2−ε3}+e^{−ε1}: matches.
- Negative control (offset-1 β → ε_{m−1}+ε_m): 18/6/9 failures. The control breaks the claim.
- m=4 brute force timed out at 500 s and was not run. m≤5 coverage comes from the PROVE 259 engine (Rem 4.21).

## Cold read (new section only, from pdftotext)
I made three fixes: (KT) now carries the K(X)-basis half; the "with it the second proof" sentence was replaced, because Prop 4.16 at e=1
*is* Thm 1.1(b), so Thm 4.19's real output is the Pieri coefficients; and the basis citation was redirected to (KT). The Lemma 4.13
bijection weights, the ρ=∅ case (ch_∅(j)=e^{jω}, consistent), the conjugation bookkeeping in Φ, and the cone substitutions under z→z^{−1} were rechecked
by hand. No further issues.

## Gaps
- (KT) has no first-hand locator (footnote). Its grade stays "proved mod (KT)".
- Stanley cone reciprocity is cited by chapter ([BeckRobins, Ch. 4]) and [Stanley74], not by theorem number.
