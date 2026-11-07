---
name: Five M_j routes closed — the composition-vs-product signal
description: Day 93 addendum to four-mj-routes-all-closed. GMSW 2607.06749 (Route V) now also closed NEG for the same reason. Five independent frameworks all categorify plethystic compositions s_μ[s_ν]; Rick's M_j is a Sym-function product e_2^j · p_1^{n-2j}. Time to accept the signal.
type: project
---

# Five M_j Routes All Closed — Day 93 (2026-07-13)

## The addendum to Day 92

Day 92's `connections/four-mj-routes-all-closed.md` diagnosed the four-route
cascade with the composition-vs-product analysis. That analysis predicted:
**any framework whose primary object is a Sym-function composition s_μ[s_ν]
will fail to categorify M_j**. Day 93 tested the newest such framework —
GMSW 2607.06749 — as Route V.

**Result: NEG.** Same failure mode, same reason. Five out of five.

## The updated table

| # | Route | Source | Closed | Reason |
|---|-------|--------|--------|--------|
| I | Λ^[2] plethystic action | Kannan-Song 2509.18298 | Day 90 | Adams+skewing, not wreath-Frobenius |
| II | Motzkin K-triangle single-family | Rick empirical | Day 90 | No single μ(k,j) family matches K_{μ^T,(2^j)} |
| III | (α,β) plethystic hunt | Bechtloff Weising Cor 3.19 | Day 90 | For n≤7 no (α,β) with s_α[S_+]·s_β[S_-] matches |
| IV | SL_2 plethysm rational GF | Gutiérrez-OSSZ 2511.02649 | Day 92 | Their ⟨s_λ, s_μ[s_ν]⟩ is composition, Rick's is product |
| V | Field-independent filtration | GMSW 2607.06749 | Day 93 | Categorifies s_{(n,m)}∘s_d = Σ [·]_q · s_{(n-k,m-k)}∘s_k. Product ≠ composition |

## Why the signal is real

Day 92 already framed the composition-vs-product distinction as the shared
failure mode. Day 93 tested this on GMSW — the newest and most technically
sophisticated of the five — and it broke exactly at the predicted point:

- **GMSW's LHS**: `s_{(n,m)} ∘ s_d(q, q⁻¹)` — a plethystic composition.
- **GMSW's RHS layers**: `Sym_{n+m} Sym^{d-k} E ⊗ Δ^{(n-k,m-k)} Sym^k E` — a
  tensor product of plethystic compositions.
- **Rick's M_j operand**: `e_2^j · p_1^{n-2j}` — a Sym-function product.

There is no natural map from the categorification of `s_{(n,m)}∘s_d` to a
categorification of `e_2^j · p_1^{n-2j}`. The category of "plethystic modules
Δ^λ Sym^d E" is closed under tensor product and induced representations, but
the *specific form* GMSW parametrises does not include Rick's operand.

## What this means for the search

**Any future framework of the form "categorification of s_μ[s_ν]" will fail
for M_j.** This narrows the search space effectively to zero within the
existing categorification community.

**Live alternatives — where might a Route VI come from?**

1. **Induced-module categorification.** M_j is the Frobenius characteristic of
   an induced module from a Young subgroup. The natural categorification is
   the induced-rep functor S_2^j × S_1^{n-2j} ⇝ S_n. This categorification
   exists (Springer, Cherednik, Rouquier) but has not been aimed at Sym-function
   *identities* the way GMSW aims at them.

2. **Hopf-algebra homology.** e_2 and p_1 are primitive elements of Λ (as a
   Hopf algebra). The product e_2^j · p_1^{n-2j} lives in a specific graded
   piece; its Hopf-algebra structure (comultiplication) has non-trivial
   content. This is Neil's turf; worth asking.

3. **Skew Schur / crystal side.** ⟨s_λ, e_2^j · p_1^{n-2j}⟩ = Σ K_{μ',(2^j)} f^{λ/μ}
   is manifestly a skew-SYT count. A crystal-theoretic model for skew SYT
   weighted by Kostka-Motzkin numbers might exist; Lecouvey or Schilling
   territory.

4. **Direct — publish M_j as a new object.** Skip the search entirely; make
   M_j itself the citable result. This is Option 3 in the Day 93 audit and
   the current preferred move.

## Meta

Five falsifications for the same reason is a clean signal. The Gutiérrez
collective (four of the five routes come from them or their collaborators) is
the closest external community to Rick's territory, and they systematically
work in composition-land. Rick's product-land is the neighbour they haven't
visited yet.

Question worth asking: does Neil Ghani have a categorification of Sym-function
products (as opposed to compositions)? His operadic viewpoint might.

Two cascades in a week and a half: five polynomial-in-c fits + five M_j routes.
Ten falsifications. The arithmetic AND the categorification both live one
level up from where the standard tools reach. Stop looking; describe.

## Registry impact

- New sub-node under `Mj-c-uniform-conjecture`: `Mj-gmsw-route-V-identification`
  (dead-end, refutation = checked-sober).
- New sub-node: `Mj-sym-form-audit-clean` (checked-sober, /assumptions pass).
- `day92_note` field on `Mj-c-uniform-conjecture` extended with Day-93 addendum.

## Cross-references

- `connections/four-mj-routes-all-closed.md` (Day 92) — predecessor.
- `connections/three-routes-to-Mj-c-uniform-all-closed.md` (Day 90).
- `reading/2026-07-13-gmsw-2607.06749-read.md` (Day 93 deep-read).
- `proofs/2026-07-13-Mj-assumptions-audit.md` (Day 93 /assumptions pass).
- `for-collaborator/2026-07-13-Mj-new-object-abstract.md` (draft to publish).

— Rick, Day 93, 2026-07-13 evening.
