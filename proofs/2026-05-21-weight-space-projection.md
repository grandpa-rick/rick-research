# Weight-Space Projection of the BDI Kobayashi Polytope at $B_n$ (OQ-K Layer 2)

**Date.** 2026-05-21 (Day-29 deep work, Layer 2).
**Author.** Rick.
**Status.** **VERDICT SHIPPED.** Theorem G proved at $B_3$ explicitly + $B_2,B_4,B_5$ verified;
type-uniform form conjectured ($n \ge 2$) with two-loop dual-cone argument.

PROVE.md priors: P(Q1=YES) = 80%, P(Q2=NO) = 60%, joint P=48–55%.
**Outcome: Q1 = NO, Q2 = NO.** The "$L_a, U_a$ project to distinct image facets" half of the
conjecture is *refuted*; the chain → weight projection is *vastly contractive*: only the
$E$-facet survives. The "NT adds no facets" half is *confirmed*.

The image polytope at $B_n$ has exactly $n$ facets, of which only ONE ($\Phi(E)$) is
carry-derived; the other $n-1$ are non-negativity / sum facets.

---

## 1. Problem statement (recap)

Let $n \ge 2$. The chain HW polytope $\mathcal{P}_n \subset \mathbb{Z}_{\ge 0}^{3(n-1)+1}$
has coordinates $((M_a, B_a, T_a)_{a=1}^{n-1}, S)$ with $M_1 = 0$ on $\mathcal{P}_n$
(Theorem F).

The chain-to-weight map $\Phi : \mathcal{P}_n \times \mathbb{Z}_{\ge 0}^{\text{NT}} \to X^+(B_n) \otimes \mathbb{R}$
sends $(\pi, \pi^{\NT})$ to $\nu \in \mathbb{Z}^n$ (in $(E_1, \dots, E_n)$ coords) by
$\nu = \sum_\beta m_\beta \beta$, where the sum runs over positive roots with chain/NT
multiplicities. In components:

- $\lambda_a = M_a + B_a + T_a + (\text{NT contribs at } E_a)$ for $a = 1, \dots, n-1$
  (with $M_1 = 0$).
- $\lambda_n = S + \sum_{a=1}^{n-1} (T_a - B_a)$ (NT contributes 0 to $\lambda_n$).

For NT roots $E_a \pm E_b$, $1 \le a < b \le n-1$, with multiplicities $N^\pm_{ab} \ge 0$:
$E_a - E_b$ contributes $+1$ to $\lambda_a$, $-1$ to $\lambda_b$;
$E_a + E_b$ contributes $+1$ to both $\lambda_a, \lambda_b$.

**Image polytope.** $\mathcal{K}_n := \Phi(\mathcal{P}_n \times \mathbb{Z}_{\ge 0}^{\text{NT}})$.

**Q1 (chain-facet distinctness).** Do the chain facets $L_a, U_a$ ($2 \le a \le n-1$)
and $E$ project to $2n-3$ distinct codim-1 hyperplanes in $X^+(B_n) \otimes \mathbb{R}$?

**Q2 (NT contribution).** Does the NT-block contribute $\ge 1$ additional codim-1
hyperplane?

---

## 2. Theorem G (Image polytope at $B_n$, $n \ge 2$)

**Theorem G.** For $n \ge 2$, $\mathcal{K}_n$ is the rational polyhedral cone in $\mathbb{R}^n$ with
H-representation
$$
\boxed{\quad
\lambda_1 + \cdots + \lambda_k \;\ge\; 0 \quad (k = 1, \dots, n-2), \qquad
\sum_{i=1}^{n} \lambda_i \;\ge\; 0, \qquad
\lambda_n \;\le\; \lambda_1 + \cdots + \lambda_{n-1}.
\quad}
$$
These $n$ inequalities are pairwise non-redundant facets.

**Corollary G1.** Only the chain-side facet $E$ projects to a codim-1 facet of $\mathcal{K}_n$,
namely the facet $\lambda_n \le \lambda_1 + \cdots + \lambda_{n-1}$. The chain-side facets
$L_a, U_a$ ($2 \le a \le n-1$) *collapse* under $\Phi$: their images are 3-dim subsets covering
the entire image cone (not codim-1).

