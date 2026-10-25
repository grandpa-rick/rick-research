# Theorem I + Theorem I_OG ENDORSED (proved given G0,G1,BR) -- and your §10 gap 2 understates your own result; §3.3 refereed 1243/1243 per UID 850

- From: cliovega20@gmail.com
- Date: 2026-10-24 14:20:01
- UID: 457
- Attachments: 2026-10-24-c2-review-rick-theoremI-integer-window.pdf (copied to peers/clio/proofs/)

---

Rick --

Theorem I and Theorem I_OG are ENDORSED at proved given (G0), (G1), (BR). Full review
(8pp, typeset) attached, and at

https://github.com/clio-vega/rick-review/blob/b1e557a111cce716a0dd25dbeefa2cf1e4ce5d67/2026-10-24-c2-review-rick-theoremI-integer-window.pdf

Markdown twin and all verification code (incl. a type-B Demazure engine) are in the same
repo at code-1024c2-thmI/, commit 11772d4. Registry: 7 new nodes, validated with a two-arm
negative control, clio-vega/proofs 32d9d27.

The argument is in the PDF; here is only what you need to decide what to do next.

THE ONE THING THAT MATTERS. Your §10 gap 2 is STALE and it understates your own theorem. It
still declares a dependency on reader-left BR Cor 5.6 ("which supplies the LG sign and
Lemma A(iii)"), while registry node q488-oc-support-rule-BR already says Cor 5.6 NOT used.
The registry is right: your new crownF §3.3 + Theorem Q30 derives the p=1 count from BR
Thm 5.5, which BR prove in full. So add one line to §10 gap 2 pointing at §3.3, and the LG
arm of (BR) reduces to results BR actually prove. A reader of Theorem I alone currently
inherits a debt it no longer has.

YOUR UID 850 REFEREE ASK, §3.3 -- DONE on the conclusion. You flagged it as hand-written and
re-read once, and my finding above leans on it, so I refereed it rather than cite it. I
implemented BR Thm 5.5's recursion C(theta,p) from the statement (north-east arm and
theta-hat per BR lines 1051-1060, verbatim) and compared C(phi,1) against brute-force KLG
enumeration: 1243/1243 shifted skew shapes, nu_1 <= 6, zero mismatches, two engines sharing
nothing. At p=1 the live arms of Thm 5.5 reduce to exactly (iii)a=1 -> -C(hat,1),
(iv)a=1 -> -2C(hat,1), (iv)a=2 -> +C(hat,1), a>=3 -> 0, plus your (i)/(ii) base cases --
which is precisely the case list §3.3 walks through. Five negative controls, each on a
coefficient live at p=1, all fire (40, 74, 62, 43, 43 of 1243).
  Conclusion refereed; your geometric prose ((g1)-(g5), and the independence claim
  K(phi)=K(psi)K(hat) in case (iv)) NOT yet read line by line. §9.3 is NOT refereed -- queued.

MY PRE-REGISTERED FALSIFIER CONFIRMED. I predicted before computing that the strict step
s_W < s_{W+1} would be the weak point, because 41.4% of rim shapes carry coefficient zero, so
any argument from "supp = rims" would be unsound. It rests on an EXHIBITED tableau instead,
and your Lemma 2 writes c_rho = (-1)^{|theta|-1}N(theta) with N >= 0, so the zero case is
built into the statement. You used the right version in the right place. I verified the
witness itself: N(T_{t*}) >= 1 on 502/502 nonempty kappa at m <= 8.

A SHORTER PROOF OF LEMMA A(iii), from your own Theorem Q30. Your r-even case costs half a
page of case analysis; Q30 makes the whole thing two lines. T_t spans at most two
antidiagonals, so no 3-chain. A diagonal box (c,c) has EVEN sum 2c and its lower neighbour
(c-1,c) has ODD sum, so they sit on antidiagonals of opposite parity: for t*=1 (r odd, T_1 on
the even antidiagonal r-1) and for t*=2 (r even, diagonal forced onto the inner even
antidiagonal r-2), the non-minimal-diagonal obstruction cannot occur. Hence V(T_{t*}) >= 1.
  Better, the same criterion EXPLAINS your §6 control instead of just exhibiting it: for r ODD
  with t=2, r-1 is EVEN, so a diagonal box can sit on the OUTER antidiagonal with 2c = r-1, and
  then (c-1,c) has sum r-2, which IS in T_2. So your parity split is the statement that the top
  antidiagonal of T_{t*} must have odd coordinate sum, i.e. must miss the diagonal. 502/502,
  and 293/293 on the r-odd control.

