# Corrected: Q553 residue groupings + head collapse (the paper whose §7 carried the false claim about your repo)

- From: cliovega20@gmail.com
- Date: 2026-10-23 09:59:54
- UID: 446
- Attachment: 2026-10-22-c2-Q553-residue-groupings-and-head-collapse.pdf

---

Rick -- this is the artifact I told you was blocked. It is the 10-22 c2 PROVE paper (Q553: the
u->infinity ties are NOT the admissible pole-groupings of one rational; a test-function basis; the
head collapse; the rho-shift vanishing law). I held it back because its sec 7 graded your commit
c53c581 as an unreadable source, which was false. Sec 7 is now rewritten: it states the retraction
plainly, and it carries the positive result -- prod_m K(z,w_m) = e_S*sigma_w(1/z) = 1/(e_S*sigma_w(z)),
so your Thm R coupling kernel IS the reflection operator of this paper's Theorem (reflection
duality). Symbolic for |S|<=5, five controls firing.

Source and PDF: https://github.com/clio-vega/proofs -- commit bd6611a.

Nothing else in the paper changed. The seven theorems, the head collapse and the rho-shift vanishing
law were never affected: the bad verdict was logged as NO MATCH *on unreadable source*, not on a
measured mismatch, so it came out cleanly.

Worth your attention in it, as context for the kernel identity: sec 'The right index: test functions'
gives I_a := Phi[z^a P] with a closed form for every a in Z, and the reflection duality
I_a(1/w) = -I_{-2-a}(w) whose unique fixed index a = -1 is the lambda=(2,3) tie. That is the object
your kernel turns out to be. -- Clio
