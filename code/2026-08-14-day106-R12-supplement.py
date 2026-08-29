"""Day 106 supplement — one extra sample at c = 796 (t = 49) for R = 12 proof.

The main job (2026-08-14-day106-R12-proof-via-fit.py) samples c = 12 + 16t for
t = 0..48 (49 targets). The t = 0 sample fails (Pochhammer collapse at c = R),
leaving only 48 usable samples — one short of what a degree-48 polynomial in t
needs. This script adds a single extra sample at c = 796 (t = 49) so that the
merge yields t = 1..49, exactly 49 usable samples.

Output format matches the main JSON: [[t, c, Q_str]].
"""

import time
import json
import sys
from importlib import util
import sympy as sp

spec = util.spec_from_file_location('hkfit', '/home/agent/projects/code/2026-07-10-hk-three-var-fit.py')
hkfit = util.module_from_spec(spec); spec.loader.exec_module(hkfit)
spec2 = util.spec_from_file_location('d102', '/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py')
d102 = util.module_from_spec(spec2); spec2.loader.exec_module(d102)


def main():
    print("Day 106 supplement — extra sample at c = 796 (t = 49)", flush=True)
    tables = hkfit.build_e2_tables(max_j=26)
    a_sym, b_sym = sp.symbols('a b')

    c = 796
    t = (c - 12) // 16  # = 49
    print(f"Computing Q_{{24}}(a, b, c={c}) then evaluating at (a, b) = (10, 12), t = {t}", flush=True)

    t0 = time.time()
    res = d102.fit_Qk_bivar(c, 24, tables)
    if res is None:
        print(f"  c={c}: fit failed", flush=True)
        sys.exit(1)
    Q_poly, _ = res
    Q_val = int(Q_poly.subs({a_sym: 10, b_sym: 12}))
    dt = time.time() - t0
    print(f"  c={c} t={t} Q={Q_val} t_fit={dt:.1f}s", flush=True)

    data = [(t, c, Q_val)]
    out_path = '/home/agent/projects/code/2026-08-14-day106-R12-supplement.json'
    with open(out_path, 'w') as f:
        json.dump([[t, c, str(Q)] for (t, c, Q) in data], f)
    print(f"Wrote {out_path}", flush=True)


if __name__ == '__main__':
    main()
