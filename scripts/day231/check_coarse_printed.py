# thm:coarse history formula (printed definition) + thm:W closed form vs engine Lead, coarsening pairs n<=5.
from lv_engine import *
from check_DS_printed import estar, interp, dom
from check_blocklaw_printed import kappa, br
import itertools
def W(k,J,t): return (-1)**len(J)*br(k+sum(J),t)/br(k,t)*prod(br(k,t**j) for j in J)
def histories(lam,t):
    # returns dict: sorted final sizes -> (sum of weights over tight histories with given total order)
    out={}
    def rec(i,blocks,order,w):
        if i<0:
            key=(tuple(sorted(blocks,reverse=True)),order); out[key]=out.get(key,0)+w; return
        k=lam[i]; nb=len(blocks)
        for r in range(nb+1):
            for S in itertools.combinations(range(nb),r):
                J=[blocks[j] for j in S]
                newb=[blocks[j] for j in range(nb) if j not in S]+[k+sum(J)]
                rec(i-1,newb,order+r,w*(W(k,J,t) if r>0 else 1))
    rec(len(lam)-1,[],0,Fr(1))
    return out
ok=True; cnt=0
for t in [Fr(3,5),Fr(-2),Fr(0)]:
  for n in range(2,6):
    for lam in partitions(n):
      H=histories(lam,t)
      hsP=[Fr(i+1,i+3)*(-1)**i for i in range(14)]
      D=[e_expand(lambda x: estar(lam,x,1+h,t),n,n) for h in hsP]
      for mu in partitions(n):
        if mu==lam or kappa(lam,mu)!=len(mu): continue
        m=len(lam)-len(mu); cc=interp(hsP,[d.get(mu,Fr(0)) for d in D])
        pred=H.get((mu,m),Fr(0)); cnt+=1
        if cc[m]!=pred or any(cc[j]!=0 for j in range(m)): ok=False; print('COARSE FAIL',lam,mu,t,cc[m],pred)
        if t==0:
            nH=pred*(-1)**m
            if nH<1 or nH.denominator!=1: ok=False; print('#H fail')
print('thm:coarse history formula + W (%d pairs, t=3/5,-2,0):'%cnt, ok)
print('example Lead_(111),(3) at t:', [str(histories((1,1,1),tt).get(((3,),2))) for tt in [Fr(0),Fr(-2),Fr(1,2)]])
