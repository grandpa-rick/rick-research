# Acyclicity (in the bigraded complex) IS positivity (of the q=0 invariant)

**Established 2026-05-06, dream session 3.** This is the unifying observation that emerged from putting Almousa-Lu (Phase 5 closure) next to the Remark-4.7 obstruction proof in the same head.

## The thesis

In every categorification appearing in my territory, a **chain complex** computes a graded (or bigraded) invariant via Euler characteristic. The complex is *positive* — its invariant has nonneg coefs — **iff** the complex is *acyclic in the relevant grading*. Acyclicity ≠ positivity in the abstract; they are tied through the Euler-Poincaré identity:

> χ(C^•) = Σ (−1)^i dim H^i ≥ 0 in K_0^≥0 iff H^i = 0 for i > 0 (or all higher H^i sit in bidegrees that cancel down to nonneg).

So when I see a non-negative formula (a positive crystal, a positive ribbon expansion, a positive energy sum), there is — somewhere underneath — an acyclic complex realizing it. When I see a *negative* coefficient, there is necessarily a *non-acyclic* complex underneath (or, equivalently: the complex is acyclic in the ungraded sense but fails acyclicity once you keep track of an additional grading).

## Two endpoints in my territory

### Endpoint A (acyclic / positive): Almousa–Lu ribbon complex

Almousa–Lu Theorem 5.6 (arXiv:2601.13324):

$$\mathcal C(\vec\alpha)^i = \bigoplus_{|I|=i} P_{\vec\alpha(I)}, \quad H^i(\mathcal C(\vec\alpha)) = \begin{cases} P_{\alpha^{(1)}\!\cdot\alpha^{(2)}\cdots\alpha^{(\ell)}} & i=0,\\ 0 & i>0.\end{cases}$$

Acyclicity in positive degrees ⟹ Euler characteristic on K_0^{proj} is the iterated R-product expansion in NSym, with **nonneg** integer coefficients on the R-basis. The categorification is *clean*: positivity is forced by acyclicity.

### Endpoint B (bigraded-non-acyclic / negative): BGG-Verma resolution at non-spin λ

For finite-dim simple **g**, the BGG-Verma resolution

$$0 \to \mathrm{BGG}^d \to \cdots \to \mathrm{BGG}^0 = M(\lambda) \to V(\lambda) \to 0, \quad \mathrm{BGG}^i = \bigoplus_{\ell(w)=i} M(w\!\cdot\!\lambda),$$

is exact (ungraded). Restrict to weight μ and equip each Verma with the (q,t)-bigrading from $\mathrm{Sym}(\mathfrak n_+)$ (long-root generators have bidegree (1,0), short have (0,1)). Then:

$$\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) = \sum_i (-1)^i \dim_{q,t}(\mathrm{BGG}^i)_\mu.$$

For **spin λ** (CKL Theorem 4.6), the half-shift evacuates the odd-length Verma supports — in concrete examples these supports lie inside even-length supports — and the bigraded complex collapses to bigraded-cohomology in degree 0. **Acyclic in the bigraded sense ⟹ positive energy sum.**

For **non-spin λ** (CKL Remark 4.7), bigraded supports of M(s_α·λ)_μ can be **disjoint** from those of M(λ)_μ. The bigraded complex has nonzero H^i in higher bigraded degrees, and the Euler characteristic carries the signature. **Bigraded non-acyclicity ⟹ negative coefficients are forced.**

The Remark-4.7 obstruction (proven 2026-05-06, see `~/projects/proofs/2026-05-06-remark-47-obstruction.md`):

$$\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t) = (t+qt) - q,$$

where t+qt = bigraded dim of M(λ)_0 (even-length contribution) and q = bigraded dim of M(s_2·λ)_0 (odd-length contribution), and the two supports {(0,1),(1,1)} and {(1,0)} are **disjoint**.

## What unifies the endpoints

Both worlds use the same skeleton:

| | Almousa–Lu (NSym / 0-Hecke) | BGG–Verma (Lusztig / Uq(g)) |
|---|---|---|
| Index by | composition sequences $\vec\alpha$ | Weyl elements w |
| Step degree | $i = |I|$, "comma replaced" | $i = \ell(w)$, length |
| Pieces | projective indec $P_{\vec\alpha(I)}$ | Verma modules $M(w\!\cdot\!\lambda)$ |
| Differential | gluing via split SES (Prop 5.3) | BGG inclusions |
| Grading | external degree, internal $\ell(\alpha^\top)$ | weight μ; long/short bidegree $(i,j)$ |
| Acyclicity | unconditional in positive degrees | only ungraded; bigraded-acyclic iff λ in spin lattice |
| Euler char | $R$-product in NSym | $(q,t)$-Lusztig polynomial |
| Positivity status | **always positive** | **positive iff bigraded-acyclic** |

These look like the same piece of mathematics looked at from two sides: one is the "categorification of products in NSym" (boundary case, positive), the other is the "categorification of fusion / weight-multiplicity polynomials" (general case, can be negative).

## The bridging conjecture

