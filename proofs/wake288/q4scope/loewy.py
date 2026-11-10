import itertools, sys, numpy as np
from ind import minreps, ind_module
from modp import P, nullspace_modp
def rowred(A):
    A=A.copy()%P; m,n=A.shape; r=0
    for c in range(n):
        if r>=m: break
        nz=np.nonzero(A[r:,c])[0]
        if len(nz)==0: continue
        k=r+nz[0]; A[[r,k]]=A[[k,r]]; A[r]=(A[r]*pow(int(A[r,c]),P-2,P))%P
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
    return A[:r]
def span(cols,n):  # cols: list of vectors -> basis rows
    if not cols: return np.zeros((0,n),dtype=np.int64)
    return rowred(np.array(cols,dtype=np.int64))
def gen_sub(vecs,G,n):  # H-submodule generated
    B=span(vecs,n)
    while True:
        new=[ (g@b)%P for g in G for b in B]
        B2=span(list(B)+new,n)
        if B2.shape[0]==B.shape[0]: return B
        B=B2
def intersect(B1,B2,n):
    if B1.shape[0]==0 or B2.shape[0]==0: return np.zeros((0,n),dtype=np.int64)
    M=np.vstack([B1,(-B2)%P]).T  # B1^T x = B2^T y
    ns=nullspace_modp(M)
    return span([(B1.T@v[:B1.shape[0]])%P for v in ns],n)
def preimage(g,B,n):  # {v : g v in span B}
    # v in ker (proj to complement of B) . g
    if B.shape[0]==0: Q=np.eye(n,dtype=np.int64)
    else:
        Q=np.array(nullspace_modp(B),dtype=np.int64)  # annihilator: rows q with q.b=0
    if Q.shape[0]==0: return np.eye(n,dtype=np.int64)
    return span(nullspace_modp((Q@g)%P),n)
def loewy(mats,n):
    G=[np.array(A.tolist(),dtype=np.int64) for A in mats.values()]
    ks=sorted(mats); C=[(G[k]@G[k+1]-G[k+1]@G[k])%P for k in range(len(G)-1)]
    # radical series
    rad=[np.eye(n,dtype=np.int64)]; cur=rad[0]
    while cur.shape[0]>0:
        nxt=gen_sub([(c@b)%P for c in C for b in cur],G,n); 
        rad.append(nxt); cur=nxt
    # socle series: soc_k = largest submodule U with C*U subset soc_{k-1}
    soc=[np.zeros((0,n),dtype=np.int64)]
    while soc[-1].shape[0]<n:
        U=np.eye(n,dtype=np.int64)
        for c in C: U=intersect(U,preimage(c,soc[-1],n),n)
        while True:  # largest submodule in U
            V=U
            for g in G: V=intersect(V,preimage(g,U,n),n)
            if V.shape[0]==U.shape[0]: break
            U=V
        soc.append(U)
    return [r.shape[0] for r in rad],[s.shape[0] for s in soc]
