"""Test a = product of factors; for each weight mu: (B) a kills I_mu u O_mu [=> a.1_mu in B, proved criterion];
(notA) exact cyclic test: (g1 a,0..0) notin span{(g1 x, g2 x, ...)} with g1 in M_mu (g1 a !=0), g_i = words of other weights with same Asc as g1."""
import sys, itertools
from collections import defaultdict
from flint import fmpz_mat
from split import asc, move, act_pi, act_pibar, w0word
def run(n,N,fs,only=None,verbose=True):
    W=list(itertools.product(range(1,n+1),repeat=N))
    wt=lambda w: tuple(w.count(c) for c in range(1,n+1))
    mus=sorted({wt(w) for w in W}); byw=defaultdict(list)
    for w in W: byw[wt(w)].append(w)
    Sv={m:asc(tuple(c for c in range(1,n+1) for _ in range(m[c-1]))) for m in mus}
    def apply(vec):
        for b,J in fs:
            for i in w0word(J): vec=(act_pibar if b else act_pi)(vec,i)
            if not vec: return vec
        return vec
    killcache={}
    def killed(w):
        if w not in killcache: killcache[w]=not apply({w:1})
        return killcache[w]
    def orbit_all_killed(w):
        O={w}; st=[w]
        while st:
            v=st.pop()
            if not killed(v): return False
            for i in range(1,N):
                u=move(v,i)
                if u not in O: O.add(u); st.append(u)
        return True
    hits=[]
    for mu in mus:
        if only and mu not in only: continue
        nz=[w for w in byw[mu] if not killed(w)]
        if not nz: continue
        ok=True
        for nu in mus:
            if nu==mu: continue
            for w in byw[mu]:
                if asc(w)<=Sv[nu] and not orbit_all_killed(w): ok=False; break
            if not ok: break
            for w in byw[nu]:
                if asc(w)<=Sv[mu] and not orbit_all_killed(w): ok=False; break
            if not ok: break
        if not ok: continue
        # non-membership
        res=False
        for g1 in nz[:6]:
            others=[v for v in W if wt(v)!=mu and asc(v)==asc(g1)]
            gs=(g1,)+tuple(others); Ost={gs}; fr=[gs]
            while fr:
                nf=[]
                for s in fr:
                    for i in range(1,N):
                        t=tuple(move(x,i) for x in s)
                        if t not in Ost: Ost.add(t); nf.append(t)
                fr=nf
            keys={}
            def key(j,w):
                if (j,w) not in keys: keys[(j,w)]=len(keys)
                return keys[(j,w)]
            rows=[]
            for s in Ost:
                r=defaultdict(int)
                for j,x in enumerate(s): r[key(j,x)]+=1
                rows.append(r)
            tg=defaultdict(int)
            for t,c in apply({g1:1}).items(): tg[key(0,t)]+=c
            nk=len(keys); M=[[r.get(k,0) for k in range(nk)] for r in rows]
            if fmpz_mat(M+[[tg.get(k,0) for k in range(nk)]]).rank()==fmpz_mat(M).rank()+1: res=True; break
        if verbose: print('  ',n,N,'weight',mu,'a.1_mu in B; notin A (cyclic, exact):',res,flush=True)
        if res: hits.append(mu)
    return hits
if __name__=='__main__':
    n,N=map(int,sys.argv[1:3])
    fs=eval(sys.argv[3])
    print(n,N,fs); h=run(n,N,fs); print('WITNESS weights:',h)
