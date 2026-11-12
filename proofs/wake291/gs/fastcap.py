"""Fast engine for c^s_{u,v} = coeff of F_s in F_u F_v (binary-string convention of cap_rank.py:
bit '1' at position i <=> descent at i). DP over shuffles instead of enumerating C(n,a) shuffles.
Ranks: exact over Q via modular elimination at two large primes (max taken) -- lower bound, generic-exact."""
import itertools, sys
from functools import lru_cache
from cap_rank_import import perm_with_des
EPS=None
def coeff_dp(u,v,s):
    if u is EPS: return int(v==s)
    if v is EPS: return int(u==s)
    a,b=len(u)+1,len(v)+1
    if a+b!=len(s)+1: return 0
    sig=perm_with_des(u); tau=[x+a for x in perm_with_des(v)]
    # f[i][j][w]: ways having placed i of sig, j of tau, last from w (0 sig,1 tau)
    f={}
    f[(1,0,0)]=1; f[(0,1,1)]=1
    for t in range(1,a+b):
        nf={}
        for (i,j,w),c in f.items():
            last = sig[i-1] if w==0 else tau[j-1]
            bit = s[t-1]
            if i<a:
                x=sig[i]; ok = (last>x)==(bit=='1')
                if ok: nf[(i+1,j,0)]=nf.get((i+1,j,0),0)+c
            if j<b:
                x=tau[j]; ok = (last>x)==(bit=='1')
                if ok: nf[(i,j+1,1)]=nf.get((i,j+1,1),0)+c
        f=nf
    return f.get((a,b,0),0)+f.get((a,b,1),0)
def rank_mod(M,p):
    M=[[x%p for x in row] for row in M]
    r=0; rows=len(M); cols=len(M[0]) if rows else 0
    for c in range(cols):
        piv=None
        for k in range(r,rows):
            if M[k][c]: piv=k;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],p-2,p)
        M[r]=[x*inv%p for x in M[r]]
        for k in range(rows):
            if k!=r and M[k][c]:
                f=M[k][c]; Mr=M[r]
                M[k]=[(x-f*y)%p for x,y in zip(M[k],Mr)]
        r+=1
        if r==rows: break
    return r
def rank(M):
    if not M or not M[0]: return 0
    return max(rank_mod(M,2147483647),rank_mod(M,1000000007))
def subseqs(s,L): return sorted({''.join(c) for c in itertools.combinations(s,L)})
def basis(s,i): return [EPS] if i==0 else subseqs(s,i-1)
def ranks(s,degs=None):
    d=len(s)+1; out=[]
    for i in (range(d+1) if degs is None else degs):
        U=basis(s,i); V=basis(s,d-i)
        M=[[coeff_dp(x,y,s) for y in V] for x in U]
        out.append(rank(M))
    return out
