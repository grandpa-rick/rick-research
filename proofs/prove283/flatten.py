import sys,json
sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from ydec import decide, Ld, Rd, std, endpoint
from cfg import inv,bru
B=json.load(open('qbest.json'))
def flat(w,fixed): return std([w[i] for i in range(len(w)) if i not in fixed])
if __name__=='__main__':
    r=B[13]; x,z=r['x'],r['z']; fixed=[2,7,8,11,12]
    xf,zf=flat(x,fixed),flat(z,fixed)
    print('xf',xf,inv(xf),'zf',zf,inv(zf),'gap',inv(zf)-inv(xf),'bru',bru(xf,zf))
    print('L',sorted(Ld(xf)),sorted(Ld(zf)),'R',sorted(Rd(xf)),sorted(Rd(zf)))
    print('endpoint',endpoint(xf,zf)); tr=[]; print('decide',decide(xf,zf,trace=tr),tr[:5])
