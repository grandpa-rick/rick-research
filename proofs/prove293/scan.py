import itertools
from eng import A_rw,B_rw
def rank2(A,B):
    ks=set(A)|set(B)
    for k in ks:
        for l in ks:
            if A.get(k,0)*B.get(l,0)-A.get(l,0)*B.get(k,0)!=0: return 2
    return 1 if (A or B) else 0
def pred(s):
    alt=all(s[i]!=s[i+1] for i in range(len(s)-1))
    return 1 if len(set(s))==1 or (alt and len(s)%2==0) else 2
for L in range(2,15):
    bad=[s for s in map(''.join,itertools.product('ru',repeat=L)) if rank2(A_rw(s),B_rw(s))!=pred(s)]
    print(L,len(bad),bad[:4])
