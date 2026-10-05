from fractions import Fraction as Q
import json
d=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
b=[0]+[int(x) for x in d['b']]
N=15
F=[Q(0)]+[Q(b[k]) for k in range(1,N+1)]
def mul(A,B,n=N):
    R=[Q(0)]*(n+1)
    for i,x in enumerate(A):
        if x==0: continue
        for j,y in enumerate(B):
            if i+j>n: break
            R[i+j]+=x*y
    return R
pw=[[Q(1)]+[Q(0)]*N]
for _ in range(6): pw.append(mul(pw[-1],F))
terms=[(i,j) for j in range(6) for i in range(2)]
rows=[]
for n in range(0,N+1):
    rows.append([pw[j][n-i] if 0<=n-i<=N else Q(0) for (i,j) in terms])
# nullspace
m=len(rows); n=len(terms); A=[r[:] for r in rows]; piv=[]; r=0
for c in range(n):
    p=None
    for i in range(r,m):
        if A[i][c]!=0: p=i;break
    if p is None: continue
    A[r],A[p]=A[p],A[r]; inv=Q(1)/A[r][c]; A[r]=[x*inv for x in A[r]]
    for i in range(m):
        if i!=r and A[i][c]!=0:
            f=A[i][c]; A[i]=[x-f*y for x,y in zip(A[i],A[r])]
    piv.append(c); r+=1
free=[c for c in range(n) if c not in piv]
fc=free[0]; v=[Q(0)]*n; v[fc]=Q(1)
for i,c in enumerate(piv): v[c]=-A[i][fc]
from math import gcd
den=1
for x in v: den=den*x.denominator//gcd(den,x.denominator)
vi=[int(x*den) for x in v]
g=0
for x in vi: g=gcd(g,abs(x))
vi=[x//g for x in vi]
print("Relation coefficients c_{i,j} for v^i F^j:")
for (t,c) in zip(terms,vi):
    if c: print("   v^%d F^%d : %d"%(t[0],t[1],c))
# pretty by powers of F
print()
for j in range(6):
    cs=[c for (t,c) in zip(terms,vi) if t[1]==j]
    print("  F^%d coeff:  %d + %d*v"%(j,cs[0],cs[1]))
