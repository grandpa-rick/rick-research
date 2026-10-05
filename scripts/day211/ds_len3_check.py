"""Day 211: operator-DS for e_k*(e_a e_b) from (TC), plus region-expansion re-extraction.
(A) coeffs via Day 210 tc_extract (sum of TC terms, poles cancel, read z^a w^b).
(B) independent extraction: expand each TC term in the region |w|<|z| (K_ij as power series in u=w/z)
    and read z^a w^b termwise; record every (b0, r1, r2) that occurs with nonzero weight and test the
    3-part max/min dominance criterion TERM BY TERM.  a>=b throughout (z carries the larger exponent)."""
import sys; sys.path.insert(0, '/home/agent/projects/scripts/day210')
import sympy as sp, itertools, pickle, time
from multiprocessing import Pool
from tc_extract import coeffs, N, K, s, t, z, w
u = sp.Symbol('u')
def srt(p): return tuple(sorted([x for x in p if x > 0], reverse=True))
def dom(mu, lam):
    A = B = 0
    for i in range(max(len(mu), len(lam))):
        A += mu[i] if i < len(mu) else 0; B += lam[i] if i < len(lam) else 0
        if A < B: return False
    return True
def region_extract(k, a, b):
    out = {}; viol = []
    for b0 in range(k+1):
        n = k - b0
        for i in range(n+1):
            for j in range(n+1-i):
                Ku = sp.series(sp.cancel(K(i, j).subs({z: 1, w: u})), u, 0, b + n + 2).removeO()
                for n1 in range(i, n-j+1):
                    n2 = n - n1
                    pref = (s**(2*b0)*t**(-b0*(i+j))*s**((n1-i)+(n2-j))*t**(-(n1-i)*j-(n2-j)*i)*N(n1, i)*N(n2, j))
                    if sp.cancel(pref) == 0: continue
                    for m in range(0, b + n2 + 1):
                        km = Ku.coeff(u, m)
                        if km == 0: continue
                        r1, r2 = a + n1 + m, b + n2 - m
                        mu = srt((b0, r1, r2))
                        out[mu] = out.get(mu, 0) + pref*km*t**(i*r1 + j*r2)
                        lam = srt((k, a, b))
                        if not dom(mu, lam): viol.append((b0, i, j, n1, m, mu))
    out = {m_: sp.factor(sp.cancel(v)) for m_, v in out.items()}
    return {m_: v for m_, v in out.items() if v != 0}, viol
def job(args):
    k, a, b = args; t0 = time.time()
    A = coeffs(k, a, b)
    lam = srt((k, a, b))
    supp = all(dom(mu, lam) for mu in A)
    lead = sp.factor(A.get(lam, 0))
    offq1 = all(sp.cancel(v.subs(s, 1)) == 0 for mu, v in A.items() if mu != lam)
    B, viol = region_extract(k, a, b) if k <= 2 or (a+b) <= 8 else (None, None)
    agree = None if B is None else all(sp.cancel(A.get(m_, 0) - B.get(m_, 0)) == 0 for m_ in set(A) | set(B))
    return (k, a, b, lam, supp, lead, offq1, agree, viol, sorted(A, reverse=True), time.time()-t0, A)
if __name__ == '__main__':
    K_ = int(sys.argv[1]); AMAX = int(sys.argv[2])
    cases = [(K_, a, b) for a in range(1, AMAX+1) for b in range(0, a+1)]
    res = {}
    with Pool(4) as P:
        for (k, a, b, lam, supp, lead, offq1, agree, viol, sup, dt, A) in P.imap(job, cases):
            res[(k, a, b)] = A
            reg = 'k<=b' if k <= b else 'k>b'
            print(f'e_{k}*(e_{a} e_{b}) [{reg}] lam={lam} supp>=lam:{supp} lead={lead} offdiag(s=1)=0:{offq1} '
                  f'region-extract==TC:{agree} termwise-violations:{len(viol) if viol is not None else None} #supp={len(sup)} ({dt:.0f}s)', flush=True)
            if not supp: print('     support:', sup, flush=True)
    pickle.dump(res, open(f'ds_len3_k{K_}_A{AMAX}.pkl', 'wb'))
