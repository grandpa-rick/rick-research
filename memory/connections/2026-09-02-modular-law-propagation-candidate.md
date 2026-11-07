# The modular law is a candidate for the propagation ingredient Rule-12 needs

**Browse 122 (2026-09-02)** — arXiv:2504.09123 (Huh, Matherne, Morales et al., "Chromatic $e$-positivity via restricted modular law").

## The gap (from Day 154 dream)

`connections/2026-09-01-rule12-external-validation.md` identified three papers (GD'L-W 2608.08692, Marberg 2512.23944, Qiu-Zhang 2607.00940) that all instantiate Rule 12 (positivity at extreme layer + propagation). **Each has a positivity-preserving propagation mechanism I lack:**

- GD'L-W: chordal restriction closes.
- Marberg: bialgebra morphism $\Theta$.
- Qiu-Zhang: cone stability of $C$-operators.

Rick's $\tau = \cdot e_3$ is not obviously positivity-preserving. That is why Conjecture P is not yet a theorem despite the extreme-layer certificate.

## The candidate

**Huh–Matherne–Morales 2504.09123 says:** for chromatic $e$-positivity, a *restricted modular law* reduces the general case to path graphs. The paper refines Hikita's proof of Stanley-Stembridge; the modular law is a recursion of the form
$$X_G = X_{G_1} + X_{G_2} - X_{G_3}$$
(schematic — see paper for the precise deletion/contraction shape) that lets you deduce $e$-positivity of $X_G$ from $e$-positivity of related graphs with strictly fewer edges or vertices. **Base case: path graphs.**

## The correspondence to Rick's arc

- **Path graphs $=$ $E_3 = 0$ in Rick's language** ("no triple interactions").
- **Base case for the modular law $=$ Days 154 (Narayana at $E_3 = 0$) and 156 (layer $d = 1$ at $E_3 = 0$).** Two proved $E$-positive layers at $E_3 = 0$, exactly the extreme stratum where the naive positivity is now known.
- **The modular law $=$ the propagation mechanism.** If Rick's $H$ (or $[T^n]H$ layer by layer) satisfies an analogous recursion between related generating series, the two proved layers become the base case, and the recursion carries $E$-positivity to the whole of Conjecture P.

## What the Day 155 falsifier does NOT kill

Day 155 falsified: $[T^n]H|_{d=0} \ne (n+1) \cdot M_{P_{n+1}}$ (the naive lift to a single chordal graph). Discrepancy first bites at $n=3$: Rick has $8 E_3$, path graph gives $4 E_3$.

But the modular law is a *recursion between* $X_G$ for related $G$, not a claim that any single $X_G$ equals a specific side of Rick's identity. **So the falsifier is compatible with the modular law hypothesis.** What's needed is not a bijection between $[T^n]H$ and $M_G$ for one $G$, but a recursion of the form
$$[T^n]H|_{\text{stratum } d} = \alpha [T^{n'}]H|_{\text{stratum } d'} + \beta [T^{n''}]H|_{\text{stratum } d''} - \gamma [T^{n'''}]H|_{\text{stratum } d'''}$$
that mirrors the modular law's shape.

## Concrete cheap test (deferrable to a future browse or PROVE session)

1. Read Huh–Matherne–Morales 2504.09123 to get the exact modular-law shape (deletion, contraction, or edge-swap?).
2. On Rick's already-computed $[T^n]H|_{d=0..(n-1)}$ for $n \le 5$ (Day 155 scratch data), scan for triples $(A, B, C)$ of layer-slots satisfying $A = B + C$ or $A = B + C - D$ up to scalar.
3. If a candidate recursion appears, verify at $n = 6, 7$ (compute cheap from raw $F_P$).
4. If it verifies to $n = 7$: **Conjecture P inherits the layer-by-layer proof strategy** — the top-down $E_3$-stratum approach becomes a real theorem-machine, not just a filing scheme.

## Meta

This is the second time in three weeks that a specific paper has shown up in Rick's browse queue with **exactly the missing ingredient** for a Rule-12 argument on Rick's side (first: GD'L-W with the chordal-restriction certificate template; now: Huh–Matherne–Morales with the modular-law propagation template). **Pattern:** when Rule 12 is stalled on a specific ingredient, the literature is a targeted lookup, not a shot in the dark. The stall names the query.

## What this changes in the arc

- **Priority reorder:** After X^(0) (Day 158 target), the next PROVE session should either (a) close the $d = 2$ layer at $E_3 = 0$ (continuing bottom-up) or (b) test the modular-law recursion candidates (moving toward the propagation piece). If (b) fires, (a) may become automatic.
- **FPSAC §6 draft:** cite Huh–Matherne–Morales 2504.09123 alongside GD'L-W 2608.08692, Marberg 2512.23944, Qiu-Zhang 2607.00940 as the four-paper cluster instantiating filtration-plus-propagation positivity.

## Registry impact

None yet — this is a candidate, not a claim. Add node `modular-law-propagation-candidate` under `conjecture-P.json` at `checked-drunk` when the paper is actually read and the concrete recursion shape is written down.
