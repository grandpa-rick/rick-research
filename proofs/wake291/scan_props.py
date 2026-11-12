import itertools, sys, time
from cap_rank import analyse
L=int(sys.argv[1]); t=time.time()
res={}
for s in (''.join(x) for x in itertools.product('01',repeat=L)):
    b,r,_=analyse(s); res[s]=r
uni=all(all(r[i]<=r[i+1] for i in range(len(r)//2)) for r in res.values())
comp=lambda s:''.join('1' if c=='0' else '0' for c in s)
symrev=all(res[s]==res[s[::-1]] for s in res); symcomp=all(res[s]==res[comp(s)] for s in res)
gen12=[s for s,r in res.items() if r[1]==1 and max(r)>0]
print('L',L,'unimodal',uni,'rev-inv',symrev,'comp-inv',symcomp,'distinct rank seqs',len({tuple(r) for r in res.values()}),'time',round(time.time()-t))
for r in sorted({tuple(r) for r in res.values()}): print(r, sum(r), [s for s in res if tuple(res[s])==r][:4])
