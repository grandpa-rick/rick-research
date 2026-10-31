# Q55 (d): Boolean intervals of W^J (LG(m,2m)), (3.6) support, parabolic KL. Written from stated claims.
import numpy as np, itertools, math, sys
sys.argv=['x']; exec(open('../prove266/check.py').read().split('tot_bad=0')[0])
# ---- polys as tuples of ints (coeff of q^i)
def padd(a,b):
    n=max(len(a),len(b)); r=[0]*n
    for i,c in enumerate(a): r[i]+=c
    for i,c in enumerate(b): r[i]+=c
    while r and r[-1]==0: r.pop()
    return tuple(r)
def pmul(a,b):
    if not a or not b: return ()
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    while r and r[-1]==0: r.pop()
    return tuple(r)
def psc(a,k,c=1): return tuple([0]*k+[c*x for x in a]) if a else ()
neg=lambda a: tuple(-x for x in a)
def Cgens(m):
    g=[]
    for i in range(m-1):
        S=np.eye(m); S[[i,i+1]]=S[[i+1,i]]; g.append(S)
    S=np.eye(m); S[m-1,m-1]=-1; g.append(S); return g
def D(k): return frozenset((a,b) for a,p in enumerate(k) for b in range(a,a+p))
def anti(X): return not any(x!=y and x[0]<=y[0] and x[1]<=y[1] for x in X for y in X)
def boolean(elts,leq):
    # is the finite poset (with unique min) isomorphic to a Boolean lattice? via atoms
    mn=[x for x in elts if all(leq(x,y) for y in elts)]
    if len(mn)!=1: return False
    mn=mn[0]; others=[x for x in elts if x!=mn]
    atoms=[a for a in others if not any(b!=a and leq(b,a) for b in others)]
    S={x:frozenset(i for i,a in enumerate(atoms) if leq(a,x)) for x in elts}
    if len(set(S.values()))!=len(elts) or len(elts)!=2**len(atoms): return False
    return all(leq(x,y)==(S[x]<=S[y]) for x in elts for y in elts)
