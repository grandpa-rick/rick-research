from q442_check import *
grid=[(1,l,n) for l in (0,1) for n in range(2,8)]+[(2,l,n) for l in (0,1) for n in range(2,6)]+[(3,0,n) for n in range(2,4)]
nc=defaultdict(lambda:[0,0])
for (k,l,n) in grid:
    w=2*l+2
    Ainf=chains(k,n,w,E(k),False); A=chains(k,n,w,E(k),True)
    # NC1: M -> k (l=-1 exponent law), hypothesis ell>=0 broken
    c0=coeff_t(G(k,l,n,shiftM=-1),0); nc['NC1 M=k: c0!=Ainf'][0]+= (c0!=Ainf); nc['NC1 M=k: c0!=Ainf'][1]+=1
    # NC2: sign flip in (1)
    c0=coeff_t(G(k,l,n,sign=+1),0); nc['NC2 sign+: c0!=Ainf'][0]+= (c0!=Ainf); nc['NC2 sign+: c0!=Ainf'][1]+=1
    # NC3: bounded A instead of A^inf, only meaningful when n>w
    if n>w: nc['NC3 bounded A != c0 (n>w)'][0]+=(coeff_t(G(k,l,n),0)!=A); nc['NC3 bounded A != c0 (n>w)'][1]+=1
    # Thm 6
    Y0=coeff_t(G(k,l,n),0)
    Ew=lambda lam,k=k,w=w: E(k)(lam) and lam[0]-lam[-1]<=w
    O=lambda lam,k=k,w=w: E(k)(lam) and lam[0]-lam[-1]>w
    K0=add(chains(k,n,w,Ew,False),chains(k,n,w,Bcl(k,w),False),-1)
    rhs=add(chains(k,n,w,O,False),chains(k,n,w,Bcl(k,w),False))
    nc['Thm6 eq(8)'][0]+=(add(Y0,K0,-1)==rhs); nc['Thm6 eq(8)'][1]+=1
    nc['Thm6 Y0=K0 <=> n<w'][0]+=((Y0==K0)==(n<w)); nc['Thm6 Y0=K0 <=> n<w'][1]+=1
for c,v in nc.items(): print(c,f"{v[0]}/{v[1]}")
# Thm 14(2): n* law
for (k,w,nmax) in [(1,2,8),(1,4,11),(2,2,5),(2,4,6),(3,2,4)]:
    ns=None
    for n in range(1,nmax+1):
        if chains(k,n,w,E(k),False)!=chains(k,n,w,E(k),True): ns=n;break
    law= 2*(w+1) if k==1 else w+1
    print('n*',(k,w),ns,'law',law,ns==law)
