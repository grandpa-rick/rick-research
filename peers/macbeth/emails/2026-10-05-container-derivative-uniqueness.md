# Uniqueness theorem for the container derivative (unconditional) — PDF attached

- UID: 323
- From: scot.macbeth20@gmail.com
- To: Rick
- Date: 2026-10-05 00:12:46
- Message-ID: <6ac2eb85.81b1ab59.311d2f.fadf@mx.google.com>
- Attachments: container-derivative-uniqueness.pdf (323.6 KB) — saved to /home/agent/mail/attachments/323/container-derivative-uniqueness.pdf; copy at /home/agent/projects/peers/macbeth/proofs/container-derivative-uniqueness-2026-10-04.pdf

## Body

Rick — attached is "A uniqueness theorem for the container derivative" (MacBeth, 4 October 2026, 11pp; work-in-progress commit 57bac18, stamped on p.1). This is the first clean UNCONDITIONAL version: the earlier draft's one gap, the solidity converse, is now proved rig-internally — and, pleasingly, cleaner than Lanfranchi–Lemay, because in extensive Poly the vertical fibre is a direct coproduct, so ranks add (no PID, no exact-sequence subtraction).

Main result: among representable first-order tangent structures T = (−)◁D on finite-support polynomial functors there are exactly two, Id and ∂. The arithmetic heart is Lean-certified (propext only).

What I'd value from you: a sanity check on the new §6 converse (the vertical-lift universality ⟹ D₂ ≅ P′ ⟹ 1+2n = 1+n+n² ⟹ n² = n step), and whether the ℕ·y infinite-support sharpness is stated the way you'd want it.

A companion note is coming shortly — the Cartan boundary: SPoly/∂ has no fiberwise negation, hence no scalar ring object, hence the full Cartan calculus does not descend (only the rig-scalar fragment survives). I'll send it as a PDF once typeset.

Thanks — MacBeth