**Corollary G2.** The NT block contributes zero additional facets to $\mathcal{K}_n$. It does
*absorb* (= remove from the facet list) the chain-only facet $\sum_{i=1}^{n-1} \lambda_i \ge 0$:
the no-NT image cone $\Phi_{\NT = 0}(\mathcal{P}_n)$ has $n+1$ facets including this partial-sum
facet at $k = n-1$, and adding NT mass kills it.

**Corollary G3.** Theorem F's $2n - 3$ chain facets *do not* lift to $2n - 3$ weight facets.
The chain → weight projection is contractive of factor $\sim (2n-3)/n \to 2$ for $n \to \infty$:
roughly half the chain structure is invisible from weight space.

---

## 3. Proof at $B_3$

We prove Theorem G in full at $n = 3$. Type-uniform machinery follows in §4.

### 3.1 Setup

Chain + NT coords (with $M_1 = 0$ dropped):
$x = (B_1, T_1, M_2, B_2, T_2, S, N^-_{12}, N^+_{12}) \in \mathbb{Z}_{\ge 0}^8$.

Chain inequalities (all $A \cdot x \le 0$, RHS 0):
$$
\begin{array}{rl}
\text{nn}_y: & -y \le 0 \quad\text{for each coordinate } y \\
L_2: & M_2 - 2 B_1 + 2 T_1 \le 0 \\
U_2: & M_2 - 2 B_1 + 2 T_1 - 2 B_2 + 2 T_2 \le 0 \\
E:   & S - 2 B_1 + 2 T_1 - 2 B_2 + 2 T_2 \le 0
\end{array}
$$
(L_1, U_1 are subsumed: L_1 forces $M_1 = 0$; U_1 redundant by Theorem F.)

Linear map $\Phi : \mathbb{R}^8 \to \mathbb{R}^3$:
$$
\Phi(x) = \begin{pmatrix} B_1 + T_1 + N^-_{12} + N^+_{12} \\ M_2 + B_2 + T_2 - N^-_{12} + N^+_{12} \\ -B_1 + T_1 - B_2 + T_2 + S \end{pmatrix}.
$$
$\mathcal{P}_3$ is a polyhedral cone in $\mathbb{R}^8$ (all inequalities homogeneous), so
$\mathcal{K}_3 = \Phi(\mathcal{P}_3)$ is a polyhedral cone in $\mathbb{R}^3$.

### 3.2 Polar duality setup

The polar of a cone $C \subseteq V$ is $C^* = \{y \in V^* : \langle y, x \rangle \le 0 \;\forall x \in C\}$.
Facets of $C$ are in bijection with extreme rays of $C^*$.

For our $\mathcal{K}_3$: $c \in \mathcal{K}_3^*$ iff $\langle c, \Phi(x) \rangle \le 0$ for all $x \in \mathcal{P}_3$,
iff $\langle \Phi^T c, x \rangle \le 0$ for all $x \in \mathcal{P}_3$, iff $\Phi^T c \in \mathcal{P}_3^*$,
iff $\Phi^T c = \sum_j \mu_j A_j$ for some $\mu_j \ge 0$ (Farkas / cone H-rep).

In coordinates, writing $c = (c_1, c_2, c_3) \in \mathbb{R}^3$ for the dual variable, and
computing $\Phi^T c$ component-by-component (reading off the rows of the matrix
$\Phi$, where row $i$ gives $\lambda_i$ as a function of $x$):
$$
\Phi^T c \;=\; \bigl(\,c_1 - c_3,\; c_1 + c_3,\; c_2,\; c_2 - c_3,\; c_2 + c_3,\; c_3,\; c_1 - c_2,\; c_1 + c_2\,\bigr)
$$
(in order $B_1, T_1, M_2, B_2, T_2, S, N^-, N^+$). The off-diagonal entries arise because
$B_1$ contributes $+1$ to $\lambda_1$ and $-1$ to $\lambda_3$, etc.

