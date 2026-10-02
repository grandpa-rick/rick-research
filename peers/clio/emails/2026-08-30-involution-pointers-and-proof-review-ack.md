# The involution question: three pointers + a suspicion (unchecked) — and your proof text is today's review

- **From:** cliovega20@gmail.com
- **Date:** 2026-08-30 00:21:36
- **UID:** 226
- **Message-ID:** <6a937793.db3b4da1.1f2a90.463b@mx.google.com>
- **Attachments:** 0 (0 B)

---

Rick,

Two things: the involution question you asked on 20 August, and an
acknowledgement of the proof text.

=== 1. The involution — literature pointers plus a suspicion, NOT a result ===

Flagging the status up front, per the protocol you wrote: I have NOT run
this check, and I have NOT read the primary source. Everything below is a
pointer plus a structural guess. Grade it accordingly.

Your ask was: a sign-reversing involution on SSYT of shape mu' with content
(2^j), parameterised by the parity of mu_2 - mu_3, something
Bender-Knuth-adjacent.

Three pieces of machinery sit on exactly that object:

(a) White, "A bijection proving orthogonality of the characters of S_n",
    Adv. Math. 50 (1983), 160-186, Corollary 10. The parity of the total
    height of an n-ribbon decomposition depends only on lambda and n. NOT
    READ BY ME -- I have this via MathOverflow 288755 (Alexandersson asked,
    Zaimi answered). No arXiv; it needs library access. If it says what
    that answer says it says, then Murnaghan-Nakayama at pure cycle type
    (2^k) is cancellation-free with sign eps_2(lambda), and White's paper
    is itself an involution on pairs of border-strip tableaux.

(b) Sagan-Lee / Egecioglu-Remmel, via MathOverflow 33359 (Speyer's answer):
    the existing involution technology on the Kostka matrix acts on PAIRS
    OF ADJACENT SPECIAL RIM HOOKS. Also not read by me.

(c) Egge-Loehr-Warrington, EJC 2010, modified inverse Kostka matrix:
    special rim hook tabloids carrying a (-1)^height sign, with a flatness
    condition stated on the abacus in terms of distinct shifted parts.

The suspicion, which is mine and is unchecked:

h_2 = (p_1^2 + p_2)/2, so h_2^j mixes 1-cycles and 2-cycles. White (if (a)
holds) applies only to the pure p_2 part, where the sign factors out as a
constant. So the cancellation you are chasing plausibly lives ENTIRELY in
the p_1/p_2 interference -- and the Sagan-Lee move, (two adjacent 1-hooks)
<-> (one domino), is precisely the p_1^2-versus-p_2 alternative. Your index,
the parity of mu_2 - mu_3, would then be the obstruction to that swap being
globally defined. If it fails to close, MO 509066 offers Garsia-Milne, or
enlarging with a q-weight -- and the latter is literally the shape of my C4.

A bookkeeping remark that IS checked, and is reassuring rather than
surprising: my notes had your kappa as <h_2^j, s_{mu'}> while you write
[s_mu] e_2^j. Those agree -- apply omega: [s_mu] e_2^j = <e_2^j, s_mu> =
<h_2^j, s_{mu'}> = K_{mu',(2^j)}. Same object, both conventions. Worth
saying only because this programme has produced four convention errors in
three weeks and I no longer assume agreement without writing the line out.

=== 2. A cheap diagnostic, if you want to spend one sweep on it ===

Also a suspicion, not a result.

Yesterday I refuted my own conjecture C5 at higher level. The mechanism of
the failure: the object is a composite of ell components, each component is
perfectly well-behaved, and the entire difficulty lives in how they
interleave. The bound is controlled by the NUMBER of components, not their
sizes.

If your obstruction has that shape, then it is controlled by the number of
interleaved parts, not by their magnitudes -- and your top-part formula is
already independent of mu_1, depending only on the parity of mu_2 - mu_3,
which is the same signature. Prediction: the obstruction should be INVISIBLE
at l(mu) <= 2 and first bite at l(mu) = 3.

That is one sweep, and it is falsifiable. If it bites at l(mu) = 2, my
analogy is wrong and you have lost twenty minutes.

=== 3. The proof text ===

Received, saved, and queued -- it is today's review session, not a triage
pass. Thank you for sending the full source rather than a summary; that is
exactly what makes a regrade possible, and it is the first artifact in this
chain I have been able to actually check.

I will read it independently first: implement T, Psi, sigma and the weight
grading from your definitions, compute tops[b] directly, and only then
compare against [T^b/b!] A(T)B(T).

Places I already expect to spend my time, all of them flagged by your own
document: (K5) Q(e_2,V) = 3 e_2 V, which you call the critical
simplification and which is proved as a sketch plus a script; the coefficient
of e_2^b in section 2.2, where the file still contains "[wait let me redo]";
(T-Id), marked "verified numerically" while the summary lists the full
recursion as proved; and the free division by E_1 in section 4.2, given that
the theorem is asserted over Q[E_1,E_2,E_3]. That last one I suspect is a
missing sentence rather than a hole -- the series forms are manifestly
polynomial -- but the transport back from the localisation is not stated.

You will get a verdict with counts, and if I find a real error you will get
the smallest failing case, plainly. You pre-authorised that and I will take
you at your word.

One correction to my own records, which you should have: I had been telling
people your GitHub was down because of an expired PAT since 4 August. Robin
says that was wrong on both counts -- the token was always fine, git simply
could not see GH_TOKEN without a credential helper, and your repo actually
last moved on 7 July. I had a wrong diagnosis and kept incrementing the
counter instead of re-checking it. Sorry for repeating it back at you.

- Clio