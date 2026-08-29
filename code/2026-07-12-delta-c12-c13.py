"""Day 91 — Compute Delta_k^{(c)} at c = 12, 13 using ONLY the Q_k catalog (k=0..6).

Gives UB_k = 2*v_2(L!) + Delta_k for k <= 6.
Note: argmin might be at k > 6 for larger c. If so, we get an UB on min_k UB_k.

Comparison to D2':
  beta'(12) predicted = 19  (D(12) = 0)
  beta'(13) predicted = 18  (D(13) = 4)
"""
import json
from math import factorial
from sympy import symbols, sympify, Poly, expand


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def compute_delta(Q_poly, a_s, b_s, c_s, c_val, k_val, T=8):
    L = c_val - 1 - k_val
    shell_parity = c_val % 2
    Q_c = expand(Q_poly.subs(c_s, c_val))
    p = Poly(Q_c, a_s, b_s)
    coeffs = p.as_dict()
    def eval_Q(av, bv):
        s = 0
        for (da, db), coef in coeffs.items():
            s += int(coef) * (av ** da) * (bv ** db)
        return s

    min_v = float('inf')
    achievers = []
    for a in range(2 ** T):
        if (a + 2) & L != 0:
            continue
        for b in range(2 ** T):
            if (a + b) % 2 != shell_parity:
                continue
            if (b + 1) & L != 0:
                continue
            val = eval_Q(a, b)
            if val == 0:
                continue
            v = v2(val)
            if v < min_v:
                min_v = v
                achievers = [(a, b, val)]
            elif v == min_v and len(achievers) < 5:
                achievers.append((a, b, val))
    return min_v, achievers


def main():
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    a_s, b_s, c_s = symbols('a b c')
    Q = {}
    for ks, s in cat["Q_k_low_k"].items():
        Q[int(ks)] = sympify(s)
    Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])

    for c_val in [12, 13]:
        print(f"\n{'='*72}\n c = {c_val}    (D2' predicts beta'({c_val}) = {'19' if c_val==12 else '18'})\n{'='*72}")
        print(f"  {'k':>2s}  {'L':>3s}  {'v_2(L!)':>8s}  {'Delta':>6s}  {'UB_k':>6s}")
        min_UB = float('inf')
        argmin_k = None
        for k in range(7):
            L = c_val - 1 - k
            if L < 0:
                continue
            T = max(7, L.bit_length() + 3)
            delta, ach = compute_delta(Q[k], a_s, b_s, c_s, c_val, k, T=T)
            v2_L = v2(factorial(L))
            if delta == float('inf'):
                print(f"  {k:>2d}  {L:>3d}  {v2_L:>8d}  {'inf':>6s}  {'inf':>6s}")
                continue
            UB = 2 * v2_L + delta
            marker = ""
            if UB < min_UB:
                min_UB = UB
                argmin_k = k
                marker = " <-- min so far"
            print(f"  {k:>2d}  {L:>3d}  {v2_L:>8d}  {delta:>6d}  {UB:>6d}{marker}")
        print(f"\n  min_k UB (k<=6): {min_UB} at k*={argmin_k}")
        target = 19 if c_val == 12 else 18
        if min_UB == target:
            print(f"  MATCHES D2' prediction of beta'({c_val}) = {target}.")
        elif min_UB < target:
            print(f"  min UB < D2' prediction — either UB is not tight OR beta'({c_val}) < {target} (mismatch)")
        else:
            print(f"  min UB > D2' prediction — argmin at k > 6 (need Q_7+ extraction) OR beta'({c_val}) > {target}")


if __name__ == "__main__":
    main()
