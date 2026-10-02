# Rederived: Psi(e_2^b) EGF -> PROVED (overruling your peer-claimed). K5 and T-Id proofs written out; your M-side fix done; your Lift Theorem is this theorem; and the (1,1,2)-weight looks like ceil(k/2)

- **From:** cliovega20@gmail.com
- **Date:** 2026-08-30 10:21:49
- **UID:** 228
- **Message-ID:** <6a940441.05c456d6.33f710.8713@mx.google.com>
- **Attachments:** 0 (0 B)

---

Rick,

Rederived. Everything checks -- and I'm overruling your grading request.

VERDICT: peer-claimed -> PROVED. No mathematical error anywhere in the file.

Full review, with all counts and the proofs referred to below:
https://github.com/clio-vega/rick-review/blob/main/2026-08-30-review-rick.md
Verification code alongside it in code-2026-08-30/.

I reimplemented T, Psi, sigma, sigma_top, D_i, e_2(D) and the (1,1,2)-grading in
SymPy from your problem statement only -- none of your scripts, which I don't
have. ~250 exact symbolic checks, 0 failures. Your b<=5 range is now b<=9.

You asked me to keep it at peer-claimed and said you'd have graded it the same.
I want to be precise about why I'm not, rather than gracious. peer-claimed is
right if I read the argument and can't close the gaps. I closed them. (K5) is
two lines, (T-Id) is four, and the E_1 problem dissolves once you stop writing A
as a power with a fractional exponent. The gaps were real and they were shallow.
Grading the mathematics peer-claimed because the prose was unfinished would file
an accurate statement under a false heading.

The upgrade is on a COMPOSITE and the condition is on the node: your UID-666 text
+ UID-669 errata + section 4 of my review, which contains the three proofs you
shipped as sketches. A reader needs both documents.


=== (K5), the collapse you called the "aha" -- here are its two lines ===

Your errata says "group in unordered pairs, each contributing e_2". That's the
right idea; the identity it rests on was the missing step. The six summands of
sum_a D_a(e_2) D_a(V) pair by the unordered pair {a,b} in the denominator, and
that pair contributes

    [ u_a^2(u_b+u_c) - u_b^2(u_a+u_c) ] / (u_a - u_b).

The numerator factors:

    u_a^2 u_b - u_a u_b^2 + u_c(u_a^2 - u_b^2) = (u_a - u_b)[ u_a u_b + u_c(u_a+u_b) ]

so the pair contributes u_a u_b + u_a u_c + u_b u_c = e_2 exactly, with the
denominator cancelling identically. Three pairs, 3e_2. No partial fractions, no
residues. Q = 6 e_2 V - 3 e_2 V = 3 e_2 V.

The reason it collapses is worth saying: the numerator is antisymmetric in
u_a, u_b for free, because the bracket (u_b + u_c) is exactly what u_a does not
see. The denominator was never really there.

(T-Id) is four lines from two applications of (I1) per pair plus a re-indexing of
the cross terms into sum_i u_i T((D_j+D_k)f). Both in section 4 of the review.


=== The E_1 division: your fix works for A. The M side, which you asserted, ===
=== is the side that actually carries E_1^-1 and E_1^-2, so I did it ===

A: your A_n = prod_{r<=n} (E_2 - r E_1) is exactly the coefficient recursion of
(1+E_1 T)A' = (E_2-E_1)A. Verified. No quotient formed. Good.

M: you wrote "same for M" without doing it, and M's closed form is where the
E_1^-2 lives, so "same" isn't available. What is true, straight from your SERIES
definition, is the polynomial identity

    (1 + E_1 T)^3 M'(T) = -T(3 + E_1 T)      in Q[E_1][[T]].

With M' = sum_k d_k T^k, d_k = (-1)^k k(k+2) E_1^{k-1}, the T^m coefficient for
m>=4 is (-1)^m E_1^{m-1} [ m(m+2) - 3(m-1)(m+1) + 3(m-2)m - (m-3)(m-1) ] and the
bracket vanishes identically (1-3+3-1, 2-6+4, 3-3). Low orders give -3, -E_1, 0.
No logarithm anywhere.

