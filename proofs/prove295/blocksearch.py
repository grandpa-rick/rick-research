"""For each weight mu: L_mu = {a in A : a kills I_mu (cross images into M_mu) and O_mu (cross images out of M_mu)}.
Then a.1_mu in B.  excess(mu) = dim(L_mu|M_mu) - dim({a|M_mu : a in A, a|rest = 0}).  mod P."""
import sys, itertools, numpy as np
from flint import nmod_mat
from split import asc, move
P=2**31-1
def rk(rows,nc):
    if not rows: return 0
    return nmod_mat(len(rows),nc,[x%P for r in rows for x in r],P).rank()
def nullsp(rows,nc):
    if not rows: return np.eye(nc,dtype=np.int64)
    M=nmod_mat(len(rows),nc,[x%P for r in rows for x in r],P); X,k=M.nullspace()
    return np.array(X.entries(),dtype=np.int64).reshape(nc,nc)[:,:k]
def run(n,N,only=None):
    W=list(itertools.product(range(1,n+1),repeat=N)); widx={w:k for k,w in enumerate(W)}; d=len(W)
    wt=lambda w: tuple(w.count(c) for c in range(1,n+1))
    mus=sorted({wt(w) for w in W})
    gens=[np.array([widx[move(w,i)] for w in W]) for i in range(1,N)]
    seen={tuple(range(N)):np.arange(d)}; fr=[tuple(range(N))]
    while fr:
        nf=[]
        for p in fr:
            for i in range(N-1):
                if p[i]<p[i+1]:
                    q=list(p); q[i],q[i+1]=q[i+1],q[i]; q=tuple(q)
                    if q not in seen: seen[q]=gens[i][seen[p]]; nf.append(q)
        fr=nf
    F=np.array(list(seen.values()))   # K x d
    K=F.shape[0]
    def orbit(w):
        O={w}; st=[w]
        while st:
            v=st.pop()
            for i in range(1,N):
                u=move(v,i)
                if u not in O: O.add(u); st.append(u)
        return O
    Sv={mu:asc(tuple(c for c in range(1,n+1) for _ in range(mu[c-1]))) for mu in mus}
    wts={mu:[k for k,w in enumerate(W) if wt(w)==mu] for mu in mus}
    out={}
    for mu in mus:
        if only and mu not in only: continue
        # I_mu: words of M_mu in orbits of S-words w in M_mu with Asc(w) subset S(nu), nu!=mu
        I=set()
        for nu in mus:
            if nu==mu: continue
            for k in wts[mu]:
                if asc(W[k])<=Sv[nu]: I|=orbit(W[k])
        O=set()
        for nu in mus:
            if nu==mu: continue
            for k in wts[nu]:
                if asc(W[k])<=Sv[mu]: O|=orbit(W[k])
        # equations on c (K coeffs): for each word y in I|O and each target t: sum_{k: F[k,y]=t} c_k = 0
        rows=[]
        for y in [widx[w] for w in I|O]:
            col=F[:,y]
            for t in np.unique(col):
                r=[0]*K
                for k in np.nonzero(col==t)[0]: r[k]=1
                rows.append(r)
        Ncoef=nullsp(rows,K)      # K x m
        Mu=wts[mu]
        # restriction to M_mu: matrix entries (t,y) for y in Mu: vector indexed by (y, F[k,y])
        def restr(cmat, ys):   # cmat: K x m -> rows m vectors over (y,t)
            keys={}; vecs=np.zeros((cmat.shape[1], 0),dtype=np.int64)
            cols=[]
            for y in ys:
                col=F[:,y]
                for t in np.unique(col):
                    cols.append(((cmat[col==t]).sum(axis=0))%P)
            return np.array(cols).T if cols else np.zeros((cmat.shape[1],0),dtype=np.int64)
        R1=restr(Ncoef,Mu); r1=rk(R1.tolist(),R1.shape[1]) if R1.size else 0
        rest=[k for k in range(d) if k not in set(Mu)]
        # a|rest = 0 : equations over all words outside M_mu
        rows2=[]
        for y in rest:
            col=F[:,y]
            for t in np.unique(col):
                r=[0]*K
                for k in np.nonzero(col==t)[0]: r[k]=1
                rows2.append(r)
        N2=nullsp(rows2,K); R2=restr(N2,Mu); r2=rk(R2.tolist(),R2.shape[1]) if R2.size else 0
        if r1!=r2: print(n,N,'weight',mu,'|I|',len(I),'|O|',len(O),'dim L|mu',r1,'dim A_only_mu',r2,'EXCESS',r1-r2,flush=True)
        out[mu]=r1-r2
    print(n,N,'total single-weight excess',sum(out.values()))
if __name__=='__main__':
    n,N=map(int,sys.argv[1:3]); run(n,N)
