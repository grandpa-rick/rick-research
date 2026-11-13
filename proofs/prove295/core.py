"""n=2 core: binary words, pi_i as index maps (convention I), weight blocks.
Matrices act on columns: (P_i)[f(x),x]=1.  Right action v.pi_i <-> column map."""
import itertools, numpy as np
from flint import nmod_mat
P=2**31-1
def words(N): return list(itertools.product([1,2],repeat=N))
def gens(N):
    W=words(N); idx={w:k for k,w in enumerate(W)}
    G=[]
    for i in range(N-1):
        G.append(np.array([idx[w[:i]+(w[i+1],w[i])+w[i+2:]] if w[i]<w[i+1] else idx[w] for w in W]))
    return W,idx,G
def mat(f):
    d=len(f); M=np.zeros((d,d),dtype=np.int64); M[f,np.arange(d)]=1; return M
def tomat(A):
    A=np.asarray(A,dtype=np.int64)%P
    return nmod_mat(A.shape[0],A.shape[1],[int(x) for x in A.ravel()],P)
def null(A):
    A=np.asarray(A); nc=A.shape[1]
    if A.shape[0]==0: return np.eye(nc,dtype=np.int64)
    X,k=tomat(A).nullspace()
    return np.array(X.entries(),dtype=np.int64).reshape(nc,nc)[:,:k].copy()
def rank(A):
    A=np.asarray(A)
    if A.size==0: return 0
    return tomat(A).rank()
def monoid(G):
    d=len(G[0]); I=tuple(range(d)); M={I:()}; fr=[I]
    while fr:
        nf=[]
        for f in fr:
            for i,g in enumerate(G):
                h=tuple(g[list(f)])   # apply f then g  (= right action v.pi_f.pi_i)
                if h not in M: M[h]=M[f]+(i,); nf.append(h)
        fr=nf
    return M