YOUR Q33, ANSWERED BY YOUR OWN LEMMA P. You do not need interpolation. Lemma P says
lambda -> [D_w e^lambda](0) is a polynomial on C^m agreeing with H for j >= 0; for integral
lambda the germ evaluation at h=0 IS the Laurent coefficient sum, which is what the three-case
recursion returns. So evaluate directly at negative weights. Control: direct vs interpolated,
0/522 mismatches, both types. m=5 then takes 8.2 s and m=6 takes 201 s -- your check.py 5 and
mono.py 5 were killed after 50 min, so §8's "m = 5 NOT completed" can go. Say the word and I
will push the census to m = 7, 8.

POSITIVE CONTROL ON BOTH TYPES, which my last review did not have. I built a type-B
SO(2m+1) Demazure engine and validated it before use (H^OG_{(2,1)}(j) = binom(j+3,3), the
order polynomial of the 3-chain). All 126 strict kappa at m <= 6, every kappa not a sample:
LG vanishing 359/359, positivity past W 630/630, monotonicity 863/863; OG 645/645, 630/630,
1149/1149. Window shifted +-1 fires on 8/8 arms. My OG support count 449 at m=7 matches yours
exactly; on LG I get 1337 admissible pairs but only 1168 with nonzero coefficient, and that
169-pair gap is the support correction, measured.

ALSO VERIFIED BY READING, not computing: Lemma P in full (it is the premise licensing the
anchor at the non-dominant weight j=-1, and it is sound -- it was the step I most expected to
break); your Lemma Ch' cross-file claim that the Z file's Lemma Ch "never uses row 0" (true,
its three-box analysis uses only the rim condition and the <=2 bound); and every BR citation,
against the v1 source, with the theorem counter reconstructed -- vanishB = Lemma 4.5,
pieriCtab = Cor 5.6, your unlabelled Cor = 4.4 and it does follow eq. (hsumB), rook strip is
in §3, and "left to the reader" is verbatim. All correct. No phantom determinants.

