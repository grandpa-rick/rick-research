from qc import *
import itertools
from collections import defaultdict
def std(w):
    idx=sorted(range(len(w)),key=lambda p:(w[p],p)); s=[0]*len(w)
    for r,p in enumerate(idx): s[p]=r+1
    return tuple(s)
def ides(s):
    pos={v:p for p,v in enumerate(s)}; return frozenset(k for k in range(1,len(s)) if pos[k+1]<pos[k])
def comps(N,n,ops):
    W=list(itertools.product(range(1,n+1),repeat=N)); par={w:w for w in W}
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for w in W:
        for i in ops:
            for op in 'ef':
                r=quasi(w,i,op)
                if r: par[f(w)]=f(r)
    C=defaultdict(list)
    for w in W: C[f(w)].append(w)
    return list(C.values())
def Fpoly(D,N,vars_):   # F_D in given ordered variable list: Counter of weight tuples
    out=Counter()
    for b in itertools.product(range(len(vars_)),repeat=N):
        if all(b[k]<=b[k+1] and (b[k]<b[k+1] if (k+1) in D else True) for k in range(N-1)):
            V=list(vars_); out[tuple(sorted(V[t] for t in b))]+=1
    return out
def wt(w,n): return tuple(sorted(c-1 for c in w))
ok=True
# 1. components = std classes, char = F_{iDes}
for N in range(1,6):
  for n in range(1,5):
    for C in comps(N,n,range(1,n)):
        S={std(w) for w in C}
        if len(S)!=1: ok=False; print('comp not one std class',N,n)
        s=S.pop()
        allw=[w for w in itertools.product(range(1,n+1),repeat=N) if std(w)==s]
        if sorted(allw)!=sorted(C): ok=False; print('std class not connected',N,n,s)
        if Counter(wt(w,n) for w in C)!=Fpoly(ides(s),N,range(n)): ok=False;print('char fail')
print('1. components=std classes, char=F_iDes :',ok)
# 2. tensor shadow: {uv: std u=s1, std v=s2} = union of std classes tau with tau|front~s1, tau|back~s2 ; multiplicities
def shuffles(s1,s2):
    m,k=len(s1),len(s2); out=[]
    for tau in itertools.permutations(range(1,m+k+1)):
        if std(tau[:m])==s1 and std(tau[m:])==s2: out.append(tau)
    return out
ok=True
for m in range(1,4):
  for k in range(1,4):
    for s1 in itertools.permutations(range(1,m+1)):
      for s2 in itertools.permutations(range(1,k+1)):
        T=set(shuffles(s1,s2)); n=3
        U={u+v for u in itertools.product(range(1,n+1),repeat=m) if std(u)==s1 for v in itertools.product(range(1,n+1),repeat=k) if std(v)==s2}
        Wt={w for w in itertools.product(range(1,n+1),repeat=m+k) if std(w) in T}
        if U!=Wt: ok=False
print('2. C_s1 (x) C_s2 = disjoint union of C_tau, tau in shifted shuffle :',ok)
# 3. counterexample: multiplicity of F_{21} (D={2}) in F_1 F_2 vs coeff of F_1(x)F_2 in Delta F_{21}
T=shuffles((1,),(1,2)); print('3. F_1*F_2 components iDes:',sorted(tuple(sorted(ides(t))) for t in T))
def decon(D,N):   # Delta F_D as list of (k, D1, D2)
    return [(k,frozenset(d for d in D if d<k),frozenset(d-k for d in D if d>k)) for k in range(N+1)]
print('   Delta F_{21} terms (k,D1,D2):',[(k,sorted(a),sorted(b)) for k,a,b in decon({2},3)],' -> no (1,{},{}) i.e. F_1(x)F_2(y)')
# 4. Levi branching = deconcatenation: restrict ops to i != a; component chars in (x_1..x_a ; x_{a+1}..x_n)
ok=True;cnt=0
for N in range(1,5):
  for n in range(2,5):
    for a in range(1,n):
      for C in comps(N,n,range(1,n)):
        s=std(C[0]); D=ides(s)
        sub=[c for c in comps(N,n,[i for i in range(1,n) if i!=a]) if std(c[0])==s]
        # predicted: for k with filling nonempty: char F_{D1}(x_<=a) F_{D2}(x_>a)
        pred=Counter()
        for k,D1,D2 in decon(D,N):
            A=Fpoly(D1,k,range(a)); B=Fpoly(D2,N-k,range(a,n))
            for x,cx in A.items():
                for y,cy in B.items(): pred[tuple(sorted(x+y))]+=cx*cy
        got=Counter(wt(w,n) for c in sub for w in c)
        # also each subcomponent has constant k = #letters<=a
        ks=[len({sum(1 for ch in w if ch<=a) for w in c}) for c in sub]
        if got!=pred or any(x!=1 for x in ks): ok=False
        cnt+=1
print('4. Levi(a) branching of each component = Delta F_alpha, cases:',cnt,ok)
# 5. literal (b): position split |u|=m, sum x^{wt u} y^{wt v} vs Delta_{m,k} F_alpha(x;y) (both in n vars each)
w_=[(2,1),(1,2)]; n=2
for s in [(2,1),(1,2)]:
    C=[w for w in itertools.product(range(1,n+1),repeat=2) if std(w)==s]
    lit=Counter((wt(w[:1],n),wt(w[1:],n)) for w in C)
    D=ides(s); pred=Counter()
    for k,D1,D2 in decon(D,2):
        if k!=1: continue
        for x,cx in Fpoly(D1,1,range(n)).items():
            for y,cy in Fpoly(D2,1,range(n)).items(): pred[(x,y)]+=cx*cy
    print('5. std',s,'literal position-split',dict(lit),' vs Delta_{1,1}',dict(pred))
