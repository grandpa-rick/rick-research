import itertools, numpy as np
for N in range(3,7):
    words=list(itertools.product([1,2],repeat=N)); idx={w:i for i,w in enumerate(words)}
    def pi(i):
        return tuple(idx[w[:i]+(w[i+1],w[i])+w[i+2:]] if w[i]<w[i+1] else idx[w] for w in words)
    gens=[pi(i) for i in range(N-1)]
    ident=tuple(range(len(words)))
    M={ident}; fr=[ident]
    while fr:
        nf=[]
        for f in fr:
            for g in gens:
                h=tuple(g[f[x]] for x in range(len(words)))
                if h not in M: M.add(h); nf.append(h)
        fr=nf
    mats=[]
    for f in M:
        A=np.zeros((len(words),len(words))); 
        for x in range(len(words)): A[f[x],x]=1
        mats.append(A.flatten())
    r=np.linalg.matrix_rank(np.array(mats))
    idem=sum(1 for f in M if tuple(f[f[x]] for x in range(len(words)))==f)
    print(N,len(M),r,'idempotents',idem)
