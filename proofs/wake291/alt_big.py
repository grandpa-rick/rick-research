import sys,time
from cap_rank import analyse
for L in map(int,sys.argv[1:]):
    t=time.time(); s=('01'*10)[:L]; b,r,_=analyse(s); print(L,s,'b=',b,'rank=',r,'sum',sum(r),'t',round(time.time()-t),flush=True)
