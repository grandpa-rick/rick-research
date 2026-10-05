#!/usr/bin/env python3
"""Day 151 task 1: compute the Arc-B Lagrange kernel psi to high order, from scratch.

H is rebuilt from the DEFINITION (see indep_check_fast.py); psi is then the Lagrange
kernel of the leading symbol calW = ell^top_0(H):
    W_n = (weighted-degree-n part of H_n)/(n+1),  wt(E1^a E2^b E3^c)=a+2b+3c
    Y(T) = T*calW(T),   psi(Y) := calW(T(Y)) = Y/T(Y),   so  Y = T*psi(Y).
"""
import pickle, math, sys
from collections import defaultdict
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day151')
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20

def mul(A,B):
    R=defaultdict(int)
    for m1,c1 in A.items():
        for m2,c2 in B.items(): R[(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])]+=c1*c2
    return {m:c for m,c in R.items() if c}
def add(A,B):
    R=defaultdict(int)
    for X in (A,B):
        for m,c in X.items(): R[m]+=c
    return {m:c for m,c in R.items() if c}
def scal(k,A): return {m:k*c for m,c in A.items()} if k else {}
ONE={(0,0,0):1}
V=mul(mul({(1,0,0):1,(0,1,0):-1},{(1,0,0):1,(0,0,1):-1}),{(0,1,0):1,(0,0,1):-1})
E2m={(1,1,0):1,(1,0,1):1,(0,1,1):1}
D=NMAX*2+8
st=[[0]*(D+1) for _ in range(D+1)]; st[0][0]=1
for n in range(1,D+1):
    for k in range(1,n+1): st[n][k]=st[n-1][k-1]+(n-1)*st[n-1][k]
def Tplus(A):
    R=defaultdict(int)
    for (i,j,k),c in A.items():
        for a in range(i+1):
            if not st[i][a]: continue
            ca=c*st[i][a]
            for b in range(j+1):
                if not st[j][b]: continue
                cb=ca*st[j][b]
                for d in range(k+1):
                    if st[k][d]: R[(a,b,d)]+=cb*st[k][d]
    return {m:c for m,c in R.items() if c}
binom=[[math.comb(n,k) for k in range(D+1)] for n in range(D+1)]
def tau(A):
    R=defaultdict(int)
    for (i,j,k),c in A.items():
        for a in range(i+1):
            ca=c*binom[i][a]
            for b in range(j+1):
                cb=ca*binom[j][b]
                for d in range(k+1): R[(a,b,d)]+=cb*binom[k][d]
    return {m:c for m,c in R.items() if c}
def divlin(A,p,q):
    byd=defaultdict(dict)
    for m,c in A.items():
        rest=list(m); dp=rest[p]; rest[p]=0; byd[dp][tuple(rest)]=c
    dmax=max(byd) if byd else 0
    Qd={}; out=defaultdict(int); rem={}
    for d in range(dmax,-1,-1):
        cur=add(dict(byd.get(d,{})),Qd)
        if d==0: rem=cur; break
        for m,c in cur.items():
            mm=list(m); mm[p]=d-1; out[tuple(mm)]+=c
        Qd={}
        for m,c in cur.items():
            mm=list(m); mm[q]+=1; Qd[tuple(mm)]=c
    assert not {m:c for m,c in rem.items() if c}
    return {m:c for m,c in out.items() if c}
def divV(A): return divlin(divlin(divlin(A,0,1),0,2),1,2)

# ---- H in u-coordinates ----
A=[]; cur=dict(V)
for n in range(NMAX+1):
    A.append(Tplus(cur)); cur=mul(cur,E2m)
