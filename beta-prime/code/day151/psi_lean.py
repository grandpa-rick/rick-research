#!/usr/bin/env python3
"""Lean version: only the LEADING SYMBOL is needed for psi.
Since wt(E1^a E2^b E3^c) = a+2b+3c = total u-degree, and deg_u H_n <= n (Day149 Thm 2),
the wt=n part of H_n is exactly the degree-n homogeneous component of H_n in u.
So symmetrize only that small piece."""
import math, sys, pickle
from collections import defaultdict
NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 36
def mul(A,B):
    R=defaultdict(int)
    for m1,c1 in A.items():
        for m2,c2 in B.items(): R[(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])]+=c1*c2
    return {m:c for m,c in R.items() if c}
def add(A,B):
    R=defaultdict(int)
    for X in (A,B):
        for m,c in X.items(): R[m]+=c
    return {m:c for m,c in R.items() if c}
def scal(k,A): return {m:k*c for m,c in A.items()} if k else {}
ONE={(0,0,0):1}
V=mul(mul({(1,0,0):1,(0,1,0):-1},{(1,0,0):1,(0,0,1):-1}),{(0,1,0):1,(0,0,1):-1})
e1m={(1,0,0):1,(0,1,0):1,(0,0,1):1}; e2m={(1,1,0):1,(1,0,1):1,(0,1,1):1}; e3m={(1,1,1):1}
D=NMAX*2+8
st=[[0]*(D+1) for _ in range(D+1)]; st[0][0]=1
for n in range(1,D+1):
    for k in range(1,n+1): st[n][k]=st[n-1][k-1]+(n-1)*st[n-1][k]
def Tplus(A):
    R=defaultdict(int)
    for (i,j,k),c in A.items():
        for a in range(i+1):
            if not st[i][a]: continue
            ca=c*st[i][a]
            for b in range(j+1):
                if not st[j][b]: continue
                cb=ca*st[j][b]
                for d in range(k+1):
                    if st[k][d]: R[(a,b,d)]+=cb*st[k][d]
    return {m:c for m,c in R.items() if c}
binom=[[math.comb(n,k) for k in range(D+1)] for n in range(D+1)]
def tau(A):
    R=defaultdict(int)
    for (i,j,k),c in A.items():
        for a in range(i+1):
            ca=c*binom[i][a]
            for b in range(j+1):
                cb=ca*binom[j][b]
                for d in range(k+1): R[(a,b,d)]+=cb*binom[k][d]
    return {m:c for m,c in R.items() if c}
def divlin(A,p,q):
    byd=defaultdict(dict)
    for m,c in A.items():
        rest=list(m); dp=rest[p]; rest[p]=0; byd[dp][tuple(rest)]=c
    dmax=max(byd) if byd else 0
    Qd={}; out=defaultdict(int); rem={}
    for d in range(dmax,-1,-1):
        cur=add(dict(byd.get(d,{})),Qd)
        if d==0: rem=cur; break
        for m,c in cur.items():
            mm=list(m); mm[p]=d-1; out[tuple(mm)]+=c
        Qd={}
        for m,c in cur.items():
            mm=list(m); mm[q]+=1; Qd[tuple(mm)]=c
    assert not {m:c for m,c in rem.items() if c}
    return {m:c for m,c in out.items() if c}
def divV(A): return divlin(divlin(divlin(A,0,1),0,2),1,2)
A=[]; cur=dict(V)
for n in range(NMAX+1):
    A.append(Tplus(cur)); cur=mul(cur,e2m)
