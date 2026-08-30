import json
from fractions import Fraction as Q
from sympy import Matrix, nsimplify
D=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
h=[Q(x) for x in D["h"]]; s=[Q(x) for x in D["s"]]; b=[Q(x) for x in D["b"]]
print("growth ratios s_{n+1}/s_n :", [float(s[n+1]/s[n]) for n in range(1,len(s)-1)])
print("growth ratios h_{j+1}/h_j :", [float(h[j+1]/h[j]) for j in range(len(h)-1)])
print("growth ratios b_{k+1}/b_k :", [float(b[k+1]/b[k]) for k in range(len(b)-1)])
print()
def algsearch(name, coeffs, dmax=4, emax=4):
    """look for sum_{j<=dmax} P_j(x) G(x)^j = 0, deg P_j <= emax"""
    N=len(coeffs)-1
    G=[coeffs+[Q(0)]*(N+1)]
    pw=[[Q(1)]+[Q(0)]*N]
    for j in range(1,dmax+1):
        prev=pw[-1]
        pw.append([sum(prev[i]*coeffs[k-i] for i in range(k+1) if k-i<len(coeffs)) for k in range(N+1)])
    print("=== algebraicity search for %s: sum_{j=0..d} P_j(x) G^j = 0, deg P_j<=e ==="%name)
    hit=False
    for d in range(1,dmax+1):
        for e in range(0,emax+1):
            nun=(d+1)*(e+1)
            rows=[]
            for k in range(N+1):
                rows.append([ (pw[j][k-t] if 0<=k-t<=N else Q(0)) for j in range(d+1) for t in range(e+1)])
            if len(rows) < nun+1: continue
            ns=Matrix(rows).nullspace()
            if ns:
                hit=True; print("   HIT d=%d e=%d (%d eqns, %d unknowns, nullity %d)"%(d,e,len(rows),nun,len(ns)))
    if not hit: print("   NONE in tested box")
    tested=[(d,e) for d in range(1,dmax+1) for e in range(0,emax+1) if (N+1)>=(d+1)*(e+1)+1]
    print("   box actually tested (d,e):", tested)
algsearch("Hcal", h)
algsearch("F", [Q(0)]+b)