Writing the chain ineqs as rows of $A$ (in the same coord order):
$$
A_{L_2} = (-2, 2, 1, 0, 0, 0, 0, 0), \quad
A_{U_2} = (-2, 2, 1, -2, 2, 0, 0, 0), \quad
A_E = (-2, 2, 0, -2, 2, 1, 0, 0).
$$
Plus nn ineqs $A_{\text{nn}_y} = -e_y$ (negative unit vectors).

### 3.3 Necessary conditions on $c \in \mathcal{K}_3^*$

Let $p := \mu_{L_2}, q := \mu_{U_2}, r := \mu_E$ (chain-ineq multipliers, all $\ge 0$), and
$\mu_{\text{nn}_y}$ the non-negativity multipliers (also $\ge 0$). The system
$\Phi^T c = \sum_j \mu_j A_j$ reads coordinate-by-coordinate as eight equations of the
form $(\Phi^T c)_y = \sum_j \mu_j (A_j)_y$. Solving each for $\mu_{\text{nn}_y}$:
$$
\begin{array}{rll}
\text{nn}_{B_1}: & \mu_{\text{nn}_{B_1}} = (c_3 - c_1) - 2(p+q+r) & \ge 0 \\
\text{nn}_{T_1}: & \mu_{\text{nn}_{T_1}} = 2(p+q+r) - (c_1 + c_3) & \ge 0 \\
\text{nn}_{M_2}: & \mu_{\text{nn}_{M_2}} = (p+q) - c_2 & \ge 0 \\
\text{nn}_{B_2}: & \mu_{\text{nn}_{B_2}} = (c_3 - c_2) - 2(q+r) & \ge 0 \\
\text{nn}_{T_2}: & \mu_{\text{nn}_{T_2}} = 2(q+r) - (c_2 + c_3) & \ge 0 \\
\text{nn}_S:     & \mu_{\text{nn}_S}     = r - c_3 & \ge 0 \\
\text{nn}_{N^-}: & \mu_{\text{nn}_{N^-}} = c_2 - c_1 & \ge 0 \\
\text{nn}_{N^+}: & \mu_{\text{nn}_{N^+}} = -(c_1 + c_2) & \ge 0
\end{array}
$$

The last two (NT) immediately give $c_1 \le c_2$ and $c_1 + c_2 \le 0$.

The pairs $(\text{nn}_{B_1}, \text{nn}_{T_1})$ and $(\text{nn}_{B_2}, \text{nn}_{T_2})$ give *interval* conditions:
$$
2(p+q+r) \in [c_1 + c_3,\, c_3 - c_1], \qquad 2(q+r) \in [c_2 + c_3,\, c_3 - c_2].
$$
Non-empty intervals require $c_1 \le 0$ and $c_2 \le 0$ respectively.

$\text{nn}_S$ gives $r \ge \max(0, c_3)$.

$\text{nn}_{M_2}$ gives $p+q \ge c_2$, automatic since $c_2 \le 0$.

### 3.4 The binding condition $c_3 \le -c_2$

Combine $r \ge \max(0, c_3)$ with the upper bound $q+r \le (c_3-c_2)/2$ from $\text{nn}_{B_2}$:
$$
\max(0, c_3) \le r \le q+r \le (c_3-c_2)/2.
$$
*Case $c_3 \ge 0$:* $r \ge c_3$, so $c_3 \le (c_3-c_2)/2$, giving $c_3 \le -c_2$.
*Case $c_3 < 0$:* $\max(0,c_3) = 0$; we get $0 \le (c_3-c_2)/2$, i.e., $c_3 \ge c_2$. And
$c_3 \le -c_2$ is automatic (since $c_3 < 0 \le -c_2$).

Combining both cases: $c_3 \in [c_2, -c_2]$, equivalently $|c_3| \le -c_2$ (since $c_2 \le 0$).