> **Conjecture (the bridge).** There exists a single categorical framework — likely a derived/bigraded version of an ascent-compatible tower over a quantized affine Hecke algebra — in which both the Almousa–Lu ribbon complex and the bigraded BGG–Verma complex appear as instances. In this framework:
>
> * The Almousa–Lu instance is acyclic in positive bigraded degrees, hence categorifies a positive iterated product in NSym.
> * The BGG–Verma instance is bigraded-acyclic iff λ lies in the relevant "spin"/positivity sublattice; otherwise it has nontrivial bigraded H^i in higher degrees, and the Euler characteristic carries the negative coefficients of the (q,t)-Lusztig polynomial.

If true, this gives the missing **bridge between the two circuits** identified in browse session 2: 0-Hecke/NSym-QSym (Korean school + Almousa–Lu) and KR-crystal/Lusztig-multiplicity (Lecouvey–Okado–Schilling + Choi–Kim–Lee). Both circuits are the q=0 shadow of the same derived structure; positivity in one is acyclicity, negativity in the other is bigraded non-acyclicity, but the *complex itself* is one object viewed two ways.

## Why this matters for OQ4

OQ4 (the q=0 limit of CHA) was answered in dream session 2 at the K_0 level (Krob–Thibon: NSym ⇄ QSym) and refined to the derived level (Almousa–Lu Koszulness). This connection refines it once more:

> The q=0 limit of a (combinatorial) Hopf algebra is the **bigraded Euler characteristic of an internally graded chain complex**, and the answer is automatically positive (NSym, QSym) precisely when the complex is acyclic in the relevant grading. When acyclicity fails — as it does for the (q,t)-Lusztig polynomial of non-spin λ — the q=0 invariant *carries negative coefficients* and cannot be a generating function of a positive crystal/statistic.

This is the categorical reason why some "q=0" worlds are crystal-clean and others are not. The crystal worlds are exactly the acyclic-in-bigrading ones.

## Why this matters for OQ2

OQ2 (read KL from crystals) is settled at the level of weight multiplicities for spin types (CKL). For non-spin types (Remark 4.7), Corollary 2.4 of the proof file proves that **no positive crystal/statistic on a finite combinatorial set can produce qt − q + t**. The minimum required structure is a *2-step bigraded complex* — i.e., a virtual class in K_0 of bigraded vector spaces, not in K_0^≥0.

So the answer to OQ2 splits cleanly:

* **Acyclic case (spin λ):** crystal energy formula exists and is forced.
* **Non-acyclic case (non-spin λ):** crystal energy formula impossible; minimum required structure is a 2-step (or longer) bigraded complex.

## Concrete next moves

1. **Identify the bridge.** Read VandeBogert 2025 (the Koszulness criterion Almousa–Lu use) and look for whether their "ribbon Schur module" framework admits a deformation/curvature interpretation that recovers BGG–Verma at the appropriate parameter. Speculative connection to the non-homogeneous Koszul duality (arXiv:2511.05140, browse 2) where q is treated as curvature in a curved dg-algebra.

2. **Compute B_3 to test the conjecture.** The B_2 result is a single example. For B_3, check whether bigraded non-acyclicity of BGG–Verma at non-spin λ continues to predict the locus of negative coefficients.

3. **Find a 0-Hecke instance of bigraded non-acyclicity.** All known H_*(0)-tower categorifications give *positive* Hopf algebras (NSym, QSym, BQSym, etc.). Conjecture 4.1 from `~/projects/proofs/2026-05-06-remark-47-obstruction.md` predicts that there should also be 0-Hecke-style towers whose Almousa–Lu-style cochain complexes fail bigraded acyclicity, and those should categorify "Lusztig-style" Hopf algebras with negative coefficients in some basis. **No such example is currently known.** The first one would be a major construction.

## How this interacts with existing connections

* **`derived-krob-thibon.md`:** that file documents the *acyclic* ribbon complex (positive endpoint). Add a cross-reference to here for the non-acyclic side.
* **`r-matrix-as-LR-symmetry.md`:** the R-matrix being idempotent at q=0 is the same phenomenon at the level of crystals/braiding. The acyclicity-vs-non-acyclicity dichotomy refines this: at q=0 the braiding becomes a projection, but whether the resulting categorification is acyclic depends on a *finer* grading datum (long/short bidegree, or column count, or whatever the relevant internal grading is).
* **`crystal-skeleton-as-qsym-crystal.md`:** the QSym-side crystal is the K_0^{fd}-level shadow of the acyclic / positive endpoint. Whether there is an analogous "crystal of the non-acyclic boundary" — some structure on Verma supports' bidegrees — is a new question.
* **`q-zero-categorification-is-frobenius.md`:** that file is a Frobenius-reciprocity-flavored thesis at the K_0 level. The current connection upgrades it to the derived/bigraded level: the thesis becomes "any tower with parabolic Frobenius reciprocity gives an *acyclic* internally bigraded categorification." Towers where Frobenius reciprocity fails (or fails in a graded sense) should give non-acyclic categorifications and possibly negative coefficients.

## Status

The conjectured bridge is unverified. Endpoints A and B are both rigorous (Almousa–Lu Theorem 5.6 is a published result; the Remark-4.7 BGG-Verma reformulation is proven in `~/projects/proofs/2026-05-06-remark-47-obstruction.md`). The unification is at the level of structural claim, not theorem. But it is a *specific* enough claim to test (computation of B_3, attempted construction of a 0-Hecke-side non-acyclic instance).
