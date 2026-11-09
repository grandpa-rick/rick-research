import sys
sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from wg_twins import parse
cells=parse('/home/agent/projects/proofs/wake285/wgraphs/B3_wg.txt')
# correct convention: line y lists x iff L(y) not<= L(x), mu(y,x)!=0
tw=[];
for ci,c in enumerate(cells):
    for x,(Dx,Ex) in enumerate(c):
        for z,(Dz,Ez) in enumerate(c):
            if z==x or not Dz<=Dx: continue
            ys=[y for y,(Dy,Ey) in enumerate(c) if not Dy<=Dx]
            if all(c[y][1].get(z,0)>=c[y][1].get(x,0) for y in ys): tw.append((ci,x,z,sorted(Dx),sorted(Dz)))
            # emulate F2 witness kill (incomparable descents, mu(y,x)!=0)
            W=[y for y in ys if not Dx<=c[y][0] and c[y][1].get(x,0)]
            killed=any(c[y][1].get(z,0)==0 for y in W)
            if killed and tw and tw[-1][:3]==(ci,x,z): print('CONTROL FAIL: F2-kill fired on twin',ci,x,z)
print('B3 twins (correct convention):',len(tw)); [print(' ',t) for t in tw]
