# Type-uniform lift of the short-long-edge tensor product rule to $B_n$

**Rick, 2026-05-17. Deep work session on PROVE.md Sub-problem 5.**

> The $B_2$ proof had the right shape. Lifting it is a relabeling argument plus
> a "the other chains aren't there" observation. Two beers, no whiskey, done.

## Headline

**Theorem (type-uniform tensor product rule).** *Let $\mathfrak{g}$ be of type
$B_n$, $n \geq 2$. The restriction of $\mathrm{Kp}(\infty)$ to the action of
the short-simple ι-coideal generator $B_n = F_n + \zeta E_n K_n^{-1}$ admits a
tensor product decomposition*
$$
\mathrm{Kp}(\infty)\big|_{B_n\text{-action}} \;\cong\; \bigotimes_{a=1}^{n-1}\mathcal{C}_a \;\otimes\; \mathcal{C}_{\mathrm{sing}}
$$
*as ι-crystals, where*
- *$\mathcal{C}_a$ ($a = 1, \ldots, n-1$) is the **chain factor** with three
  generators $(c_{\mathrm{mid}_a}, c_{\mathrm{bot}_a}, c_{\mathrm{top}_a})$ and
  internal bracket block*
  $$
  \mathrm{br}(\mathcal{C}_a)(M, B, T) \;=\; )^{M}_{E_a}\; (^{2B}_{E_a - E_n}\; )^{2T}_{E_a + E_n}\; (^{M}_{E_a},
  $$
- *$\mathcal{C}_{\mathrm{sing}} \cong \mathbb{K}[B_n]$ is the **singleton
  factor** with internal bracket block $)^{S}_{E_n}$.*

*Both factor families are uniformly defined in $n$, and the tensor product
agrees with $\mathrm{Kp}(\infty)|_{B_n}$ as a graded vector space and as an
ι-crystal under the $B_n$-action. The on-slice $e_n^2$ catalog of the tensor
product is the $\binom{2n}{2} = n(2n-1)$-move catalog with three-class split
$3(n-1)\;+\;2(n-1)(n-2)\;+\;(2n-1)$ matching the empirical catalogs at $B_2,
B_3, B_4, B_5$.*

The conditions PROVE.md asks for are proved:

| Condition | Status | Note |
|---|---|---|
| (C1n) Per-node compatibility | ✓ | $\mathcal{C}_{\mathrm{sing}}$ = Watanabe §4.1 split-node verbatim. $\mathcal{C}_a$ is the new building block extending Watanabe past (S1)–(S3)'. |
| (C3n) On-slice catalog | ✓ | §5 below; verified at $B_2, B_3, B_4, B_5$ in `proofs/2026-05-17-multiorbit-aug-b5/`. |
| (C4n) Type-uniform | ✓ | §6 wrap. No per-rank ansatz; all dependence on $n$ is arithmetic. |

(C2) — external iSerre shadow — is dropped. Day-19 refuted it on
locality-vs-quadratic-growth grounds (`c2-iserre-cross-chain-REFUTED.md`).

---

## 1. Setup

$\mathfrak{g}$ of type $B_n$, $n \geq 2$, simple roots $\alpha_1, \ldots,
\alpha_n$ with $\alpha_a = E_a - E_{a+1}$ long for $a < n$ and $\alpha_n = E_n$
short. The Cartan matrix entry $a_{n-1, n} = -2$ is the short-long edge that
fails Watanabe arXiv:2110.07177 (S1)–(S3)'.

Positive roots $\Phi^+(B_n)$ partition under the $\alpha_n$-action into:

- **Chains** $\mathrm{Chain}(a) := \{E_a - E_n,\;E_a,\;E_a + E_n\}$ for
  $a \in \{1, \ldots, n-1\}$ — length-3 $\alpha_n$-strings (bot, mid, top).
- **Singleton** $\mathrm{Sing} := \{E_n\}$ — length-1 string ($\alpha_n$ itself).
- **Non-touching** $\mathrm{NT} := \{E_a \pm E_b : 1 \leq a < b < n\}$ —
  length-1 $\alpha_n$-strings with $\langle E_a \pm E_b, \alpha_n^\vee\rangle = 0$
  and $E_a \pm E_b \pm \alpha_n \notin \Phi^+$. These play no role in the
  $B_n$-action (Remark 4.3 below).

The CST bracketing $S_n(\pi)$ for the short simple (per CST Def 2.14 / `b_i_b{n}.py`):
$$
S_n(\pi) \;=\; \Bigl[\,)^{c_{\mathrm{mid}_a}}_{E_a}\; (^{2 c_{\mathrm{bot}_a}}_{E_a - E_n}\; )^{2 c_{\mathrm{top}_a}}_{E_a + E_n}\; (^{c_{\mathrm{mid}_a}}_{E_a}\,\Bigr]_{a = 1}^{n-1}\; )^{c_{E_n}}_{E_n}.
$$

Chain blocks appear in **convex order of the mid root** $E_a$ (chain 1 first,
then chain 2, ..., then chain $n-1$); the singleton block is last. Non-touching
roots contribute no symbols.

Cancellation: repeatedly delete any adjacent `(` immediately followed by `)`,
across factor-block boundaries. The canonical $S_n^c(\pi)$ has all surviving
`)`s left of all surviving `(`s. $\varepsilon_n(\pi)$ = # surviving `)`,
$\varphi_n(\pi)$ = # surviving `(`. The action $e_n$: replace the rightmost
surviving `)` (with label $\beta$) by $e_{\beta - \alpha_n}$ (or remove if
$\beta = \alpha_n$). The action $f_n$: leftmost surviving `(` analogously.

The slice $S_n := \{\pi : \varepsilon_n(\pi) \geq 2\}$. The "catalog" $C_n :=
\{e_n^2(\pi) - \pi : \pi \in S_n\}$ as multiplicity-difference vectors.

---

## Phase A — Chain factor uniformity

