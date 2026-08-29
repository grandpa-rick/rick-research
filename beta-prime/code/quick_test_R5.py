"""Quick timing test: fit Q_10 at c=12 to estimate cost per c-value."""
import sys, time
sys.path.insert(0, '/home/agent/projects/code')
from importlib import util
import sympy as sp

spec_hk = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec_hk); spec_hk.loader.exec_module(hkfit)
spec_d102 = util.spec_from_file_location(
    "d102", "/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py"
)
d102 = util.module_from_spec(spec_d102); spec_d102.loader.exec_module(d102)

R = 5
t0 = time.time()
tables = hkfit.build_e2_tables(max_j=2*R+2)
print(f"tables built {time.time()-t0:.1f}s")

for cv in [12, 13]:
    t0 = time.time()
    r = d102.fit_Qk_bivar(cv, 2*R, tables)
    print(f"c={cv}: {time.time()-t0:.1f}s, result: {'ok' if r else 'FAIL'}")
    if r is not None:
        poly, D = r
        a, b = sp.symbols('a b')
        # substitute a = -2
        p_sliced = sp.expand(poly.subs(a, -2))
        print(f"  Q_bivar has D = {D}, a=-2 slice as b-poly:")
        p_sliced_poly = sp.Poly(p_sliced, b) if p_sliced != 0 else None
        if p_sliced_poly is not None:
            print(f"    degree in b: {p_sliced_poly.degree()}, coefs: {p_sliced_poly.all_coeffs()}")
        else:
            print(f"    identically zero")
