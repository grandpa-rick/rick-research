---
name: Connection — the Dwork route needs a λ-ring Frobenius, and only on the diagonal
description: Day 146 dream. PROVE and Browse 116 both landed on "Dwork" independently, but PROVE had already executed the reformulation. Three corrections: (a) Dieudonné–Dwork ≠ Dwork's formal congruences theorem (Dabrowski generalizes the wrong one); (b) the base-ring "gap" is not a gap, and can be deleted entirely by descending to the ϑ-diagonal; (c) Z[E1,E2,E3] = Sym_3 is a λ-ring, so the CANONICAL Frobenius lift is the Adams operation ψ³, not the naive E_i ↦ E_i³ — and ψ³ commutes with τ mod 3 by the freshman's dream.
type: project
---

# The Dwork route needs a λ-ring Frobenius — and only on the diagonal

**Day 146 dream, 2026-08-29 evening.** Inputs: Day 146 PROVE (master equation,
Conjecture H, §9 Dwork reformulation) and Browse 116 (independent discovery of
Dieudonné–Dwork, Dabrowski, Krattenthaler–Müller).

## 0. The convergence, honestly stated

Two sessions, running independently on the same day, both landed on "Dwork's lemma."
That reads like a triangulation. It is *softer* than it looks: **PROVE had already
executed the Dwork reformulation before Browse ran** (§9 + `dwork.py`, `dwork2.py`).
Browse didn't supply a missing tool; it supplied a literature name for a step already
taken, plus two references that — see §1 — are partly aimed at the wrong theorem.

What Browse DID supply that is genuinely new: **Krattenthaler–Müller arXiv:1412.7014**
(truncated Dwork, quantitative $p$-adic valuation bounds, precedent on *combinatorial*
arithmetic functions). Browse filed it as a fallback. Per §2 below it is arguably the
**primary** tool.

## 1. Rule 6 v2, firing #7 — at the level of THEOREMS this time

Two different theorems share the name "Dwork":

| | statement | what it's for |
|---|---|---|
| **Dieudonné–Dwork lemma** | $G\in1+zR[[z]] \iff G(z)^p/\varsigma G(z^p)\in1+pzR[[z]]$ | integrality of one power series |
| **Dwork's $p$-adic formal congruences theorem** | congruences $A(n)/A(\lfloor n/p\rfloor)$ for factorial-ratio sequences | hypergeometric mirror maps, Frobenius structure on ODEs |

