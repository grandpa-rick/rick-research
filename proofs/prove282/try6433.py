import sys,json,random
sys.path.insert(0,'.')
from ydec import *
from rskmod import rsk
from count_int import syt
random.seed(1)
S=json.load(open('../wake282/sieve16.json'))
for r in S:
    for e in r['elems']:
        if e['kind']=='ii' and e['muyz'] is None:
            Py=[list(R) for R in rsk(e['y'])[0]]; Pz=r['Pz']; lam=r['lam']
            cells=syt(lam); random.shuffle(cells); res=None; tried=0
            for Q in cells[:3000]:
                tried+=1; Q=[list(R) for R in Q]
                y=rsk_inv(Py,Q); z=rsk_inv(Pz,Q); tr=[]
                v=decide(y,z,trace=tr)
                if v is not None: res=(v,tr); break
            print(lam,r['verdict'],'tried',tried,'result',res,flush=True)
