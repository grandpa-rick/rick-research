exec(open('a13_caseB.py').read().split('\nn=14')[0])
n=14
cases={(4,4,3,3):([[1,2,6,10],[3,7,11,14],[4,8,12],[5,9,13]],[[1,2,3,7],[4,5,6,11],[8,9,10],[12,13,14]])}
for lam,(PX,PZ) in cases.items():
    best=[]
    for t in syts(lam):
        Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
        x=rsk_inv(PX,Q); z=rsk_inv(PZ,Q); best.append((max(inv(x),inv(z)),inv(x),inv(z),Q,x,z))
    best.sort(key=lambda a:a[0])
    for b in best[:3]: print(b)
