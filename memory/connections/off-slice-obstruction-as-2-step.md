---
name: Off-slice coideal obstruction as a 2-step complex
description: Conjectural structural parallel — the off-slice [e_i^k, B_i]π = e_i^(k-1)π obstruction is a derived correction term, mirroring Cor 2.4's 2-step complex shape for non-spin B_n bigraded acyclicity failure.
type: project
---

# Off-slice coideal obstruction as a 2-step complex (conjectural)

**Status:** Structural analogy, no proof of equivalence. Two phenomena share a shape; the hypothesis is they share a common categorical home.

## The two phenomena

### A. Off-slice coideal obstruction (proved 2026-05-14 at B_2)

On $\mathrm{Kp}(\infty)$ at $B_2$:
$$[e_i^{k(i)}, B_i]\,\pi = \begin{cases} 0 & \varepsilon_i(\pi) \geq k(i) \\ e_i^{k(i)-1}\pi & \varepsilon_i(\pi) = k(i) - 1 \\ 0 & \varepsilon_i(\pi) < k(i) - 1 \end{cases}$$

At the slice boundary, strict commutativity fails by a single degree-1 correction term. The natural "module" picture (Aug~ as a coideal-module morphism) breaks at this boundary; what survives is a *2-term* correction.

### B. Cor 2.4 / Remark-4.7 obstruction (proved 2026-05-06)

For non-spin $B_n$ bigraded cases, $(q,t)$-Lusztig polynomial = $qt - q + t$ at a specific minuscule pair. By Cor 2.4 of the Remark-4.7 obstruction note: no positive crystal/statistic (single-graded acyclic invariant) factors this. The only structural completion is a **2-step bigraded complex**:
$$0 \to V_1 \to V_2 \to 0$$
with bigraded Euler characteristic equal to $qt - q + t$.

## The structural parallel

Both phenomena live at the boundary where:
- The "natural q=0 picture" (slice-bounded module / acyclic single-graded statistic) reaches its limit.
- One additional layer of homological data is needed for the structure to close up.

The doubly-laced asymmetry shows up in both cases as the source of the extra layer:
- (A) The unit factor $k(i) \in \{1, 2\}$ creates a boundary at $\varepsilon_i = k - 1$. Only happens for $k > 1$ — i.e., doubly-laced.
- (B) The non-spin minuscule case at $B_n$ only fails acyclicity for doubly-laced (CKL Thm 4.6 + Lemma 3.1 says spin/acyclic).

## The conjecture

**Conjecture.** The off-slice coideal obstruction (A) is the chain-level avatar of the Cor 2.4 obstruction (B). Equivalently: there is a 2-step *complex* of coideal modules whose Euler characteristic, on the doubly-laced minuscule pair, is the non-spin $(q,t)$-Lusztig polynomial $qt - q + t$; the differential of this complex *is* the boundary $e_i^{k-1}$ correction term.

If true: the "categorical home" of Aug~ off-slice is a *derived* coideal-module category — not honest modules but $D^b(B_i\text{-mod})$ or similar. The off-slice action of Aug~ is a chain-map between complexes, not a strict module morphism.

## Why this is plausible

1. **Both obstructions are doubly-laced-specific.** No corresponding phenomenon in simply-laced types.

2. **The boundary at $\varepsilon_i = k - 1$ matches Cor 2.4's "minuscule pair just below the spin case."** Both are "one step away from where the natural picture would close."

3. **Bowman–Norton–Simental arXiv:2107.01190 already builds BGG resolutions in cyclotomic Hecke.** The BGG-resolution machinery is exactly the homological structure that would make this conjecture concrete. BNS sections 4–5 are the natural place to look.

4. **The Aug~ → BGG-differential identification (2026-05-12 onwards) puts Aug~ at the chain level by construction.** Promoting "Aug~ commutes with $B_i$" to "Aug~ is a chain map of $B_i$-complexes" is the natural next step.

## Tests of the conjecture

- **At B_2, check whether the off-slice obstruction $e_i^{k-1}\pi$ is a coboundary in a natural 2-step complex.** If yes, the conjecture has a concrete instance.
- **Compute the bigraded Euler characteristic of the 2-step coideal complex (if it exists) on the non-spin minuscule pair.** Should equal $qt - q + t$.
- **Read BNS arXiv:2107.01190 sections 4–5.** Look for a literal correspondence: their BGG-resolution differential ↔ Rick's $e_i^{k-1}$ boundary.

## Why I'm filing this now (rather than waiting for proof)

The two phenomena were *not* visible as connected until today. Yesterday's CST bridge framing + today's prove session produced both endpoints in clean form. The connection itself is the gold; filing it now means tomorrow's reading has a target.

The conjecture may turn out to be wrong in detail (the 2-step complex may not be a coideal complex, or the differential may not be $e_i^{k-1}$ exactly). But the structural parallel is the kind of thing that, if it holds even partially, opens a research program. Worth a connection file even at low confidence.

## Cross-references

- (A) Off-slice obstruction: `connections/coideal-commutativity-on-slice-B2-PROVED.md`, `proofs/2026-05-14-coideal-commutativity-B2.md`.
- (B) Cor 2.4 obstruction: `proofs/2026-05-06-remark-47-obstruction.md`, `connections/acyclicity-is-positivity.md`.
- BNS bridge candidate: arXiv:2107.01190 (Bowman–Norton–Simental, JIMJ 2024).
- iQSP categorification background: Bao–Wang arXiv:1310.0103, Watanabe arXiv:2509.00853.
