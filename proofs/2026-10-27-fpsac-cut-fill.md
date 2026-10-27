# PROVE 260 — Fill the FPSAC 2027 cut (no new theorems)

Date 2026-10-27. WIP commit **bac1058** (work-in-progress, pushed). Nothing submitted (PROTOCOL §5).

## Problem
Turn `work-in-progress/papers/lg-og-fpsac-cut/main.tex` (45-TODO skeleton) into a complete ≤12 pp FPSAC2027
extended abstract (incl. bib, excl. AI declaration). Every statement must be proved from (G1)+(LS) (LG main line) or
explicitly cited (BR = Buch–Ravikumar 1005.2605; classical). No \cite in the abstract.

## Result: DONE
- 0 TODOs. 12 counted pages (body pp1–11, refs end on p12 at ~85% fill, so ~6 lines of slack). AI declaration
  pp13–14 (uncounted). latexmk exit 0, 0 undefined refs, 0 overfull hboxes, 1 overfull vbox (3.3pt, p2, already in the skeleton).
- 6 blue `\robin{...}` placeholders remain: authorship/presenter, affiliation, human acks, AI-decl wording,
  model list, human role. These are Robin's decisions and not mathematics.

## Structure as printed
1 Intro: Thm 1.1 (SR_LG a/b/c), Ex 1.2, Thm 1.3 (OG; classical, cited [LS86, Seshadri, GL96, Hibi87] + Stanley,
  no novelty), Thm 1.4 window, Thm 1.5 HZ, Cor 1.6; "Why the factor two"; literature, with novelty claimed only for
  1.1(b),(c) and 1.5 (Q30 dropped from the novelty claims).
2 Prelims: shifted diagrams + r(κ) inline; Lemma 2.1 (Npos) with proof; reciprocity; (G1), (LS) (Lit94 locator
  footnote kept); Lemma 2.2 polynomial extension with proof; Lemma 2.3 anchor with proof.
3 LS proof: Lemma 3.1 bonds (sketch), Lemma 3.2 LS parity (proof), Prop 3.3 model (proof), proof of Thm 1.1.
4 Recursion: Lemma 4.1 (V(P,D)), Lemma 4.2 peel (proof), Prop 4.3 (★) LS-only (proof by polynomiality).
  Remark 4.4: the Pieri coefficients. c_ρ=(−1)^{|θ|−1}V(θ) is cited as the p=1 case of [BR12, Cor 5.6] via
  Cor 5.4/Thm 5.5, with the (3,2) example, primes = odd values, a warning that the H_ρ are dependent at κ=(3,1),
  [LS12] (Lenart–Shimozono, 1203.3237) as owner in principle, and the line "we plan a T-equivariant BR-free proof in
  the full version". Remark 4.5: OG K-sketch citing [BR12, Cor 4.4, Lemma 4.5].
5 Window: proof from counts; Remark 5.1 inductive argument phrased with V and Lemma 4.1 (LG only), with the
  (3,2) worked case s_3=1, s_4=13.
6 Half-integers: Prop 6.1 bridge (sketch, with the ∧U reading folded in), Thm 6.2 (proof), Lemma 6.3 layers,
  Cor 6.4 row formula, proof of Thm 1.5 (fibre + shift + one-row, compressed), proof of Cor 1.6, Remark 6.5
  (Thm Z, support only), Remark 6.6 (T, statement only).
7 Table 1 (LG(3,6) values), reading of the entries, checks sentence, 2 questions. AI declaration: three lists
  (LS-proved / BR-cited / classical-cited), plus Clio's review status per result.

Dropped to fit: ex:ls-small, the Canonical-modules question, and rem:wedgeU (folded into the bridge sketch).
The half-step remark was cut to 3 lines.

## Verification (PDF is the claim)
`work-in-progress/scripts/prove260/pdf_check.py` re-implements the following from the printed statements, with a
fresh type-C Demazure engine (not the prove25x engines):
- every Table 1 entry (35 integer and 35 half-integer values);
- Thm 1.1(b) at j≤5;
- Prop 6.1 bridge (D_w F_a at y=1) against the interpolated polynomial;
- Thm 6.2, Cor 6.4, Thm 1.5(i)(ii)(iii) incl. integrality, and the window;
- Ex 1.2 counts [0,0,1,5];
- the V-values of Remark 4.4 and the s_3=1, s_4=13 recursion of Remark 5.1;
- (★) as a polynomial identity for all κ at m=3;
- the hyperplane identity (4.2) with the printed c_ρ, for all κ at m=3,4. This is consistency only: (4.2) cannot
  separate the c_ρ because the H_ρ are dependent, as the remark itself says.
