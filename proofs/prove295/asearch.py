"""Search a = product of parabolic elements (pi_{w0 J} or pibar_{w0 J}) with a.1_mu in B \\ A.
B-test: a kills I_mu (vectors) and O_mu.  A-test: exact cyclic test with src=all words of M_mu? -> use mod-P rank vs A_only."""
import sys, itertools, numpy as np
from collections import defaultdict
from split import asc, move, act_pi, act_pibar, w0word
def run(n,N,mu,maxf=2):
    W=list(itertools.product(range(1,n+1),repeat=N))
    wt=lambda w: tuple(w.count(c) for c in range(1,n+1))
    mus=sorted({wt(w) for w in W})
    Sv={m:asc(tuple(c for c in range(1,n+1) for _ in range(m[c-1]))) for m in mus}
    def orbit(w):
        O={w}; st=[w]
        while st:
            v=st.pop()
            for i in range(1,N):
                u=move(v,i)
                if u not in O: O.add(u); st.append(u)
        return O
    I=set(); O=set()
    for nu in mus:
        if nu==mu: continue
        for w in W:
            if wt(w)==mu and asc(w)<=Sv[nu]: I|=orbit(w)
            if wt(w)==nu and asc(w)<=Sv[mu]: O|=orbit(w)
    kill=I|O
    Js=[J for r in range(N) for J in itertools.combinations(range(1,N),r)]
    facs=[(b,J) for J in Js for b in (0,1) if J]
    def apply(vec,fs):
        for b,J in fs:
            for i in w0word(J): vec=(act_pibar if b else act_pi)(vec,i)
            if not vec: return vec
        return vec
    Mu=[w for w in W if wt(w)==mu]
    found=[]
    for k in range(1,maxf+1):
        for fs in itertools.product(facs,repeat=k):
            if all(not apply({y:1},fs) for y in kill):
                img=[apply({w:1},fs) for w in Mu]
                if any(img): found.append(fs)
    print(n,N,mu,'|kill|',len(kill),'candidates killing cross images & nonzero on M_mu:',len(found))
    return found,Mu,kill
if __name__=='__main__':
    n,N=map(int,sys.argv[1:3]); mu=tuple(map(int,sys.argv[3].split(',')))
    f,_,_=run(n,N,mu,int(sys.argv[4]) if len(sys.argv)>4 else 2)
    for fs in f[:40]: print('  ',[('pibar' if b else 'pi',J) for b,J in fs])
