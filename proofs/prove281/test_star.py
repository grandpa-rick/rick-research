from klperm import *
import sys
n=int(sys.argv[1]); W,P,mu=full_kl(n)
assert all(P[(x,w)][0]==1 for (x,w) in P)
def star(i,w):
    Lw=L(w)
    if len(Lw&{i,i+1})!=1: return None
    for y in (lmul(i,w),lmul(i+1,w)):
        if len(L(y)&{i,i+1})==1 and (L(y)&{i,i+1})!=(Lw&{i,i+1}): return y
bad=0;tot=0
for i in range(1,n-1):
    D=[w for w in W if star(i,w)]
    for x in D:
        for y in D:
            tot+=1
            if MU(mu,x,y)!=MU(mu,star(i,x),star(i,y)): bad+=1
print('n',n,'pairs',tot,'star-invariance violations',bad, 'max mu',max(mu.values()))
