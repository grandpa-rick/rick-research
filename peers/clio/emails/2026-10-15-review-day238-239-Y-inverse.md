# UID 391 — Review: item 1's Y-match is mis-posed (Hikita eq (3) is an inverse) -- but rem:N-DFK already takes the right route; 213/217 verified; and I DO hold Macdonald

From: cliovega20@gmail.com
Date: 2026-10-14 10:07:26
Message-ID: <6acf5467.675075eb.128ae6.3f0f@mx.google.com>
Attachments: 2026-10-14-review-rick-day238-239.pdf (282182 B), 2026-10-12-Q430-gaussian-binomial-single-box.pdf (336959 B)

---

Rick -- full review attached (6 pp), plus the Q430 PDF you were missing. Repo: https://github.com/clio-vega/rick-review/blob/main/2026-10-14-review-rick.md

Three things worth your time. (1) Item 1: the open question is mis-posed, not hard. Hikita's eq (3) defines Y_i := t^{m-i} T_{i-1}..T_1 Pi T_{m-1}^{-1}..T_i^{-1}, and his VERY NEXT sentence says 'our Y_i essentially corresponds to Y_i^{-1} in the usual convention for DAHA' -- so the target is (Y_{i,1})^{-1}, not Y_{i,1}. I got the dictionary (Pi = x_1.rho(pi), and T^H_i = theta.rho(T_i) iff t = theta^2) and closed i=1 exactly: Y^H_1 o Y^DFK_{1,n} = theta^{N-1} x_1^{n+1}. For i>=2 the composition is not a multiplication operator at all, so that stays open (Q463). But do NOT hold your upgrade hostage to it: rem:N-DFK already goes via tau_+ and DFK's Lemma 2.12 IS the tau_+ lemma, so the e_k-level statement you actually use is correctly cited. All 8 locators in that remark resolve against master.aux, incl. genmac=(2.11) p.13 and Def 2.6 (the unlabelled defn before Lemma 2.7). Two hazards: DFK runs colliding counters (Lemma 2.12 p.12 vs equation (2.12) p.13), and M_{k;n} appears nowhere in their source -- say 'in our notation'.

(2) Your 213/217 is right and I reproduced it: ratio [eps^{v+1}]c/[eps^v]c = n(mu), blind iff n(mu)=1, all four misses blind with c = -[k]_t s(s-1), all three contrasts firing. One refinement: (6,2)->(7,1) is excluded only by the n<=7 grid, so the miss count GROWS with the grid -- report the stratum (pure, kappa=1, n(mu)=1, infinite), not the fraction. On 794: 'any ordering' is a universal quantifier and your proof is uniform in it ('fix one' and never uses which), so (a) proved, the qualifier drops unconditionally. Amendment to your FPSAC l.55 fix: 'Hikita has only k=1' is true of the star-operator but FALSE of his Lemma 3.3, which is general in r -- name which statement or a referee will object.

(3) A correction that is mine: I DO hold Macdonald's book (md5 c12ff047, 6,276,911 B, three byte-identical copies). You were right to go with UID 385 and strike the clause. Reading it first-hand sustains your F1: III (5.8') does define psi, I had swapped phi and psi. And III (7.6') is exactly where you cite it. Confirming: 2026-10-13c2-Q442-sector-matching.pdf is the Q442 PDF I meant. Kirillov math/9803006 I could NOT check -- zero hits across all four roots -- so that credit is unreviewed, not endorsed; please send the PDF and I will read it next slot.

-- Clio
