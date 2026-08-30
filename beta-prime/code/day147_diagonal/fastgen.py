"""Fast regeneration of b_k, h_j.

Key speedup: Psi_{b+1} = (E2-(b+1)E1+(b+1)^2)Psi_b - 3b E3 sigma(Psi_{b-1})
                          - b(b-1)(E1-2b-2) E3 sigma(Psi_{b-2}),
with sigma: E1->E1-3, E2->E2-2E1+3, E3->E3-E2+E1-1.
Evaluating at a NUMERIC (E1,E2)=(e1,e2) but SYMBOLIC E3 only ever requires Psi_{b-1},
Psi_{b-2} at the sigma-image point, with E3 translated by c = e1-e2-1.  So we can walk the
sigma-orbit of the base point and keep only univariate polynomials in E3.  O(BMAX^4) instead
of full 3-variable expansion.

Validated against day146_prove/bigdata.py output at BMAX=36.
"""
import sys, math, json, time
from fractions import Fraction as Q
from collections import defaultdict

def shift(p, c):
    """p(E3) -> p(E3+c);  p = list of int coeffs."""
    if c == 0: return p[:]
    d = len(p)-1
    out=[0]*(d+1)
    # binomial powers of c
    cp=[1]*(d+1)
    for i in range(1,d+1): cp[i]=cp[i-1]*c
    C=[[0]*(d+1) for _ in range(d+1)]
    for i in range(d+1):
        C[i][0]=1
        for j in range(1,i+1): C[i][j]=C[i-1][j-1]+(C[i-1][j] if j<=i-1 else 0)
    for k,a in enumerate(p):
        if a==0: continue
        for j in range(k+1):
            out[j]+=a*C[k][j]*cp[k-j]
    return out

def padd(a,b):
    n=max(len(a),len(b)); r=[0]*n
    for i,x in enumerate(a): r[i]+=x
    for i,x in enumerate(b): r[i]+=x
    return r
def pscal(k,a): return [k*x for x in a]
def pshiftE3(a): return [0]+a   # multiply by E3

def psi_at(e1_0, e2_0, BMAX):
    """returns list Psi[b] = coeffs (in E3) of Psi_b at base point, b=0..BMAX"""
    # orbit
    pts=[(e1_0,e2_0)]
    for _ in range(BMAX+1):
        e1,e2=pts[-1]; pts.append((e1-3, e2-2*e1+3))
    cs=[e1-e2-1 for e1,e2 in pts]
    # Psi[n][b], need n+b<=BMAX
    Psi=[[None]*(BMAX+1) for _ in range(BMAX+2)]
    for n in range(BMAX+1):
        Psi[n][0]=[1]
        if BMAX>=1: Psi[n][1]=[pts[n][1]-pts[n][0]+1]
    for b in range(1,BMAX):
        for n in range(0,BMAX-b):
            e1,e2=pts[n]; c=cs[n]; cc=b+1
            t=pscal(e2-cc*e1+cc*cc, Psi[n][b])
            t=padd(t, pscal(-3*b, pshiftE3(shift(Psi[n+1][b-1], c))))
            if b>=2:
                t=padd(t, pscal(-b*(b-1)*(e1-2*b-2), pshiftE3(shift(Psi[n+1][b-2], c))))
            Psi[n][b+1]=t
    return [Psi[0][b] for b in range(BMAX+1)]

def Pseries(e1,e2,BMAX):
    """P_b = phi(Psi_b): E1->-E1, E3->-E3.  Return {b:{k:val}} at given (E1,E2)=(e1,e2)."""
    ps=psi_at(-e1,e2,BMAX)   # substitute E1 -> -e1
    out={}
    for b,p in enumerate(ps):
        out[b]={k:((-1)**k)*v for k,v in enumerate(p) if v}
    return out

def smul(A,B,N):
    R=defaultdict(lambda: defaultdict(Q))
    for b1,d1 in A.items():
        if b1>N: continue
        for b2,d2 in B.items():
            if b1+b2>N: continue
            for k1,v1 in d1.items():
                for k2,v2 in d2.items(): R[b1+b2][k1+k2]+=v1*v2
    return {b:{k:v for k,v in d.items() if v} for b,d in R.items()}
def sinv(A,N):
    B={0:{0:Q(1)}}
    for n in range(1,N+1):
        acc=defaultdict(Q)
        for j in range(1,n+1):
            for k1,v1 in A.get(j,{}).items():
                for k2,v2 in B.get(n-j,{}).items(): acc[k1+k2]-=v1*v2
        B[n]={k:v for k,v in acc.items() if v}
    return B
def slog(A,N):
    u={b:d for b,d in A.items() if b>=1}
    out=defaultdict(lambda: defaultdict(Q)); term={0:{0:Q(1)}}
    for m in range(1,N+1):
        term=smul(term,u,N)
        if not term: break
        c=Q((-1)**(m-1),m)
        for b,d in term.items():
            for k,v in d.items(): out[b][k]+=c*v
    return {b:{k:v for k,v in d.items() if v} for b,d in out.items()}

if __name__=="__main__":
    BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 36
    t0=time.time()
    Pa=Pseries(-2,1,BMAX); Pb=Pseries(1,0,BMAX)
    t1=time.time(); print(f"Psi orbit computation: {t1-t0:.1f}s",flush=True)
    FP ={b:{k:Q(v,math.factorial(b)) for k,v in Pa[b].items()} for b in range(BMAX+1)}
    FPt={b:{k:Q(v,math.factorial(b)) for k,v in Pb[b].items()} for b in range(BMAX+1)}
    H=smul(FPt,sinv(FP,BMAX),BMAX); LG=slog(FP,BMAX)
    print(f"series ops: {time.time()-t1:.1f}s",flush=True)
    K=(BMAX+1)//3
    bk=[str((3*k-1)*LG.get(3*k-1,{}).get(k,Q(0))) for k in range(1,K+1)]
    hj=[str(H.get(3*j,{}).get(j,Q(0))) for j in range(0,K+1)]
    badint=[(b,k) for b in H for k,v in H[b].items() if v.denominator!=1]
    badord=[(b,k) for b in H for k,v in H[b].items() if v and b<3*k]
    print("BMAX",BMAX)
    print("b_k:",bk)
    print("h_j:",hj)
    print("H integral up to T^%d:"%BMAX,"YES" if not badint else badint[:5])
    print("H order>=0:","YES" if not badord else badord[:5])
    json.dump({"BMAX":BMAX,"b":bk,"h":hj},open(f"data_{BMAX}.json","w"))
    print("total %.1fs"%(time.time()-t0))
