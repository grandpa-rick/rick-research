"""Pairs x!=z in a left cell with L(z) subset L(x) that survive the star-matching kill
(boundary s in L(x)∩L(z) with a neighbour t notin L(x), m=3). For survivors, list killing y's."""
import sys
from coxkl import *
exec(open('twin_criterion.py').read().split("for name in")[0].split("from coxkl import *")[1])
for name in sys.argv[1].split(','):
    M=CASES[name]; G = coxeter_group(M); P, mu = kl(G); cells, D = left_cells(G, mu)
    w = lambda u: ''.join(str(s + 1) for s in G['word'][u]) or 'e'
    n=G['n']; tot=0; surv=0; stats={}
    for c in cells:
        for x in c:
            for z in c:
                if x==z or not D[z]<=D[x]: continue
                tot+=1
                if any(s in D[z] and t not in D[x] and M[s][t]==3 for s in D[x] for t in range(n)): continue
                surv+=1
                bad=[y for y in c if D[y]-D[x] and mu[y,z]<mu[y,x]]
                # classify killers: is killer adjacent to x via a star? descent comparisons
                kinds=tuple(sorted(set(('inc' if not D[x]<=D[y] else 'sup', int(mu[y,x]), int(mu[y,z])) for y in bad)))
                stats[kinds]=stats.get(kinds,0)+1
                if surv<=6: print(name,'surv x=',w(x),sorted(D[x]),'z=',w(z),sorted(D[z]),'killers',[(w(y),sorted(D[y]),int(mu[y,x]),int(mu[y,z])) for y in bad][:4])
    print(name,'pairs',tot,'survive star-kill',surv)
    for k,v in sorted(stats.items(),key=lambda a:-a[1])[:10]: print('  ',k,v)
