import sys,time
from fastcap import ranks
for L in map(int,sys.argv[1:]):
    t=time.time(); s=('01'*20)[:L]; r=ranks(s); print(L,s,'rank=',r,'sum',sum(r),'t',round(time.time()-t),flush=True)
