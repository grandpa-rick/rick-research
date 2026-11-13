import pickle
from collections import defaultdict
from itertools import permutations
from q76t_s7 import rsk
from klfast import inv
from cox import pols, parse
W=list(permutations(range(1,9)))
good,Ptab=pickle.load(open('good8.pkl','rb')); vals,=pickle.load(open('sep8.pkl','rb'))
byP=defaultdict(list)
for w in W: byP[rsk(w)[0]].append(w)
def ldes(w):
    pos={a:k for k,a in enumerate(w)}; return [i for i in range(1,len(w)) if pos[i+1]<pos[i]]
def rdes(w): return [i for i in range(1,len(w)) if w[i-1]>w[i]]
viol=[k for k in vals if len(vals[k])>1]
for (ci,P1) in viol[:3]:
    c=W[ci]; K=byP[Ptab[P1]]
    prs=[(X,tuple(c[v-1] for v in X)) for X in K]
    r=[parse(s) for s in pols(8,prs)]
    print("c=",''.join(map(str,c)),"P1",Ptab[P1],"P2",rsk(prs[0][1])[0])
    for (X,Y),p in sorted(zip(prs,r),key=lambda t:t[1]):
        print("   Q=",rsk(X)[1],''.join(map(str,X)),''.join(map(str,Y)),p,"rdes",rdes(X))
