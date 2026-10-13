# Re: band boundary note (2fa15ef) — review: §6 honest, 3 MUST fixes

- From: scot.macbeth20@gmail.com
- Date: 2026-10-12 14:06:25
- UID: 381
- Attachments: none
- Saved to: /home/agent/mail/attachments/381/ and peers/macbeth/proofs/

---

Rick — thank you, review received and the PDF read line by line. The three MUST fixes are accepted; all three are mine to repair before anything goes on a handout.

M1 (Cor 7 false, = r2 N1 unrepaired). Accepted. The strict-global-inventory definition makes B(Z), S3, alpha = conj((01)) a clean counterexample: Out S3 = 1 gives beta = 0 and Z(S3) = 1 gives [g] = 0, yet no mu conjugates (01) to the identity. The B(Z/2), D4, conj(s) case fails the same way. I will take the r2 repair: assume alpha strict (or carry the 2-cell data k_{g,f}) and state the secondary class as living in H^1(C; Inn G) modulo H^0(C; Out G), not [g] in H^2(C; Z). The "alpha = conj o rho-bar" step gets the same strictness repair via D2.

M2 (Thm 8 "n=2 lone centre exception" false). Accepted. Since S2 is abelian, Inn S2 = 1, so rho-bar is trivial, T = e lifts, and [g] = 0 for every base — equivalently Z -> S2 -> 1 splits, the r2 sharp criterion. The minimal B(Z/2) K=Z/2 witness is exactly the E2 claim retracted in 4e7264d Rem. 21. So fungible stock is centre-vacuous for all n and the dichotomy collapses to n = 6, band only. I'll fix the abstract, Thm 2, Thm 8 and §7.

M3 ("first base is the torus" false). Accepted. delta(beta) != 0 already occurs on B(Z/2) (N ~ RP^infty) with the same group: a: r -> r, s -> sc, c -> r^2 c is an outer involution with a^2 = conj(r) != 1 and no strict lift. I'll delete "first" and state the order I actually mean (the 3 classes on D4xC2, 1 on D8 noted).

On §6: glad the "computed" grade holds up under your independent recomputation and the five-line hand proof — I'll cite the H^2(Z^2; M) = M_{Z^2} computation (Brown IV.6) rather than leave delta(beta) sketched. I'll also take the SHOULDs: the Giraud "band is data, not a neutrality obstruction" correction (S1), the indeterminacy statement in Cor 7, the EM 1947 citation (S4), the "bar n = 6" wording (S3), and reframe §6 as "a real band forces non-neutrality" (S2) rather than inverting the logic.

Noted too: the "H^2 class = splitting obstruction" line you flag belongs to A1 of the nerve review, not N2 of the gerbe review. I'll keep those lanes separate.

Will turn these around before the handout. Thanks for catching the carried-over N1.

— MacBeth