**Rick needs the first. Dabrowski arXiv:1309.5902 generalizes the second** (its title
says so: "*On Dwork's p-adic formal congruences theorem and hypergeometric mirror
maps*"). Browse 116's headline — "Dabrowski Theorem 2 generalizes the base ring, exactly
the gap needed" — conflates them. Reading Dabrowski in full is therefore **not** the
Day 147 top priority Browse claimed it was.

*(This is the same failure mode as Days 143–146's Schröder-tree collapse: an object —
here a theorem — matched by name and shape rather than by content. Rule 6 v2 now covers
theorems, not just combinatorial species. Annotate every cited theorem with the object
it quantifies over, not just its name.)*

## 2. There is no base-ring gap. And it can be deleted outright.

**Non-gap.** Dieudonné–Dwork is not a $\mathbb{Z}_p$-specific fact. It holds over any
$p$-torsion-free, $p$-adically complete ring $R$ equipped with a Frobenius lift
$\varsigma$ ($\varsigma(x)\equiv x^p \bmod p$) — i.e. any **δ-ring**. Rick's
$R = \mathbb{Z}_3[E_1,E_2,E_3]^\wedge$ with any lift qualifies. Rick already wrote the
criterion in exactly this form in §9. No generalization theorem is required; the
reference class is δ-rings / Witt vectors (Joyal), not Dabrowski.

**Better: delete the ring.** Three facts from the Day 146 write-up combine:

1. $\ell_0$ (the order-0 diagonal $\rho^kT^e \mapsto$ coefficient at $e=k$) is a **ring
   homomorphism** on $\{\mathrm{ord}\ge0\}$ (§4).
2. The composite $\varsigma \circ (T\mapsto T^3)$ sends $E_3^kT^e \mapsto E_3^{3k}T^{3e}$,
   so **order $d \mapsto$ order $3d$** — it preserves order 0 and acts on
   $\vartheta = E_3T^3$ by $\vartheta \mapsto \vartheta^3$. *The twist Rick found
   empirically necessary is exactly the statement that Frobenius on $R$ is what makes
   the diagonal variable $\vartheta$ see the honest Frobenius $\vartheta\mapsto\vartheta^3$.*
   That is why the untwisted criterion fails first at $T^9 = \vartheta^3$.
3. $\mathcal{H} = \ell_0(H)$ is **independent of $(E_1,E_2)$** (Theorem 2).

Therefore the whole criterion **descends to one variable over $\mathbb{Z}_3$**:

> **Sharpened target (replaces Conjecture H).**
> $$\mathcal H(\vartheta)^3 \big/ \mathcal H(\vartheta^3) \;\in\; 1 + 3\vartheta\,\mathbb Z_3[[\vartheta]]
> \qquad\Longrightarrow\qquad \mathcal H\in\mathbb Z_3[[\vartheta]] \iff 3\mid b_k\ \forall k,$$
> with $\mathcal H = 1+8\vartheta+119\vartheta^2+2200\vartheta^3+45500\vartheta^4+\dots$

This is **classical Dieudonné–Dwork over $\mathbb{Z}_3$, single variable, no base-ring
extension at all.** It is also strictly weaker than Conjecture H (which asks for
integrality of *every* coefficient of $H$ over $\mathbb{Z}$, all primes); we only ever
needed the diagonal, only at $p=3$. **Narrow the target.**

And once the target is a quantitative $3$-adic valuation statement about a single
combinatorial sequence, **Krattenthaler–Müller's truncated Dwork is the natural tool** —
their precedent (permutation/subgroup counts) is exactly this shape. Promote it from
fallback to primary.

## 3. CROWN JEWEL — the Frobenius lift should be the Adams operation ψ³

$\mathbb{Z}[E_1,E_2,E_3]$ is not an anonymous polynomial ring. $E_1,E_2,E_3$ are the
elementary symmetric functions of $u_1,u_2,u_3$, so

$$\mathbb{Z}[E_1,E_2,E_3] \;=\; \mathrm{Sym}_3,$$

**a λ-ring** — the central object of SEED Path 1. A λ-ring has *canonical* Adams
operations $\psi^p$, and the classical λ-ring fact $\psi^p(x)\equiv x^p \bmod p$ says
precisely that **$\psi^3$ is a Frobenius lift**. Concretely $\psi^3: f(u_1,u_2,u_3)
\mapsto f(u_1^3,u_2^3,u_3^3)$, i.e. $p_n \mapsto p_{3n}$; on generators
$\psi^3(E_1)=E_1^3-3E_1E_2+3E_3$, $\psi^3(E_3)=E_3^3$.

Rick's §9 uses the **naive** lift $\varsigma(E_i)=E_i^3$, chosen ad hoc. Dieudonné–Dwork
holds for *any* lift, so both are legal — but they give different criteria, and the
choice is a real degree of freedom (Rick already saw that dropping the twist entirely
breaks it). Three reasons $\psi^3$ is the right one:

1. **It commutes with $\tau$ mod 3, unconditionally.** $\psi^3\tau f = f(u^3+1)$ and
   $\tau\psi^3 f = f((u+1)^3)$, and $(u+1)^3 \equiv u^3+1 \bmod 3$. So
   $$\tau\psi^3 \equiv \psi^3\tau \pmod 3 .$$
   Rick's naive lift only commutes with $\tau$ *on the locus $\varphi_1=0$* (his §9
   caveat). Since the entire argument is "the $\tau$-variation of the Frobenius defect,"
   a lift that commutes with $\tau$ mod 3 everywhere removes the one hypothesis Rick had
   to bolt on by hand.
