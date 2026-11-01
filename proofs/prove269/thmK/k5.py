import sys, collections, time
exec(open('q_cominuscule_scout.py').read().split('def boolean')[0])
def run(t,n,J):
    T=time.time()
    C=Cox(cartan(t,n)); J=set(J); lam,els=quotient(C,J)
    Wj=list(els); ln=lambda a: els[a][2]; wr={m:els[m][0] for m in Wj}; wd={m:els[m][1] for m in Wj}
    LE={(a,b):C.le(wr[a],wr[b]) for a in Wj for b in Wj}
    leq=lambda a,b: LE[(a,b)]
    def act(i,a):
        c=a[i]
        if c==0: return ('stay',None)
        return ('up' if c>0 else 'down', C.refl(i,a))
    P=parKL(Wj,leq,ln,act,range(C.n),'q')
    bad=0; nd=0; tot=0
    for x in Wj:
        for y in Wj:
            if not leq(x,y): continue
            tot+=1
            iv=[z for z in Wj if leq(x,z) and leq(z,y)]
            d=not any(C.le(C.apply_word(wd[z]+[j],C.rho),wr[y]) for z in iv for j in J)
            nd+=d; bad+= d != (P[(x,y)]==(1,))
    print(t+str(n),'K=',[i for i in range(n) if i not in J],'|W^J|',len(Wj),'pairs',tot,'(d)',nd,'(b)<=>(d) fails',bad,'%.0fs'%(time.time()-T),flush=True)
for t,n in [('F',4),('B',4),('D',5),('B',5),('A',6)]:
    for k in range(n): run(t,n,[i for i in range(n) if i!=k])
run('E',6,[i for i in range(6) if i!=2])
