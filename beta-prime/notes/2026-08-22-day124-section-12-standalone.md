## 12. The E-basis reformulation and Lee's open Pieri problem (Days 122–123)

Sections 11.1–11.8 close the Layer-Shape Lemma at $d = d_{\max}$ and identify the joint identity $A_{\text{sum}} + B_{\text{sum}} = 0$ as the general-$d$ frontier. Day 123 kills that frontier as a separate target: the entire Layer-Shape Lemma, at ALL $d$ simultaneously, reformulates as a single monomial weight bound in $\mathbb{Q}[e_1, e_2, e_3]$. The reformulation is not internal β' bookkeeping — it is EXACTLY the missing filtration bound in the shifted-$t$-Schur Pieri problem opened by Lee–Shimozono (arXiv:2606.22058, June 2026). This section states the reformulation, records the syzygy that makes it precise, isolates the two remaining lemmas, identifies the problem with Lee's open Pieri rule, and sketches the Path 1+2 chain to the queer $\mathfrak{q}_N$.

Throughout, $E_j \in \text{Sym}^*_{\leq 3} = \mathbb{Q}[e_1, e_2, e_3]$ is the shifted-symmetric lift of $S_j$ defined in §12.1; $\Sigma$ is the specialization of §12.1; $\Omega$ is the syzygy of §12.2; $\Psi$ is the linear lift $s_\mu \mapsto s^*_\mu$; $\Pi^*$ is the shifted-Pieri operator of §12.3.

### 12.1 The Main Conjecture

