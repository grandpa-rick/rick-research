"""Anchor identity (E) β'(4k) = β(4k) — check against γ upper bound.

Day 84 note (proofs/2026-07-08-d1-partial.md) states:
    (E) β'(4k) = β(4k) for all k ≥ 1

Data verifies:
    k=1: β'(4) = 4 = β(4) ✓
    k=2: β'(8) = 11 = β(8) ✓

But β'(c) ≤ γ(c) always (j=0 is a valid choice in min).
So (E) requires γ(4k) ≥ β(4k) for all k.

Test this constraint at k=1..8.
"""
from hc import beta, gamma, v2, s2, H_c_at_j0


def brute_min_j0_valid_parity(c, box=80):
    """Min v₂(H_c(a,b,0)) over (a,b) same-parity (valid for even c)."""
    best = float('inf')
    pt = None
    for a in range(box):
        for b in range(box):
            if (a + b) % 2 != 0:
                continue
            h = H_c_at_j0(a, b, c)
            if h == 0:
                continue
            val = v2(h)
            if val < best:
                best = val
                pt = (a, b)
    return best, pt


print("=" * 78)
print("Anchor (E) β'(4k) = β(4k) check via β' ≤ γ constraint")
print("=" * 78)
print(f"{'k':>3} {'c=4k':>5} {'β(c)':>5} {'γ(c)':>5} {'γ<β?':>7} {'(E) impossible?':>17}")
for k in range(1, 9):
    c = 4 * k
    b_c = beta(c)
    g_c = gamma(c)
    violated = g_c < b_c
    verdict = "YES — (E) FAILS" if violated else "no — (E) possible"
    print(f"{k:>3} {c:>5} {b_c:>5} {g_c:>5} {str(violated):>7} {verdict:>17}")

print()
print("=" * 78)
print("At k=1,2: (E) empirically verified (β'(4)=4, β'(8)=11)")
print("At k≥3: γ(4k) < β(4k), so β'(4k) ≤ γ(4k) < β(4k) — (E) IS FALSE.")
print("=" * 78)

# Concrete brute-force sanity check
print("\nBrute-force min v₂(H_c(a,b,0)) at c=12, 16 (same-parity, box=80):")
for c in [4, 8, 12, 16]:
    v, pt = brute_min_j0_valid_parity(c, box=80)
    print(f"  c={c}: min v₂ = {v} at (a,b) = {pt}, β(c) = {beta(c)}, γ(c) = {gamma(c)}")


print()
print("=" * 78)
print("CONSEQUENCE for Day 84 Theorem 4:")
print("=" * 78)
print("""
Theorem 4 (β'(c) = β(c) − D(c) with D(4k)=0) predicts:
    β'(12) = β(12) = 19
    β'(16) = β(16) = 26

But actually:
    β'(12) ≤ γ(12) = 18 (with 18 achieved at j=0)
    β'(16) ≤ γ(16) = 26 (this one might be tight)

So Theorem 4 FAILS at c=12 (predicts 19, actual ≤ 18).

At c=16 the situation is more delicate:
    γ(16) = β(16) = 26. So β'(16) ≤ 26, and β'(16) = 26 is *possible*.
    But we haven't verified it — could still be lower.

REVISION NEEDED: (E) β'(4k)=β(4k) holds only when γ(4k)=β(4k),
which is when 2 + s₂(2k) + s₂(2k-1) = s₂(4k-1).

Let's check:
""")
for k in range(1, 9):
    c = 4 * k
    lhs = 2 + s2(2*k) + s2(2*k - 1)
    rhs = s2(4*k - 1)
    match = "✓" if lhs == rhs else "✗"
    print(f"  k={k}, c={c}: 2 + s₂({2*k}) + s₂({2*k-1}) = {lhs}; s₂({4*k-1}) = {rhs}  {match}")

print()
print("So (E) can hold only at k ∈ {1, 2, 4, 8, ...} — powers of 2!?")
print("Notice: k=4 gives c=16, and γ(16) = β(16) = 26 (as we computed).")
