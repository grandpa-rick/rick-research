# re-run S7 KL via crownU_sep internals and list radius-0 separating classes (shape,L,R each, d, cell relation)
import sys; sys.argv=['x','7','0']
exec(open('crownU_sep.py').read().split('# arc candidates')[0])
arcs=[(u,w,m) for (u,w),m in mu.items() if L[w]-L[u]>=3 and Ldes(w)<=Ldes(u) and Rdes(w)<=Rdes(u) and (Ldes(w),Rdes(w))!=(Ldes(u),Rdes(u))]
def rel(u,w): return (RS[u][0]==RS[w][0], RS[u][1]==RS[w][1], shape[u]==shape[w])
c0=lambda w:(shape[w],tuple(sorted(Ldes(w))),tuple(sorted(Rdes(w))))
G=collections.defaultdict(list)
for u,w,m in arcs: G[(c0(u),c0(w),L[w]-L[u],rel(u,w))].append((u,w,m,P[(u,w)]))
bad=sorted([(k,g) for k,g in G.items() if len(set(t[2] for t in g))>1],key=lambda kg:(kg[0][2],L[kg[1][0][1]]))
out=[]
for k,g in bad:
    print(k); 
    for t in g: print('   ',''.join(map(str,t[0])),''.join(map(str,t[1])),'mu',t[2],'P',t[3],'l',L[t[0]],L[t[1]])
    out.append({'key':repr(k),'pairs':[[''.join(map(str,t[0])),''.join(map(str,t[1])),t[2],list(t[3])] for t in g]})
json.dump(out,open('r0_separators_S7.json','w'),indent=1)
