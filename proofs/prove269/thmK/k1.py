# For every J: pairs s<=t in W^J with [s,t]_W subset W^J and P_{s,t} != 1. Report by J.
import sys; sys.argv=['x']
exec(open('q55.py').read().split('for m in range(1,6):')[0])
def Agens(n):
    g=[]
    for i in range(n):
        S=np.eye(n+1); S[[i,i+1]]=S[[i+1,i]]; g.append(S)
    return g
tests=[('A3',Agens(3)),('B3',Cgens(3)),('A4',Agens(4)),('C4',Cgens(4))]
for name,gens in tests:
    G=group(gens); N=G['N']; ln=G['ln']; r=G['r']; Pf=fullKL(G)
    for k in range(r+1):
        for J in itertools.combinations(range(r),k):
            Wmin=[a for a in range(N) if all(ln[G['R'][a][j]]>ln[a] for j in J)]
            Wset=set(Wmin); good=0; bad=[]
            for s in Wmin:
                for t in Wmin:
                    if not le(G,s,t): continue
                    if any(le(G,G['R'][s][j],t) for j in J): continue
                    good+=1
                    if Pf[(s,t)]!=(1,): bad.append((s,t,Pf[(s,t)]))
            print(name,"J=",J,"K=",[i for i in range(r) if i not in J],"pairs(d)",good,"P!=1:",len(bad), bad[:2])
