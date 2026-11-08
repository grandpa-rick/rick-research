"""Crown U' separator search: arcs (mu on non-simple pairs) vs local crystal/dual-equivalence data, S_n small.
Method A: own KL recursion using RIGHT multiplication (w = v s), Bruhat via rank-matrix test.
Local data = WL colour refinement of the Knuth/dual-Knuth graph (pure combinatorics, mu-free)."""
import itertools,sys,json,collections
n=int(sys.argv[1]); K=int(sys.argv[2]) if len(sys.argv)>2 else 6
def length(w): return sum(1 for i in range(n) for j in range(i+1,n) if w[i]>w[j])
def inv(w):
    r=[0]*n
    for i,a in enumerate(w): r[a-1]=i+1
    return tuple(r)
def Rdes(w): return frozenset(i for i in range(1,n) if w[i-1]>w[i])
def Ldes(w): return Rdes(inv(w))
def rmul(w,i): w=list(w); w[i-1],w[i]=w[i],w[i-1]; return tuple(w)   # w s_i
def leq(u,w):
    for k in range(1,n):
        a=sorted(u[:k]); b=sorted(w[:k])
        if any(p>q for p,q in zip(a,b)): return False
    return True
def rsk(w):
    P=[];Q=[]
    for k,a in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([a]);Q.append([k]);break
            row=P[r]; j=next((j for j,b in enumerate(row) if b>a),None)
            if j is None: row.append(a);Q[r].append(k);break
            row[j],a=a,row[j]; r+=1
    return tuple(map(tuple,P)),tuple(map(tuple,Q))
W=sorted(itertools.permutations(range(1,n+1)),key=lambda w:(length(w),w)); L={w:length(w) for w in W}
below={w:[u for u in W if L[u]<=L[w] and leq(u,w)] for w in W}
P={};mu={}
def add(r,p,sh,c):
    if len(r)<len(p)+sh: r.extend([0]*(len(p)+sh-len(r)))
    for k,v in enumerate(p): r[k+sh]+=c*v
for w in W:
    if L[w]==0: P[(w,w)]=(1,);continue
    s=next(i for i in sorted(Rdes(w))); v=rmul(w,s)
    zs=[z for z in below[v] if z!=v and s in Rdes(z) and mu.get((z,v),0)]
    for u in below[w]:
        if u==w: P[(u,w)]=(1,);continue
        us=rmul(u,s); c=1 if s in Rdes(u) else 0; r=[0]
        if (us,v) in P: add(r,P[(us,v)],1-c,1)
        if (u,v) in P: add(r,P[(u,v)],c,1)
        for z in zs:
            if (u,z) in P: add(r,P[(u,z)],(L[w]-L[z])//2,-mu[(z,v)])
        while len(r)>1 and r[-1]==0: r.pop()
        P[(u,w)]=tuple(r); d=L[w]-L[u]
        if d%2: mu[(u,w)]=r[(d-1)//2] if len(r)>(d-1)//2 else 0
# ---- Knuth / dual Knuth graph (mu-free) ----
def knuth_nbrs(w):
    out=[]
    for i in range(1,n-1):  # positions i-1,i,i+1 (0-based i-1..i+1)
        a,b,c=w[i-1],w[i],w[i+1]
        if b<a<c or c<a<b: out.append(('K',i,rmul(w,i)))      # swap pos i,i+1 (1-based i, i+1) ... witness left
        if a<c<b or b<c<a: out.append(('K',i+1,rmul(w,i+1)))
    return out
def dual_nbrs(w):
    return [('D',lab,inv(x)) for _,lab,x in knuth_nbrs(inv(w))]
NB={w:[(t,lab,x) for t,lab,x in knuth_nbrs(w)+dual_nbrs(w)] for w in W}
RS={w:rsk(w) for w in W}
shape={w:tuple(len(r) for r in RS[w][0]) for w in W}
def wl(labelled):
    col={w:(shape[w],tuple(sorted(Ldes(w))),tuple(sorted(Rdes(w)))) for w in W}
    hist=[col]
    for k in range(K):
        new={w:(col[w],tuple(sorted((t,lab if labelled else 0,col[x]) for t,lab,x in NB[w]))) for w in W}
        # compress
        ids={};c2={}
        for w in W: c2[w]=ids.setdefault(new[w],len(ids))
        col=c2; hist.append(col)
    return hist
# arc candidates
arcs=[]
for (u,w),m in mu.items():
    d=L[w]-L[u]
    if d>=3 and Ldes(w)<=Ldes(u) and Rdes(w)<=Rdes(u) and (Ldes(w),Rdes(w))!=(Ldes(u),Rdes(u)):
        arcs.append((u,w,m))
print(f"S_{n}: pairs {len(P)}, arc candidates {len(arcs)}, mu!=0 among them {sum(1 for a in arcs if a[2])}, mu values {collections.Counter(a[2] for a in arcs)}")
def rel(u,w):
    return (RS[u][0]==RS[w][0], RS[u][1]==RS[w][1], shape[u]==shape[w])
res={}
def window(u,w):
    # Dynkin-local data: indices where descents of u,w differ, closed neighbourhood, translated to start at 0
    A=(Ldes(u)^Ldes(w))|(Rdes(u)^Rdes(w))
    N=sorted(set(j for i in A for j in (i-1,i,i+1) if 1<=j<n)); m=N[0]
    f=lambda S:tuple(sorted(i-m for i in S if i in N))
    return (tuple(i-m for i in N),f(Ldes(u)),f(Rdes(u)),f(Ldes(w)),f(Rdes(w)))
for name,key in (('T0 window-local descents+d',lambda u,w:(window(u,w),L[w]-L[u])),
                 ('T0s window+shapes',lambda u,w:(window(u,w),L[w]-L[u],shape[u],shape[w],rel(u,w))),
                 ('T1 full descents+d',lambda u,w:(Ldes(u),Rdes(u),Ldes(w),Rdes(w),L[w]-L[u]))):
    groups=collections.defaultdict(list)
    for u,w,m in arcs: groups[key(u,w)].append((u,w,m))
    bad=[g for g in groups.values() if len(set(m for _,_,m in g))>1]
    print(f" {name}: data-classes {len(groups)}, separating classes {len(bad)}")
    if bad:
        g=min(bad,key=lambda g:min(L[w]-L[u] for u,w,_ in g))
        a=next(t for t in g if t[2]==0); b=next(t for t in g if t[2]!=0)
        res[(name,0)]=(a,b); print("   example:",a,b,key(a[0],a[1]))
for labelled in (False,True):
    hist=wl(labelled)
    for k,col in enumerate(hist):
        ncol=len(set(col.values()))
        groups=collections.defaultdict(list)
        for u,w,m in arcs: groups[(col[u],col[w],L[w]-L[u],rel(u,w))].append((u,w,m))
        bad=[g for g in groups.values() if len(set(m for _,_,m in g))>1]
        print(f" labelled={labelled} radius={k}: colours {ncol}, data-classes {len(groups)}, separating classes {len(bad)}")
        if bad:
            g=min(bad,key=lambda g:(min(L[w]-L[u] for u,w,_ in g)))
            a=next(t for t in g if t[2]==0) if any(t[2]==0 for t in g) else g[0]; b=next(t for t in g if t[2]!=a[2])
            res[(labelled,k)]=(a,b)
            print("   example:",a,b)
json.dump({f"{l}_{k}":[[list(a[0]),list(a[1]),a[2]],[list(b[0]),list(b[1]),b[2]]] for (l,k),(a,b) in res.items()},open(f"/home/agent/projects/proofs/wake284/seps_S{n}.json","w"))
