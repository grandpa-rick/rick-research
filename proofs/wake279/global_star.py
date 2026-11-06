import sys
from coxkl import *
exec(open('twin_criterion.py').read().split("for name in")[0].split("from coxkl import *")[1])
for name in sys.argv[1].split(','):
    M=CASES[name]; G = coxeter_group(M); P, mu = kl(G); cells, D = left_cells(G, mu); n=G['n']; N=G['N']; L=G['length']; lm=G['lm']
    nb=lambda s:[t for t in range(n) if t!=s and M[s][t]==3]
    intr=lambda A: frozenset(s for s in A if all(t in A for t in nb(s)))
    def star(x,s,t):
        for y in (lm[s,x],lm[t,x]):
            if len(D[y]&{s,t})==1: return y
    cid={w:i for i,c in enumerate(cells) for w in c}
    cnt=0;samecell=0
    for x in range(N):
        I=intr(D[x]); bps=[(s,t) for s in D[x] for t in nb(s) if t not in D[x]]
        if not bps: continue
        for z in range(N):
            if z==x or not D[z] or not D[z]<=I: continue
            if all(mu[star(x,s,t),z]>=1 for s,t in bps):
                cnt+=1; samecell+= cid[x]==cid[z]
                if cnt<=5: print(name,'x',G['word'][x],sorted(D[x]),'z',G['word'][z],sorted(D[z]),'cells',cid[x],cid[z])
    print(name,'global star-twin pairs',cnt,'same cell',samecell)
