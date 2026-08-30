import json
from fractions import Fraction as Q
from sympy import Matrix
D=json.load(open('data.json')); s=[Q(x) for x in D["s"]]
# asymptotic fit  s_{n+1}/s_n = L (1 - a/n),  a = r/2  (r = number of variables)
print("=== two-point fits of s_{n+1}/s_n = L(1-a/n):  a = r/2, so r = 2a ===")
r=[s[n+1]/s[n] for n in range(1,len(s)-1)]   # r[i] corresponds to n=i+1
for i in range(1,len(r)):
    n1,n2=i,i+1; R1,R2=float(r[i-1]),float(r[i])
    # R1 = L(1-a/n1), R2 = L(1-a/n2)
    # R2/R1 = (1-a/n2)/(1-a/n1) -> solve
    k=R2/R1
    a=(n1*n2*(1-k))/(n2-k*n1) if (n2-k*n1)!=0 else float('nan')
    L=R2/(1-a/n2)
    print("  n=(%2d,%2d)   a=%.4f  => r=2a=%.3f    L=%.4f"%(n1,n2,a,2*a,L))
print()
Sg=[Q(1)]+list(s[1:])   # Sigma(z) = sum_{n>=0} s_n z^n , s_0 = Cst(lambda^0)=1
def algsearch(name, c, dmax=5, emax=5):
    N=len(c)-1
    pw=[[Q(1)]+[Q(0)]*N]
    for j in range(1,dmax+1):
        p=pw[-1]; pw.append([sum(p[i]*c[k-i] for i in range(k+1)) for k in range(N+1)])
    print("=== algebraicity of %s: sum_{j<=d} P_j(z) G^j = 0, deg P_j <= e ==="%name)
    hit=False; tested=[]
    for d in range(1,dmax+1):
        for e in range(0,emax+1):
            nun=(d+1)*(e+1)
            if (N+1) < nun+1: continue
            tested.append((d,e))
            rows=[[ (pw[j][k-t] if 0<=k-t<=N else Q(0)) for j in range(d+1) for t in range(e+1)] for k in range(N+1)]
            ns=Matrix(rows).nullspace()
            if ns: hit=True; print("   HIT d=%d e=%d nullity %d"%(d,e,len(ns)))
    if not hit: print("   NONE in tested box", tested)
def prec(name, c, rmax=5, dmax=5, off=0):
    L=len(c); print("=== holonomy of %s ==="%name); hit=False; tested=[]
    for rr in range(1,rmax+1):
        for d in range(0,dmax+1):
            nun=(rr+1)*(d+1)
            if (L-rr) < nun+1: continue
            tested.append((rr,d))
            rows=[[ (n+off)**e * c[n+i] for i in range(rr+1) for e in range(d+1)] for n in range(0,L-rr)]
            ns=Matrix(rows).nullspace()
            if ns: hit=True; print("   HIT order=%d deg=%d nullity %d"%(rr,d,len(ns)))
    if not hit: print("   NONE in tested box", tested)
algsearch("Sigma(z)=sum s_n z^n", Sg)
prec("s_n", [int(x) for x in Sg], off=0)
