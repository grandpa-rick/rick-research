from q66 import *
def wordQC(els,n):
    e={(w,i):quasi(w,i,'e') for w in els for i in range(1,n)}
    f={(w,i):quasi(w,i,'f') for w in els for i in range(1,n)}
    eps={(w,i):qstr(w,i)[0] for w in els for i in range(1,n)}
    phi={(w,i):qstr(w,i)[1] for w in els for i in range(1,n)}
    wt={w:tuple(w.count(j) for j in range(1,n+1)) for w in els}
    return QC(list(els),n,wt,e,f,eps,phi)
def comps(Q):
    seen=set();out=[]
    for x in Q.els:
        if x in seen: continue
        c=[x];seen.add(x);k=0
        while k<len(c):
            y=c[k];k+=1
            for i in range(1,Q.n):
                for z in (Q.e[y,i],Q.f[y,i]):
                    if z is not None and z not in seen: seen.add(z);c.append(z)
        out.append(c)
    return out
def canon(Q,c):
    hws=[x for x in c if all(Q.e[x,i] is None and Q.eps[x,i]!=INF and Q.eps[x,i]==0 or Q.e[x,i] is None and Q.eps[x,i]==INF for i in range(1,Q.n))]
    hws=[x for x in c if all(Q.e[x,i] is None for i in range(1,Q.n))]
    assert len(hws)==1, ("hw not unique",len(hws))
    idx={hws[0]:0};order=[hws[0]];k=0
    while k<len(order):
        y=order[k];k+=1
        for i in range(1,Q.n):
            z=Q.f[y,i]
            if z is not None and z not in idx: idx[z]=len(order);order.append(z)
    assert len(order)==len(c)
    return tuple((Q.wt[y],tuple((idx.get(Q.f[y,i]),idx.get(Q.e[y,i]),Q.eps[y,i],Q.phi[y,i]) for i in range(1,Q.n))) for y in order)
def comp_of_D(D,N):
    cuts=[0]+sorted(D)+[N]; return tuple(cuts[j+1]-cuts[j] for j in range(len(cuts)-1)) if N else ()
def std(w):
    order=sorted(range(len(w)),key=lambda p:(w[p],p)); s=[0]*len(w)
    for r,p in enumerate(order): s[p]=r+1
    return tuple(s)
def ides(s):
    pos={v:p for p,v in enumerate(s)}; return frozenset(k for k in range(1,len(s)) if pos[k+1]<pos[k])
# (i)
iso2comp={};bad=0;ncomp=0
for n in (1,2,3,4):
  for N in range(0,7 if n<=3 else 6):
    Q=wordQC(list(itertools.product(range(1,n+1),repeat=N)),n)
    for c in comps(Q):
        ncomp+=1
        sig={std(w) for w in c}; assert len(sig)==1
        a=comp_of_D(ides(next(iter(sig))),N); cf=(n,canon(Q,c))
        if cf in iso2comp and iso2comp[cf]!=a: bad+=1
        iso2comp.setdefault(cf,a)
        # hw weight = alpha padded
        assert cf[1][0][0]==tuple(list(a)+[0]*(n-len(a)))
byn=Counter(n for (n,_) in iso2comp)
from math import comb
print("(i) components",ncomp,"isoclasses per n",dict(byn),"expected #compositions N<=5, l<=n:",{n:sum(comb(N-1,k-1) for N in range(1,7 if n<=3 else 6) for k in range(1,min(n,N)+1))+1 for n in (1,2,3,4)},"collisions",bad)
canon_by={v:k for k,v in iso2comp.items()}
# (ii) abstract quasi-tensor of abstract components; decomposition vs F-product; commutativity up to iso
def component_QC(n,sigma,N):
    els=[w for w in itertools.product(range(1,n+1),repeat=N) if std(w)==sigma]; return wordQC(els,n)
n=3;fails=0;noncanon=0;tests=0
from itertools import permutations
perms=[p for N in range(0,4) for p in permutations(range(1,N+1))]
for s1 in perms:
  for s2 in perms:
    A=component_QC(n,s1,len(s1));B=component_QC(n,s2,len(s2))
    if not A.els or not B.els: continue
    T=qtensor(A,B);Tr=qtensor(B,A)
    d=Counter(iso2comp[(n,canon(T,c))] for c in comps(T)); dr=Counter(iso2comp[(n,canon(Tr,c))] for c in comps(Tr))
    # predicted: shuffles tau of positions, iDes(tau), keep l<=n
    m,k=len(s1),len(s2);pred=Counter()
    for P in itertools.combinations(range(m+k),m):
        Qs=[p for p in range(m+k) if p not in P]
        # tau: values; tau restricted to position-block standardises to s1, s2 -- all such tau = choose which values go to first block
        for V in itertools.combinations(range(1,m+k+1),m):
            pass
    # generate tau directly: tau in S_{m+k} with std(tau[:m])=s1, std(tau[m:])=s2
    for V in itertools.combinations(range(1,m+k+1),m):
        W=[v for v in range(1,m+k+1) if v not in V]
        tau=tuple(V[x-1] for x in s1)+tuple(W[x-1] for x in s2)
        a=comp_of_D(ides(tau),m+k)
        if len(a)<=n: pred[a]+=1
    tests+=1; fails+= d!=pred; noncanon+= d!=dr
print("(ii) n=3 pairs",tests,"decomposition != F-product prediction:",fails,"| C(x)''C' vs C'(x)''C non-iso:",noncanon)
