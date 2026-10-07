---
name: Type D analog of Goertzen-Williamson KL cone optimization?
description: Goertzen-Williamson 2604.18894 characterizes KL basis for type A as the maximal (1+s)-invariant cone in Specht modules (proved for hooks, two-column, (n-2,2)). Type D is completely open. Rick has DIII polytope machinery + Svyatnyy regular cell tables. Uncrowded territory.
type: project
---

# OQ-TYPE-D-KL-OPTIMIZATION

## Setup

Goertzen-Williamson 2604.18894 (April 2026): the Kazhdan-Lusztig basis of the
type A Specht module $S^\lambda$ spans the **maximal $(1 + s)$-invariant cone**
inside $S^\lambda$, where $s$ ranges over simple reflections. Proved for
hook shapes, two-column shapes, and $(n-2, 2)$. Minimization inside the same
feasible region uniquely recovers Young's seminormal basis.

**Reformulation:** the KL basis is the solution to a continuous quadratic
optimization problem on the Specht module weight space. This is the
crystallization of the ML/KL trajectory (DeepMind 2021 → Lacabanne-Tubbenhauer-Vaz
2412.01283 → Goertzen-Williamson).

## The type D gap

**Zero mention of type B/C/D anywhere in Goertzen-Williamson.** The (1+s)-cone
framework is pure type A.

**What type D would need:**
1. **Type D_n Specht modules or their analogues.** Multiple candidates:
   - Direct type D Specht construction from the D_n cellular basis.
   - Regular cells from Svyatnyy 2504.14344 / 2605.00514 — these give the
     combinatorial substrate.
   - Domino tableaux + Garfinkle insertion (classical D_n RSK).
2. **Simple-reflection operators $(1 + s_\alpha)$ for the D_n Weyl group.**
   Well-understood.
3. **The cone extremization theorem — DOES it extend?** Type A proof uses
   Springer-basis triangularity (Haidar-Yacobi 2411.04432). Type D analog
   of Springer basis exists but is less canonical.

**Nobody has touched this.** DIII sentinels are 18 consecutive 0-citation
checks. Rick's DIII polytope machinery (Lean-closed) provides the geometric
backdrop; the KL cone question is a natural next layer.

## Connection to Rick's territory

- **Path 3 (Hecke algebra):** direct — this IS about H_q(D_n) canonical
  bases.
- **Path 4 (crystal branching):** the cone extremization at type A recovers
  KL bases which are simultaneously canonical bases in Kashiwara's sense.
  Type D analog would relate to Lusztig's type D canonical basis and its
  crystal at q = 0.
- **DIII polytope program (Rick's ongoing):** the Specht module analog for
  DIII should live inside the polytopes Rick already understands.

## Strategy scoping

**Path 1 — Extend Goertzen-Williamson result to type D directly.**
- Start with hooks in type D. Small n cases (n = 3, 4).
- If the cone structure survives: aim for a Rank Theorem for type D_n.
- 15-20 page paper doable.

**Path 2 — Use Svyatnyy cell tables as substrate.**
- Regular cells 2504.14344 give a combinatorial index set.
- Test whether KL cone extremization on these cells matches the type D KL basis.
- Could reveal WHICH type D combinatorics is the "right" Specht substitute.

**Path 3 — Consult Goertzen directly.**
- Postdoc at U Sydney with Williamson.
- Ask: has the type D case been considered? What are the obstructions?
- One email, low cost.

## Priority

**MEDIUM-LOW (long-horizon).** The H3 / β' sprint takes precedence through
FPSAC 2027 target. But this is a completely open direction with Rick's
existing tools directly applicable. Worth 30 minutes of scoping in a slow
week.

## Related

- OQ-2 (existing): "the KL cone framework applied to DIII / mu-involution
  Specht modules" — see `questions/q-KL-from-crystal.md`. This new OQ is a
  narrower, more concrete version.
- OQ-HAIDAR-YACOBI-D: does Haidar-Yacobi 2411.04432 (KL upper triangular
  over all GT bases) extend to type D? Prerequisite for the cone story
  extending.
- OQ-ZHANG-FPF-WGRAPH-DIII (Browse 96): Yifeng Zhang's affine matrix-ball
  for FPF W-graphs. If Zhang's molecule structure gives type D Specht
  analogues, that's the substrate.

## Files

- `reading/2026-08-14.md` — Goertzen-Williamson 2604.18894 deep read.
- `reading/2026-08-13-browse96.md` — Zhang 2608.03792 context.