**Definition A.1 (chain factor).** For each $a \in \{1, \ldots, n-1\}$, the
*chain factor* is the $\mathbb{Z}_{\geq 0}^3$-graded vector space
$$
\mathcal{C}_a \;:=\; \mathbb{K}\bigl\langle (M, B, T) : M, B, T \in \mathbb{Z}_{\geq 0}\bigr\rangle
$$
on three generators labeled $\mathrm{mid}_a = E_a$, $\mathrm{bot}_a = E_a - E_n$,
$\mathrm{top}_a = E_a + E_n$. Its internal bracket block is
$$
\mathrm{br}(\mathcal{C}_a)(M, B, T) \;=\; )^{M}_{E_a}\; (^{2B}_{E_a - E_n}\; )^{2T}_{E_a + E_n}\; (^{M}_{E_a}.
$$

**Lemma A.2 (structural uniformity in $a$).** For all $a, a' \in \{1, \ldots, n-1\}$
and all $n \geq 2$, $\mathcal{C}_a$ and $\mathcal{C}_{a'}$ are isomorphic as
graded vector spaces, and their bracket blocks have identical shape (four
sub-blocks of widths $M, 2B, 2T, M$ with bracket types $),(,),(\,$); only the
*labels* on the bracket symbols differ.

*Proof.* The graded vector space structure is the same polynomial ring on
three generators (no $a$-dependence). The bracket block depends on
- the *local Cartan data* at chain $a$: pairings of $\alpha_n^\vee = 2 E_n$
  with the three chain roots,
  $$
  \langle E_a - E_n, \alpha_n^\vee\rangle = -2,\quad
  \langle E_a, \alpha_n^\vee\rangle = 0,\quad
  \langle E_a + E_n, \alpha_n^\vee\rangle = +2,
  $$
- and *chain position* (top/mid/bot), reading off the standard Kashiwara
  signature of a length-3 $\alpha_n$-string:
  - $\mathrm{top}$ has $\langle\cdot,\alpha_n^\vee\rangle = +2$ → contributes
    `)^{2T}` per multiplicity $T$;
  - $\mathrm{bot}$ has $\langle\cdot,\alpha_n^\vee\rangle = -2$ → contributes
    `(^{2B}` per multiplicity $B$;
  - $\mathrm{mid}$ has $\langle\cdot,\alpha_n^\vee\rangle = 0$ → contributes
    both `)^M` (leading) and `(^M` (trailing) per multiplicity $M$, with
    bot-`(`s and top-`)`s sandwiched between them.

Both pieces of data — the local pairing values $(-2, 0, +2)$ and the chain
position — depend ONLY on the *type* of the root (long $E_a \pm E_n$ vs short
$E_a$) and its $\alpha_n^\vee$-pairing, not on the index $a$ itself. Hence
$\mathrm{br}(\mathcal{C}_a)$ is the same shape for every $a$, with only the
labels relabeled $a \to a'$. ∎

**Remark A.3 (mid-framing comes from $\langle\mathrm{mid}, \alpha_n^\vee\rangle = 0$).**
The "mid framing" $)^M \ldots (^M$ enclosing the bot-(s and top-)s is the
bracket-level encoding of the fact that the chain middle is *fixed* by the
short reflection $s_n$, while having an $\alpha_n$-string of length 3 (i.e.,
$\mathrm{mid} \mp \alpha_n \in \Phi^+$). The mid contributes both raising
(`(`) and lowering (`)`) capacity per multiplicity, but at different positions
in the local order; the leading mid-`)`s are bracket-precedent and the
trailing mid-`(`s are bracket-subsequent, sandwiching the bot/top pair.

**Remark A.4 (doubling is exactly $a_{n,a} = -2$).** The 2× counts on the
bot-(s and top-)s are the bracket-level expression of the short-long entry
$|a_{n,a}| = 2$ (with $a_{n,a} = \langle\alpha_a^\vee, \alpha_n\rangle = -2$
for $a = n-1$, and equivalently $\langle E_a \pm E_n, \alpha_n^\vee\rangle = \pm 2$
for any $a < n$). Watanabe's framework handles $|a_{ij}| \leq 1$; this
doubling is the new ingredient.

---

## Phase B — Tensor product as ι-crystal

**Definition B.1 (tensor product bracket).** Given chain factors
$\mathcal{C}_1, \ldots, \mathcal{C}_{n-1}$ and the singleton factor
$\mathcal{C}_{\mathrm{sing}}$, the tensor product
$\mathcal{T}_n := \bigotimes_{a=1}^{n-1}\mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$
is the $\mathbb{Z}_{\geq 0}^{3(n-1) + 1}$-graded vector space whose
$((M_a, B_a, T_a)_{a=1}^{n-1}, S)$-component has bracket
$$
\mathrm{br}_{\mathcal{T}_n}\bigl((M_a, B_a, T_a)_a, S\bigr)
\;=\;
\mathrm{br}(\mathcal{C}_1)(M_1, B_1, T_1)\;\cdot\;\mathrm{br}(\mathcal{C}_2)(M_2, B_2, T_2)\;\cdots\;\mathrm{br}(\mathcal{C}_{n-1})(M_{n-1}, B_{n-1}, T_{n-1})\;\cdot\;\mathrm{br}(\mathcal{C}_{\mathrm{sing}})(S),
$$
i.e., string concatenation in convex chain order followed by the singleton.

The ι-crystal operators on $\mathcal{T}_n$:
- $\varepsilon_n$: # surviving `)` in $\mathrm{cancel}(\mathrm{br}_{\mathcal{T}_n})$.
- $\varphi_n$: # surviving `(` in $\mathrm{cancel}(\mathrm{br}_{\mathcal{T}_n})$.
- $e_n$: act on the rightmost surviving `)` (label $\beta$); update the
  factor multiplicity by $-e_\beta + e_{\beta - \alpha_n}$ if $\beta \neq
  \alpha_n$, or $-e_{\alpha_n}$ otherwise.
- $f_n$: act on the leftmost surviving `(` analogously.
- $B_n = e_n + f_n$ at $q = 0$.

**Theorem B.2 (identification with $\mathrm{Kp}(\infty)|_{B_n}$).** The map
$$
\iota:\ \mathcal{T}_n \;\to\; \mathrm{Kp}(\infty)\big|_{B_n\text{-action}},\quad
((M_a, B_a, T_a)_a, S) \;\mapsto\; \sum_{a=1}^{n-1} \bigl(M_a E_a + B_a (E_a - E_n) + T_a (E_a + E_n)\bigr) + S\, E_n
$$
identifies $\mathcal{T}_n$ with the chain+singleton sector of $\mathrm{Kp}(\infty)$
as a graded vector space, and intertwines $\mathrm{br}_{\mathcal{T}_n}$ with the
CST bracketing $S_n(\pi)$.

*Proof.* The graded vector space identification is by reading off
multiplicities: $\iota$ is bijective onto the sub-lattice of $\mathrm{Kp}(\infty)$
spanned by the chain and singleton roots, with each factor's $\mathbb{Z}_{\geq 0}^3$
(or $\mathbb{Z}_{\geq 0}$) coordinate corresponding directly to multiplicities
of the three chain roots (or the singleton root).

The bracket intertwining: $\mathrm{br}_{\mathcal{T}_n}$ is the string concatenation
of chain-$a$ blocks $)^{M_a} (^{2B_a} )^{2T_a} (^{M_a}$ in convex order of $a$,
followed by the singleton block $)^S$. The CST bracketing $S_n(\pi)$ from §1 is
EXACTLY the same string concatenation, with $(M_a, B_a, T_a, S) = (c_{\mathrm{mid}_a},
c_{\mathrm{bot}_a}, c_{\mathrm{top}_a}, c_{E_n})$. The cancellation rule
("repeatedly delete adjacent `(`,`)`") is the same on both sides — bracket
labels are inert under cancellation. The action of $e_n, f_n$ via
rightmost/leftmost surviving bracket is CST Def 2.14. Hence $\iota$ intertwines
the bracket structures and the crystal actions on the nose. ∎

**Remark B.3 (non-touching roots).** $\mathrm{Kp}(\infty)$ has additional
factors for non-touching roots $E_a \pm E_b$ ($a < b < n$), each a 1-dim
ι-crystal under $B_n$-action with $e_n = f_n = 0$. These are TRIVIAL tensor
factors that we omit from $\mathcal{T}_n$ above; including them adds $(n-1)(n-2)/2 + (n-1)(n-2)/2 = (n-1)(n-2)$ trivial factors. They participate in the
long-simple actions $B_a$ ($a < n$), but are irrelevant to the short-simple
$B_n$ action that is the subject of this theorem.

**Remark B.4 (ι-crystal axioms).** $\mathcal{T}_n$ satisfies the ι-crystal
axioms relative to $B_n$ because (by Theorem B.2) it is isomorphic to
$\mathrm{Kp}(\infty)$ — which carries the Kashiwara crystal of $U_q^-(B_n)$, and
in particular the ι-crystal structure under $B_n$-action obtained by restricting
the full Kashiwara crystal. The substantive content of Definition B.1 is not
that $\mathcal{T}_n$ is an ι-crystal — that follows tautologically from the
CST identification — but that the ι-crystal structure FACTORIZES through chain-
and singleton-factor data with the explicit bracket-concatenation rule. This
factorization is the content beyond Watanabe Props 5.1.1 + 5.1.3, which
provide such a factorization only for simply-laced edges ($a_{ij} \in \{0, -1\}$
satisfying (S1)–(S3)').

**Lemma B.5 (Watanabe per-node match for the singleton).** $\mathcal{C}_{\mathrm{sing}}
\cong \mathbb{K}[B_n]$ as an ι-crystal, matching Watanabe arXiv:2110.07177 §4.1
split-node rank-1 ι-crystal $U^i_i = \mathbb{K}[B_i]$ at $a_{i, \tau(i)} = 2$.

*Proof.* The generator is the polynomial generator $B_n$. The lowering
operator $e_n$ is "decrement exponent"; the raising operator $f_n$ is
"increment exponent". The bracket is $)^S$ which gives $\varepsilon_n = S$,
$\varphi_n = 0$; this is Watanabe's split-node bracket. The ι-coideal generator
$B_n = e_n + f_n$ acts as $S \mapsto S - 1$ plus $S \mapsto S + 1$, which is
Watanabe's split-node $\mathrm{sgn}(s_n)$-action. ∎

**Note B.6 (chain factor as new building block).** The chain factor
$\mathcal{C}_a$ is NOT one of Watanabe's per-node ι-crystals — Watanabe's
framework has no rank-3 building block, only rank-1 per-node objects glued by
simply-laced edges. $\mathcal{C}_a$ is the *new* short-long-edge building
block needed at $a_{n-1, n} = -2$. Its structure (3 generators with the
specific bracket block of Definition A.1) is precisely the data needed to
extend Watanabe's tensor product rule across the short-long edge.

---

## Phase C — On-slice catalog factor-by-factor

Recall (Lemma 2.1 of `2026-05-15-three-strand-braid-Bn.md`) that the $2n - 1$
*step types* are
$$
\{\mathrm{MB}(a) : 1 \leq a \leq n-1\} \;\cup\; \{\mathrm{TM}(a) : 1 \leq a \leq n-1\} \;\cup\; \{\mathrm{Sing}\},
$$
with net deltas
$\delta_{\mathrm{MB}(a)} = -e_{E_a} + e_{E_a - E_n}$,
$\delta_{\mathrm{TM}(a)} = -e_{E_a + E_n} + e_{E_a}$,
$\delta_{\mathrm{Sing}} = -e_{E_n}$.

In the tensor-product framing of §B, each step type corresponds to a
*per-factor primitive operator*:

| Factor | Per-factor primitives | Catalog name |
|---|---|---|
| $\mathcal{C}_a$ ($a < n$) | $e_n^{\mathcal{C}_a}: (M,B,T) \to \begin{cases}(M+1, B, T-1) & T > B \\ (M-1, B+1, T) & T \leq B, M > 0\end{cases}$ | TM(a) and MB(a) respectively |
| $\mathcal{C}_{\mathrm{sing}}$ | $e_n^{\mathcal{C}_{\mathrm{sing}}}: S \to S - 1$ | Sing |

The chain factor $\mathcal{C}_a$ contributes 2 primitives (MB(a), TM(a)) per
chain; the singleton contributes 1 (Sing). Total: $2(n-1) + 1 = 2n - 1$ step
types, in bijection with per-factor primitives.

**Definition C.1 (factor incidence of a pair).** An unordered pair (with
repetition) $\{p, q\}$ of step types has a *factor incidence* — the multiset
of factors $\{\mathrm{fac}(p), \mathrm{fac}(q)\}$ where $\mathrm{fac}(\mathrm{MB}(a))
= \mathrm{fac}(\mathrm{TM}(a)) = \mathcal{C}_a$ and $\mathrm{fac}(\mathrm{Sing})
= \mathcal{C}_{\mathrm{sing}}$.

The three structural classes:
- **Intra-chain**: $\mathrm{fac}(p) = \mathrm{fac}(q) = \mathcal{C}_a$ for some
  $a$.
- **Cross-chain**: $\mathrm{fac}(p) = \mathcal{C}_a \neq \mathcal{C}_b = \mathrm{fac}(q)$,
  both chains.
- **Singleton-involving**: at least one of $\mathrm{fac}(p),
  \mathrm{fac}(q)$ is $\mathcal{C}_{\mathrm{sing}}$.

**Counts:**
- Intra-chain: 3 unordered pairs per chain (MM, TT, MT) × $(n-1)$ chains $= 3(n-1)$.
- Cross-chain: 4 unordered pairs per chain pair ($\{p_a, p_b\}$ with $p_a \in
  \{$MB(a), TM(a)$\}$, $p_b \in \{$MB(b), TM(b)$\}$) × $\binom{n-1}{2}$ pairs
  $= 4 \cdot \binom{n-1}{2} = 2(n-1)(n-2)$.
- Singleton-involving: $\{$Sing, Sing$\}$ + $\{$Sing$, p\}$ for $p \in $
  $\{$MB(a), TM(a) : $1 \leq a \leq n-1\}$ = $1 + 2(n-1) = 2n - 1$.

Sum: $3(n-1) + 2(n-1)(n-2) + (2n-1) = (n-1)(2n-1) + (2n-1) = n(2n-1) = \binom{2n}{2}$. ✓

**Theorem C.2 (factor-by-factor realisation of the catalog).** For each
unordered pair $\{p, q\}$ of step types, there is a Kostant partition
$\pi_{p,q} \in S_n$ supported on the factor(s) of $p, q$ such that
$e_n^2(\pi_{p,q}) - \pi_{p,q} = \delta_p + \delta_q$.

The witnesses are uniform in their parameters:

| Class | Pair $\{p, q\}$ | Witness $\pi_{p, q}$ | Support |
|---|---|---|---|
| intra ($a$) | $\{$MB(a), MB(a)$\}$ | $2 E_a$ | $\mathcal{C}_a$: $(M, B, T) = (2, 0, 0)$ |
| intra ($a$) | $\{$TM(a), TM(a)$\}$ | $2(E_a + E_n)$ | $\mathcal{C}_a$: $(0, 0, 2)$ |
| intra ($a$) | $\{$MB(a), TM(a)$\}$ | $E_a + (E_a + E_n)$ | $\mathcal{C}_a$: $(1, 0, 1)$ |
| cross ($a < b$) | $\{$MB(a), MB(b)$\}$ | $E_a + 2 E_b$ | $\mathcal{C}_a$: $(1, 0, 0)$, $\mathcal{C}_b$: $(2, 0, 0)$ |
| cross ($a < b$) | $\{$MB(a), TM(b)$\}$ | $E_a + (E_b + E_n)$ | $\mathcal{C}_a$: $(1, 0, 0)$, $\mathcal{C}_b$: $(0, 0, 1)$ |
| cross ($a < b$) | $\{$TM(a), MB(b)$\}$ | $(E_a + E_n) + E_b$ | $\mathcal{C}_a$: $(0, 0, 1)$, $\mathcal{C}_b$: $(1, 0, 0)$ |
| cross ($a < b$) | $\{$TM(a), TM(b)$\}$ | $(E_a + E_n) + E_a + (E_b + E_n)$ | $\mathcal{C}_a$: $(1, 0, 1)$, $\mathcal{C}_b$: $(0, 0, 1)$ |
| sing | $\{$Sing, Sing$\}$ | $2 E_n$ | $\mathcal{C}_{\mathrm{sing}}$: $S = 2$ |
| sing-chain ($a$) | $\{$Sing, MB(a)$\}$ | $E_a + 2 E_n$ | $\mathcal{C}_a$: $(1, 0, 0)$, $\mathcal{C}_{\mathrm{sing}}$: $S = 2$ |
| sing-chain ($a$) | $\{$Sing, TM(a)$\}$ | $(E_a + E_n) + E_n$ | $\mathcal{C}_a$: $(0, 0, 1)$, $\mathcal{C}_{\mathrm{sing}}$: $S = 1$ |

In every row, all factors NOT named in the "Support" column have multiplicity zero.

*Proof.* We give the bracket-level argument for each class.

### (i) Intra-chain ($p, q$ both in $\mathcal{C}_a$)

Witness $\pi$ has zero multiplicity on all chains $c \neq a$ and zero
singleton. Hence $S_n(\pi)$ reduces to the chain-$a$ block alone (plus possibly
nothing else): $)^{M}_{E_a}\; (^{2B}_{E_a - E_n}\; )^{2T}_{E_a + E_n}\;
(^{M}_{E_a}$.

- **MM (witness $2 E_a$, $(M,B,T) = (2,0,0)$):** Bracket $)^2_{E_a}\,
  (^2_{E_a}$. Cancel? No `(` followed by `)` adjacency yet (the `(`s are AFTER
  the `)`s). $\varepsilon_n = 2$. Step 1: rightmost `)` is $)_{E_a}$ → MB(a),
  $\pi' = E_a + (E_a - E_n)$. After step, $(M, B, T) = (1, 1, 0)$, bracket
  $)_{E_a}\, (^2_{E_a - E_n}\, (_{E_a}$, no cancellation, $\varepsilon_n = 1$.
  Step 2: rightmost `)` is $)_{E_a}$ → MB(a), $\pi'' = 2(E_a - E_n)$. Net delta
  $-2 e_{E_a} + 2 e_{E_a - E_n} = 2 \delta_{\mathrm{MB}(a)}$. ✓
- **TT (witness $2(E_a + E_n)$, $(0,0,2)$):** Bracket $)^4_{E_a + E_n}$.
  $\varepsilon_n = 4$. Step 1: rightmost `)` is top → TM(a), $\pi' = (E_a +
  E_n) + E_a$, $(M, B, T) = (1, 0, 1)$, bracket $)_{E_a}\, )^2_{E_a + E_n}\,
  (_{E_a}$. Cancel positions 3,4 ($(_{E_a}$ has nothing after it, so no cancel).
  $\varepsilon_n = 3$. Step 2: rightmost `)` is top → TM(a), $\pi'' = 2 E_a$.
  Net delta $-2 e_{E_a + E_n} + 2 e_{E_a} = 2 \delta_{\mathrm{TM}(a)}$. ✓
- **MT (witness $E_a + (E_a + E_n)$, $(1,0,1)$):** Bracket $)_{E_a}\, )^2_{E_a + E_n}\, (_{E_a}$. $\varepsilon_n = 3$. Step 1: rightmost `)` is top → TM(a),
  $\pi' = 2 E_a$, $(M, B, T) = (2, 0, 0)$, same as MM case after one step.
  Step 2: rightmost `)` is mid → MB(a), $\pi'' = E_a + (E_a - E_n)$. Net delta
  $-e_{E_a + E_n} + e_{E_a - E_n} = \delta_{\mathrm{TM}(a)} + \delta_{\mathrm{MB}(a)}$. ✓

These witnesses are uniform in $a$ — the same construction in $a$ works for
every $a \in \{1, \ldots, n-1\}$ since chain factors are structurally identical
(Phase A) and the chain-$a$ block is isolated in $S_n(\pi)$ when all other
chain multiplicities are zero. The bracket-level argument depends only on the
chain-$a$ block's $(M, B, T)$, not on the label $a$.

### (ii) Cross-chain ($p \in \mathcal{C}_a$, $q \in \mathcal{C}_b$ with $a < b$)

Witness $\pi$ has zero multiplicity on all chains $c \neq a, b$ and zero
singleton. Hence $S_n(\pi)$ reduces to (chain-$a$ block)·(chain-$b$ block):
$$
S_n(\pi) \;=\; \underbrace{)^{M_a} (^{2 B_a} )^{2 T_a} (^{M_a}}_{\text{chain } a}\;\cdot\;\underbrace{)^{M_b} (^{2 B_b} )^{2 T_b} (^{M_b}}_{\text{chain } b},
$$
with chain-$a$ labels $E_a, E_a \pm E_n$ and chain-$b$ labels $E_b, E_b \pm E_n$.
The intermediate chains $c$ with $a < c < b$ contribute NO symbols (their
multiplicities are zero), so chain-$a$'s trailing $(^{M_a}_{E_a}$ is
directly followed by chain-$b$'s leading $)^{M_b}_{E_b}$ in the bracket
string, REGARDLESS OF WHETHER $a, b$ ARE ADJACENT.

The cross-cancellation engine: $(^{M_a}_{E_a}$ adjacent to $)^{M_b}_{E_b}$
cancels $\min(M_a, M_b)$ pairs across the chain-$a$/chain-$b$ boundary. After
this, the bracket reorganizes; the rightmost surviving `)` and the second
rightmost surviving `)` belong to chain-$a$ and chain-$b$ in a pattern
determined by the residual multiplicities.

**Direct verification of the 4 cases at general $(a, b)$ with $a < b$:**

- **MM (witness $E_a + 2 E_b$):** chain-$a$ $(M, B, T) = (1, 0, 0)$:
  $)_{E_a}\, (_{E_a}$. Chain-$b$ $(M, B, T) = (2, 0, 0)$: $)^2_{E_b}\, (^2_{E_b}$.
  Full: $)_{E_a}\, (_{E_a}\, )^2_{E_b}\, (^2_{E_b}$. Cross-cancel position 2-3
  (chain-$a$'s mid-`(` × chain-$b$'s first mid-`)`): $)_{E_a}\, )_{E_b}\,
  (^2_{E_b}$. $\varepsilon_n = 2$. Step 1: rightmost `)` is $)_{E_b}$ → MB(b),
  $\pi' = E_a + E_b + (E_b - E_n)$. Bracket: $)_{E_a}\, (_{E_a}\, )_{E_b}\,
  (_{E_b}\, (^2_{E_b - E_n}$. Cross-cancel 2-3: $)_{E_a}\, (_{E_b}\, (^2_{E_b - E_n}$. $\varepsilon_n = 1$. Step 2: rightmost `)` is $)_{E_a}$ → MB(a),
  $\pi'' = (E_a - E_n) + E_b + (E_b - E_n)$. Net delta $\delta_{\mathrm{MB}(a)} + \delta_{\mathrm{MB}(b)}$. ✓

- **MT (witness $E_a + (E_b + E_n)$):** chain-$a$ $(1, 0, 0)$:
  $)_{E_a}\, (_{E_a}$. Chain-$b$ $(0, 0, 1)$: $)^2_{E_b + E_n}$. Full:
  $)_{E_a}\, (_{E_a}\, )^2_{E_b + E_n}$. Cancel position 2-3: $)_{E_a}\,
  )_{E_b + E_n}$. $\varepsilon_n = 2$. Step 1: rightmost `)` is top of $b$ →
  TM(b), $\pi' = E_a + E_b$. Bracket: $)_{E_a}\, (_{E_a}\, )_{E_b}\, (_{E_b}$.
  Cross-cancel 2-3: $)_{E_a}\, (_{E_b}$. $\varepsilon_n = 1$. Step 2: rightmost
  `)` is $)_{E_a}$ → MB(a), $\pi'' = (E_a - E_n) + E_b$. Net delta
  $\delta_{\mathrm{MB}(a)} + \delta_{\mathrm{TM}(b)}$. ✓

