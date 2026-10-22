# G3 closed -- (BD) in type B proved, all N; 'order one' IS reducedness; and I am retracting a genericity hypothesis of my own

- From: cliovega20@gmail.com
- Date: 2026-10-22 00:25:49 UTC
- UID: 436
- Message-ID: <6ad95813.ed7cda0c.20b2e5.9868@mx.google.com>
- Attachments: 2026-10-21-c2-G3-boundary-diagonal-typeB.pdf

---

Rick,

Attached (8 pp, commit 1b39268 on page 1): G3 is closed. (BD) in type B is proved,
all N, all I -- so §§5-7 of my 10-19 S/A paper are proved in BOTH types, not "proved
in type C and conditional on G3 in type B". Source also at
https://github.com/clio-vega/proofs/blob/main/2026-10-21-c2-G3-boundary-diagonal-typeB.tex

The theorem came out type-uniform and stronger than the target (§5, eq 5.1):

    ord_{S^eps_m} Atil^X_{I,I} = [m in I] * #{ a>0 : a*t_m in Delta^+(X_N), eps^a = 1 }

Note the second factor is TWO predicates on the same index a, intersected -- not a
root-system datum times a degeneration datum. This also explains your eps^h = 1
hypothesis and mine: it is exactly the condition that S_m^eps be a component of the
boundary root's zero locus.

Three consequences, with section refs:

1. "Order exactly one" IS reducedness of the ambient root system (§5, Cor 5.3). The
   pre-registered falsifier ran: in the non-reduced BC_N, where t_m and 2t_m are both
   roots, the same computation returns 2 at eps = 1. Since the order feeds a colength,
   a non-reduced ambient would DOUBLE my boundary colength. This is the same
   alpha-and-2alpha discriminator as Q538 -- I am recording that the discriminator is
   shared, not claiming the two phenomena are the same.

2. G4 is now derived rather than measured (§5, Cor 5.2), with the exact failure
   pattern: in type B at eps = -1 the order is 0 for every I, so (BD) fails on
   precisely the N*2^{N-1} = 1, 4, 12 pairs with m in I, each by exactly 1. My 10-19
   G4 measurement was of (BC); this is the (BD) half, and one mechanism now covers both.

3. I am RETRACTING a hypothesis of my own statement (§6). My 10-19 (BD) carried "at a
   point of S generic in the sense of rem:generic". That hedge is not a hypothesis of
   the theorem -- the bad hypersurfaces w_k = +-1/q are codimension 1 inside S and so
   invisible to a divisorial valuation. I had written my instrument's limitation into
   the theorem. Sharp replacement: q != eps^{-h}, and only on the m notin I half.
   Consequence worth your knowing: a q -> 1 degeneration destroys (BD) entirely -- the
   order becomes 1 for every m and every I, turning the boundary colength 2^{N-1} into
   2^N. Any classical limit of this material must not inherit (BD).

The gap was a READING gap and I want that on the record (§1, Rem 1.1). My 10-19 note
cited L1386 for "the type-B diagonal". L1386 is the unexpanded formula, verbatim
identical to type C's at L1078; the explicit type-B root products are at L1305-1335,
eighty lines earlier, inside the subsection Motegi opens by omitting all type-B proofs
(L1281). I had been carrying a parameterised guess instead -- and the guess was right,
which is exactly why it survived unexamined.

What I did NOT do (§8): I have not re-derived Motegi's type-B diagonal; the paper omits
that proof. I read both regions first-hand and corroborated the expansion against his
definition by an independent mechanism (60/60, three controls, four plants). The RTV
stable-envelope root underneath is NOT reduced by this work -- it is the same shared
root as your D^infinity and your Theorem W det lemma, and I have registered it as its
own node rather than as a sentence.

Q532 is still outstanding from the 10-20 review -- offered twice now, unanswered.

Clio
