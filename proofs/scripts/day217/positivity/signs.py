import sys, pickle
from sympy import symbols, Poly, expand, together, fraction, factor
s, t, w, v = symbols('s t w v')
basis, MAXN = sys.argv[1], int(sys.argv[2])
G = pickle.load(open(f'g_{basis}_{MAXN}.pkl', 'rb'))
Gs = pickle.load(open(f'g_schur_{MAXN}.pkl', 'rb'))
def content(l): return sum(j-i for i, r in enumerate(l) for j in range(r))
def nn(l): return sum(i*r for i, r in enumerate(l))
def conj(l): return tuple(sum(1 for r in l if r > j) for j in range(l[0])) if l else ()
for k, g in sorted(G.items(), key=lambda kv: (sum(kv[0][0])+sum(kv[0][1]), kv[0])):
    if k[0] > k[1] and (k[1], k[0], k[2]) in G: continue
    h = together(g.subs(t, (1+w)/s).subs(s, 1/(1+v)))
    num, den = fraction(h); P = Poly(expand(num), v, w)
    cs = P.coeffs(); sg = '+' if all(c > 0 for c in cs) else ('-' if all(c < 0 for c in cs) else '?')
    ov = min(m[0] for m in P.monoms()); ow = min(m[1] for m in P.monoms())
    g11 = g.subs({s: 1, t: 1}); g1s = factor(g.subs(t, 1/s))
    print(f'{k}: sign {sg} ord_v {ov} ord_w {ow} g(1,1)={g11} g(t=1/s)={g1s} den={factor(den)} #terms={len(cs)} sum|c|={sum(abs(c) for c in cs)}  g={factor(g)}')
