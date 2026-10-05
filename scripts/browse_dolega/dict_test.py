"""Separator tests: Rick's Lead_{lam,(n)} (Thm G) vs Dolega 1707.02656 Macdonald cumulants.
(a) single-row cumulants kappa(H_(l1),...,H_(lr)) and coefficient extractions;
(b) column cumulants: H~_{lam'} expanded in products of g_k = H~_{1^k}(x;t), coefficient of g_n."""
import sys; sys.path.insert(0,'/home/agent/projects/scripts/day216b')
import sympy as sp, itertools
from symf import *
from math import factorial
def setparts(S):
    S=list(S)
    if not S: yield []; return
    a=S[0]
    for p in setparts(S[1:]):
        for i in range(len(p)): yield p[:i]+[[a]+p[i]]+p[i+1:]
        yield [[a]]+p
def oplus(parts_list):  # entrywise sum of partitions
    L=max(len(p) for p in parts_list); return tuple(sum(p[i] if i<len(p) else 0 for p in parts_list) for i in range(L))
def cumulant(lams):
    r=len(lams); out={}
    for pi in setparts(range(r)):
        k=len(pi); c=(-1)**(k-1)*factorial(k-1)
        term=prod([Htilde(oplus([lams[b] for b in B])) for B in pi])
        out=add(out,term,c)
    return {kk:sp.factor(sp.together(v)) for kk,v in out.items()}
def conn_graph_sum(lam,x):
    l=len(lam); pairs=[(i,j) for i in range(l) for j in range(i+1,l)]; tot=0
    for mask in range(1<<len(pairs)):
        E=[pairs[k] for k in range(len(pairs)) if mask>>k&1]
        par=list(range(l))
        def f(a):
            while par[a]!=a: a=par[a]
            return a
        for i,j in E: par[f(i)]=f(j)
        if len({f(i) for i in range(l)})==1: tot+=sp.prod([x**(lam[i]*lam[j])-1 for i,j in E])
    return tot
def RickLead(lam,x=t):
    n=sum(lam); return sp.factor((1-x**n)/sp.prod([1-x**k for k in lam])*conn_graph_sum(lam,x))
def lowest(expr,var=q):
    e=sp.factor(expr); u=sp.Symbol('u'); ex=sp.expand(sp.together(e).subs(var,u+1))
    num,den=sp.fraction(sp.together(ex)); num=sp.Poly(sp.expand(num),u)
    v=min(m[0] for m in num.monoms()); return v, sp.factor(num.coeff_monomial(u**v)/den.subs(u,0))
if __name__=='__main__':
    cases=[(1,1),(2,1),(1,1,1),(2,2),(3,1),(2,1,1)]
    print("== Rick Lead (Thm G) ==")
    for lam in cases: print(lam, RickLead(lam))
    print("== (a) Dolega single-row cumulants, q-lowest coefficients in several bases ==")
    for lam in cases:
        n=sum(lam); K=cumulant([(k,) for k in lam])
        eb={('e',m):prod([e(i) for i in m]) for m in parts(n)}
        ce=to_basis(K,eb)
        sb={('s',m):schur(m) for m in parts(n)}; cs=to_basis(K,sb)
        print(lam,'[e_n]:',lowest(ce[('e',(n,))]),'[s_n]:',lowest(cs[('s',(n,))]),'[s_1^n]:',lowest(cs[('s',(1,)*n)]))
    print("== (b) column cumulants: H~_{lam'} in g-basis, g_k=H~_{1^k}(x;t) ==")
    for lam in cases:
        n=sum(lam); lp=transpose(tuple(sorted(lam,reverse=True)))
        H=Htilde(lp)
        gb={m:prod([Htilde((1,)*i) for i in m]) for m in parts(n)}
        d=to_basis(H,gb)
        v,c=lowest(d[(n,)])
        R=RickLead(lam)
        print(lam,'val',v,'D-lead',c,' Rick/D =',sp.factor(R/c))