**0 failures.**

## Gaps / honest flags
- The Remark 5.1 and Remark 6.5 arguments use (★), which is itself proved from Thm 1.1(b). They show what structure
  forces the window, not that it holds independently. The text now says "forced by the shape of (★)".
- The dictionary X_κ=X^{κ^∨} (needed only for Remarks 4.4/4.5) is stated without proof in the cut. The AI
  declaration says the agent proved it (T-fixed point + dimension count), and the proof is in the long draft (Lemma 2.4).
- BR bib entry: refs.bib says J. Reine Angew. Math. 668 (2012) 109–132, but sources.json notes say "ANT 9(3) 2015".
  The two disagree. **Not resolved** (no browsing this session). Check before submission.
- sources.json schema: the trustcheck validator reports 49 problems, all in the sources index (extraction values
  'pdf'/'locator', missing 'read'). They predate this session. The two structural errors on q488-degree-identity
  (missing children, bad file path) were fixed.

## Registry
q488-converse.json (both copies, md5 f3e06476…): HZ node sources 1005.2605 removed (its route is LS-only);
integer-strict-reciprocity now depends on q488-oc-SR_LG-via-LS-paths, with a note; degree-identity node structure
fixed. No grade changes: this was a writing session, not a math session.

## Next (Wake 261)
Email Clio the PDF (raw GitHub URL at bac1058) with a cover note, cc Robin: "cut ready for review; 6 Robin fields".
Ask Robin for the venue yes/no and the authorship fields. Resolve the BR journal citation.

## Session 260b (same day, second PROVE slot): cold referee read — WIP **6dbecb8** (pushed)
PROVE.md had not been rotated, so the slot went to a line-by-line sober re-derivation of every printed proof in the cut
(Lemmas 2.1, 2.2, 2.3, 3.1–3.2, Prop 3.3, Thm 1.1, Lemmas 4.1–4.2, Prop 4.3, Rem 4.4 sign translation + (3,2) example, Rem 4.5
OG recursion + anchor, Rem 5.1 incl. the T-antidiagonal argument and s_3/s_4 of (3,2), Prop 6.1 conjugation identities
D_m(e^{-ω/2}g)=e^{-ω/2}(1+y_m)^{-1}D^B_m g and D'_m(Φg)=ΦD_m g by hand, Thm 6.2 reduced word + kill chain, Lemma 6.3 a/b/c,
Cor 6.4 + s_{5/2}(3)=7/8, the HZ fibre/shift proof incl. the iterate count Ψ_{M+1}(0)=(−½)^{n−M−1} and the u≥2 bookkeeping,
Cor 1.6, Rem 6.5 edge terms −1/8,+1/4, intro LG(2,4)/OG(2,5) example). **No mathematical error found.** Three precision fixes:
1. Prop 3.3 forward map used a_s without defining it → "with a_s=1".
2. §6: "(G1) turns this into χ(X_κ,∧U⊗O(−a))" overclaimed — (G1) is stated for dominant weights only; now "(G1) for χ at all
   weights". The identity is still flagged "we do not use it".
3. §7: "H(−7/2)=2^{-3}N_{(2,1)}(3)" for (3,2,1) read as the equality case of Thm 1.5(iii), but 2a=6>κ_1. It is true
   numerically (the unique g gives Φ=1/8 by hand) → now "attains the bound of Theorem 1.5(iii)".
Wording trims (Lemma 6.3(c) proof, Cor 1.6 proof) kept the layout identical: 12 counted pp, AI decl pp13–14, 0 undefined refs,
0 overfull hbox (1 pre-existing 3.3pt vbox, counted with grep -a). pdf_check.py rerun: 0 failures.
Minor note, not changed: in the HZ proof, "u_β≥β+1 guarantees" u≥2 for existing row-1 boxes; for absent boxes u=M'+1≥2 holds
because the iteration stops at M'≥1. Correct as printed ("valid while M≥1 and u≥2"), just terse.
BR journal: no local file cites the journal (only the arXiv v1 LaTeX is on disk). Agent recall agrees with refs.bib
(J. Reine Angew. Math. 668 (2012) 109–132); the sources.json "ANT 9(3) 2015" note is the outlier. Still to confirm online at Wake.
