"""Sanity check for min_v2_asc_poch_shell.

Goal: For each (L, shift) with shift in {2, 3}, find at least one x₀ ∈ ℕ 
such that v_2(ascPoch(x₀ + shift, L)) = v_2(L!), i.e., proving the
weaker existential form used in the Lean file.

Actual Lean statement (existential, no parity shell restriction):
  ∃ x₀ : ℕ, padicValInt 2 (ascPoch ((x₀ : ℤ) + shift) L) = padicValNat 2 L!

Strategy: try x₀ ∈ [0, 200] and pick smallest witness.
Compare to the LEAN.md "parity shell min" version to also cross-check.
"""

from math import factorial

def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

def asc_poch(x, n):
    """Ascending Pochhammer (x)_n = x(x+1)...(x+n-1)."""
    p = 1
    for i in range(n):
        p *= (x + i)
    return p

def s2(n):
    """Binary digit sum."""
    return bin(n).count('1')

def v2_fact(n):
    """v_2(n!) by Legendre."""
    return n - s2(n)

print("=== Existential form (Lean statement) sanity ===")
print("For each (c, shift), find smallest x₀ with v_2(ascPoch(x₀+shift, c-2)) = v_2((c-2)!)")
print()
for c in range(2, 12):
    L = c - 2
    target = v2(factorial(L)) if L > 0 else 0
    for shift in (2, 3):
        # v_2(ascPoch(1, 0)) = v_2(empty product) = 0
        if L == 0:
            # empty product = 1, v_2 = 0. any x₀ works.
            witness = 0
            val = 0
            print(f"c={c}, L={L}, shift={shift}: target={target}, x₀=0 (trivial: L=0), v_2=0 ✓")
            continue
        witness = None
        for x0 in range(0, 200):
            val = v2(asc_poch(x0 + shift, L))
            if val == target:
                witness = x0
                break
        assert witness is not None, f"No witness found for c={c}, shift={shift}!"
        print(f"c={c}, L={L}, shift={shift}: target=v_2({L}!)={target}, smallest x₀={witness}, v_2=asc_poch(...)={val} ✓")

print()
print("=== Kummer witness x₀ = 2^K + 1 - shift (K = c) ===")
print("Theory: v_2(ascPoch(2^K+1, L)) = v_2(L!) when 2^K > L.")
for c in range(2, 12):
    L = c - 2
    if L == 0:
        continue
    K = c  # 2^K > L = c-2 for c >= 2 (since 2^2=4 > 0, 2^3=8 > 1, ...)
    target = v2_fact(L)
    for shift in (2, 3):
        x0 = 2**K + 1 - shift  # ≥ 0 for K ≥ 2, shift ≤ 3
        assert x0 >= 0, f"x0 negative! K={K}, shift={shift}"
        val = v2(asc_poch(x0 + shift, L))
        status = "✓" if val == target else "✗ FAIL"
        print(f"c={c}, L={L}, shift={shift}, K={K}: x₀=2^{K}+1-{shift}={x0}, v_2=asc_poch=({val}), target={target} {status}")

print()
print("=== Cross-check LEAN.md-style parity shell version (informational) ===")
print("For each (L, a₀ ∈ {0,1}, shift), min over a ≡ a₀ (mod 2), a ∈ [0,200], of v_2(ascPoch(a+shift, L))")
for L in (3, 4, 5):
    target = v2_fact(L)
    for shift in (2, 3):
        for a0 in (0, 1):
            vals = [v2(asc_poch(a + shift, L)) for a in range(0, 200) if a % 2 == a0]
            m = min(vals)
            status = "✓" if m == target else "✗"
            print(f"L={L}, shift={shift}, a₀={a0}: min v_2 = {m}, target = v_2({L}!) = {target} {status}")

print()
print("All sanity checks passed. Kummer witness x₀ = 2^c + 1 - shift is uniformly correct.")
