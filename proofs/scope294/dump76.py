import sys
from collections import defaultdict
from klfast import full_kl_fast, unpack
from q76t_s7 import rsk
def mul(a,b): return tuple(a[b[i]-1] for i in range(len(a)))  # (ab)(i)=a(b(i))
def invp(a):
    r=[0]*len(a)
    for i,v in enumerate(a): r[v-1]=i+1
    return tuple(r)
n=int(sys.argv[1])
W,idx,ln,P=full_kl_fast(n)
R=[rsk(w) for w in W]
byQ=defaultdict(dict)
for k,(pt,qt) in enumerate(R): byQ[qt][pt]=k
grp=defaultdict(dict); allQ=defaultdict(set); lens=defaultdict(set)
for Q,d in byQ.items():
    it=list(d.items())
    for P1,x in it:
        for P2,y in it:
            key=(P1,P2); allQ[key].add(Q)
            p=P[y].get(x)
            if p is not None: grp[key][Q]=(x,y,unpack(p)); lens[key].add(ln[y]-ln[x])
full=[k for k in grp if len(grp[k])==len(allQ[k]) and len(lens[k])==1]
print("const-len all-Q keys",len(full))
from collections import Counter
print("len diffs", Counter(next(iter(lens[k])) for k in full))
print("shapes", Counter(tuple(map(len,k[0])) for k in full))
for k in full:
    vals=set(v[2] for v in grp[k].values())
    if vals!={(1,)}:
        print("KEY",k, "ldiff",lens[k],"P",vals)
        for Q,(x,y,p) in grp[k].items():
            X=W[x];Y=W[y]
            print("   ",''.join(map(str,X)),''.join(map(str,Y)),"x^-1y=",''.join(map(str,mul(invp(X),Y))),"yx^-1=",''.join(map(str,mul(Y,invp(X)))))
# global check: is yx^-1 constant on every const-len all-Q key? is ldiff = l(c)?
from klfast import inv
bad=0; badl=0
for k in full:
    cs=set(); 
    for Q,(x,y,p) in grp[k].items(): cs.add(mul(W[y],invp(W[x])))
    if len(cs)>1: bad+=1
    c=next(iter(cs))
    if inv(c)!=next(iter(lens[k])): badl+=1
print("keys with nonconstant c:",bad," keys with ldiff != l(c):",badl)