- **TM (witness $(E_a + E_n) + E_b$):** chain-$a$ $(0, 0, 1)$:
  $)^2_{E_a + E_n}$. Chain-$b$ $(1, 0, 0)$: $)_{E_b}\, (_{E_b}$. Full:
  $)^2_{E_a + E_n}\, )_{E_b}\, (_{E_b}$. No cross-cancellation possible (no
  `(` followed by `)`). $\varepsilon_n = 3$. Step 1: rightmost `)` is
  $)_{E_b}$ → MB(b), $\pi' = (E_a + E_n) + (E_b - E_n)$. Bracket: $)^2_{E_a + E_n}\, (^2_{E_b - E_n}$. No cancellation. $\varepsilon_n = 2$. Step 2: rightmost
  `)` is top of $a$ → TM(a), $\pi'' = E_a + (E_b - E_n)$. Net delta
  $\delta_{\mathrm{TM}(a)} + \delta_{\mathrm{MB}(b)}$. ✓

- **TT (witness $(E_a + E_n) + E_a + (E_b + E_n)$):** chain-$a$ $(M, B, T) =
  (1, 0, 1)$: $)_{E_a}\, )^2_{E_a + E_n}\, (_{E_a}$. Chain-$b$ $(0, 0, 1)$:
  $)^2_{E_b + E_n}$. Full: $)_{E_a}\, )^2_{E_a + E_n}\, (_{E_a}\, )^2_{E_b + E_n}$.
  Cross-cancel position 4-5 ($(_{E_a}$ against $)_{E_b + E_n}$): $)_{E_a}\,
  )^2_{E_a + E_n}\, )_{E_b + E_n}$. $\varepsilon_n = 4$. Step 1: rightmost `)`
  is $)_{E_b + E_n}$ → TM(b), $\pi' = (E_a + E_n) + E_a + E_b$. Chain-$a$
  $(1, 0, 1)$ unchanged; chain-$b$ now $(1, 0, 0)$: $)_{E_b}\, (_{E_b}$. Full:
  $)_{E_a}\, )^2_{E_a + E_n}\, (_{E_a}\, )_{E_b}\, (_{E_b}$. Cross-cancel 4-5
  ($(_{E_a}$ against $)_{E_b}$): $)_{E_a}\, )^2_{E_a + E_n}\, (_{E_b}$.
  $\varepsilon_n = 3$. Step 2: rightmost `)` is top of $a$ → TM(a), $\pi'' =
  2 E_a + E_b$. Net delta $\delta_{\mathrm{TM}(a)} + \delta_{\mathrm{TM}(b)}$. ✓

**Empirical confirmation at $B_5$.** The witness construction with $a, b$ replacing
$1, 2$ in the $B_3$ template was tested on all $\binom{4}{2} = 6$ chain pairs
at $B_5$ (including the non-adjacent pairs $(1,3), (1,4), (2,4)$) by direct
computation in `proofs/remark47/coideal_check/b_i_b5.py`. All 24 = 4 × 6
cross-chain witnesses produce the predicted net delta. See verification log
at `proofs/2026-05-17-short-long-tensor-rule-Bn-verification.txt` for the
full output (all 45 = 12 intra + 9 sing + 24 cross witnesses).

The cross-chain mechanism is type-uniform: the bracket-level argument depends
ONLY on the local interaction between chain-$a$'s trailing mid-`(`s and
chain-$b$'s leading mid-`)`s, with all other chains contributing zero symbols
to the bracket. Hence the construction lifts verbatim from $B_3$ to general
$B_n$ at every chain pair.

### (iii) Singleton-involving (one of $p, q$ is Sing)

Witness $\pi$ has support on $\mathcal{C}_{\mathrm{sing}}$ and possibly one
chain $\mathcal{C}_a$ (for the "Sing + chain primitive" entries); other chains
have zero multiplicity.

- **SS (witness $2 E_n$, $S = 2$, all chains empty):** Bracket $)^2_{E_n}$.
  $\varepsilon_n = 2$. Step 1: $)_{E_n}$ → Sing, $\pi' = E_n$. Step 2: $)_{E_n}$
  → Sing, $\pi'' = 0$. Net delta $-2 e_{E_n} = 2 \delta_{\mathrm{Sing}}$. ✓
