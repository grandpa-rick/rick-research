# Verify: in V=C^2^{(x)N} (Jung-Oh (4.5) action), weight (N-1,1) and (1,N-1) spaces;
# W=span{u_1..u_{N-1}}, W'=span{v_2..v_N} are submodules; dim Hom_H(W,W')>0 and Hom_H(W',W)>0;
# both indecomposable (End local: dim End = 1 + nilpotents -> check End has no nontrivial idempotent via dim of End/rad... just print dims)
# Negative control: generic q (T_i^2=(q-1)T_i+q, here q=2 analogue on same words) Hom between the analogous pieces.
import sympy as sp, itertools
def act(w,i,q=0):
    a,b=w[i],w[i+1]; u=list(w); u[i],u[i+1]=b,a; u=tuple(u)
    if q==0:
        if a<b: return {u:1}
        if a>b: return {w:-1}
        return {}
def mats(words,N):
    idx={w:k for k,w in enumerate(words)}; d=len(words); Ms=[]
    for i in range(N-1):
        M=sp.zeros(d,d)
        for w in words:
            for u,c in act(w,i).items(): M[idx[w],idx[u]]+=c   # row vector convention: w.pi = row
        Ms.append(M)
    return Ms
def hom(A,B):  # right modules given by row-action matrices; X with A_i X = X B_i
    da,db=A[0].shape[0],B[0].shape[0]; xs=sp.symbols('x0:%d'%(da*db)); X=sp.Matrix(da,db,xs)
    eqs=[]
    for a,b in zip(A,B): eqs+=list(A_i_X(a,X,b))
    sol=sp.linsolve(eqs,xs); s=list(sol)[0]; return len(set().union(*[e.free_symbols for e in s]))
def A_i_X(a,X,b): return (a*X-X*b)
for N in range(3,7):
    U=[tuple(1 if j==p else 0 for j in range(N)) for p in range(N)]   # u_{p+1}
    Vv=[tuple(0 if j==p else 1 for j in range(N)) for p in range(N)]  # v_{p+1}
    MU=mats(U,N); MV=mats(Vv,N)
    # W = span u_1..u_{N-1} (indices 0..N-2) submodule? W' = span v_2..v_N (indices 1..N-1)
    okW=all(all(M[r,c]==0 for r in range(N-1) for c in [N-1]) for M in MU)
    okW2=all(all(M[r,0]==0 for r in range(1,N)) for M in MV)
    WA=[M[:N-1,:N-1] for M in MU]; WB=[M[1:,1:] for M in MV]
    print(N,"submods",okW,okW2,"dimHom(W,W')",hom(WA,WB),"dimHom(W',W)",hom(WB,WA),"dimEnd W",hom(WA,WA),"dimEnd W'",hom(WB,WB))
def homsol(A,B):
    da,db=A[0].shape[0],B[0].shape[0]; xs=sp.symbols('x0:%d'%(da*db)); X=sp.Matrix(da,db,xs)
    eqs=[]
    for a,b in zip(A,B): eqs+=list(a*X-X*b)
    s=list(sp.linsolve(eqs,xs))[0]; return sp.Matrix(da,db,list(s))
for N in [3,4,5]:
    U=[tuple(1 if j==p else 0 for j in range(N)) for p in range(N)]
    Vv=[tuple(0 if j==p else 1 for j in range(N)) for p in range(N)]
    MU=mats(U,N); MV=mats(Vv,N)
    WA=[M[:N-1,:N-1] for M in MU]; WB=[M[1:,1:] for M in MV]
    print(N,"W->W' (rows u_1..u_{N-1}, cols v_2..v_N)");sp.pprint(homsol(WA,WB))
    print(N,"W'->W");sp.pprint(homsol(WB,WA))
