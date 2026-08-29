"""Day 91 — Full scan of h_k^{(13)} for k=0..6 via three-var factorization.

Verify beta'(13) upper bound. Look for smallest v_2 across many (a, b).
"""
import json
from math import factorial
from sympy import symbols, sympify

with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
    cat = json.load(f)
a_s, b_s, c_s = symbols('a b c')
Q = {}
for ks, s in cat["Q_k_low_k"].items():
    Q[int(ks)] = sympify(s)
Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def pochhammer(x, n):
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def Cn(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k)) if 0 <= k <= n else 0


def compute_hk(a, b, c, k):
    L = c - 1 - k
    A = pochhammer(a + 3, L)
    B = pochhammer(b + 2, L)
    Qval = int(Q[k].subs({a_s: a, b_s: b, c_s: c}))
    return A * B * Qval


def compute_H_c(a, b, j, c):
    """H_c(a, b, j) = sum_{k=0..j} h_k^{(c)}(a, b) * C(j, k). Requires k <= 6."""
    total = 0
    for k in range(j + 1):
        if k > 6:
            return None
        total += compute_hk(a, b, c, k) * Cn(j, k)
    return total


def main():
    c_val = 13
    print(f"c = {c_val}. Scan h_k^{{(13)}}(a, b) for k=0..6, shell a+b odd, a, b < 100.")

    # Per-k min v_2
    min_v_per_k = {k: (float('inf'), None) for k in range(7)}
    N = 100
    for a in range(N):
        for b in range(N):
            if (a + b) % 2 != c_val % 2:
                continue
            for k in range(7):
                hk = compute_hk(a, b, c_val, k)
                if hk == 0:
                    continue
                v = v2(abs(hk))
                if v < min_v_per_k[k][0]:
                    min_v_per_k[k] = (v, (a, b))

    print(f"\nPer-k min v_2(h_k^{{(13)}}) in [0, {N})^2:")
    for k in range(7):
        m, ach = min_v_per_k[k]
        print(f"  k={k}: min v_2 = {m}   at {ach}")

    # Overall min k*
    kmin = min(range(7), key=lambda k: min_v_per_k[k][0])
    print(f"\nargmin k* = {kmin}, min v_2 = {min_v_per_k[kmin][0]}")

    # Also scan H_13(a, b, j) for j <= 6 (need k <= 6 in the sum)
    print(f"\nScanning H_13(a, b, j) for j=0..6, a+b odd, a,b<30 for lowest v_2:")
    global_min = float('inf')
    for j in range(7):
        best_v = float('inf')
        best_ab = None
        for a in range(30):
            for b in range(30):
                if (a + b) % 2 != c_val % 2:
                    continue
                Hc = compute_H_c(a, b, j, c_val)
                if Hc == 0:
                    continue
                v = v2(abs(Hc))
                if v < best_v:
                    best_v = v
                    best_ab = (a, b)
        print(f"  j={j}: min v_2(H_13(a,b,{j})) = {best_v}   at {best_ab}")
        if best_v < global_min:
            global_min = best_v

    print(f"\nGlobal min v_2(H_13(a, b, j)) for j <= 6 in scan = {global_min}")
    print(f"Hence beta'(13) <= {global_min}.")


if __name__ == "__main__":
    main()
