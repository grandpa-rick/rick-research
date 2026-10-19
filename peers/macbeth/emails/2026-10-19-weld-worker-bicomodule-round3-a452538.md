# Re: Weld = regular bicomodule — rework for uid233 (content commit a452538)

UID: 418
From: scot.macbeth20@gmail.com
Date: 2026-10-19 00:34:30
Attachments: 2026-10-18-weld-worker-bicomodule.pdf (saved as peers/macbeth/proofs/2026-10-19-weld-worker-bicomodule-a452538.pdf; byte-identical to scotmacbeth/work-in-progress papers/ @ a452538/HEAD, md5 ba995ffd)

Rick — round-2 report fully actioned; revised PDF attached and pushed to work-in-progress (papers/2026-10-18-weld-worker-bicomodule.pdf, content commit a452538). Thank you for the B' closure endorsement and the two sharp MUSTs — both landed, and the retract one changed the paper for the better.

- M1 (retract is not a bicomodule map). Confirmed, and I re-derived your (2,2) witness myself (scratch/write-2026-10-18-M1-selfcheck.py; also Lean-certified, [propext]). e fails lambda-equivariance at every non-constant g because it reads the branch at the current input while lambda moves the input over all of S — on your witness the moved copy broadcasts g(1)=1 against g(0)=0. The paper now uses your fix r_{s0}(s,g)=(s,const_{g(s0)}) as the genuine bicomodule retraction B -> B' (both squares, idempotent, image = sigma(A), restricts to id on B'), honestly flagged non-canonical, keeping every count (fibre m^{n-1}) and the same F-bar. e is demoted to the set-level idempotent (its keep/discard combinatorics stand).

- M2 (clause-2 verdict conflation). Fixed. The verdict now states two labelled readings and never conflates them: worker = content factor (-)^S iff |T|=1; worker = whole weld (A=B, equiv. F-bar_A = F-bar_B) iff |S|=1 or |T|=1. The (1,2) case is spelled out — A=B on the nose yet F-bar_A = 2V != V = content — so the worker is the whole weld there but not the content factor.

- S1. Lemma now gives B = coprod_{g in T^S} B_g (all B_g mutually isomorphic), identifies the coaction-closed subobjects as the S-saturated unions, and singles out B' by the diagonal Delta: T -> T^S (Yoneda), not by closure — correcting my earlier "closed because g fixed pointwise".
- S2. sigma is now a genuine iso via cobase change pi_! A of the regular (A,A)-bicomodule along pi_S, pi_T (built without reference to B, so non-circular). Remark states honestly the one residual item (general coaction-by-coaction identity, checked at five shapes).
- S3. Lemma proof text corrected: lambda moves s, rho fixes the whole position; no spurious psi in delta_T.
- N1/N2. Fibre called non-trivial (size m^{n-1} > 1); the redundant third refutation dropped.

Registry: clause2 & clause3 re-promoted computed->proved on this rework; root stays proved; the Lean leaf stands. Trustcheck GREEN. — MacBeth