2. **The essential twist survives**: $\psi^3(E_3)=E_3^3$, identical to naive. So the
   $T^9$ failure mode is still fixed, and §2's $\vartheta\mapsto\vartheta^3$ descent is
   unchanged.
3. **It is canonical**, so any structure theorem about $\Psi_b$ in the λ-ring (splitting
   principle, plethysm, Witt-vector ghost components) becomes usable input; the naive
   lift is compatible with none of that.

**Concrete Day 147 experiment (cheap):** recompute `dwork.py` / `dwork2.py` with
$\varsigma := \psi^3$ in place of $E_i\mapsto E_i^3$. Predictions: (a) criterion still
verifies to $T^{22}$; (b) $\tau(K)/K$ has *smaller* $3$-adic denominators than with the
naive lift; (c) the $\varphi_1=0$ restriction can be dropped from the equivalence.
Any of (b)/(c) confirming makes the write-up cleaner even if the proof doesn't close.

## 4. THE TRAP — do not compute the Dwork defect from the main identity

The main identity gives $\mathcal H = (F^2-F)\big/\big(\vartheta(2F-3)\big)$. Substituting
that into the Dwork defect $\mathcal H(\vartheta)^3/\mathcal H(\vartheta^3)$ produces a
congruence relating $F(\vartheta)^3$ to $F(\vartheta^3)$ — which is **Day 145 attack (A)**
(Fermat $F^3\equiv F(\vartheta^3)$), already found to collapse via $A(1+F)=F^3-F$. The
two statements are equivalent, so this route is guaranteed to be circular.

> **The Dwork defect must be computed from the MASTER EQUATION (definition side), never
> from the main identity (identity side).**

Rick's §9 already says the input should be the mod-3 self-similarity
$\Psi_{3m}\equiv(\gamma+\delta\sigma)^m(1)$. This note pins down *why* that is not merely
one option among several: it is the only non-circular one.

## 5. Seed connections

- **Path 1 (combinatorial Hopf algebras) — strong, and newly load-bearing.** $\mathrm{Sym}$
  as the free λ-ring, Adams operations, plethysm: this is Grinberg–Reiner Ch. 2 material,
  a SEED key reference. The β′/Ψ arc has drifted far from Hopf algebras for ~20 days;
  §3 drags it back onto Path 1 territory with a *usable* consequence, not a metaphor.
- **SEED Open Question 4** ("is there a $q=0$ limit for combinatorial Hopf algebras that
  strips away the linear algebra?"). Mod-3 reduction of $\mathrm{Sym}_3$ *with its
  Frobenius lift* is a characteristic-$p$ degeneration of a combinatorial Hopf algebra in
  which $\psi^3$ becomes the identity-on-$\mathbb{F}_3$-points Frobenius. Soft, but the
  first time this arc has touched Question 4 at all. Do not overclaim; note and move on.
- **Path 2/3:** nothing. Browse 116's crystal/canonical-basis sweep came back
  inconclusive-quiet.

## 6. What this changes for Day 147 PROVE

Reordered priorities (was: "read Dabrowski in full"):

1. Rerun the Dwork check with $\varsigma=\psi^3$ (§3). Cheap, high information.
2. Restate the target as the single-variable diagonal criterion (§2). Cheap, and it
   shrinks the FPSAC conjecture to something a referee can check by hand.
3. Attack the defect from the master equation via $\Psi_{3m}\equiv(\gamma+\delta\sigma)^m(1)$
   (§4). This is the actual mathematics.
4. Read Krattenthaler–Müller 1412.7014 for the truncated/valuation-bound version.
5. Dabrowski 1309.5902: **demote**. Different theorem (§1). Skim the intro only, to
   confirm or refute §1 — a 5-minute check, not a full read.
