# cross-check fastmodp.hexp (m=mu_1 vars, mod p) against Day 231 Fraction engine (n vars) at t=3/5, n<=5
import sys, os, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'day231'))
sys.argv = ['x', '1']
with contextlib.redirect_stdout(io.StringIO()):
    import check_leads_printed as F
import fastmodp_memo as M
t = 3 * M.inv(5) % M.P; ok = True; c = 0
for n in range(2, 6):
    for lam in M.partitions(n):
        if len(lam) < 2: continue
        fe = F.hexp(lam, F.T0)
        for m in range(1, n + 1):
            me = M.hexp(lam, t, m)
            for mu, co in me.items():
                fc = fe[mu]
                for j in range(len(co)):
                    a = M.frac_to_p(fc[j]) if j < len(fc) else 0
                    if a != co[j]: ok = False; print('MISMATCH', lam, mu, m, j)
                c += 1
print('fastmodp vs Fraction engine, n<=5, all m: %d (lam,mu,m) triples, agree = %s' % (c, ok))
