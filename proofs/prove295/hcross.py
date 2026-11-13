"""For D_n = [1,n-1] u [N-n+1,N-1]: test (i) O(w).h == 0 for all S-words w: M_mu->M_nu, mu!=nu, mu,nu in supp;
(ii) [O(w):S_D]==0 (no D-word reachable).  h = pibar_{w0[1,n-1]} pibar_{w0[N-n+1,N-1]}."""
import sys, itertools
from collections import defaultdict
from split import asc, move, act_pibar, w0word
def run(n,N,allpairs=False):
    D=frozenset(list(range(1,n))+list(range(N-n+1,N)))
    W=list(itertools.product(range(1,n+1),repeat=N))
    wt=lambda w: tuple(w.count(c) for c in range(1,n+1))
    Dwords=[w for w in W if asc(w)==D]; supp={wt(w) for w in Dwords}
    print(n,N,'D',sorted(D),'D-words',len(Dwords),'supp',sorted(supp))
    hword=w0word(range(1,n))+w0word(range(N-n+1,N))
    def orbit(w):
        O={w}; fr=[w]
        while fr:
            nf=[]
            for v in fr:
                for i in range(1,N):
                    u=move(v,i)
                    if u not in O: O.add(u); nf.append(u)
            fr=nf
        return O
    bad_h=bad_cf=tot=0
    mus=[tuple(m) for m in itertools.product(range(N+1),repeat=n) if sum(m)==N] if allpairs else sorted(supp)
    for mu in mus:
        v0=tuple(c for c in range(1,n+1) for _ in range(mu[c-1])); S=asc(v0)
        for nu in (mus):
            if nu==mu: continue
            # S-words in M_nu with Asc subset S
            letters=[c for c in range(1,n+1) for _ in range(nu[c-1])]
            for w in set(itertools.permutations(letters)):
                if not asc(w)<=S: continue
                tot+=1; O=orbit(w)
                if any(asc(v)==D for v in O): bad_cf+=1
                # O.h : apply h to each word in O
                nz=False
                for v in O:
                    vec={v:1}
                    for i in hword: vec=act_pibar(vec,i)
                    if vec: nz=True; break
                if nz:
                    bad_h+=1
                    if bad_h<=3: print('  h-nonzero on O(w): mu',mu,'nu',nu,'w',w)
    print('  cross S-words',tot,' with D-word in orbit',bad_cf,' with O(w)h!=0',bad_h,flush=True)
if __name__=='__main__':
    n,N=map(int,sys.argv[1:3]); run(n,N,allpairs=len(sys.argv)>3)
