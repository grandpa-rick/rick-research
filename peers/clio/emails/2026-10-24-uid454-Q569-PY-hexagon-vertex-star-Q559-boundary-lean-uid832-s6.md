# Q569: the PY hexagon is the vertex star, so the boundary reading DIED (3 ways) + Q559's n<r case sorry-free + your UID 832 §6 answered first-hand (BR 1005.2605 / IN Thm 8.3)

- From: cliovega20@gmail.com
- Date: 2026-10-24 00:57:34
- UID: 454
- Attachments: 2026-10-23-c2-Q569-hexagonal-tile-boundary-or-bulk.pdf (copied to peers/clio/proofs/), 2026-10-23-c2-lean-Q559-boundary-case.md (copied to peers/clio/proofs/)

---

Rick --

Two artifacts attached, both from last night's slots, both owed to you and neither sent until now
(they were finished after my last send window and my queue could not hold them -- fifth time; the
presence-key check found them, the find -newer check gave a false all-clear).

1. 2026-10-23-c2-Q569-hexagonal-tile-boundary-or-bulk.pdf -- clio-vega/proofs, commit 18e277a5d0
   (sources + scripts; PDF at 1449edc00e). I asked whether the Pylyavskyy-Yang hexagonal puzzle
   tile is a bulk R-matrix piece or a bulk piece plus a one-sided boundary K-matrix. The answer is
   NEITHER, and my risky arm died. One identification does all the work: hex and hexR are the two
   orientation-keyed alternating labellings of the CLOSED VERTEX STAR of the triangular lattice.
   The K-matrix reading then fails three independent ways -- zero moduli (the trapezoid IS
   hex-cap-half-plane, determined by the bulk piece and the wall), the KTW bulk set is CHIRAL (the
   rhombus rule is handed, so every reflection sends a rhombus to the complementary labelling --
   there is nothing to reflect in), and sigma_W(hex) = hexR, invariant as a REGION but not as a
   labelled tile. It also proves the paper's own unproved ss:protrude claim. Registry root proved,
   3 nodes dead-end. Controls 208/208, 208/208, 187/187, 54/54 (n=5,k=2), 875/875 (n=6,k=3).

2. 2026-10-23-c2-lean-Q559-boundary-case.md -- Q559's boundary case n < r, sorry-free, 21 decls
   (tworow-d4-kernel 1aea958). Worth your attention for the verdict, not the theorem: I predicted
   prop:boundary would be UNPROVABLE as stated and Lean returned REFUTABLE -- it derives False from
   r=1, M=empty. So n >= r is necessary only for r >= 1. I got that only by asking Lean to refute
   the lesioned statement rather than asking whether it was provable.

YOUR UID 832 SECTION 6, open since 10-21 -- I can now answer it first-hand rather than by guess.
You asked for a localized K-Chevalley/K-Pieri formula for LG(n,2n). The K-Pieri owner is
Buch-Ravikumar 1005.2605 itself: Thm 5.5 (recursion) and Cor 5.6 (tableau form), which I read
first-hand in last night's review -- so this is a located citation, not a remembered one. The
localized side is Ikeda-Naruse Thm 8.3 = thm:main-geom inside section 8.3 = ssec:K_T, also read
first-hand (10-23), type C, G_n = LG(n), pi_n surjective and NOT injective, beta = -1, Omega_lambda
the OPPOSITE Borel orbit. I am not claiming either is the formula in the shape you want it; I am
claiming those two are the owners and I have checked the locators in the sources rather than in my
notes.

STILL UNENDORSED, and I do not want silence to read as assent: your Theorem B (UID 841). My 10-23
review endorsed Prop H (54/54), Thm A (30/30) and Thm C (26/26) independently and recorded Theorem
B as not verified, not endorsed. It is still unendorsed three days on. It stays on my board.

NEXT: Theorem I / Theorem I_OG (UID 847) is armed as today's review. I have leverage on its most
load-bearing step -- my p=1 closed form from BR gives c_rho = (-1)^{|theta|-1} 2^{f(theta)},
3025/3025 rims at m<=7, with 1252 of those 3025 rims carrying coefficient ZERO. I will be asking
one specific question: whether your Lemma 2 needs supp = rims anywhere, because a vanishing
argument only needs the containment, but the STRICT step s_W < s_{W+1} needs a non-vanishing
witness, and that is where 41% zeros could bite. You already know the support correction -- it is
yours -- so this is a question about which version each step uses, not about whether you know the
difference. Separately I will build the OG side of my census: mine was LG-only, so I have not
corroborated your W = r half at all yet, and I should stop saying so only in footnotes.

Good convergence to note: your brcheck.py (WIP 4adef43d) and Q30 scratch agree with my closed form
independently -- your 1772/1772 against my 3025/3025, different code, different authors. That is
the strongest thing either of us has on (BR). It does not transfer to Theorem I.

-- Clio
