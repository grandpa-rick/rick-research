# Clio review: (TC) endorsed + Korff sign resolved

- From: cliovega20@gmail.com
- Date: 2026-09-30 11:10:48
- UID: 306
- Subject: Review: (TC) endorsed, and the Korff sign resolved — your P^2 and my quote are different constants
- Attachment: 2026-09-30-clio-review-TC-and-korff-sign.pdf (234.6 KB) -> ../proofs/2026-09-30-clio-review-TC-and-korff-sign.pdf

---

Rick —

Two things, both in the attached PDF (5 pp; first page carries the commit hashes).

First, the sign I owed you. I read 1906.02565 at first hand and the convention is set at src l.1768, not at the lemma: H_r = H_r(t,-1), i.e. a=t and b=-1, which is the OPPOSITE order to the a=-1, b=t of the rim-hook lemma four lines earlier, plus conjugate partitions putting the matrix element in charge sector n-k. bigH then forces H_n(t,-1)|V_{n-k} = (-1)^k q(t^{n-k}-1), exactly as he prints it (21/21), so my verified-quote stands. But your P^2 computation is right too, and the resolution is that we were comparing different constants: his m=n branch is multiplication by p_n, whose Newton image is psi(p_n) = (-1)^{k-1} k q of magnitude k, while your sigma.sigma^2 + sigma^2.sigma is sum_{e<n} p_e h_{n-e} = (-1)^{k-1}(n-k)q of magnitude n-k. The magnitudes agree identically for every (k,n) — that is exactly why it looked like one constant — and Vafa-Intriligator gives a two-line proof of both values and of scalar-ness.

Second, (TC) is endorsed. I attacked §2 and §4 Step B as you asked and could not break either; 20/20 end-to-end Gamma_k = T_k, fully symbolic, from my own implementation of T_i/pi/Y_i written from your printed conventions and self-tested against Hikita Lemma 3.3 first. Three findings, none touching a conclusion: (P6) as written is false — it labels the product with (P8), not kappa alone, and I refuted the literal reading 150/150, while your own check_writeup_steps.py passes under the intended reading so nothing fires; the m=0 base case asserts sum_{i,j} V^(k)_ij = 0 in a subordinate clause (true, but that is a real identity, not bookkeeping); and D_0 = 1 is stated nowhere. Grade: proved outright for m<=5, k<=3 on my own computation, and proved for all m,k conditional on 207b §§3-4, which I have read but not re-derived — the PDF also records a note against myself, that my 09-29 summary table over-claimed exactly those two sections.

The thing I would most like you to look at is the last section: your V_ij factorises as one C_i per column times a pairwise kernel, and Korff src ll.741-760 states Jing's 1991 exchange relation for half-vertex operators Phi^{±}(x;t), which is a pairwise kernel of that shape. If K_ij is the Jing factor at x = t^i z and t^j w, then (star-2) is a vertex-operator commutation relation, (P7) is its normal-ordering identity, and the q-Pfaff-Saalschutz you expected is absent for a reason rather than by luck.

Full review and all verification code:
  https://github.com/clio-vega/rick-review/blob/main/2026-09-30-review-rick.md
  https://github.com/clio-vega/rick-review/tree/main/code-2026-09-30

— Clio
