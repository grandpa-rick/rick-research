"""Day 104 sanity: Q_4(0, 2, c) is constant v_2 = 5 for c ≡ 2 mod 16?"""

import json
from sympy import symbols, sympify


CATALOG_PATH = "/home/agent/projects/code/2026-07-11-Qk-catalog.json"


def v2(n):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def main():
    a, b, c = symbols('a b c')
    with open(CATALOG_PATH) as f:
        cat = json.load(f)
    Q4 = sympify(cat['Q_k_low_k']['4'])
    print("Q_4(a, b, c) =", Q4)

    print("\nQ_4(0, 2, c) for c ≡ 2 mod 16, c ≥ 18:")
    for c_val in range(18, 500, 16):
        val = int(Q4.subs({a: 0, b: 2, c: c_val}))
        v = v2(val)
        print(f"  c={c_val:3d}  Q_4(0,2,{c_val}) = {val}   v_2 = {v}")


if __name__ == '__main__':
    main()
