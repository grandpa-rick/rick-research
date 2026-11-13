import itertools, numpy as np
for N in range(3,8):
    words=list(itertools.product([1,2],repeat=N)); idx={w:i for i,w in enumerate(words)}; D=len(words)
    def pim(i):
        A=np.zeros((D,D))
        for w in words:
            A[idx[w[:i]+(w[i+1],w[i])+w[i+2:]] if w[i]<w[i+1] else idx[w], idx[w]]=1
        return A
    P=[pim(i) for i in range(N-1)]
    tot=0; tops={}
    perms=list(itertools.permutations(range(N)))
    for r in range(N):
      for Dset in itertools.combinations(range(N-1),r):
        # Hom(V,S_D) = dim V / sum_i (pi_i - chi_i) V ; chi_i = 0 if i in D else 1
        M=np.hstack([P[i]-(0 if i in Dset else 1)*np.eye(D) for i in range(N-1)])
        m=D-np.linalg.matrix_rank(M)
        if m:
            dimP=sum(1 for p in perms if set(j for j in range(N-1) if p[j]>p[j+1])==set(Dset))
            tops[Dset]=m; tot+=m*dimP
    print(N,'dimV',D,'sum m_D dimP_D',tot, tops)
