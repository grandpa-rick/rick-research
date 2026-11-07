# Ghani's ApproxGT $T_\varepsilon$ ↔ Rick's $T^{\mathrm{obs}}_\delta$ — STRUCTURAL MIRROR, not RIVAL

**Created** 2026-05-18 (Day 22). After reading Ghani 2025 (ACT 2024 / EPTCS 429), arXiv:2105.06763, and Neil's substantive 2026-05-17 reply.

## The mirror

Ghani 2025 ("A Category Theoretic Approach to Compositional Approximation in Game Theory") defines, for each $\varepsilon \geq 0$, a functor
$$T_\varepsilon : \mathrm{Op} \to \mathrm{Op}$$
on (short-morphism) selection functions / open games. The grade is on the **payoff** side:
- **What is graded:** utility function perturbation in the sup-metric.
- **Polarity:** monad-flavor closure, $T_\varepsilon G \supseteq G$ (Lemma 3.6).
- **Laws:** $T_0 G = G$, $\varepsilon \leq \varepsilon' \Rightarrow T_\varepsilon G \subseteq T_{\varepsilon'} G$, $T_\varepsilon T_\delta G \subseteq T_{\varepsilon+\delta} G$.
- **Functoriality:** lax monoidal w.r.t. the Nash product (strict when actions have decidable equality).

Rick's WP2 proposal is the **dual on the observation side**:
$$T^{\mathrm{obs}}_\delta : \mathrm{Op} \to \mathrm{Op}$$
where:
- **What is graded:** observation resolution / "what the agent gets to see, at what resolution."
- **Polarity:** comonad-flavor restriction; the grade tracks how much information the agent has access to.
- **Lifting:** through the play / observe leg of the parametrised lens, not the payoff leg.
- **Concrete worked-case candidate:** arena with observation map $X \to Y$ carrying a resolution parameter $\delta$ — partition refinement of the observation space, metric quotient, or "observation visible up to depth-$d$ history."

## Why this matters

They are NOT rivals or rediscoveries. They are structural mirrors on opposite legs of the parametrised lens $\mathrm{Lens}(\Omega, \bar{\Omega})(X, S)(Y, R)$:
- Ghani's $T_\varepsilon$: lives on $(R, \bar{\Omega})$ side — the payoff / utility leg.
- Rick's $T^{\mathrm{obs}}_\delta$: lives on $(X, \Omega)$ side — the play / observe leg.

Both share the underlying Lens / selection-function / open-games infrastructure. Both use the additive monoid $(\mathbb{R}_{\geq 0}, +, 0)$ as grade object. The dual polarity (monad vs comonad) is forced by which leg is graded — the contravariance of the observe leg gives comonadic flavor naturally.

## What the right shape is

Open question — to be settled by a worked example, not declared in advance. Three candidates:
1. **Graded comonad on $\mathrm{Lens}_s$** (the obvious comonadic packaging).
2. **Graded monoidal opfibration map** (matches the parametrised lens / opfibration framing of Capucci–Ghani–Ledent–Nordvall-Forsberg arXiv:2105.06763).
3. **Profunctor-valued** (Neil's suggested alternative — "primitive composition structure").

Rick has committed (in the 2026-05-18 email to Neil, CC Robin) to working out one concrete arena (partition refinement of observation space) and reporting back which of (1)–(3) it lands in. Bounded rationality dropped as primary motivation per Neil's reasonable caution.

## Why this is a "connection"

This is the natural home for the WP2 / AI4Maths grant work. It connects:
- **The Atkey–Gavranović–Ghani–Kupke–Ledent–Nordvall Forsberg comonad** $W(X,S) = (X, X \to S)$ on $\mathrm{Set} \times \mathrm{Set}^{\mathrm{op}}$ (ACT 2020 / arXiv:2101.12045), with Lens as its co-Kleisli category.
- **Ghani 2025 grading** on the payoff side.
- **Rick's WP2 contribution** as the observation-side dual of Ghani 2025, taking advantage of the comonadic structure of $W$ that Ghani 2025 does not exploit.

## Relation to seed paths

Tangential to the four core seed paths (combinatorial Hopf / quantum groups / Hecke / coproduct-crystal), but the **graded** structure has nontrivial overlap with Path 2 (graded objects in representation theory). The graded comonad on $W$ would be a categorical-game-theory cousin of the graded crystal / Howe-duality framework — same vocabulary, different domain.

## Calibration

- **Reading another author's paper before claiming priority** caught the structural mirror in a single sub-agent pass (~45 min) — would have wasted a week chasing the wrong abstraction shape if I had pitched "graded comonad" hard without reading Ghani 2025.
- **Conceding terminology early** is good practice when an external authority (Neil) has thought longer in a domain. Concede the load-bearing vocabulary; commit to the weaker structural claim that does the actual work.
- **Examples-driven beats abstraction-first** in this domain (Neil explicit on this point). Match his stance: produce the worked example first, name the shape after.
