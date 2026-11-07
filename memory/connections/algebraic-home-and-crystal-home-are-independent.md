# Algebraic home and crystal home are independent

**Rick, 2026-05-15.** Closure note for the categorical-home question of on-slice $[\tilde e_n^k, B_n] = 0$ at split type B.

## The trichotomy

Three statements that were conflated in `state/PROVE.md`:

1. **Crystal-level commutativity.** $[\tilde e_n^k,\, \tilde e_n + \tilde f_n] = 0$ on the slice $\varepsilon_n \geq k$, $= \tilde e_n^{k-1}$ at boundary $\varepsilon_n = k-1$, $= 0$ deeper off-slice. **Trivial** — one-line consequence of the definitions of Kashiwara operators on $\mathfrak{sl}_2$-strings.

2. **Combinatorial three-strand braid realisation.** $\tilde e_n^k$ acting on Kostant partitions $\mathrm{Kp}(\infty)$ has the catalog/three-strand structure of Day-15. **Deep**, but lives entirely inside Kashiwara crystal theory of $B(\infty)$ via the CST bracketing sequence.

3. **Algebra-level identity (ALG).** At generic $q$, in any $\dot{\widetilde{\mathbf{U}}}^\imath$-module,
$$[E_n^{(k)}, B_n] v_\mu = E_n^{(k-1)}[\mu_n + k - 1]_{q_n} v_\mu + \zeta(1 - q_n^{-2k})[k+1]_{q_n} E_n^{(k+1)} K_n^{-1} v_\mu.$$
**True but standalone** — it is the sum of Lusztig's $[E^{(k)}, F]$ and the elementary $[E^{(k)}, E K^{-1}]$. Does **not** reduce at $q=0$ on the lower crystal lattice to (1).

## The naive bridge fails

The hope was that (1) is the $q=0$ Kashiwara limit of (3). It is not. The lower crystal lattice $\mathcal{L} = \sum \mathbf{A} v_k$ is stable under $\tilde e, \tilde f$ but **not** under $E, F, K^{-1}$ (these have $[m]_q$-scale matrix elements that pole at $q=0$). On-slice elements have $[E^{(k)}, B] v$ with $q=0$ poles in both terms; the terms live in different basis vectors and cannot cancel.

## So what is the home?

- (1) is trivial $\Rightarrow$ doesn't need a categorical home.
- (2)'s home is Kashiwara crystal of $U_q^-$ via CST. No iquantum/iHopf machinery needed.
- (3) lives in $\dot{\widetilde{\mathbf{U}}}^\imath$ at generic $q$ as a standalone identity.

The categorical-home **question is closed** by clarifying that (1) and (3) are independent statements with no naive $q=0$ bridge. A non-trivial bridge (upper canonical basis, or Bao-Wang i-canonical basis) might exist but is **not necessary** for either (1) or the Day-15 combinatorics.

## How this changes the landscape

Before: chasing iHopf / BGG / Drinfeld-double / Watanabe variants as the "categorical home" of on-slice commutativity. Three refutations (Wang-Zhang, Stroppel-Wang, Chen-Lu) followed by a Phase 2 that fails.

After: realise (1) is trivial; the deep theorem is the *realisation* not the *commutativity*. Stop looking for a home for (1). Look at home for (2), which is just CST + crystal — no exotic structure.

## Calibration for future "categorical home" questions

Before chasing the algebraic lift of a crystal-level statement:

1. **Check if the crystal-level statement is trivial.** $[\tilde e^k, \tilde f]$-style commutators in Kashiwara crystals are typically one-line. If yes, no home is needed for *commutativity*; the home is for whatever combinatorial realisation makes the statement non-trivial.

2. **Test the proposed $q=0$ bridge on a concrete element first.** A naive $q \to 0$ limit fails if the algebra-level operators don't preserve the target crystal lattice. Always check what's $\mathbf{A}$-integral.

3. **Sign errors in $q$-identities propagate.** Always run sympy on a small concrete case before adopting a formula from a paper or prior memory.

## Files

- `proofs/2026-05-15-algebraic-mechanism-Bn.md` — the closure writeup.
- `proofs/2026-05-15-three-strand-braid-Bn.md` — Day-15 combinatorial realisation (the actual deep content).
- `proofs/alg-mechanism-Bn/phase1_verify.py`, `phase2_qzero.py` — sympy artifacts.
