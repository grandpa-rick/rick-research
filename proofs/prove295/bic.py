import sys, numpy as np, time
from core import *
def run(N):
    W,idx,G=gens(N); d=len(W)
    blk={}
    for k,w in enumerate(W): blk.setdefault(w.count(2),[]).append(k)
    B_=[np.array(blk[a]) for a in sorted(blk)]
    Pm=[mat(g) for g in G]
    # S: phi: block a -> block b with phi P|a = P|b phi
    S=[]
    for i,ba in enumerate(B_):
        for j,bb in enumerate(B_):
            da,db=len(ba),len(bb); rows=[]
            for Pi in Pm:
                Pa=Pi[np.ix_(ba,ba)]; Pb=Pi[np.ix_(bb,bb)]
                rows.append(np.kron(np.eye(db,dtype=np.int64),Pa.T)-np.kron(Pb,np.eye(da,dtype=np.int64)))
            K=null(np.vstack(rows))
            for c in range(K.shape[1]): S.append((i,j,K[:,c].reshape(db,da)))
    # B: block diagonal x_a; first per-block commutant with End(block)
    off=[];tot=0
    for b in B_: off.append(tot); tot+=len(b)**2
    Gb=None
    # iterative: global basis matrix Z (tot x k)
    Z=np.eye(tot,dtype=np.int64)
    order=sorted(S,key=lambda s:(s[0]!=s[1]))
    for (i,j,phi) in order:
        di,dj=len(B_[i]),len(B_[j])
        E=np.zeros((di*dj,tot),dtype=np.int64)
        E[:,off[j]:off[j]+dj*dj]+=np.kron(np.eye(dj,dtype=np.int64),phi.T)
        E[:,off[i]:off[i]+di*di]-=np.kron(phi,np.eye(di,dtype=np.int64))
        EZ=(tomat(E%P)*tomat(Z))
        EZ=np.array(EZ.entries(),dtype=np.int64).reshape(di*dj,Z.shape[1])
        if not EZ.any(): continue
        K=null(EZ); Z=np.array((tomat(Z)*tomat(K)).entries(),dtype=np.int64).reshape(tot,K.shape[1])
    # A
    M=monoid(G)
    def vecof(f):
        v=np.zeros(tot,dtype=np.int64)
        for a,b in enumerate(B_):
            pos={x:t for t,x in enumerate(b)}
            for t,x in enumerate(b): v[off[a]+pos[f[x]]*len(b)+t]=1
        return v
    Av=np.array([vecof(f) for f in M])
    rA=rank(Av); rB=Z.shape[1]; rAB=rank(np.vstack([Av,Z.T]))
    print(N,'dimS',len(S),'dimA',rA,'dimB',rB,'A+B',rAB,'|M|',len(M),flush=True)
    return dict(W=W,B_=B_,off=off,Z=Z,Av=Av,M=M,S=S,G=G)
if __name__=='__main__':
    for N in map(int,sys.argv[1:]): run(N)
