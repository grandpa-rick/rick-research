"""Sanity check: Q_k catalog eval vs extract_h_k for c=14 at (14, 14)."""
import json
from importlib import util
from math import factorial

from sympy import symbols, sympify

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
    d = json.load(f)

a_s, b_s, c_s = symbols('a b c')
Q = {}
for k_str, poly_str in d['Q_k_low_k'].items():
    Q[int(k_str)] = sympify(poly_str)
for k_str, entry in d['Q_k_extended'].items():
    if entry is None:
        continue
    Q[int(k_str)] = sympify(entry['poly_expanded'])

# c=14, a=b=14
c_val = 14
a_val, b_val = 14, 14
tables = mod.build_e2_tables(max_j=8)
hks_extracted = mod.extract_h_k(a_val, b_val, c_val, 6, tables)
print(f"extract_h_k({a_val}, {b_val}, {c_val}) k=0..6 = {hks_extracted}")

for k in range(7):
    L = c_val - 1 - k
    Qv = int(Q[k].subs({a_s: a_val, b_s: b_val, c_s: c_val}))
    pa = rising_fact(a_val + 3, L)
    pb = rising_fact(b_val + 2, L)
    hk_catalog = pa * pb * Qv
    hk_ex = hks_extracted[k]
    match = "OK" if hk_catalog == hk_ex else "MISMATCH"
    print(f"  k={k}: L={L}, Q={Qv}, (a+3)_L={pa}, (b+2)_L={pb}")
    print(f"    h_k catalog = {hk_catalog}")
    print(f"    h_k extract = {hk_ex}    {match}")
