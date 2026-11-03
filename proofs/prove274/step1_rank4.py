# PROVE 274 Step 0 check in rank 4: far = alpha_j non-simple in Delta_theta^+ = (not closed&coclosed) = E_j not normalising n_T
import q60c_allG as Q
F4=[[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]]
D4=[[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]]
orig=Q.cartan
for name,C in [('F4',F4),('D4',D4),('B4',orig('B',4)),('C4',orig('C',4))]:
    Q.cartan=lambda t,n,C=C:C
    C_,R,br=Q.build('X',4)   # asserts Jacobi + N_{a,b}!=0 iff a+b root
    thetas=Q.weyl_group_thetas(C_,R)
    Rs=set(R); add=lambda a,b:tuple(x+y for x,y in zip(a,b))
    th=lambda t,v:sum(t[k]*v[k] for k in range(4))
    inv={frozenset(b for b in R if th(t,b)<0) for t in thetas}
    stats={}
    for t in thetas:
        S={b for b in R if th(t,b)>0}; T={b for b in R if th(t,b)<0}
        for j in range(4):
            aj=tuple(int(i==j) for i in range(4))
            if aj not in S: continue
            X=T|{aj}
            far=any(add(a,aj) in S for a in T)
            nonsimp=frozenset(X) not in inv
            closed=all(add(a,b) in X for a in X for b in X if add(a,b) in Rs)
            cocl=all(add(a,b) not in X for a in S-{aj} for b in S-{aj} if add(a,b) in Rs)
            notideal=any(add(aj,a) in S for a in T)
            k=(far,nonsimp,not(closed and cocl),notideal); stats[k]=stats.get(k,0)+1
    print(name,len(R),'|W|=',len(thetas),stats)
