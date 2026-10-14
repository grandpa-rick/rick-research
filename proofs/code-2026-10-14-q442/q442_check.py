"""Sober re-implementation of Clio Q442 (c_alpha(0) = A^inf_alpha) from the PRINTED statement.
Laurent polys in x1..xn and t as dicts {(e1..en, tdeg): coeff}. No use of Lemma 2(ii) in engine W."""
import itertools, sys
from collections import defaultdict

def mul(a,b):
    r=defaultdict(int)
    for ka,va in a.items():
        for kb,vb in b.items():
            r[tuple(x+y for x,y in zip(ka,kb))]+=va*vb
    return {k:v for k,v in r.items() if v}
def add(a,b,s=1):
    r=defaultdict(int,a)
    for k,v in b.items(): r[k]+=s*v
    return {k:v for k,v in r.items() if v}

def edot(m,n):
    # e_m(x1..xn, 1/x1..1/xn) as Laurent poly, last coord = t degree 0
    if m<0 or m>2*n: return {}
    r=defaultdict(int)
    vars_=[(i,1) for i in range(n)]+[(i,-1) for i in range(n)]
    for S in itertools.combinations(range(2*n),m):
        e=[0]*(n+1)
        for s in S: e[vars_[s][0]]+=vars_[s][1]
        r[tuple(e)]+=1
    return dict(r)

def G(k,l,n,sign=-1,shiftM=0):
    """Warnaar G_t, eq (1), via row separability is NOT assumed: full sum over y in Z^k."""
    M=k+l+1+shiftM; N=2*(k+l+1)
    # range of y with possibly nonzero entries
    Y=[y for y in range(-(3*n+2*k)//max(N,1)-2,(3*n+2*k)//max(N,1)+3)]
    cache={}
    def ed(m):
        if m not in cache: cache[m]=edot(m,n)
        return cache[m]
    total={}
    for ys in itertools.product(Y,repeat=k):
        # matrix entries
        mat=[[None]*k for _ in range(k)]
        nz=True
        for i in range(1,k+1):
            y=ys[i-1]
            for j in range(1,k+1):
                ent=add(ed(n-i+j-N*y), ed(n+i+j-N*y), sign)
                tdeg=M*y*y-j*y
                ent={kk[:-1]+(kk[-1]+tdeg,):v for kk,v in ent.items()}
                mat[i-1][j-1]=ent
        det={}
        for p in itertools.permutations(range(k)):
            sg=1
            for a in range(k):
                for b in range(a+1,k):
                    if p[a]>p[b]: sg=-sg
            term={tuple([0]*(n+1)):sg}
            for i in range(k):
                term=mul(term,mat[i][p[i]])
                if not term: break
            det=add(det,term)
        total=add(total,det)
    # multiply by (x1..xn)^k
    return {tuple(list(kk[:-1][:])[q]+k for q in range(n))+(kk[-1],):v for kk,v in total.items()}

def coeff_t(Gt,d):
    return {kk[:-1]:v for kk,v in Gt.items() if kk[-1]==d}
def at_t1(Gt):
    r=defaultdict(int)
    for kk,v in Gt.items(): r[kk[:-1]]+=v
    return {k:v for k,v in r.items() if v}

def chains(k,n,w,endclass,bounded):
    """sum over vertical-strip chains (<=2k rows) of x^alpha, endpoint in class."""
    R=2*k
    states={tuple([0]*R):{tuple([0]*n):1}}
    for j in range(n):
        new=defaultdict(lambda: defaultdict(int))
        for lam,pol in states.items():
            for S in itertools.product((0,1),repeat=R):
                mu=tuple(a+b for a,b in zip(lam,S))
                if any(mu[i]<mu[i+1] for i in range(R-1)): continue
                if bounded and mu[0]-mu[R-1]>w: continue
                a=sum(S)
                for mon,c in pol.items():
                    m2=list(mon); m2[j]=a
                    new[mu][tuple(m2)]+=c
        states=new
    r=defaultdict(int)
    for lam,pol in states.items():
        if endclass(lam):
            for m,c in pol.items(): r[m]+=c
    return {k:v for k,v in r.items() if v}

def E(k): return lambda lam: all(lam[2*i]==lam[2*i+1] for i in range(k))
def Bcl(k,w): return lambda lam: lam[0]-lam[2*k-1]==w and all(lam[2*i+1]==lam[2*i+2] for i in range(k-1))

def efun(r,n):
    if r<0 or r>n: return {}
    out={}
    for S in itertools.combinations(range(n),r):
        e=[0]*n
        for s in S: e[s]=1
        out[tuple(e)]=1
    return out
def fpol(r,n):
    out={}
    for i in range(0,n+1): out=add(out,mul(efun(i,n),efun(i+r,n)))
    return out
def detf(k,n):
    mat=[[add(fpol(-i+j,n),fpol(i+j,n),-1) for j in range(1,k+1)] for i in range(1,k+1)]
    det={}
    for p in itertools.permutations(range(k)):
        sg=1
        for a in range(k):
            for b in range(a+1,k):
                if p[a]>p[b]: sg=-sg
        term={tuple([0]*n):sg}
        for i in range(k): term=mul(term,mat[i][p[i]])
        det=add(det,term)
    return det
