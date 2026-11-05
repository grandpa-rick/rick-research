from hecke_qc import *
# split failures by whether std-values at positions j,j+1 are consecutive (=> ides changes under swap)
for fam in ('P0','P2','P3'):
    c=defaultdict(int)
    for n in range(2,5):
        for k in range(2,6):
            for w in itertools.product(range(1,n+1),repeat=k):
                s=std(w)
                for j in range(k-1):
                    P=FAM[fam](j); cons=abs(s[j]-s[j+1])==1
                    for i in range(1,n):
                        L=fq(i); ok=apply(P,L(w))==apply(L,P(w))
                        c[(cons,ok)]+=1
    print(fam,dict(c))
