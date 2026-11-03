# Lusztig-data model of B(inf) in type A_n via PL transition maps (Lusztig's (a,b,c)->(b+c-p,p,a+b-p), p=min(a,c)).
# e~_j : move to a word starting with j, decrement n_1 (Kamnitzer 0505398 Prop 3.4 = BZ Prop 3.6).
import itertools, sys
from functools import lru_cache
from collections import deque

def setup(n):
    N=n*(n+1)//2
    def s(i,v):  # simple reflection on root vector (coords in simple roots), A_n Cartan
        v=list(v); c=[0]*n
        pair=sum(v[k]*(2 if k==i else (-1 if abs(k-i)==1 else 0)) for k in range(n))
        v[i]-=pair; return tuple(v)
    def roots(word):
        out=[]
        for k,i in enumerate(word):
            v=tuple(1 if t==i else 0 for t in range(n))
            for a in reversed(word[:k]): v=s(a,v)
            out.append(v)
        return out
    # reduced words of w0 via BFS on braid moves from a standard one
    w0=tuple(i for m in range(n,0,-1) for i in range(m))  # e.g. n=3: 0,1,2,0,1,0
    words={w0}; dq=deque([w0]); adj={}
    while dq:
        w=dq.popleft(); adj[w]=[]
        for k in range(N-1):
            a,b=w[k],w[k+1]
            if abs(a-b)>1:
                u=w[:k]+(b,a)+w[k+2:]; adj[w].append((u,('c',k)))
                if u not in words: words.add(u); dq.append(u)
        for k in range(N-2):
            a,b,c=w[k:k+3]
            if a==c and abs(a-b)==1:
                u=w[:k]+(b,a,b)+w[k+3:]; adj[w].append((u,('b',k)))
                if u not in words: words.add(u); dq.append(u)
    return N,words,adj,roots

def apply(move,d):
    t,k=move; d=list(d)
    if t=='c': d[k],d[k+1]=d[k+1],d[k]
    else:
        a,b,c=d[k:k+3]; p=min(a,c); d[k:k+3]=[b+c-p,p,a+b-p]
    return tuple(d)

class Model:
    def __init__(s,n):
        s.n=n; s.N,s.words,s.adj,s.roots=setup(n); s.paths={}
    def path(s,u,v):
        if (u,v) in s.paths: return s.paths[(u,v)]
        prev={u:None}; dq=deque([u])
        while dq:
            w=dq.popleft()
            if w==v: break
            for x,m in s.adj[w]:
                if x not in prev: prev[x]=(w,m); dq.append(x)
        p=[]; w=v
        while prev[w] is not None: w0,m=prev[w]; p.append(m); w=w0
        p.reverse(); s.paths[(u,v)]=p; return p
    def trans(s,d,u,v):
        for m in s.path(u,v): d=apply(m,d)
        return d
    def e(s,j,d,u):
        v=next(w for w in sorted(s.words) if w[0]==j)
        x=s.trans(d,u,v)
        if x[0]==0: return None
        return s.trans((x[0]-1,)+x[1:],v,u)
    def f(s,j,d,u):
        v=next(w for w in sorted(s.words) if w[0]==j)
        x=s.trans(d,u,v)
        return s.trans((x[0]+1,)+x[1:],v,u)
