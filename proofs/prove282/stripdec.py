import json,sys
sys.path.insert(0,'.')
from skew import strips
from corner import evac
from rskmod import rsk
def eject_seq(T,S):
    T=[list(R) for R in T]; out=[]
    for r in S:
        a=T[r].pop()
        for rr in range(r-1,-1,-1):
            row=T[rr]; j=max(j for j,b in enumerate(row) if b<a); row[j],a=a,row[j]
        out.append(a)
    return out,[R for R in T if R]
def std(seq):
    s=sorted(seq); r={v:i+1 for i,v in enumerate(s)}; return [r[v] for v in seq]
R=json.load(open('rest16.json'))
for c in R:
    if c['res'] is not None: continue
    lam=c['lam']; best=None; eqs=0
    for tag,(Ty,Tz) in (('',(c['Py'],c['Pz'])),('e',(evac(c['Py']),evac(c['Pz'])))):
        for m in range(1,int(sys.argv[1])+1):
            for S in strips(lam,m):
                ey,Ry=eject_seq(Ty,S); ez,Rz=eject_seq(Tz,S)
                if sorted(ey)!=sorted(ez): continue
                eqs+=1
                sy=std(list(reversed(ey))); sz=std(list(reversed(ez)))
                if sy!=sz and Ry!=Rz: best=('KILL',tag,m,S); break
            if best: break
        if best: break
    print(lam,c['A'],c['kind'],'equal-ejection strips',eqs,'->',best,flush=True)
