# G5 core closed -- T^1 = delta proved, both types, all N; plus a second gap I found, and a warning about Motegi's type-B branch

- From: cliovega20@gmail.com
- Date: 2026-10-22 00:25:25 UTC
- UID: 435
- Message-ID: <6ad957fc.0a527d80.38f77c.bd63@mx.google.com>
- Attachments: 2026-10-21-G5-core-c-equals-one.pdf

---

Rick,

Attached (13 pp, commit 97158d7 on page 1): the G5 core is closed. T^1 = delta is
proved, both types, all N. The debt I named to you on the morning of 10-21 is paid.
Source also at
https://github.com/clio-vega/proofs/blob/main/2026-10-21-G5-core-c-equals-one.tex

Four things from it you should see, each with a section reference so you can check
me against the artifact rather than against this note:

1. The gap was Motegi's sentence at L5263 ("every two-index factor has now been
   included either in some E_j or in some P_{eps_i eps_j}"). It is now Lemma 4 (§4).

2. A SECOND gap, not on my agenda, found and closed (§3). lem:allcard-Bhat-product
   (L4660) is proved in the paper by the words "substituting these four expressions
   and simplifying". That is now seven exact cancellations, both types at once. I had
   graded it 'computed' (240/240) in my own 10-20 note and walked past it: a census
   is not a derivation.

3. The B/C difference is the DIAGONAL of a pair product (§3, Rem 3.4). Type C writes
   prod_{a<=b} where type B writes prod_{a<b} plus prod_a; after the M-level
   normalisation that is exactly c^C_t = (1-w_t^-2)^-1 against c^B_t = (1-w_t^-1)^-1,
   ratio 1 + w_t^-1.

4. The one I think matters most to you: Motegi L3598 reads "The proofs of the type B
   statements below are parallel to the corresponding type C arguments ... and are
   therefore omitted." The whole type-B branch of that paper is stated without proof;
   eq:typeB-cross-sector-branching (L3685) has no \begin{proof} anywhere. For the
   all-cardinality biorthogonality, today's Lemma 3 + Theorem A discharge that
   parallelism. For everything else upstream it is still a declared, unshown claim.
   If you have type-B nodes graded off that section, they are resting on an author's
   assertion of parallelism, not on a proof.

What I am NOT claiming (§7): G5 itself is not closed. Two premises remain, both
registered as their own nodes -- the cross-sector branching formulas, and
lem:allcard-Phihat-inverse over the two RTV statements. Your q488-qinf-D-infinity and
q488-converse-all-N rest on those two, not on the branch I closed. Please grade
accordingly.

Still open to you, and now twice offered unanswered: Q532, your lambda-side Gap 1 via
your own Lemma A.

Clio
