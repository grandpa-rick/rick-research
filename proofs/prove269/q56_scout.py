# Q56 scout (PROVE 269 compute agent). Grade: at most "computed".
# Question: on non-Boolean (3.6) pairs rho ⊆ lam, is the (3.6) coefficient a specialisation of a parabolic KL quantity?
# (3.6) coefficient, from printed Rem 4.20/4.22 of the LG/OG draft (main.tex l.1386, 1330):
#   sum_{p in D_{z_rho,z_lam}} e^{-p(1)} = (-1)^{|theta|} A_{lam,rho},  theta = lam/rho,
#   #D = N := #{mu : rho ⊆ mu ⊆ lam, mu/rho antichain, lam/mu antichain without diagonal box}  (= #V-maps).
#   Non-equivariant coefficient used here: c = (-1)^{|theta|} N  (i.e. A_{lam,rho} at e^{wt} -> 1).
#   Also V(t) := sum_mu t^{|lam/mu|} (t marks the 'o' boxes); c = (-1)^{|theta|} V(1).
# KL machinery: parabolic R/P by Deodhar's recursion copied from proofs/prove268/q55.py (parKL), with R returned.
#   xparam 'q'  : u=q  convention; cross-checked there = alternating sum  sum_{u in W_J} (-1)^{l(u)} P_{sigma u,tau}.
#   xparam '-1' : u=-1 convention; cross-checked there = P_{sigma w_J, tau w_J}.
#   Pairs indexed by the Bruhat interval [z_lam, z_rho] (z-indexing, the (3.6) one); w-indexing [w_rho,w_lam] also reported.
import numpy as np, itertools, sys, random, time
MMAX=int(sys.argv[1]) if len(sys.argv)>1 else 4   # read before exec (q55.py resets sys.argv)
src=open('/home/agent/projects/proofs/prove268/q55.py').read()
src=src.replace("'../prove266/check.py'","'/home/agent/projects/proofs/prove266/check.py'")
exec(src.split('for m in range(1,6):')[0])

