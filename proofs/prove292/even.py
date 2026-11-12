import sys; sys.argv=['x','0']
exec(open('ident.py').read().split("K=int")[0])
import sympy
K=6; N=2*K+1
W,Th=series(N); WT=smul(W,Th,N)
pw=[{0:{():1}}]  # (WT)^o as series
P=[{} for _ in range(N+1)]; P[0]={():1}; pws=[P]
for o in range(1,N+2): pws.append(smul(WT,pws[-1],N))
bad=tot=0
for k in range(0,K+1):
    d=2*k+1; Rs=R(tuple([2]*k+[1]))
    # generating identity
    g={kk:(-1)**k*v for kk,v in pws[1][d].items()}
    g={a:b for a,b in g.items() if b}
    assert g==Rs,(k,g,Rs)
    ranks=[]
    for i in range(d+1):
        imgs=[]
        for al in comps(i):
            lhs=Mperp(al,Rs) if i>0 else Rs
            if i>0:
                o=sum(1 for x in al if x%2); l=len(al)
                if al[-1]%2==0: rhs={}
                else:
                    rhs={}
                    add(rhs,pws[o+1][d-i],(-1)**(k+l)); add(rhs,pws[o-1][d-i],(-1)**(k+l-1))
                    rhs={a:b for a,b in rhs.items() if b}
                tot+=1; bad+= lhs!=rhs
            imgs.append(lhs)
        keys=sorted({kk for im in imgs for kk in im})
        ranks.append(sympy.Matrix(len(imgs),len(keys),lambda a,b: imgs[a].get(keys[b],0)).rank() if keys else 0)
    pred=[1 if i in (0,d) else min((i+1)//2,(d-i+1)//2) for i in range(d+1)]
    print("L",2*k,ranks,ranks==pred)
print("even identity checks",tot,"bad",bad)
