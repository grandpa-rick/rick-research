"""Cross-check: at c=13, k=0..6, (a, b) = (13, 13) (b >= c required for extraction).
Compare h_k^{(13)}(a, b) computed via:
  (i)   Sym-side extract_h_k (uses M_j-c-uniform-conjecture — CHECKED-SOBER independent of Q_k catalog).
  (ii)  Three-var factorization h_k = (a+3)_L (b+2)_L Q_k(a, b, c) using Q_k from Day-89 catalog.
"""
import json
from importlib import util
from sympy import symbols, sympify

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables

with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
    cat = json.load(f)
a_s, b_s, c_s = symbols('a b c')
Q = {}
for ks, s in cat["Q_k_low_k"].items():
    Q[int(ks)] = sympify(s)
Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])


def pochhammer(x, n):
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def main():
    c_val = 13
    jmax = 8

    tables = build_e2_tables(max_j=jmax + 2)

    # Try several (a, b) with b >= c
    for (a, b) in [(13, 13), (15, 13), (20, 15), (30, 13)]:
        print(f"\n(a, b) = ({a}, {b}), c = {c_val}")
        hks_ext = extract_h_k(a, b, c_val, jmax, tables)
        if hks_ext is None:
            print("  extract_h_k returned None")
            continue
        for k in range(7):
            L = c_val - 1 - k
            A = pochhammer(a + 3, L)
            B = pochhammer(b + 2, L)
            Qval = int(Q[k].subs({a_s: a, b_s: b, c_s: c_val}))
            hk_cat = A * B * Qval
            hk_ext = hks_ext[k]
            match = hk_cat == hk_ext
            print(f"  k={k}: catalog={hk_cat}   extract={hk_ext}   match={'YES' if match else 'NO'}")


if __name__ == "__main__":
    main()
