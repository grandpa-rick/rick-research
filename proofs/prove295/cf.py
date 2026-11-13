"""composition factors of B/A as left and right A-module (traces of pi_{w0(J)})."""
import sys, numpy as np, itertools
from core import *
import bic
def run(N):
    R=bic.run(N); Z,Av,B_,off=R['Z'],R['Av'],R['B_'],R['off']; G=R['G']
    tot=Z.shape[0]
    def unvec(v): return [v[off[a]:off[a]+len(b)**2].reshape(len(b),len(b)) for a,b in enumerate(B_)]
    def vec(Ms): return np.concatenate([M.ravel() for M in Ms])%P
    Pb=[[mat(g)[np.ix_(b,b)] for b in B_] for g in G]   # per block matrices
    # basis: A rows then complement of B
    RA=Av; rA=rank(RA)
    # choose basis of B/A: B rows reduced
    Bb=Z.T%P
    # basis of B: A-basis (independent rows) + extra
    M=tomat(Av); Mr,r=M.transpose().rref()  # not needed
    # build basis of B as: Bb itself (dim B); quotient map: coordinates mod A
    # coordinates of vector in B-basis:
    Bt=tomat(Bb)  # dimB x tot
    # solve x*Bb = v  -> use pivots
    E,rk=tomat(Bb).rref(); E=np.array(E.entries(),dtype=np.int64).reshape(Bb.shape)[:rk]
    piv=[int(np.nonzero(e)[0][0]) for e in E]
    def coords(v): return v[piv]%P   # coords in basis E (rref)
    Acoords=np.array([coords(a) for a in Av])
    # quotient: complement basis
    Q=null(Acoords)  # vectors y with Acoords y=0  -> functionals vanishing on A: dimB-dimA of them (column)
    k=Q.shape[1]; print(N,'defect',k)
    def opmat(f):  # matrix of linear map on B/A in dual coordinates: compute f on E rows then pair with Q
        # quotient B/A dual = Q (functionals). Represent map's transpose action on functionals: tr = tr on quotient
        img=np.array([coords(f(e)) for e in E])   # rk x rk, row i = coords of f(E_i)
        return img
    def left(i):
        return lambda v: vec([Mb@Pi for Mb,Pi in zip(unvec(v),Pb[i])])
    def right(i):
        return lambda v: vec([Pi@Mb for Mb,Pi in zip(unvec(v),Pb[i])])
    # trace on quotient = trace on B - trace on A ; easier: trace on B minus trace on A both computed via the rref basis
    # basis of A inside coords: Acoords rows (span). Use: tr_quot(F) = tr(F on B) - tr(F on A)
    Ab=np.array(tomat(Acoords).rref()[0].entries(),dtype=np.int64).reshape(Acoords.shape)[:rA]
    pa=[int(np.nonzero(e)[0][0]) for e in Ab]
    out={}
    for side,act in (('left',left),('right',right)):
        trs={}
        for r in range(N):
            for J in itertools.combinations(range(N-1),r):
                # pi_{w0(J)}: product over reduced word of w0 of parabolic J; idempotent so (prod pi_j for j in J)^(big) works
                def F(v,J=J):
                    for _ in range(N*(N-1)//2):
                        for j in J: v=act(j)(v)
                    return v
                img=np.array([coords(F(e)) for e in E])  # rows
                trB=int(np.trace(img))%P
                imgA=np.array([coords(F(Ab[t]@E%P)) for t in range(rA)]) if rA else np.zeros((0,rk))
                trA=int(sum(imgA[t,pa[t]] for t in range(rA)))%P
                t=(trB-trA)%P; trs[J]=t if t<P//2 else t-P
        # mobius: tr(J)=sum_{D cap J empty} m_D  -> m_D = sum_{J subset D^c} ... inversion: f(J)=sum_{D subset J^c} m_D
        mult={}
        allJ=list(trs)
        for D in allJ:
            Dc=tuple(x for x in range(N-1) if x not in D)
            # m_D = sum_{K superset D} (-1)^{|K|-|D|} f(K^c)
            s=0
            for r2 in range(len(D)+1):
                for Ee in itertools.combinations(D,r2):
                    Ec=tuple(x for x in range(N-1) if x not in Ee)
                    s+=(-1)**(len(D)-len(Ee))*trs[Ec]
            if s: mult[tuple(x+1 for x in D)]=s
        print(side,mult,flush=True); out[side]=mult
    return out
if __name__=='__main__':
    for N in map(int,sys.argv[1:]): run(N)
