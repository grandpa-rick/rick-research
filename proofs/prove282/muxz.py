"""Decide mu(x,z) for every candidate pair (x,z) in cached certs (n=15,16). Computed tool."""
import sys,json,glob,os; sys.path.insert(0,'/home/agent/projects/proofs/prove281')
os.chdir('/home/agent/projects/proofs/prove281')
from common import *
from orbit2 import search12 as search2
def ln(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
files=sys.argv[1:]
for f in files:
    for c in json.load(open(f)):
        x,z=c['x'],c['z']; g=(ln(z)-ln(x))
        if g%2==0: st='parity-even'; p=None
        else: st,p,_,_=search2(x,z)
        print(json.dumps(dict(f=os.path.basename(f),lam=c['lam'],A=c['A'],Pz=c['Pz'],gap=g,verdict=c['verdict'],muxz=st,path=p)),flush=True)
