# Correction to my Thm 6.6 report: your d7bca5e widening is CORRECT — ignore my 'do not widen' paragraph

- From: cliovega20@gmail.com
- Date: 2026-10-09 10:40:50
- UID: 352
- Message-ID: <6ac8c4b8.1c79dfcc.28be14.4ca9@mx.google.com>
- Attachments: 2026-10-09-rick-fpsac-thm66-cold-read.pdf (raw: /home/agent/mail/attachments/352/)

---

Rick — one correction to the report I sent minutes ago, and it matters because acting on the stale paragraph would make your draft worse, not better.

Updated PDF attached; repo updated at ed81e45.
https://github.com/clio-vega/rick-review/blob/main/2026-10-09-rick-fpsac-thm66-cold-read.pdf

RETRACTED. My report's closing section said 'please do not widen past the numerator shape t^c prod(1-t^{d_i}).' Ignore that sentence. I wrote it from a brief prepared at 00:40 and had not read your 09:18 mail (UID 793) when I sent it — I read the brief's account of my inbox instead of the inbox.

YOUR WIDENING IS CORRECT AND I ENDORSE IT. At d7bca5e the sentence reads t^c prod_i (1-t^{d_i})^{e_i} with e_i in Z, products and quotients. That is exactly the right scope, and it is WIDER than what I told you to stay within — had you acted on my paragraph you would have narrowed a correct citation. The reason e_i in Z is right: nonvanishing survives inversion, so the +-1 hypothesis is never used, and quotients are obstructed on the same grounds as products. Your matching change from 'a product of cyclotomic factors' to 'a product or quotient' is also correct.

THE BOUNDARY THAT STILL HOLDS, unchanged, and you already satisfy it: what is machine-checked is the obstruction for the written-down polynomial. Y^lambda_rho, Hall-Littlewood P_lambda, Kostka-Foulkes and charge have no Lean definitions in my development, and Theorem D itself is not formalised. I checked the draft: zero occurrences of 'Lean', 'formalis*' or 'machine-check', and Clio26 cited exactly once. Nothing to change.

TWO OF YOUR CLAIMS, VERIFIED RATHER THAN TAKEN ON TRUST. You wrote that Thm 6.6 is untouched since 0dcdc5e: diff 0dcdc5e..d7bca5e on the draft is a single changed line, and it is the Example 6.5 sentence, not the Theorem 6.6 block — so my report stands against d7bca5e as well. And you asked me to send back any t>0 sign failure in cor:G(d) as a real error: there is none. Regular at t=1 for all 13 shapes, value (-1)^{l-1} n^{l-1} matching (c), sign (-1)^{l-1} across t in {0.01, 0.5, 0.9, 1, 1.1, 2, 5, 50}, no violation, and the test has a working control.

Everything else in the report stands as sent: the <,> vs <,>_t finding, Prop 6.1 having no proof idea, m_xy, the undefined bracket, the X clash, and the retracted Phi asymmetry that was my own bug.

— Clio
