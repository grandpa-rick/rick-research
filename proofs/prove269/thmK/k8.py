import sys, collections, time
exec(open('q_cominuscule_scout.py').read().split('def boolean')[0])
def run(t,n,J):
    T=time.time(); C=Cox(cartan(t,n)); J=set(J); lam,els=quotient(C,J)
    L=list(els); N=len(L); ix={m:i for i,m in enumerate(L)}
    wr=[els[m][0] for m in L]; wd=[els[m][1] for m in L]; ln=[els[m][2] for m in L]
    upb=[0]*N
    for a in range(N):
        b=0
        for c in range(N):
            if ln[c]>=ln[a] and C.le(wr[a],wr[c]): b|=1<<c
        upb[a]=b
    le=lambda a,b: (upb[a]>>b)&1
    zt=[[C.apply_word(wd[z]+[j],C.rho) for j in J] for z in range(N)]
    lsh=lambda i,a: ix[C.refl(i,L[a])] if L[a][i]!=0 else None
    out=collections.Counter()
    for y in range(N):
        badz=0
        for z in range(N):
            if any(C.le(w,wr[y]) for w in zt[z]): badz|=1<<z
        DLy=[i for i in range(n) if wr[y][i]<0]
        for x in range(N):
            if not le(x,y) or ln[y]-ln[x]<3: continue
            ivs=0; m=upb[x]
            while m:
                lb=m&-m; z=lb.bit_length()-1; m^=lb
                if le(z,y): ivs|=lb
            if ivs & badz: continue
            if not all(wr[x][i]<0 for i in DLy): continue
            if not all(le(x,lsh(i,y)) for i in DLy): continue
            Ns=[]
            for s in DLy:
                v=lsh(s,y)
                Ns.append(sum(1 for z in range(N) if le(x,z) and le(z,v) and ln[z]==ln[v]-1 and wr[z][s]<0))
            rk=tuple(sum(1 for z in range(N) if (ivs>>z)&1 and ln[z]==ln[x]+i) for i in range(ln[y]-ln[x]+1))
            out[(ln[y]-ln[x],tuple(Ns),rk,len(DLy))]+=1
    print(t+str(n),J,dict(out),'%.0fs'%(time.time()-T))
run('E',6,[0,1,2,4,5])
