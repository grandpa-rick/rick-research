"""g = c*s^{dc} + (1-s)(st-1) R(s,t): test R Laurent and sign coherent."""
import sys, pickle
from sympy import symbols, Poly, expand, together, fraction, factor, cancel, simplify
s, t = symbols('s t')
MAXN = int(sys.argv[1])
G = pickle.load(open(f'g_schur_{MAXN}.pkl', 'rb'))
def content(l): return sum(j-i for i, r in enumerate(l) for j in range(r))
lines = []; stats = {'+': 0, '-': 0, '?': 0, 'nonlaurent': 0}; bad = []
for k, g in sorted(G.items(), key=lambda kv: (sum(kv[0][0])+sum(kv[0][1]), kv[0])):
    lam, mu, nu = k
    c = g.subs({s: 1, t: 1}); dc = content(nu)-content(lam)-content(mu)
    assert cancel(g.subs(t, 1/s) - c*s**dc) == 0, k
    R = cancel((g - c*s**dc)/((1-s)*(s*t-1)))
    num, den = fraction(together(R))
    if len(Poly(den, s, t).terms()) != 1: stats['nonlaurent'] += 1; bad.append(k); continue
    cs = Poly(expand(num), s, t).coeffs() if num != 0 else [0]
    sg = '0' if num == 0 else ('+' if all(x > 0 for x in cs) else ('-' if all(x < 0 for x in cs) else '?'))
    stats[sg] = stats.get(sg, 0)+1
    lines.append(f'{k}: c={c} dc={dc} R={factor(R)} sign {sg}')
open(f'R_schur_{MAXN}.txt', 'w').write('\n'.join(lines))
print(MAXN, stats, 'nonlaurent ex', bad[:3])
