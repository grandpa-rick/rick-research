"""Localization check of Thm 4.20 (pulled back, LS12 indexing) independent of LS12 Cor 3.4.
Uses LS12 (2.6),(2.8),(2.14),(2.15): psi^v(w) = coeff of T_v in w in K_Q; L^lam(u)=e^{u lam}.
Checks e^{-u om} psi^{z_k}(u) = sum_rho A_{k rho} psi^{z_rho}(u) for all u in W."""
import sys, itertools
import sympy as sp
sys.setrecursionlimit(10000)
from check import setup
from fractions import Fraction as Fr
m = int(sys.argv[1]); variant = sys.argv[2] if len(sys.argv)>2 else "printed"
S = setup(m); W, act, mul, L, leq = S['W'], S['act'], S['mul'], S['L'], S['leq']
x = sp.symbols('x1:%d' % (m+1))
def mono(mu):
    r = sp.Integer(1)
    for i, c in enumerate(mu): r *= x[i]**int(c)
    return r
def sact(w, f):  # w acting on Laurent poly: x^mu -> x^{w mu}
    sub = {}
    # x_i = e^{eps_i} -> e^{w eps_i} = x_{p(i)}^{s}
    for i, (j, s) in enumerate(w): sub[x[i]] = x[j]**s
    return f.subs(sub, simultaneous=True)
e = tuple((i, 1) for i in range(m))
simple = []
for i in range(m-1):
    img = list(e); img[i] = (i+1, 1); img[i+1] = (i, 1); simple.append(tuple(img))
img = list(e); img[m-1] = (m-1, -1); simple.append(tuple(img))
alpha = []
for i in range(m-1):
    a = [0]*m; a[i] = 1; a[i+1] = -1; alpha.append(a)
a = [0]*m; a[m-1] = 2; alpha.append(a)
def Ti_on(i, f):  # T_i . f = (1-e^{a_i})^{-1}(s_i f - f)
    return sp.cancel((sact(simple[i], f) - f) / (1 - mono(alpha[i])))
def left_si(i, elt):
    out = {}
    for v, f in elt.items():
        g = sp.expand(sact(simple[i], f))
        out[v] = out.get(v, 0) + g
        h = sp.expand(g * (1 - mono(alpha[i])))
        siv = mul(simple[i], v)
        if L[siv] > L[v]: out[siv] = out.get(siv, 0) + h
        else: out[v] = out.get(v, 0) - h
    return out
# group elements as products of simple reflections via BFS
expr = {e: {e: sp.Integer(1)}}
frontier = [e]
while frontier:
    nf = []
    for w in frontier:
        for i in range(m):
            u = mul(simple[i], w)
            if u not in expr and L[u] == L[w] + 1:
                expr[u] = left_si(i, expr[w]); nf.append(u)
    frontier = nf
def psi(v, u): return sp.expand(expr[u].get(v, 0))
om = tuple([1]*m); w0 = tuple((i, -1) for i in range(m))
coset = {}
for w in W: coset.setdefault(act(w, om), []).append(w)
minrep = {mu: min(ws, key=lambda w: L[w]) for mu, ws in coset.items()}
maxrep = {mu: max(ws, key=lambda w: L[w]) for mu, ws in coset.items()}
import check as C
# reuse A from check.run internals: re-define quickly
def D(k): return {(a, a+d) for a, ka in enumerate(k) for d in range(ka)}
def v(k): return tuple(-1 if (m - i) in k else 1 for i in range(m))
def beta(xx):
    a, b = xx; d = b - a; ee = [0]*m
    if d == 0: ee[m-1] = 1
    else: ee[m-d-1] += 1; ee[m-d] -= 1
    return ee
def le(p, q): return p[0] <= q[0] and p[1] <= q[1]
def A(k, r):
    if not D(r) <= D(k): return sp.Integer(0)
    th = sorted(D(k) - D(r)); tot = sp.Integer(0)
    for g in itertools.product('eo', repeat=len(th)):
        G = dict(zip(th, g))
        if any(p[0] == p[1] and G[p] != 'e' for p in th): continue
        if not all(not (p != q and le(p, q)) or (G[p] == 'e' and G[q] == 'o') for p in th for q in th): continue
        ee = list(v(k))
        for p in th:
            if G[p] == 'o': ee = [ee[i] + beta(p)[i] for i in range(m)]
        tot += (-1)**len(th) * mono(ee)
    return tot
parts = [tuple(c) for r in range(m+1) for c in itertools.combinations(range(m, 0, -1), r)]
def z(k):
    if variant == "printed": return mul(maxrep[v(k)], w0)
    return minrep[v(k)]
sgnL = -1 if variant != "flipL" else 1
ok = bad = 0
for k in parts:
    for u in W:
        lhs = mono([sgnL*c for c in act(u, om)]) * psi(z(k), u)
        rhs = sum(A(k, r) * psi(z(r), u) for r in parts)
        if sp.expand(lhs - rhs) == 0: ok += 1
        else: bad += 1
print(variant, "m=%d" % m, "fixed-point identities ok", ok, "fail", bad)
