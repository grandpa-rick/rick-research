import json, itertools
from fractions import Fraction as Q
d=json.load(open("data.json")); b=[int(x) for x in d["b"]]; h=[int(x) for x in d["h"]]
def v3(n):
    v=0
    while n%3==0: n//=3;v+=1
    return v
print("v3(b_k) k=1..:",[v3(x) for x in b])
print("v3(h_j) j=0..:",[v3(x) if x else '-' for x in h])
# P-recurrence search: sum_{i=0..R} p_i(n) a_{n+i} = 0, deg p_i <= D
def prec(a,R,D,name):
    # unknowns: coefficients c_{i,d}
    rows=[]; N=len(a)
    for n in range(0,N-R):
        row=[]
        for i in range(R+1):
            for dd in range(D+1):
                row.append(Q(a[n+i]*n**dd))
        rows.append(row)
    m=len(rows); ncol=(R+1)*(D+1)
    if m< ncol+2: return None
    # gaussian elim for nullspace
    import copy
    A=[r[:] for r in rows]; piv=[]; r=0
    for c in range(ncol):
        pr=None
        for rr in range(r,m):
            if A[rr][c]!=0: pr=rr;break
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for rr in range(m):
            if rr!=r and A[rr][c]!=0:
                f=A[rr][c]; A[rr]=[x-f*y for x,y in zip(A[rr],A[r])]
        piv.append(c); r+=1
        if r==m: break
    if r<ncol:
        print(f"  {name}: NONTRIVIAL nullspace R={R} D={D} (rank {r}/{ncol}, {m} eqs)")
        return True
    return False
for R in range(1,5):
    for D in range(0,5):
        prec(b,R,D,"b_k")
        prec(h,R,D,"h_j")
print("done recurrence scan")
