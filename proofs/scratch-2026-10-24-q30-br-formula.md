# Scratch 2026-10-24 — Q30 vs Buch–Ravikumar K-Pieri (p = 1)

**Grade: SKETCHED** (hand proof below + exhaustive machine check n ≤ 6; not refereed, not committed).

Source: Buch–Ravikumar, *Pieri rules for the K-theory of cominuscule Grassmannians*, arXiv 1005.2605
(Crelle 668 (2012)), `.tex` fetched to `/tmp/br/kpieri.tex` 2026-10-24. Numbering reconstructed from the
source (theorem counter per section, shared; equations numbered globally): §4 = OG, §5 = LG.
Section 4: Lemma 4.1 chopB, Lemma 4.2 fiberB, Prop 4.3, Cor 4.4, Lemma 4.5 vanishB, Cor 4.6 (symmetry),
Thm 4.7 pieriBrec, Cor 4.8 pieriBtab, Ex 4.9. Section 5: Lemma 5.1, 5.2, Prop 5.3, Cor 5.4, Thm 5.5,
Cor 5.6, Ex 5.7, 5.8. Equations: h-def = (7), h-rel = (8), dual classes = (9), $\mathcal B$-sum = (10),
$\mathcal C$-sum = (11). Page numbers not checked (no PDF compiled).

---

## 1. BR statements, verbatim

### 1a. Conventions (§4, used also in §5)

Indexing/shape convention (§4):

> When we are working in the context of the maximal orthogonal Grassmannian $X = \OG(n,2n+1)$, we will
> identify a strict partition $\la = (\la_1 > \dots > \la_\ell > 0)$ with its {\em shifted Young diagram}.
> The $i$-th row in this diagram contains $\la_i$ boxes, which are preceded by $i-1$ unused positions. The
> boxes of the staircase partition $\rho_n = (n,n-1,\dots,1)$ thus correspond to the upper-triangular
> positions in an $n\times n$ matrix. If $\mu$ is a strict partition with $\mu_1 \leq n$, then the
> $n$--dual partition $\mu^\vee$ consists of the parts of $\rho_n$ which are not parts of $\mu$. We have
> $X^\la(E_\bull) \cap X^\mu(E^\op_\bull) \neq \emptyset$ if and only if $\la \subset \mu^\vee$. In this
> case the shifted skew diagram $\theta = \mu^\vee/\la$ is obtained by removing the boxes of $\la$ from the
> upper-left corner of $\rho_n$ and the boxes of $\mu$ from the lower-right corner, after mirroring $\mu$
> in the south-west to north-east antidiagonal. [...]
> The set of leftmost boxes of $\rho_n$ are called {\em diagonal boxes}.

Schubert varieties are **codimension-indexed**: $X^\la(F_\bull) = \{ V \in X \mid \dim(V \cap
F_{n+1-\la_i}) \geq i ~\forall i\}$, $\cO^\la=[\cO_{X^\la}]$, special classes $\cO^p$; $c^\nu_{\la,p}$ is
the coefficient of $\cO^\nu$ in $\cO^\la\cdot\cO^p$.

Rim, $N$, $N'$, $d$ (§4, just before Lemma 4.2):

> The {\em south-east rim\/} of the shifted skew diagram $\theta$ is the set of boxes $B \in \theta$ such
> that no box of $\theta$ is located strictly south and strictly east of $B$. Let $\wb\theta$ denote the
> diagram obtained by removing the south-east rim from $\theta$. We say that $\theta$ is a {\em rim\/} if
> $\wb\theta = \emptyset$. Let $d(\theta) = |\theta| - |\wb\theta|$ be number of boxes in the south-east
> rim. Let $N(\theta)$ denote the number of connected components of the diagram $\theta$, where two boxes
> are connected if they share a side. Set $N^-(\theta) = \max(N(\theta)-1,0)$. For use with the Lagrangian
> Grassmannian, we also let $N'(\theta)$ be the number of components that do not contain any diagonal
> boxes.

$h$ (eq. (7)):

