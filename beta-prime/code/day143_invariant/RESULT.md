# Day 143 — Universal Invariant Quadratic Identity

## Headline

For the Frobenius identity L·F_P = F_P·X (Day 142), the universal
invariant sequence [E_3^k T^{3k-1}] X satisfies a QUADRATIC generating-
function identity:

    ┌─────────────────────────────────────────────────────────┐
    │  a_k = −b_k + Σ_{i+j=k, i,j≥1} b_i b_j                  │
    │                                                          │
    │  (1 − 2F(τ))² = 1 + 4 A(τ)                              │
    │                                                          │
    │  where A(τ) = Σ_k a_k τ^k,                              │
    │        F(τ) = Σ_k (3k−1) · N_k[T^{3k-1}] · τ^k          │
    └─────────────────────────────────────────────────────────┘

Companion statement:  [E_3^k T^b] X = 0 for all b < 3k−1.

## Sequences

    a_k :=  [E_3^k T^{3k-1}] X       = -3, -18, -255, -4620, -94500,
                                       -2078802, -48005802  (k = 1..7)

    b_k := (3k-1) · N_k[T^{3k-1}]    = 3, 27, 417, 7851, 164124,
                                       3661389, 85384566   (k = 1..7)

Related:  n_k := b_k / (3k-1) = 3/2, 27/5, 417/8, 7851/11, 82062/7,
                                3661389/17, 42692283/10.

## Verification

- a_k directly computed at (U,V)=(0,0) for k=1..7 (`extend_invariant.py`, `extend_k7.py`).
- Identity a_k = -b_k + Σ b_i b_j verified for k=1..6 (`verify_recurrence.py`).
- Predicted b_7 = 85384566 from the identity (using known a_7 and b_1..b_6).
- INDEPENDENTLY VERIFIED b_7 = 85384566 by directly computing n_7 = 42692283/10 (`compute_n7.py`).
- Vanishing lemma N_k[T^b] = 0 for 2k ≤ b < 3k-1 verified at (U,V) = (0,0), (1,1), (2,3), (-1,2) for k ≤ 5 (`check_lowT_Nk.py`).
- Vanishing [E_3^k T^b] X = 0 for b < 3k-1 verified at (U,V)=(0,0) for k=1..7 (`verify_vanishing.py`, `verify_k7_vanishing.py`).
- b_k does NOT satisfy any P-recurrence of order ≤ 3, degree ≤ 4 with 7 data points (`search_b_recurrence.py`).
- X_1 in Vieta variables (α,β=U+V,UV) — β=0 slice = -(α+1)_{b-3}[(2b-1)α + (b-2)(b-1)], no full closure (`vieta_X1.py`).

## Files

| File | Purpose |
|---|---|
| `extend_invariant.py` | Compute a_1..a_6 at (U,V)=(0,0) via X = L·F_P/F_P |
| `extend_k7.py` | Compute a_7 = -48005802 (needs B_MAX=21) |
| `compute_n7.py` | Independent verification: n_7 = 42692283/10 |
| `check_lowT_Nk.py` | Verifies lowest-T of N_k at multiple (U,V) |
| `check_other_diagonals.py` | Confirms [T^{3k-2}] X = 0 universal; [T^{3k}] depends on (U,V) |
| `verify_recurrence.py` | Confirms a_k = -b_k + Σ b_i b_j for k=1..6 |
| `verify_vanishing.py` | Full [E_3^k T^b] X vanishing pattern for k=1..6 |
| `verify_k7_vanishing.py` | Extends vanishing verification to k=7 |
| `analyze_seq.py` | Rational search for closed form of a_k directly (negative) |
| `search_b_recurrence.py` | No low-order P-recurrence for b_k (negative) |
| `vieta_X1.py` | X_1 in Vieta variables α=U+V, β=UV |

## Proof sketch

Starting from L(f·G)/(f·G) = (LG − TUV·G)/G + 2Tφ·(θG/G), with G = exp(R),

    X = [T(U+V) − 1 + 2Tφ] · θR + T · θ²R + T · (θR)².

At E_3^k and [T^b] for b ≤ 3k−1, the linear terms give 0 unless b = 3k−1
(need N_k[T^{b or b-1}] which vanish for b < 3k-1); the quadratic
(θR)² term forces (a, c) = (3i−1, 3j−1) at b = 3k−1, contributing
Σ b_i b_j.  The linear terms give exactly −b_k.

## Consequence

The invariant sequence (a_k) is not closable as a hypergeometric or
factorial-ratio expression (prime factors like 17, 10499, 4743587 rule
these out), but IS closable via a quadratic transform of the leading
cumulant sequence (b_k).  The identity 1 + 4A = (1 − 2F)² is a
NONTRIVIAL structural fact about A.

## FPSAC placement

- Theorem 3.7: quadratic identity and companion vanishing.
- Conjecture 4.2: closed form for b_k (or equivalently a_k).
- Predicts b_8, a_8 verifiable via extension to B_MAX=24.

## Time

Deep-work session ~2 hours: 40 min for (0,0)-side computations, remainder
for structural derivation, verification, and write-up.

## Deliverable to Rick

`/home/agent/projects/proofs/2026-08-28-day143-invariant-quadratic-identity.md`
`/home/agent/projects/memory/for-collaborator/2026-08-28-day143-quadratic-identity.md`
