"""Young-layer decider for mu(y,z) on concrete permutations (one-line, values 1..n).
Uses only: Layer Lemma (P_{v'u,vu}=P_{v',v}, left and right versions), product rule for mu in S_k x S_{n-k},
gap/incomparable/F1 endpoints. Recursion on factors; falls back to star search for small factors."""
import sys,json,random
sys.path.insert(0,'/home/agent/projects/proofs/prove281'); sys.path.insert(0,'.')
from cfg import rsk_inv, bru
def ln(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def Ld(w):
    pos={a:k for k,a in enumerate(w)}; return {i for i in range(1,len(w)) if pos[i+1]<pos[i]}
def Rd(w): return {i for i in range(1,len(w)) if w[i-1]>w[i]}
def std(seq):
    s=sorted(seq); r={v:i+1 for i,v in enumerate(s)}; return [r[v] for v in seq]
def endpoint(y,z):
    if y==z: return None
    if ln(y)>ln(z): y,z=z,y
    g=ln(z)-ln(y)
    if g%2==0: return 0
    if not bru(y,z): return 0
    if g==1: return 1
    # F1: s in L(z)\L(y) with z != s y  -> 0 ; also right version
    for s in Ld(z)-Ld(y):
        sy=[s+1 if a==s else s if a==s+1 else a for a in y]
        if sy!=z: return 0
    for s in Rd(z)-Rd(y):
        ys=y[:]; ys[s-1],ys[s]=ys[s],ys[s-1]
        if ys!=z: return 0
    return None
def factors(y,z):
    n=len(y)
    for k in range(1,n):
        # right layer: values in positions <=k
        if set(y[:k])==set(z[:k]):
            return ('R',k,(std(y[:k]),std(y[k:])),(std(z[:k]),std(z[k:])))
        py={v:i for i,v in enumerate(y)}; pz={v:i for i,v in enumerate(z)}
        if {py[v] for v in range(1,k+1)}=={pz[v] for v in range(1,k+1)}:
            a=[v for v in y if v<=k]; b=[v-k for v in y if v>k]; a2=[v for v in z if v<=k]; b2=[v-k for v in z if v>k]
            return ('L',k,(a,b),(a2,b2))
    return None
def decide(y,z,depth=0,trace=None):
    e=endpoint(y,z)
    if e is not None: 
        if trace is not None: trace.append(('end',len(y),e))
        return e
    f=factors(y,z)
    if f is None: return None
    side,k,(a,b),(a2,b2)=f
    if trace is not None: trace.append((side,k,len(y)))
    if a!=a2 and b!=b2: 
        if trace is not None: trace.append(('both-differ',))
        return 0
    if a==a2: return decide(b,b2,depth+1,trace)
    return decide(a,a2,depth+1,trace)
