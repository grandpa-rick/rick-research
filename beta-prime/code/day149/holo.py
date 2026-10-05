import pickle, itertools
from fractions import Fraction as Q
import sys
H=pickle.load(open('H16.pkl','rb'))
def ev(A,e): return sum(c*e[0]**m[0]*e[1]**m[1]*e[2]**m[2] for m,c in A.items())
def prec_search(seq,maxord,maxdeg):
    """find c_{i,j}: sum_{i<=ord} P_i(n) a_{n+i} = 0 with deg P_i <= maxdeg"""
    N=len(seq)
    for ordr in range(1,maxord+1):
        for deg in range(0,maxdeg+1):
            cols=(ordr+1)*(deg+1)
            rows=N-ordr
            if rows<cols+3: continue
            M=[]
            for n in range(rows):
                row=[]
                for i in range(ordr+1):
                    for d in range(deg+1):
                        row.append(Q(seq[n+i])*Q(n)**d)
                M.append(row)
            # nullspace over Q
            import copy
            A=[r[:] for r in M]; m=len(A); ncol=cols
            piv=[]; r=0
            for c in range(ncol):
                pr=None
                for rr in range(r,m):
                    if A[rr][c]!=0: pr=rr;break
                if pr is None: continue
                A[r],A[pr]=A[pr],A[r]
                pv=A[r][c]
                A[r]=[x/pv for x in A[r]]
                for rr in range(m):
                    if rr!=r and A[rr][c]!=0:
                        f=A[rr][c]; A[rr]=[a-f*b for a,b in zip(A[rr],A[r])]
                piv.append(c); r+=1
                if r==m: break
            if r<ncol:
                return (ordr,deg,ncol-r)
    return None
for pt in [(0,0,0),(1,0,0),(0,1,0),(1,1,1)]:
    seq=[ev(H[n],pt) for n in range(17)]
    print(pt, seq[:8])
    res=prec_search(seq,4,4)
    print("   P-recursive (ord<=4,deg<=4):",res)