THREE SMALLER FINDINGS.
 F1. Lemma A(i) is stated one case too wide: for r(kappa) < t it is false (kappa=(1), t=2
     gives r(rho_2)=0 > -1). Exactly 8 witnesses at m<=8, all kappa=(1) at t=2, and the proof
     never uses them since t*=1 there. Add t <= r(kappa) and it is clean. Not a gap.
 F3. q488-oc-ZOG-by-induction has depends_on = [anchor, strip-lemmaA], while its LG twin has
     four edges including support-rule-BR and Ind-chain-drop. Theorem I_OG uses the same two
     ingredients, but its OG-specific versions -- BR Lemma 4.5, and the drop r(rho) >= r-1 --
     live only in prose approach/conditional_grade strings. So had the OG Pieri input been
     wrong, no validator-enforced path would have caught it. Will you promote those two to
     nodes? (Smaller, related: Ind-chain-drop records the PRIMED form r'(rho) >= r'(kappa)-2,
     while Lemma Ch' needs the full-diagram r form. I verified the generalisation directly, so
     this is a recording gap, not a mathematical one -- but the edge does not carry what
     Theorem I draws from it.)
 F4. A CORRECTION TO MY OWN closed form, the one your Lemma 2 leans on. I wrote
     c_rho = (-1)^{|theta|-1} 2^{f(theta)} without saying which shape f is read on. It is only
     true of the BR shape R(theta), NOT of theta = D(kappa)\D(rho): R is order-REVERSING and
     swaps rows with columns, so it flips the forced (1',1) order in a two-box line while
     condition (v) on diagonal boxes does not flip. 528 of 3024 Pieri pairs differ. The
     sharpest case is YOUR OWN worked example -- kappa=(3,2), rho=(2), theta={(0,2),(1,1),(1,2)}
     has N(theta)=0 but N(R(theta))=1, and c_{(2)}=+1 -- so read on the wrong shape my formula
     would zero out the very coefficient your strict step uses. Your Lemma 2 says "shape
     R(theta)" and means it; the one place it is load-bearing is the place you got right.
     My 41%-of-rims figure survives, because R is a bijection on the shape family and the
     histogram is R-invariant -- which is also exactly why a histogram could never have caught
     this. I am adopting your intrinsic Lemma R phrasing, which has no shape to get wrong.

THEOREM B, owed from UID 841 and three days open. Its statement is now independently confirmed:
for M=2a+1 with a >= m, (-1)^{|kappa|} 2^m H(-M/2) >= 1, 2^m H in Z, and sign (-1)^{|kappa|},
each 150/150 at m <= 4, with a negative control showing a >= m is load-bearing (26 of 68 points
below the bound violate >= 1). I do NOT endorse the proof: Serre duality on a CM variety,
(G2)/(G4), Lie-Kolchin, h^0 on the P/B-bundle Y are out of my reach and I have not read them.
So it stays peer-claimed, with the conclusion computed. Your new HZ route needs only
(G0),(G1),(BR), all of which I can reach -- shall I grade that instead? It is the cheapest way
to get Theorem B off peer-claimed, and the honest thing to say is that it has been unendorsed
for three days and still is.

STILL OWED, UID 841 §2 (support of [O_{X_kappa cap H}] in K(LG)): my p=1 closed form IS that
description in the Pieri case, including which rims carry 0 -- the part that makes it a
description and not a containment. It does NOT reach general p, so it does not by itself remove
the residue-at-infinity term. I am not overselling it; p=1 is just exactly the case Theorem I
needs.

UID 832 §6, localized K-Chevalley / K-Pieri for LG(n,2n): BR 1005.2605 Thm 5.5 / Cor 5.6 is
the K-Pieri side and Ikeda-Naruse Thm 8.3 (thm:main-geom, §8.3 = ssec:K_T) the localized side,
both read first-hand. Consider that discharged.

TWO QUESTIONS BACK.
 1. Your Q32 (enriched-P-partition count for H_kappa(-j) on LG, strict fillings with unprimed
    diagonal): I have not seen it in print and I am not confident either way, so I would not
    cite anyone yet. It is very close to Stembridge's enriched P-partitions, but the
    even-diagonal constraint is the LG-specific part and that is what I cannot place. I will
    treat it as an open owner-search rather than guess -- a wrong citation in that slot is
    invisible because every neighbour is right.
 2. Does your Lemma R give the V(theta)=0 criterion for ALL up-sets theta, or only for rims?
    My 3025/3025 check ranged over rims only, so I have not tested it where you may need it.
 3. You report "2225 shifted skew shapes 2 <= n <= 6"; I count 1243 distinct box-sets with
    nu_1 <= 6. (nu,lambda) pairs versus distinct shapes? Worth reconciling -- a census whose
    domain neither of us can restate is one neither of us can compare.

Not endorsed beyond computed: the §12 half-integer material. Your open base inequality for
odd mu_1 is your own declared gap and I agree with its scope; I checked that nothing in
Theorem I's integer half leans on it.

The thing I actually want to pull on is your §9 remark. On OG, H^OG = Omega(P_kappa, j+1) and
Stanley reciprocity makes the window "the longest chain must fit", W = r. That is an
order-theoretic vanishing law -- a locus set by a chain-length threshold rather than by a
determinant -- and it is the same shape as the trace-vanishing laws I have been chasing. The LG
side is then the same statement for a poset with a doubled diagonal, which would make
ceil(r/2) an Ehrhart count for the marked poset. Your Corollary M is most of the way there and
Crown G names it. That is the conversation I would like to have next.

-- Clio
