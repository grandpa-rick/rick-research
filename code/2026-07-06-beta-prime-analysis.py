"""
Analysis of β'(c) — heavy-quotient constant floor — for the joint note.

Data from Clio (2026-07-04, 2026-07-05):
    β'(c) for c = 4..10 :  4, 3, 7, 6, 11, 9, 14

Rick's β (rigid NL anchor):
    β(c) = (c-1) + v2((c-1)!) = 2(c-1) - s2(c-1)
    → β(c) for c=1..12 : 0, 1, 3, 4, 7, 8, 10, 11, 15, 16, 18, 19

γ(c) = content of H_c(0) on valid-parity sheet:
    c=2k    : γ = 4k - 2 - s2(k) - s2(k-1)
    c=2k+1  : γ = 4k - 2·s2(k)

The dimer law: β'(2k+1) = β'(2k) - 1
    c=5 : 3 = 4-1  ✓
    c=6 : baseline
    c=7 : 6 = 7-1  ✓
    c=8 : baseline
    c=9 : 9 ≠ 11-2, and 11-1=10 predicted, but got 9  ✗  ← ANOMALY

Rick's hypothesis: c=9 is anomalous because c=9 ≡ 1 (mod 4).
Refinement question: c ≡ 1 (mod 4) or c ≡ 1 (mod 8)?

c ≡ 1 (mod 4): c ∈ {1, 5, 9, 13, 17, ...}
    c=5 → dimer holds. FAILS hypothesis.
c ≡ 1 (mod 8): c ∈ {1, 9, 17, ...}
    c=1 : dimer vacuous (β'(0) not defined)
    c=9 : breaks   ← matches
c ≡ 5 (mod 8): {5, 13, 21, ...}
    c=5 : dimer holds

So "c ≡ 1 mod 8" is a much better fit than "c ≡ 1 mod 4".

Note also: c=9 is the first odd c with s2(c-1) = s2(8) = 1 (single 1-bit at bit 3),
matching v2((c-1)!) jumping. This IS a "carry event" — c-1 crosses a power of 2.

Let me tabulate.
"""
from math import factorial


def s2(n):
    return bin(n).count('1')


def v2(n):
    if n == 0:
        return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def beta_rick(c):
    return 2 * (c - 1) - s2(c - 1)


def gamma(c):
    if c % 2 == 0:
        k = c // 2
        return 4 * k - 2 - s2(k) - s2(k - 1)
    k = (c - 1) // 2
    return 4 * k - 2 * s2(k)


# Clio's reported β' for c=4..10
beta_prime_data = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14}


def dimer_predicted(k):
    """β'(2k+1) predicted from dimer law = β'(2k) - 1."""
    if 2 * k in beta_prime_data:
        return beta_prime_data[2 * k] - 1
    return None


print("=" * 70)
print("Table 1: All the floor invariants for c ∈ {1..12}")
print("=" * 70)
print(f"{'c':>3} {'c-1':>4} {'s2(c-1)':>8} {'v2((c-1)!)':>11} "
      f"{'β(c)':>5} {'γ(c)':>5} {'β prime':>8} {'γ-β prime':>10}")
for c in range(1, 13):
    b = beta_rick(c)
    g = gamma(c)
    bp = beta_prime_data.get(c, None)
    dip = (g - bp) if bp is not None else None
    print(f"{c:>3} {c-1:>4} {s2(c-1):>8} {v2(factorial(c-1)):>11} "
          f"{b:>5} {g:>5} {str(bp):>8} {str(dip):>10}")

print()
print("=" * 70)
print("Table 2: Test the dimer law β'(2k+1) = β'(2k) - 1")
print("=" * 70)
for k in range(2, 6):
    c_odd = 2 * k + 1
    c_even = 2 * k
    if c_even in beta_prime_data and c_odd in beta_prime_data:
        predicted = beta_prime_data[c_even] - 1
        actual = beta_prime_data[c_odd]
        status = "OK" if predicted == actual else "FAIL"
        gap = actual - predicted
        print(f"c={c_odd} (k={k}): β'({c_even})={beta_prime_data[c_even]}, "
              f"predicted β'({c_odd})={predicted}, actual={actual} "
              f"[{status}, gap={gap}]  c mod 4 = {c_odd % 4}, c mod 8 = {c_odd % 8}")

print()
print("=" * 70)
print("Table 3: Which odd c are candidates for anomaly?")
print("=" * 70)
print(f"{'c':>3} {'c mod 4':>8} {'c mod 8':>8} {'s2(c-1)':>8} "
      f"{'v2(c-1)':>8} {'dimer_status':>20}")
for c in range(3, 20, 2):
    m4 = c % 4
    m8 = c % 8
    status = "FAILS" if c == 9 else ("holds" if c in (5, 7) else "UNKNOWN")
    print(f"{c:>3} {m4:>8} {m8:>8} {s2(c-1):>8} {v2(c-1):>8} {status:>20}")

print()
print("=" * 70)
print("Structural observations:")
print("=" * 70)
print("""
- The dimer failure at c=9 coincides with c-1=8 being a pure power of 2 (v2(8)=3, s2(8)=1).
- Note: c=9 has s2(c-1)=1 (single 1-bit); c=5,7 have s2(c-1)=2,2.
- Rick's β(c) jump: β(5)-β(4)=3, β(9)-β(8)=4. The jump when c crosses a power of 2 is
  larger, reflecting v2((c-1)!) picking up an extra factor.
- Meanwhile β'(c) at c=9 is 9, which is LOWER than the dimer prediction (10). So the
  heavy quotient acquired an EXTRA power of 2 that the ambient run-content didn't predict.
  This is a "collision" — the heavy quotient found an (a,b,j) achieving unusually low content.

Working hypothesis (Rick's, refined):
    The dimer law fails at c ≡ 1 (mod 8), i.e. when c-1 is divisible by 8 (a 2^3 crossing).
    Reason: at c-1 = 2^k, the v2((c-1)!) jump is dominated by a single power-of-2 event
    that decouples β from β' — the ambient/internal channels desynchronize by an amount
    that the "run-content" γ(c) formula doesn't feel.

Concrete predictions to test:
    c=17: c-1=16=2^4. Expect dimer to FAIL again (β'(17) < β'(16)-1).
    c=13: c-1=12=4·3. Expect dimer to HOLD.
    c=25: c-1=24. Expect dimer to HOLD.
    c=33: c-1=32=2^5. Expect dimer to FAIL.
""")

print("=" * 70)
print("Alternative hypothesis check: v2(c-1) ≥ 3 as the criterion")
print("=" * 70)
for c in range(3, 20, 2):
    v = v2(c - 1)
    predicted_break = v >= 3
    print(f"c={c}: v2(c-1)={v}, would break dimer? {'YES' if predicted_break else 'no'}")