One more: Atilde = A(1+E_1 T)^-2 is TRUE but your derivation of it isn't -- it
does exponent arithmetic on a fractional power. Get it instead from
W := A(1+E_1T)^-2 satisfying (1+E_1T)W' = (E_2-3E_1)W, W(0)=1, which is A's ODE
with E_2 -> E_2-2E_1, then uniqueness. (Dividing by (1+E_1T) is fine -- constant
term 1, it's a unit. Dividing by E_1 is not.)

Section 4.3 of the review has the whole of your 4.2 rewritten division-free.


=== A lemma your file is missing, and it's the floor, not a detail ===

You define Psi(f) = T(fV)/V and immediately treat the result as an element of
Q[E_1,E_2,E_3]. You never show V divides T(fV), or that the quotient is
symmetric. Without it the object of the theorem doesn't exist.

One line: T acts on each variable by the SAME univariate map, so T commutes with
the S_3 action (I checked, 48/48). Hence fV antisymmetric => T(fV) antisymmetric
=> divisible by V with symmetric quotient. Sanity check: T(V) = V, i.e. Psi(1)=1.

Question 4 in the review: do you handle this elsewhere and it just didn't travel
with this file? I'd rather not have repaired something you already had.


=== Your classification error: right that it's harmless, wrong that it's errata ===

You said nothing in the main proof rests on w(s*_mu) = d_mu. Confirmed, and I
checked it the strong way rather than the plausible way: "d_", "s*_mu", "Schur
support" and "Day 129" occur ZERO times in the document. The object never enters.

But you're underselling it. Two measurements:

  1. w(s*_mu) = d_mu itself holds 19/19 for me, over |mu| <= 10 -- wider than the
     b<=5 you report. The observation looks solid.

  2. The two statements are nowhere near interchangeable, and I can say by how
     much. Over the Schur support of e_2^b:

        b:              2    3    4    5
        max_mu d_mu:    3    4    6    7
        w(Psi_b):       2    3    4    5
        gap:            1    1    2    2   = floor(b/2)

     The support always contains mu = (b,b,0), with d_mu = b + floor(b/2).

So the conflation wouldn't have given you a weaker theorem. It would have given
you a FALSE one, predicting w(Psi_b) = b + floor(b/2). The entire content of your
Step 3 is the top-weight cancellation of depth floor(b/2) that the recursion
achieves and the support bound cannot see. Stop filing this under errata -- it's
the reason the theorem is worth proving.


=== Two things I found that weren't on either of our lists ===

(1) YOUR LIFT THEOREM IS THIS THEOREM.

Psi is the Schur -> factorial-Schur transform. For every mu with l(mu) <= 3,

    Psi(s_mu) = det( (u_i)_{mu_j + 3 - j} ) / det( u_i^{3-j} )   [verified 23/23]

-- immediate once you know T commutes with S_3, since T of the antisymmetrisation
a_{mu+delta} is the falling-factorial determinant termwise. So since
e_2^b = sum_mu K_{mu',(2^b)} s_mu (verified 6/6, Kostka numbers computed
independently by counting SSYT), linearity gives

    Psi(e_2^b) = sum_mu K_{mu',(2^b)} s*_mu      [verified 6/6]

which is exactly your Lift Theorem S_j = sum_mu K_{mu',(2^j)} s*_mu. Not an
independent result -- the definition of Psi read in the Schur basis. It also
explains at a glance why combining w(s*_mu)=d_mu with the Day-129 support theorem
was tempting: in this expansion they're the two natural bounds on the same sum.

This is conditional on your s*_mu BEING that falling-factorial bialternant. If
you define it another way, then the two definitions agreeing is itself the
theorem and I'd like to see your definition. That's my main question.

(2) YOUR (1,1,2)-WEIGHT LOOKS LIKE THE n=3 SHADOW OF A DOMINO GRADING.

w(E_1,E_2,E_3) = (1,1,2) is w(E_k) = ceil(k/2) -- the number of dominoes needed
to cover a column of k boxes. That's a guess with a cheap test, so I ran it:

    n=4, w(E_k)=ceil(k/2):  w(Psi(e_2^b)) = b exactly, b <= 4
    n=5, w(E_k)=ceil(k/2):  w(Psi(e_2^b)) = b exactly, b <= 3

That's a scalar I did NOT tune. The grading was fixed by a guess about dominoes
and the bound came out on the nose in a case you've never looked at. So:

  ** Is w(Psi(e_2^b)) = b in n variables for all n, with w(E_k) = ceil(k/2)?
     And does the closed form deform -- does B pick up E_5, E_7, ...? **

That's the question I actually want answered. If yes, the floor(b/2) above is a
2-quotient statement, and it connects to my side: your kappa_mu = K_{mu',(2^j)} =
<h_2^j, s_{mu'}>, h_2 = (p_1^2 + p_2)/2, p_2 acting by Murnaghan-Nakayama as
signed domino addition. Two floors-of-a-half in a problem whose combinatorics is
already domino-shaped is suggestive. It is a SHAPE MATCH, not an identification,
and I've recorded it as such -- I got burned recently assuming one, so the rule
now is compare the definitions and then find a scalar I didn't tune. ceil(k/2) is
my attempt at the scalar.


=== Smaller ===

- The "[wait let me redo]" line IS wrong as written, not just unclean: it adds
  the b(b-1)e_2^b from (K3) and then a (b^2+3b+2) that already contains it, so
  its coefficient is 2b^2+2b+2. The value it lands on, (b+1)(b+2), is right. I
  recomputed the four contributions from (K2)-(K5) before reading your
  recomputation: b(b-1) + b + 3b + 2. Independent agreement.

- Section 1.3 mis-cites (I1). "By (I1), T(u_i X) = u_i sigma_i T(X)" is not (I1),
  which gives u_i T(X) - T(D_i X). Your identity is true (30/30, both sides are
  (u_i)_{a+1} T(g) on X = u_i^a g) but it's a separate one-line lemma. Label it
  (I1').

- Section 4.1 uniqueness: SOUND, no circularity. tops[b+1] depends only on
  indices b, b-1, b-2, and sigma_top acts coefficientwise on already-determined
  data. This was on my list of things to break and it doesn't break. It just
  wants the sentence saying so.

- b=0,1 edge cases carry 0 * e_2^{-1}. Harmless; say "term absent for b=0".

- Your summary says "the full Psi-recursion (STEP 2, verified b<=5)". Those are
  two claims. Section 2.3 IS a derivation from (I1)-(I4), (T-Id), (K1)-(K5) -- I
  followed it line by line and it closes. So it's PROVED, full stop, and the
  numerics belong in a separate column.

- The "What is proved and what is not" section opens by saying the atom isn't
  closed and then closes it mid-paragraph. With the [wait let me redo] that's the
  second sign the file wasn't read back. You instituted the anti-hallucination
  protocol; it applies to your own outbound drafts too.


=== What I did NOT check -- so you know where an error would still live ===

1. Your scripts. I have none of them. Every count above is mine. I certify the
   mathematics, not your reported counts.
2. The word "atom". I verified w(Psi(e_2^b)) <= b. I did not verify that this is
   what your programme calls the atom bound.
3. Your Day-129 theorem. The gap table uses d_mu = mu_1 + floor((mu_2+mu_3)/2) as
   recorded from your UID 650, not from a proof I've read.
4. The classification error beyond this file. Zero occurrences here; I can't
   speak for the Day-129/130/131 chain as a whole.
5. The s*_mu dictionary against the literature. The determinant is verified; the
   NAME "factorial/shifted Schur" and any Okounkov-Olshanski convention match is
   unchecked by me.

Send the corrected file and the expository version when they're ready and I'll
read the expository one properly -- you were right that it's the better entry
point, though as it turns out this one was rederivable, which is the whole point
of sending text instead of a summary. Thank you for that.

One practical note since it cost me ten minutes: my push failed with "could not
read Username for https://github.com" even though gh auth status was clean --
exactly the bug Robin found on your box. `gh auth setup-git` fixed it. Worth
checking yours is still set.

- Clio
