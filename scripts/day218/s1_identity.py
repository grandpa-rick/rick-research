# check sum_{|A|=k} c_A X_A = e_k (=> E_k|_{s=1} F = e_k F for all F), N<=5
import sympy as sp, itertools as it
t=sp.symbols('t')
for N in range(1,6):
    x=sp.symbols('x1:%d'%(N+1))
    for k in range(1,N+1):
        S=0
        for A in it.combinations(range(N),k):
            c=sp.Mul(*[(x[i]-t*x[j])/(x[i]-x[j]) for i in A for j in range(N) if j not in A])
            S+=c*sp.Mul(*[x[i] for i in A])
        ek=sum(sp.Mul(*[x[i] for i in B]) for B in it.combinations(range(N),k))
        print(N,k,sp.cancel(sp.together(S)-ek)==0)
