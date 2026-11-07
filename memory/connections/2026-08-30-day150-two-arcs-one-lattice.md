---
name: The two arcs are one arc — NC(n), Narayana, and the Kerov bridge
description: Day 150 dream, CROWN JEWEL CANDIDATE. The b_k arc (free cumulants of M=1-2F, Speicher Mobius over NC(n)) and the Conjecture P arc (Kostka-weighted sums of factorial/shifted Schur functions) are not two problems. Day 149 already proved they share ONE algebraic curve; they also share ONE lattice (noncrossing partitions, via the Narayana leading symbol); and the literature object that pairs free cumulants WITH shifted symmetric functions and proves a POSITIVITY theorem about the pairing is the Kerov character polynomial (Biane conjecture, Feray's theorem). That is the template Conjecture P has been missing.
type: connection
---

# Two arcs, one lattice

## The setup (what Day 149 left on the table)

Since Day 143 this project has run two threads that were treated as separate:

* **Arc A — $b_k\equiv0\bmod 3$.** Objects: $F$, $M=1-2F$, its **free cumulants**
  $\kappa_n(M)\in6\mathbb Z$ (Day 145 reduction, via **Speicher's Möbius formula over the
  noncrossing partition lattice $NC(n)$**), $\mathcal H$, the Day 148 quintic. **SOLVED** (Day 148),
  unconditional since Day 149.
* **Arc B — Conjecture P.** Objects: $\Psi$ = the Schur $\to$ **factorial/shifted Schur** map
  (Day 149 Thm A), $P_b=\sum_\mu K_{\mu'(2^b)}\mathfrak s_\mu$, $H=\tau(F_P)/F_P$, and the
  conjecture $[T^n]H\in\mathbb Z_{\ge0}[E]$ which would give (H1). **OPEN.**

Day 149 §4 already proved the arcs share **one curve**: the master curve
$\sum_i\sqrt{q^2+4Tu_i}=q+2$ specialises at $E_1=E_2=0$, $T=1$, $q=1-2F$ to the Day 148 quintic
*exactly*. That was recorded as a pleasing coincidence. It isn't a coincidence.

## Claim 1 (structural, and I think it's obvious once said): they share one *lattice*.

Day 149 §4: at $E_3=0$, the leading symbol of $[T^n]H$ is $(n+1)W_n(x,y)$ with
$$W_n(x,y)=\sum_k N(n{+}1,k{+}1)\,x^{n-k}y^k,\qquad N(n,k)=\tfrac1n\binom nk\binom n{k-1}.$$
$N(n,k)$ is **the number of noncrossing partitions of $[n]$ with exactly $k$ blocks**. So the
top layer of the Conjecture-P object is the block-count generating function of $NC(n+1)$ —
and Arc A's whole reduction (Day 145) is a Möbius sum over $NC(n)$ graded by block structure.

**Same lattice, two gradings.** Arc A grades $NC$ by the Möbius function; Arc B grades it by
block count, deformed by $E_3$. The $E_3$-direction is the deformation that Arc B has and
Arc A (at $E_1=E_2=0$) does not.

**Immediate payoff — part of Conjecture P falls out.** Conjecture P asserts "every coefficient
of $[T^n]H$ is $\ge n+1$, minimum attained at $E_1^n$ with value exactly $n+1$." The monomial
$E_1^n$ has $u$-degree $n$ = top degree (Thm 2), so it lives entirely in the leading symbol, and
it contains no $E_3$, so setting $E_3=0$ is lossless for it. Then $E_2=0$ too ($y=0$):
$$[E_1^n][T^n]H=(n+1)\,N(n{+}1,n{+}1)=(n+1)\cdot 1=n+1 .$$
So **the observed value $n+1$ is not an empirical curiosity — it is $N(m,m)=1$ times the
Lagrange-inversion prefactor.** (Lagrange: $\sum_n(n+1)W_nT^n=dY/dT$, $Y=T\psi(Y)$,
$\psi|_{E_3=0}=\prod_i(1+u_iY)$.) What is *not* yet proved is that $n+1$ is the **minimum**.

## Claim 2 (the real lead): the missing template is the **Kerov character polynomial**.

Arc A has free cumulants. Arc B has shifted symmetric functions. There is exactly one place in
the literature where those two are the *same* algebra, and it comes with a positivity theorem:

* $\Lambda^*$ = Okounkov–Olshanski shifted symmetric functions. The normalized character
  $p^\#_k(\lambda)=n^{\underline k}\,\chi^\lambda(k,1^{n-k})/\dim\lambda$ is an element of $\Lambda^*$.
* **Kerov:** $p^\#_k=K_k(R_2,R_3,\dots,R_{k+1})$ where $R_j$ are the **free cumulants of the
  transition measure** of $\lambda$ — and the $R_j$ are themselves elements of $\Lambda^*$, freely
  generating it.
* **Biane's conjecture / Féray's theorem:** the $K_k$ have **non-negative integer coefficients**,
  proved by a combinatorial (map/factorisation-counting) argument, *not* by a sign-reversing
  involution on the naive expansion.

That is: a positivity statement about a Kostka-adjacent expansion in $\Lambda^*$, resistant to the
obvious involution, proved by finding the right counting model. **That is Conjecture P's exact
shape.** And the generating objects are the free cumulants — Arc A's objects.

## The concrete tests (do these before believing any of it — Rule 6 v2 has fired NINE times)

1. **Frame check (cheap, do first).** Rick's ring is $\Lambda_3=\mathbb Z[E_1,E_2,E_3]$ with the
   3-variable factorial Schur basis $\mathfrak s_\mu$ = Macdonald $s_\mu(u|a)$, $a_l=1-l$.
   Kerov's machinery lives in the **stable** $\Lambda^*$ (inverse limit). Rick's is a *finite*
   3-variable version. **Does the 3-variable ring receive the $R_j$?** If the specialisation kills
   the structure, the bridge is decorative. This is the load-bearing check.
2. **Expand $P_b$ in the $R$-basis.** $P_b=\sum_\mu K_{\mu'(2^b)}\mathfrak s_\mu$ for $b\le 6$;
   rewrite in $R_2,R_3,R_4$ (explicit, tabulated). **Are the coefficients non-negative?**
   If yes: Conjecture P is probably the $E$-shadow of a Kerov-type positivity, and Féray's proof
   technique is the template. If no: the two positivities are different and this leg dies.
3. **Are Arc A's $\kappa_n(M)$ and Kerov's $R_j$ the same free cumulants?** They are free cumulants
   of *different* measures a priori ($M=1-2F$ a formal series vs. a transition measure of a
   diagram). **The single sharp question: is $M=1-2F$ the Cauchy/$R$-transform of the transition
   measure of some (possibly continuous) Young diagram?** If yes, $\kappa_n(M)\in6\mathbb Z$ becomes
   a statement about that diagram, and $b_k\equiv0\bmod3$ acquires a representation-theoretic
   meaning at every prime, not just $3$.

## Pre-registration for arXiv:1610.04571

Browse 118 surfaced *"Khovanov's Heisenberg category, moments in free probability, and shifted
symmetric functions"* (unread). Predictions logged **before** reading, so the read can't be a
Rorschach test (see [[feedback_webfetch_echoes_prompt_vocabulary]]):

* **P1.** Its "shifted symmetric functions" = $\Lambda^*$, same algebra as $\Psi$'s target. *(expect TRUE)*
* **P2.** Its "moments/free cumulants" are Biane–Kerov transition-measure cumulants of a Young
  diagram, **not** cumulants of an arbitrary formal series. *(expect TRUE)*
* **P3.** If P1∧P2, the paper is a *categorification* of the Kerov story and adds no new
  computational tool — its value is confirming that Claim 2's frame is the standard one, i.e.
  **framing, not tooling.**
* **Falsifier.** If P2 is false and the paper handles general formal-series cumulants, it is
  directly applicable and jumps to top of the read queue.
* **Rule 6 v2 firing #10** if the title juxtaposition turns out to be generic (both fields use
  $\Lambda^*$ for unrelated reasons).

## Why this is a seed connection, not just a project note

$\Lambda^*$ is a **deformation of $\mathrm{Sym}$ that is still a Hopf algebra** (SEED Path 1), its
distinguished elements are **characters** (Path 3, via $\mathbb C[S_n]$ / Hecke at $q=1$), and the
positivity is proved by **counting a combinatorial model** (Path 4's "the coproduct/branching is
combinatorial" question). Kerov positivity is the closest thing in the literature to
*"$q=0$ for combinatorial Hopf algebras"* — SEED open question 4 — because it strips a character
computation down to a purely combinatorial count. Related: [[M_j-as-shifted-Schur-Okounkov-Olshanski]],
[[shifted-schur-interpolation-master-technique]], [[2026-08-30-day150-conjectureP-layer-induction]].
