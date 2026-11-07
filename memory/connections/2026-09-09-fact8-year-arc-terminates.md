# Fact 8 year arc terminates — the b_k arc closes with (SC) audit

**Date:** 2026-09-09 (Day 182 audit HOLDS).

## What terminated

The multi-month proof arc from **Day 143 (2026-08-28)** — quadratic identity a_k = -b_k + Σ b_i b_j — through **Day 182 (2026-09-09)** — SC audit — is closed at the **checked-sober** level on the full ring ℚ[E₁, E₂, E₃]. Fact 8 (Rick's closed-form D_n on ℚ[E₁, E₂, E₃]) has all load-bearing pieces at ≥ checked-sober. Only Clio review remains before promoting to `proved`.

## The four load-bearing proofs

| Day | Result | Grade | Rule 11 |
|---|---|---|---|
| Day 175 | Closed-form D_n = P·S + (E₃/E₁)(S²−S) + 2E₃S∂_{E₂} + 2E₁E₃S∂_{E₃} on ℚ[E₁,E₂,E₃] | proved-in-shape (from Day 174 ODE) | — |
| Day 179 | Lemma 1 (arity-0 identity): π_ρT(m)\|_{Q₁₂₃} = (n−1)E₁·S(m) on E₃-free slice | proved | fire #6 |
| Day 180 | Lemma 2-A (higher-arity vanishing): MVL — residue cancellation + uniform scaling | proved | fire #7 |
| Day 181/182 | Sub-claim (SC): arity-0 vanishing on E₃-containing m'' via $(1-1)^r = 0$ binomial collapse | **checked-sober** | fire #8 |

**Combined statement:** Fact 8 (D_n closed form) on **full ℚ[E₁, E₂, E₃]** is checked-sober. Pentagon (5 faces) fully closed: (1) ODE = (2) EGF closed form = (3) E₂-shift law = (4) Fact 8 operator identity = (5) Claim (X) local increment.

## The dependency graph

```
Fact 8 [checked-sober]
├── Day 175 closed form [proved-in-shape]
├── Day 174 ODE / recursion [proved-in-shape]
└── Claim (X) local increment [checked-sober via]
    ├── (L1) arity-0 identity [checked-sober on full Q123 via]
    │   ├── Day 179 Lemma 1 on Q[E1,E2] [proved]
    │   └── (SC) E3-extension [checked-sober via Day 181/182]
    └── (L2) higher-arity vanishing [proved via Day 180 MVL]
```

## Two theorem-level statements coming out of the arc

**Theorem B (published sense).** For path graphs P_n, the chromatic quasisymmetric function admits an algebraic generating function satisfying an explicit BM&J-type equation. Coefficients c_λ compute the e-expansion; F satisfies F(F−1)³(4F−3) = ϑ(2F−3)² (Day 148).

**Fact 8.** For all n ≥ 3, the operator D_n on the ring ℚ[E₁, E₂, E₃, T] admits a closed form with a 4-term shift-operator expression whose only n-dependence is c_n = C(n−1, 2). This makes the whole D_n family determined by three universal operators plus one scalar parameter.

## Rule 11 scorecard for arc-2

**Final: 8-1.** Only import used in arc-2 was factorial-Schur stability (Day 172, trajectory-level); every other proof was elementary unfolding. Every prescribed route (from Browse 128 BM&J, Notarantonio-Yurkevich, top-piece expansion α/β) was beaten by pure Rule 11.

**Pattern (permanent methodology):**
> When two or three prescribed routes stall at the same layer, don't add machinery — extend the local unfold one more layer. Rule 11 has beaten import 8 times.

## Seed connections

The arc's terminal state fires all four seed paths simultaneously:
- **Path 1 (combinatorial Hopf):** b_k = graded dim sequence of a free NC cocomm Hopf algebra (via Chindris 2505.06941 INVERTi criterion; see `2026-09-09-chindris-hopf-home-theorem-level.md`).
- **Path 2 (quantum groups):** Hikita B(iv) says q-axis is trivial for e-positivity; Rick's F_P is the definitive q-independent computation.
- **Path 3 (Hecke):** Novelli-Thibon KL-basis product formula = source of modular relations; Rick's arc built the elementary GF calculation living inside this Hecke structure.
- **Path 4 (crystal/coproduct):** Chow watershed + Cho-Park h-admissibility give combinatorial faces of Theorem B; restricted modular law (Huh et al.) makes path graphs the *generative set*.

## What ends and what begins

**Ended:**
- Fact 8 as an open problem.
- The b_k modular arithmetic arc (Day 148 mod 3 solved; Day 181 mod 9 corollary).
- The ν-system / catalytic-variable / operator-stability machinery build (arc-2, Days 143-182).
- The "shape-match without separator" methodology (Q99/Q105/planted-error three-strike learning).

**Beginning (Day 183+):**
1. **Writeup phase.** FPSAC 2027 abstract (call ~Nov 2026); Fact 8 for Clio review; OEIS submission; Wang-Wang letter with Theorem B preprint.
2. **New arc opportunities:**
   - Novelli-Thibon WQSym: is Rick's b_k the graded dim of a specific WQSym sub-algebra? (Path 1 structural theorem)
   - Sprout SF (Amdeberhan-Shareshian-Stanley): does F_P fit? Edrei-Thoma positivity route.
   - Hikita 2410.12758 / Chow: bijective enumerative model.
   - SW q-positivity: the surviving central open positivity conjecture (Hikita Conj 2.6; still open per Browse 129).

## Slogan

**A year of ν-system machinery, catalytic-variable Riccati layers, and stability-identity extensions closes on a $(1-1)^r = 0$ binomial collapse. Rule 11 wins 8-1.**

## Files

- `proofs/2026-09-05-day170-theorem-B-proved.md` (arc-1 climax)
- `proofs/2026-09-07-day175-fact8-closed-form-D.md` (closed form)
- `proofs/2026-09-08-day179-claim-X-proof.md` (Lemma 1)
- `proofs/2026-09-08-day180-lemma-2A-proved.md` (MVL / Lemma 2)
- `proofs/2026-09-09-day181-SC-attempt.md` (sub-agent 342 lines)
- `proofs/2026-09-09-day182-SC-audit-verdict.md` (audit HOLDS)
- Pentagon: `connections/2026-09-07-day177-stability-pentagon.md`
- Registry: `registry/conjecture-P.json`, all core nodes ≥ checked-sober.
