import numpy as np, sympy as sp, random
P=1000003
def nullspace_modp(A):
    A=A.copy()%P; m,n=A.shape; piv=[]; r=0
    for c in range(n):
        if r>=m: break
        nz=np.nonzero(A[r:,c])[0]
        if len(nz)==0: continue
        k=r+nz[0]; A[[r,k]]=A[[k,r]]
        inv=pow(int(A[r,c]),P-2,P); A[r]=(A[r]*inv)%P
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%P
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]; basis=[]
    for f in free:
        v=np.zeros(n,dtype=np.int64); v[f]=1
        for i,c in enumerate(piv): v[c]=(-A[i,f])%P
        basis.append(v)
    return basis
def endo_modp(mats,n):
    I=np.eye(n,dtype=np.int64); rows=[]
    for A in mats.values():
        A=np.array(A.tolist(),dtype=np.int64)
        rows.append(np.kron(I,A)-np.kron(A.T,I))  # vec(AX - XA), column-major vec
    M=np.vstack(rows) if rows else np.zeros((1,n*n),dtype=np.int64)
    return [v.reshape(n,n,order='F') for v in nullspace_modp(M)]
def nsum_modp(E,n,seed=0):
    random.seed(seed)
    phi=np.zeros((n,n),dtype=np.int64)
    for B in E: phi=(phi+random.randrange(P)*B)%P
    t=sp.symbols('t')
    cp=sp.Poly(sp.Matrix(phi.tolist()).charpoly(t).as_expr(),t,modulus=P)
    g=sp.gcd(cp,cp.diff(t)); return sp.quo(cp,g).degree()
