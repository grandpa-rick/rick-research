"""Verify distinct-min witnesses at c=15 and c=17 using Q_k catalog."""
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


def check_witness(a, b, c_val, k_star, label=""):
    print(f"\n{label}: (a,b,k*)=({a},{b},{k_star}), c={c_val}")
    summands = []
    total = 0
    for k in range(k_star + 1):
        hk = compute_hk(a, b, c_val, k)
        C = Cn(k_star, k)
        contrib = C * hk
        total += contrib
        summands.append((k, hk, C, contrib, v2(abs(contrib))))
    v_H = v2(abs(total))
    carrier_v = summands[k_star][4]
    others = [s[4] for i, s in enumerate(summands) if i != k_star]
    ok = all(o > carrier_v for o in others) if others else False
    print(f"  H_{c_val}({a},{b},{k_star}) = {total}   v_2 = {v_H}   carrier v_2 = {carrier_v}   distinct-min: {ok}")
    print(f"  per-j v_2: {[s[4] for s in summands]}")
    return v_H, ok


def main():
    # c=15 scan said min at (1, 2, j=6) with v_2 = 20
    check_witness(1, 2, 15, 6, "c=15, k=6")
    check_witness(2, 3, 15, 3, "c=15, k=3")

    # c=17 scan said min at (15, 0, j=2 or 3 or 6) with v_2 = 23
    check_witness(15, 0, 17, 2, "c=17, k=2")
    check_witness(15, 0, 17, 3, "c=17, k=3")
    check_witness(15, 0, 17, 6, "c=17, k=6")

    # c=12 min at (1, 3) for j=0 (with v_2=18)
    check_witness(1, 3, 12, 1, "c=12, k=1")
    check_witness(0, 0, 12, 6, "c=12, k=6")


if __name__ == "__main__":
    main()
