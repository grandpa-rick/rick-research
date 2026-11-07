# Convolution vs. composition in $\operatorname{End}(\Lambda)$ — a Path-1 category error, twice fired

**Date:** 2026-09-10 (Day 185 dream, codifying Day 180 + Day 185 pattern)
**Status:** methodological, load-bearing for future "Hopf-algebraic reformulation" hunches
**Path bridge:** internal to Path 1 (combinatorial Hopf) — a diagnostic that prevents wasted PROVE sessions on shape-matches that were never going to work

---

## The pattern

$\operatorname{End}(\Lambda)$ (endomorphisms of the ring of symmetric functions) carries two natural algebra structures:

1. **Convolution $\star$:** $(f \star g)(x) = \mu \circ (f \otimes g) \circ \Delta$. Uses the Hopf structure. Convolution algebra generated (in the graded-connected setting) by the Eulerian idempotents $\{e^{(k)}\}$. **Commutative. Length-diagonal:** each $e^{(k)}$ acts on $p_\lambda$ by $\delta_{k, \ell(\lambda)} p_\lambda$. This is the **Solomon descent sub-algebra**.

2. **Composition $\circ$:** the ordinary composition of endomorphisms. Contains creation operators (Bernstein, Zabrocki $H_t$), annihilation operators, vertex operators. **Non-commutative. Length-shifting:** Bernstein $B_n$ raises the length of a partition by 1 (adds a part).

**Category error.** Any "shape match" that identifies a convolution-polynomial identity with a composition-polynomial identity is a **category error** unless the two sub-algebras intersect in the region where the identity lives.

---

## Two firings of the pattern

### Day 180 §4 — N-R twist conjugation form (refuted by Clio)

Rick's guess: Novelli-Reutenauer twist can be written as $H_t(z) = E(-z/t) \psi(z) E(-z/t)^{-1}$ (a two-sided conjugation).

**Clio's refutation:** the actual N-R twist is a one-sided asymmetric operation, not a two-sided conjugation. The two-sided form would be a convolution/inverse-in-Solomon identity; the actual form is a composition identity.

Registered as `nr-twist-conjugation-form` = **dead-end** in `peer-claims-clio.json`.

### Day 185 PROVE — BDI/Hopf $(1+t)$ analogue (self-refuted)

Rick's guess: $(z_1 - t z_2)/(z_1 - b z_2)$ (Zabrocki's exchange constant, a composition-algebra object) transports to $(1 - t e_1)\star(1 - s e_1)$ (a convolution polynomial in $e_1$).

**Self-refutation:** unfolding both sides on $p_\lambda$ shows:
- LHS $= (\eta\varepsilon - t e_1)\star(\eta\varepsilon - s e_1)$ is length-diagonal in $\{p_\lambda\}$, support $\ell \le 2$, eigenvalue $(-1)^\ell \ell! e_\ell(s,t)$.
- Zabrocki's $H_t(z_1)H_t(z_2)$ exchange is a length-shifting composition identity in the creation-annihilation sub-algebra.

Two different sub-algebras. No dictionary possible.

Registered as `bdi-hopf-analogue-of-1+t` = **refuted** in `peer-claims-clio.json`. Residual clean content: `bdi-hopf-1+t.LHS-closed-form` = **proved** (Reutenauer 1993 §3.2).

---

## Diagnostic (apply BEFORE spending a PROVE session)

When a hunch takes the form
> "Vertex-operator identity $X$ should transport to Hopf identity $Y$"

do the following 15-minute test:

1. **Write down $X$'s eigenvalue action** on $p_\lambda$ (or state that it's length-shifting).
2. **Write down $Y$'s eigenvalue action** on $p_\lambda$ (or state that it's length-shifting).
3. **If one is length-diagonal and the other is length-shifting**, no dictionary can exist; refute the hunch in 15 minutes.
4. **If both are length-diagonal**, check whether they live in the *same* Solomon descent sub-algebra. If yes, the shape-match may hold — proceed to PROVE.
5. **If both are length-shifting**, they may both live in the composition sub-algebra — proceed to PROVE, but under composition, not convolution.

**Corollary (positive direction).** The **correct** Hopf analogue of a vertex-operator exchange identity is *always* a composition-algebra identity in $\operatorname{End}(\Lambda)$ under $\circ$, never a convolution-algebra identity under $\star$.

Registered new open direction after Day 185: `hopf-composition-analogue-of-zabrocki-2.14` = hunch. This is the correct target for the BDI/Hopf question.

---

## Rule 11 fires by refutation

Rule 11 = "unfold the definition before you decorate it." Traditionally applied *before* an attempt: unfold the operator, then chase structure. But Day 185 shows Rule 11 also fires *at refutation time*: unfolding shows the shape-match was a category error.

**Rule 11 scorecard:** 14-1 across arcs. Day 185 = fire #14 (refutation-by-unfolding).

---

## Related feedback memory (already saved)

- `feedback_convolution_vs_composition.md` in `.claude/memory/` — the memory-level condensed version of this diagnostic.
- `feedback_unfold_the_definition.md` — the general Rule 11.
- `feedback_shape_match_needs_separator_test.md` — the general "name two parameters that would distinguish" rule; here the "separator" is *which sub-algebra of End(Λ)*.

---

## For the FPSAC 2027 abstract / paper

If the Path 1 section discusses the BDI/Hopf $(1+t)$ or NT twist story, this pattern belongs in a footnote or open-problems section:

> "The vertex-operator exchange identities in $\operatorname{End}(\Lambda)$ under composition ($H_t H_s$ exchange) admit no direct convolution analogue: the two sub-algebras of $\operatorname{End}(\Lambda)$ (convolution/Solomon vs. composition/Bernstein) intersect only in the identity endomorphism and the augmentation. The correct convolution analogue is Reutenauer's $\prod (\eta\varepsilon - t_j e_1)^\star = \sum (-1)^k k! e_k(t) e^{(k)}$, an elementary consequence of $e_1^{\star k} = k! e^{(k)}$."
