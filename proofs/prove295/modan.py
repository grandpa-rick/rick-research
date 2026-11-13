"""analyze right modules: span of block-matrix vectors, right action m -> m.pi = P@M."""
import numpy as np, itertools
from core import *
def setup(R,N):
    B_,off,G=R['B_'],R['off'],R['G']
    Pb=[[mat(g)[np.ix_(b,b)] for b in B_] for g in G]
    I=[np.eye(len(b),dtype=np.int64) for b in B_]
    def unvec(v): return [v[off[a]:off[a]+len(b)**2].reshape(len(b),len(b)) for a,b in enumerate(B_)]
    def vec(Ms): return np.concatenate([M.ravel() for M in Ms])%P
    def ract(v,i): return vec([(Pj@M)%P for M,Pj in zip(unvec(v),Pb[i])])
    def lact(v,i): return vec([(M@Pj)%P for M,Pj in zip(unvec(v),Pb[i])])
    def w0(J,bar):
        X=[i.copy() for i in I]
        for _ in range(N*(N-1)//2):
            for j in J: X=[(((Ii-Pj) if bar else Pj)@Xb)%P for Xb,Pj,Ii in zip(X,Pb[j],I)]
        return X
    def xD(D):
        Dc=[j for j in range(N-1) if j not in D]
        X1=w0(D,True); X2=w0(Dc,False); return vec([(b@a)%P for a,b in zip(X1,X2)])
    return dict(unvec=unvec,vec=vec,ract=ract,lact=lact,xD=xD)
def basis(V):
    V=np.asarray(V)%P
    E,r=tomat(V).rref(); return np.array(E.entries(),dtype=np.int64).reshape(V.shape)[:r]
def socle(Mb,act,N,sub=None):
    """Mb: basis rows of module M (closed). If sub given (rows of submodule), compute socle of M/sub.
    returns {D: dim} of joint eigenspaces (pi_i = 0 on D, 1 off D)."""
    k=Mb.shape[0]
    if sub is None: sub=np.zeros((0,Mb.shape[1]),dtype=np.int64)
    # coordinates: express in basis [sub; complement]
    Sb=basis(sub) if len(sub) else sub
    full=basis(np.vstack([Sb,Mb]))
    # quotient: work with matrices of pi_i on M in basis full, then quotient by first rows? do generic: solve coords
    E,r=tomat(full).rref(); E=np.array(E.entries(),dtype=np.int64).reshape(full.shape)[:r]
    piv=[int(np.nonzero(e)[0][0]) for e in E]
    def co(v): return v[piv]%P
    # build matrices Ti (r x r) acting on coords (row vectors): co(E_t . pi)
    Ts=[np.array([co(act(e,i)) for e in E]) for i in range(N-1)]
    Sc=np.array([co(s) for s in Sb]) if len(Sb) else np.zeros((0,r),dtype=np.int64)
    out={}
    for rr in range(N):
        for D in itertools.combinations(range(N-1),rr):
            # y (row coords) with y T_i - eps_i y in span(Sc), y not in span(Sc)
            # unknowns: y (r), and z_i (|Sc|) per i: y(T_i-eps I) - z_i Sc = 0
            s=len(Sc); nv=r+s*(N-1)
            rows=[]
            for i in range(N-1):
                eps=0 if i in D else 1
                Mi=np.zeros((nv,r),dtype=np.int64)
                Mi[:r]=(Ts[i]-eps*np.eye(r,dtype=np.int64))%P
                if s: Mi[r+s*i:r+s*(i+1)]=(-Sc)%P
                rows.append(Mi)
            K=null(np.hstack(rows).T)  # nv x k : columns solutions (y,z)
            Y=K[:r].T
            d=rank(np.vstack([Sc,Y]))-rank(Sc) if Y.size else 0
            if d: out[tuple(x+1 for x in D)]=d
    return out
def cfactors(Mb,act,N):
    E=basis(Mb); r=E.shape[0]; piv=[int(np.nonzero(e)[0][0]) for e in E]
    co=lambda v: v[piv]%P
    trs={}
    for rr in range(N):
        for J in itertools.combinations(range(N-1),rr):
            T=np.eye(r,dtype=np.int64); 
            Ts={i:np.array([co(act(e,i)) for e in E]) for i in J}
            for _ in range(N*(N-1)//2):
                for j in J: T=(T@Ts[j])%P
            t=int(np.trace(T))%P; trs[J]=t if t<P//2 else t-P
    mult={}
    for D in trs:
        s=0
        for r2 in range(len(D)+1):
            for Ee in itertools.combinations(D,r2):
                Ec=tuple(x for x in range(N-1) if x not in Ee); s+=(-1)**(len(D)-len(Ee))*trs[Ec]
        if s: mult[tuple(x+1 for x in D)]=s
    return mult
