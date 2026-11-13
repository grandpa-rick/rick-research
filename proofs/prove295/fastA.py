"""dim A = sum_D dim Q_D,  Q_D = image of P_D = span{ (b.m)_{b in basis of V x_D} : m in monoid }."""
import sys, itertools, time, numpy as np
from collections import defaultdict
from flint import nmod_mat
from split import asc, move, act_pi, act_pibar, w0word
P=2**31-1
def run(n,N):
    t0=time.time()
    W=list(itertools.product(range(1,n+1),repeat=N)); widx={w:k for k,w in enumerate(W)}
    Ds=sorted({asc(w) for w in W},key=lambda s:(len(s),sorted(s)))
    def xD(vec,D):
        Dc=[j for j in range(1,N) if j not in D]
        for i in w0word(D): vec=act_pibar(vec,i)
        for i in w0word(Dc): vec=act_pi(vec,i)
        return vec
    # monoid elements: BFS on permutations, store as transformation of words (tuple of indices)
    gens=[np.array([widx[move(w,i)] for w in W]) for i in range(1,N)]
    ident=np.arange(len(W)); seen={tuple(range(N)):ident}; fr=[tuple(range(N))]
    while fr:
        nf=[]
        for p in fr:
            for i in range(N-1):
                if p[i]<p[i+1]:
                    q=list(p); q[i],q[i+1]=q[i+1],q[i]; q=tuple(q)
                    if q not in seen: seen[q]=gens[i][seen[p]]; nf.append(q)
        fr=nf
    mons=list(seen.values())
    tot=0; global PER; PER={}
    for D in Ds:
        # basis of V x_D: rref per whole V (vectors in word coords)
        vs=[xD({w:1},D) for w in W]; vs=[v for v in vs if v]
        A=np.zeros((len(vs),len(W)),dtype=np.int64)
        for r,v in enumerate(vs):
            for w,c in v.items(): A[r,widx[w]]=c%P
        E,r=nmod_mat(A.shape[0],A.shape[1],[int(x) for x in A.ravel()],P).rref()
        E=np.array(E.entries(),dtype=np.int64).reshape(A.shape)[:r]
        # rows: for each monoid element f, concat over basis b of (b.f) ; b.f = sum_w b_w e_{f(w)}
        rows=[]
        nz=[np.nonzero(e)[0] for e in E]
        mat=np.zeros((len(mons),r*len(W)),dtype=np.int32)
        for k,f in enumerate(mons):
            for bi,(e,z) in enumerate(zip(E,nz)):
                np.add.at(mat[k], bi*len(W)+f[z], (e[z]%P).astype(np.int32)) if False else None
                for zz in z: mat[k,bi*len(W)+f[zz]]=(int(mat[k,bi*len(W)+f[zz]])+int(e[zz]))%P
        mat%=P
        mat=mat[:,mat.any(axis=0)]
        rk=nmod_mat(mat.shape[0],mat.shape[1],[int(x) for x in mat.ravel()],P).rank()
        tot+=rk; PER[tuple(sorted(D))]=rk
    print(n,N,'dim A =',tot,'time',round(time.time()-t0,1),flush=True)
    return tot
if __name__=='__main__':
    for a in sys.argv[1:]:
        n,N=map(int,a.split(',')); run(n,N)