- **Sing + MB(a) (witness $E_a + 2 E_n$):** Chain-$a$ $(1, 0, 0)$: $)_{E_a}\,
  (_{E_a}$. Singleton: $)^2_{E_n}$. Full: $)_{E_a}\, (_{E_a}\, )^2_{E_n}$.
  Cross-cancel position 2-3: $)_{E_a}\, )_{E_n}$. $\varepsilon_n = 2$. Step 1:
  rightmost `)` is $)_{E_n}$ → Sing, $\pi' = E_a + E_n$. Bracket: $)_{E_a}\,
  (_{E_a}\, )_{E_n}$. Cancel 2-3: $)_{E_a}$. $\varepsilon_n = 1$. Step 2:
  $)_{E_a}$ → MB(a), $\pi'' = (E_a - E_n) + E_n$. Net delta $-e_{E_a} +
  e_{E_a - E_n} - e_{E_n} = \delta_{\mathrm{MB}(a)} + \delta_{\mathrm{Sing}}$. ✓
- **Sing + TM(a) (witness $(E_a + E_n) + E_n$):** Chain-$a$ $(0, 0, 1)$:
  $)^2_{E_a + E_n}$. Singleton: $)_{E_n}$. Full: $)^2_{E_a + E_n}\, )_{E_n}$.
  No cancellation. $\varepsilon_n = 3$. Step 1: rightmost `)` is $)_{E_n}$ →
  Sing, $\pi' = E_a + E_n$. Bracket: $)^2_{E_a + E_n}$. $\varepsilon_n = 2$.
  Step 2: rightmost `)` is top → TM(a), $\pi'' = E_a$. Net delta $-(E_a + E_n)
  + E_a - E_n = \delta_{\mathrm{TM}(a)} + \delta_{\mathrm{Sing}}$. ✓

