"""Empirical scan: min v_2(h_k^{(13)}(a, b)) for k = 7..12 over shell a+b odd,
a, b in [0, 256).

This is EMPIRICAL evidence — not a proof. But if min v_2 >= 16 for all k in
scan range, that's strong evidence LB_k^{(13)} >= 16 for k >= 7.
"""
import pickle
import sys
import time

import numpy as np

# Load fitted h_k coeff for k = 7..12
with open("/home/agent/projects/code/2026-07-12-c13-coeff-high-k.pkl", "rb") as f:
    coeff_high = pickle.load(f)


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def eval_poly(coeff, a, b):
    s = 0
    for (da, db), c in coeff.items():
        s += c * (a ** da) * (b ** db)
    return s


def main():
    c_val = 13
    N = 256
    print(f"Scan min v_2(h_k^{{(13)}}(a, b)) over a+b odd, a, b in [0, {N})")
    for k in sorted(coeff_high.keys()):
        min_v = float('inf')
        argmin = None
        for a in range(N):
            for b in range(N):
                if (a + b) % 2 != c_val % 2:
                    continue
                val = eval_poly(coeff_high[k], a, b)
                if val == 0:
                    continue
                v = v2(val)
                if v < min_v:
                    min_v = v
                    argmin = (a, b, val)
        print(f"  k={k}: min v_2 = {min_v}, argmin (a, b) = {argmin[:2] if argmin else None}")


if __name__ == "__main__":
    sys.exit(main())
