"""Sieve test (Wake 282). For every candidate pair (x,z) in certs<n>_*.json (prove281 certifyn format):
list (i)-elements (star images s.x, L(sx) not<= A, mu=1) and (ii)-elements (y=(U,Q), Des U > A strictly, mu(y,x)!=0),
with Des P_y, Des>A?, is P_y an x-half of a candidate pair at (lam, Des P_y)?, its twin status, mu(y,x), mu(y,z).
Usage: python3 sieve.py n certdir violfile  -> sieve<n>.json"""
import sys,json,glob,os
sys.path.insert(0,'../prove281')
from common import *
n=int(sys.argv[1]); cdir=sys.argv[2]; V=json.load(open(sys.argv[3]))
C=[]
for f in sorted(glob.glob(os.path.join(cdir,'certs%d_*.json'%n))): C+=json.load(open(f))
key=lambda T:json.dumps(T)
verd={}; 
for c in C: verd[(tuple(c['lam']),tuple(c['A']),key(c['Px']),key(c['Pz']))]=c['verdict']
Xidx={}
for e in V:
    for X in e['X']: Xidx[(tuple(e['lam']),tuple(e['A']),key(X))]=e
def tw(lam,A,Px,Pz): return verd.get((lam,tuple(A),key(Px),key(Pz)),'not-a-pair')
def mu_of(v): return 1 if v=='mu=1' else 0 if v.startswith('kill') else None
out=[]
for c in C:
    lam=tuple(c['lam']); A=set(c['A']); x=tuple(c['x']); z=tuple(c['z'])
    par_ok=(inv(x)-inv(z))%2==0
    si=star_images(x)
    labels=[('i',s,y) for s,y in si]+[('ii','U',tuple(u['y'])) for u in c['Ucerts'] if u['verdict']=='mu=1']
    assert len(labels)==len(c['certs'])
    for (k,s,y),ce in zip(labels,c['certs']): assert tuple(ce['y'])==tuple(y)
    elems=[]
    def rec(kind,s,y,muyx,muyz):
        Py=rsk(list(y))[0]; D=sorted(L(list(y)))
        e=Xidx.get((lam,tuple(D),key(Py)))
        cand=e is not None
        twins=[(Z,tw(lam,D,Py,Z)) for Z in e['Z']] if cand else []
        return dict(kind=kind,s=s,y=list(y),DesPy=D,sup=set(D)>A,cand_x=cand,
                    pair_with_same_Pz=tw(lam,D,Py,c['Pz']) if cand else None,
                    any_twin_at_DesPy=any(t=='TWIN' for _,t in twins) if cand else None,
                    muyx=muyx,muyz=muyz,ly=inv(y))
    for (k,s,y),ce in zip(labels,c['certs']):
        elems.append(rec(k,s,y,1,mu_of(ce['verdict'])))
    # (ii)-candidates with mu(y,x)=0 are recorded separately (not (ii)-elements)
    zero=[rec('Des>A,mu(y,x)=0','U',tuple(u['y']),mu_of(u['verdict']),None) for u in c['Ucerts'] if u['verdict']!='mu=1']
    out.append(dict(lam=list(lam),A=sorted(A),Px=c['Px'],Pz=c['Pz'],lx=inv(x),lz=inv(z),parity_ok=par_ok,verdict=c['verdict'],elems=elems,zero=zero))
for r in out:
    for e in r['elems']+r['zero']: e['sup']=bool(e['sup'])
json.dump(out,open('sieve%d.json'%n,'w'),indent=0)
print('pairs',len(out),'twins',sum(r['verdict']=='TWIN' for r in out))