Uniform in $a$ by the same isolation argument.

**Completeness of the catalog.** We have realized all $\binom{2n}{2} = n(2n-1)$
unordered pairs of step types. By the injectivity lemma (Lemma 2.2 of
`2026-05-15-three-strand-braid-Bn.md`), distinct multisets of step types yield
distinct net deltas. Hence the catalog $C_n$ contains the $\binom{2n}{2}$
distinct vectors listed above; and by Theorem 4.1(i) of three-strand-braid (every
catalog entry IS a sum of two step deltas), $|C_n| \leq \binom{2n}{2}$. Equality. ∎

**Remark C.3 (each class lives at a distinct factor incidence).** The three
classes are characterized precisely by their factor incidence: intra-chain =
"both step deltas come from per-factor primitives of the SAME $\mathcal{C}_a$";
cross-chain = "from DISTINCT $\mathcal{C}_a, \mathcal{C}_b$"; singleton =
"at least one from $\mathcal{C}_{\mathrm{sing}}$". This is the structural
content of the three-class decomposition under the tensor product framing —
the classes correspond to which tensor factors the two $e_n$-steps "touch."

**Remark C.4 (cross-chain as tensor product interaction term).** Intra-chain
entries can be computed entirely within one factor (the witness lives in
$\mathcal{C}_a$ alone). Singleton-involving entries couple $\mathcal{C}_{\mathrm{sing}}$
with at most one $\mathcal{C}_a$, but their non-trivial behavior reduces to
a single cross-factor cancellation between two factors. Cross-chain entries
are the GENUINE *tensor product interaction term* — they require two distinct
chain factors $\mathcal{C}_a, \mathcal{C}_b$ to be jointly nontrivial, with
the bracket cross-cancellation between chain-$a$'s trailing mid-`(`s and
chain-$b$'s leading mid-`)`s providing the coupling that makes the two
$e_n$-steps land on different chain factors.

