from core import *
for (n,N) in [(2,2),(2,3)]:
    W, idx, d = setup(n,N); U = U0_ops(n,N); Ts=T_ops(n,N)
    def comm_dim(gens):
        rows=[]
        for g in gens:
            for r in range(d):
                for c in range(d):
                    row=[0]*(d*d)
                    for k in range(d):
                        if g[r,k]: row[k*d+c]+=int(g[r,k])
                        if g[k,c]: row[r*d+k]-=int(g[k,c])
                    if any(row): rows.append(row)
        return len(nullspace_int(rows,d*d))
    print(n,N,'comm(U0)=',comm_dim(list(U.values())),'comm(H)=',comm_dim(Ts))
    # also commutant of U0 generated only by e,f (no k)
    print(' comm(e,f only)=',comm_dim([U[k] for k in U if k[0]!='k']))
