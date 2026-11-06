"""All (*)-violating (lambda, A) at n=14 and all candidate pairs (P_x,P_z) with {} != Des Pz subset int Des Px."""
import sys
sys.path.insert(0,'.')
from common import syts
n=14
def parts(n,m=None):
    if m is None: m=n
    if n==0: yield []; return
    for k in range(min(n,m),0,-1):
        for p in parts(n-k,k): yield [k]+p
def comp(cuts):
    c=sorted(cuts); prev=0; out=[]
    for i in c: out.append(i-prev); prev=i
    out.append(n-prev); return sorted(out,reverse=True)
def conj(a): return [sum(1 for x in a if x>=k) for k in range(1,(a[0] if a else 0)+1)]
def dom(b,a):
    sb=sa=0
    for k in range(max(len(a),len(b))):
        sb+= b[k] if k<len(b) else 0; sa+= a[k] if k<len(a) else 0
        if sb>sa: return False
    return True
intr=lambda A:{i for i in A if all(j in A for j in (i-1,i+1) if 1<=j<=n-1)}
viol=[]
for m in range(1,2**(n-1)-1):
    A={i for i in range(1,n) if m>>(i-1)&1}; I=intr(A)
    if not I: continue
    al=comp(I); be=comp(set(range(1,n))-A)
    for lam in parts(n):
        if dom(be,conj(lam)) and dom(al,lam): viol.append((tuple(lam),tuple(sorted(A))))
print('violating (lambda,A):',len(viol))
for v in viol: print(' ',v)
