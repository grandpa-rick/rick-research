# PROVE 289: check the intermediate claims of the induction proof of Q72(i).
# Word model: basis = subsets A of [N] (|A|=a) <-> words x_1..x_N in {A,B}; pi^2=pi convention, chi(p)=[p in D].
import itertools,sys,numpy as np
sys.path.insert(0,'/home/agent/projects/proofs/wake288/q4scope')
from modp import P,nullspace_modp
def words(n,k):  # words length n with k B's
    return [tuple('B' if j in S else 'A' for j in range(n)) for S in itertools.combinations(range(n),k)]
def module(nA,nB,DI,DJ):
    """Ind_{H_nA x H_nB}(C_DI x C_DJ) in the word model. DI subset [1,nA-1], DJ subset [1,nB-1]."""
    n=nA+nB; W=words(n,nB); idx={w:t for t,w in enumerate(W)}; G={}
    for i in range(1,n):
        M=np.zeros((len(W),len(W)),dtype=np.int64)
        for w,t in idx.items():
            x,y=w[i-1],w[i]
            if x=='A' and y=='B': M[idx[w[:i-1]+('B','A')+w[i+1:]],t]=1
            elif x=='B' and y=='A': M[t,t]=1
            elif x=='A':
                p=w[:i].count('A'); M[t,t]=1 if p in DI else 0
            else:
                q=w[:i].count('B'); M[t,t]=1 if q in DJ else 0
        G[i]=M
    return W,G
def check_rel(G):
    for i in G:
        assert (G[i]@G[i]==G[i]).all()
        if i+1 in G: assert (G[i]@G[i+1]@G[i]==G[i+1]@G[i]@G[i+1]).all()
def eig(G,chi,skip=None):
    n=G[1].shape[0] if G else 1
    rows=[(G[i]-chi(i)*np.eye(n,dtype=np.int64))%P for i in G if i!=skip]
    if not rows: return [np.eye(n,dtype=np.int64)[0]]
    return nullspace_modp(np.vstack(rows))
def sets(m): return [frozenset(S) for r in range(m) for S in itertools.combinations(range(1,m),r)]
proj=lambda D,m: len(D)==0 or len(D)==m-1
def run(i,D):  # length of run of D ending at i (i,i-1,... in D)
    r=0
    while i-r in D: r+=1
    return r
bad=0;tot=0
for N in range(2,int(sys.argv[1])+1):
  for a in range(1,N):
    b=N-a
    for DI in sets(a):
      for DJ in sets(b):
        D=set(DI)|{a+q for q in DJ}; Z2=D|{a}
        W,G=module(a,b,DI,DJ); check_rel(G); n=len(W)
        chi=lambda i: 1 if i in D else 0
        E=eig(G,chi,skip=a)
        e0=W.index(tuple('A'*a+'B'*b))
        rp=run(a-1,DI); sp_=0
        while sp_+1 in DJ: sp_+=1
        al,be=a-rp,a+sp_
        f2=np.array([1 if all(c=='A' for c in w[:al-1]) and all(c=='B' for c in w[be+1:]) else 0 for w in W],dtype=np.int64)
        f1=np.zeros(n,dtype=np.int64); f1[e0]=1
        # claim: f2 is a module map to C_{Z2}, f1 to C_D
        for i in G:
            assert ((f2@G[i]-(1 if i in Z2 else 0)*f2)%P==0).all(), ('f2',a,DI,DJ,i)
            assert ((f1@G[i]-(1 if i in D else 0)*f1)%P==0).all(), ('f1',a,DI,DJ,i)
        sep=any(((f2-f1)@u)%P for u in E)   # decomposable iff sep
        bp=proj(DI,a) and proj(DJ,b)
        # per-k criterion via the small modules L_k, R_k
        crit=False
        for k in range(1,min(a,b)+1):
            DI1={p for p in DI if p<a-k}; DJ1={q for q in DJ if q<k}
            DI2={p-(a-k) for p in DI if p>a-k}; DJ2={q-k for q in DJ if q>k}
            WL,GL=module(a-k,k,DI1,DJ1); WR,GR=module(k,b-k,DI2,DJ2)
            UL=eig(GL,lambda i:1 if i in DI else 0); UR=eig(GR,lambda i:1 if i in DJ else 0)
            lamL=np.array([1 if all(c=='A' for c in w[:al-1]) else 0 for w in WL]); lamR=np.array([1 if all(c=='B' for c in w[be+1-a:]) else 0 for w in WR])
            if any((lamL@u)%P for u in UL) and any((lamR@u)%P for u in UR): crit=True
        tot+=1
        if not (sep==bp==crit): bad+=1; print('MISMATCH',N,a,sorted(DI),sorted(DJ),sep,bp,crit)
  print(N,'cases',tot,'bad',bad,flush=True)
