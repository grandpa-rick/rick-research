# Master Vanishing Lemma — a re-usable proof template for rational sums indexed by pairs with Δ-factors

**Source:** Day 180 PROVE (2026-09-08), `proofs/2026-09-08-day180-lemma-2A-proved.md`.

## The template

**Setup.** Let $S$ be a finite index set, $|S| = N \ge 3$, and $\Delta_{ij}(l)$ a rational function of $(u_i, u_j, u_l)$ with simple poles only on hyperplanes $\{u_a = u_b\}$. Consider

$$\Pi_P^{(S)}(u_S) = \sum_{\{i,j\} \subseteq S} \operatorname{prefactor}(u_i, u_j) \cdot P(u_i, u_j) \cdot \prod_{l \in S \setminus \{i,j\}} \Delta_{ij}(l)$$

where $P$ is symmetric of total degree $d$.

**Claim.** $\Pi_P^{(S)}$ is a polynomial in $u_S$ of degree $\le d - (N - 3)$.

**Proof template (2 steps).**

**Step 1 (residue cancellation → polynomial).** Poles can only occur on hyperplanes $\{u_a = u_b\}$. Fix $a \ne b$ and compute the residue. The factor $(u_a - u_b)^{-1}$ enters exactly two families:
- From pair $\{a, l\}$: $\Delta_{a,l}(b)$ carries $(u_a - u_b)^{-1}$.
- From pair $\{b, l\}$: $\Delta_{b,l}(a)$ carries $(u_b - u_a)^{-1}$.

The residues at these two families **pair up by $l$** (for each $l \in S \setminus \{a, b\}$) and **cancel because their residue values are equal in magnitude and opposite in sign**, with all other factors evaluating to the same expression under $u_a \to u_b$. Sum over $l$: total residue $= 0$. No higher-order poles.

**Step 2 (uniform scaling → degree bound).** Under $u \to tu$, each $\Delta_{ij}(l)$ scales as $t^{-1}$ (leading order). Prefactor $(u_i + u_j + 1)$ scales as $t$. $P(u_i, u_j)$ scales as $t^d$. Total scaling of each summand: $t \cdot t^d \cdot t^{-(N-2)} = t^{d - N + 3}$. Since $\Pi_P^{(S)}$ is polynomial (Step 1), its degree equals the leading scaling weight $\le d - (N - 3)$.

∎

## Why this is a template

Both steps are **generic**:
- Residue cancellation uses only that $\Delta$ has simple poles on hyperplanes and adjacent pair families produce equal-magnitude opposite-sign residues.
- Scaling uses only the rational-function weight of each factor.

Neither uses:
- The specific form of $\Delta_{ij}(l) = \frac{1}{u_i-u_l} + \frac{1}{u_j-u_l} + \frac{1}{(u_i-u_l)(u_j-u_l)}$.
- The specific prefactor $(u_i + u_j + 1)$.
- The polynomial identity of $P$.

**Any sum of shape $\sum_{\text{pairs}} \operatorname{prefactor} \cdot P \cdot \prod \Delta$ with pole cancellation between adjacent pairs admits the same 2-line polynomial + degree bound.**

## What this beats

- **Route α (prescribed):** direct symmetric-function identity for $\prod\Delta$, expanded via power-sum basis. Loses because the individual $\Delta$-factors do NOT simplify — cancellation is *between summands*, not *within* summands.
- **Route β (prescribed):** Sub-lemma B on $S_r$, top-piece expansion. Loses because top-piece expansion is combinatorially messy and only proves ρ-bound, not polynomial-ness.

MVL wins by choosing the right *global* invariants (poles + scaling), rather than local (top-piece expansion).

## Application domains

**Immediate:** Fact 8 arc (Rick's Day 180 PROVE).

**Latent — worth checking whether the template applies:**
1. **Any V-ratio arity expansion** (Day 176 V-ratio machinery). The V-ratio decomposes into arity-graded pieces, each of which is a sum over pairs with $\Delta$-factors. If the outer sum has adjacent-pair pole structure, MVL applies directly.
2. **Bethe ansatz / off-shell scalar products.** Slavnov's determinant formula, Korepin norm formula — often expressed as sums indexed by pairs of Bethe roots with $\Delta$-factors. Would need to check if pole cancellation between adjacent pairs holds.
3. **Nekrasov instanton partition functions.** Contour integrals over Coulomb-branch parameters $\{a_i\}$; the residue sum is over pairs $\{a_i, a_j\}$ with $\Delta$-factors. Uniform scaling + residue cancellation is exactly the standard proof of holomorphicity/polynomial-ness.
4. **Macdonald polynomial norm identities.** Cherednik's proof of the norm conjecture uses residue cancellation between adjacent difference operators.

## Seed connections

- **Path 3 (Hecke):** Bethe ansatz sums live in affine-type-A representations of quantum groups; polynomial-ness of scalar products via MVL-style residue cancellation is a well-known trick in that literature (Slavnov, Korepin). This makes MVL familiar in Path 3.
- **Path 4 (crystal/combinatorial):** ρ-drop bounds (which MVL delivers) are exactly the degree-bounds needed for crystal-basis polynomiality arguments. Any time a crystal-graph sum reduces to a rational sum indexed by pairs, MVL applies.

## Slogan

**When a sum over pairs has adjacent-pair pole structure and uniform scaling, polynomial-ness costs 2 lines: residue cancellation + uniform scaling. Don't expand top pieces.**

## Files

- Proof: `proofs/2026-09-08-day180-lemma-2A-proved.md`.
- Feedback memory: `feedback_MVL_residue_plus_scaling.md`.
- Numerical verification: `scratch/day180/verify_mvl.py` (16/16 at |S| = 3, 4, 5; degree bound tight).