Hu=[]
for n in range(NMAX+1):
    acc=tau(A[n])
    for k in range(1,n+1):
        acc=add(acc,scal(-(math.factorial(n)//math.factorial(k)),mul(A[k],Hu[n-k])))
    fn=math.factorial(n)
    assert all(c%fn==0 for c in acc.values()),n
    Hu.append(divV({m:c//fn for m,c in acc.items()}))
    assert max(sum(m) for m in Hu[-1]) <= n, ("deg_u H_n > n",n)
print("H built to T^%d, deg_u H_n <= n verified"%NMAX); sys.stdout.flush()
# leading symbol
mono_cache={}
def Emon(a,b,c):
    if (a,b,c) in mono_cache: return mono_cache[(a,b,c)]
    r={(0,0,0):1}
    for _ in range(a): r=mul(r,e1m)
    for _ in range(b): r=mul(r,e2m)
    for _ in range(c): r=mul(r,e3m)
    mono_cache[(a,b,c)]=r; return r
def toE(P):
    P=dict(P); out=defaultdict(int)
    while P:
        m=max(P); c=P[m]
        assert m[0]>=m[1]>=m[2],("bad lead",m)
        key=(m[0]-m[1],m[1]-m[2],m[2]); out[key]+=c
        P=add(P,scal(-c,Emon(*key)))
    return {m:c for m,c in out.items() if c}
W=[]
for n in range(NMAX+1):
    top={m:c for m,c in Hu[n].items() if sum(m)==n}
    assert all(c%(n+1)==0 for c in top.values()),n
    W.append(toE({m:c//(n+1) for m,c in top.items()}))
assert W[0]==ONE
for n in range(1,NMAX+1):
    coef=defaultdict(int)
    for (a,b,c),co in W[n].items():
        if c: continue
        for i in range(a+1): coef[(a-i+b,i+b)]+=co*math.comb(a,i)
    got=[coef.get((n-k,k),0) for k in range(n+1)]
    want=[math.comb(n+1,k)*math.comb(n+1,k+1)//(n+1) for k in range(n+1)]
    assert got==want,(n,got,want)
print("Narayana at E3=0 verified n=1..%d"%NMAX); sys.stdout.flush()
M=NMAX
def compose(f,g):
    res=[{} for _ in range(M+1)]; gp=[{} for _ in range(M+1)]; gp[0]=dict(ONE)
    for k in range(M+1):
        if k>0:
            new=[{} for _ in range(M+1)]
            for i in range(M+1):
                if not gp[i]: continue
                for j in range(1,M+1-i):
                    if g[j]: new[i+j]=add(new[i+j],mul(gp[i],g[j]))
            gp=new
        if f[k]:
            for i in range(M+1):
                if gp[i]: res[i]=add(res[i],mul(f[k],gp[i]))
    return res
calW=[W[n] for n in range(M+1)]
Yc=[{}]+[W[n] for n in range(M)]
Tc=[{} for _ in range(M+1)]; Tc[1]=dict(ONE)
for m in range(2,M+1):
    c=compose(Yc,Tc)
    if c[m]: Tc[m]=add(Tc[m],scal(-1,c[m]))
c=compose(Yc,Tc)
for k in range(M+1): assert c[k]==(ONE if k==1 else {}),k
psi=compose(calW,Tc)
chk=[{} for _ in range(M+1)]
for i in range(M+1):
    for j in range(M+1-i):
        if psi[i] and Tc[j]: chk[i+j]=add(chk[i+j],mul(psi[i],Tc[j]))
for k in range(M+1): assert chk[k]==(ONE if k==1 else {}),("psi*T!=Y",k)
print("reversion + psi*T=Y verified to Y^%d"%M)
pickle.dump({'W':W,'psi':psi},open('/home/agent/projects/beta-prime/code/day151/psi_lean%d.pkl'%NMAX,'wb'))
seq=[psi[3*n].get((0,0,n),0) for n in range(M//3+1)]
print("[W^n] psi|E1=E2=0 :",seq)
print("Catalan C_{n+1}   :",[math.comb(2*n+2,n+1)//(n+2) for n in range(len(seq))])
neg=[(k,m,c) for k in range(M+1) for m,c in psi[k].items() if c<0]
print("negative coefficients:",neg if neg else "NONE (E-positive to Y^%d)"%M)
bad=[(k,m) for k in range(3,M+1) for m in psi[k] if m[2]==0]
print("E3-divisible from Y^3 on:","YES" if not bad else bad)
print("#monomials per order:",[len(psi[k]) for k in range(M+1)])