This justifies the Day-19 closure of the iSerre correspondence: the cross-chain
class is NOT a shadow of any external algebraic object (the iSerre relation
is local with constant monomial count, while cross-chain count is quadratic in
$n$). Instead, it is the INTRINSIC tensor-product interaction term of
$\bigotimes_a \mathcal{C}_a$, with the bracket-cross-cancellation mechanism
providing its structural origin.

---

## Phase D — Type-uniformity wrap

The construction is uniform in $n$ at every step:

**(D1) Factor structure (Phase A).** $\mathcal{C}_a$ is defined identically
for every $a \in \{1, \ldots, n-1\}$ and every $n \geq 2$; its bracket block
depends on the local pairings $(-2, 0, +2)$ of chain roots with $\alpha_n^\vee$
and the chain position (top/mid/bot), neither of which depend on $a$ or $n$.
$\mathcal{C}_{\mathrm{sing}} = \mathbb{K}[B_n]$ is Watanabe's split-node
ι-crystal, uniform in $n$.

**(D2) Tensor product (Phase B).** $\mathcal{T}_n = \bigotimes_{a=1}^{n-1}\mathcal{C}_a
\otimes \mathcal{C}_{\mathrm{sing}}$ has $n - 1$ chain factors and 1 singleton,
with bracket-concatenation in convex order. The identification with $\mathrm{Kp}(\infty)|_{B_n}$
holds for all $n \geq 2$ by Theorem B.2, since the CST bracketing is itself
type-uniform.

**(D3) Catalog (Phase C).** The witnesses in Theorem C.2 are functions of
$(a, b, n)$ via the chain labels $E_a, E_a \pm E_n$ etc.; the bracket-level
computation depends only on the local bracket block structures (uniform by
(D1)) and on the chains-not-named-having-zero-multiplicity argument (uniform
because the bracket is empty wherever a chain has no support). No $n$-specific
ansatz appears.

**(D4) Counts.** The arithmetic $\binom{2n}{2} = n(2n-1) = 3(n-1) + 2(n-1)(n-2) + (2n-1)$
is identity in $n$, with each summand identified with a factor-incidence
class. No combinatorial ansatz beyond the factor decomposition.

**Theorem D.1 (type-uniform main theorem).** The tensor product decomposition
$$
\mathrm{Kp}(\infty)\big|_{B_n\text{-action}} \;\cong\; \bigotimes_{a=1}^{n-1}\mathcal{C}_a \;\otimes\; \mathcal{C}_{\mathrm{sing}}
$$
holds as ι-crystals for all $n \geq 2$, with chain factors $\mathcal{C}_a$ and
singleton factor $\mathcal{C}_{\mathrm{sing}}$ defined uniformly in $n$
(Definitions A.1, Lemma B.5), tensor product bracket given by convex-order
chain concatenation followed by singleton block (Definition B.1), and on-slice
$e_n^2$ catalog of size $n(2n-1)$ with the three-class decomposition
$3(n-1) + 2(n-1)(n-2) + (2n-1)$ (Theorem C.2).

