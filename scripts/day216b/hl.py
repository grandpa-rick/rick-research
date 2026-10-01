import sympy as sp, itertools, sys
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import Ek, e, parts, transpose, nstat
from functools import lru_cache
def HLP(lam, xs, t):
    """Macdonald III (2.2): P_lam = sum_{w in S_n/S_n^lam} w(x^lam prod_{lam_i>lam_j} (x_i-t x_j)/(x_i-x_j))"""
    n=len(xs); lam=tuple(lam)+(0,)*(n-len(lam))
    if len(lam)>n: return sp.Integer(0)
    tot=0; seen=set()
    V=sp.prod([xs[i]-xs[j] for i in range(n) for j in range(i+1,n)])
    for w in itertools.permutations(range(n)):
        key=tuple(lam[w.index(i)] for i in range(n))  # exponent placed at variable i
        if key in seen: continue
        seen.add(key)
        y=[xs[w[i]] for i in range(n)]
        term=sp.prod([y[i]**lam[i] for i in range(n)])*sp.prod([(y[i]-t*y[j]) for i in range(n) for j in range(i+1,n) if lam[i]>lam[j]]) \
            *sp.prod([ (y[i]-y[j]) for i in range(n) for j in range(i+1,n) if lam[i]==lam[j]])
        # multiply by V/(prod over all i<j (y_i-y_j)) sign: prod_{i<j}(y_i-y_j) = sgn(w) V
        sgn=sp.combinatorics.Permutation(list(w)).signature()
        tot+=sgn*term
    q,r=sp.div(sp.Poly(sp.expand(tot),*xs),sp.Poly(V,*xs)); assert r.is_zero
    return q.as_expr()
def expand_in_P(G, ys, xs, t, deg):
    """G polynomial in ys (symmetric) with coeffs in xs; expand in P_rho(ys;t). returns dict rho->coef"""
    out={}; G=sp.expand(G); k=len(ys)
    for d in range(deg,-1,-1):
        pass
    P=sp.Poly(G,*ys); 
    res={}
    while not P.is_zero:
        mon,c=max(P.terms(),key=lambda mc:(sum(mc[0]),mc[0]))
        rho=tuple(a for a in mon if a>0)
        res[rho]=res.get(rho,0)+c.as_expr() if hasattr(c,'as_expr') else c
        P=P-sp.Poly(sp.expand(c*HLP(rho,ys,t)),*ys)
    return res