> $h(a,b) = \sum_{j=0}^b\, (-1)^j\, 2^{a-j}\, \binom{a}{j}$. Here we set $\binom{a}{j} = 0$ unless
> $0 \leq j \leq a$. Notice that for $b \geq a$ we have $h(a,b) = (2-1)^a = 1$.

South-east corners (§4, before eq. (10)):

> A south-east corner of the shifted skew shape $\theta$ is any box $B$ of $\theta$ such that $\theta$ does
> not contain a box directly below or directly to the right of $B$. Let $\theta'$ be the skew shape obtained
> by removing the south-east corners of $\theta$.

North-east arm (§4, before Thm 4.7):

> If $\theta$ is a non-empty rim, then we define the {\em north-east arm\/} of $\theta$ to be the largest row
> or column that can be obtained by intersecting $\theta$ with a square whose upper-right box agrees with the
> upper-right box of $\theta$. We let $\wh\theta$ be the diagram obtained by removing the north-east arm from
> $\theta$. Notice that $\theta$ is a row or a column if and only if $\wh\theta = \emptyset$.

### 1b. LG(n,2n), §5

Prop 5.3 (proved): $\euler{X}(\cO_\theta \cdot \cO^p) = h(N'(\theta), d(\theta)-p)$ for $0\le p\le n$.

Eq. (11) and Cor 5.4 (proved, from Prop 5.3 + duality $\euler{X}(\cO_\nu^*\cO^\mu)=\delta_{\nu\mu}$):

> $\cC(\theta,p) = \sum_{\theta' \subset \varphi \subset \theta} (-1)^{|\theta|-|\varphi|}\,
> h(N'(\varphi), d(\varphi)-p)$ where the sum is over all shifted skew diagrams $\varphi$ obtained by
> removing a subset of the south-east corners from $\theta$.
>
> **Cor 5.4.** Let $\la \subset \nu$ be strict partitions with $\nu_1 \leq n$ and let $0 \leq p \leq n$.
> Then $c^\nu_{\la,p} = \cC(\nu/\la, p)$.

**Thm 5.5** (pieriCrec, proved in BR):

> Let $\theta$ be a shifted skew diagram and let $p \in \Z$. If $\theta$ is not a rim then
> $\cC(\theta,p)=0$. If $p \leq 0$ then $\cC(\theta,p) = \delta_{\theta,\emptyset}$, and
> $\cC(\emptyset,p)$ is equal to one if $p\leq 0$ and is zero otherwise. If $\theta \neq \emptyset$ is a rim
> and $p>0$, then $\cC(\theta,p)$ is determined by the following rules, with $a = |\theta|-|\wh\theta|$.
> (i) If $\wh\theta = \emptyset$ and $\theta$ meets the diagonal, then we have $\cC(\theta,p) =
> \delta_{p,|\theta|} - \delta_{p,|\theta|-1}$ if $\theta$ is a column, and $\cC(\theta,p) =
> \delta_{p,|\theta|}$ otherwise.
> (ii) If $\wh\theta = \emptyset$ and $\theta$ is disjoint from the diagonal, then $\cC(\theta,p) = 2\,
> \delta_{p,|\theta|} - \delta_{p,|\theta|-1}$.
> (iii) If $\wh\theta \neq \emptyset$ and the north-east arm of $\theta$ is connected to $\wh\theta$, then
> we have $\cC(\theta,p) = \cC(\wh\theta,p-a) - \cC(\wh\theta,p-a+1)$.
> (iv) Finally assume that $\wh\theta \neq \emptyset$ and the north-east arm of $\theta$ is not connected to
> $\wh\theta$. If $a=1$ then $\cC(\theta,p) = 2\, \cC(\wh\theta,p-a) - 2\, \cC(\wh\theta,p-a+1)$, while if
> $a>1$ we have $\cC(\theta,p) = 2\, \cC(\wh\theta,p-a) - 3\, \cC(\wh\theta,p-a+1) +
> \cC(\wh\theta,p-a+2)$.

KLG-tableaux and **Cor 5.6** (pieriCtab):

> Let $\theta$ be a rim. A {\em KLG-tableau\/} of shape $\theta$ is a labeling of the boxes of $\theta$ with
> elements from the ordered set $\{1'<1<2'<2<\cdots\}$ such that (i) each row of $\theta$ is strictly
> increasing from left to right; (ii) each column of $\theta$ is strictly increasing from top to bottom;
> (iii) each box containing an unprimed integer must be larger than or equal to all boxes southwest of it,
> (iv) each box containing a primed integer must be smaller than or equal to all boxes southwest of it, and
> (v) no diagonal box contains a primed integer. If $\theta$ is not a rim, then there are no KLG-tableaux of
> shape $\theta$. The content of a KLG-tableau is the set of integers $i$ such that some box contains $i$ or
> $i'$. **The proof of the following corollary is similar to Corollary~\ref{cor:pieriBtab} and left to the
> reader.**
>
> **Cor 5.6.** The constant $c^\nu_{\la,p}$ for $K(\LG(n,2n))$ is equal to $(-1)^{|\nu/\la|-p}$ times the
> number of KLG-tableaux of shape $\nu/\la$ with content $\{1,2,\dots,p\}$.

### 1c. OG(n,2n+1), §4

Cor 4.4: $c^\nu_{\la,p} = \cB(\nu/\la,p)$, $\cB$ = eq. (10) = eq. (11) with $N^-$ in place of $N'$.
Thm 4.7 (recursion, (i) row/column: $\delta_{|\theta|,p}$; (ii) connected arm: $\cB(\wh\theta,p-a) -
\cB(\wh\theta,p-a+1)$; (iii) disconnected: $0$ if $p<a$, else $(2-\delta_{p,a})(\cB(\wh\theta,p-a) -
\cB(\wh\theta,p-a+1)) + (1-\delta_{a,1})(\cB(\wh\theta,p-a+2)-\cB(\wh\theta,p-a+1))$).

> Let $\theta$ be a rim. A {\em KOG-tableau\/} of shape $\theta$ is a labeling of the boxes of $\theta$ with
> positive integers such that (i) each row of $\theta$ is strictly increasing from left to right; (ii) each
> column of $\theta$ is strictly increasing from top to bottom; and (iii) each box is either smaller than or
> equal to all the boxes south-west of it, or it is greater than or equal to all the boxes south-west of it.
>
> **Cor 4.8.** The constant $c^\nu_{\la,p}$ for $K(\OG(n,2n+1))$ is equal to $(-1)^{|\nu/\la|-p}$ times the
> number of KOG-tableaux of shape $\nu/\la$ with content $\{1,2,\dots,p\}$.

In the proof of Cor 4.8 BR check only one case: "**The remaining cases are left to the reader.**"
So: Cor 4.8 partly reader-left, Cor 5.6 entirely reader-left. Prop 5.3, Cor 5.4, Thm 5.5 (and the §4 twins)
are proved in the paper.

---

## 2. Rick's side and the elementary reduction

Setup: $X_\kappa = X^{\kappa^\vee}$ (dimension-indexed), $c_\rho$ = coefficient of $[\cO_{X_\rho}]$ in
$[\cO_{X_\kappa}]\cdot\cO^1$, i.e. $c_\rho = c^{\rho^\vee}_{\kappa^\vee,1}$. $\theta=\kappa/\rho$, order
$a\le b$ iff $a$ weakly NW of $b$. This is exactly what `brpieri.pieri_dim` computes.

**Reflection.** $\rho^\vee/\kappa^\vee = R(\kappa/\rho)$ with $R(r,c)=(n+1-c,n+1-r)$ (BR's own description:
$\mu^\vee/\la$ = staircase minus $\la$ NW minus mirrored $\mu$ SE; apply with $\la=\kappa^\vee$,
$\mu=\rho$, and $\kappa^\vee$ = staircase minus mirrored $\kappa$). $R$ fixes the diagonal setwise and
**reverses** the NW order. So "strict order-preserving $\theta\to\{e<o\}$, diagonal $=e$" becomes, on
$\theta_{BR}=\nu/\la$, "strict order-preserving $\theta_{BR}\to\{1'<1\}$, diagonal $=1$" (identify $e\mapsto 1$,
$o\mapsto 1'$). Machine-confirmed in q30.py (`reflok`).

**Reduction (hand proof).** Let $P$ be a finite poset, $D\subseteq P$ ("diagonal"), and count strict
order-preserving $f:P\to\{e<o\}$ with $f|_D=e$.
- A 3-chain $x<y<z$ needs three distinct values: count $0$.
- If $d\in D$ and $x<d$: $f(x)<f(d)=e$ impossible: count $0$.
- Otherwise ($P$ has height $\le 2$, no diagonal element is non-minimal): every non-isolated $x$ is either
  non-maximal (then $f(x)=e$ forced) or non-minimal (then $f(x)=o$ forced), not both; these forced values
  satisfy all relations and are compatible with $D$ (a non-isolated diagonal element is minimal, forced
  $e$). Isolated elements are free unless in $D$. Count $=2^{\#\{\text{isolated }x\notin D\}}$. ∎

Shifted-shape simplification: in $\kappa/\rho$ a diagonal box $(c,c)$ can only be above $(c-1,c)$ (nothing
lies to its left in row $c$; a smaller box strictly NW forces $(c-1,c)\in\theta$ by convexity, giving a
3-chain anyway). So the support condition is: **no 3-chain, and no diagonal box $(c,c)\in\theta$ with
$(c-1,c)\in\theta$.**

---

## 3. Comparison with BR at p = 1

### 3a. Translation of Cor 5.6 at p = 1 (route (i), one line modulo Cor 5.6)

Content $\{1\}$ ⇒ labels in $\{1',1\}$. Then:
- (iii) is vacuous (1 is the largest label), (iv) vacuous (1' is the smallest), under either reading
  (weak/strict) of "southwest".
- (i),(ii): strict increase along rows and columns.
- (v): diagonal boxes = 1.
- rim condition.

**Lemma (rim ⟺ no strictly-NW–SE pair; such a pair gives a 3-chain).** Let $a=(r,c)$, $b=(r',c')\in\nu/\la$
with $r<r'$, $c<c'$. Right ends of rows of a shifted strict $\nu$ are weakly decreasing, so $(r,c')\in\nu$;
$(r,c)\notin\la$ and rows of $\la$ are initial segments, so $(r,c')\notin\la$. Thus $a<(r,c')<b$ is a
3-chain in $\theta$. Hence: non-rim ⇒ Rick count 0 = BR count 0; rim ⇒ comparable pairs are exactly
same-row/same-column pairs, so "strict on rows and columns" = "strict order-preserving". ∎

So for every $\theta_{BR}$: #KLG(content {1}) = #strict maps $\to\{1'<1\}$ with diagonal $=1$ = Rick's count
on $R^{-1}\theta_{BR}=\kappa/\rho$, and $c_\rho=(-1)^{|\theta|-1}\cdot$count. The support statement
"$c_\rho\neq 0$ iff count $\neq 0$" is then trivial (sign is a unit). The closed form $2^{\#\text{isolated
off-diagonal}}$ is §2.

### 3b. Avoiding the reader-left Cor 5.6: check the count against Thm 5.5 at p = 1 (route (ii))

At $p=1$, using $\cC(\wh\theta,q)=0$ for $q\le 0$, $\wh\theta\ne\emptyset$, Thm 5.5 becomes:
(i) diagonal row/column: column $|\theta|=1\mapsto 1$, $=2\mapsto -1$, else $0$; row: $1$ iff $|\theta|=1$.
(ii) off-diagonal row/column: $|\theta|=1\mapsto 2$, $=2\mapsto -1$, else 0.
(iii) connected arm: $a=1$: $-\cC(\wh\theta,1)$; $a\ge2$: $0$.
(iv) disconnected arm: $a=1$: $-2\cC(\wh\theta,1)$; $a=2$: $+\cC(\wh\theta,1)$; $a\ge3$: $0$.

Let $T(\theta)=(-1)^{|\theta|-1}K(\theta)$, $K$ = #labelings (rows/cols strict, diag unprimed). Facts used:
rows and columns of a shifted skew shape are intervals; a diagonal box is leftmost in its row and lowest in
its column; the upper-right box $B=(r,c)$ has maximal column, nothing above/right of it; its only possible
neighbours are $L=(r,c-1)$, $D=(r+1,c)$; $L,D$ cannot both be in a rim ($D$ strictly SE of $L$).
- (i)/(ii): direct (diagonal leftmost of a row ⇒ a diagonal row of length ≥2 needs a primed diagonal box ⇒
  $K=0$; diagonal at bottom of a 2-column gets 1, fine). ✓
- (iv): disconnected ⇒ no box of $\psi$ shares a row/column with $\wh\theta$ (interval property), and
  $\psi$ is off-diagonal when $\wh\theta\ne\emptyset$ (a diagonal box in $\psi$ forces every box of
  $\wh\theta$ into a column/row of $\psi$, hence adjacency). Comparabilities in a rim are row/column only,
  so $K(\theta)=K(\psi)K(\wh\theta)$ with $K(\psi)=2,1,0$ for $a=1,2,\ge3$; signs give
  $T(\theta)=(-1)^aK(\psi)T(\wh\theta)$ = $-2T,\,+T,\,0$. ✓
- (iii), $a=1$: exactly one of $L$, $D$ is in $\theta$ and the SW square corner $S=(r+1,c-1)$ is in
  $\theta$ (else the 2-square meets $\theta$ in a row/column, $a\ge2$). If $L\in\theta$: $L$ above $S$ ⇒
  $L=1'$ already forced in $\wh\theta$, and $B=1$ forced. If $D\in\theta$: $S$ left of $D$ ⇒ $D=1$ forced in
  $\wh\theta$, $B=1'$ forced, and $B$ is off-diagonal ($c\ge r+1$). So $K(\theta)=K(\wh\theta)$,
  $T(\theta)=-T(\wh\theta)$. ✓
- (iii), $a=2$: arm $\{L,B\}$ (resp. $\{B,D\}$); connection cannot go through $D$ (resp. $L$) or $S$ (they'd
  be in the 2-square), so it goes through $(r,c-2)$ (resp. $(r+2,c)$): a row (column) of 3 ⇒ $K=0$. ✓
  $a\ge3$: arm itself has 3 in a row/column ⇒ $K=0$. ✓
- non-rim: both 0; $\theta=\emptyset$ excluded ($\rho\subsetneq\kappa$).

Same induction on $|\theta|$ as BR's, so $T(\theta)=\cC(\theta,1)=c^\nu_{\la,1}$ using only proved BR
results (Thm 5.5). This is the p = 1 case of the reader-left Cor 5.6, done by hand. (Grade: sketched —
the arm case analysis should get one cold re-read.)

### 3c. OG twin (Cor 4.8 at p = 1)

Content $\{1\}$, positive integers ⇒ all boxes labeled 1; strict rows/columns ⇒ ≤1 box per row and column;
plus rim ⇒ $\theta$ is an antichain (lemma 3a), (iii) vacuous. So $c=(-1)^{|\theta|-1}$ iff $\theta$ is an
antichain, else 0. In $\kappa/\rho$ orientation $\theta$ is an up-set of $P_\kappa$, and an up-set is an
antichain iff it is a set of maximal elements: support = nonempty subsets of corners of $P_\kappa$,
$|c|=1$ — exactly the q30.py OG output. (Cor 4.8 is also partly reader-left; Thm 4.7 at $p=1$ gives the
same by the analogous check: (i) $\delta_{|\theta|,1}$, (ii) $a=1$: $-\cB(\wh\theta,1)$, (iii) $a=1$:
$\cB(\theta,1)= -\cB(\wh\theta,1)$, $a\ge2$: $0$ — not written out.)

---

## 4. Machine checks

`brpieri.py` (wake252/caseB) implements **Cor 5.4 + eq. (11)** literally: SE corners, $\theta'$, sum
over subsets, $N'$ = components without diagonal boxes, $d$ = |SE rim|, $h(a,b)=0$ for $b<0$. That is the
*proved* formula (not the reader-left Cor 5.6, not Thm 5.5). Indexing: dimension-indexed $X_\kappa =
X^{\kappa^\vee}$, coefficient of $X_\rho$ = $\cC(\rho^\vee/\kappa^\vee,1)$. Matches the verbatim theorem.

New script `scripts/wake254/q30/brcheck.py`: over **all** shifted skew $\nu/\la\subseteq\rho_n$ (not just
those q30 meets), compares (A) eq. (11) $\cC(\theta,1)$, (B) $(-1)^{|\theta|-1}\#$KLG (definition (i)–(v)
implemented literally, incl. (iii)/(iv)), (C) Rick's closed form on $R^{-1}\theta$:

| n | shapes | A=B | A=C |
|---|---|---|---|
| 2 | 6 | 6 | 6 |
| 3 | 27 | 27 | 27 |
| 4 | 110 | 110 | 110 |
| 5 | 430 | 430 | 430 |
| 6 | 1652 | 1652 | 1652 |

## 5. Hand examples (κ/ρ orientation, n=3; all agree with `pieri_dim`)

- κ=(1): θ={(1,1)} diagonal isolated ⇒ 1. $X_1\cdot\cO^1=X_\emptyset$.
- κ=(2): ρ=(1): {(1,2)} isolated off-diag ⇒ +2; ρ=∅: chain (1,1)<(1,2), diag minimal ⇒ −1.
  $2X_1-X_\emptyset$.
- κ=(3): ρ=(2): +2; ρ=(1): 2-chain ⇒ −1; ρ=∅: 3-chain ⇒ 0. $2X_2-X_1$.
- κ=(2,1): ρ=(2): {(2,2)} ⇒ +1; ρ=(1): (1,2)<(2,2), diagonal non-minimal ⇒ 0; ρ=∅: 3-chain ⇒ 0. $X_2$
  (whole LG(2,4) times hyperplane = divisor ✓).
  BR side for ρ=(1), n=2: ν/λ=(2)/∅ is a row whose left box is diagonal ⇒ must be 1′ ⇒ forbidden ⇒ 0 ✓.
- κ=(3,1): ρ=(3): +1; ρ=(2,1): {(1,3)} ⇒ +2; ρ=(2): {(1,3),(2,2)} incomparable, (2,2) diag forced ⇒ −2;
  ρ=(1): (1,2)<(2,2) ⇒ 0; ρ=∅ ⇒ 0. $X_3+2X_{21}-2X_2$.
  h-sum check for ρ=(2): θ_BR={(1,3),(2,2)}, both SE corners, θ'=∅:
  $h(1,1)-h(1,0)-h(0,0)+0 = 1-2-1=-2$ ✓; KLG: (2,2)=1, (1,3)∈{1′,1} ⇒ 2, sign − ✓.
- κ=(3,2,1): only ρ=(3,2) survives ⇒ $X_{32}$ ✓.
- (n=4) κ=(4,2), ρ=(2): θ={(1,3),(1,4),(2,2),(2,3)}, height 2, no isolated ⇒ −1 ✓; ρ=(3,1):
  {(1,4),(2,3)} two isolated ⇒ −4 ✓.

## 6. Verdict

Q30 (|c_ρ| = strict {e<o}-fillings with diagonal = e; support) is a **one-line translation** of BR
Cor 5.6 at p = 1 once one notes (a) the antidiagonal reflection reverses the order and swaps e/o into
1/1′, (b) conditions (iii)/(iv) are vacuous at p = 1, (c) rim ⟺ no strictly-SE pair, and such a pair
yields a 3-chain by convexity. The only soft spot: Cor 5.6's proof is "left to the reader" in BR. Section 3b
closes that at p = 1 by a short case check against the proved Thm 5.5 (and the proved Cor 5.4 formula is
machine-matched for all shapes n ≤ 6). No real obstacle found. Same for the OG twin (Cor 4.8, also
partly reader-left).
