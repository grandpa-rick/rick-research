# Independent check of E6 node-4 candidate counterexample: full-W R-polynomials on w(rho) vectors -> P_{x,y}.
import sys, functools
exec(open('q_cominuscule_scout.py').read().split('def boolean')[0])
sys.setrecursionlimit(100000)
C=Cox(cartan('E',6)); J={0,1,2,4,5}; lam,els=quotient(C,J)
L=list(els); wr=[els[m][0] for m in L]; wd=[els[m][1] for m in L]; ln=[els[m][2] for m in L]; N=len(L)
ix={m:i for i,m in enumerate(L)}
def word(a): return wd[a]
# find one candidate pair again (doubly stuck gap 3) quickly: restrict to y of small length
@functools.lru_cache(None)
def R(u,w):
    if w==C.rho: return (1,) if u==C.rho else ()
    s=next(i for i in range(C.n) if w[i]<0); sw=C.refl(s,w); su=C.refl(s,u)
    if u[s]<0: return R(su,sw)
    return padd(pmul((-1,1),R(u,sw)), psc(R(su,sw),1))
def KL(x,y,iv):
    # iv: list of w(rho) in [x,y]; P_{z,y} for all z in iv by inversion
    iv=sorted(iv,key=C.length,reverse=True); P={}
    for z in iv:
        if z==y: P[z]=(1,); continue
        F=()
        for w in iv:
            if w!=z and C.le(z,w): F=padd(F,pmul(R(z,w),P[w]))
        d=C.length(y)-C.length(z); p=[-c for c in F[:(d-1)//2+1]]
        while p and p[-1]==0: p.pop()
        P[z]=tuple(p)
    return P[x]
found=0
for y in sorted(range(N),key=lambda a:ln[a]):
    DLy=[i for i in range(6) if wr[y][i]<0]
    for x in range(N):
        if ln[y]-ln[x]!=3 or not C.le(wr[x],wr[y]): continue
        if not all(wr[x][i]<0 for i in DLy): continue
        iv=[wr[z] for z in range(N) if C.le(wr[x],wr[z]) and C.le(wr[z],wr[y])]
        # (d): no z in iv, j in J with z s_j <= y  (Prop 1 / G1 form)
        if any(C.le(C.apply_word(wd[ix_] + [j],C.rho),wr[y]) for ix_ in [ix[L[z]] for z in range(N) if wr[z] in iv] for j in J): continue
        if not all(C.le(wr[x],C.refl(s,wr[y])) for s in DLy): continue
        # full W interval check: enumerate all w in W with x<=w<=y by BFS down from y
        full=set([wr[y]]); fr=[wr[y]]
        while fr:
            nf=[]
            for w in fr:
                # all u covered... use: elements <= y of length l-1 reachable via reflections; simpler: subwords
                pass
            fr=nf
        P=KL(wr[x],wr[y],iv)
        print('x=',wd[x],'y=',wd[y],'|iv|',len(iv),'P_{x,y} =',P); found+=1
        if found>=3: raise SystemExit
