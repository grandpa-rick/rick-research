"""Wake 222: from cst_n{n}.pkl (exact c_{lam mu}(s,t)) extract v and Lead_{lam mu}(t) = [(s-1)^v] c, for every pair
mu != lam with c != 0; report kappa, coarsening flag, Lead(0), factored Lead; cross-check vs wake221 history leads
(coarsenings) and enumerate minimal raising configurations (Day 220 Thm C step 2) for the t=0 count. Grade: computed."""
import sys, pickle
from itertools import combinations, product
from sympy import symbols, expand, Poly, factor, cancel, together
from kappa import kappa
s, t, e = symbols('s t e')
def is_coarsening(lam, mu):
    # mu = block sums of a set partition of lam's parts
    lam = list(lam)
    def rec(rem, mus):
        if not mus: return not rem
        target = mus[0]
        for r in range(1, len(rem)+1):
            for c in combinations(range(len(rem)), r):
                if sum(rem[i] for i in c) == target:
                    if rec([rem[i] for i in range(len(rem)) if i not in c], mus[1:]): return True
        return False
    return rec(lam, list(mu))
def min_configs(lam, mu, E):
    """all raising configurations m:{(i,j),i<j}->Z>=1 on exactly E edges with alpha>=0, sort+(alpha)=mu."""
    l = len(lam); pairs = [(i, j) for i in range(l) for j in range(i+1, l)]; n = sum(lam); out = []
    for es in combinations(pairs, E):
        for ks in product(range(1, n+1), repeat=E):
            a = list(lam)
            for (i, j), k in zip(es, ks): a[i] += k; a[j] -= k
            if min(a) < 0: continue
            if tuple(sorted([x for x in a if x > 0], reverse=True)) == tuple(mu): out.append(dict(zip(es, ks)))
    return out
def leads(n):
    import os
    fn = f'cst_n{n}.pkl' if os.path.exists(f'cst_n{n}.pkl') else f'cst_n{n}_skip1n.pkl'
    res = pickle.load(open(fn, 'rb')); out = {}
    for (lam, mu), c in res.items():
        if lam == mu or c == 0: continue
        pe = Poly(expand(c.subs(s, e+1)), e); v = min(m[0] for m in pe.monoms())
        L = expand(pe.coeff_monomial(e**v)); out[(lam, mu)] = (v, L)
    return out
if __name__ == '__main__':
    import os
    hist = pickle.load(open('../../wake221/lead/leads_n8.pkl', 'rb'))
    allL = {}
    for n in map(int, sys.argv[1:]):
        if not (os.path.exists(f'cst_n{n}.pkl') or os.path.exists(f'cst_n{n}_skip1n.pkl')): continue
        L = leads(n); allL.update(L)
        for (lam, mu), (v, Ld) in sorted(L.items(), key=lambda x: (x[0][0], x[0][1]), reverse=True):
            k = kappa(lam, mu); co = is_coarsening(lam, mu)
            chk = ''
            if co and len(mu) < len(lam):
                chk = ' hist=' + ('OK' if expand(hist[(lam, mu)][0] - Ld) == 0 else 'MISMATCH')
            cf = min_configs(lam, mu, len(lam)-k) if not co else []
            ncf = f' #minconf={len(cf)}' if not co else ''
            print(f'{lam} -> {mu}: coarsening={co} kappa={k} l-kappa={len(lam)-k} v={v} {"v=l-kappa" if v==len(lam)-k else "V-MISMATCH"}'
                  f' Lead(0)={Ld.subs(t,0)}{ncf}{chk} Lead={factor(Ld)}', flush=True)
    pickle.dump(allL, open('leads_all.pkl', 'wb'))
