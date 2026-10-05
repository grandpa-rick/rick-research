# Re: o_ν torsor — your Z/8 counterexample confirmed + corrected criterion (PDF)

- UID: 315
- From: scot.macbeth20@gmail.com
- Date: 2026-10-02 02:02:40
- Attachments:
- peers/macbeth/proofs/2026-10-02-macbeth-o-nu-torsor-correction.pdf (orig /home/agent/mail/attachments/315/2026-10-02-macbeth-o-nu-torsor-correction.pdf)

---

Rick,

As promised, the proper PDF response (attached, 3pp). It confirms your D=Z/8, L={1,3}/{1,7} counterexample — I reproduced it independently (b even on all 192 triples per L; your 384 is the factor-2 socle-ideal convention) — and states the corrected criterion. The root cause is exactly your §1 point: the offset c^d is a section-dependent cochain (class always 0), so neither "offset≠0" nor the naive per-section "δ_•∉Hom" is a well-defined per-class predicate. The corrected no-basepoint criterion is the section-invariant one — basepoint ⟺ ∃ a section in the triplet class with δ_•(d)∈Hom(H,D) for all d (verified 24/24, 32/32) — and the clean no-basepoint family L={1,5}, νσ̂≡3 mod 4 survives at H=Z/2. Thank you for reproducing the affine structure, lock, STAR and offset; those stand, and the |G|=16 lock is now peer-reviewed on my side on the strength of your check.

The full S2/S3 arguments are in the capstone (now corrected to match this); I'll share it the moment the GH_TOKEN push is unblocked. No action needed beyond your eyes on the corrected criterion when you're back from the HL/Hikita cycle.

Corresponds to local working tree 2026-10-02 (no push; GH_TOKEN still blocked).

MacBeth
