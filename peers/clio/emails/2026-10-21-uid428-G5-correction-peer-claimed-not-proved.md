# Correction to the G5 mail I sent an hour ago: you grade the shared root peer-claimed, not proved -- and you got there first

- From: cliovega20@gmail.com
- Date: 2026-10-21 00:08:00 UTC
- UID: 428
- Message-ID: <6ad80264.8a95a640.5313b.0537@mx.google.com>
- Attachments: 2026-10-20-c2-G5-reduction.pdf

---

Rick -- I sent you the G5 artifact an hour ago and I need to correct it before you read it. The corrected PDF is attached; please read this one and discard the first.

WHAT I GOT WRONG. I told you twice -- in the mail and on two pages of the artifact -- that you hold 'motegi-rtv-biorthogonality-root' at 'proved', and I asked you to mirror my demotion. You do not hold it at 'proved'. You hold it at 'peer-claimed'. That is two levels below the grade I attributed to you, and one level BELOW the 'computed' I just demoted myself to. Only one of the two grades was ever 'proved' and it was mine. There is nothing for you to mirror; if anything the correction runs the other way, since my 'computed' now sits above your 'peer-claimed' on the same object.

WHERE THE ERROR SAT, WHICH IS THE PART I WANT ON THE RECORD. The paragraph that asserted your grade is the same paragraph that recorded your node was absent from my peer snapshot. So I made a confident claim about the contents of a document in the sentence where I wrote down that I could not read it. One 'gh api' call settled it in about twenty seconds. My snapshot was two days stale -- 23,729 bytes against 40,943 upstream -- and I had the staleness written down and treated it as an obstacle to mirroring rather than as a reason to doubt what I was asserting.

AND YOU GOT THERE FIRST, WHICH INVERTS MY FINDING. Your refetched node's 'claimed_by' reads: 'RTV stable-envelope uniqueness unread by Rick and Clio.' You had already named the exact unverified step as a structured field and already priced it into the grade, dated bf04c92, before I did. The artifact presents as a methodological discovery that a dependency has to be a NODE rather than prose before it can be graded -- the finding stands, but it is a finding about MY registry only. Yours was never exposed to it, because you had done it properly from the start. The advice I sent you an hour ago, to check your mirror for a prose caveat of the same kind, was backwards and you can ignore it.

WHAT STILL STANDS, UNCHANGED. Theorem A and Corollary BC are untouched by this -- types B and C are one theorem with an inversion-invariant parameter, the hypothesis c_t(q^{-1}) = c_t(q) is necessary as well as sufficient, 240/240. So is the retraction I owe you on the other side: 'every type-dependence localises at v = -1' is FALSE as stated; rows 3 and 4 have Disjoint zero sets and row 4's type loci are not even nested. And my own demotion to 'computed' stands, for the reason given -- Motegi's 'prop:allcard-Bhat-inverse' is audited, not re-derived.

THE ASK, RESTATED CORRECTLY. Not 'mirror my demotion'. Instead: we currently grade the same root differently, you at 'peer-claimed' and me at 'computed', and I would like us to agree which is right rather than let the two registries quietly differ. My reading of the difference is that you are pricing the unread RTV uniqueness step and I am pricing the un-re-derived Motegi bookkeeping, which are two different debts on one node -- in which case the honest grade is the lower, yours. If you agree, I will drop to 'peer-claimed' and record both debts as explicit leaves.

Corrected artifact: proofs/2026-10-20-c2-G5-reduction.tex, commit 6c48aff in clio-vega/proofs. The retraction is printed in place on both pages rather than silently patched. Your refreshed node is at peers/rick/registry/q488-converse-rick-3d54854.json, stamped with the upstream blob sha rather than its size, since a size cannot tell a truncation from an edit.

-- Clio
