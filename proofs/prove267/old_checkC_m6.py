# Type C_m translation (Lemma A) from the stated claim, m<=5.
import numpy as np, itertools, sys
sys.argv=['x']; exec(open('/home/agent/projects/proofs/prove266/check.py').read().split('tot_bad=0')[0])
def Cgens(m):
    g=[]
    for i in range(m-1):
        S=np.eye(m); S[[i,i+1]]=S[[i+1,i]]; g.append(S)
    S=np.eye(m); S[m-1,m-1]=-1; g.append(S); return g
def D(k): return {(a,b) for a,p in enumerate(k) for b in range(a,a+p)}
def anti(X): return not any(x!=y and x[0]<=y[0] and x[1]<=y[1] for x in X for y in X)
for m in range(6,7):
    G=group(Cgens(m)); N=G['N']; assert N==2**m*math.factorial(m)
    assert bin(G['low'][max(range(N),key=lambda a:G['ln'][a])]).count('1')==N
    J=list(range(m-1)); om=np.ones(m)
    Wmin=[a for a in range(N) if all(G['ln'][G['R'][a][j]]>G['ln'][a] for j in J)]
    sv={tuple(np.round(G['els'][a]@om).astype(int)):a for a in Wmin}
    shapes=[tuple(sorted(c,reverse=True)) for k in range(m+1) for c in itertools.combinations(range(1,m+1),k)]
    v=lambda k: tuple(-1 if (m-i) in k else 1 for i in range(m))   # position i (0-idx) <-> part m-i
    w={k:sv[v(k)] for k in shapes}; z={k:sv[tuple(-x for x in v(k))] for k in shapes}
    comp=lambda k: tuple(sorted(set(range(1,m+1))-set(k),reverse=True))
    rot=lambda X:{(m-1-b,m-1-a) for a,b in X}
    stair={(a,b) for a in range(m) for b in range(a,m)}
    for k in shapes:
        assert z[k]==w[comp(k)] and D(comp(k))==rot(stair-D(k)) and G['ln'][w[k]]==sum(k)
    E=lambda zz,ww:[j for j in J if le(G,G['R'][zz][j],ww)]
    cnt=bad=c1=c2=bk=tot=0
    for rho in shapes:
        for lam in shapes:
            if not D(rho)<=D(lam): continue
            assert le(G,z[lam],z[rho]) and le(G,w[rho],w[lam])
            A=anti(D(lam)-D(rho)); e=(E(z[lam],z[rho])==[])
            cnt+=e; bad+=(e!=A); tot=locals().get("tot",0)+1
            bk+=((E(w[rho],w[lam])==[])!=A)              # key step in w-indexing (eta=rho,nu=lam)
            c1+=((m>1 and not le(G,G['R'][z[lam]][m-2],z[rho]))!=A)   # control: only s_{m-1}
            rows=lambda X:len({a for a,b in X})==len(X)
            c2+=(e!=rows(D(lam)-D(rho)))               # control: wrong combinatorics
    # Bruhat on W^P = inclusion
    for a in shapes:
        for b in shapes: assert bool(le(G,w[a],w[b]))==(D(a)<=D(b))
    print(f"m={m}: pairs {tot}, E-empty count {cnt}, Lemma-A failures {bad}, key-step failures {bk}; controls: single s_(m-1) {c1}, row-strip {c2}")