*Proof.* Assemble (D1)–(D4) and Theorems A.2, B.2, C.2. ∎

---

## 5. Empirical verification

Empirical confirmation of the catalog count and three-class split:

| Rank $n$ | Catalog size | intra | cross | sing | File |
|---|---|---|---|---|---|
| 2 | 6 | 3 | 0 | 3 | `proofs/2026-05-16-short-long-tensor-rule-B2.md` §5 |
| 3 | 15 | 6 | 4 | 5 | `proofs/2026-05-14-multiorbit-aug-b3/characterize_moves.py` |
| 4 | 28 | 9 | 12 | 7 | `proofs/2026-05-14-multiorbit-aug-b4/characterize_moves_b4.py` |
| 5 | 45 | 12 | 24 | 9 | `proofs/2026-05-17-multiorbit-aug-b5/result.md` |

All four ranks match the predicted $\binom{2n}{2} = n(2n - 1) = 3(n-1) + 2(n-1)(n-2) + (2n - 1)$
formula.

Cross-chain witnesses for ALL chain pairs at $B_5$ (including non-adjacent
$(1, 3), (1, 4), (2, 4)$) computed in this session:

| Chain pair | TT | TM | MT | MM |
|---|---|---|---|---|
| (1, 2) | ✓ | ✓ | ✓ | ✓ |
| (1, 3) | ✓ | ✓ | ✓ | ✓ |
| (1, 4) | ✓ | ✓ | ✓ | ✓ |
| (2, 3) | ✓ | ✓ | ✓ | ✓ |
| (2, 4) | ✓ | ✓ | ✓ | ✓ |
| (3, 4) | ✓ | ✓ | ✓ | ✓ |

All 24 cross-chain witnesses fire with the predicted net delta. The
non-adjacent witnesses use the same construction template as adjacent ones —
the bracket cross-cancellation between chain-$a$'s trailing mid-(s and
chain-$b$'s leading mid-)s works identically regardless of whether $a, b$ are
adjacent in convex order, because intermediate chains contribute zero symbols
when given zero multiplicity in the witness.

---

## 6. Status of conditions

| Condition | Status | Phase | Note |
|---|---|---|---|
| (C1n) Per-node compatibility | ✓ proved | A + B.5 | $\mathcal{C}_{\mathrm{sing}}$ matches Watanabe §4.1 split-node verbatim; $\mathcal{C}_a$ is new building block for $a_{n,a} = -2$, with structurally uniform definition. |
| (C3n) On-slice catalog | ✓ proved | C | All $\binom{2n}{2}$ catalog entries realized factor-by-factor with type-uniform witnesses; verified empirically at $B_2, B_3, B_4, B_5$. |
| (C4n) Type-uniformity | ✓ proved | D | All construction uniform in $n$; no per-rank ansatz; cross-chain witnesses work for all $(a, b)$, adjacent or not. |

---

## 7. The "side check": commutativity ideal hypothesis

PROVE.md flagged a parallel ~30 min side check: whether the $2(n-1)(n-2)$
cross-chain entries correspond to $2 \cdot |\{$ordered pairs $(a, b) : a \neq b\}|
= 2(n-1)(n-2)$ commutators in the commutativity ideal of the long-simple
subalgebra of $U^\iota$.

The count matches: 4 entries per unordered chain pair × $\binom{n-1}{2}$
unordered pairs = $2(n-1)(n-2)$ = 2 × ordered-pair count.

But the most natural structural correspondence — "each cross-chain entry
arises from a specific ordered commutator" — doesn't have a clean obstruction-free
formulation. The 4 entries per unordered $\{a, b\}$ pair are TT, TM, MT, MM,
all with "step 1 lands on the LATER chain" (Observation §10.5 of the Day-18
proof). Hence they all naturally correspond to ONE ordered pair (later, earlier)
= (b, a), not 2 ordered pairs. The factor of 2 doesn't come from convex-order
ordering.

The factor of 2 might come from primitive direction (MB vs TM at the earlier
chain $a$). Each $\{*(a), *(b)\}$ pair has step 1 at chain $b$; the "earlier
chain $a$ primitive" can be MB(a) or TM(a) (2 choices) and the "later chain
$b$ primitive" can be MB(b) or TM(b) (2 choices), giving 4 entries.

Splitting by primitive at chain $a$:
- $\{$MB(a), MB(b)$\}$, $\{$MB(a), TM(b)$\}$: MB at earlier chain. 2 entries per
  unordered pair.
- $\{$TM(a), MB(b)$\}$, $\{$TM(a), TM(b)$\}$: TM at earlier chain. 2 entries per
  unordered pair.

The "primitive at earlier chain" gives a binary classification, and (with the
convex-order ordering selected for "step 1 on later chain") there are
$\binom{n-1}{2}$ unordered chain pairs × 2 primitives at earlier chain ×
2 primitives at later chain = $2(n-1)(n-2)$ entries. The 2 × ordered-pair
match corresponds to: choose an ordered pair $(b, a)$ (i.e., later chain first),
then pick 1 of 2 primitive directions at the earlier chain.

This is internally meaningful but does NOT correspond to a natural action of
the $\binom{n-1}{2} \cdot 2 = (n-1)(n-2)$ ordered pairs $[B_a, B_b]$ —
those are bilinear in pairs of long-simple ι-coideal generators, while cross-chain
entries are decorated by per-chain primitives (MB vs TM), not by which factor
is taken first in a commutator.

**Verdict.** Count match is structural up to the "primitive direction at
earlier chain" factor of 2, but no clean correspondence with $[B_a, B_b]$
commutators emerges. **Drop the side check.** The intrinsic tensor-product
framing (cross-chain class = interaction term of $\bigotimes_a \mathcal{C}_a$)
remains the home, with no external algebraic mirror needed.

This is consistent with the Day-19 calibration: external-shadow conjectures
for the cross-chain class are now refuted at 7 candidate correspondences
(including this one). The shape is hardstop-malformed.

---

## 8. Comparison with Watanabe

Watanabe arXiv:2110.07177 gives:
- §4.1: per-node ι-crystals $U^i_i$, three cases by $a_{i, \tau(i)} \in \{2, 0, -1\}$.
- §5.1: tensor product rule for ι-crystals at simply-laced edges ($a_{ij} \in
  \{0, -1\}$), via Kashiwara signature rules conditioned by (S1)–(S3)'.

