# Roots of order polynomials Ω(P,t) — literature + checks (2026-10-22, lit agent for Rick)

Convention: Ω(P,m) = #order-preserving maps P → [m]; Ehrhart of order polytope i(n) = Ω(P,n+1).
r = #elements of a longest chain. Forced zeros: Ω(P,0)=Ω(P,−1)=…=Ω(P,−(r−1))=0 (reciprocity).
Question: do all roots lie in −(r−1) ≤ Re t ≤ 0 ?

## Verdict: (ii)-ish / effectively FALSE in general — a known explicit order polytope kills it.
No paper states the strip as a theorem or conjecture for order polynomials (searched web, arXiv API,
S2 citation trails of Golyshev/Manivel). But the strip is FALSE for general (even graded = Gorenstein) P,
by an example already in the literature (not phrased as a strip counterexample):

### BDDPS math/0402148 [NEW], proof of Theorem 1.3 (verbatim)
> "Given a positive integer d, consider the convex polytope Pd defined by the facet inequalities:
> 0 ≤ x0 ≤ xk ≤ 1 for 1 ≤ k ≤ d − 1. Pd is an order polytope in the sense of [20] and thus it has 0/1
> vertices. We claim that the Ehrhart polynomial of Pd is given by iPd(n) = (Bd(n + 2) − Bd(0))/d where
> Bd(x) is the d-th Bernoulli polynomial. ... the results of [24] imply that the largest real zero of Bd(n)
> is asymptotically d/(2πe). Therefore, as stated, as the degree d grows, the Ehrhart polynomial of Pd
> has larger and larger real roots."

