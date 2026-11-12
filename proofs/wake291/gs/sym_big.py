# Sym shadow for alternating s up to large L, via a(nu) = #ribbon fillings of s with content nu (DP); compare to QSym (out_alt_blind / pred)
import sys,time
from functools import lru_cache
from shadow import partitions
from fastcap import rank
from predict import pred
from controls import alt
def a_count(s,nu):
    n=len(s)+1
    @lru_cache(None)
    def go(pos,last,rem):
        if pos==n: return 1
        tot=0
        for x,m in enumerate(rem):
            if m==0: continue
            if pos>0:
                b=s[pos-1]
                if b=='0' and not last<=x: continue
                if b=='1' and not last>x: continue
            r=list(rem); r[x]-=1; tot+=go(pos+1,x,tuple(r))
        return tot
    return go(0,-1,tuple(nu))
def sym_hilb(s):
    d=len(s)+1; cache={}; out=[]
    def a(nu):
        if nu not in cache: cache[nu]=a_count(s,nu)
        return cache[nu]
    for i in range(d+1):
        M=[[a(tuple(sorted(l+m,reverse=True))) for m in partitions(d-i)] for l in partitions(i)]
        out.append(rank(M))
    return out
for L in map(int,sys.argv[1:]):
    t=time.time(); s=alt(L); h=sym_hilb(s); print(L,s,'Sym',h,'=pred' if h==pred(L) else '!=pred','t',round(time.time()-t),flush=True)
