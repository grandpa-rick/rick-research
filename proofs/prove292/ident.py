# Verify Key Identity: M_alpha^perp R_(2^k) = (-1)^{k+l(alpha)} [z^{2k-i}] (W Theta)^{o(alpha)} W
# NSym in S-basis: dict tuple(comp)->Fraction. M_alpha^perp S^gamma = sum over strictly increasing positions lowering.
import itertools, sys
from fractions import Fraction
import sympy
def comps(n):
    if n==0: yield (); return
    for f in range(1,n+1):
        for r in comps(n-f): yield (f,)+r
def add(a,b,c=1):
    for k,v in b.items(): a[k]=a.get(k,0)+c*v
    return a
def mul(a,b):
    o={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=k1+k2; o[k]=o.get(k,0)+v1*v2
    return {k:v for k,v in o.items() if v}
def Mperp(alpha,a):
    o={}
    l=len(alpha)
    for g,v in a.items():
        for pos in itertools.combinations(range(len(g)),l):
            h=list(g); ok=True
            for p,m in zip(pos,alpha):
                h[p]-=m
                if h[p]<0: ok=False;break
            if not ok: continue
            h=tuple(x for x in h if x>0)
            o[h]=o.get(h,0)+v
    return {k:v for k,v in o.items() if v}
def R(alpha):  # ribbon = sum over coarsenings
    l=len(alpha); o={}
    for cuts in itertools.product([0,1],repeat=max(l-1,0)):
        b=[alpha[0]]
        for c,x in zip(cuts,alpha[1:]):
            if c: b[-1]+=x
            else: b.append(x)
        o[tuple(b)]=o.get(tuple(b),0)+(-1)**(l-len(b))
    return o
# power series in z with NSym coeffs: list indexed by z-degree, truncated at N
def smul(A,B,N):
    C=[{} for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1-i):
            if A[i] and B[j]: add(C[i+j],mul(A[i],B[j]))
    return C
def series(N):
    Psi=[{} for _ in range(N+1)]; Th=[{} for _ in range(N+1)]
    for n in range(N+1):
        e={(n,) if n>0 else ():1}
        (Psi if n%2==0 else Th)[n]=e
    # W = Psi^{-1} = sum (1-Psi)^r
    U=[{} for _ in range(N+1)]
    for n in range(2,N+1,2): U[n]={(n,):-1}
    W=[{} for _ in range(N+1)]; W[0]={():1}
    P=[{} for _ in range(N+1)]; P[0]={():1}
    for r in range(1,N+1):
        P=smul(P,U,N)
        for n in range(N+1): add(W[n],P[n])
    return W,Th
K=int(sys.argv[1]) if len(sys.argv)>1 else 5
N=2*K
W,Th=series(N)
WT=smul(W,Th,N)
pw=[W]  # (WT)^o W
for o in range(1,N+1): pw.append(smul(WT,pw[-1],N))
bad=0;tot=0
for k in range(1,K+1):
    d=2*k; Rs=R(tuple([2]*k))
    ranks=[]
    for i in range(d+1):
        imgs=[]
        for al in comps(i):
            lhs=Mperp(al,Rs) if i>0 else Rs
            o=sum(1 for x in al if x%2); l=len(al)
            rhs={kk:(-1)**(k+l)*v for kk,v in pw[o][d-i].items() if v}
            rhs={kk:v for kk,v in rhs.items() if v}
            tot+=1
            if lhs!=rhs: bad+=1
            imgs.append(lhs)
        keys=sorted({kk for im in imgs for kk in im})
        M=sympy.Matrix(len(imgs),len(keys),lambda a,b: imgs[a].get(keys[b],0))
        ranks.append(M.rank() if keys else 0)
    pred=[min(i//2,(d-i)//2)+1 for i in range(d+1)]
    print("k",k,"L",2*k-1,"ranks",ranks,"pred",pred,ranks==pred)
print("identity checks",tot,"bad",bad)
