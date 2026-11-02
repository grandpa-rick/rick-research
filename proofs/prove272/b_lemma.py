import sys, itertools
from lusztig import Model
n=int(sys.argv[1]); H=int(sys.argv[2]); M=Model(n); N=M.N
pos=M.roots(next(iter(M.words))); simple=[tuple(1 if t==i else 0 for t in range(n)) for i in range(n)]
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def closed(X): return all(add(x,y) not in pos or add(x,y) in X for x in X for y in X)
def estar_count(k,d,w):  # eps*_k = last coordinate in a word whose last root is alpha_k
    v=next(u for u in sorted(M.words) if M.roots(u)[-1]==simple[k])
    return M.trans(d,w,v)[-1]
tot=ok=0; cases=0
for w in sorted(M.words):
    R=M.roots(w)
    for l in range(N):
        T=set(R[:l]); a=R[l]
        if a not in simple or a in T: continue
        if not closed(T|{a}): continue
        j=simple.index(a); cases+=1
        for nt in itertools.product(range(3),repeat=l):
            if sum(c*sum(r) for c,r in zip(nt,R)) > H: continue
            for mm in range(3):
                d=tuple(nt)+(mm,)+(0,)*(N-l-1)
                tot+=1; ok+= estar_count(j,d,w)==mm
print("adj (word,l) cases",cases," eps*_j(b(n_T,m,0))==m :",ok,"/",tot)
