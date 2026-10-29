"""PROVE 264: check the explicit bijection {(rho,lam,kap)} -> {0,1,2}^m of the Q50 proof, and the box/diagonal dictionary.
w_d = 2 if diagonal d has a box of kap/rho; elif d+1<m and diag d+1 has a box: w_d = step (0/1) of that box (step1->0, step2->1);
else w_d = [d+1 in rho]."""
import sys, itertools
from q50_count import strict_parts, diagram, vmaps_brute, steps
def addable(rho_diag, m):
    out=set()
    for a in range(m):
        for b in range(a,m):
            x=(a,b)
            if x in rho_diag: continue
            if (a==0 or (a-1,b) in rho_diag) and (b==a or (a,b-1) in rho_diag): out.add(x)
    return out
def lam_of(S): return tuple(sorted(S, reverse=True))
for m in range(1,int(sys.argv[1])+1):
    seen={}; bad=0; dictbad=0
    for rho in strict_parts(m):
        R=diagram(rho)
        for S1,_ in steps(frozenset(rho),m,True):
            lam=lam_of(S1); L=diagram(lam)
            A1=L-R
            if not (R<=L and A1<=addable(R,m)): dictbad+=1
            for S2,_ in steps(S1,m,False):
                kap=lam_of(S2); K=diagram(kap); A2=K-L
                if not (L<=K and A2<=addable(L,m) and all(b!=a for a,b in A2)): dictbad+=1
                step={}
                for (a,b) in A1: step.setdefault(b-a,[]).append(0)
                for (a,b) in A2: step.setdefault(b-a,[]).append(1)
                if any(len(v)>1 for v in step.values()): bad+=1
                w=[]
                for d in range(m):
                    if d in step: w.append(2)
                    elif d+1<m and d+1 in step: w.append(step[d+1][0])
                    else: w.append(int(d+1 in rho))
                w=tuple(w)
                if w in seen: bad+=1
                seen[w]=(rho,lam,kap)
    # antichain-dictionary converse: every lam with lam/rho antichain arises
    conv=0
    if m<=5:
        for rho in strict_parts(m):
            for kap in strict_parts(m):
                cnt=sum(1 for w,(r,l,k) in seen.items() if r==rho and k==kap)
                if cnt!=vmaps_brute(kap,rho): conv+=1
    print(f"m={m}: triples={len(seen)} 3^m={3**m} collisions/doubles={bad} dict_fail={dictbad} Vmap_mismatch={conv} surj={len(seen)==3**m}")
