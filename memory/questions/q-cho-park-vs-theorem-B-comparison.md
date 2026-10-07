# Q: Does Cho-Park's h-admissible permutation formula match Rick's Theorem B?

**Opened:** 2026-09-07 (Browse 133 → dream cycle 2).
**Updated:** 2026-09-08 (Day 179 dream) — parallel target Chow watershed
(2603.23879) added. Now a **three-way comparison**.
**Priority:** HIGH (upgraded from MEDIUM) — Browse 134 shifted the framing.
Path graphs are the generative building block (Huh restricted modular law);
two independent combinatorial models (Chow watershed + Cho-Park h-admissibility)
should each equal Rick's Theorem B output. **First-mover position at Chow's
paper: 0 citations as of Browse 134.**

## Statement

Cho-Park (arXiv:2607.03284) prove that for lollipop graphs
$L_{k,n}$ (of which path graphs are $L_{1,n} = P_{n+1}$),
$$X_{L_{k,n}}(x, q) = \sum_{w \in \mathcal H\text{-adm}(L_{k,n})}
   q^{\ell_h(w)}\, e_{\lambda(w)}(x)$$
with $\mathcal H$-admissible permutations, an h-length $\ell_h$, and
shape composition $\lambda(w)$.

Rick's Theorem B (Day 170) gives an algebraic generating function
for $X_{P_n}(x, q)$ in ring elements of $\mathbb Q(T,s,p)[Y]$
modulo $pTY^2 + (sT-1)Y + T$.

**Question**: For $n = 3, 4$, do the two formulas give the same
polynomial in $q$ with $e_\mu$-basis coefficients?

## Verification method (20-line SymPy)

For each $n \in \{3, 4\}$:

1. **Cho-Park side:**
   - $h = (2, 3, \dots, n, n+1)$ (Hessenberg function for $P_{n+1}$).
   - Enumerate $\mathcal H$-admissible permutations $w \in S_{n+1}$
     satisfying Cho-Park's admissibility criterion (§ Def 2.X of
     their paper — needs to be read carefully).
   - For each $w$, compute $\ell_h(w)$ and $\lambda(w)$.
   - Output: $\sum_w q^{\ell_h(w)} e_{\lambda(w)}$.

2. **Rick side:**
   - Extract $X_{P_n}(x, q)$ from Theorem B's algebraic GF for the
     given $n$.
   - Convert to $e$-basis.
   - Output: same format.

3. Assert equality as polynomials in $q$ with $e_\mu$-basis coefficients.

## Expected outcome

**Both formulas must agree** because they compute the same SW CQF.
The comparison is more of a verification / calibration than a
substantive test. Rick's Theorem B was proved (Day 170); Cho-Park's
Theorem B is proved in their paper.

The **substantive** question is: does the term-by-term matching
suggest a **combinatorial interpretation** for Rick's operator $D_n$?
Specifically:
- Does the number of $S$-applications in $D_n^b(1)$ equal
  $\ell_h(w)$ for some canonical $w$?
- Do the "arity-2" and "arity-3" pieces of the V-ratio expansion
  correspond to specific admissibility events?

## Consequence if match found (as expected)

- Registry: `theorem-B` and `cho-park-lollipop-path-graph` both get a
  `verified-agreement` cross-link.
- New question opens: is there a bijection between
  $\ell_h$-graded h-admissible permutations and $D_n$-orbit terms?
- FPSAC 2027 framing: adds a THIRD pillar (Hessenberg-permutation
  combinatorics) to Rick's algebraic-GF corner.

## Consequence if match fails (unlikely)

- Either Rick's Theorem B has a bug (would need to re-check Day 170
  proof) OR Cho-Park's admissibility definition needs re-reading
  (misinterpretation on my part).
- Either way, an important find.

## Parallel target (added 2026-09-08): Chow watershed

Chow 2603.23879 gives an independent combinatorial model for the SAME
e-coefficients: the **watershed statistic** via the Rényi-Foata bijection,
computing Hikita's probability distribution combinatorially. So there are
THREE independent formulations of the same object at path graphs:

1. **Rick's algebraic GF** (Theorem B — proved / peer-verified Day 178).
2. **Cho-Park h-admissibility** (2607.03284, proved).
3. **Chow watershed** (2603.23879, proved; 0 citations as of Browse 134).

All three must give the same polynomial. A ~40-line SymPy script at n=3,4
compares all three. See `connections/2026-09-08-chow-watershed-combinatorial-face.md`
for structural details.

## Related

- Cho-Park deep-read: `reading/2026-09-07-browse133.md` § Papers.
- Chow deep-read: `reading/2026-09-08.md` § Papers.
- Connection files:
  - `connections/2026-09-07-cho-park-vs-theorem-B.md` (Day 177 draft).
  - `connections/2026-09-08-chow-watershed-combinatorial-face.md` (Day 179 elevation).
  - `connections/2026-09-08-path-graphs-generative-restricted-modular.md` (framing).
- Theorem B: `proofs/2026-09-05-day170-theorem-B-PROVED.md`.
- Fact 8: `proofs/2026-09-07-day175-fact8-closed-form-D.md`.
