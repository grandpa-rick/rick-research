import json,sys
sys.path.insert(0,'.')
import tdec
from tdec import dec_tab
from rskmod import rsk
S=json.load(open('../wake282/sieve16.json')); out=[]
for r in S:
    if r['verdict']!='UNDECIDED': continue
    for e in r['elems']:
        if e['muyz'] is None:
            Py=[list(R) for R in rsk(e['y'])[0]]
            tdec.memo.clear()
            res=dec_tab(Py,r['Pz'],budget=int(sys.argv[1]))
            print(r['lam'],r['A'],e['kind'],e['s'],'->',None if res is None else (res[0],[t[:3] for t in res[1]]),flush=True)
            out.append(dict(lam=r['lam'],A=r['A'],Px=r['Px'],Pz=r['Pz'],kind=e['kind'],s=e['s'],y=e['y'],Py=Py,res=res))
json.dump(out,open('rest16.json','w'),default=list)
