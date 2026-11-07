# $T^{\mathrm{obs}}_\delta$ lives on the SELECTION-FUNCTION OPFIBRATION, not on $\mathrm{Lens}_s$

**Created** 2026-05-18 (Day 23 P_DEEP #2 verdict).
**Companion to** `connections/ghani-grading-payoff-vs-observation-mirror.md` (Day 22).
**Full worked example & proof** `proofs/2026-05-18-Tobs-delta-worked-example.md`.

## The verdict in one sentence

The observation-side grading $T^{\mathrm{obs}}_\delta$ is a graded family of **vertical, strict-Nash-monoidal endomorphisms of the parametrised-lens / selection-function opfibration $\int\!\mathrm{Sel} \to \mathrm{Lens}$ of Capucci–Ghani–Ledent–Nordvall-Forsberg (arXiv:2105.06763), over the identity on the base $\mathrm{Lens}$** — **NOT** a graded comonad on $\mathrm{Lens}_s$, **NOT** profunctor-valued. Shape (2) of the three candidates.

## The "trivial-on-lens-layer" lemma

The reason shape (1) ("graded comonad on $\mathrm{Lens}_s$") is wrong **as stated** is structural, not technical:

> The arena (= the underlying lens $\ell$) does not change under $T^{\mathrm{obs}}_\delta$.

$T^{\mathrm{obs}}_\delta$ shrinks the *selection function* (= set of allowed strategies on the parameter object) by restricting to $\sim_\delta$-measurable strategies. The lens itself — its observation type $X$, action type $Y$, coplay map, etc. — stays unchanged. Therefore, at the level of $\mathrm{Lens}_s$, $T^{\mathrm{obs}}_\delta$ is **forced to be the identity functor**. Shape (1) is satisfied **vacuously**.

The genuine content lives one categorical level **up** — on the total space $\int\!\mathrm{Sel}$ of the selection-function opfibration. At that level, $T^{\mathrm{obs}}_\delta$ is a non-trivial graded family of vertical endomorphisms, with strict counit ($T_0 = \mathrm{Id}$) and *lax* comult ($T_{r+s} \subsetneq T_r T_s$ strict in general). Fiberwise, this gives a chain of idempotent restriction operators on $\mathrm{Sel}(\ell)$ — a "graded filtration" of selection functions, in the language Ghani's Lemma 3.6 sets up on the payoff side.

## Why this matters for the mirror with Ghani 2025

Ghani's $T_\varepsilon$ (payoff side, monad-flavor closure) is genuinely an endofunctor on $\mathrm{Op}$ in the morphism direction — Lemma 3.6 of Ghani 2025 establishes the graded-structure laws at the level of selection functions over arenas.

My $T^{\mathrm{obs}}_\delta$ (observation side, comonad-flavor restriction) is **NOT** an endofunctor on $\mathrm{Op}$ in the morphism direction. It is a vertical endomorphism of the opfibration over the identity in the base. So the **mirror is real but ASYMMETRIC**:

| | Ghani $T_\varepsilon$ (payoff) | Rick $T^{\mathrm{obs}}_\delta$ (observation) |
|---|---|---|
| Grading monoid | $(\mathbb{R}_{\geq 0}, +, 0)$ | $(\mathbb{R}_{\geq 0}, +, 0)$ |
| Polarity | Monad (closure) | Comonad (restriction) |
| Unit law | $T_0 G = G$ | $T_0 G = G$ |
| Monotonicity | $\varepsilon \leq \varepsilon' \Rightarrow T_\varepsilon \subseteq T_{\varepsilon'}$ | $\delta \leq \delta' \Rightarrow T_{\delta'} \subseteq T_\delta$ |
| Lax law | $T_\varepsilon T_\delta \subseteq T_{\varepsilon+\delta}$ (mult) | $T_{\delta+\delta'} \subseteq T_\delta T_{\delta'}$ (comult) |
| Categorical home | endofunctor of $\mathrm{Op}$ on morphisms | vertical endo of $\int\!\mathrm{Sel}$ over $\mathrm{Lens}$ |
| Each fixed grade | not idempotent in general | idempotent ($T_r^2 = T_r$) |

The asymmetry in the bottom rows is structural: the observation-side grading is *poset-flavored* (each $T_r$ is a closure operator on a power set), whereas the payoff-side grading is genuinely functorial in the morphism-extension sense.

## Why this matters for the WP2 / AI4Maths grant pitch

Two implications:

1. **Concede shape-(1) framing.** The "graded comonad on observations" pitch as originally written was *at the wrong categorical level*. The comonadic flavor exists but it lives in the fibers of the opfibration, not on the lens layer. Reframing for any external talk/paper: position $T^{\mathrm{obs}}_\delta$ as a graded vertical endomorphism of CGLN's opfibration; mention comonadic-flavor fiberwise as a corollary.

2. **Confirm Neil's instinct, partially.** Neil was right that "arrows/profunctors may be cleaner than (co)monadic constructions" — the right framework is the opfibration of CGLN, which already does most of the heavy lifting. Comonadic packaging is fiber-level corollary, not primary. **But profunctor-valued (shape 3) is still wrong** — it doesn't capture the restriction structure naturally. The opfibration sits in between (co)monadic and profunctor framings, and is the right answer.

## Open questions / next moves

- **OQ-Tobs-multi-arena.** Honest multi-arena extension via $\mathrm{Lens}^{\mathrm{filt}}$ (sub-opfibration of filtered arenas with filtration-preserving lens morphisms). Defined the framework in `proofs/2026-05-18-Tobs-delta-worked-example.md` §5.1 but not written precisely.

- **OQ-Tobs-equilibrium-preservation.** The strict Nash-monoidal compatibility (§4.1 of worked example) should yield: "Equilibria of $T^{\mathrm{obs}}_\delta G$ are exactly the $\sim_\delta$-measurable equilibria of $G$, and CGLN Theorem 1 (Nash-from-monoidal) lifts compositionally to the restricted setting." Easy follow-up; worth stating as a Proposition in a paper draft.

- **OQ-Tobs-three-page-note.** PROVE.md stretch goal: draft a 3pp note "Observation-side grading on parametrised lenses: a worked example" for Neil + Robin. Structure proposed in worked-example §8.

## Calibration carry-forward

- **Examples-driven beat abstraction-first** (Neil's stance, confirmed). The "graded comonad on $\mathrm{Lens}_s$" framing was naive; one worked example exposed the wrong-level issue in a single session.
- **Concede terminology, commit to structure.** The conceded "graded comonad" framing turned out to be at the wrong level entirely. The structural claim — vertical opfibration endomorphism — is stronger, more accurate, and more useful for the WP2 pitch.
- **Polarity check FIRST** (F1 of PROVE.md). $T^{\mathrm{obs}}_\delta G \subseteq G$ is the right polarity; locked in §2 before doing any law-checking. Saved time.
- **Sub-agent verification for small-case enumeration** (PROVE.md "use computation to test, not to prove"). All grade-pair comult inclusions verified at $n = 4$ via direct enumeration; Hamming-ball ruled out as filtration parameter via transitive-closure computation. Reasoning stayed mine; computation just rejected wrong design.
