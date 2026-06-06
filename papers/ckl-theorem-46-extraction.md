# CKL Theorem 4.6 — proof structure extraction (focused on the (SA) question)

**Source:** Choi–Kim–Lee, arXiv:2412.20757v2, §4.3 (pp. 23–24); supporting Appendix A.5–A.6.
**Question:** Does the proof use bigraded acyclicity of the BGG–Verma resolution at spin λ?

---

## ⚠ EDITORIAL CORRECTION (added 2026-05-07, session 3)

**Earlier sections of this note imply that Theorem 4.6 is the q-only or
"polynomial-level" statement, with the q,t-bigraded version still open.
That implication is wrong.**

CKL Theorem 4.6 IS the q,t-bigraded statement: it asserts
$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \sum_T \mathrm{energy}_{q,t}(\phi_c(T))$
where each summand is $q^a t^b$ with $a, b \ge 0$. So Theorem 4.6 ⟹ (SA) for
dominant spin λ, μ directly. The "BMR conjecture" in `state/PROVE.md` is
equivalent to Theorem 4.6 (modulo eq. 4.13).

The proof of Theorem 4.6 in §4.3 IS bigraded throughout: Lemma 4.21
(q^r t^m energy shift) and Remark A.17 (D̄-invariance under Aug for spin
column) are the bigraded refinements of the type-C / un-bigraded versions.
The only step CKL leave implicit is the **vac-invariance under Aug**, which
is elementary: for $b_1 = [1..k] \in B^{\mu_1, 1}$, vac = $\mu_1 - k$;
for $b_1' = [1..k+r] \in B^{\mu_1+r, 1}$, vac = $(\mu_1+r) - (k+r) = \mu_1 - k$.
Same. (Proved fully as Lemma 3.1 in `proofs/2026-05-07-BMR-via-CKL.md`.)

Section 4 below ("structural mismatch") still correctly identifies that
CKL's signs are at the n-indexed (Morris) level, not the W-indexed (Verma)
level. That is a real distinction. But it does NOT mean (SA) is open —
it means CKL prove (SA) via a *different* combinatorial route than the
Aug~ on (w, π) program. Both routes prove the same theorem.

---

## 1. The proof skeleton (verbatim sketch, p. 23)

> "4.3. Proof of Theorem 4.6. In [Lec06, Theorem 3.2.1], Morris type recurrence formula for type B is derived. A straightforward generalization of the argument there leads to the following q,t version: [eq. (4.13)]
>
> $$\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t) = \sum_{i\ge 1}(-1)^{i-1}\sum_{r+m=\lambda_i-\mu_1+1-i}\, q^r t^m \sum_{(\lambda^{(i)},\tau,\nu)\in\mathrm{ROHS}^{\le n-1}(\lambda^{(i)},r)}\mathrm{KL}^{B_{n-1}}_{\nu^\sharp,(\mu')^\sharp}(q,t).$$
>
> We proceed with **induction on n**. The base case n=1 is covered easily. … The right-hand side becomes [eq. (4.14)]" — a triple sum over $i$, ROHS data, and GSSOT.
>
> Footnote 5 (p. 23): "**For weights that are not spin weights, we do not have a recurrence for the q,t version as elegant as (4.13).**"

The induction step uses two technical lemmas:

- **Lemma 4.20** (counterpart to 4.9): bijection $\Phi^{(i)}:\mathcal A^{(i)}\to \mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\gamma^{(i)})$.
- **Lemma 4.21** (counterpart to 4.10): $\mathrm{energy}_{q,t}(\phi_c(\Phi^{(i)}(S,T))) = q^r t^m\,\mathrm{energy}_{q,t}(\phi_c(T))$. *Follows from Proposition A.26.*

Then "the proof follows exactly as in the derivation of (4.8)" — i.e., a **sign-reversing involution** on $\bigsqcup_{i\ge 1}\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda^{(i)},g),\beta^{(i)})$ whose fixed-point set bijects to $\mathrm{GSSOT}_{g+\frac12}(\mathrm{oc}(\lambda,g),\mathrm{oc}(\mu,g))$.

## 2. What machinery is used

1. **Lecouvey's Morris-type recurrence** [Lec06, Thm 3.2.1] — a Pieri/branching identity at the level of *characters*, q,t-deformed via combinatorics of horizontal strips. Crucially this is a recurrence in $n$ on the polynomial $\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t)$ itself, **not** a Verma/BGG identity.
2. **Splitting map** S, energy invariance under R-matrix and within classical components (Appendix A; Prop A.13, Prop A.26). Pure crystal/combinatorial content.
3. **Sign-reversing involution / jeu-de-taquin (Aug)** matching ROHS-paired GSSOTs (Section 4.2 for type C; "exactly parallel" for type B spin per p. 24). The signs that get cancelled are the $(-1)^{i-1}$ from Morris recurrence — *not* Weyl-length signs.

## 3. What's NOT used

- **No mention of Verma modules, BGG resolution, or Kostant partition function anywhere in §4.3 or its supporting appendices** (verified by grep of the full PDF for "Verma", "BGG", "Kostant partition").
- The Weyl-character formula appears only in §5 (level-restricted multiplicities) and only in its standard form, not as an alternating Verma sum.
- The reference [Bry89] (Brylinski's filtration → Lusztig polynomial) appears once in the introduction as historical context; never used in the proof.
- The "(SA) bigraded acyclicity at every $(i,j)$" — the statement that **odd-length Verma supports at $\mu^\sharp$ are bidegree-dominated by even-length ones** — is **never stated, never used, and never implied** by their argument.

## 4. The structural mismatch

CKL's signs are $(-1)^{i-1}$ from the Morris recurrence index $i\in\{1,\ldots,n\}$. Rick's signs are $(-1)^{\ell(w)}$ from $w\in W=(\mathbb Z/2)^n\rtimes S_n$, $|W|=2^n n!$.

These two alternating sums **both equal $\mathrm{KL}^{B_n}_{\lambda^\sharp,\mu^\sharp}(q,t)$** but they live on different index sets and cancel different things. CKL's sign-reversing involution operates on horizontal strips and uses the splitting map; it never indexes by Weyl group elements at all. So CKL's proof factors $\mathrm{KL}$ as a *positive* sum without ever computing or comparing the $2^n n!$ Verma weight-bidegree supports that (SA) requires.

## 5. Why the spin restriction enters CKL's proof

The spin restriction enters via **footnote 5 + Proposition A.26** (which uses $r+m$ rather than $r+2m$ — see eq. (4.13) vs. (4.4)): only for spin weights does the q,t-Morris recurrence have the elegant form (4.13) where $r$ counts long-root contributions and $m$ counts short-root, additively (not $2m$). For non-spin weights, the recurrence breaks and no clean q,t-deformation exists. This is consistent with Remark 4.7's negative coefficient.

## 6. Citations
- §4.3, p. 23–24: proof sketch, eq. (4.13)–(4.16), Lemmas 4.20, 4.21.
- Appendix A.5 (Prop A.13): D-invariance under Aug.
- Appendix A.6, Proposition A.26 (p. 56): $\mathrm{energy}_{q,t}(v\otimes T)= q^r t^m \mathrm{energy}_{q,t}(T)$ — the "single-prepended-letter" energy shift, which powers Lemma 4.21.
- Footnote 5, p. 23: explicit acknowledgement that the recurrence breaks for non-spin weights.
- [Lec06, Thm 3.2.1]: source of the Morris recurrence for type B.

(~595 words.)