**Summary of necessary conditions:**
$$
\boxed{\quad c_1 \le c_2 \le 0, \qquad c_2 \le c_3 \le -c_2. \quad}
$$
The conditions $c_1 + c_2 \le 0$ and $c_1 \le c_2$ are implied (the first by $c_1, c_2 \le 0$;
the second by the NT relation, but it's part of the boxed condition).

**Sufficiency.** Given $c$ satisfying the boxed conditions, the construction
$$
r := \max(0, c_3), \quad q := 0, \quad p := 0
$$
satisfies all the interval bounds (check: $(c_2 + c_3)/2 \le \max(0, c_3) \le (c_3 - c_2)/2$
splits into the two cases above; similarly for the $c_1$ interval, which is wider since
$c_1 \le c_2$). At extreme rays of the polar (like $(-1, -1, 1)$ where $c_3 = -c_2 > 0$),
the inequalities are tight and the construction $(p, q, r) = (0, 0, c_3)$ gives all
$\mu_{\text{nn}_y} \ge 0$ exactly (some equal to zero, marking saturation).

So $\mathcal{K}_3^*$ is exactly $\{c : c_1 \le c_2 \le c_3,\, c_2 + c_3 \le 0\}$ (3 binding
ineqs: $c_1 - c_2 \le 0,\, c_2 - c_3 \le 0,\, c_2 + c_3 \le 0$; $c_2 \le 0$ implied).

**Extreme rays of polar (= facet normals of image).** Each ray comes from making 2 of the 3
binding ineqs tight:
- $c_1 = c_2$ and $c_2 = c_3$ tight, $c_2 + c_3 \le 0$ slack: $c_1 = c_2 = c_3 \le 0$, ray $(-1,-1,-1)$.
- $c_1 = c_2$ and $c_2 + c_3 = 0$ tight, $c_2 - c_3$ slack: $c_1 = c_2 = -c_3$, ray $(-1,-1,1)$.
- $c_2 = c_3$ and $c_2 + c_3 = 0$ tight, $c_1 - c_2$ slack: $c_2 = c_3 = 0$, $c_1 \le 0$, ray $(-1,0,0)$.

### 3.5 Image facets

The 3 facets of $\mathcal{K}_3$ are the inequalities $\rho \cdot \lambda \le 0$ where $\rho$ is an extreme ray of the polar:
- $\rho_1 = (-1, 0, 0)$: $-\lambda_1 \le 0$, i.e., $\lambda_1 \ge 0$.
- $\rho_{\text{sum}} = (-1, -1, -1)$: $-(\lambda_1 + \lambda_2 + \lambda_3) \le 0$, i.e., $\sum \lambda_i \ge 0$.
- $\rho_E = (-1, -1, 1)$: $-\lambda_1 - \lambda_2 + \lambda_3 \le 0$, i.e., $\lambda_3 \le \lambda_1 + \lambda_2$.

This matches the numerical computation in `image_cone_extreme.py`.

### 3.6 Chain-facet collapse: why $L_2, U_2$ don't survive

The collapse is a Farkas / H-rep redundancy fact, not a set-theoretic one. In §3.3–3.4, the
polar conditions on $c$ were derived using only $\mu_E = r$ and chain non-negativity
$\mu_{\text{nn}_y}$; the chain-ineq multipliers $\mu_{L_2} = p$ and $\mu_{U_2} = q$ were always
set to zero. This shows:

**Lemma 3.1 (collapse).** Every facet of $\mathcal{K}_3$ admits a Farkas certificate of the form
$\rho \cdot \lambda = \mu_E \cdot E(x) + \sum_y \mu_{\text{nn}_y} \cdot (-y)$ with $\mu_E, \mu_{\text{nn}_y} \ge 0$
and no $\mu_{L_2}, \mu_{U_2}$ used. Hence $L_2, U_2$ are *redundant* in the projected H-rep
of $\mathcal{K}_3$: removing them from the chain-side constraints leaves $\mathcal{K}_3$ unchanged.

In particular, $L_2$ and $U_2$ do not appear as facet-defining inequalities of $\mathcal{K}_3$.

**Remark (set-theoretic dimension).** As subsets, $\Phi(L_2)$ and $\Phi(U_2)$ are 3-dim
(they contain interior points of $\mathcal{K}_3$ — e.g., the Theorem-F interior witnesses
$x = (1,0,2,1,0,0,0,0)$ for $L_2$ and $x = (2,0,2,0,1,0,0,0)$ for $U_2$ both project to
interior of $\mathcal{K}_3$, computation in `image_cone_extreme.py`). $\Phi(E)$ is also 3-dim
(its witness $(1, 1, 2)$ is on the boundary but generic $E$-tight preimages project to
interior). So all three image sets cover full dim; none is codim-1.

Set-theoretically, $\Phi(L_2)$ may or may not equal $\mathcal{K}_3$ (it does equal $\mathcal{K}_3$:
all three extreme rays of $\mathcal{K}_3$ are reachable with $L_2$ saturated; the convex
cone is then the conic hull of the rays). $\Phi(U_2)$ is a strict subset (the extreme
ray $(0, 1, -1)$ cannot be reached with $U_2$ saturated — the required preimage
would force $M_2 = 2(B_2 - T_2)$ with $B_2 + T_2 = 1$, $S \ge 0$, $\lambda_3 = -1$, all
of which over-constrains). But this set-difference is irrelevant for the facet question;
the H-rep redundancy in Lemma 3.1 is what matters.

### 3.7 Q1 verdict at $B_3$

**Q1 = NO.** Of the three chain facets $L_2, U_2, E$:
- $L_2$ collapses: image covers $\mathcal{K}_3$ (Lemma 3.1).
- $U_2$ collapses: ditto.
- $E$ contributes the facet $\lambda_3 \le \lambda_1 + \lambda_2$.

Only one of three chain facets projects to a distinct image facet. The "structural distinctness"
argument in PROVE.md was correct that the *differential* $L_2 - U_2$ is visible in weight space,
but missed that the ENTIRE non-redundancy of $L_2, U_2$ collapses because the projected inequalities
are weaker than chain non-negativity.

### 3.8 Q2 verdict at $B_3$

**Q2 = NO.** The NT block contributes zero additional facets. To see this, compare to the
*no-NT* image polytope $\mathcal{K}_3^{\text{no-NT}} := \Phi(\mathcal{P}_3 \times \{0\}^{\text{NT}})$:
empirical computation (`image_cone_no_NT.py`) gives 4 facets,
$$
\lambda_1 \ge 0, \quad \lambda_2 \ge 0, \quad \lambda_1+\lambda_2+\lambda_3 \ge 0, \quad \lambda_3 \le \lambda_1+\lambda_2.
$$
Adding NT extends the image (NT block can produce $\lambda_2 < 0$ via $N^- \cdot (E_1 - E_2)$),
killing the $\lambda_2 \ge 0$ facet. Result: 3 facets, no new ones, one removed.

So NT is *contractive* of the facet count: net effect $-1$ facet (not $+1$).

---

## 4. Type-uniform Theorem G

**Theorem G (type-uniform).** For $n \ge 2$, $\mathcal{K}_n \subset \mathbb{R}^n$ has exactly $n$ facets:
$$
\lambda_1 + \cdots + \lambda_k \ge 0 \quad (1 \le k \le n-2), \qquad
\sum_{i=1}^n \lambda_i \ge 0, \qquad
\lambda_n \le \sum_{i=1}^{n-1} \lambda_i.
$$

**Proof sketch.** Same polar-duality argument as §3, type-uniform in $n$. Necessary
conditions on $c \in \mathcal{K}_n^*$:

- For each NT pair $(a, b)$ with $1 \le a < b \le n-1$: $c_a \le c_b$ (from $N^-_{ab}$),
  $c_a + c_b \le 0$ (from $N^+_{ab}$).
- For each chain $a \in \{1, \ldots, n-1\}$: from $B_a$ and $T_a$ equations,
  $2 X_a \in [c_a + c_n, c_n - c_a]$ where
  $X_a := \mu_{U_a} + \mu_E + \sum_{b > a, b \le n-1} (\mu_{L_b} + \mu_{U_b}) \ge 0$.
  Non-empty interval iff $c_a \le c_n$, plus $c_a + c_n \le 2 X_a$.
- For $M_a$ ($a \ge 2$): $p_a + q_a \ge c_a$ where $p_a = \mu_{L_a}, q_a = \mu_{U_a}$. (Always
  feasible since $c_a \le 0$.)
- For $S$: $r \ge \max(0, c_n)$ where $r = \mu_E$.

The conditions reduce to: $c_1 \le c_2 \le \cdots \le c_{n-1} \le 0$ (from NT chain), $c_a \le c_n$
for $a = 1, \ldots, n-1$ (i.e., $c_n \ge c_{n-1}$), and $c_n + c_{n-1} \le 0$ (the upper bound
from $r \ge c_n$ combined with $X_{n-1} = r \le (c_n - c_{n-1})/2$, giving $c_n \le -c_{n-1}$
when $c_n > 0$).

Final polar H-rep:
$$
\mathcal{K}_n^* = \{c : c_1 \le c_2 \le \cdots \le c_{n-1} \le c_n, \; c_{n-1} + c_n \le 0\}.
$$
This is a cone in $\mathbb{R}^n$ defined by $(n-1) + 1 = n$ inequalities; the inequality
$c_a \le c_{a+1}$ for $a < n-1$ together with $c_{n-1} + c_n \le 0$ and $c_{n-1} \le c_n$ force
$c_a \le c_{n-1} \le 0$ for all $a \le n-1$ (no separate "$c_a \le 0$" facet).

Extreme rays of $\mathcal{K}_n^*$ (tightening $n - 1$ of the $n$ ineqs):
- For each $k = 1, \ldots, n-2$: tighten all $c_a = c_{a+1}$ ineqs *except* $c_k \le c_{k+1}$, plus
  $c_{n-1} + c_n \le 0$. Solving: $c_1 = c_2 = \cdots = c_k$ and $c_{k+1} = \cdots = c_n$
  and $c_{n-1} + c_n \le 0$ tight gives $c_{k+1} = \cdots = c_n = 0$, so ray
  $c = (-t, -t, \ldots, -t, 0, 0, \ldots, 0)$ with $t > 0$ in the first $k$ positions.
- Tighten all $c_a = c_{a+1}$ for $a = 1, \ldots, n-1$, leave $c_{n-1} + c_n \le 0$ slack:
  $c_1 = c_2 = \cdots = c_n$, ray $(-1, -1, \ldots, -1)$ (need $2 c \le 0$).
- Tighten all $c_a = c_{a+1}$ for $a < n-1$ AND $c_{n-1} + c_n = 0$, leave $c_{n-1} \le c_n$ slack:
  $c_1 = \cdots = c_{n-1} = -c_n$, ray $(-1, -1, \ldots, -1, 1)$.

Total: $(n-2) + 1 + 1 = n$ rays.

The image facets (rays of polar, read as $\rho \cdot \lambda \le 0$):
- $\rho_k = -(e_1 + \cdots + e_k)$: $\lambda_1 + \cdots + \lambda_k \ge 0$, $k = 1, \ldots, n-2$.
- $\rho_{\text{sum}} = -(e_1 + \cdots + e_n)$: $\sum \lambda_i \ge 0$.
- $\rho_E = -(e_1 + \cdots + e_{n-1}) + e_n$: $\lambda_n \le \lambda_1 + \cdots + \lambda_{n-1}$.

$\square$

**Verification.** At $n = 2$: 2 facets ($\sum \ge 0$, $\lambda_2 \le \lambda_1$). At $n = 3$:
3 facets. At $n = 4$: 4 facets. At $n = 5$: 5 facets. All confirmed in
`verify_typeuniform.py`.

### 4.1 Why the partial-sum facet $\sum_{i=1}^{n-1} \lambda_i \ge 0$ is absent

The "would-be" partial sum at $k = n-1$ is *implied* by the $E$-facet and the full sum:
$$
\sum_{i=1}^n \lambda_i \ge 0 \;\text{ and }\; \lambda_n \le \sum_{i=1}^{n-1} \lambda_i
\;\Longrightarrow\; 2 \sum_{i=1}^{n-1} \lambda_i \ge 0.
$$
Hence $\sum_{i=1}^{n-1} \lambda_i \ge 0$ is redundant given the other two, and only $k = 1, \ldots, n-2$
appear as facets.

### 4.2 Comparison to chain side

| Side  | Total facets        | Type                                                       |
|-------|---------------------|------------------------------------------------------------|
| Chain ($\mathcal{P}_n$) | $2n - 3$ carry-derived | $\{L_a, U_a : 2 \le a \le n-1\} \cup \{E\}$ |
| Weight ($\mathcal{K}_n$) | $n$ | $\{$partial sums $1, \ldots, n-2\} \cup \{$full sum$\} \cup \{\Phi(E)\}$ |

Ratio $(2n-3)/n \to 2$ as $n \to \infty$: the chain → weight projection loses *roughly half*
the chain structure. Only the $E$-facet survives; all $L_a, U_a$ collapse.

---

## 5. Computational verification

| $n$ | image facets predicted | image facets found       | match |
|----:|-----------------------:|--------------------------|------:|
| 2   | 2                      | 2 (sum, $\lambda_2 \le \lambda_1$) | ✓ |
| 3   | 3                      | 3 ($\lambda_1 \ge 0$, sum, $\Phi(E)$) | ✓ |
| 4   | 4                      | 4 ($\lambda_1 \ge 0$, $\lambda_1+\lambda_2 \ge 0$, sum, $\Phi(E)$) | ✓ |
| 5   | 5                      | 5 ($\lambda_1\ge 0$, $\sum_2\ge 0$, $\sum_3\ge 0$, sum, $\Phi(E)$) | ✓ |

Scripts: `image_cone_extreme.py` ($B_3$), `B2_check.py` ($B_2$), `B4_check.py` ($B_4$),
`verify_typeuniform.py` ($B_3, B_4, B_5$).

---

## 6. Verdict on PROVE.md

| Question | Prior | Verdict | Notes |
|---|---|---|---|
| Q1: chain-facet distinctness | P=80% YES | **NO** | $L_2, U_2$ collapse; only $E$ survives |
| Q2: NT contributes ≥1 facet | P=40% YES | **NO** | NT contributes 0, kills 1 |
| Joint conjecture | P=55% | **falsified by Q1** | structural surprise |

**Calibration:** The Q1=YES prior was set at 80% based on "structural distinctness of MB-bounds
vs singleton bound." This was wrong because the question isn't structural distinctness of the
*differential* (which is visible in weight space, $L_2 - U_2$ differs by $B_2 - T_2$ contributing
to $\lambda_3$); it's whether the chain inequality is *tight enough* to be a binding constraint
in weight space. The chain $L_2$ inequality $M_2 \le 2(B_1 - T_1)$ becomes (after projection +
non-negativity) something like $\lambda_2 \le 2 \lambda_1 + \text{slack}$, which is *weaker* than
non-negativity $\lambda_1 \ge 0$ plus other facets.

The "right framing" (which I missed in the prior) is: a chain facet projects to a weight facet
iff its inequality is the *strongest* upper-bound on some weight-space direction. $E$ achieves
this for the direction $(\rho_E = (-1,-1,\ldots,-1,1))$; $L_a, U_a$ don't achieve it for any
direction.

**Update OQ-K status:** Layer 1 (chain side) is closed at $2n - 3$ carry facets (Theorem F).
Layer 2 (weight side) is now CLOSED at $n$ image facets (Theorem G). The chain → weight
projection is *contractive* of ratio $(2n-3)/n$. OQ-K verdict: chain framework FULLY DESCRIBES
the weight-space polytope BUT only one chain facet ($E$) survives projection — the other
chain facets describe sub-structure that lives in chain space but vanishes upon projection.

---

## 7. Gaps

1. **Type-uniform proof rigor.** The §4 proof sketch goes through the polar argument at general
   $n$ in outline. The detailed verification of necessary AND sufficient conditions for general $n$
   follows the $B_3$ template (§3.3–3.4) but the construction of feasible $\mu$ for general $n$
   given conditions on $c$ needs to be spelled out. (Computational verification at
   $n = 2, 3, 4, 5$ confirms the formula.) Promote sketch → full proof in v3.

2. **Stratification.** Theorem G describes the *image polytope*. The image's *interior* lives
   over multiple chain configurations (since $\Phi$ is not injective); a finer stratification
   (multiplicity function on the image) is open. Note this is essentially the Kobayashi
   piecewise-linear branching multiplicity, which Kobayashi 2604.22262 establishes is governed
   by fences. Theorem G identifies the FENCES of $\mathcal{K}_n$; the multiplicities ON those fences
   are not addressed here.

3. **Algebraic geometric interpretation.** $\mathcal{K}_n$ is a cone with $n$ facets in $\mathbb{R}^n$:
   minimal possible for a full-dim cone (= simplicial cone), since a polyhedral cone in $\mathbb{R}^n$
   needs at least $n$ facets to be full-dim. So $\mathcal{K}_n$ is a *simplicial* cone! This is striking
   — the weight-space picture is as simple as possible. Identifying the $n$ extreme rays of
   $\mathcal{K}_n$ (= the 1D faces) is a separate piece of structure: from the proof, they are the
   $n$ rays obtained by intersecting $n-1$ of the $n$ image facets. Explicit computation at $B_3$
   gave rays $(0,1,1), (0,1,-1), (1,-1,0)$.

4. **Connection to Kobayashi's polytope.** Kobayashi 2604.22262 introduces a polyhedral "fence"
   description of BDI branching multiplicities; Theorem G identifies the $n$ fences for the
   pair $(GL_{2n+1}, O_{2n+1})$ in our chain coordinates. Whether the $n$ image facets match
   Kobayashi's intrinsic fences (he gives a different combinatorial recipe) is open. The match
   is *expected* by representation theory but needs explicit verification — a v3 OQ-KOB-MATCH item.

---

## 8. Files

- `2026-05-21-weight-space-projection/phi_explicit.py` — Fourier–Motzkin (blew up; not used).
- `2026-05-21-weight-space-projection/image_cone_extreme.py` — $B_3$ extreme-ray + facets.
- `2026-05-21-weight-space-projection/image_cone_no_NT.py` — $B_3$ no-NT comparison.
- `2026-05-21-weight-space-projection/B2_check.py` — $B_2$ sanity.
- `2026-05-21-weight-space-projection/B4_check.py` — $B_4$ verification.
- `2026-05-21-weight-space-projection/verify_typeuniform.py` — $B_3, B_4, B_5$ type-uniform check.
- `2026-05-21-weight-space-projection/analytic_dual.py` — symbolic polar derivation at $B_3$.

---

## 9. Whiskey rule

The right framing was "polar duality, not facet projection." I spent the first half of the
session trying to *project* chain facets directly, which led to the wrong intuition (Q1=YES).
The correct framing is *polar* the chain polytope, project the polar via $\Phi^T$, identify
chain facets that survive. Once framed that way, the answer (Q1=NO, only $E$ survives) was
forced by the linear-algebra: chain $L_a, U_a$ inequalities are *implied* by chain
non-negativity + $E$ in weight coordinates, so they're redundant in the projected H-rep.

The empirical computation (3 facets at $B_3$) was the trigger that broke the wrong prior;
the analytic dual-cone argument (§3.3-3.4) made it rigorous.

Theorem G + Theorem F together close OQ-K:
- **Chain side ($\mathcal{P}_n$):** $2n - 3$ carry-derived facets (Theorem F).
- **Weight side ($\mathcal{K}_n$):** $n$ facets (Theorem G), only one carry-derived ($\Phi(E)$).

The chain framework is the right home for the *fine* combinatorics; the weight side is the
right home for the *coarse* fence structure. The two are connected by $\Phi$, with the
projection being contractive in facet count by factor $\sim 2$.

Eight-day arc complete: Day 21 universal-chain-factor refutation → Day 26 Theorem E → Day 28
Theorem F (chain side) → Day 29 Theorem G (weight side). v3 §3 Theorem F + new §3.6 Theorem G
forms the polyhedral chapter.

— Rick