At type BDI ($\tau = \mathrm{id}$), every node is split with $a_{i, \tau(i)}
= 2$, so per-node $U^i_i = \mathbb{K}[B_i]$ for all $i$. Watanabe Prop 5.1.1
handles all long-long edges $a_{a, b} = -1$ ($|a - b| = 1$, both $a, b < n$).
The short-long edge $a_{n-1, n} = -2$ is the unique exception: Watanabe Prop
5.1.1 does NOT apply.

**This paper's tensor product rule fills exactly this gap.** Specifically:
- The singleton factor $\mathcal{C}_{\mathrm{sing}}$ IS Watanabe's per-node
  $U^n_n = \mathbb{K}[B_n]$ for the short simple.
- The chain factor $\mathcal{C}_a$ is the NEW building block for the
  short-long-edge tensor product. It is NOT per-node — it bundles three roots
  (bot, mid, top) into one factor, encoding the doubled-bracket pattern that
  the $|a_{n, a}| = 2$ pairing creates.
- The tensor product rule across $\mathcal{C}_a$'s and $\mathcal{C}_{\mathrm{sing}}$
  is the Kashiwara signature rule extended past Watanabe's (S1)–(S3)' restriction.

Schematically: the full type-BDI ι-crystal $\mathrm{Kp}(\infty)|_{U^\iota}$ is
the gluing of (i) Watanabe Prop 5.1.1 at each long-long edge $a_{a, b} = -1$,
(ii) Rick's chain-factor rule at the unique short-long edge $a_{n-1, n} = -2$,
(iii) Watanabe §4.1 per-node $\mathbb{K}[B_i]$ at every split node.

The rule is type-specific (BDI / type B short-simple) but type-UNIFORM within
that scope: every $B_n$ for $n \geq 2$ has the same factorization structure,
with $(n-1)$ chain factors plus 1 singleton, glued by the same
bracket-concatenation rule.

---

## 9. Calibration takeaways

1. **The type-uniform lift is a relabeling argument plus an "other-chains-empty"
   observation.** No new ideas beyond Day-18; the $B_2$ proof had the right
   shape. The lift is essentially: (i) $\mathcal{C}_a$ depends only on local
   Cartan data uniform in $a$, (ii) the convex-order chain concatenation
   makes cross-chain witnesses work by isolating two chains at a time (other
   chains have zero multiplicity → zero bracket contribution → cross-cancellation
   between named chains is local). Together these collapse the type-uniform
   theorem to per-chain bracket arithmetic plus arithmetic in $n$.

2. **Non-adjacent chain pairs work IDENTICALLY to adjacent ones.** This was
   the key worry going in (Pitfall F1 of PROVE.md). It dissolves: the witness
   construction puts zero multiplicity on every chain $c \neq a, b$, so
   intermediate chains contribute no bracket symbols; chain-$a$ trailing mid-(s
   and chain-$b$ leading mid-)s are then ADJACENT in the bracket. The bracket
   cancellation algorithm only cares about adjacency in the (possibly empty
   chains filtered out) string.

3. **Watanabe's framework is the right home.** This proof articulates exactly
   how. The chain factor $\mathcal{C}_a$ is Watanabe's missing building block
   for $a_{ij} = -2$. The tensor product rule is Watanabe's missing 5.1.1
   extension past (S1)–(S3)'. v2 can be written squarely inside the Watanabe
   tradition with the chain factor as the precise additional ingredient.

4. **Pitfall F5 (rule dissolves) did not fire.** It snapped into place in
   ~3h of work, including verification at $B_5$ and full bracket-level
   computations of all witness templates. The structural argument is short
   (Phase A is 1 paragraph + 1 remark; Phase B is 3 statements; Phase C is the
   main content but factorizes cleanly into 3 classes × $\leq 4$ entries
   each).

5. **PROVE.md's Decision Rule path: "Phases A + B + C complete at $B_3$".**
   Met, in fact stronger — Phases A + B + C complete type-uniformly at $B_n$
   with empirical $B_5$ verification of all 24 cross-chain witnesses. v2 main
   theorem in hand.

---

## 10. Files / verification

- This proof: `proofs/2026-05-17-short-long-tensor-rule-Bn.md`.
- Building blocks:
  - $B_2$ proof: `proofs/2026-05-16-short-long-tensor-rule-B2.md` (Day 18 PM,
    starting point).
  - Type-uniform catalog count: `proofs/2026-05-15-three-strand-braid-Bn.md`
    Theorem 4.1, 5.1 (Day 15).
  - $B_3, B_4, B_5$ catalog computations: `proofs/2026-05-14-multiorbit-aug-b{3,4}/`,
    `proofs/2026-05-17-multiorbit-aug-b5/`.
  - Crystal operator implementations: `proofs/remark47/coideal_check/b_i_b{2,3,4,5}.py`.
- Refuted side conjectures (informing strategy): `connections/c2-iserre-cross-chain-REFUTED.md`,
  `connections/aug-tilde-purely-combinatorial-after-four-refutations.md`.
- v2 keystone (this is now upgraded): `connections/short-long-tensor-product-rule.md`.

---

## 11. Gaps

**No gaps in the type-uniform theorem as stated.** The argument is:

1. Phase A — chain factor structure is uniform in $a$ by local Cartan data
   argument. Bracket block shape is determined by chain position and
   $\alpha_n^\vee$-pairing values, both $a$-independent.
2. Phase B — tensor product as ι-crystal is the CST bracketing in disguise
   (Theorem B.2); ι-crystal axioms inherit from CST.
3. Phase C — catalog drops out from per-factor primitives by direct
   bracket-level computation, with type-uniform witnesses verified at $B_5$
   for all $\binom{n-1}{2} = 6$ chain pairs.
4. Phase D — assembling 1–3 gives type-uniform main theorem.

Each phase is constructive and computational; no appeal to deeper structural
theorems (beyond CST and the three-strand braid theorem of 2026-05-15).

**Caveat: ι-crystal axioms cited via CST, not independently verified.** The
proof that $\mathrm{Kp}(\infty)$ carries a valid Kashiwara crystal for $B_n$
is standard (Kashiwara 1994); the ι-coideal generator $B_n = e_n + f_n$
inherits the crystal structure by restriction. This is treated as known input.

**What this proof does NOT do:**
- Doesn't give a category-theoretic justification of why Watanabe's framework
  *should* extend across short-long edges via this chain-factor rule. It
  shows that the rule EXISTS and matches the empirical data; the natural
  abstract framework (perhaps Bao-Wang's ψ-crystal extension to type BDI, or
  Kolb's coideal categorification) is left for future work.
- Doesn't address the long-simple ι-coideal generator actions $B_a$ ($a < n$)
  beyond noting (Remark B.3) that Watanabe Prop 5.1.1 applies at long-long
  edges and our framework is silent there.

---

— Rick, 2026-05-17, post-whiskey, the rule snapped clean
