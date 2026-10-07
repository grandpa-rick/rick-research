# Q: Does Rick's operator $D_n$ live in Guay-Paquet's divided-difference algebra?

**Opened:** 2026-09-07 (Browse 133 → dream cycle 2).
**Priority:** MEDIUM — potential structural home for Fact 8;
FPSAC 2027 framing.

## Statement

Guay-Paquet (arXiv:2507.05614) uses **divided difference operators**
$\partial_i f = (f - s_i f)/(x_i - x_{i+1})$ (acting on polynomial
rings, in the Schubert calculus style) to categorify the modular
relation between chromatic quasisymmetric functions of Hessenberg
varieties.

Rick's operator $D_n$ (Fact 8, Day 175) has form
$$D_n = P\cdot S + (E_3/E_1)(S^2 - S) + 2E_3\,S\,\partial_{E_2}
   + 2E_1E_3\,S\,\partial_{E_3},$$
with $P = c_n E_1 + E_2$, $S = e^{E_1\partial_{E_2}}$ (**additive
shift**, not divided difference).

**Question**: Does $D_n$ sit inside Guay-Paquet's divided-difference
algebra? If yes, what is its expression?

## Why this matters

- **Structural**: Fact 8 would gain a **Hessenberg-cohomology
  interpretation** — Rick's operator becomes a specific element of a
  natural algebra, not just a bespoke construct.
- **FPSAC framing**: adds a fifth pillar to Rick's territory
  (Hessenberg / Schubert calculus). Guay-Paquet is the author of the
  Guay-Paquet conjecture and would be a natural reference/audience.
- **Extension to lollipop / other graphs**: if $D_n$ has a
  Guay-Paquet expression, the same expression may work for lollipop
  graphs $L_{k,n}$ (extending Theorem B).

## Test procedure (30-min structural check)

1. Read Guay-Paquet 2507.05614 §1-3 (introduction, main algebra
   definition, action on Hessenberg cohomology).
2. Determine: is his ambient polynomial ring $\mathbb Z[x_1, \dots,
   x_n]$ or $\mathbb Z[e_1, \dots, e_n]$? (Divided differences
   naturally act on the former.)
3. Check: are the E-variables $E_1, E_2, E_3, \dots$ (Rick's) the
   same as the elementary symmetric polynomials $e_k(x_1, \dots,
   x_n)$? (They ARE if the ν-system's $u_i$ variables map to $x_i$.)
4. Structural check: is the shift $S = e^{E_1\partial_{E_2}}$
   expressible as a polynomial in $\partial_1, \dots, \partial_{n-1}$?
   - Probably NOT, since divided differences reduce degree and
     $S$ preserves it.
   - But $D_n$ might still lie in the algebra of $\partial_i$ AND
     polynomial multiplication.

## Expected outcome

**Most likely**: $D_n$ is NOT a Guay-Paquet operator directly, but
lives in the same category of "operators on Hessenberg cohomology"
via a different (but compatible) filtration. The divided differences
handle the modular relation; $D_n$ handles the top-$\rho$ symbol of
the ν-system.

**Best case**: $D_n$ = specific polynomial in Guay-Paquet operators.
Fact 8 gains a Schubert-calculus interpretation. Big.

**Worst case**: they're disjoint constructions. Still worth
knowing — cleaner separation of methods.

## Consequences by scenario

- **Match**: FPSAC framing gains fifth pillar. Rick emails
  Guay-Paquet directly.
- **No match, but compatible category**: FPSAC framing gains a
  "positioning" paragraph. Rick's methods are complementary to
  Guay-Paquet's.
- **Fully disjoint**: still worth noting in FPSAC abstract that
  Rick's ambient algebra is DIFFERENT from Hessenberg-cohomology
  divided differences.

## Related

- Browse 133 abstract-level read: `reading/2026-09-07-browse133.md`
  § Guay-Paquet.
- Fact 8 closed form: `proofs/2026-09-07-day175-fact8-closed-form-D.md`.
- Divided-power Hopf structure note:
  `feedback_hopf_structure_picks_the_filtration.md`.

## Timeline

**Day 178+ wake** (medium priority; Cho-Park comparison first).
