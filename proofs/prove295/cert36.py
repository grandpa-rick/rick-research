"""Exact certificate for a rank-one witness b = delta_src (x) tgt supported on one weight space.
(a) b commutes with every S word map phi_{mu,w} (exact, integer, all words).
(b) b notin A: (src.b, 0,...,0) not in span{(src.x, g_1.x, ..., g_k.x)} over monoid x, g_i = other D-words. exact fmpz rank."""
import sys, itertools
from collections import defaultdict
from flint import fmpz_mat
from split import asc, move
def parse(s): return tuple(int(c) for c in s)
def run(n,N,src,tgt):
    src=parse(src); tgt={parse(t):c for t,c in tgt}
    W=list(itertools.product(range(1,n+1),repeat=N))
    wt=lambda w: tuple(w.count(c) for c in range(1,n+1))
    mu=wt(src); assert all(wt(t)==mu for t in tgt)
    def bmap(vec):  # b applied to vector (dict)
        c=vec.get(src,0); return {t:c*x for t,x in tgt.items()} if c else {}
    wts=defaultdict(list)
    for w in W: wts[wt(w)].append(w)
    path={}
    for m in wts:
        v0=tuple(c for c in range(1,n+1) for _ in range(m[c-1])); Pp={v0:()}; fr=[v0]
        while fr:
            nf=[]
            for v in fr:
                for i in range(1,N):
                    u=move(v,i)
                    if u not in Pp: Pp[u]=Pp[v]+(i,); nf.append(u)
            fr=nf
        path[m]=(v0,Pp)
    def phi(m,w,v):  # phi_{m,w}(word v)
        u=w
        for i in path[m][1][v]: u=move(u,i)
        return u
    bad=0; cnt=0
    for m in wts:
        S=asc(path[m][0])
        for nu in wts:
            if m!=mu and nu!=mu: continue
            for w in wts[nu]:
                if not asc(w)<=S: continue
                cnt+=1
                # check phi(b v) == b(phi v) for all words v in M_m
                for v in wts[m]:
                    lhs=defaultdict(int)
                    for t,c in bmap({v:1}).items(): lhs[phi(m,w,t)]+=c
                    rhs=bmap({phi(m,w,v):1})
                    l={k:c for k,c in lhs.items() if c}; r={k:c for k,c in rhs.items() if c}
                    if l!=r: bad+=1; break
    print(n,N,'S word maps touching weight',mu,':',cnt,' non-commuting:',bad)
    D=asc(src); others=[w for w in W if asc(w)==D and wt(w)!=mu]
    gs=[src]+others
    st=tuple(gs); O={st}; fr=[st]
    while fr:
        nf=[]
        for s in fr:
            for i in range(1,N):
                t=tuple(move(x,i) for x in s)
                if t not in O: O.add(t); nf.append(t)
        fr=nf
    keys={}
    def key(j,w):
        if (j,w) not in keys: keys[(j,w)]=len(keys)
        return keys[(j,w)]
    rows=[]
    for s in O:
        r=defaultdict(int)
        for j,x in enumerate(s): r[key(j,x)]+=1
        rows.append(r)
    target=defaultdict(int)
    for t,c in tgt.items(): target[key(0,t)]+=c
    nk=len(keys)
    M=[[r.get(k,0) for k in range(nk)] for r in rows]
    r0=fmpz_mat(M).rank(); r1=fmpz_mat(M+[[target.get(k,0) for k in range(nk)]]).rank()
    print('  D',sorted(D),'#other D-words',len(others),'orbit',len(O),' b notin A:',r1==r0+1)
if __name__=='__main__':
    run(2,5,'12112',[('12112',1),('12211',-1),('21112',-1),('22111',1)])
    t36='+1*232123 -1*232132 -1*232213 +1*232231 +1*233212 -1*233221 -1*322123 +1*322132 +1*322213 -1*322231 -1*332212 +1*332221'
    run(3,6,'123223',[(x.split('*')[1],int(x.split('*')[0])) for x in t36.split()])
