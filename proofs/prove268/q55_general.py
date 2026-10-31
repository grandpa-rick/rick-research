# General-Coxeter checks for Q55 lemmas, every J, every sigma<=tau in W^J:
#  (G1) dn(tau, sigma W_J)=sigma  <=>  [sigma,tau]_W subset W^J
#  (G2) C={u in W_J: sigma u<=tau} = sigma*[e,u0]   (u0: dn = sigma u0)
#  (G3) P^{J,q}_{sigma,tau}(0) := sum_{u in W_J}(-1)^l(u) P_{sigma u,tau}(0) = [dn=sigma]
#  (G4) dn=sigma => P^{J,q}_{sigma,tau} = P_{sigma,tau}
import sys; sys.argv=['x']
exec(open('q55.py').read().split('for m in range(1,6):')[0])
def Agens(n):
    g=[]
    for i in range(n):
        S=np.eye(n+1); S[[i,i+1]]=S[[i+1,i]]; g.append(S)
    return g
def H3():
    # reuse check.py's generator if present
    return None
tests=[('A3',Agens(3)),('B3',Cgens(3)),('C4',Cgens(4)),('A4',Agens(4))]
for name,gens in tests:
    G=group(gens); N=G['N']; ln=G['ln']; r=G['r']; Pf=fullKL(G)
    mulR=lambda a,u: G['idx'][G['key'](G['els'][a]@G['els'][u])]
    b=[0]*4; tot=0; ctl=0
    for k in range(r+1):
        for J in itertools.combinations(range(r),k):
            WJel=sorted(coset(G,0,list(J)))
            Wmin=[a for a in range(N) if all(ln[G['R'][a][j]]>ln[a] for j in J)]
            Wset=set(Wmin)
            for s in Wmin:
                for t in Wmin:
                    if not le(G,s,t): continue
                    tot+=1
                    C=[u for u in WJel if le(G,mulR(s,u),t)]
                    u0=max(C,key=lambda u:ln[u]); dnis=(u0==0)
                    assert all(le(G,mulR(s,u),mulR(s,u0)) for u in C)
                    full=[x for x in range(N) if le(G,s,x) and le(G,x,t)]
                    b[0]+= dnis != all(x in Wset for x in full)
                    b[1]+= set(C)!={u for u in WJel if le(G,u,u0)}
                    alt=()
                    for u in WJel: alt=padd(alt,psc(Pf.get((mulR(s,u),t),()),0,(-1)**ln[u]))
                    c0=alt[0] if alt else 0
                    b[2]+= c0!=int(dnis)
                    if dnis: b[3]+= alt!=Pf[(s,t)]
                    ctl+= (c0!=0) != (len(full)==2**(ln[t]-ln[s]))   # control: "full interval Boolean"
    print(name,"triples",tot,"fails G1..G4",b,"| control (Boolean full W interval) disagreements",ctl)
