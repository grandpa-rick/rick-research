# PROVE 271 -- Q58 separator: Littelmann a-chains (0<a<1) vs P^{J,q}=1 on (d)-pairs.
# W^J <-> orbit W.lam (lam dominant, stabiliser W_J), weights in fundamental-weight coords.
# Cover mu < s_b mu in W^J iff <mu,b^v> > 0 and l(s_b mu) = l(mu)+1; its BOND is <mu,b^v>.
# a-chain for (tau,sig) (Littelmann Invent. 116 §4): saturated chain tau=k0>...>ks=sig, a*bond_i in Z for all i.
# => exists a in (0,1) with an a-chain  <=>  some saturated chain has gcd(bonds) >= 2.
import sys, math, collections, functools
sys.path.insert(0,'..'); exec(open('../prove269/q_cominuscule_scout.py').read().split('def boolean')[0])

def posroots(A):
    n=len(A); res={}
    fr=[(tuple(int(i==j) for j in range(n)),tuple(int(i==j) for j in range(n))) for i in range(n)]
    for r in fr: res[r[0]]=r[1]
    while fr:
        nf=[]
        for b,c in fr:
            for i in range(n):
                p=sum(b[j]*A[i][j] for j in range(n))      # <b, a_i^v>
                q=sum(c[j]*A[j][i] for j in range(n))      # <a_i, b^v>
                nb=tuple(b[j]-(p if j==i else 0) for j in range(n)); nc=tuple(c[j]-(q if j==i else 0) for j in range(n))
                if all(x>=0 for x in nb) and any(nb) and nb not in res: res[nb]=nc; nf.append((nb,nc))
        fr=nf
    return list(res.items())   # (root in alpha coords, coroot in alpha^v coords)

def setup(t,n,lam):
    A=cartan(t,n); C=Cox(A); R=posroots(A)
    alpha=[tuple(A[k][j] for k in range(n)) for j in range(n)]
    def pair(mu,c): return sum(mu[i]*c[i] for i in range(n))
    def refl(mu,b,c):
        p=pair(mu,c); return tuple(mu[k]-p*sum(b[j]*alpha[j][k] for j in range(n)) for k in range(n)), p
    orb={lam:0}; fr=[lam]
    while fr:
        nf=[]
        for mu in fr:
            for i in range(n):
                if mu[i]>0:
                    nu=C.refl(i,mu)
                    if nu not in orb: orb[nu]=orb[mu]+1; nf.append(nu)
        fr=nf
    L=sorted(orb,key=lambda m:orb[m]); ix={m:i for i,m in enumerate(L)}; ln=[orb[m] for m in L]
    for m in L: assert ln[ix[m]]==sum(1 for b,c in R if pair(m,c)<0)   # length = #negative pairings
    up=[[] for _ in L]
    for a,m in enumerate(L):
        for b,c in R:
            nu,p=refl(m,b,c)
            if p>0 and ln[ix[nu]]==ln[a]+1: up[a].append((ix[nu],p))
    N=len(L); upb=[0]*N
    for a in reversed(range(N)):
        s=1<<a
        for v,_ in up[a]: s|=upb[v]
        upb[a]=s
    return dict(C=C,L=L,ix=ix,ln=ln,up=up,upb=upb,N=N,n=n,J={i for i in range(n) if lam[i]==0})

def gcds(S,a):   # for sig=a: dict node -> set of gcds of bond sequences over saturated chains a->node
    G={a:{0}}
    for v in sorted([u for u in range(S['N']) if (S['upb'][a]>>u)&1],key=lambda u:S['ln'][u]):
        for w,p in S['up'][v]:
            G.setdefault(w,set()).update(math.gcd(g,p) for g in G.get(v,()))
    return G

def dpairs(S):  # (d): [sig,tau]_W subset W^J  <=>  no z in [sig,tau]^J, j in J with z s_j <= tau (z s_j > z)
    C=S['C']; L=S['L']; n=S['n']; J=S['J']; N=S['N']; ln=S['ln']; upb=S['upb']
    # z s_j as w(rho)-vector: need words. Rebuild via quotient for words keyed by weight.
    lam=L[0]; _,els=quotient(C,J); wr=[els[m][0] for m in L]; wd=[els[m][1] for m in L]
    zt=[[C.apply_word(wd[z]+[j],C.rho) for j in J] for z in range(N)]
    out=[]
    for y in range(N):
        badz=0
        for z in range(N):
            if (upb[z]>>y)&1 and any(C.le(w,wr[y]) for w in zt[z]): badz|=1<<z
        for x in range(N):
            if not (upb[x]>>y)&1: continue
            iv=upb[x]&~0; ivs=0; m=upb[x]
            while m:
                lb=m&-m; z=lb.bit_length()-1; m^=lb
                if (upb[z]>>y)&1: ivs|=lb
            if not ivs&badz: out.append((x,y,ivs))
    return out

def parP(S,pairs):  # Deodhar P^{J,q} (u=q: s.sig notin W^J gives factor -1), restricted to (d)-sets
    L=S['L']; ix=S['ix']; ln=S['ln']; upb=S['upb']; n=S['n']; C=S['C']
    le=lambda a,b:(upb[a]>>b)&1
    @functools.lru_cache(None)
    def R(a,b):
        if a==b: return (1,)
        if not le(a,b): return ()
        tb=L[b]; s=next(i for i in range(n) if tb[i]<0); sb=ix[C.refl(s,tb)]; ta=L[a]
        if ta[s]<0: return R(ix[C.refl(s,ta)],sb)
        if ta[s]>0: return padd(pmul((-1,1),R(a,sb)),psc(R(ix[C.refl(s,ta)],sb),1))
        return neg(R(a,sb))
    byy=collections.defaultdict(list)
    for x,y,ivs in pairs: byy[y].append(x)
    P={}
    for y,xs in byy.items():
        Py={}
        for x in sorted(xs,key=lambda a:-ln[a]):
            if x==y: Py[x]=(1,); continue
            F=()
            for r in xs:
                if r!=x and le(x,r) and le(r,y): F=padd(F,pmul(R(x,r),Py[r]))
            d=ln[y]-ln[x]; p=list(neg(tuple(F[:(d-1)//2+1]))) if F else []
            while p and p[-1]==0: p.pop()
            Py[x]=tuple(p)
        for x in xs: P[(x,y)]=Py[x]
    return P

def run(t,n,lam,show=0):
    S=setup(t,n,lam); N=S['N']
    pr=dpairs(S); P=parP(S,pr)
    conf=collections.Counter(); ex=collections.defaultdict(list)
    Gc={}
    for x,y,_ in pr:
        if x==y: continue
        if x not in Gc: Gc[x]=gcds(S,x)
        gs=Gc[x][y]; A=max(gs)>=2
        g=S['ln'][y]-S['ln'][x]; key=(g,P[(x,y)]!=(1,),A)
        conf[key]+=1
        if len(ex[key])<2: ex[key].append((S['L'][x],S['L'][y],P[(x,y)],sorted(gs)))
    print(f'{t}{n} lam={lam} |W^J|={N} (d)-pairs(x<y)={sum(conf.values())}')
    print('  bonds present:',sorted({p for a in range(N) for _,p in S['up'][a]}))
    for k in sorted(conf): print('  gap %d  P!=1:%-5s A:%-5s  %d'%(k[0],k[1],k[2],conf[k]), ex[k][0] if show else '')
    return S,pr,P,conf
if __name__=='__main__':
    a=sys.argv[1:]
    if a: run(a[0],int(a[1]),tuple(int(c) for c in a[2].split(',')),show=1)
