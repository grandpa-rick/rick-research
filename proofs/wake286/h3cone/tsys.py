import json, sympy as sp, itertools
cells=json.load(open('cells5.json'))
E=sp.eye(5)
def conj_ok(A,T):
    Ti=T.inv(); Bs=[Ti*a*T for a in A]
    return all(x>=0 for B in Bs for x in B), Bs
# all T = I - sum_{(x,z) in P} E[x,z] (column z gets -c_x), P a set of off-diagonal pairs, up to size 3
for ci in range(len(cells)):
    A=[sp.Matrix(a) for a in cells[ci]['A']]
    pairs=[(x,z) for x in range(5) for z in range(5) if x!=z]
    hits=[]
    for k in (1,2,3):
        for P in itertools.combinations(pairs,k):
            T=sp.eye(5)
            for (x,z) in P: T[x,z]-=1
            if T.det()==0: continue
            ok,_=conj_ok(A,T)
            if ok: hits.append(P)
    # keep minimal
    mins=[P for P in hits if not any(set(Q)<set(P) for Q in hits)]
    print(ci,cells[ci]['cell'][0],'D',cells[ci]['D'],'minimal 0/1 twin systems (x,z):',mins)
A=[sp.Matrix(a) for a in cells[3]['A']]
T=sp.eye(5); T[0,4]=-1; T[1,3]=-1
ok,Bs=conj_ok(A,T); print('T=',T.tolist(),'ok',ok)
for s,B in enumerate(Bs): print(' T^-1(1+s%d)T='%(s+1),B.tolist())
