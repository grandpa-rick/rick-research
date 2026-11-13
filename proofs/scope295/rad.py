import itertools, numpy as np, sympy
for N in range(3,7):
    words=list(itertools.product([1,2],repeat=N)); idx={w:i for i,w in enumerate(words)}; D=len(words)
    def pim(i):
        A=np.zeros((D,D),dtype=np.int64)
        for w in words:
            A[idx[w[:i]+(w[i+1],w[i])+w[i+2:]] if w[i]<w[i+1] else idx[w], idx[w]]=1
        return A
    gens=[pim(i) for i in range(N-1)]
    basis=[np.eye(D,dtype=np.int64)]; B=np.array([basis[0].flatten()],dtype=float); fr=[basis[0]]
    while fr:
        nf=[]
        for f in fr:
            for g in gens:
                h=g@f; C=np.vstack([B,h.flatten()])
                if np.linalg.matrix_rank(C)>B.shape[0]: B=C; basis.append(h); nf.append(h)
        fr=nf
    G=np.array([[np.trace(a@b) for b in basis] for a in basis],dtype=float)
    print(N,len(basis),'dim A/rad =',np.linalg.matrix_rank(G))
