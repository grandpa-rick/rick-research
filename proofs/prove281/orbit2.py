"""Two-sided simultaneous star orbit of (y,z): left stars (Lemma S) and right stars (Lemma S on inverses,
P_{x,w}=P_{x^-1,w^-1}). Right stars are applied only when y,z share Q (always true here) and act on positions."""
import sys; sys.path.insert(0,'.')
from common import *
from orbit import star, status
from collections import deque
def invp(w):
    r=[0]*len(w)
    for k,a in enumerate(w): r[a-1]=k+1
    return r
def rstar(i,w):
    v=star(i,invp(w)); return None if v is None else invp(v)
def search2(y,z,cap=500000,sides='LR'):
    n=len(y); start=(tuple(y),tuple(z)); par={start:None}; dq=deque([start])
    while dq:
        a,b=dq.popleft()
        st,g=status(list(a),list(b))
        if st!='open':
            p=[]; cur=(a,b)
            while par[cur] is not None: cur,mv=par[cur]; p.append(mv)
            return st,p[::-1],(a,b),len(par)
        for side,f in [t for t in (('L',star),('R',rstar)) if t[0] in sides]:
            for i in range(1,n-1):
                a2=f(i,list(a))
                if a2 is None: continue
                b2=f(i,list(b))
                if b2 is None: continue
                nx=(tuple(a2),tuple(b2))
                if nx not in par:
                    par[nx]=((a,b),(side,i)); dq.append(nx)
                    if len(par)>cap: return 'cap',None,None,len(par)
    return 'exhausted',None,None,len(par)

def search12(y,z):
    r=search2(y,z,cap=300000,sides='L')
    if r[0] in ('cap','exhausted'): r=search2(y,z,cap=2000000)
    return r
