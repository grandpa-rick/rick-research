# PROVE283 consequences: cross-reference open26 instances against (ii)-instances and (i)-elements of the S_16 census (sieve16.json)
import json,sys
sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from rskmod import rsk
T=lambda P: tuple(tuple(r) for r in P)
O=json.load(open('/home/agent/projects/proofs/prove282/open26.json'))
S=json.load(open('/home/agent/projects/proofs/wake282/sieve16.json'))
key=lambda lam,Px,Pz:(tuple(lam),T(Px),T(Pz))
okeys={key(o['lam'],o['Px'],o['Pz']):i for i,o in enumerate(O)}
hits={}
for pi,p in enumerate(S):
    for e in p['elems']:
        Py,_=rsk(e['y'])
        k=key(p['lam'],Py,p['Pz'])
        if k in okeys:
            hits.setdefault(okeys[k],[]).append(dict(pair=pi,lam=p['lam'],A=p['A'],Px=p['Px'],Pz=p['Pz'],parity_ok=p['parity_ok'],verdict=p['verdict'],kind=e['kind'],s=e.get('s'),DesPy=e['DesPy'],muyx=e['muyx'],muyz=e['muyz'],ly=e['ly'],lx=p['lx'],lz=p['lz']))
for i in range(len(O)):
    print(i,O[i]['lam'],'A=',O[i]['A'])
    for h in hits.get(i,[]): print('   ',h)
# also: is each open26 instance itself a census pair? (it should be: pfail = parity-failing census pairs)
ck={key(p['lam'],p['Px'],p['Pz']):(pi,p['verdict'],p['parity_ok']) for pi,p in enumerate(S)}
for i in (11,13,14): print('inst',i,'as census pair:',ck.get(key(O[i]['lam'],O[i]['Px'],O[i]['Pz'])))
json.dump({str(k):v for k,v in hits.items()},open('/home/agent/projects/proofs/prove283/q68xref.json','w'))
