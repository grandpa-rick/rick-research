# End(Ind(C_I x C_J)) via Frobenius reciprocity: End = {v in M: pi_i v = eps_i v, i != a}, phi_v(T_w (x) 1) = pi_w v.
import itertools,sys,random,numpy as np,sympy as sp
from ind import ind_module
from modp import P, nullspace_modp
def comps_sets(m): return [frozenset(S) for r in range(m) for S in itertools.combinations(range(1,m),r)]
def comp(S,m):
    c=[];prev=0
    for s in sorted(S)+[m]: c.append(s-prev); prev=s
    return tuple(c)
proj=lambda c: len(set(c))==1 and (c[0]==1 or len(c)==1)
def redword(w):  # reduced word with pi_w = pi_{i1}...pi_{ik} applied right-to-left; build by bubble
    w=list(w); word=[]
    # find left descents repeatedly: w = s_i w' with l(w')<l(w)
    while True:
        inv={v:p for p,v in enumerate(w)}
        d=next((i for i in range(1,len(w)) if inv[i]>inv[i+1]),None)
        if d is None: break
        word.append(d); w=[d+1 if v==d else d if v==d+1 else v for v in w]
    return word  # w = s_{word[0]} s_{word[1]} ...
Nlo,Nhi=int(sys.argv[1]),int(sys.argv[2])
for N in range(Nlo,Nhi+1):
  res={'brick':0,'indec':0,'bad':[], 'endformula_bad':0,'n':0}
  for a in range(1,N):
    b=N-a
    for S1 in comps_sets(a):
      for S2 in comps_sets(b):
        I,J=comp(S1,a),comp(S2,b)
        if proj(I) and proj(J): continue
        D=set(S1)|{s+a for s in S2}
        reps,mats=ind_module([a,b],D); n=len(reps)
        G={i:np.array(A.tolist(),dtype=np.int64) for i,A in mats.items()}
        rows=[(G[i]-(1 if i in D else 0)*np.eye(n,dtype=np.int64))%P for i in G if i!=a]
        V=nullspace_modp(np.vstack(rows))
        e0=reps.index(tuple(range(1,N+1)))
        def phi(v):
            M=np.zeros((n,n),dtype=np.int64)
            for k,w in enumerate(reps):
                x=v.copy()
                for i in reversed(redword(w)): x=(G[i]@x)%P
                M[:,k]=x
            return M
        Phis=[phi(v) for v in V]
        random.seed(7); X=np.zeros((n,n),dtype=np.int64)
        for F in Phis: X=(X+random.randrange(P)*F)%P
        t=sp.symbols('t'); cp=sp.Poly(sp.Matrix(X.tolist()).charpoly(t).as_expr(),t,modulus=P)
        k=sp.quo(cp,sp.gcd(cp,cp.diff(t))).degree()
        # sanity: phi commutes
        assert all(((G[i]@F-F@G[i])%P==0).all() for F in Phis for i in G)
        # top/socle labels predicted: top {D+a, D}; socle: J-first concatenations
        Dsoc0={s for s in S2}|{s+b for s in S1}; socl={frozenset(Dsoc0),frozenset(Dsoc0|{b})}
        topl={frozenset(D),frozenset(D|{a})}
        ov=len(topl&socl)
        res['n']+=1
        if k==1: res['indec']+=1
        else: res['bad'].append((I,J,k))
        if len(V)==1: res['brick']+=1
        if len(V)!=1+ov: res['endformula_bad']+=1; print('endformula mismatch',I,J,len(V),ov)
  print(N,res,flush=True)