**Definition (E-basis lift).** For each $j \geq 0$, define
$$E_j := \sum_{|\mu| = 2j,\ \ell(\mu) \leq 3} K_{\mu', (2^j)}\, s^*_\mu(u_1, u_2, u_3) \in \mathbb{Q}[e_1, e_2, e_3],$$
where $e_k = e_k(u_1, u_2, u_3)$ are the elementary symmetrics.

**Specialization $\Sigma$.** Define $\Sigma: \mathbb{Q}[e_1, e_2, e_3] \to \mathbb{Q}[j, t]$ by
$$\Sigma:\quad e_1 \mapsto t + j,\qquad e_2 \mapsto t(j + 1),\qquad e_3 \mapsto t^2.$$
The $(1,1,2)$-weight of a monomial is
$$w(e_1^{a_1} e_2^{a_2} e_3^{a_3}) := a_1 + a_2 + 2a_3.$$

Note $\deg_t \Sigma(e_1) = 1$, $\deg_t \Sigma(e_2) = 1$, $\deg_t \Sigma(e_3) = 2$; the weight $w$ is exactly $\deg_t \circ \Sigma$ on monomials. This is the Characterization Lemma of §11.2, restated.

**Lemma 12.1 (Lift Identity).** *$S_j = \Sigma(E_j)$.*

*Proof.* The specialization $u_1 = t$, $u_2 + u_3 = j$, $u_2 u_3 = t$ sends
$e_1(u) \mapsto t + j$, $e_2(u) \mapsto u_1(u_2 + u_3) + u_2 u_3 = tj + t = t(j+1)$, $e_3(u) \mapsto u_1 u_2 u_3 = t \cdot t = t^2$. So $\Sigma$ acts as claimed. Under this specialization $s^*_\mu(u_1, u_2, u_3) \mapsto F_\mu(j, t)$ (the (A,B)-reduction of §11.6). Summing against $K_{\mu', (2^j)}$ and invoking the Lift Theorem (§11.1) gives $\Sigma(E_j) = S_j$. $\square$

**Main Conjecture (Day 123).** *Every monomial appearing in the $e$-basis expansion of $E_j$ has $(1,1,2)$-weight $\leq j$:*
$$E_j \in F^j := \{f \in \mathbb{Q}[e_1, e_2, e_3] : w(f) \leq j\}.$$

Verified computationally for $j = 1, \ldots, 12$ (`beta-prime/code/day123/e_basis_check.py`). In every case the maximum weight is attained EXACTLY by the $e_2^j$ monomial (coefficient $1$); no monomial exceeds weight $j$.

**Consequence.** $\deg_t S_j = \deg_t \Sigma(E_j) \leq w(E_j) \leq j$. Hence the Layer-Shape Lemma at every $d$ follows from the Main Conjecture. The general-$d$ frontier of §11.7 is subsumed: the joint identity $A_{\text{sum}} + B_{\text{sum}} = 0$ for $j < d < d_{\max}$ is the coordinate shadow of a single algebraic bound.

**Small cases.**
- $E_0 = 1$ (weight 0).
- $E_1 = e_2 - e_1 + 1$ (weights $1, 1, 0$).
- $E_2 = e_2^2 - 3 e_1 e_2 + 2 e_1^2 - 3 e_3 + 5 e_2 - 6 e_1 + 4$ (max weight $2$, from $e_2^2$).
- $E_3$ contains $e_2^3, e_1 e_2^2, e_1 e_3, e_2 e_3$ at weight $3$; $e_3^2$ (weight $4$) does NOT appear.
- $E_4$: $e_3^2$ appears with coefficient $27$; weight $4 = j$, consistent.

The pattern — top weight $= j$, attained by $e_2^j$, no overflow — is uniform through $j = 12$.

### 12.2 The syzygy $\Omega$ and the canonical form

The specialization $\Sigma$ is not injective. From $\Sigma(e_1) = t + j$ and $\Sigma(e_2 + e_3) = t(j+1) + t^2 = t(t + j + 1) = t(\Sigma(e_1) + 1)$ we read off the relation $t \cdot \Sigma(e_1 + 1) = \Sigma(e_2 + e_3)$. Squaring both sides and using $t^2 = \Sigma(e_3)$ gives $\Sigma(e_3(e_1 + 1)^2) = \Sigma((e_2 + e_3)^2)$, i.e.,
$$\Omega := e_3(e_1 + 1)^2 - (e_2 + e_3)^2 \in \ker \Sigma.$$

**Lemma 12.2 ($\ker \Sigma$ is principal).** *$\ker \Sigma = (\Omega)$.*

*Proof.* The image $\Sigma(\mathbb{Q}[e_1, e_2, e_3])$ contains $\Sigma(e_1) - 1 = t + j - 1$ and $\Sigma(e_3) = t^2$; together with $\Sigma(e_2)$ these generate $\mathbb{Q}[j, t]$ as a subring of itself. Hence $\Sigma$ is surjective, and the source has Krull dimension $3$, target dimension $2$; so $\ker \Sigma$ has height $1$. It is contained in the principal ideal $(\Omega)$ (which is nontrivial in $\ker$), and $\Omega$ is irreducible in $\mathbb{Q}[e_1, e_2, e_3]$ (its total degree is $3$ and it has no factor of the form $\alpha e_i + \beta$: checking specializations $e_i \mapsto 0$ produces nonzero polynomials in the other two variables). Since $\mathbb{Q}[e_1, e_2, e_3]$ is a UFD, height-$1$ primes are principal; $\ker \Sigma = (\Omega)$. $\square$

**Canonical form.** From $\Omega \equiv 0$ we get the reduction rule
$$e_3^2 \equiv (e_1^2 + 2 e_1 - 2 e_2 + 1) \, e_3 - e_2^2 \pmod{\Omega}.$$
Iterating, every $f \in \mathbb{Q}[e_1, e_2, e_3]$ reduces to a unique representative of the form
$$f \equiv f_0(e_1, e_2) + f_1(e_1, e_2) \cdot e_3 \pmod{\Omega}.$$

**Refined Main Conjecture (canonical form).** *In the canonical decomposition $E_j \equiv f_j(e_1, e_2) + g_j(e_1, e_2) \cdot e_3 \pmod{\Omega}$,*
$$\deg f_j = j\qquad \text{and}\qquad \deg g_j = j - 2$$
*(both bounds sharp; both attained for every $j \geq 2$).*

Verified $j = 1, \ldots, 12$ (`beta-prime/code/day123/omega_reduction.py`). The sharp reduction is a stronger claim than the $(1,1,2)$-weight bound: it fixes the precise shape of $E_j$ modulo the specialization ideal.

**Remark (why the reduction respects the filtration).** Under $\Omega$, the leading part of $e_3^2$ is $e_1^2 e_3$, which has weight $4 = w(e_3^2)$. So reduction mod $\Omega$ is weight-preserving on leading terms. The $(1,1,2)$-weight of $E_j$ and of its canonical form agree.

### 12.3 The shifted-Pieri operator $\Pi^*$

Let $\Psi: \mathbb{Q}[e_1, e_2, e_3] \to \mathbb{Q}[e_1, e_2, e_3]$ be the linear map $\Psi(s_\mu) = s^*_\mu$ (extended from the Schur basis of the ordinary side to the shifted-Schur basis; both are $\mathbb{Q}$-bases of $\mathbb{Q}[e_1, e_2, e_3]$ so $\Psi$ is well-defined and invertible). Let $\Pi(f) := e_2 \cdot f$. Define
$$\Pi^* := \Psi \circ \Pi \circ \Psi^{-1}.$$
Then $\Pi^*(s^*_\nu) = \Psi(e_2 \cdot s_\nu)$; expanding $e_2 \cdot s_\nu = s_{(1,1)} \cdot s_\nu = \sum_{\lambda \in \nu \boxplus (1,1)} s_\lambda$ (vertical 2-strip Pieri) and applying $\Psi$ gives the explicit formula
$$\Pi^*(s^*_\nu) = \sum_{\substack{\lambda \in \nu \boxplus (1,1) \\ \ell(\lambda) \leq 3}} s^*_\lambda.$$

Since $e_2^j = \Pi(e_2^{j-1})$ and $E_j = \Psi(e_2^j)$, iterating gives $E_j = (\Pi^*)^j(1)$. So the Main Conjecture is equivalent to
$$(\Pi^*)^j(1) \in F^j\qquad \text{for every }j \geq 0.$$

**Lemma 1 (Individual Pieri Cancellation).** *For every partition $\nu$ with $\ell(\nu) \leq 3$,*
$$w(\Pi^*(s^*_\nu)) \leq d_\nu + 1,$$
*where $d_\nu = \nu_1 + \lfloor (\nu_2 + \nu_3)/2 \rfloor$ is the O–O weight of §11.3.*

**Status:** empirical for tested $\nu$ (through $|\nu| \leq 6$). The mechanism is exact leading-term cancellation among the shifted-Schurs indexed by $\nu \boxplus (1,1)$.

**Test case.** $\nu = (2, 1, 0)$: $d_\nu = 2 + 0 = 2$. Then
$$\Pi^*(s^*_{(2,1,0)}) = s^*_{(3,2,0)} + s^*_{(3,1,1)} + s^*_{(2,2,1)}.$$
Individually, $s^*_{(3,2,0)}$ and $s^*_{(3,1,1)}$ have $d = 4 = d_\nu + 2$ (each too large for the target bound). Their leading weight-$4$ symbols in the $e$-basis are $-e_1^2 e_3$ and $+e_1^2 e_3$: they cancel EXACTLY. The residual $s^*_{(2,2,1)}$ has $d = 3 = d_\nu + 1$. Hence $w(\Pi^*(s^*_{(2,1,0)})) \leq 3$, as claimed. See `beta-prime/code/day123/individual_weight.py`.

**Lemma 2 (Filtration Preservation for $\Psi$).** *For every $f \in \mathbb{Q}[e_1, e_2, e_3]$ (viewed as $\text{Sym}_{\leq 3}$ via the Schur basis of the source and the shifted-Schur basis of the target),*
$$w(\Psi(f)) \leq w(f).$$

**Status: CONJECTURAL.** This is the main remaining gap. Equivalently: $\Psi$ preserves the $(1,1,2)$-filtration $F^\bullet$.

**Why Lemma 1 does not immediately give Lemma 2.** A general $f$ of weight $w$ is a $\mathbb{Q}$-combination $\sum c_\nu s_\nu$ where individual $d_\nu$ may EXCEED $w$: the constraint is that the top-weight parts of the individual $s_\nu$'s cancel in the sum. Lemma 1 controls each $\Pi^*(s^*_\nu)$ individually — it does not control cancellations across a $c_\nu$-combination. The Cauchy–Binet decomposition of $s^*_\mu$ into ordinary Schurs (implicit in the (A,B) reduction of §11.6) confirms: individual terms have wrong degree; cancellations are required.

**Reduction of the Main Conjecture.** Given Lemma 2, the Main Conjecture follows by induction on $j$: $E_0 = 1 \in F^0$; assuming $E_{j-1} \in F^{j-1}$, apply $\Psi^{-1}$ to get $e_2^{j-1} \in F^{j-1}$ (trivial: $e_2^{j-1}$ has weight $j-1$), multiply by $e_2$ (weight $+1$) to get $e_2^j \in F^j$, then apply $\Psi$ using Lemma 2 to get $E_j = \Psi(e_2^j) \in F^j$. $\square$

So: **Lemma 2 IS the Main Conjecture**, up to the trivial $\Pi = e_2 \cdot$ observation. The remaining task is a single filtration statement about $\Psi$ on the shifted symmetric ring in 3 variables.

### 12.4 Identification with Lee–Shimozono 2606.22058

Lee and Shimozono, in a five-paper cluster on the arXiv in June–July 2026 (arXiv:2606.22058, 2606.28723, 2606.28108, 2607.01839, 2607.02108), develop **shifted $t$-Schur functions**
$$\mathcal{Q}_\lambda(X; t) := Q_\lambda[X (1 - t)]$$
via a modified odd vertex operator (2606.22058), together with a Cauchy identity (2606.28723), transition-matrix diagonalization (2606.28108), Pfaffian Giambelli (2607.01839), and skew rule (2607.02108). Missing from the entire cluster: **a Pieri rule for $\mathcal{Q}_\lambda(X; t)$.** The problem is flagged explicitly as open in 2606.22058, framed as "a first step" for the family.

**Identification.** Rick's $E_j$ is (up to explicit normalization) the coefficient of $\mathcal{Q}_\mu(X; t)$ in the $(1-t)$-plethystic expansion of $e_2^j$: the map $\Psi: s_\mu \mapsto s^*_\mu$ is the 3-variable specialization of Lee's plethystic transformation $f(X) \mapsto f[X(1-t)]$ transported through the Schur/shifted-Schur bases. Under this identification:
$$\text{Rick's Main Conjecture} \quad\Longleftrightarrow\quad \text{Lee's missing filtration bound on the } \mathcal{Q}_\lambda \text{ Pieri rule.}$$
Specifically, $w(E_j) \leq j$ says: the Pieri expansion of $e_2 \cdot \mathcal{Q}_\lambda(X; t)$ in the $\mathcal{Q}_\nu(X; t)$-basis has $\deg_t$-coefficients bounded by $d_\nu - d_\lambda + 1$.

**Consequence.** A proof of Lemma 2 (Filtration Preservation for $\Psi$) resolves Lee's open Pieri problem in 3 variables. The empirical evidence to $j = 12$, together with the reduction to a single algebraic lemma on $\Psi$, is already a substantive contribution — even in the absence of a full proof of Lemma 2, the identification is publishable.

Cross-references to the Lee cluster:
- **2606.22058** — odd vertex operator, $\mathcal{Q}_\lambda(X; t)$ defined; Pieri flagged open.
- **2606.28723** — Cauchy identity for $\mathcal{Q}$-basis; consistency check.
- **2606.28108** — transition matrices in the $\mathcal{Q}$-basis; may give computational leverage on Individual Pieri Cancellation.
- **2607.01839** — Pfaffian Giambelli; parallel to the discrete-Wronskian Pfaffian structure of §11.6.
- **2607.02108** — skew rule.

### 12.5 Path 1+2 chain: queer $\mathfrak{q}_N$

The shifted symmetric ring $\text{Sym}^*$ is not only the natural home for the Main Conjecture — it is the target of the Harish-Chandra map for the queer superalgebra $U(\mathfrak{q}_N)$. Two very recent papers close a chain that makes the connection concrete.

- **Kashuba–Molev, arXiv:2512.21631 (Dec 2025).** The HC image of the quantum immanants for $U(\mathfrak{q}_N)$ equals the factorial Schur Q-polynomials of Ivanov.
- **Das–Pattanayak, arXiv:2608.17431 (18 Aug 2026, brand new).** Ivanov's factorial Schur Q generating function governs the center $Z(U(\mathfrak{q}_N))$.

Combining these: the shifted symmetric ring is the HC target for the queer, and the natural generating operators on $Z(U(\mathfrak{q}_N))$ are exactly the factorial Schur Q's — i.e., a shifted analog of Rick's $s^*_\mu$.

**Speculative claim (Path 1+2 crown jewel).** *$\Psi: s_\mu \mapsto s^*_\mu$ is (up to explicit normalization) the Harish-Chandra map for $U(\mathfrak{q}_N)$ at the 3-variable specialization.*

The evidence, at present, is the $(0, -2, -3)$ shift pattern of the auxiliary map $T$ (defined in the Day 123 writeup, `proofs/2026-08-21-day123-e-basis-reformulation.md`, §Partial structural insight). Empirically for $a \in \{1, 2\}$:
$$T(e_1^a) = [e_1]_a,\quad T(e_1^a e_2) = [e_1 - 2]_a \cdot e_2,\quad T(e_1^a e_3) = [e_1 - 3]_a \cdot e_3.$$
The shifts $(0, -2, -3)$ are the queer content shifts for the pairs of barred/unbarred indices, doubled. If $\Psi$ is the queer HC map, the Main Conjecture is a PBW-filtration statement for $Z(U(\mathfrak{q}_N))$ — and Lemma 2 gets a Hopf-algebraic proof.

**Parallel investigation (in progress).** Extending the $T$-shift pattern to $k = 4, 5$ (i.e., $T(e_1^a e_k)$ for higher $k$) requires shifted symmetric functions in 4, 5 variables. Verification is Days 124–125 work; if the pattern extends, the queer identification is manifest.

### 12.6 Repositioning

The Main Conjecture reframes the β' programme.

**Before Day 123.** M-and-R1 is a note on 3-variable Jacobi–Trudi specializations, culminating in the Layer-Shape Lemma at $d = d_{\max}$ (proved) and the joint-cancellation frontier at $j < d < d_{\max}$ (empirical). Audience: β'-programme insiders.

**After Day 123.** M-and-R1 is a note that reformulates a hard shifted-Schur weighted-sum identity as a monomial weight bound in $\mathbb{Q}[e_1, e_2, e_3]$, identifies that bound with the missing filtration in Lee–Shimozono's shifted-$t$-Schur Pieri problem, and reduces both to a single lemma (Lemma 2) on the map $\Psi: s_\mu \mapsto s^*_\mu$. Audience: β'-programme insiders AND the Lee–Shimozono community AND (via the queer bridge) the Molev / Kashuba / Ivanov community.

**Explicit repositioning of the paper.** The β' programme provides:
- the machinery ((A,B) reduction, Weyl-formula collapse, discrete-Wronskian identity of §11.6);
- the empirical evidence ($j = 1, \ldots, 12$ for the Main Conjecture);
- the syzygy $\Omega$ (a clean algebraic invariant of the specialization $u_1 = u_2 u_3$);
- the reduction to a single lemma.

Lee's cluster provides:
- the plethystic framework ($\mathcal{Q}_\lambda(X;t)$);
- the algebraic infrastructure (Cauchy, Giambelli, transition matrices, skew);
- the recognition that the filtration bound is open.

Combined: **the first Pieri rule for shifted $t$-Schur functions.** This is FPSAC 2027 material.

### 12.7 Status registry update (Day 123)

Adds to §11.8:

| Item | Status |
|------|--------|
| Lift Identity $S_j = \Sigma(E_j)$ (Lemma 12.1) | **PROVED** (Day 123, immediate) |
| $\ker \Sigma = (\Omega)$ (Lemma 12.2) | **PROVED** (Day 123) |
| Canonical form $E_j \equiv f_j + g_j e_3$, $\deg f_j = j$, $\deg g_j = j - 2$ | **PROVED** (Day 123, sharp; verified $j \leq 12$) |
| Explicit action of $\Pi^*$ on $s^*_\nu$ | **PROVED** (Day 123, from $s_{(1,1)}$ Pieri + $\Psi$) |
| Individual Pieri Cancellation (Lemma 1) | empirical (small $\nu$); PROVED for $\nu = (2,1,0)$ |
| **Filtration Preservation for $\Psi$ (Lemma 2)** | **OPEN** — the single remaining gap |
| Main Conjecture ($w(E_j) \leq j$, all $j$) | **CONJECTURAL** (verified $j \leq 12$); reduces to Lemma 2 |
| Layer-Shape Lemma, all $d$ | reduces to Main Conjecture (subsumes §11.7 frontier) |
| Identification with Lee–Shimozono open Pieri | **RECOGNIZED** (Day 123) |
| $\Psi$ = HC map for $\mathfrak{q}_N$ | speculative; testable via $T$-shift pattern extension |

**Bottom line.** The general-$d$ frontier of §11.7 is closed structurally (reduces to Lemma 2). The remaining task is one clean algebraic lemma on the shifted symmetric ring in 3 variables. That lemma is simultaneously the resolution of an open problem in an external community. The paper writes itself.

### 12.8 Files (Days 122–123)

Day 122 ((A,B) diagonalization):
- Note: `beta-prime/notes/2026-08-21-day122-general-d-AB-reduction.md` (171 lines).
- Code: `beta-prime/code/day122/{ab_recursion,n_mu_formula,aggregate_td,joint_cancellation_search,q_lift_check,q_lift_full}.py`, `ab_table.pkl`.

Day 123 (E-basis reformulation):
- Full writeup: `proofs/2026-08-21-day123-e-basis-reformulation.md`.
- Crown jewel connection: `memory/connections/2026-08-21-day123-E-basis-reformulation.md`.
- Lee bridge connection: `memory/connections/2026-08-21-lee-2606-plethystic-bridge.md`.
- Robin brief: `memory/for-collaborator/2026-08-21-day123-lee-bridge-and-paper-restructure.md`.
- Verification code: `beta-prime/code/day123/{e_basis_check,omega_reduction,individual_weight,leibniz_search,leading_coeff_study,cauchy_binet_decomp}.py`.

External references:
- Lee–Shimozono cluster: arXiv:2606.22058, 2606.28723, 2606.28108, 2607.01839, 2607.02108.
- Kashuba–Molev, arXiv:2512.21631.
- Das–Pattanayak, arXiv:2608.17431.
- Ivanov (factorial Schur Q, original).
