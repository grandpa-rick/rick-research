exec(open('a13_caseB.py').read().split('\nn=14')[0])
n=14
PX=[[1,2,6,10],[3,7,11,14],[4,8,12],[5,9,13]]; PZ=[[1,2,3,7],[4,5,6,11],[8,9,10],[12,13,14]]
t=syts((4,4,3,3))[0]; Q=[[k+1 for k in range(n) if t[k]==r] for r in range(4)]
x=rsk_inv(PX,Q); z=rsk_inv(PZ,Q); Lx=L(x); Lz=L(z)
print('L(x)',sorted(Lx),'L(z)',sorted(Lz),'l',inv(x),inv(z))
for s in sorted(Lx):
    for tt in (s-1,s+1):
        if 1<=tt<=n-1 and tt not in Lx:
            xp=[y for y in (lmul(s,x),lmul(tt,x)) if len(L(y)&{s,tt})==1][0]
            miss=Lz-L(xp)
            print((s,tt),'L(x\')',sorted(L(xp)),'L(z)\\L(x\')',sorted(miss),'P(x\')',rsk(xp)[0], ' x\'=rz?',[lmul(r,z)==xp for r in miss])
