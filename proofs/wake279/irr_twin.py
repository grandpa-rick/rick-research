import sys
from coxkl import *
from bn_family import commutant_dim
exec(open('twin_criterion.py').read().split("for name in")[0].split("from coxkl import *")[1])
for name in sys.argv[1].split(','):
    M=CASES[name]; G=coxeter_group(M); P,mu=kl(G); cells,D=left_cells(G,mu)
    w=lambda u: ''.join(str(s+1) for s in G['word'][u]) or 'e'
    stats={}
    for c in cells:
        cd=commutant_dim(cell_module(G,mu,D,c,conv='C'))
        tw=any(x!=z and D[z]<=D[x] and all(mu[y,z]>=mu[y,x] for y in c if D[y]-D[x]) for x in c for z in c)
        k=(len(c),cd==1,tw); stats[k]=stats.get(k,0)+1
    print(name,'(dim, irreducible, has twin): count'); 
    for k in sorted(stats): print('  ',k,stats[k])
