# Compositional Game Theory — summary for WP2 / Neil Ghani correspondence

**Compiled:** 2026-05-17. For Rick's reply to Neil Ghani's pushback on the WP2 comonad framing.

## Foundational papers (downloaded to this directory)

1. **Ghani, Hedges, Winschel, Zahn** — *Compositional Game Theory*. LICS 2018. arXiv:1603.04641. **The foundation.**
2. **Hedges** — *The selection monad as a CPS translation*. 2015. arXiv:1503.06061. **Cleanest explanation of monadicity.**
3. **Hedges** — *Coherence for lenses and open games*. 2017. arXiv:1704.02230. **Defines teleological categories (counits without units).**
4. **Hedges** — *Morphisms of open games*. 2017. arXiv:1711.07059. **The symmetric monoidal double category with lenses as vertical 1-morphisms — Neil's "monoidal fibration over lenses."**
5. **Atkey, Gavranović, Ghani, Kupke, Ledent, Nordvall Forsberg** — *Compositional Game Theory, Compositionally*. ACT 2020. arXiv:2101.12045. **CRITICAL: graded arrows + W(X,S) = (X, X→S) comonad with Lens as co-Kleisli.**
6. **Ghani, Kupke, Lambert, Nordvall Forsberg** — *Probabilistic open games*. 2020. arXiv:2009.06831.
7. **Bolt, Hedges, Zahn** — *Bayesian open games*. 2023. arXiv:1910.03656.
8. **Hedges, Oliva, Winschel, Zahn** — *Higher-order decision and games*. 2014. arXiv:1409.7411.

Hedges' DPhil thesis "Towards Compositional Game Theory" (QMUL 2016) cited as [8] of LICS 2018 — not on arXiv; Robin can supply.

## The selection (co)functor

- Deterministic (Hedges 2015): $J_R X = (X \to R) \to X$ with $\eta x = \lambda k. x$.
- Generalized (Bolt-Hedges-Zahn, Escardó-Oliva): $J^P_R X = (X \to R) \to P X$. **This is Neil's $S X = (X \to V) \to P X$.**
- Strong monad on Set whenever $P$ is. Canonical: $\arg\max : (X \to \mathbb{R}) \to P X$.

## Why MONADIC, not comonadic

- Selection consumes a context (continuation $k : X \to R$) and produces a choice at $X$. Composition = continuation-monad bind.
- To be a comonad you'd need natural $\varepsilon : P X \to X$, i.e. a natural section of $X \to P X$. **No such natural map exists.**
- Refinement: $J \to K$ given by $\exists p = p(\varepsilon p)$ and $\max p = p(\arg\max p)$ — a monad morphism, not a comonad.

## Nash from monoidal structure

$J$ is strong and commutative → canonical tensor $\otimes : J X \times J Y \to J(X \times Y)$. Applied to two $\arg\max$ functions with a shared continuation $k : X \times Y \to \mathbb{R} \times \mathbb{R}$, the product $\delta_1 \otimes \delta_2$ returns exactly the **Nash equilibrium** profiles. Sequential composition = backward induction / SPE.

## Monoidal fibration over lenses

- LICS 2018 Lemma 1 (§III): the (play, coplay) pair is a $\Sigma$-indexed family of polymorphic lenses $(X, S) \to (Y, R)$.
- Hedges 2017: symmetric monoidal **double category**; objects = pairs of sets; horizontal 1-cells = open games; vertical 1-morphisms = **lenses**; 2-cells preserve best responses.
- Atkey et al. 2021: open games = $\mathrm{Fam}(\mathrm{Lens} \times \mathrm{Equib}(\mathrm{Lens}))$, with Equib a bimodule on the lens arrow.

## Comonadic structures on the observation/context side — THE RESCUE FOR WP2

(a) **Atkey et al. 2021, §3.2 Prop. 13:** $W(X, S) = (X, X \to S)$ is a comonad on $\mathbf{Set} \times \mathbf{Set}^{\mathrm{op}}$, with **Lens as its co-Kleisli category**. The entire data/observation layer of CGT is comonadic.

(b) **Teleological categories (Hedges 2017):** open games and lenses have counits without units — the "backward-looking" side has comonadic structure inheriting from the lens side.

(c) The contravariant coordinate ($S$ in $(X, S)$, $R$ in $(Y, R)$) is the natural home for comonadic / coeffectful structure.

## Graded structures

- Atkey et al. 2021 §4.2: **graded arrows** parameterise open games by strategies. Lax monoidal functor $A : P \to \mathrm{StrProf}(\mathcal{C})$.
- **No published graded selection comonad. No published graded $W$.**
- Plausible unwritten extension: grade $W$ by information content / resource budget / deliberation cost. **This is WP2's natural novelty slot.**

## Bottom line for WP2

- **Don't fight monadicity of $S$.** Selection is monadic. Period.
- **The comonad is on the lens / observation side, already published.** $W(X, S) = (X, X \to S)$, Atkey et al. 2021.
- **WP2 framing:** decision = monadic effect ($S$); observation = comonadic coeffect ($W$); grading on the observation side tracks resource / belief / refinement budget.
- **Plan-eval-act = distributive law between $S$ (monad) and $W_n$ (graded comonad).** This is the load-bearing piece.
