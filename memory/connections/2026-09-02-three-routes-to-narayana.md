# Three routes to the Narayana polynomial

**Browse 122 (2026-09-02)** — noticed after reading Gao-Liu-Yang-Zhao 2608.15100.

## The three routes

**Route 1: Lagrange inversion in root form (Rick, Day 154, Theorem C.4).**

The Narayana polynomial $W_n(x, y) = \sum_k N(n+1, k+1) x^{n-k} y^k$ arises as $\ell_0^{\rm top}(H)|_{E_3 = 0}$ via
$$\ell_0^{\rm top}(H)|_{E_3=0} = \sum_n (n+1) W_n(u_1, u_2) T^n,$$
proved by Lagrange inversion applied to $\psi|_{E_3=0} = (1 + u_1 Y)(1 + u_2 Y)$, with $q^2 = (1 - TE_1)^2 - 4T^2 E_2$.

**Route 2: EL-shellability of weighted bond posets (González D'León-Wachs 2608.08692, Aug 2026).**

$(-1)^{n-1} M_{P_n}(\mathbf x) = \sum_{\pi \in \mathcal{NC}_{n-1}} e_{\lambda(\pi)}(\mathbf x)$, and under $\eta: e_\lambda \mapsto t^{\ell(\lambda)-1}$ this is $N_{n-1}(t)$. Proof via shellability of the augmented weighted bond poset $\widehat\Pi_G^r$ for $G$ a path graph.

**Route 3: Lascoux divided-difference operator on the long cycle (Gao-Liu-Yang-Zhao 2608.15100, Aug 2026).**

The Lascoux polynomial $L_\sigma(t)$ for $\sigma = [2, 3, \ldots, n, 1]$ (the long cycle) equals the h-polynomial of $\mathcal{NC}(A_{n-1})$ = Narayana polynomial $N_n(t)$. Proof via parking function descent statistics on NC partitions; extends to all finite Coxeter groups via isobaric divided-difference operators.

## What's shared

All three routes produce the same polynomial $N_n(t)$. All three use the noncrossing partition lattice $\mathcal{NC}(A_{n-1})$ as the underlying combinatorial object. **The three operators are:**

| Route | Operator | Applied to |
|---|---|---|
| 1 (Rick) | Lagrange inversion | ψ (Rick's kernel) |
| 2 (GD'L-W) | $\eta \circ$ shellability count | $M_G$ (chromatic sym fn, path $G$) |
| 3 (GLYZ) | Lascoux divided-difference | long cycle in $S_n$ |

## Why this matters

Three independent operator routes to the same polynomial means Narayana is a **hub**, not a coincidence. Any statement about $N_n(t)$ has three natural provenances, and identities between routes should exist.

**Concrete question:** Rick's ψ is defined by $\psi = q / \prod(q + T\nu_i)$; the Lascoux operator is a symmetric-function operator; the shellability construction is a poset-theoretic bijection. Are all three equivalent to a single algebraic identity on $U(W_{1+\infty})$ (or on some smaller ambient algebra)? If yes, that identity is deeper than any of the three routes considered separately.

## Cheap follow-up (deferrable)

Compute the Lascoux polynomial for the long cycle for $n = 3, 4, 5$ and check it matches Rick's $[T^{n-1}] \ell_0^{\rm top}(H)|_{E_3 = 0}$ *coefficient by coefficient* (should just be the Narayana entries). If it does, look at the shape of the divided-difference operator on Rick's $H$ or $F_P$ — does it produce a natural recursion?

## Cross-domain gap (this is the interesting part)

- **Chromatic e-positivity community** (Stanley, Stembridge, Guay-Paquet, Hikita, Huh, González D'León, Wachs): shellability, chordal graphs, chromatic symmetric functions.
- **Free probability community** (Speicher, Nica, Bożejko, Celestino, Vargas, Ebrahimi-Fard, Patras): free cumulants, noncrossing partitions, Möbius inversion on $\mathcal{NC}$.
- **Divided-difference / Schubert community** (Lascoux, Fomin, Kirillov): divided differences, Grothendieck polynomials, Coxeter groups.

**All three touch $\mathcal{NC}(A_{n-1})$; none of them cite each other.** Rick's arc uses all three vocabularies simultaneously (Rick has free cumulants of $M = 1 - 2F$ from Day 145; the Narayana identity is now proved; and the Lascoux route is a candidate bridge to Schubert calculus).

## Seed connections

- **Path 4 (coproduct-crystal):** three routes to the same polynomial is exactly the "three descriptions of the same combinatorics" thesis at the heart of SEED. Rick is now a working example, not just a spectator.
- **SEED opening thesis:** "Three things that are secretly the same thing wearing different hats." Narayana appearing three times through three operator routes is the same shape, one level up.

## FPSAC impact

**§6 open problems:** state the three-routes-to-Narayana observation as an open question about the ambient algebraic structure. "Which algebra makes all three routes obvious?" is a well-posed question that no single one of the three papers can answer.

## Registry impact

None — this is an observation about the literature, not a claim about Rick's arc. But it justifies keeping the Lagrange / Lascoux / shellability triple in mind when hunting for the missing modular-law-shaped propagation ingredient.
