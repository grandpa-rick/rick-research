"""Independent KL computation: R-polynomial recursion + inversion on interval [x,z]. Written from scratch."""
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)

def length(w):
    n=len(w); return sum(1 for i in range(n) for j in range(i+1,n) if w[i]>w[j])

def leq(u,v):
    """Bruhat u<=v via rank criterion: for all i, sorted prefix of u <= sorted prefix of v (tableau criterion)."""
    n=len(u)
    for i in range(1,n):
        a=sorted(u[:i]); b=sorted(v[:i])
        for p,q in zip(a,b):
            if p>q: return False
    return True

# polynomials: lists of ints, index = degree
def padd(a,b):
    if len(a)<len(b): a,b=b,a
    r=list(a)
    for i,c in enumerate(b): r[i]+=c
    while r and r[-1]==0: r.pop()
    return r
def pmul(a,b):
    if not a or not b: return []
    r=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        if c:
            for j,d in enumerate(b): r[i+j]+=c*d
    while r and r[-1]==0: r.pop()
    return r

def rswap(w,i):  # w*s_i (swap positions i,i+1), 0-indexed i
    l=list(w); l[i],l[i+1]=l[i+1],l[i]; return tuple(l)
def lswap(w,i):  # s_i*w (swap values i+1,i+2 in 1-indexed), i 0-indexed
    a,b=i+1,i+2
    return tuple(b if c==a else a if c==b else c for c in w)
def rdes(w): return [i for i in range(len(w)-1) if w[i]>w[i+1]]
def ldes(w):
    inv={c:k for k,c in enumerate(w)}
    return [i for i in range(len(w)-1) if inv[i+1]>inv[i+2]]

RMEMO={}
def R(u,v,lu=None,lv=None):
    if lu is None: lu=length(u)
    if lv is None: lv=length(v)
    # strip common descents (right and left) -> no branching
    n=len(u)
    while True:
        if u==v: return [1]
        if lu>=lv: return []
        hit=-1
        for i in range(n-1):
            if v[i]>v[i+1] and u[i]>u[i+1]: hit=i; break
        if hit>=0:
            u=rswap(u,hit); v=rswap(v,hit); lu-=1; lv-=1; continue
        iu=[0]*(n+1); iv=[0]*(n+1)
        for k in range(n): iu[u[k]]=k; iv[v[k]]=k
        for a in range(1,n):
            if iv[a]>iv[a+1] and iu[a]>iu[a+1]: hit=a-1; break
        if hit>=0:
            u=lswap(u,hit); v=lswap(v,hit); lu-=1; lv-=1; continue
        break
    key=(u,v)
    if key in RMEMO: return RMEMO[key]
    if not leq(u,v):
        RMEMO[key]=[]; return []
    i=rdes(v)[0]  # u*s_i > u here
    vs=rswap(v,i); us=rswap(u,i)
    res=padd(pmul([-1,1],R(u,vs,lu,lv-1)), pmul([0,1],R(us,vs,lu+1,lv-1)))
    RMEMO[key]=res
    return res

def lower_covers(w):
    n=len(w); out=[]
    for i in range(n):
        for j in range(i+1,n):
            if w[i]>w[j]:
                ok=True
                for k in range(i+1,j):
                    if w[j]<w[k]<w[i]: ok=False; break
                if ok:
                    l=list(w); l[i],l[j]=l[j],l[i]; out.append(tuple(l))
    return out

def interval(x,z):
    """elements of [x,z] by downward cover BFS from z, keeping those >= x."""
    if not leq(x,z): return []
    seen={z}; frontier=[z]
    while frontier:
        nf=[]
        for w in frontier:
            for c in lower_covers(w):
                if c not in seen and leq(x,c):
                    seen.add(c); nf.append(c)
        frontier=nf
    return list(seen)

def kl_interval(x,z,verbose=False,ckpt=None,tlimit=None):
    """return dict y->P_{y,z} for y in [x,z]"""
    import time
    t0=time.time()
    I=interval(x,z)
    L={w:length(w) for w in I}
    I.sort(key=lambda w:-L[w])
    idx={w:k for k,w in enumerate(I)}
    if verbose: print('interval size',len(I),'time',time.time()-t0,flush=True)
    # up-sets as bitsets
    up=[0]*len(I)
    for k,w in enumerate(I):
        b=1<<k
        for c in lower_covers(w):
            pass
    # build upper covers: for each w, its lower covers in I get w as upper cover
    upc=[[] for _ in I]
    for k,w in enumerate(I):
        for c in lower_covers(w):
            if c in idx: upc[idx[c]].append(k)
    for k in range(len(I)):
        b=1<<k
        for c in upc[k]: b|=up[c]
        up[k]=b
    npairs=sum(bin(b).count('1') for b in up)
    if verbose: print('comparable pairs',npairs,'time',time.time()-t0,flush=True)
    lz=L[z]
    P={}
    import os,pickle
    if ckpt and os.path.exists(ckpt):
        P,mem=pickle.load(open(ckpt,'rb')); RMEMO.update(mem)
        if verbose: print('resumed',len(P),flush=True)
    for k,y in enumerate(I):
        if y in P: continue
        if tlimit and time.time()-t0>tlimit:
            pickle.dump((P,RMEMO),open(ckpt,'wb')); print('checkpoint',len(P),flush=True); return None
        if y==z: P[y]=[1]; continue
        ly=L[y]
        rhs=[]
        b=up[k] & ~(1<<k)
        while b:
            low=b & -b; j=low.bit_length()-1; b^=low
            t=I[j]
            r=R(y,t,ly,L[t])
            if r: rhs=padd(rhs,pmul(r,P[t]))
        d=(lz-ly-1)//2
        p=[-(rhs[i] if i<len(rhs) else 0) for i in range(d+1)]
        while p and p[-1]==0: p.pop()
        # consistency: q^{L}p(1/q) - p == rhs
        Lg=lz-ly
        chk=[0]*(Lg+1)
        for i,c in enumerate(p): chk[Lg-i]+=c; chk[i]-=c
        while chk and chk[-1]==0: chk.pop()
        assert chk==rhs, (y,p,rhs,chk)
        P[y]=p
        if verbose and k%1000==0: print(k,len(RMEMO),time.time()-t0,flush=True)
    return P
