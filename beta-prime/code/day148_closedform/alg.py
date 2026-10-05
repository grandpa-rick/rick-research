from fractions import Fraction as Q
import json, itertools
d=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
b=[0]+[int(x) for x in d['b']]   # b[1..15]
N=15
# F(v) = sum_{k>=1} b_k v^k  as list of coeffs index 0..N
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
for _ in range(8): pw.append(mul(pw[-1],F))
def nullspace(M):
    # M: list of rows (Fractions). return basis of nullspace of M (columns=unknowns)
    import copy
    m=len(M); n=len(M[0]) if m else 0
    A=[row[:] for row in M]; piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i;break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        inv=Q(1)/A[r][c]
        A[r]=[x*inv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    basis=[]
    for fc in free:
        v=[Q(0)]*n; v[fc]=Q(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        basis.append(v)
    return basis
print("algebraicity of F: search sum_{i<=D} sum_{j<=E} c_ij v^i F^j = 0")
for E in range(1,7):
    for D in range(0,7):
        terms=[(i,j) for j in range(E+1) for i in range(D+1)]
        nun=len(terms)
        rows=[]
        for n in range(0,N+1):
            row=[]
            for (i,j) in terms:
                row.append(pw[j][n-i] if 0<=n-i<=N else Q(0))
            rows.append(row)
        if len(rows)<nun+1: continue   # need more equations than unknowns
        ns=nullspace(rows)
        if ns: print("  HIT D=%d E=%d  dim=%d  (unknowns %d, eqs %d)"%(D,E,len(ns),nun,len(rows)))
print("done")
