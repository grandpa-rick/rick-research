"""Tableau-level decider: mu(T,T') (same shape) via random cells + Young-layer factorisation + recursion on same-cell factors."""
import sys,json,random
sys.path.insert(0,'.')
from ydec import endpoint, std, ln
from cfg import rsk_inv
from rskmod import rsk
from count_int import syt
random.seed(282)
memo={}
_syt={}
def cells_of(lam):
    if lam not in _syt:
        S=syt(lam); random.shuffle(S); _syt[lam]=S
    return _syt[lam]
def key(T): return tuple(map(tuple,T))
def all_factors(y,z):
    n=len(y); out=[]
    py={v:i for i,v in enumerate(y)}; pz={v:i for i,v in enumerate(z)}
    for k in range(1,n):
        if set(y[:k])==set(z[:k]): out.append(('R',k,(std(y[:k]),std(y[k:])),(std(z[:k]),std(z[k:]))))
        if {py[v] for v in range(1,k+1)}=={pz[v] for v in range(1,k+1)}:
            out.append(('L',k,([v for v in y if v<=k],[v-k for v in y if v>k]),([v for v in z if v<=k],[v-k for v in z if v>k])))
    return out
def dec_perm(a,a2,budget,depth):
    if a==a2: return None
    e=endpoint(a,a2)
    if e is not None: return (e,[('end',len(a))])
    Pa,Qa=rsk(a); Pb,Qb=rsk(a2)
    if Qa==Qb and len(Pa)==len(Pb) and [len(r) for r in Pa]==[len(r) for r in Pb]:
        return dec_tab([list(r) for r in Pa],[list(r) for r in Pb],budget,depth+1)
    return None
def dec_tab(Ty,Tz,budget=400,depth=0):
    k0=(key(Ty),key(Tz))
    if k0 in memo: return memo[k0]
    memo[k0]=None
    if depth>6: return None
    lam=tuple(len(r) for r in Ty)
    for Q in cells_of(lam)[:budget]:
        Q=[list(r) for r in Q]; y=rsk_inv(Ty,Q); z=rsk_inv(Tz,Q)
        e=endpoint(y,z)
        if e is not None:
            memo[k0]=(e,[('end',len(y),key(Q))]); return memo[k0]
        for side,k,(a,b),(a2,b2) in all_factors(y,z):
            if a!=a2 and b!=b2:
                memo[k0]=(0,[('both-differ',side,k,key(Q))]); return memo[k0]
            sub=(b,b2) if a==a2 else (a,a2)
            r=dec_perm(sub[0],sub[1],budget//2,depth)
            if r is not None:
                memo[k0]=(r[0],[(side,k,key(Q))]+r[1]); return memo[k0]
    return None
if __name__=='__main__':
    S=json.load(open('../wake282/sieve16.json'))
    for r in S:
        for e in r['elems']:
            if e['kind']=='ii' and e['muyz'] is None:
                Py=[list(R) for R in rsk(e['y'])[0]]
                res=dec_tab(Py,r['Pz'])
                print(r['lam'],r['verdict'],'->',None if res is None else (res[0],[t[:3] for t in res[1]]),flush=True)
