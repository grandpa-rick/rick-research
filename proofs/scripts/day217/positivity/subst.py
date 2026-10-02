import sys, pickle
from sympy import symbols, Poly, expand, together, fraction, factor, sign
s, t, w, a, v = symbols('s t w a v')
basis, MAXN = sys.argv[1], int(sys.argv[2])
G = pickle.load(open(f'g_{basis}_{MAXN}.pkl', 'rb'))
def conj(l): return tuple(sum(1 for r in l if r > j) for j in range(l[0])) if l else ()
def coh(p, vs):
    cs = Poly(p, *vs).coeffs(); return 1 if all(c > 0 for c in cs) else (-1 if all(c < 0 for c in cs) else 0)
subs = {
 't=(1+w)/s': (lambda g: g.subs(t, (1+w)/s), (s, w)),
 't=(1+w)/s, s=1/(1+v)': (lambda g: g.subs(t, (1+w)/s).subs(s, 1/(1+v)), (v, w)),
 't=(1+w)/s, s=1-a': (lambda g: g.subs(t, (1+w)/s).subs(s, 1-a), (a, w)),
 'q=st free': (lambda g: g.subs(t, w/s), (s, w)),
}
for name, (f, vs) in subs.items():
    res = {}
    for k, g in G.items():
        num, den = fraction(together(f(g)))
        sd = coh(den, vs)
        res[k] = coh(expand(num), vs)*sd if sd else 0
    nz = [k for k in res if res[k] == 0]
    print(f'{basis} n<={MAXN} {name}: coherent {len(G)-len(nz)}/{len(G)}', ('fail ex '+str(nz[0])+' '+str(factor(G[nz[0]]))) if nz else '')
    if name.startswith('t=(1+w)/s, s=1/'):
        negs = [k for k in res if res[k] < 0]
        print('  negatives:', negs[:12])