Poset = claw (one minimum covered by d−1 maxima) = Stanley EC1 2nd ed. Exercise 3.164 (per Ferroni–Higashitani
2307.10852 [NEW], proof of Thm 4.6: "These posets were described by Stanley in [Sta12, Exercise 3.164] and
further studied by Liu and Tsuchiya in [LT19]" = 1806.08403 [KNOWN]). It is graded (r=2), so its Hibi ring is
Gorenstein. Ferroni–Higashitani Thm 4.14: positive real Ehrhart roots r_i with |r_i − i| < ε, s ≈ d/(2πe) of them.

### My computation (sympy/mpmath, /tmp/claw.py, /tmp/op2.py)
Claw with p elements (r=2, strip should be [−1,0]); roots symmetric about −1/2 (Gorenstein):
- p=2,3,4: OK (Re range [−1,0]).
- p=5: Re range [−1.2638, 0.2638] — VIOLATES. Smallest claw counterexample: p=5 (1 min, 4 max).
- p=6: [−1.366,0.366]; p=10: [−1.618,0.618]; p=30: real root 1.775.
- First claw with a root Re t ≥ 1 (= violates Golyshev CS after rescaling, see below): p=17 (max Re 1.0634).

Young-diagram posets (Grassmannian Schubert / minuscule type A) and shifted-diagram posets (spinor variety
Schubert): ALL partitions of n ≤ 11 checked (≈230 shapes): every root in [−(r−1),0]; the extremes are the forced
integer zeros; most shapes are real-rooted, a few have one nonreal pair strictly inside
(e.g. young [3,3,2], shifted [4,3,1], young [5,3,2], [4,4,2], [3,3,2,2], shifted [5,4,1]). No violation.
So the strip may be TRUE for d-complete / minuscule posets — that version is NOT found in literature (open/not found).
Note: claw (one element covered by ≥4 elements) is not a Young/shifted diagram poset — it's outside the Schubert world.

## Translation to Golyshev normalization (0903.2076 [KNOWN])
> "(CS) We say that X satisfies the canonical strip hypothesis if all roots zi of H(z) are in the canonical strip
> −1 < Re z < 0. (NCS) ... narrowed canonical strip −1 + 1/(dim X + 1) ≤ Re z ≤ −1/(dim X + 1).
> (CL) ... all roots zi are on the vertical line Re z = −1/2."
Gorenstein Hibi toric variety of pure P: Fano index r+1 (Miura 1301.7632 [NEW] Prop 2.8(1): "X(w) is Gorenstein if and
only if Pw is pure. In this case X(w) is a Fano variety of index hPw"; check OG(2,5)=P^3, r=3, index 4). So
H_{−K}(z) = Ω(P,(r+1)z+1); forced zeros ↦ z = −j/(r+1), j=1..r (Kodaira-forced). The Ω-strip [−(r−1),0] ⇔
roots in [−r/(r+1), −1/(r+1)] — STRONGER than NCS (dim = |P| ≥ r). This is Manivel's "refined" form.
Manivel 0904.2470 [KNOWN]: "a refined version of Golyshev's canonical strip hypothesis does hold for the Hilbert
polynomials of complete intersections in rational homogeneous spaces." Claw shows Gorenstein *Hibi toric* (singular,
terminal) varieties violate the refined strip at p=5 and even CS at p=17.
Citers of Golyshev/Manivel (S2): none apply it to Hibi rings/toric degenerations/Schubert varieties. Belmans–Galkin–
Mukhopadhyay 1806.07648 [KNOWN] = first smooth Fano violations (moduli of rank-2 bundles).

## General Ehrhart root-location literature (for context)
- BDDPS math/0402148 [NEW] Conj 1.4: all roots satisfy −d ≤ Re α ≤ d−1. Thm 1.2: real roots in [−d, ⌊d/2⌋).
- Higashitani 1106.4633 [NEW] "Counterexamples of the conjecture on roots of Ehrhart polynomials" (kills Conj 1.4).
- Ohsugi–Shibata 1109.0791 [NEW]: smooth Fano (del Pezzo, cycle length 127) root with Re > dimension.
- Matsui–Higashitani–Nagazawa–Ohsugi–Hibi Conj 4.10 (Gorenstein Fano: −d/2 ≤ Re ≤ d/2−1); Higashitani 1112.5777 [NEW]
  verifies for d ≤ 5 / real roots; Hegedüs–Higashitani–Kasprzyk 1503.05739 [NEW]: half-strip holds dim ≤ 5,
  "We give an example of a 10-dimensional reflexive polytope which violates the half-strip condition".
- Hibi–Higashitani–Ohsugi 1001.4165 [NEW], Hegedüs–Kasprzyk 1004.3817 [NEW] (Golyshev CL for smooth dim ≤ 5, fails 6),
  Kölbl 2207.08011 [NEW], Hachimori–Higashitani–Yamada 2110.03579 [NEW], Pfeifle math/0610399 [NEW].
- Rodriguez-Villegas (Proc AMS 2002): h* roots on unit circle ⇒ Ehrhart roots on Re = −1/2.
- Order-polytope-specific: only h*-side results (Brändén γ-positivity for graded P, FH Thm 3.29; Stembridge
  counterexamples math/0408312 [NEW] context; Brenti Memoir Thm 7.6.5 log-concavity). No root-location theorem for Ω itself.

## (b) CORRECTION on the shifted / strict-partition identification (computed, /tmp/lgcheck.py)
Hibi ring of the lattice of strict partitions in the staircase (= J(shifted staircase)) has Hilbert function
= Ω(shifted staircase, k+1) = dim V_{SO(2n+1)}(kω_n) (SPIN rep, minuscule) — the SPINOR variety OG(n,2n+1) ≅ OG⁺(n+1,2n+2),
NOT LG(n,2n):
- n=2: LG Sp: [1,5,14,30,55]; spinor: [1,4,10,20,35]; Ω(k+1): [1,4,10,20,35]
- n=3: LG Sp: [1,14,84,330,1001]; spinor: [1,8,35,112,294]; Ω(k+1): [1,8,35,112,294]
LG is cominuscule but ω_n of C_n is NOT minuscule; its SMT uses admissible pairs (Lakshmibai–Musili–Seshadri / De Concini
symplectic tableaux), Hilbert function ≠ multichain count. W^P for C_n/P_n and B_n/P_n are the same distributive lattice;
the line bundle differs. Shifted plane-partition Ω for the full staircase has a product formula (Proctor) ⇒ integer roots.
Nothing found on roots of Hilbert polynomials of Schubert varieties in LG or OG.

## Citable SMT / Hibi sources
- Hibi, "Distributive lattices, affine semigroup rings and algebras with straightening laws", Adv. Stud. Pure Math. 11
  (1987) 93–109: Hibi ring is a normal ASL on D; Gorenstein iff P pure (cited as Miura Prop 2.15 ← [33]).
- Hilbert series via chains: Hibi–Watanabe, Hiroshima Math J 15 (1985) (Miura Prop 2.14 ← [35, Corollary of Lemma 5]):
  "The Poincaré series of the Hibi algebra AJ(P) has the following form: P(t) = Σ ci (t/(1 − t))^i, where c0 = 1 and
  ci is the number of chains of length i in J(P)". Equivalently h(k) = #multichains of length k in J(P) = Ω(P,k+1).
- Minuscule W^P is a distributive lattice: Proctor, "Interactions between combinatorics, Lie theory and algebraic geometry
  via the Bruhat orders" (thesis 1981), Prop V.2 (Miura Prop 2.3).
- SMT minuscule: Lakshmibai–Musili–Seshadri, Geometry of G/P III (quasi-minuscule), Proc. Indian Acad. Sci. 88 (1979)
  93–177; vanishing/surjectivity [48, Theorem 7.1] (Miura Thm 2.10). Standard monomials p_{τ1}…p_{τk}, w ≥ τ1 ≥ … ≥ τk
  in W^P, form a basis of H^0(X_w, L^k) (Seshadri G/P I for minuscule; Brion–Lakshmibai math/0111054 [NEW] intro (i)-(iii)
  for Grassmannian, Thm 1 general with LS-path index sets).
- Toric degeneration: Gonciulea–Lakshmibai, Transform. Groups 1 (1996) 215–248, Theorem 7.34 (as cited by Miura Thm 2.23):
  "The minuscule Schubert variety X(w) degenerates to the Hibi toric variety P∆(Pw) ... a flat family V → C such that
  Vt ≃ X(w) for all t ∈ C∗ and V0 ≃ P∆(Pw)." ⇒ Hilbert function of X_w = Ω(P_w, k+1). (Not first-hand checked in G–L.)
- Gorenstein criterion for minuscule Schubert: Perrin, Adv. Math 220 (2009) (Miura Prop 2.8).
