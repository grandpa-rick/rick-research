# (3.6) support characterisation: exists lambda  <=>  theta has no 3-chain and every non-minimal box of theta is off-diagonal.
import itertools
def D(k): return frozenset((a,b) for a,p in enumerate(k) for b in range(a,a+p))
def anti(X): return not any(x!=y and x[0]<=y[0] and x[1]<=y[1] for x in X for y in X)
lt=lambda x,y: x!=y and x[0]<=y[0] and x[1]<=y[1]
for m in range(1,9):
    shapes=[tuple(sorted(c,reverse=True)) for k in range(m+1) for c in itertools.combinations(range(1,m+1),k)]
    bad=nb=tot=0
    for rho in shapes:
        for kap in shapes:
            if not D(rho)<=D(kap): continue
            th=D(kap)-D(rho); tot+=1
            ex=any(D(rho)<=D(l)<=D(kap) and anti(D(l)-D(rho)) and anti(D(kap)-D(l)) and all(a!=b for a,b in D(kap)-D(l)) for l in shapes)
            no3=not any(lt(x,y) and lt(y,z) for x in th for y in th for z in th)
            nonmin_off=all(x[0]!=x[1] for x in th if any(lt(y,x) for y in th))
            bad+= ex!=(no3 and nonmin_off); nb+= ex and not anti(th)
    print(m,"pairs",tot,"char failures",bad,"non-Boolean pairs in (3.6)",nb)
