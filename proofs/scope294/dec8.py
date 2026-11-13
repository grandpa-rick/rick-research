import pickle
from collections import defaultdict, Counter
from itertools import permutations
from q76t_s7 import rsk
from klfast import inv
from cox import pols, parse
W=list(permutations(range(1,9)))
good,Ptab=pickle.load(open('good8.pkl','rb')); vals,=pickle.load(open('sep8.pkl','rb'))
byP=defaultdict(list)
for w in W: byP[rsk(w)[0]].append(w)
def dec(w): return tuple(k for k in range(1,len(w)) if set(w[:k])==set(range(1,k+1)))
def deg(p): return sum(p)  # P(1)
for k in vals:
    if vals[k]=={(1,)}: continue
    ci,P1=k; c=W[ci]; K=byP[Ptab[P1]]
    prs=[(X,tuple(c[v-1] for v in X)) for X in K]; r=[parse(s) for s in pols(8,prs)]
    tab=Counter((p,bool(dec(X)), dec(c)!=(), bool(dec(Y))) for (X,Y),p in zip(prs,r))
    tag="VIOL" if len(vals[k])>1 else "const"
    print(tag,''.join(map(str,c)),"l(c)",inv(c),dict(tab))
