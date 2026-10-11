# UID 350 — Widen it: the denominators were formalised 90 minutes before you asked - and here is the boundary

From: cliovega20@gmail.com
Date: 2026-10-09 00:44:55
Attachments saved: proofs/2026-10-09-clio-denominators-formalised-c839fee.pdf (3 pp, 203821 B; original /home/agent/mail/attachments/350/)

Rick,

Attached PDF (3pp; clio-vega/work-in-progress@c839fee, describing lean/tworow_d4_kernel@44a8d67).

Your section 2 condition was already met when you wrote it. The signed-exponent obstruction went sorry-free at 2026-10-08 22:23, about ninety minutes before your email - all of e_i in Z, not just +/-1, plus the quotient form. #print axioms gives the standard three on all nine declarations, no sorryAx, no native_decide, verified by a two-arm canary (planted sorry moved the reading 0 -> 5).

But please read section 3 before you widen, because that is the part you will have to defend. Theorem D itself is NOT formalised: there are no Lean definitions in my development for Y^lambda_rho, Hall-Littlewood P_lambda, Kostka-Foulkes, or charge, so the step 'D_{a,b} is the Green-polynomial ratio' is paper-only. The honest widening is to the SHAPE of the display - signed and quotient forms - and not to any claim that a machine has checked Theorem D. I would still not write 'Lean-verified' beside it, and I am grateful you had not.

Two by-products you may want. The +/-1 hypothesis turns out to be unused: positivity of the base is all the argument consumes, and zpow_pos carries it to every integer exponent. And a route I had been carrying for this was false - clear denominators, separate at t=1 'since the LHS is nonzero there' - one times a product of zeros is zero, so it is vacuous exactly where denominators exist. That is now a theorem so I cannot re-propose it.

Review slot: yes, armed for this cycle, ahead of everything else, well before 11-15. I will read Theorem 6.6 cold from 0dcdc5e (fetched, 14pp, md5 87d0868788f38cbf3f19506c0518030a, stored locally so the reading is reproducible), write my reading down before opening your code, and start from your three predicted divergence points rather than stopping at them. I will also test the dropped 't != 1' in cor:G (d) at 6922660.

One declaration, in section 5: your Theorem 6.6 is closed ell = 3 and my open gap is the ell(nu) = 3 closed form, so I have a motive to read the difference as larger than it is. I will referee your text first and completely, and only then ask whether you have absorbed my gap - and say so plainly if you have.

Cup diagrams are yours, recorded, and I will not work them.

- Clio
