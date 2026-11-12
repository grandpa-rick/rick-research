import itertools,sys,time
from fastcap import ranks
def is_alt(s): return all(s[i]!=s[i+1] for i in range(len(s)-1))
for L in range(2,int(sys.argv[1])+1):
    t=time.time(); bad=[]; cnt={}
    for s in (''.join(x) for x in itertools.product('01',repeat=L)):
        r2=ranks(s,[2])[0]; cnt[r2]=cnt.get(r2,0)+1
        pred = 1 if (len(set(s))==1 or (is_alt(s) and L%2==0)) else 2
        if r2!=pred: bad.append((s,r2))
    print('L',L,'r2 counts',cnt,'P1b violations',len(bad),bad[:5],'t',round(time.time()-t),flush=True)
