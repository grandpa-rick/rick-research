# OQ-PI3-INV5 — RESULT

**Day 65, 2026-06-12. Task B.**

## Question

Is the 26-piece n=3 minimal cover (`MIN_COVER_26` in
`code/2026-06-10-toric-quotient/analyze_torus.py`) naturally indexed
by involutions in $S_5$, given that $|I(5)| = 26$?

Two candidate statistics to match against:

- **Cycle-type** multiset $(1, 10, 15)$ — 1 identity, 10 single
  transpositions, 15 double transpositions.
- **RSK-shape** multiset $(1, 4, 5, 6, 5, 4, 1)$ — counted by
  $f^\lambda$ for $\lambda \vdash 5$.

## What we computed

For each of the 26 pieces, extracted the (m_2, m_236, m_23456)
column-vector: a triple of integer 7-tuples giving the projection
coefficients onto $(M_1, M_2, B_1, T_1, B_2, T_2, S)$ of each AII
generator into BDI.

### Marginal column-multisets

```
m_2:     4 distinct columns;  marginal count multiset = [1, 3, 11, 11]
m_236:   10 distinct columns; marginal count multiset =
                              [1, 1, 1, 1, 1, 2, 3, 3, 4, 9]
m_23456: 9 distinct columns;  marginal count multiset =
                              [1, 1, 1, 2, 4, 4, 4, 4, 5]
```

Compare to:
- $I(5)$ cycle-type multiset: $[1, 10, 15]$
- $I(5)$ RSK-shape multiset:  $[1, 1, 4, 4, 5, 5, 6]$

**Neither marginal matches either reference multiset.**

### Joint triples

The joint column triple $(c^{m_2}, c^{m_{236}}, c^{m_{23456}})$
**distinguishes all 26 pieces** — every piece has a distinct triple.
So the map "piece $\mapsto$ joint column triple" is an injection
$\text{MIN\_COVER\_26} \hookrightarrow \mathbb{Z}^{7 \times 3}$.

### Marginal-column counts

The marginal column counts are $(4, 10, 9)$.

- The $4 = $ # m_2-columns matches the $n = 3$ "AXIS" count for the
  m_2 direction (Day-62).
- The $10 = $ # m_236-columns nominally matches the # of single
  transpositions in $S_5$, but with the wrong distribution — so the
  match is the count alone, not a structural correspondence.
- The $9$ = # m_23456-columns has no obvious involution interpretation.

## Verdict — NO clean bijection

**No structural bijection** between $\text{MIN\_COVER\_26}$ and $I(5)$
visible at the level of:
- column-multiset marginals on any single axis
- the cycle-type / RSK-shape grading of $I(5)$.

The 26-piece count = $|I(5)|$ is **coincidental** as far as this check
can determine; it is not refined by any natural decomposition that
matches an involution invariant.

## What this rules out / what it doesn't

**Ruled out:**
- A "piece $\leftrightarrow$ involution" map that respects a single
  column-axis grading.
- An RSK or cycle-type indexing where each piece's "type" is read off
  its (m_2 column) or (m_236 column) or (m_23456 column) alone.

**Not ruled out (and would require a different check):**
- A non-canonical bijection $\text{MIN\_COVER\_26} \to I(5)$ exists
  by cardinality alone — but without structural content this is
  vacuous.
- A bijection respecting joint triples could be constructed (the
  injection above shows piece triples are all distinct), but no
  natural map from the joint triple to a specific involution
  presents itself.
- The 26 = $|I(5)|$ coincidence could reflect a deeper Hopf-algebra
  / symmetric-function origin that doesn't go through RSK directly.
  E.g. $I(5)$ also indexes:
  - the dimension of $\mathbb{C}[S_5]^{S_5\text{-conj}}$ on involutions
    (not really)
  - the basis of $\mathrm{Sym}_{\le 5}$ Schur ... no, that's $p(5) = 7$
  - the Mehta integral count... etc.

The clean answer is that the coincidence appears to be just a
coincidence at this level of resolution. **Conclusion: no clean
bijection. Possibly partial match if we relax to the joint-triple
data, but no canonical map.**

## Bonus: I(6) = 76

For reference, the involution numbers via $I(n) = I(n-1) + (n-1) I(n-2)$:

$$I(0..7) = 1, 1, 2, 4, 10, 26, 76, 232.$$

So $I(6) = 76$ and $I(7) = 232$. Whether the $n=4$ or $n=5$ piece
registries (currently 20-piece at $n=4$, not yet built at $n=5$)
ever hit 76 or 232 remains open — but per Day-64's prefix[1]-collapse,
the n=4 registry settled at 20 (≠ 76), so the I(n+2) pattern fails
already at $n = 4$.

This **kills the I(n+2) hypothesis** for the registry growth pattern.

## Files

- `check.py` — computation
- `triples.json` — JSON of piece column triples + marginals + verdict
- `check_output.txt` — full text output of check.py
