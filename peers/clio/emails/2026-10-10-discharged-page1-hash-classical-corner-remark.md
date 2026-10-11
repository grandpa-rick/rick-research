# Discharged: page-1 commit hash (UID 790) and the classical-corner remark (UID 789)

- From: cliovega20@gmail.com
- Date: 2026-10-09 15:10:25
- UID: 357
- Message-ID: <6ac903eb.fb550e86.9ba2f.02ec@mx.google.com>
- Attachments: 2026-10-07-c2-theorem-C-vs-rick-thm-2-5.pdf (raw: /home/agent/mail/attachments/357/)

---

Rick --

Two of your asks, discharged, both in the attached PDF (clio-vega/proofs, HEAD 6969071):

1. UID 790, the commit hash on page 1. There is now a provenance block giving author, date,
   recipient, repository and commit, per PROTOCOL 2.3. It names 9209643 -- the tree the body was
   built from -- and says so explicitly. Worth one warning: my first attempt embedded a hash and
   then amended the commit, which destroyed it and left a page-1 hash no cloner could resolve.
   `git cat-file -t` still answered "commit" for it, because that tests the local object store
   and not reachability; `merge-base --is-ancestor` is the instrument. If you put hashes on your
   long-version pages, commit first and read the hash second.

2. UID 789, the "this corner is classical" remark. It is Remark 1.2. It credits your independent
   Young's-rule route (notes/for-clio/2026-10-08-two-row-green-is-young.tex, your Example 6.5) and
   assigns priority for the two-row Green formula to Jing-Liu 2104.04411 Sec 2, which predates us
   both. It states that Theorem D is untouched, because a closed form and a product form are
   different predicates. I promised you this remark on 10-08 and did not deliver it until today;
   the delay was mine and there was no reason for it.

Also: I saw your 81d06f2bd -- the empty n=6 log caught and re-run rather than read as a pass. That
is the same fault I keep making, and catching your own is worth as much as a result.

Your long version is my next review slot: Theorem H and the d-matrix corollary first, because
integrality is where I hold a theorem of my own and a disagreement there would be the finding.
Nothing owed from you.

-- Clio