def fullKL(G):
    N=G['N']; ln=G['ln']; r=G['r']; L=G['L']
    order=sorted(range(N),key=lambda a:ln[a]); P={}; mu={}
    below=[[x for x in range(N) if le(G,x,w)] for w in range(N)]
    for w in order:
        if w==0: P[(0,0)]=(1,); continue
        s=next(i for i in range(r) if ln[L[w][i]]<ln[w]); v=L[w][s]
        zs=[z for z in below[v] if ln[L[z][s]]<ln[z] and mu.get((z,v),0)]
        for x in below[w]:
            c=1 if ln[L[x][s]]<ln[x] else 0
            sx=L[x][s]
            t=padd(psc(P.get((sx,v),()) ,1-c), psc(P.get((x,v),()),c))
            for z in zs:
                if le(G,x,z): t=padd(t,neg(psc(P[(x,z)],(ln[w]-ln[z])//2,mu[(z,v)])))
            P[(x,w)]=t
            d=ln[w]-ln[x]
            if d%2==1 and len(t)==(d-1)//2+1: mu[(x,w)]=t[-1]
    return P
def parKL(Wj,leq,lnf,act,gens,xparam):
    # act(s,sig) -> ('up',tau) | ('down',tau) | ('stay',None). xparam in {'-1','q'}
    order=sorted(Wj,key=lnf); R={}
    fac = (0,1) if xparam=='-1' else (-1,)     # q-1-x : x=-1 -> q ; x=q -> -1
    for tau in order:
        for sig in Wj:
            if not leq(sig,tau): continue
            if sig==tau: R[(sig,tau)]=(1,); continue
            s=next(i for i in gens if act(i,tau)[0]=='down'); st=act(s,tau)[1]
            k,ss=act(s,sig)
            if k=='down': R[(sig,tau)]=R.get((ss,st),())
            elif k=='up': R[(sig,tau)]=padd(pmul((-1,1),R.get((sig,st),())), psc(R.get((ss,st),()),1))
            else: R[(sig,tau)]=pmul(fac,R.get((sig,st),()))
    P={}
    for tau in order:
        for sig in sorted([s for s in Wj if leq(s,tau)],key=lnf,reverse=True):
            if sig==tau: P[(sig,tau)]=(1,); continue
            F=()
            for rho in Wj:
                if rho!=sig and leq(sig,rho) and leq(rho,tau): F=padd(F,pmul(R[(sig,rho)],P[(rho,tau)]))
            d=lnf(tau)-lnf(sig); P[(sig,tau)]=neg(tuple(F[:(d-1)//2+1])) if F else ()
            while P[(sig,tau)] and P[(sig,tau)][-1]==0: P[(sig,tau)]=P[(sig,tau)][:-1]
    return P
for m in range(1,6):
    G=group(Cgens(m)); N=G['N']; J=list(range(m-1)); om=np.ones(m); ln=G['ln']
    Wmin=[a for a in range(N) if all(ln[G['R'][a][j]]>ln[a] for j in J)]
    sv={tuple(np.round(G['els'][a]@om).astype(int)):a for a in Wmin}
    shapes=[tuple(sorted(c,reverse=True)) for k in range(m+1) for c in itertools.combinations(range(1,m+1),k)]
    v=lambda k: tuple(-1 if (m-i) in k else 1 for i in range(m))
    z={k:sv[tuple(-x for x in v(k))] for k in shapes}; w={k:sv[v(k)] for k in shapes}
    inv={a:k for k,a in w.items()}
    leqJ=lambda a,b: bool(le(G,a,b))
    def act(i,a):
        b=G['L'][a][i]
        if b in inv: return ('up' if ln[b]>ln[a] else 'down', b)
        return ('stay',None)
    PJ={x:parKL(Wmin,leqJ,lambda a:ln[a],act,range(m),x) for x in ['-1','q']}
    # cross-check vs full KL (m<=4)
    xc='skip'
    if m<=4:
        Pf=fullKL(G); WJ=[a for a in range(N) if all(i in J for i in [])]  # placeholder
        # W_J elements = coset of identity
        WJel=sorted(coset(G,0,J)); wJ=max(WJel,key=lambda a:ln[a])
        mulR=lambda a,u: G['idx'][G['key'](G['els'][a]@G['els'][u])]
        bad1=bad2=0
        for s in Wmin:
            for t in Wmin:
                if not leqJ(s,t): continue
                bad1+= PJ['-1'][(s,t)]!=Pf.get((mulR(s,wJ),mulR(t,wJ)),())
                alt=()
                for u in WJel:
                    su=mulR(s,u)
                    alt=padd(alt, psc(Pf.get((su,t),()),0,(-1)**ln[u]))
                bad2+= PJ['q'][(s,t)]!=alt
        xc=f"x=-1 vs P(sw_J,tw_J): {bad1} bad; x=q vs alt-sum: {bad2} bad"
    stats={}
    for rho in shapes:
        for kap in shapes:
            if not D(rho)<=D(kap): continue
            th=D(kap)-D(rho); A=anti(th)
            lo,hi=z[kap],z[rho]                      # z_kap <= z_rho
            IJ=[a for a in Wmin if le(G,lo,a) and le(G,a,hi)]
            BJ=boolean(IJ,leqJ)
            IW=[a for a in range(N) if le(G,lo,a) and le(G,a,hi)]
            BW=boolean(IW,leqJ)
            # (3.6) support: lambda with rho<=lambda<=kap, lam/rho antichain, kap/lam antichain no diagonal box
            nV=sum(1 for lam in shapes if D(rho)<=D(lam)<=D(kap) and anti(D(lam)-D(rho)) and anti(D(kap)-D(lam)) and not any(a==b for a,b in D(kap)-D(lam)))
            p1=PJ['-1'][(lo,hi)]==(1,); pq=PJ['q'][(lo,hi)]==(1,)
            p1w=PJ['-1'][(w[rho],w[kap])]==(1,); pqw=PJ['q'][(w[rho],w[kap])]==(1,)
            key=(A,BJ,BW,nV>0,p1,pq,p1w,pqw); stats[key]=stats.get(key,0)+1
    print(f"m={m} |W^J|={len(Wmin)} pairs={sum(stats.values())}  {xc}")
    print("   (antichain, Bool_WJ, Bool_W, in(3.6), P^-1[z]=1, P^q[z]=1, P^-1[w]=1, P^q[w]=1): count")
    for k in sorted(stats): print("   ",tuple(int(x) for x in k),stats[k])
    sys.stdout.flush()
