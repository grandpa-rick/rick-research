# stuck pairs: (d)-pairs x<y with D_L(y) subset D_L(x)
import sys; sys.argv=['x']
exec(open('q55.py').read().split('for m in range(1,6):')[0])
def Agens(n):
    g=[]
    for i in range(n):
        S=np.eye(n+1); S[[i,i+1]]=S[[i+1,i]]; g.append(S)
    return g
def Dgens(n):
    g=[]
    for i in range(n-1):
        S=np.eye(n); S[[i,i+1]]=S[[i+1,i]]; g.append(S)
    S=np.eye(n); S[n-2,n-2]=0;S[n-1,n-1]=0;S[n-2,n-1]=-1;S[n-1,n-2]=-1; g.append(S)
    return g
tests=[('A3',Agens(3)),('B3',Cgens(3)),('D4',Dgens(4)),('A4',Agens(4)),('C4',Cgens(4))]
for name,gens in tests:
    G=group(gens); N=G['N']; ln=G['ln']; r=G['r']
    L=G['L'] if 'L' in G else None
    for k in range(r+1):
        for J in itertools.combinations(range(r),k):
            Wmin=[a for a in range(N) if all(ln[G['R'][a][j]]>ln[a] for j in J)]
            nd=0; st=[]
            for s in Wmin:
                for t in Wmin:
                    if s==t or not le(G,s,t): continue
                    if any(le(G,G['R'][s][j],t) for j in J): continue
                    nd+=1
                    DLt=[i for i in range(r) if ln[G['L'][t][i]]<ln[t]]
                    if all(ln[G['L'][s][i]]<ln[s] for i in DLt): st.append((s,t))
            print(name,"J=",J,"(d)pairs x<y",nd,"stuck",len(st))
