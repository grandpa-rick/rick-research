"""Day 147 Task 0: independent regeneration of h_j and s_n.
Uses only core.py (the Psi-recursion = the DEFINITION); all series algebra rewritten."""
import sys, math, json, time
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P, subs_E12
from fractions import Fraction as Q
from collections import defaultdict

BMAX = int(sys.argv[1]) if len(sys.argv)>1 else 36
t0=time.time()
P = build_P(BMAX)
print("built P in %.1fs"%(time.time()-t0)); sys.stdout.flush()

# F_P = sum_b P_b T^b/b!   -> dict b -> {E3power: Fraction}
def series_at(e1,e2):
    out={}
    for b in range(BMAX+1):
        f=math.factorial(b)
        out[b]={k:Q(v,f) for k,v in subs_E12(P[b],e1,e2).items()}
    return out
FP  = series_at(-2,1)   # base point (U,V)=(0,0)
FPt = series_at(1,0)    # tau of base point; E3 unshifted since phi_1=0

def mul(A,B,N):
    R=[defaultdict(Q) for _ in range(N+1)]
    for b1 in range(N+1):
        d1=A.get(b1)
        if not d1: continue
        for b2 in range(N+1-b1):
            d2=B.get(b2)
            if not d2: continue
            tgt=R[b1+b2]
            for k1,v1 in d1.items():
                for k2,v2 in d2.items(): tgt[k1+k2]+=v1*v2
    return {b:{k:v for k,v in d.items() if v} for b,d in enumerate(R)}
def inv(A,N):
    assert A[0]=={0:Q(1)}, A[0]
    B={0:{0:Q(1)}}
    for n in range(1,N+1):
        acc=defaultdict(Q)
        for j in range(1,n+1):
            for k1,v1 in A.get(j,{}).items():
                for k2,v2 in B.get(n-j,{}).items(): acc[k1+k2]-=v1*v2
        B[n]={k:v for k,v in acc.items() if v}
    return B

H = mul(FPt, inv(FP,BMAX), BMAX)
J = BMAX//3
h = [H.get(3*j,{}).get(j,Q(0)) for j in range(J+1)]
print("\nh_j (j=0..%d):"%J)
for j,v in enumerate(h): print("  h_%-2d = %-28s int? %s"%(j,v,v.denominator==1))
assert all(v.denominator==1 for v in h)

# ---- b_k independently, from log F_P ----
def slog(A,N):
    # log of A with A[0]={0:1}
    out=[defaultdict(Q) for _ in range(N+1)]
    term={0:{0:Q(1)}}
    u={b:d for b,d in A.items() if b>=1}
    for m in range(1,N+1):
        term=mul(term,u,N)
        if not any(term.values()): break
        c=Q((-1)**(m-1),m)
        for b,d in term.items():
            for k,v in d.items(): out[b][k]+=c*v
    return {b:{k:v for k,v in d.items() if v} for b,d in enumerate(out)}
LG=slog(FP,BMAX)
K=(BMAX+1)//3
bk=[(3*k-1)*LG.get(3*k-1,{}).get(k,Q(0)) for k in range(1,K+1)]
print("\nb_k:", [str(x) for x in bk])
print("v3(b_k):", [ (lambda n: (0 if n==0 else (len(str(n))*0 or _v3(n))))(int(x)) for x in bk] if False else [_v3(int(x)) for x in bk] if False else None)

# ---- S = log(Hdiag), s_n = n*[theta^n]S ----
Hd=[Q(x) for x in h]                       # coefficients of curly-H in theta
N=len(Hd)-1
# log of power series with constant term 1
Ld=[Q(0)]*(N+1)
# use  L' * H = H'  ->  n*L_n = n*H_n - sum_{j=1}^{n-1} j*L_j*H_{n-j}
for n in range(1,N+1):
    acc = n*Hd[n] - sum(j*Ld[j]*Hd[n-j] for j in range(1,n))
    Ld[n]=acc/n
s=[n*Ld[n] for n in range(N+1)]
print("\nS = log(Hcal) coefficients L_n and s_n = n*L_n:")
for n in range(1,N+1):
    print("  n=%-3d L_n = %-34s s_n = %-30s int? %s"%(n,Ld[n],s[n],s[n].denominator==1))
json.dump({"BMAX":BMAX,"h":[str(x) for x in h],"b":[str(x) for x in bk],
           "s":[str(x) for x in s]},open('/home/agent/projects/beta-prime/code/day147_gauss/data.json','w'))
print("\ntotal %.1fs"%(time.time()-t0))