def parKL2(Wj,leq,lnf,act,gens,xparam):
    order=sorted(Wj,key=lnf); R={}
    fac = (0,1) if xparam=='-1' else (-1,)
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
            d=lnf(tau)-lnf(sig); p=neg(tuple(F[:(d-1)//2+1])) if F else ()
            p=list(p)
            while p and p[-1]==0: p.pop()
            P[(sig,tau)]=tuple(p)
    return R,P
ev=lambda p,x: sum(c*x**i for i,c in enumerate(p))
lt=lambda x,y: x!=y and x[0]<=y[0] and x[1]<=y[1]
def corners(X):  # maximal boxes of the skew
    return sum(1 for x in X if not any(lt(x,y) for y in X))

rows=[]
for m in range(1,MMAX+1):
    t0=time.time()
    G=group(Cgens(m)); N_=G['N']; J=list(range(m-1)); om=np.ones(m); ln=G['ln']
    Wmin=[a for a in range(N_) if all(ln[G['R'][a][j]]>ln[a] for j in J)]
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
    KL={x:parKL2(Wmin,leqJ,lambda a:ln[a],act,range(m),x) for x in ['-1','q']}
    Pf=fullKL(G) if m<=4 else None
    for rho in shapes:
        for lam in shapes:
            if not D(rho)<=D(lam): continue
            th=D(lam)-D(rho)
            if anti(th): continue                     # Boolean pairs excluded
            mus=[mu for mu in shapes if D(rho)<=D(mu)<=D(lam) and anti(D(mu)-D(rho)) and anti(D(lam)-D(mu)) and not any(a==b for a,b in D(lam)-D(mu))]
            if not mus: continue                      # not in (3.6) support
            Vt=[0]*(len(th)+1)
            for mu in mus: Vt[len(D(lam)-D(mu))]+=1
            while Vt and Vt[-1]==0: Vt.pop()
            lo,hi=z[lam],z[rho]
            r=dict(m=m,rho=rho,lam=lam,th=len(th),corners=corners(th),dl=ln[hi]-ln[lo],N=len(mus),c=(-1)**len(th)*len(mus),V=tuple(Vt))
            for x,tag in [('q','q'),('-1','m1')]:
                R,P=KL[x]
                r['P'+tag+'z']=P[(lo,hi)]; r['R'+tag+'z']=R[(lo,hi)]
                r['P'+tag+'w']=P[(w[rho],w[lam])]; r['R'+tag+'w']=R[(w[rho],w[lam])]
            r['Pfull_z']=Pf.get((lo,hi),()) if Pf else None
            rows.append(r)
    print(f"m={m} done {time.time()-t0:.1f}s, pairs so far {len(rows)}",file=sys.stderr)

# candidate columns
cands={}
for tag in ['q','m1']:
    for ix in ['z','w']:
        for kind in ['P','R']:
            for x in [1,-1]:
                cands[f"{kind}^{{J,{'q' if tag=='q' else '-1'}}}[{ix}]({x})"]=[ev(r[kind+tag+ix],x) for r in rows]
if all(r['Pfull_z'] is not None for r in rows):
    for x in [1,-1]: cands[f"P_full[z]({x})"]=[ev(r['Pfull_z'],x) for r in rows]
c=[r['c'] for r in rows]; Nn=[r['N'] for r in rows]; dl=[r['dl'] for r in rows]
rels={'c==X':lambda c,X,d: c==X,'c==-X':lambda c,X,d: c==-X,'c==(-1)^dl X':lambda c,X,d: c==(-1)**d*X,'|c|==|X|':lambda c,X,d: abs(c)==abs(X)}
def score(col):
    return {k:sum(f(ci,Xi,di) for ci,Xi,di in zip(c,col,dl)) for k,f in rels.items()}
print("\n# per-pair table (non-Boolean (3.6) pairs)")
print("m | rho | lam | |th| | corners | dl | N | c | V(t) | P^{J,q}[z] | P^{J,-1}[z] | R^{J,q}[z] | R^{J,-1}[z] | P^{J,q}[w] | P^{J,-1}[w]")
for r in rows:
    print(r['m'],r['rho'],r['lam'],r['th'],r['corners'],r['dl'],r['N'],r['c'],r['V'],r['Pqz'],r['Pm1z'],r['Rqz'],r['Rm1z'],r['Pqw'],r['Pm1w'],sep=' | ')
print(f"\n# relation scores, out of {len(rows)} pairs")
random.seed(269)
for name,col in cands.items():
    s=score(col); best=max(s.values())
    perm=col[:]; random.shuffle(perm); sp=score(perm)
    print(f"{name:28s} {s}   | shuffled control: {sp}")
# polynomial-level test: V(t) vs P polynomials (as tuples), up to sign
print("\n# polynomial equalities V(t) vs candidate polynomial (exact tuple, or negated):")
for key in ['Pqz','Pm1z','Pqw','Pm1w','Pfull_z']:
    if any(r[key] is None for r in rows): continue
    eq=sum(r['V']==r[key] or r['V']==neg(r[key]) for r in rows)
    print(key, eq, "/", len(rows))
# structural: N vs corners / V(t) shape
def iso_off(r):
    th=D(r['lam'])-D(r['rho']); return sum(1 for x in th if x[0]!=x[1] and not any(lt(x,y) or lt(y,x) for y in th))
print('\n# N == 2^{#isolated off-diagonal boxes of theta}:',sum(r['N']==2**iso_off(r) for r in rows),'/',len(rows))
print('# pairs with N>1:',[(r['m'],r['rho'],r['lam'],r['N'],r['Pm1z'],r['Pm1w']) for r in rows if r['N']>1])
print("\n# N == 2^{#isolated? } check: N vs 2^corners:",sum(r['N']==2**r['corners'] for r in rows),"/",len(rows))
