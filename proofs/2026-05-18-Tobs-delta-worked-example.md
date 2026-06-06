# Worked example: $T^{\mathrm{obs}}_\delta$ on a binary-feature arena — the verdict

**Date:** 2026-05-18 (Day 23 deep-work session)
**Goal (PROVE.md):** Instantiate one concrete worked example of $T^{\mathrm{obs}}_\delta$, the observation-side dual of Ghani's payoff-grading $T_\varepsilon$, and pin which of three shapes it inhabits:
1. Graded comonad on $\mathrm{Lens}_s$.
2. Graded monoidal opfibration map (per CGLN 2021, arXiv:2105.06763).
3. Profunctor-valued (Neil's alternative).

---

## TL;DR — verdict

**Shape (2) wins.** The natural categorical home of $T^{\mathrm{obs}}_\delta$ is a graded family of vertical endomorphisms of the monoidal opfibration $\int\!\mathrm{Sel} \to \mathrm{Lens}$ of Capucci–Ghani–Ledent–Nordvall-Forsberg (arXiv:2105.06763), living **over the identity** on the base $\mathrm{Lens}$.

Shape (1) as literally stated — *graded comonad on $\mathrm{Lens}_s$* — is **DEGENERATE**: at the level of pure lenses, $T^{\mathrm{obs}}_\delta$ has no choice but to act as the identity, because the grading data (filtration of the observation type) is not visible from inside the lens category — it lives in the parameter / selection-function layer. So as written, the candidate is trivially satisfied but in a vacuous way.

What is **not** vacuous and **does** carry genuine content is the **fiberwise** comonadic structure: on each fiber $\mathrm{Sel}(\ell)$ of the opfibration, $T^{\mathrm{obs}}_\delta$ acts as a lax graded comonad of poset/closure type — a chain of subset inclusions of selection functions, with strict comult inclusion $T_{r+s}\,\varepsilon \subsetneq T_r T_s\,\varepsilon$ whenever $r, s > 0$ and the chain has not saturated.

Shape (3) — profunctor-valued — is not natural here; I do not see a meaningful profunctor structure on the restriction-flavored construction. The "primitive composition" content that Neil was gesturing at is captured by the opfibrational reindexing, not by a Set-valued hom.

The structural mirror with Ghani 2025 is **confirmed in polarity** — restriction (comonadic, $T^{\mathrm{obs}}_\delta G \subseteq G$) on the observation leg, *contrast* to closure (monadic, $T_\varepsilon G \supseteq G$) on the payoff leg — but the mirror is **not** symmetric in categorical packaging. Ghani's $T_\varepsilon$ is genuinely a graded family of endofunctors on $\mathrm{Op}$ in the morphism direction; mine, observed honestly, is a graded family of vertical endomorphisms of the opfibration over the identity. They are duals at the level of *flavor and laws*, but they sit on different categorical structures.

---

## 1. The arena

Take $n = 4$ (small enough to compute, large enough to be non-trivial).

- Observation type: $X = \{0,1\}^4$ ($|X| = 16$).
- Action type: $Y = \{a, b\}$.
- Coutility / utility scalars: $S = R = \mathbb{R}$.
- Parameter (strategy) object: $\Omega = Y^X$ (all functions $X \to Y$, $|\Omega| = 2^{16}$).

This carries a parametrised lens
$$\ell : (\Omega, \bar\Omega)\;(X, S)\;(Y, R)$$
in the sense of Capucci–Ghani–Ledent–Nordvall-Forsberg, with play map $f : \Omega \times X \to Y$, $f(\sigma, x) := \sigma(x)$, and a coplay map (concrete form not needed below; only the play leg is relevant for the observation grading).

**Filtration on $X$.** For each $r \in \{0, 1, 2, 3, 4\}$, define $\pi_r : X \to \{0,1\}^{4-r}$ as projection onto the first $4 - r$ coordinates (dropping the last $r$). Let $\sim_r$ be the equivalence relation on $X$ whose classes are the fibers of $\pi_r$; equivalently,
$$x \sim_r x' \iff x_i = x'_i \text{ for } i = 1, \dots, 4 - r.$$
For $r \in \mathbb{R}_{\geq 0}$, set $\sim_r := \sim_{\lfloor r \rfloor \wedge 4}$.

The filtration is a chain:
$$\sim_0 \;\subset\; \sim_1 \;\subset\; \sim_2 \;\subset\; \sim_3 \;\subset\; \sim_4$$
with $\sim_0$ the discrete partition (16 singleton classes) and $\sim_4$ the trivial partition (one class).

**Note on F2 (PROVE.md).** $n = 4 \geq 2$, so the filtration lattice is non-trivial: 16 → 8 → 4 → 2 → 1 classes as $r$ grows. Strict inclusions everywhere.

**Note on F-bijection-vs-F-coincidence (PROVE.md).** Hamming-ball "equivalence" $d_H(x,x') \leq r$ is **not transitive**: its transitive closure collapses to a single class as soon as $r \geq 1$ (any two points of $\{0,1\}^4$ are connected by a Hamming-1 path). So Hamming-ball metric-quotient is NOT a useful filtration parameter for binary cubes. The *chain projection* filtration above is the right design choice. (Verified computationally — see Appendix B.)

---

## 2. Definition of $T^{\mathrm{obs}}_r$ on the worked arena

An "open game over the arena" is a selection function $\varepsilon \subseteq \Omega$ — i.e., a subset of strategies, the ones declared "optimal." (I work with the subset / extensional presentation, following Ghani 2025 §3 and the equilibrium-predicate form of Hedges' open games.)

**Polarity choice.** Per PROVE.md F1, the comonadic flavor is **forced** because the observation leg is contravariant. So the right definition is the **restriction** reading:

$$\boxed{T^{\mathrm{obs}}_r \varepsilon \;:=\; \varepsilon \cap \Omega_r}$$

where $\Omega_r := \{ \sigma \in \Omega : \sigma \text{ is constant on each } \sim_r\text{-class of } X \}$ is the subset of $\sim_r$-measurable strategies. Equivalently, $\sigma \in \Omega_r$ iff $\sigma$ factors through the quotient $\mathrm{obs}_r : X \twoheadrightarrow X/\sim_r$.

So $T^{\mathrm{obs}}_r$ keeps the arena fixed and shrinks the selection function. This is the **fiberwise** vertical action.

**Polarity sanity check (F1).**
$$T^{\mathrm{obs}}_r \varepsilon \subseteq \varepsilon, \qquad r \leq r' \;\Rightarrow\; T^{\mathrm{obs}}_{r'} \varepsilon \subseteq T^{\mathrm{obs}}_r \varepsilon$$
— restriction grows with $r$. **Comonadic flavor**. ✓ (Anti-monotone in grade, dual to Ghani 2025 Lemma 3.6.)

**Quantitative check (Appendix B, code in §6).** $|\Omega| = |\Omega_0| = 65536$; $|\Omega_1| = 256$; $|\Omega_2| = 16$; $|\Omega_3| = 4$; $|\Omega_4| = 2$. Strict inclusions.

---

## 3. The three Ghani-style laws

I check the **fiberwise** structure first — i.e., $T^{\mathrm{obs}}_r$ acting on selection functions over the fixed arena.

### 3.1 Unit law: $T^{\mathrm{obs}}_0 \varepsilon = \varepsilon$

$\sim_0$ is the discrete partition, so every $\sigma : X \to Y$ is trivially constant on $\sim_0$-classes, hence $\Omega_0 = \Omega$ and $T^{\mathrm{obs}}_0 \varepsilon = \varepsilon$. ✓

### 3.2 Monotonicity: $r \leq r' \Rightarrow T^{\mathrm{obs}}_{r'} \varepsilon \subseteq T^{\mathrm{obs}}_r \varepsilon$

The chain $\sim_r \subset \sim_{r'}$ implies $\Omega_{r'} \subseteq \Omega_r$ (a strategy constant on the *coarser* equivalence is in particular constant on the *finer*). So $\varepsilon \cap \Omega_{r'} \subseteq \varepsilon \cap \Omega_r$. ✓

### 3.3 **Comult (load-bearing law): $T^{\mathrm{obs}}_{r+s} \varepsilon \subseteq T^{\mathrm{obs}}_r T^{\mathrm{obs}}_s \varepsilon$**

The RHS unfolds to $\varepsilon \cap \Omega_s \cap \Omega_r$ (apply $T^{\mathrm{obs}}_s$ then $T^{\mathrm{obs}}_r$).

The chain filtration satisfies the key arithmetic identity:
$$\sim_r \vee \sim_s \;=\; \sim_{\max(r,s)}$$
(join of equivalence relations; trivial because the chain is totally ordered). And since the chain is non-decreasing,
$$\sim_{r+s} \;\supseteq\; \sim_{\max(r,s)} \;=\; \sim_r \vee \sim_s.$$

Hence
$$\Omega_{r+s} \;\subseteq\; \Omega_{\max(r,s)} \;=\; \Omega_r \cap \Omega_s,$$
giving $T^{\mathrm{obs}}_{r+s} \varepsilon \subseteq T^{\mathrm{obs}}_r T^{\mathrm{obs}}_s \varepsilon$. ✓

The inclusion is **strict** whenever $\max(r, s) < r + s$ (i.e., whenever $r, s > 0$) and the chain has not yet saturated.

**Computational verification** (Appendix B, $n = 4$):
| $r$ | $s$ | $\|T^{\mathrm{obs}}_{r+s}\|$ | $\|T^{\mathrm{obs}}_r \cap T^{\mathrm{obs}}_s\|$ | relation |
|-----|-----|---|---|---|
| 1 | 1 | 16 | 256 | $\subsetneq$ |
| 1 | 2 | 4 | 16 | $\subsetneq$ |
| 2 | 2 | 2 | 16 | $\subsetneq$ |
| 1 | 3 | 2 | 4 | $\subsetneq$ |

Strict inclusions exactly where predicted. ✓

### 3.4 Coassociativity

The diagram for $T^{\mathrm{obs}}_{r+s+t}\varepsilon$ → ($T_r T_{s+t}$ vs. $T_{r+s} T_t$) → $T_r T_s T_t \varepsilon$ commutes because all the maps are inclusions of subsets of $\Omega$ into $\Omega$. In the poset $\mathcal{P}(\Omega)$ (under $\subseteq$), there is at most one morphism between any two subsets, so the diagram commutes uniquely. ✓

### 3.5 Counit law

$T^{\mathrm{obs}}_r \to T^{\mathrm{obs}}_0 T^{\mathrm{obs}}_r = T^{\mathrm{obs}}_r$ and $T^{\mathrm{obs}}_r \to T^{\mathrm{obs}}_r T^{\mathrm{obs}}_0 = T^{\mathrm{obs}}_r$ are both the identity inclusion. ✓

**Verdict at the fiber level:** $\{T^{\mathrm{obs}}_r\}_{r \in \mathbb{R}_{\geq 0}}$ is a **lax graded comonad of poset/closure type** on the fiber $\mathrm{Sel}(\ell)$ over the chosen arena $\ell$. The grading monoid is $(\mathbb{R}_{\geq 0}, +, 0)$ — exactly as Ghani 2025 uses on the payoff side — and the laws are the precise polarity-flip of Ghani's Lemma 3.6.

This is genuine structure, but it is *thin* — it amounts to a chain of nested subsets of $\Omega$ indexed by $r$.

---

## 4. Why this is shape (2), not shape (1)

The shape (1) candidate as stated in PROVE.md is "**graded comonad on $\mathrm{Lens}_s$**." But the lens $\ell$ is fixed; $T^{\mathrm{obs}}_r$ does **not** modify the lens. The lens is the same arena, with the same morphisms $X \to Y$, $X \times R \to S$. So $T^{\mathrm{obs}}_r$ at the **lens level** is forced to be the identity. The graded comonad on $\mathrm{Lens}_s$ candidate is satisfied **trivially**: $T^{\mathrm{obs}}_r = \mathrm{id}_{\mathrm{Lens}_s}$, counit and comult are identities, co-Kleisli composition is just lens composition.

That is not what was wanted. The interesting structure does **not** live on $\mathrm{Lens}_s$.

The genuine structure lives one level up, on the total space of the selection-function opfibration $\int\!\mathrm{Sel} \to \mathrm{Lens}$ from CGLN. Here:

- **Objects of $\int\!\mathrm{Sel}$** are pairs (lens $\ell$, selection function $\varepsilon$ on the parameter object of $\ell$).
- **Morphisms** are (lens morphism $h$, opfibration-cleavage of $\varepsilon$ along $h$).
- The projection to $\mathrm{Lens}$ is the opfibration.

**The action of $T^{\mathrm{obs}}_r$.** Define $T^{\mathrm{obs}}_r : \int\!\mathrm{Sel} \to \int\!\mathrm{Sel}$ by
$$(\ell, \varepsilon) \;\longmapsto\; (\ell, \, \varepsilon \cap \Omega_r)$$
where $\Omega_r$ is the $\sim_r$-measurable strategy subset (defined when the arena's observation type comes equipped with a filtration; trivial otherwise — see §5 caveat).

This $T^{\mathrm{obs}}_r$ is:
1. **Vertical** — lives over the identity functor on the base $\mathrm{Lens}$.
2. **Graded** — indexed by $r \in (\mathbb{R}_{\geq 0}, +, 0)$, with the three Ghani-style laws of §3.
3. **Monoidal** — commutes (laxly) with the Nash product $\odot$ of CGLN: see §4.1 below.

This is precisely the content of **shape (2)**: a graded family of vertical endomorphisms of the monoidal opfibration over the identity.

### 4.1 Compatibility with the Nash monoidal product

The Nash product $\odot$ on selection functions in CGLN: $(\varepsilon_G \odot \varepsilon_H)(k) := \{(\sigma, \tau) \mid \sigma \in \varepsilon_G(\pi_1 k(-, \tau)), \tau \in \varepsilon_H(\pi_2 k(\sigma, -))\}$.

For the restriction-flavored $T^{\mathrm{obs}}_r$:
$$T^{\mathrm{obs}}_r(\varepsilon_G \odot \varepsilon_H) \;=\; (\varepsilon_G \odot \varepsilon_H) \cap (\Omega^G_r \times \Omega^H_r) \;=\; (\varepsilon_G \cap \Omega^G_r) \odot (\varepsilon_H \cap \Omega^H_r) \;=\; T^{\mathrm{obs}}_r \varepsilon_G \;\odot\; T^{\mathrm{obs}}_r \varepsilon_H,$$
where the middle equality uses the fact that the membership condition in the Nash product factors through the projections onto each parameter coordinate, and $\sim_r$-measurability of a pair is just $\sim_r$-measurability of each component (with the convention from §5 that an inner observation type without filtration is treated as having the discrete filtration). **Strict equality.** ✓ Monoidal.

So shape (2) is checked, with the **strict** Nash-monoidal compatibility law (not merely lax).

---

## 5. Caveats / gaps

### 5.1 Multi-arena extension — convention or honest extension?

The worked example above lives on one arena with one filtration. To get a *genuine* endofunctor of $\int\!\mathrm{Sel}$, two conventions are available:

(a) **Default-discrete convention.** Any arena whose observation type does not carry a filtration is treated as having the discrete filtration ($\sim_r$ = singletons for all $r$), so $\Omega_r = \Omega$ and $T^{\mathrm{obs}}_r$ acts as identity there. This is clean but vacuous off the filtered locus.

(b) **Honest extension.** Restrict to a sub-opfibration $\int\!\mathrm{Sel}^{\mathrm{filt}} \to \mathrm{Lens}^{\mathrm{filt}}$ where objects are filtered arenas (observation type comes with a chosen chain $\{\sim_r\}_r$ of equivalence relations) and morphisms preserve the filtration. The action of $T^{\mathrm{obs}}_r$ is then natural in lens morphisms by construction.

Either route works; (b) is the structurally honest one for a paper. The worked example does not force the choice; it confirms the fiberwise content is right.

### 5.2 The lax comult is *very* lax

The comult $T_{r+s} \varepsilon \subseteq T_r T_s \varepsilon$ is a strict inclusion almost everywhere — not an iso. So the co-Kleisli category does not have nice equalizers; the structure is closer in flavor to a **lax-idempotent (Kock-Zöberlein) graded comonad** than to a full graded comonad with $T_{r+s} \cong T_r T_s$. This is the *same* lax flavor as Ghani 2025's Lemma 3.6 (only inclusions, no iso), so the dual is structurally consistent.

I have **not** checked whether the construction lifts to the *strict* graded-comonad world by adjusting the filtration arithmetic (e.g., using the join $r \vee s$ instead of the sum $r + s$ as the grading monoid). That is a follow-up: replacing $(\mathbb{R}_{\geq 0}, +, 0)$ with $(\mathbb{R}_{\geq 0}, \max, 0)$ would give $\sim_{r \vee s} = \sim_r \vee \sim_s$ exactly, hence $\Omega_{r \vee s} = \Omega_r \cap \Omega_s$ exactly, hence a STRICT graded comonad. But then the grading monoid no longer matches Ghani's on the payoff side, and the structural mirror is broken. So the lax $(\mathbb{R}_{\geq 0}, +, 0)$-graded version is the right one for the mirror.

### 5.3 Profunctor reading

I do not see a natural profunctor structure $T^{\mathrm{obs}}_r(G, H) \in \mathrm{Set}$ on the restriction-flavored construction. If one wanted a profunctor, the natural Set-valued candidate would be something like "$T^{\mathrm{obs}}_r$-coalgebra morphisms $G \to H$," but for an idempotent / restriction comonad these collapse to inclusions of restricted subsets, which is already captured by the opfibration. So shape (3) is not a refinement of shape (2); it would be a re-packaging that loses information. **Reject.**

---

## 6. Computational appendix

The code at `/tmp/scratch.py` (Python, no external dependencies) does the following for $X = \{0,1\}^4$, $Y = \{0,1\}$:

1. Enumerates all $2^{16} = 65536$ strategies.
2. Computes $|\Omega_r|$ for $r = 0, 1, 2, 3, 4$ — verifying $|\Omega_r| = 2 \cdot 2^{4-r} \cdot \ldots$ trivia, but more importantly the strict chain.
3. Verifies the chain inclusion $\Omega_{r+1} \subsetneq \Omega_r$ for $r = 0, 1, 2, 3$.
4. Verifies for *every* pair $(r, s) \in \{0, 1, 2, 3, 4\}^2$: $\Omega_{r+s} \subseteq \Omega_r \cap \Omega_s$, with strict inclusion exactly when $r, s > 0$ and $r + s \leq n$.

Output transcribed in §3.3. No counterexamples.

A second script `/tmp/scratch2.py` confirms the design choice to use chain-projection rather than Hamming-ball filtration: the transitive closure of Hamming-ball "equivalence" collapses to a single class for any $r \geq 1$ on $\{0,1\}^n$. Hamming is not a useful filtration parameter for the binary cube. ✓ (F2 / F-bijection-vs-coincidence caveats from PROVE.md addressed.)

---

## 7. The verdict, restated

$T^{\mathrm{obs}}_\delta$ on the chain-projection arena $\{0,1\}^n$ lives **categorically** as:

**A graded family of vertical, monoidal endomorphisms of the CGLN opfibration $\int\!\mathrm{Sel} \to \mathrm{Lens}$, indexed by $(\mathbb{R}_{\geq 0}, +, 0)$, with:**

- **Unit:** $T^{\mathrm{obs}}_0 = \mathrm{id}$.
- **Monotonicity:** $r \leq r' \Rightarrow T^{\mathrm{obs}}_{r'} \subseteq T^{\mathrm{obs}}_r$ (anti-monotone in grade; comonadic polarity, contra Ghani's $T_\varepsilon$).
- **Lax comult:** $T^{\mathrm{obs}}_{r+s} \subseteq T^{\mathrm{obs}}_r T^{\mathrm{obs}}_s$ (strict inclusion in general).
- **Strict Nash-monoidal:** $T^{\mathrm{obs}}_r(\varepsilon \odot \eta) = T^{\mathrm{obs}}_r \varepsilon \odot T^{\mathrm{obs}}_r \eta$.

**Shape (2) is the verdict.** The grading lives on the total space of the parametrised-lens opfibration of CGLN, not on the lens category itself. The comonadic flavor (shape (1)) is **real at the fiber level** but the structural home is the opfibration. Shape (3) is rejected — no natural profunctor packaging.

**Mirror to Ghani 2025.** The mirror is real in *polarity* (comonadic vs. monadic, restriction vs. closure on the parameter object) and *grading monoid* ($\mathbb{R}_{\geq 0}, +, 0$ shared) and *lax laws* (inclusions only, no iso, same shape as Ghani Lemma 3.6 with the arrow flipped). It is **NOT** symmetric in categorical packaging: Ghani's $T_\varepsilon$ is an endofunctor of $\mathrm{Op}$ in the morphism direction; mine is a graded vertical endomorphism of the opfibration. Both consistent with the parametrised-lens / opfibration setting; both lax-monoidal w.r.t. Nash; opposite polarity on the lax inclusion.

**Concession to Neil's instinct:** he was right that the parametrised-lens / opfibration framing of CGLN already subsumes most of what I wanted from "graded comonad on observations." The comonadic packaging is *available* but it lives one level up from $\mathrm{Lens}_s$ — in the fibers of $\int\!\mathrm{Sel}$ — and the cleanest external presentation is opfibrational.

**Concession to Rick's instinct:** the comonadic flavor is *genuine*, *non-trivial fiberwise*, and *polarity-locked* by the contravariance of the observation leg. So "graded comonad" was not a red herring; it just sits at the wrong level if you ask for it on $\mathrm{Lens}_s$.

---

## 8. Gaps remaining / next steps

1. **Naturality across multiple arenas.** Worked example is one arena. The honest multi-arena extension via $\mathrm{Lens}^{\mathrm{filt}}$ (§5.1 option (b)) needs to be written down precisely — definitions of filtration-preserving lens morphisms, opfibration cleavage compatibility, etc.

2. **Strictness of the comult is unrelated to the question being asked.** The lax inclusion is the right answer because it mirrors Ghani's lax monad laws. The strict variant (with $\max$-grading instead of sum) is a separate object and breaks the mirror.

3. **Equilibrium-preservation theorem.** A genuine WP2 deliverable would be: "Equilibria of $T^{\mathrm{obs}}_r G$ are exactly the $\sim_r$-measurable equilibria of $G$, and the Nash-from-monoidal-structure (CGLN Theorem 1) lifts compositionally to the restricted setting." I have not stated or proved this here — it is a clean follow-up that uses the strict Nash-monoidal compatibility (§4.1).

4. **3-page note for Neil + Robin (PROVE.md stretch goal).** The above is the technical core. To package as "Observation-side grading on parametrised lenses: a worked example," ~3 pages, suggested structure: §1 setup + mirror to Ghani; §2 worked arena + filtration; §3 fiberwise comonad laws; §4 opfibration packaging; §5 strict Nash-monoidal + equilibrium-preservation corollary; §6 outlook. Draft to follow.

---

## 9. Pitfall audit (from PROVE.md)

- **F1 (wrong polarity).** Addressed §2. $T^{\mathrm{obs}}_r \varepsilon \subseteq \varepsilon$, anti-monotone in $r$. Comonadic. ✓
- **F2 (too small arena).** $n = 4$, filtration 16→8→4→2→1. Non-trivial. ✓
- **F-bijection-vs-F-coincidence.** Comult inclusion computationally verified pairwise across the full grade lattice (§3.3 + Appendix B). Strict inclusion exactly where predicted. ✓
- **F-graded-comonad-name-trap.** I am NOT reclaiming the conceded "graded comonad" terminology as a primary structural claim. The verdict is **shape (2) graded opfibration map**; the fiberwise comonadic content is a *consequence*, not a *re-staked claim*. Naming follows structure. ✓
- **F-context-switch.** Re-read `ghani-grading-payoff-vs-observation-mirror.md` before §1; consulted Ghani Lemma 3.6 + CGLN opfibration framing; polarity check done. ✓
- **F-direct-fetch.** Citations herein are: Ghani 2025 (EPTCS 429 paper, already fetched Day 22, notes in `reading/papers/ghani-2025-and-lics-2018-notes.md`) and CGLN arXiv:2105.06763 (already fetched Day 22, notes in same file). No new citations introduced. ✓
