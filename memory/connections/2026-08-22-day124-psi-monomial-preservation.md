---
name: Day 124 — Ψ preserves (1,1,2)-weight monomial-by-monomial
description: Reduces Lemma 2 (Filtration Preservation for Ψ, the last gap in Rick's Main Conjecture) from "on linear combinations" to "on individual e-monomials." Verified 147/147 monomials to u-degree 14, zero violations. Explicit closed form for top(Ψ(e_1^a e_2 e_3^c)) — the (2c+1)-shift is the queer content signature.
type: project
---

# Day 124 — Ψ monomial-level (1,1,2)-weight preservation

## The claim (empirical, 147/147)

Let $\Psi: \mathbb{Q}[e_1, e_2, e_3] \to \mathbb{Q}[e_1, e_2, e_3]$ be the linear map defined by $\Psi(s_\mu) = s^*_\mu$ (both Schurs and shifted Schurs expressed in the $e$-basis in 3 variables). For each $e$-monomial $m = e_1^{a_1} e_2^{a_2} e_3^{a_3}$, define its $(1,1,2)$-weight $w(m) = a_1 + a_2 + 2 a_3$.

**Claim:** for every $e$-monomial $m$, every monomial of $\Psi(m)$ has $(1,1,2)$-weight $\le w(m)$, with equality on the top symbol.

**Evidence:** 147 monomials of $u$-degree $\le 14$ checked; **zero violations, zero looseness on top**. Also $\Psi^{-1}$ preserves the filtration (checked $N \le 10$).

**Consequence.** Lemma 2 (Filtration Preservation for the operator $\Pi^* = \Psi \circ (e_2 \cdot) \circ \Psi^{-1}$) is a one-liner:
$$w(\Pi^*(f)) = w(\Psi(e_2 \cdot \Psi^{-1}(f))) \le w(e_2 \cdot \Psi^{-1}(f)) = w(\Psi^{-1}(f)) + 1 \le w(f) + 1.$$

This immediately implies the Main Conjecture (E-basis, Day 123), which implies the Layer-Shape Lemma at all $d$, which is the last remaining piece of Rick's β' programme.

## Structural facts

1. $w(s_\mu) = w(s^*_\mu) = d_\mu = \mu_1 + \lfloor (\mu_2 + \mu_3)/2 \rfloor$ for all tested $\mu$, $|\mu| \le 8$.
2. $\deg_t \Sigma(s_\mu) = \deg_t \Sigma(s^*_\mu) = d_\mu$ (where $\Sigma$ is the Day 123 specialization).
3. $\Psi$ is EXACTLY the identity on pure $e_1^a$, pure $e_3^c$, and mixed $e_1^a e_3^c$ monomials — top-weight action.
4. Multiplicativity in $e_1$: $\text{top}(\Psi(e_1^a \cdot m)) = e_1^a \cdot \text{top}(\Psi(m))$.
5. **Explicit closed form:** $\text{top}(\Psi(e_1^a e_2 e_3^c)) = e_1^a e_2 e_3^c - (2c+1)\, e_1^{a+1} e_3^c$.
6. $\text{top}(s_\mu) = \text{top}(s^*_\mu)$ for MOST $\mu$; exceptions have a specific pattern (to be characterized).

## The queer content signature

The $(2c+1)$-shift in fact 5 doubles the $\mathfrak{q}_N$ content shift $(0, -2, -3, -4, \ldots)$ observed via the parallel Day 124 T-shift analysis. This is the strongest signal to date that $\Psi$ IS (up to normalization) the Harish-Chandra map for the queer superalgebra $U(\mathfrak{q}_N)$, connecting via Kashuba-Molev 2512.21631 + Das-Pattanayak 2608.17431.

## Remaining gap

**Rigorous algebraic proof of the monomial claim.** Candidate route:

- Weyl determinant form: $s^*_\mu = \det[[u_i]_{k_j}] / V(u)$ with $k = (\mu_1 + 2, \mu_2 + 1, \mu_3)$.
- Expand each $[u_i]_{k_j}$ via Stirling numbers of the first kind: $[u_i]_k = \sum_{r} s(k, r)\, u_i^r$.
- Reduce the resulting polynomial to $e$-basis via Newton-Girard.
- Show that the $(1,1,2)$-weight of the reduced form is $\le d_\mu$.

This is a self-contained combinatorial identity — Cauchy-Binet meets Stirling. Should be tractable.

## Files

- `proofs/2026-08-22-day124-lemma2-attempt.md` — full writeup (Day 124 A).
- `beta-prime/code/day124/psi_filtration_test.py` — KEY 147-monomial check.
- `beta-prime/code/day124/psi_top_symbol.py`, `top_symbol_formula.py` — closed-form derivation.
- `beta-prime/code/day124/pi_star_data.py`, `pi_star_on_monomials.py` — Π* action data.
- `beta-prime/code/day124/verify_monomial_filtration.py` — filtration verification.
- Assumptions analysis: `.claude/scratch/assumptions-20260822-day124.md`.

## Cross-references

- Day 123 (E-basis reformulation) — the setting.
- Day 124 T-shift theorem (`connections/2026-08-22-day124-t-shift-theorem.md`) — parallel discovery.
- Lee 2606 bridge (`connections/2026-08-21-lee-2606-plethystic-bridge.md`) — external identification.
- Path 1+2 chain — queer $\mathfrak{q}_N$ (Kashuba-Molev + Das-Pattanayak).
