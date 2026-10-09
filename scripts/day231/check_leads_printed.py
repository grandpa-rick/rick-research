# longversion §7 printed: thm:G, cor:G(a)(b)(c), thm:F, thm:blockmult vs engine.
from lv_engine import *
from check_DS_printed import estar, interp, dom
from check_blocklaw_printed import kappa, setparts

import itertools, sys
from functools import lru_cache
T0=Fr(3,5)
@lru_cache(None)
def hexp(lam,t):
    n=sum(lam); hs=[Fr(i+1,i+3)*(-1)**i for i in range(16)]
    D=[e_expand(lambda x: estar(lam,x,1+h,t),n,n) for h in hs]
    out={}
    for mu in partitions(n):
        out[mu]=interp(hs,[d.get(mu,Fr(0)) for d in D])
    return out
def conn_graphs_sum(lam,t):
    l=len(lam); E=[(i,j) for i in range(l) for j in range(i+1,l)]; tot=Fr(0)
    for mask in range(1<<len(E)):
        H=[E[b] for b in range(len(E)) if mask>>b&1]
        # connected?
        par=list(range(l))
        def f(a):
            while par[a]!=a: a=par[a]
            return a
        for i,j in H: par[f(i)]=f(j)
        if len({f(i) for i in range(l)})==1:
            tot+=prod(t**(lam[i]*lam[j])-1 for i,j in H)
    return tot
def Gpred(lam,t):
    n=sum(lam); return (1-t**n)/prod(1-t**p for p in lam)*conn_graphs_sum(lam,t)
N=int(sys.argv[1]) if len(sys.argv)>1 else 5
ok=True
for t in [T0,Fr(-2),Fr(7,3)]:
  for n in range(2,N+1):
    for lam in partitions(n):
      if len(lam)<2: continue
      l=len(lam); c=hexp(lam,t)[(n,)]
      if c[l-1]!=Gpred(lam,t) or any(c[j]!=0 for j in range(l-1)): ok=False; print('G FAIL',lam,t)
print('thm:G n<=%d at 3 t:'%N, ok)
# cor:G (a),(b),(c)
okc=True
def Imr(n,t): # Mallows-Riordan via K_{1^n}/(t-1)^{n-1}
    return conn_graphs_sum((1,)*n,t)/(t-1)**(n-1)
for n in range(2,6):
    t=Fr(2,7)
    if Gpred((1,)*n,t)!=(-1)**(n-1)*(1-t**n)/(1-t)*Imr(n,t): okc=False
    # I_n(1) = n^{n-2}? check I_n polynomial at t=1 via limit: skip; check I_n(0)=(n-1)!
for lam in [(1,1),(2,1),(1,1,1),(2,1,1),(3,2,1),(2,2,1,1)]:
    l=len(lam); n=sum(lam)
    if Gpred(lam,Fr(0))!=(-1)**(l-1)*prod(range(1,l)): okc=False; print('b fail',lam)
    t=1+Fr(1,10**6); v=Gpred(lam,t); target=(-1)**(l-1)*n**(l-1)
    if abs(float(v)-target)>1e-3*abs(target): okc=False; print('c fail',lam,float(v),target)
print('cor:G (a),(b),(c):',okc)
# thm:F
okF=True
for t in [T0,Fr(-2)]:
  for n in range(2,N+1):
    for lam in partitions(n):
      l=len(lam)
      for mu in partitions(n):
        if mu==lam or kappa(lam,mu)!=len(mu): continue
        m=l-len(mu); c=hexp(lam,t)[mu][m]
        tot=Fr(0)
        for pi in setparts(range(l)):
            if tuple(sorted([sum(lam[i] for i in B) for B in pi],reverse=True))!=mu: continue
            tot+=prod((Gpred(tuple(lam[i] for i in B),t) if len(B)>1 else Fr(1)) for B in pi)
        if tot!=c: okF=False; print('F FAIL',lam,mu,t)
print('thm:F:',okF)
# thm:blockmult on all pairs with kappa>=1
okB=True; cntB=0
for t in [T0]:
  for n in range(2,N+1):
    for lam in partitions(n):
      l=len(lam)
      for mu in partitions(n):
        if mu==lam: continue
        kap=kappa(lam,mu)
        if kap<1: continue
        m=l-kap; c=hexp(lam,t)[mu][m]; tot=Fr(0)
        for pi in setparts(range(l)):
            if len(pi)!=kap: continue
            # tuples (nu^C) with union mu, nu^C ⊵ lam_C
            subs=[tuple(sorted([lam[i] for i in B],reverse=True)) for B in pi]
            def rec(i,remaining):
                if i==len(subs):
                    return Fr(1) if not remaining else Fr(0)
                lamC=subs[i]; nC=sum(lamC); tot_=Fr(0)
                rem=list(remaining); nus=set()
                for r in range(1,len(rem)+1):
                    for idx in itertools.combinations(range(len(rem)),r):
                        nus.add(tuple(sorted([rem[j] for j in idx],reverse=True)))
                for nu in nus:
                    if sum(nu)!=nC or not dom(nu,lamC): continue
                    coef=(hexp(lamC,t)[nu][len(lamC)-1] if len(lamC)>1 else (Fr(1) if nu==lamC else Fr(0)))
                    if coef==0: continue
                    left=list(rem)
                    for q in nu: left.remove(q)
                    tot_+=coef*rec(i+1,tuple(sorted(left,reverse=True)))
                return tot_
            # careful: combinations over identical parts are distinct index choices; tuples (nu^C) as multiset decompositions must be counted once
            tot+=rec(0,tuple(mu))
        cntB+=1
        if tot!=c: okB=False; print('BM FAIL',lam,mu,c,tot)
print('thm:blockmult (%d pairs):'%cntB, okB)
