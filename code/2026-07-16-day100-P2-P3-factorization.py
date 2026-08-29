"""Day 100 PROVE — Verification of the P_hat_k clean factorisation lemma (Lemma 5.1).

For c = 4m+2:
    P_hat_2(a, b, 4m+2) = 2(a+2)(b+1) - 4m(4m+1)^2
    P_hat_3(a, b, 4m+2) = 6(a+2)(b+1) - 4m(4m-1)(4m+1)

Both are used in proofs/2026-07-16-day100-G3-matching-LB.md §5 for
G3 at k=2 and k=3.
"""
from sympy import symbols, expand

a, b, c, m = symbols('a b c m')

# P_hat_k = Q_k / (leading c-linear factors), evaluated at c = 4m+2

# k=2: Q_2 = -c * P_hat_2, so P_hat_2 = 2ab + 2a + 4b + (-c^3 + 4c^2 - 5c + 6)
P2_hat = 2*a*b + 2*a + 4*b + (-c**3 + 4*c**2 - 5*c + 6)
P2_at = expand(P2_hat.subs(c, 4*m + 2))
guess2 = expand(2*(a+2)*(b+1) - 4*m*(4*m+1)**2)
assert expand(P2_at - guess2) == 0, f"P_hat_2 fails: {expand(P2_at - guess2)}"
print("Lemma 5.1a (P_hat_2): VERIFIED")
print(f"  P_hat_2(a, b, 4m+2) = 2(a+2)(b+1) - 4m(4m+1)^2 = {P2_at}")

# k=3: Q_3 = c(c-1)(c-2) * P_hat_3
P3_hat = 6*a*b + 6*a + 12*b + (-c**3 + 6*c**2 - 11*c + 18)
P3_at = expand(P3_hat.subs(c, 4*m + 2))
guess3 = expand(6*(a+2)*(b+1) - 4*m*(4*m-1)*(4*m+1))
assert expand(P3_at - guess3) == 0, f"P_hat_3 fails: {expand(P3_at - guess3)}"
print("Lemma 5.1b (P_hat_3): VERIFIED")
print(f"  P_hat_3(a, b, 4m+2) = 6(a+2)(b+1) - 4m(4m-1)(4m+1) = {P3_at}")


# --- Exhaustive numerical verification of G3 for k=0, 1, 2, 3 ---

def v2(n):
    if n == 0: return 100
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

def s2(n):
    return bin(n).count('1')

def carries(x, y):
    return s2(x) + s2(y) - s2(x + y)

print("\nExhaustive verification of G3 bounds for k in {0,1,2,3}:")
print("  m in [1, 19], (a, b) in [0, 32)^2 shell (a+b even)")

fails = 0
oks = 0
for m_val in range(1, 20):
    c_val = 4 * m_val + 2
    target = 8 * m_val + 1 - 2 * s2(m_val) - v2(m_val)  # beta - D_anchor
    for k in [0, 1, 2, 3]:
        L = c_val - 1 - k
        Lv2fact = L - s2(L)
        for a_val in range(0, 32):
            for b_val in range(0, 32):
                if (a_val + b_val) % 2 != 0:
                    continue
                if k == 0:
                    v2Q = 0
                elif k == 1:
                    v2Q = v2(c_val) + v2(c_val - 1)
                elif k == 2:
                    P = 2 * (a_val + 2) * (b_val + 1) - 4 * m_val * (4 * m_val + 1) ** 2
                    v2Q = v2(c_val) + v2(P) if P != 0 else 100
                elif k == 3:
                    P = 6 * (a_val + 2) * (b_val + 1) - 4 * m_val * (4 * m_val - 1) * (4 * m_val + 1)
                    v2Q = v2(c_val) + v2(c_val - 1) + v2(c_val - 2) + v2(P) if P != 0 else 100
                ca = carries(a_val + 2, L)
                cb = carries(b_val + 1, L)
                total = 2 * Lv2fact + ca + cb + v2Q
                if total < target:
                    fails += 1
                    if fails < 5:
                        print(f"  FAIL: m={m_val}, k={k}, (a,b)=({a_val},{b_val}): total={total} < target={target}")
                else:
                    oks += 1

print(f"\nResult: {oks} passing, {fails} failures")
assert fails == 0, "G3 for k <= 3 should hold everywhere!"
print("All G3 bounds for k in {0,1,2,3} verified.")
