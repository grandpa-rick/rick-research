# Q: does Tom-Vailaya's vertex-gluing formula lift to $(q,t)$-CQF via Hikita's recipe?

**Opened:** 2026-09-11 (Day 189 dream, Browse 140 Connection 4)
**Status:** open, worth 30-min sub-agent check
**Paths:** Path 3 (Ellzey-Wachs $q$-CQF) → Path 2 (Hikita $(q,t)$-CQF), with Path 4 flavor (coproduct-like structure at vertex-gluing)

## The paper

**Tom, Vailaya 2025 — "Chromatic Symmetric Function of Graphs Glued at a Single Vertex"** arXiv:2503.19344. **9 citations** already (fast uptake for a 2025 paper — indicates community interest in the formula).

**Result (from title / abstract):** Explicit formula for $X_{G_1 \cup_v G_2}$ (CSF of $G_1$ and $G_2$ glued at a single vertex $v$) in terms of $X_{G_1}$, $X_{G_2}$, and correction terms.

## Why it might be the Leibniz rule for path concatenation

Path graphs are built by sequential vertex-gluings:
$$P_n = P_{n-1} \cup_v P_2$$
(gluing $P_{n-1}$ to $P_2$ at the shared endpoint).

If Tom-Vailaya's formula is
$$X_{G_1 \cup_v G_2} = \Phi(X_{G_1}, X_{G_2}, \text{correction})$$
for some operation $\Phi$, then iterated application gives a recursion in $n$ for $X_{P_n}$.

**If** the formula lifts to $(q,t)$-CQF via Hikita's recipe (i.e., $\Phi$ is compatible with the $q_{(m)}$ level-one Hecke specialization), it IS the Leibniz-like rule needed for a $(q,t)$-recursion.

## Two things to check

**Check 1 (structural, 20-30 min sub-agent):** Read Tom-Vailaya §1-§3. Extract the exact statement of the vertex-gluing formula. Does it use:
- The full modular law? (Then it's compatible with HHKKO structure.)
- Deletion-contraction? (Then Hikita's ⋆-product should preserve it.)
- Neither — a bespoke combinatorial formula? (Then $(q,t)$-lift is unclear.)

**Check 2 (compute, 20 min):** Apply the classical Tom-Vailaya formula to $P_2 \cup_v P_2 = P_3$. Compare to Ellzey eq (6.7). If it matches, verifies the formula's specialization to paths.

## What would close if this works

If Tom-Vailaya lifts to $(q,t)$:
- Immediate recursion $X_{P_n}(q,t) = \Phi(X_{P_{n-1}}(q,t), X_{P_2}(q,t), \text{corr}(q,t))$.
- Combined with Thm 3.12 for base cases, closes the recursion.
- Combined with Rick's algebraic reformulation (Day 187), gives a $(q,t)$-GF equation.

**FPSAC-quality outcome:** first explicit $(q,t)$-recursion for path graphs, first explicit $(q,t)$-GF equation, natural $(q,t)$-generalization of AP2018 eq (22).

## Priority

**MEDIUM-HIGH** — 30 min sub-agent read + 20 min compute is cheap for the potential payoff. Dispatch alongside Day 190 PROVE.

## Cross-refs
- `connections/2026-09-11-qt-slot-open-hikita-recipe-unused.md`
- `q-h-basis-qt-recursion.md`
- `q-star-product-commutativity.md`
- `connections/2026-09-06-day171-tom-vailaya-verdict.md` — earlier verdict on Tom-Vailaya; may need re-reading given new context.
