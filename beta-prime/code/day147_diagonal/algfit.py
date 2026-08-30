"""Task 4 extra: algebraic-equation fit  sum_{a<=A, b<=B} c_{ab} v^a S(v)^b = 0 for S = F or Hcal."""
import json,sys
from fractions import Fraction as Q
d=json.load(open(sys.argv[1] if len(sys.argv)>1 else "data_36.json"))
h=[Q(int(x)) for x in d["h"]]; b=[Q(int(x)) for x in d["b"]]
N=len(h)-1
F=[Q(0)]+b[:N]
F=F[:N+1]
def mul(A,B,N):
    R=[Q(0)]*(N+1)
    for i,x in enumerate(A):
        if x==0: continue
        for j,y in enumerate(B):
            if i+j>N: break
            R[i+j]+=x*y
    return R
def nullity(rows,ncol):
    A=[r[:] for r in rows]; m=len(A); r=0
    for c in range(ncol):
        pr=next((rr for rr in range(r,m) if A[rr][c]!=0),None)
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for rr in range(m):
            if rr!=r and A[rr][c]!=0:
                f=A[rr][c]; A[rr]=[x-f*y for x,y in zip(A[rr],A[r])]
        r+=1
        if r==m: break
    return ncol-r
def scan(S,name,margin=3):
    S=S[:N+1]
    pw=[[Q(1)]+[Q(0)]*N]
    for _ in range(5): pw.append(mul(pw[-1],S,N))
    print(f"--- algebraic fit for {name} ({N+1} coefficients) ---")
    for A in range(0,5):
        for Bd in range(1,5):
            ncol=(A+1)*(Bd+1)
            rows=[]
            for n in range(N+1):
                row=[]
                for a in range(A+1):
                    for bb in range(Bd+1):
                        row.append(pw[bb][n-a] if n-a>=0 else Q(0))
                rows.append(row)
            if len(rows)<ncol+margin:
                print(f"  degv<={A} degS<={Bd}: UNDERDETERMINED ({len(rows)} eqs < {ncol}+{margin})"); continue
            nl=nullity(rows,ncol)
            print(f"  degv<={A} degS<={Bd}: {len(rows)} eqs, {ncol} unk, nullity {nl} -> {'CANDIDATE' if nl>0 else 'none'}")
    print()
scan(F,"F = sum b_k v^k")
scan(h,"Hcal")
