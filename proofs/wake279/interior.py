import sys
from coxkl import *
exec(open('twin_criterion.py').read().split("for name in")[0].split("from coxkl import *")[1])
for name in sys.argv[1].split(','):
    M=CASES[name]; G = coxeter_group(M); P, mu = kl(G); cells, D = left_cells(G, mu); n=G['n']
    nb=lambda s:[t for t in range(n) if t!=s and M[s][t]==3]
    intr=lambda A: frozenset(s for s in A if all(t in A for t in nb(s)))
    # global: over ALL x,z in W (not same cell) with L(z) sub int L(x)?  and within cells
    cnt_cell=0; ex=0
    for c in cells:
        for x in c:
            I=intr(D[x])
            for z in c:
                if z!=x and D[z] and D[z]<=D[x] and D[z]&I: ex+=1
                if z!=x and D[z] and D[z]<=I: cnt_cell+=1
    print(name,'pairs in cell with L(z) sub int L(x):',cnt_cell,' with L(z) meeting int L(x) (and sub L(x)):',ex)
    # cell-level: do two elements of a cell ever have one interior containing other's descent?