Hu=[]
for n in range(NMAX+1):
    acc=tau(A[n])
    for k in range(1,n+1):
        acc=add(acc,scal(-(math.factorial(n)//math.factorial(k)),mul(A[k],Hu[n-k])))
    fn=math.factorial(n)
    assert all(c%fn==0 for c in acc.values()),n
    Hu.append(divV({m:c//fn for m,c in acc.items()}))
    print("  H T^%d"%n); sys.stdout.flush()

# ---- convert to E-basis by leading-term reduction ----
def toE(P):
    P=dict(P); out=defaultdict(int)
    e=[{(0,0,0):1},{(1,0,0):1,(0,1,0):1,(0,0,1):1},E2m,{(1,1,1):1}]
    while P:
        # lex-largest monomial
        m=max(P); c=P[m]
        assert m[0]>=m[1]>=m[2], ("not symmetric / bad lead",m)
        a,b,cc=m[0]-m[1], m[1]-m[2], m[2]
        out[(a,b,cc)]+=c
        t={(0,0,0):c}
        for _ in range(a): t=mul(t,e[1])
        for _ in range(b): t=mul(t,e[2])
        for _ in range(cc): t=mul(t,e[3])
        P=add(P,scal(-1,t))
    return {m:c for m,c in out.items() if c}
H=[toE(h) for h in Hu]

# cross-check against H16.pkl where available
ref=pickle.load(open('/home/agent/projects/beta-prime/code/day149/H16.pkl','rb'))
for n in range(min(NMAX,16)+1): assert H[n]==ref[n], ("H mismatch vs H16.pkl at",n)
print("H matches day149 H16.pkl for n<=%d"%min(NMAX,16))

# ---- leading symbol W ----
W=[]
for n in range(NMAX+1):
    S={m:c for m,c in H[n].items() if m[0]+2*m[1]+3*m[2]==n}
    assert all(c%(n+1)==0 for c in S.values()),n
    W.append({m:c//(n+1) for m,c in S.items()})
assert W[0]==ONE
# Narayana check at E3=0
for n in range(1,NMAX+1):
    coef=defaultdict(int)
    for (a,b,c),co in W[n].items():
        if c: continue
        for i in range(a+1): coef[(a-i+b,i+b)]+=co*math.comb(a,i)
    got=[coef.get((n-k,k),0) for k in range(n+1)]
    want=[math.comb(n+1,k)*math.comb(n+1,k+1)//(n+1) for k in range(n+1)]
    assert got==want,(n,got,want)
print("Narayana at E3=0 verified for n=1..%d"%NMAX)

# ---- reversion; psi valid to Y^NMAX ----
M=NMAX
def compose(f,g):
    res=[{} for _ in range(M+1)]; gp=[{} for _ in range(M+1)]; gp[0]=dict(ONE)
    for k in range(M+1):
        if k>0:
            new=[{} for _ in range(M+1)]
            for i in range(M+1):
                if not gp[i]: continue
                for j in range(1,M+1-i):
                    if g[j]: new[i+j]=add(new[i+j],mul(gp[i],g[j]))
            gp=new
        if f[k]:
            for i in range(M+1):
                if gp[i]: res[i]=add(res[i],mul(f[k],gp[i]))
    return res
calW=[W[n] for n in range(M+1)]
Yc=[{}]+[W[n] for n in range(M)]
Tc=[{} for _ in range(M+1)]; Tc[1]=dict(ONE)
for m in range(2,M+1):
    c=compose(Yc,Tc)
    if c[m]: Tc[m]=add(Tc[m],scal(-1,c[m]))
c=compose(Yc,Tc)
for k in range(M+1): assert c[k]==(ONE if k==1 else {}),k
psi=compose(calW,Tc)
chk=[{} for _ in range(M+1)]
for i in range(M+1):
    for j in range(M+1-i):
        if psi[i] and Tc[j]: chk[i+j]=add(chk[i+j],mul(psi[i],Tc[j]))
for k in range(M+1): assert chk[k]==(ONE if k==1 else {}),("psi*T!=Y",k)
print("reversion + psi*T=Y verified to Y^%d"%M)
pickle.dump({'W':W,'psi':psi,'H':H},open('/home/agent/projects/beta-prime/code/day151/psi%d.pkl'%NMAX,'wb'))

def fmt(A):
    if not A: return "0"
    def key(m): return (m[0]+2*m[1]+3*m[2],m[2],m[1],m[0])
    ps=[]
    for m in sorted(A,key=key):
        co=A[m]; s=""
        for sym,e in zip(("E1","E2","E3"),m):
            if e==1: s+=sym
            elif e>1: s+="%s^%d"%(sym,e)
        pre="+ " if co>0 else "- "
        if s=="": ps.append(pre+str(abs(co)))
        else: ps.append(pre+(("%d "%abs(co)) if abs(co)!=1 else "")+s)
    o=" ".join(ps)
    return o[2:] if o.startswith("+ ") else o
KNOWN={0:"1",1:"E1",2:"E2",3:"2E3",4:"E1E3",5:"2E2E3",6:"E1E2E3 + 5E3^2"}
print("\n=== psi ===")
for k in range(M+1):
    t="      <-- published Day149/150: %s"%KNOWN[k] if k in KNOWN else ""
    print("[Y^%2d] %s%s"%(k,fmt(psi[k]),t))
print("\n=== (A) slice E1=E2=0, W=E3*Y^3 ===")
seq=[]
for n in range(M//3+1):
    S={m:c for m,c in psi[3*n].items() if m[0]==0 and m[1]==0}
    seq.append(S.get((0,0,n),0))
    assert set(S)<= {(0,0,n)}
print("[W^n] psi|E1=E2=0 :",seq)
print("Catalan C_{n+1}   :",[math.comb(2*n+2,n+1)//(n+2) for n in range(len(seq))])
# also: any non-pure-E3 survivors on the slice?
for k in range(M+1):
    S={m:c for m,c in psi[k].items() if m[0]==0 and m[1]==0}
    if S and k%3: print("  UNEXPECTED at Y^%d: %s"%(k,fmt(S)))
print("\n=== (B) E-positivity ===")
neg=[(k,m,c) for k in range(M+1) for m,c in psi[k].items() if c<0]
print("negative coefficients:", neg if neg else "NONE  -> psi is E-positive to Y^%d"%M)
print("all integers: True (exact Z arithmetic)")
# divisibility by E3 from Y^3 on
bad=[(k,m) for k in range(3,M+1) for m in psi[k] if m[2]==0]
print("every coeff from Y^3 on divisible by E3:", "YES" if not bad else bad)
