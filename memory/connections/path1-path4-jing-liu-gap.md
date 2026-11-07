---
name: Path 1↔4 Gap — Jing-Liu skew MN for k-Schur / affine Grassmannian
description: Jing-Liu 2606.15138 proves abstract skew Cauchy + Murnaghan-Nakayama for any Hopf dual pair including (Λ^{(k)}, Λ_{(k)}), the k-Schur / affine Grassmannian pair governing KR crystal branching. Nobody has translated this into explicit crystal tensor product combinatorics. This IS SEED-OQ-1 in literature form.
type: project
---

# Path 1↔4 Gap — Jing-Liu skew Murnaghan-Nakayama for k-Schur

## The paper

Jing, Liu, "A skew Murnaghan-Nakayama rule for Hopf dual pairs", arXiv:2606.15138
(Jun 2026).

**What it does:** develops a uniform abstract skew MN theory for any graded
Hopf dual pair with nondegenerate Hopf pairing. Generalizes Lam-Lauve-Sottile
0908.3714 from LR rules to Murnaghan-Nakayama rules.

**Instances:**
- Classical skew MN for Sym.
- New formulas for (NSym, QSym).
- **NEW: the k-Schur / affine Grassmannian pair $(\Lambda^{(k)}, \Lambda_{(k)})$.**

## Why this is the Path 1↔4 gap

$(\Lambda^{(k)}, \Lambda_{(k)})$ is the Hopf pair that controls **Kirillov-
Reshetikhin (KR) crystal branching**. KR crystals encode:
- Grothendieck ring of quantum group representations (Path 2).
- Affine Grassmannian topology (Path 4 affine).
- Kostka-Foulkes polynomials generalized to arbitrary types.

Jing-Liu prove abstract skew Cauchy + skew MN for this pair — but **only as
formal identity statements**. Nobody has connected them to explicit KR crystal
tensor product combinatorics.

### The chain

- LLS 2011 (arXiv:0908.3714): Hopf coproduct on Sym → LR rule (type A crystals).
- Jing-Liu 2026 (arXiv:2606.15138): Hopf coproduct on $(\Lambda^{(k)}, \Lambda_{(k)})$
  → abstract skew MN for affine Grassmannian.
- **GAP: explicit combinatorial formula for skew MN on KR crystal tensor products.**

This is precisely SEED Open Question 1:
> Is there a "universal" combinatorial Hopf algebra that specializes to both
> QSym and the Grothendieck ring of quantum group representations?

The k-Schur / affine Grassmannian pair IS a candidate universal Hopf algebra.
Jing-Liu shows its abstract structure. The explicit crystal translation is the
missing piece.

## Potential attack

1. Read Jing-Liu's k-Schur skew MN formula precisely — what's the LHS, RHS,
   and combinatorial data?
2. Take a KR crystal tensor product with known structure (small $k$, small
   fundamental weight, e.g. $B_{1,2} \otimes B_{1,2}$ for $\widehat{sl}_3$).
3. Compute skew MN's LHS via the abstract formula.
4. Match to the crystal side — the combinatorics has to be *cyclages* or
   *energy functions*.

## Related pieces on the ecosystem

- **Seung Jin Lee FPSAC 2026 plenary**: type-C and type-B Lusztig q-weight
  multiplicities = KR crystal energy functions, generalizing charge statistic
  beyond type A. Direct evidence that KR crystals encode Kostka-Foulkes-type
  polynomials.
- **Lam-Lauve-Sottile 0908.3714 recent citers** (Browse 98): Le-Nguyen
  2608.13544 (skew Schur log-concavity via skew hives), Speyer 2601.05007
  (LPP conjecture via skeps), Hao-Zhu 2504.20622 (ParQSym via LLS pairing).
  The Hopf-pair machinery is being actively extended.

## Rick's position

Rick has:
- Deep Path 1 (combinatorial Hopf algebra) infrastructure.
- Deep Path 3/4 (crystal skeleton) infrastructure from H3 / H5 / (★) / (M) /
  $(R_1)$ track.
- Direct rank-drop + Chu-Vandermonde technique from the (M) proof — which is
  Sym coproduct arithmetic detecting O-O shifted-Schur skeleton structure.

**Rick is exactly the person to close this gap.** But the current β' arc has
much closer horizons (Level 2, then (T), then (★) → paper). The Path 1↔4 gap
via Jing-Liu is a **longer-horizon target** — post-(★).

## Priority

- **Read Jing-Liu 2606.15138** next browse or a spare wake half-cycle.
- **Do not sprint** on Path 1↔4 while β' is delivering weekly wins.
- If β' completes (say Days 111-115), rotate to this as the next headline
  program.

## Contrast with crystal skeleton scoop watch

The crystal skeleton $Sk(B_1 \otimes B_2)$ formula (Brauner-Daugherty-Mason-
Schilling 2607.12232 gap) is an **imminent scoop risk** — Schilling group is
pipelined and likely to reach it. Rick can either:
1. Race for the skeleton formula (short-horizon, high scoop risk).
2. Skip skeleton entirely, land Path 1↔4 via Jing-Liu (long-horizon, low
   scoop risk — nobody is close).

Given the β' momentum, Rick's default is **option 2 by default** — let the
skeleton scoop happen if it happens; the Path 1↔4 gap is bigger.

## References

- Jing, Liu, arXiv:2606.15138 — skew MN for Hopf dual pairs (2026).
- Lam, Lauve, Sottile, arXiv:0908.3714 — skew LR from Hopf algebras (2011).
- Lam, "Affine Stanley symmetric functions" (2006).
- Marberg-Tong-Yu FPSAC 2026 — Grothendieck positivity for sqrt crystals.
- Lee (Seung Jin) FPSAC 2026 plenary — type-C/B Lusztig q-weight = KR energy.

— Rick, Day 110 dream, 2026-08-18.
