import sys; sys.argv=['x']
exec(open('../prove269/thmK/k2.py').read().split('tests=')[0])
def word(G,a):
    w=[]; 
    while G['ln'][a]>0:
        for i in range(G['r']):
            b=G['L'][a][i]
            if G['ln'][b]<G['ln'][a]: w.append(i); a=b; break
    return ''.join(map(str,w))
for name,gens,J in [('D4',Dgens(4),(0,2,3)),('C4',Cgens(4),(0,1,3)),('B3',Cgens(3),(0,2))]:
    G=group(gens); N=G['N']; ln=G['ln']; r=G['r']; Pf=fullKL(G)
    Wmin=[a for a in range(N) if all(ln[G['R'][a][j]]>ln[a] for j in J)]
    for s in Wmin:
        for t in Wmin:
            if s==t or not le(G,s,t): continue
            if any(le(G,G['R'][s][j],t) for j in J): continue
            DLt=[i for i in range(r) if ln[G['L'][t][i]]<ln[t]]
            DLs=[i for i in range(r) if ln[G['L'][s][i]]<ln[s]]
            if all(i in DLs for i in DLt):
                iv=[z for z in range(N) if le(G,s,z) and le(G,z,t)]
                rk=[sum(1 for z in iv if ln[z]==ln[s]+i) for i in range(ln[t]-ln[s]+1)]
                print(name,J,'x=',word(G,s),'y=',word(G,t),'DLx',DLs,'DLy',DLt,'ranks',rk,'P',Pf[(s,t)])
