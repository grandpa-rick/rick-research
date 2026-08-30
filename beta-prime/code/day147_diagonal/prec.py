"""Task 4: holonomic (P-recursive) search + growth analysis for h_j (and b_k)."""
import json,sys
from fractions import Fraction as Q
fn=sys.argv[1] if len(sys.argv)>1 else "data_36.json"
d=json.load(open(fn)); B=[int(x) for x in d["b"]]; H=[int(x) for x in d["h"]]

def nullspace_dim(rows,ncol):
    A=[r[:] for r in rows]; m=len(A); r=0
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
        r+=1
        if r==m: break
    return ncol-r, r

def scan(a,name,Rmax=4,Dmax=4,margin=3):
    print(f"--- P-recursion scan for {name} ({len(a)} terms), sum_i p_i(n) a_{{n+i}} = 0 ---")
    found=False
    for R in range(1,Rmax+1):
        for DD in range(0,Dmax+1):
            ncol=(R+1)*(DD+1)
            rows=[]
            for n in range(0,len(a)-R):
                row=[]
                for i in range(R+1):
                    for dd in range(DD+1):
                        row.append(Q(a[n+i])*Q(n)**dd)
                rows.append(row)
            m=len(rows)
            if m < ncol+margin:
                print(f"  R={R} D={DD}: UNDERDETERMINED ({m} eqs < {ncol}+{margin} unknowns) -- not tested")
                continue
            dim,rk=nullspace_dim(rows,ncol)
            tag = "CANDIDATE" if dim>0 else "none"
            print(f"  R={R} D={DD}: {m} eqs, {ncol} unknowns, rank {rk}, nullity {dim}  -> {tag}")
            if dim>0: found=True
    print(f"  VERDICT {name}: {'candidate(s) found' if found else 'NO P-recurrence with order<=%d, deg<=%d in the tested (overdetermined) range'%(Rmax,Dmax)}")
    print()
scan(H,"h_j"); scan(B,"b_k")

print("--- growth of h_j ---")
import math
r=[H[j+1]/H[j] for j in range(len(H)-1)]
print("  ratios h_{j+1}/h_j:", [round(x,4) for x in r])
# Richardson: assume r_j = L + c/j (+...) ; L_j = j*r_j - (j-1)*r_{j-1}
print("  Richardson-1 (L=j*r_j-(j-1)*r_{j-1}):", [round(j*r[j]-(j-1)*r[j-1],3) for j in range(1,len(r))])
R1=[j*r[j]-(j-1)*r[j-1] for j in range(1,len(r))]
print("  Richardson-2:", [round((j+1)*R1[j]-j*R1[j-1],3) for j in range(1,len(R1))])
print("  r_j/27:", [round(x/27,5) for x in r])
print("  27 - r_j:", [round(27-x,4) for x in r])
print("  j*(27-r_j):", [round(j*(27-r[j]),4) for j in range(1,len(r))])
print()
print("--- is h_j ~ C * 27^j * j^a ? ---")
for j in range(1,len(H)):
    x=H[j]/(27.0**j)
    print(f"   j={j:2d}  h_j/27^j = {x:.6g}   log ratio = {math.log(H[j]/H[j-1])/math.log(27):.5f}")
