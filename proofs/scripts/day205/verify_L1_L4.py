"""Direct re-verification of (L1)-(L4) with the EXACT Day 198/204 convention
(common.sigma, cross-checked vs day204 sigma_m_apply in check_convention.py).
Checked as POLYNOMIAL identities in Q(t)[X_1..X_m] (no e-basis extraction needed,
so this is meaningful for every m, including m < r+2 where e_n = 0 for n > m).
Usage: python3 verify_L1_L4.py RMAX MEXTRA
"""
import sys, time
import sympy as sp
from common import sigma, Xs, e, qint, t

def pieces(m, r):
    X = Xs(m); x1 = X[0]; tl = list(X[1:]); E = lambda n: e(X, n)
    L = {}
    L['L1'] = (x1*e(tl, r)*e(tl, 1),
               qint(r+2)*E(r+2) + t*qint(r)*E(r+1)*E(1))
    L['L2'] = (x1**2*e(tl, r),
               -qint(r+2)*E(r+2) + E(r+1)*E(1))
    L['L3'] = (x1**2*e(tl, r-1)*e(tl, 1),
               -qint(r+2)*E(r+2) - t*qint(r)*E(r+1)*E(1) + qint(2)*E(r)*E(2))
    L['L4'] = (x1**3*e(tl, r-1),
               qint(r+2)*E(r+2) - E(r+1)*E(1) - qint(2)*E(r)*E(2) + E(r)*E(1)*E(1))
    return L

rmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
mextra = int(sys.argv[2]) if len(sys.argv) > 2 else 3
ok = True
for r in range(0, rmax+1):
    for m in range(1, r+mextra+1):
        t0 = time.time()
        res = []
        for name, (F, rhs) in pieces(m, r).items():
            d = sp.expand(sigma(F, m) - rhs)
            res.append(d == 0)
            if d != 0:
                ok = False
                print(f"  FAIL r={r} m={m} {name}: diff = {sp.factor(d)}")
        print(f"r={r} m={m}: L1..L4 {res}  ({time.time()-t0:.1f}s)", flush=True)
print("(L1)-(L4) direct:", "PASS" if ok else "FAIL")
